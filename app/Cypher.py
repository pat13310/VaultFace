import os
import logging
import functools
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, serialization, hmac
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import DES, DES3, Blowfish

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CypherError(Exception):
    """Classe de base pour les exceptions de Cypher"""
    pass


class KeyNotGeneratedError(CypherError):
    """Levée quand une clé n'a pas été générée"""
    pass


class UnsupportedAlgorithmError(CypherError):
    """Levée quand un algorithme non supporté est utilisé"""
    pass


class EncryptionError(CypherError):
    """Levée quand une erreur survient pendant le chiffrement"""
    pass


class DecryptionError(CypherError):
    """Levée quand une erreur survient pendant le déchiffrement"""
    pass


def key_required(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.key:
            raise KeyNotGeneratedError(f"Clé non générée pour {func.__name__}")
        return func(self, *args, **kwargs)

    return wrapper


class Cypher:
    def __init__(self):
        logger.info("Initialisation de la classe Cypher")
        self._key = None
        self._iv = None
        self._nonce = None
        self._public_key = None
        self._private_key = None

        self._cipher_instances = {}

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if value == "":
            self._key = None
        else:
            if not isinstance(value, bytes):
                raise ValueError("La clé doit être de type bytes")
            self._key = value

    @property
    def iv(self):
        return self._iv

    @iv.setter
    def iv(self, value):
        if value == "":
            self._key = None
        else:
            if not isinstance(value, bytes):
                raise ValueError("L'IV doit être de type bytes")
            self._iv = value

    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, value):
        if value == "":
            self._key = None
        else:
            if not isinstance(value, bytes):
                raise ValueError("Le nonce doit être de type bytes")
            self._nonce = value

    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        if value == "":
            self._key = None
        else:
            if not isinstance(value, rsa.RSAPublicKey):
                raise ValueError("La clé publique doit être de type RSAPublicKey")
            self._public_key = value

    @property
    def private_key(self):
        return self._private_key

    @private_key.setter
    def private_key(self, value):
        if value == "":
            self._key = None
        else:
            if not isinstance(value, rsa.RSAPrivateKey):
                raise ValueError("La clé privée doit être de type RSAPrivateKey")
            self._private_key = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.clear_sensitive_data()

    def encrypt(self, plaintext, algorithm='aes'):
        logger.info(f"Chiffrement avec l'algorithme {algorithm}")
        if algorithm.lower() == '3des':
            algorithm = 'des3'  # Redirection vers des3
        try:
            if algorithm not in ['aes', 'des', 'des3', 'chacha20', 'blowfish', 'rsa']:
                raise UnsupportedAlgorithmError(f"Algorithme non supporté : {algorithm}")

            getattr(self, f'generate_{algorithm}_key')()
            ciphertext = getattr(self, f'{algorithm}_encrypt')(plaintext)

            if algorithm == 'rsa':
                return ciphertext, {
                    'public_key': self.export_public_key().decode('utf-8'),
                    'private_key': self.export_private_key().decode('utf-8')
                }
            elif algorithm == 'chacha20':
                return ciphertext, {'key': self.key.hex(), 'nonce': self.nonce.hex()}
            else:
                return ciphertext, {'key': self.key.hex(), 'iv': self.iv.hex()}

        except CypherError:
            raise
        except Exception as e:
            raise EncryptionError(f"Erreur lors du chiffrement : {str(e)}")

    def generate_aes_key(self, key_size=256, iterations=100000):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=key_size // 8,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        self.key = kdf.derive(os.urandom(32))
        self.iv = os.urandom(16)

    def generate_des_key(self):
        self.key = os.urandom(8)
        self.iv = os.urandom(8)

    def generate_des3_key(self):
        self.key = DES3.adjust_key_parity(os.urandom(24))
        self.iv = os.urandom(8)

    def generate_chacha20_key(self):
        self.key = os.urandom(32)
        self.nonce = os.urandom(16)

    def generate_blowfish_key(self):
        self.key = os.urandom(16)
        self.iv = os.urandom(8)

    def generate_rsa_key(self, key_size=2048):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    @key_required
    def aes_encrypt(self, plaintext, mode='CBC'):
        modes_map = {
            'CBC': modes.CBC(self.iv),
            'CFB': modes.CFB(self.iv),
            'OFB': modes.OFB(self.iv),
            'CTR': modes.CTR(self.iv),
        }
        cipher = Cipher(algorithms.AES(self.key), modes_map[mode], backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = self._pad(plaintext.encode(), algorithms.AES.block_size)
        return encryptor.update(padded_data) + encryptor.finalize()

    @key_required
    def des_encrypt(self, plaintext):
        cipher = DES.new(self.key, DES.MODE_CBC, self.iv)
        padded_data = self._pad(plaintext.encode(), DES.block_size)
        return cipher.encrypt(padded_data)

    @key_required
    def des3_encrypt(self, plaintext):
        cipher = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        padded_data = self._pad(plaintext.encode(), DES3.block_size)
        return cipher.encrypt(padded_data)

    @key_required
    def chacha20_encrypt(self, plaintext):
        cipher = self._get_cipher_instance('chacha20')
        encryptor = cipher.encryptor()
        return encryptor.update(plaintext.encode())

    @key_required
    def blowfish_encrypt(self, plaintext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, self.iv)
        padded_data = self._pad(plaintext.encode(), Blowfish.block_size)
        return cipher.encrypt(padded_data)

    def rsa_encrypt(self, plaintext):
        if not self.public_key:
            raise KeyNotGeneratedError("Clé publique RSA non générée.")
        return self.public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def _get_cipher_instance(self, algorithm):
        if algorithm not in self._cipher_instances:
            if algorithm == 'aes':
                self._cipher_instances[algorithm] = Cipher(algorithms.AES(self.key), modes.CBC(self.iv),
                                                           backend=default_backend())
            elif algorithm == 'chacha20':
                self._cipher_instances[algorithm] = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None,
                                                           backend=default_backend())
        return self._cipher_instances[algorithm]

    def _pad(self, data, block_size):
        padding_len = block_size - len(data) % block_size
        padding = bytes([padding_len] * padding_len)
        return data + padding

    def _unpad(self, padded_data):
        padding_len = padded_data[-1]
        return padded_data[:-padding_len]

    def decrypt(self, ciphertext, algorithm):
        logger.info(f"Déchiffrement avec l'algorithme {algorithm}")
        if algorithm.lower() == '3des':
            algorithm = 'des3'  # Redirection vers des3
        try:
            if algorithm not in ['aes', 'des', 'des3', 'chacha20', 'blowfish', 'rsa']:
                raise UnsupportedAlgorithmError(f"Algorithme non supporté : {algorithm}")
            return getattr(self, f'{algorithm}_decrypt')(ciphertext)
        except CypherError:
            raise
        except Exception as e:
            raise DecryptionError(f"Erreur lors du déchiffrement : {str(e)}")

    @key_required
    def aes_decrypt(self, ciphertext):
        cipher = self._get_cipher_instance('aes')
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return self._unpad(decrypted_data).decode()

    @key_required
    def des_decrypt(self, ciphertext):
        cipher = DES.new(self.key, DES.MODE_CBC, self.iv)
        decrypted_data = cipher.decrypt(ciphertext)
        return self._unpad(decrypted_data).decode()

    @key_required
    def des3_decrypt(self, ciphertext):
        cipher = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decrypted_data = cipher.decrypt(ciphertext)
        return self._unpad(decrypted_data).decode()

    @key_required
    def chacha20_decrypt(self, ciphertext):
        cipher = self._get_cipher_instance('chacha20')
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext).decode()

    @key_required
    def blowfish_decrypt(self, ciphertext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, self.iv)
        decrypted_data = cipher.decrypt(ciphertext)
        return self._unpad(decrypted_data).decode()

    def rsa_decrypt(self, ciphertext):
        if not self.private_key:
            raise KeyNotGeneratedError("Clé privée RSA non générée.")
        return self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    def export_public_key(self):
        if not self.public_key:
            raise KeyNotGeneratedError("Clé publique RSA non générée.")
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def export_private_key(self):
        if not self.private_key:
            raise KeyNotGeneratedError("Clé privée RSA non générée.")
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

    def clear_sensitive_data(self):
        self._key = None
        self._iv = None
        self._nonce = None
        import gc
        gc.collect()


def test_algorithm(cypher, algorithm, plaintext):
    print(f"\nTests {algorithm.upper()}...")
    try:
        encrypted, keys = cypher.encrypt(plaintext, algorithm=algorithm)
        decrypted = cypher.decrypt(encrypted, algorithm=algorithm)
        assert decrypted == plaintext, f"{algorithm.upper()} échec du test"
        print(f"{algorithm.upper()} test réussi: {decrypted}\nClefs: {keys}")
    except Exception as e:
        print(f"Erreur lors du test {algorithm.upper()} : {str(e)}")


def run_all_tests():
    with Cypher() as cypher:
        algorithms = ['aes', 'des', 'des3', 'chacha20', 'blowfish', 'rsa']
        for algorithm in algorithms:
            test_algorithm(cypher, algorithm, f"Message secret {algorithm.upper()}")


if __name__ == "__main__":
    run_all_tests()
