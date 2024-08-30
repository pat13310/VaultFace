from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from hashlib import sha256
import os

# Importation de `pycryptodome` pour DES et 3DES
from Crypto.Cipher import DES, DES3


class Cypher:
    def __init__(self):
        self.key = None
        self.iv = None
        self.nonce = None
        self.public_key = None
        self.private_key = None

    def encrypt_value(self, value, algorithm='aes'):
        if algorithm == 'aes':
            return self.aes_encrypt(value)
        elif algorithm == 'des':
            return self.des_encrypt(value)
        elif algorithm == '3des':
            return self.des3_encrypt(value)
        elif algorithm == 'chacha20':
            return self.chacha20_encrypt(value)
        elif algorithm == 'rsa':
            return self.rsa_encrypt(value)
        else:
            raise ValueError("Algorithme de chiffrement non supporté")

    def decrypt_value(self, encrypted_value, algorithm='aes'):
        if algorithm == 'aes':
            return self.aes_decrypt(bytes.fromhex(encrypted_value))
        elif algorithm == 'des':
            return self.des_decrypt(bytes.fromhex(encrypted_value))
        elif algorithm == '3des':
            return self.des3_decrypt(bytes.fromhex(encrypted_value))
        elif algorithm == 'chacha20':
            return self.chacha20_decrypt(bytes.fromhex(encrypted_value))
        elif algorithm == 'rsa':
            return self.rsa_decrypt(bytes.fromhex(encrypted_value))
        else:
            raise ValueError("Algorithme de déchiffrement non supporté")

    # Chiffrement symétrique AES
    def generate_aes_key(self, key_size=256):
        self.key = os.urandom(key_size // 8)
        self.iv = os.urandom(16)

    def aes_encrypt(self, plaintext):
        if not self.key or not self.iv:
            raise ValueError("Clé AES ou IV non généré.")
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = self._pad(plaintext.encode(), algorithms.AES.block_size)
        return encryptor.update(padded_data) + encryptor.finalize()

    def aes_decrypt(self, ciphertext):
        if not self.key or not self.iv:
            raise ValueError("Clé AES ou IV non généré.")
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return self._unpad(decrypted_data).decode()

    # Chiffrement symétrique DES
    def generate_des_key(self):
        self.key = os.urandom(8)  # Clé de 64 bits pour DES
        self.iv = os.urandom(8)   # IV de 64 bits pour DES

    def des_encrypt(self, plaintext):
        if not self.key or not self.iv:
            raise ValueError("Clé DES ou IV non généré.")
        cipher = DES.new(self.key, DES.MODE_CBC, self.iv)
        padded_data = self._pad(plaintext.encode(), DES.block_size)
        return cipher.encrypt(padded_data)

    def des_decrypt(self, ciphertext):
        if not self.key or not self.iv:
            raise ValueError("Clé DES ou IV non généré.")
        cipher = DES.new(self.key, DES.MODE_CBC, self.iv)
        decrypted_data = cipher.decrypt(ciphertext)
        return self._unpad(decrypted_data).decode()

    # Chiffrement symétrique 3DES (Triple DES)
    def generate_3des_key(self):
        self.key = DES3.adjust_key_parity(os.urandom(24))  # Clé de 192 bits pour 3DES
        self.iv = os.urandom(8)   # IV de 64 bits pour 3DES

    def des3_encrypt(self, plaintext):
        if not self.key or not self.iv:
            raise ValueError("Clé 3DES ou IV non généré.")
        cipher = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        padded_data = self._pad(plaintext.encode(), DES3.block_size)
        return cipher.encrypt(padded_data)

    def des3_decrypt(self, ciphertext):
        if not self.key or not self.iv:
            raise ValueError("Clé 3DES ou IV non généré.")
        cipher = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decrypted_data = cipher.decrypt(ciphertext)
        return self._unpad(decrypted_data).decode()

    # Chiffrement symétrique ChaCha20
    # Chiffrement symétrique ChaCha20
    def generate_chacha20_key(self):
        self.key = os.urandom(32)  # Clé de 256 bits pour ChaCha20
        self.nonce = os.urandom(16)  # Nonce de 128 bits pour ChaCha20

    def chacha20_encrypt(self, plaintext):
        if not self.key or not self.nonce:
            raise ValueError("Clé ChaCha20 ou nonce non généré.")
        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None, backend=default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(plaintext.encode())

    def chacha20_decrypt(self, ciphertext):
        if not self.key or not self.nonce:
            raise ValueError("Clé ChaCha20 ou nonce non généré.")
        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None, backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext).decode()
    # Chiffrement asymétrique RSA
    def generate_rsa_keys(self, key_size=2048):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def rsa_encrypt(self, plaintext):
        if not self.public_key:
            raise ValueError("Clé publique RSA non générée.")
        ciphertext = self.public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def rsa_decrypt(self, ciphertext):
        if not self.private_key:
            raise ValueError("Clé privée RSA non générée.")
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode()

    # Hachage SHA-256
    def sha256_hash(self, data):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(data.encode())
        return digest.finalize().hex()

    # Dérivation de clé par mot de passe avec PBKDF2
    def derive_key_from_password(self, password, salt=None, iterations=100000, length=32):
        if salt is None:
            salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=length,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        self.key = kdf.derive(password.encode())
        return self.key, salt

    # Fonctions de padding et unpadding
    def _pad(self, data, block_size):
        padding_len = block_size - len(data) % block_size
        padding = bytes([padding_len] * padding_len)
        return data + padding

    def _unpad(self, padded_data):
        padding_len = padded_data[-1]
        return padded_data[:-padding_len]


# Exemple d'utilisation de la classe Cypher
if __name__ == "__main__":
    # Initialisation de la classe
    cypher = Cypher()

    # AES Chiffrement/Déchiffrement
    cypher.generate_aes_key()
    ciphertext_aes = cypher.aes_encrypt("Message secret AES")
    print(f"Message AES chiffré: {ciphertext_aes.hex()}")
    plaintext_aes = cypher.aes_decrypt(ciphertext_aes)
    print(f"Message AES déchiffré: {plaintext_aes}")

    # DES Chiffrement/Déchiffrement
    cypher.generate_des_key()
    ciphertext_des = cypher.des_encrypt("Message secret DES")
    print(f"Message DES chiffré: {ciphertext_des.hex()}")
    plaintext_des = cypher.des_decrypt(ciphertext_des)
    print(f"Message DES déchiffré: {plaintext_des}")

    # 3DES Chiffrement/Déchiffrement
    cypher.generate_3des_key()
    ciphertext_3des = cypher.des3_encrypt("Message secret 3DES")
    print(f"Message 3DES chiffré: {ciphertext_3des.hex()}")
    plaintext_3des = cypher.des3_decrypt(ciphertext_3des)
    print(f"Message 3DES déchiffré: {plaintext_3des}")

    # ChaCha20 Chiffrement/Déchiffrement
    cypher.generate_chacha20_key()
    ciphertext_chacha20 = cypher.chacha20_encrypt("Message secret ChaCha20")
    print(f"Message ChaCha20 chiffré: {ciphertext_chacha20.hex()}")
    plaintext_chacha20 = cypher.chacha20_decrypt(ciphertext_chacha20)
    print(f"Message ChaCha20 déchiffré: {plaintext_chacha20}")

    # RSA Chiffrement/Déchiffrement
    cypher.generate_rsa_keys()
    ciphertext_rsa = cypher.rsa_encrypt("Message secret RSA")
    print(f"Message RSA chiffré: {ciphertext_rsa.hex()}")
    plaintext_rsa = cypher.rsa_decrypt(ciphertext_rsa)
    print(f"Message RSA déchiffré: {plaintext_rsa}")

    # Hachage SHA-256
    hash_result = cypher.sha256_hash("Message à hacher")
    print(f"Hash SHA-256: {hash_result}")

    # Dérivation de clé à partir d'un mot de passe
    derived_key, salt = cypher.derive_key_from_password("motdepasse")
    print(f"Clé dérivée: {derived_key.hex()} avec le sel: {salt.hex()}")
