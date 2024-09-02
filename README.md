# Vault Face

**Vault Face** est un utilitaire conçu pour offrir un stockage sécurisé de données sensibles en les protégeant contre tout accès non autorisé ou toute exposition indésirable. Dans le contexte actuel où la sécurité des données est primordiale, Vault Face garantit que les informations confidentielles (comme les mots de passe, les numéros de carte bancaire, les informations personnelles ou professionnelles) ne sont jamais stockées sous une forme lisible, mais plutôt chiffrées selon des standards de sécurité éprouvés.

## Principes Clés de Vault Face

### Chiffrement des Données Sensibles

Vault Face repose sur le principe que les données sensibles ne doivent jamais être stockées en texte clair, même sur des supports de stockage considérés comme sécurisés. L'utilitaire utilise des algorithmes de chiffrement robustes pour transformer ces données en un format illisible sans la clé de déchiffrement appropriée. Cela garantit que même en cas de compromission du fichier de données, les informations demeurent protégées.

### Stockage Sécurisé

Les données chiffrées sont stockées dans un fichier local ou sur un support de stockage choisi par l'utilisateur, comme un disque dur, un serveur distant, ou un espace de stockage dans le cloud. Vault Face s'assure que ces fichiers ne contiennent aucune information qui puisse être utilisée directement sans un déchiffrement autorisé.

### Accès Sécurisé et Contrôlé

Vault Face intègre un mécanisme d'authentification permettant de contrôler l'accès aux données sensibles. Seules les personnes disposant de la clé appropriée ou des droits d'accès spécifiques peuvent déchiffrer et lire les données stockées. Cela empêche les accès non autorisés et protège les informations même en cas de perte ou de vol de l'appareil de stockage.

### Flexibilité dans le Choix de l'Algorithme de Chiffrement

Vault Face offre plusieurs options d'algorithmes de chiffrement, adaptés à différents besoins de sécurité :

- **AES (Advanced Encryption Standard)** : Standard de chiffrement symétrique largement adopté pour sa robustesse et sa rapidité.
- **RSA (Rivest-Shamir-Adleman)** : Algorithme de chiffrement asymétrique, particulièrement utile pour le chiffrement de données et l'échange sécurisé de clés.
- **ChaCha20** : Algorithme de chiffrement moderne, rapide et sécurisé, particulièrement efficace sur les appareils mobiles.

Cette flexibilité permet aux utilisateurs de choisir l'algorithme qui convient le mieux à leur contexte et à leurs besoins spécifiques en matière de performance et de sécurité.

### Facilité d'Utilisation et Accessibilité

Vault Face est conçu pour être simple à utiliser, même pour ceux qui n'ont pas une expertise technique en sécurité informatique. Grâce à une interface conviviale, les utilisateurs peuvent facilement ajouter, lire, ou supprimer des données sensibles en quelques clics ou commandes. Cela en fait une solution idéale pour les particuliers, les petites entreprises, et même les grandes organisations qui souhaitent une gestion sécurisée de leurs informations sensibles.

### Protection contre les Attaques et le Piratage

En chiffrant les données sensibles et en les rendant illisibles sans déchiffrement autorisé, Vault Face réduit considérablement le risque de piratage. Même si un attaquant parvient à accéder aux fichiers de données, il ne pourra pas exploiter les informations sans la clé de déchiffrement. En outre, les algorithmes de chiffrement proposés sont éprouvés contre diverses formes d'attaques, y compris les attaques par force brute.

### Sécurité Adaptative et Mise à Jour Continue

Vault Face est conçu pour être adaptatif aux nouvelles menaces de sécurité. Les algorithmes de chiffrement peuvent être mis à jour ou remplacés par de nouvelles technologies de chiffrement plus robustes au fur et à mesure qu'elles deviennent disponibles. Cette capacité d'évolution garantit que Vault Face reste une solution de stockage sécurisé pertinente face à l'évolution constante des techniques de piratage et des menaces.

## Cas d'Utilisation de Vault Face

- **Stockage de Mots de Passe** : Permet de conserver en toute sécurité des mots de passe pour des comptes en ligne, des accès système ou des applications, sans risque de fuite ou de compromission.
- **Sauvegarde de Documents Sensibles** : Stocke des fichiers critiques tels que des contrats, des informations financières, des données médicales, ou des documents légaux de manière sécurisée.
- **Gestion de Clés de Cryptographie** : Conserve des clés de chiffrement privées ou d'autres informations de sécurité de manière sûre et contrôlée.
- **Protection des Informations Personnelles** : Garantit que les données personnelles (comme les numéros de carte d'identité, les numéros de sécurité sociale, ou les coordonnées bancaires) ne sont jamais exposées directement.



### Tableau Résumé des chiffrements et clés dans la Classe `Cypher`
Voici un tableau récapitulatif de la classe `Cypher`, indiquant les différents algorithmes de chiffrement pris en charge ainsi que les clés associées nécessaires pour chaque type de chiffrement.

| **Algorithme**  | **Type de Clé**             | **Longueur de la Clé** | **Paramètres Associés**        | **Description**                                                                                     |
|-----------------|-----------------------------|-------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------|
| **AES**         | Clé symétrique (`self.key`) | 128, 192, 256 bits      | IV (`self.iv`), 16 octets      | Chiffrement symétrique utilisant AES en mode CBC. Utilise une clé symétrique et un vecteur d'initialisation. |
| **DES**         | Clé symétrique (`self.key`) | 56 bits (7 octets)      | IV (`self.iv`), 8 octets       | Chiffrement symétrique utilisant DES en mode CBC. Utilise une clé de 56 bits et un IV de 64 bits.            |
| **3DES (Triple DES)** | Clé symétrique (`self.key`) | 112 ou 168 bits        | IV (`self.iv`), 8 octets       | Version améliorée de DES, effectue trois passes de chiffrement. Utilise une clé symétrique de 112 ou 168 bits.|
| **ChaCha20**    | Clé symétrique (`self.key`) | 256 bits (32 octets)    | Nonce (`self.nonce`), 16 octets | Chiffrement symétrique utilisant ChaCha20. Utilise une clé symétrique de 256 bits et un nonce de 128 bits.   |
| **RSA**         | Clé asymétrique (`self.public_key` et `self.private_key`) | Variable (2048, 4096 bits typiquement) | Aucun                        | Chiffrement asymétrique utilisant RSA. Utilise une clé publique pour le chiffrement et une clé privée pour le déchiffrement. |
| **Blowfish**    | Clé symétrique (`self.key`) | Variable (32 à 448 bits) | Aucun                         | Chiffrement symétrique utilisant Blowfish. La longueur de la clé peut varier entre 32 et 448 bits.            |

### Détails sur Chaque Algorithme

1. **AES (Advanced Encryption Standard)**
   - Utilise une clé symétrique pour chiffrer et déchiffrer les données.
   - Nécessite un vecteur d'initialisation (IV) de 16 octets.
   - Convient pour des opérations de chiffrement rapide et sécurisé sur de grands volumes de données.

2. **DES (Data Encryption Standard)**
   - Utilise une clé symétrique de 56 bits.
   - Désuet et moins sécurisé que les autres algorithmes; principalement pour la compatibilité historique.
   - Nécessite un vecteur d'initialisation (IV) de 8 octets.

3. **3DES (Triple DES)**
   - Amélioration du DES classique par application du chiffrement trois fois.
   - Utilise une clé de 112 ou 168 bits et un IV de 8 octets.
   - Plus sécurisé que DES mais plus lent comparé à AES.

4. **ChaCha20**
   - Utilise une clé symétrique de 256 bits et un nonce de 16 octets.
   - Conçu pour offrir une sécurité élevée et des performances rapides, même sur des matériels ne supportant pas AES matériellement.
   - Adapté pour les applications nécessitant un chiffrement rapide, comme les communications en temps réel.

5. **RSA (Rivest-Shamir-Adleman)**
   - Utilise une paire de clés asymétriques (publique et privée).
   - La clé publique chiffre les données; seule la clé privée correspondante peut les déchiffrer.
   - Idéal pour le chiffrement de petites quantités de données, comme les clés de session pour les algorithmes symétriques.

6. **Blowfish**
   - Utilise une clé symétrique dont la longueur peut varier entre 32 et 448 bits.
   - Un des premiers algorithmes de chiffrement rapide destiné à remplacer DES.
   - Convient pour les applications nécessitant une flexibilité dans la taille de clé.


## Conclusion

Vault Face est une solution de stockage sécurisé innovante et fiable, adaptée à tous ceux qui cherchent à protéger leurs données sensibles de manière proactive. En combinant des algorithmes de chiffrement de pointe avec une interface simple d'utilisation et un accès sécurisé, Vault Face offre une défense efficace contre les menaces de sécurité modernes, tout en restant facile à utiliser pour une large audience.