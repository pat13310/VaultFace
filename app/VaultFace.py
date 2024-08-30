import json
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QApplication, QMessageBox, QDialog, QTableWidgetItem, \
    QAbstractItemView, QHeaderView
from cryptography.fernet import Fernet

from app.Cypher import Cypher
from app.InfoDlg import InfoDlg
from app.MessageDlg import MessageDlg
from ui.Ui_VaultFace import \
    Ui_VaultFace


class VaultFace(QMainWindow, Ui_VaultFace):
    def __init__(self):
        super(VaultFace, self).__init__()
        self.setupUi(self)
        self.treeWidget.setStyleSheet("""
                   QTreeWidget::item:hover
                    {
                        background-color: #2D2D2D;  /* Couleur de fond pour le survol */
                        color:  white;  /* Couleur du texte pour le survol */
                    } 
                   QTreeWidget::item:selected {
                       background-color: #fcd33b;  /* Couleur de fond pour la sélection */
                       color: #000000;  /* Couleur du texte pour la sélection */
                   }                                       
            """)
        ## dossier caché
        self.create_hidden_directory()
        # Générer ou charger la clé de chiffrement
        self.key_file = os.path.join(self.hidden_dir, "key.key")
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)

        self.CACHE_FILE = "vault_tree.json"
        self.treeWidget.setIconSize(QSize(31, 31))
        self.vault_icon = QIcon("icons/vault.svg")
        self.folder_icon = QIcon("icons/folder.svg")
        self.data_icon = QIcon("icons/data.svg")

        self.setup_connection()
        self.vault_item = QTreeWidgetItem(["Coffre-fort", "", "root"])
        self.treeWidget.addTopLevelItem(self.vault_item)
        self.vault_item.setIcon(0, self.vault_icon)  # Appliquer l'icône à la première colonne (nom)
        self.vault_item.setData(0, Qt.UserRole, "root")
        self.msg_box = MessageDlg()
        self.info_box = InfoDlg()
        # Instance de la classe Cypher
        self.cypher = Cypher()
        self.load_tree_cache()
        self.treeWidget.expandAll()
        self.btn_add_data.setVisible(False)
        self.listView.setIconSize(QSize(48, 48))  # Ajustez la taille de l'icône selon vos besoins
        self.listView.setSpacing(16)  # Augmente l'espacement entre les éléments de la liste
        self.current_folder = None
        self.current_data = None

        self.init_table()

    def load_or_generate_key(self):
        # Charger la clé de chiffrement ou en générer une nouvelle
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            return key

    def setup_connection(self):
        # Connexions
        self.btn_add_vault.clicked.connect(self.go_vault)
        self.btn_add_data.clicked.connect(self.go_data)
        self.treeWidget.itemClicked.connect(self.on_tree_item_clicked)
        self.treeWidget.currentItemChanged.connect(self.on_tree_item_clicked)
        self.btn_save_folder.clicked.connect(self.addVault)
        self.btn_modify.clicked.connect(self.addData)
        self.btn_delete.clicked.connect(self.delete_current_item)
        self.btn_delete_folder.clicked.connect(self.delete_current_item)
        self.listView.doubleClicked.connect(self.on_listview_double_clicked)
        self.tableDatas.cellDoubleClicked.connect(self.on_table_cell_double_clicked)

    def init_table(self):
        self.tableDatas.setColumnCount(3)
        self.tableDatas.setHorizontalHeaderLabels(["Nom", "Valeur", "Encodage"])
        self.tableDatas.verticalHeader().setVisible(False)
        self.tableDatas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDatas.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableDatas.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableDatas.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.tableDatas.setColumnWidth(2, 100)
        self.tableDatas.itemChanged.connect(self.update_tree_item_from_table)

        self.tableDatas.setStyleSheet("""
                        QTableView {
                            background-color: #333;
                            color: white;
                            gridline-color: #444;
                            font-size: 14px;
                        }
                        QTableView::item:selected {
                            background-color: #fcd33b;  /* Couleur de fond pour la sélection (vert clair) */
                            color: black;  /* Couleur du texte pour la sélection */
                        }
                        QHeaderView::section {
                            background-color: #444;
                            color: white;
                            padding: 4px;
                            font-size: 14px;
                            border: 1px solid #333;
                        }
                        QTableCornerButton::section {
                            background-color: #444;
                            border: 1px solid #333;
                        }
                    """)

    def go_vault(self):
        self.stackedWidget.setCurrentWidget(self.page_folder)

    def go_data(self):
        self.stackedWidget.setCurrentWidget(self.page_data)

    def addVault(self):
        # Récupérer les données du formulaire
        nom = self.edit_folder.text()  # Le champ de texte pour le nom

        encodage = self.select_cyfer.currentText()  # Le champ de sélection pour l'encodage
        valeur = self.edit_value.text()  # Le champ de texte pour la valeur

        if nom == "":
            self.info_box.setMessage("Nom absent !")
            self.info_box.showModal()

        elif nom != "":
            # Créer un nouvel élément pour le QTreeWidget
            folder_item = QTreeWidgetItem([nom, encodage, valeur])
            folder_item.setIcon(0, QIcon(self.folder_icon))
            folder_item.setData(0, Qt.UserRole, "folder")
            self.vault_item.addChild(folder_item)
            self.edit_folder.clear()
            self.save_tree_cache()
        else:
            self.info_box.setMessage("Valeur absente !")
            self.info_box.showModal()

    def addData(self):
        # Récupérer les données du formulaire
        nom = self.edit_name.text()  # Le champ de texte pour le nom
        encodage = self.select_cyfer.currentText()  # Le champ de sélection pour l'encodage
        valeur = self.edit_value.text()  # Le champ de texte pour la valeur

        if nom == "":
            self.info_box.setMessage("Nom absent !")
            self.info_box.showModal()

        elif nom != "":

            # item = self.findItem(nom, self.current_folder)
            item = self.current_data

            if item is None:
                # Créer un nouvel élément pour le QTreeWidget
                folder_item = QTreeWidgetItem([nom, valeur, encodage])
                icon = self.data_icon
                folder_item.setIcon(0, icon)  # Appliquer l'icône à la première colonne (nom)
                folder_item.setData(0, Qt.UserRole, "data")

                if self.current_folder is not None:
                    self.current_folder.addChild(folder_item)
                    self.edit_name.clear()
                    self.select_cyfer.setCurrentIndex(0)  # Réinitialiser à la première option
                    self.edit_value.clear()
                    self.save_tree_cache()
                    self.populate_table_with_folder_data(self.current_folder)
                    self.stackedWidget.setCurrentWidget(self.page_datas)
            else:  # on modifie
                item.setText(0, nom)
                item.setText(1, valeur)
                item.setText(2, encodage)
                self.save_tree_cache()
                self.populate_table_with_folder_data(self.current_folder)
                self.stackedWidget.setCurrentWidget(self.page_datas)

        else:
            self.info_box.setMessage("Valeur absente !")
            self.info_box.showModal()

    def decryptVault(self):
        selected_item = self.treeWidget.currentItem()
        if selected_item is not None:
            nom = selected_item.text(0)
            encodage = selected_item.text(1)
            valeur_chiffree = selected_item.text(2)

            try:
                decrypted_value = self.cypher.decrypt_value(valeur_chiffree, algorithm=encodage.lower())
                selected_item.setText(2, decrypted_value)
                self.info_box.setMessage(f"Le texte a été déchiffré avec {encodage}.")
                self.info_box.showModal()
            except ValueError as e:
                self.info_box.setMessage(f"Erreur de déchiffrement: {str(e)}")
                self.info_box.showModal()
        else:
            self.info_box.setMessage("Aucun élément sélectionné pour la décryptage.")
            self.info_box.showModal()

    def save_tree_cache(self):
        def serialize_item(item):
            # Récupérer les données de chaque élément
            children = []
            for i in range(item.childCount()):
                child = item.child(i)
                children.append(serialize_item(child))

            # Récupérer les propriétés de l'élément
            return {
                "nom": item.text(0),  # Nom de l'élément
                "encodage": item.text(2),  # Type d'encodage (colonne 2)
                "valeur": item.text(1),  # Valeur de l'élément (colonne 1)
                "type": item.data(0, Qt.UserRole),  # Type de l'élément (folder, data, etc.)
                "children": children  # Liste des enfants de l'élément
            }

        tree_data = serialize_item(self.vault_item)
        try:
            with open(self.CACHE_FILE, "w") as f:
                json.dump(tree_data, f, indent=4)
                print(f"Cache sauvegardé avec succès dans {self.CACHE_FILE}")  # Débogage
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier JSON: {e}")  # Débogage

    def load_tree_cache(self):
        def deserialize_item(data):
            # Créer un QTreeWidgetItem avec le texte de l'élément
            item = QTreeWidgetItem([data.get("nom", ""), data.get("valeur", ""), data.get("encodage", "")])
            item_type = data.get("type", "folder")
            item.setData(0, Qt.UserRole, item_type)

            # Appliquer les propriétés en fonction du type
            if item_type == "folder":
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                item.setIcon(0, self.folder_icon)
            elif item_type == "data":
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                item.setIcon(0, self.data_icon)
            else:
                item.setIcon(0, self.vault_icon)

            # Désérialiser les enfants
            for child_data in data.get("children", []):
                child_item = deserialize_item(child_data)
                child_item.setFlags(child_item.flags() | Qt.ItemIsEditable)
                item.addChild(child_item)

            return item

        try:
            with open(self.CACHE_FILE, "r") as f:
                tree_data = json.load(f)
                self.vault_item = deserialize_item(tree_data)
                self.treeWidget.clear()
                self.treeWidget.addTopLevelItem(self.vault_item)
                self.vault_item.setIcon(0, self.vault_icon)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erreur de chargement du fichier JSON: {e}")  # Débogage

    def on_listview_double_clicked(self, index):
        """
        Méthode appelée lorsque l'utilisateur double-clique sur un élément dans la QListView.
        Affiche la liste des données du dossier sélectionné.
        """
        # Récupérer le modèle de l'élément double-cliqué
        model = self.listView.model()
        item_text = model.data(index)  # Obtenir le texte de l'élément double-cliqué

        # Trouver l'élément correspondant dans le QTreeWidget
        folder_item = None
        for i in range(self.vault_item.childCount()):
            child_item = self.vault_item.child(i)
            if child_item.text(0) == item_text:  # Comparer le nom du dossier
                folder_item = child_item
                break

        # Si le dossier est trouvé, passer à la page des données du dossier
        if folder_item:
            self.current_folder = folder_item  # Définir le dossier courant
            self.populate_table_with_folder_data(folder_item)  # Remplir la table avec les données du dossier
            self.stackedWidget.setCurrentWidget(self.page_datas)  # Passer à la page des données

    def on_tree_item_clicked(self, item):
        """
             Méthode pour gérer le clic sur un élément du treeWidget.
             """
        self.edit_name.clear()
        self.edit_parent.clear()
        self.edit_value.clear()
        self.current_data = None
        self.current_folder = None
        item_type = item.data(0, Qt.UserRole)  # Récupérer le type de l'élément ('folder' ou autre)
        item_text = item.text(0)

        if item_type == "folder":
            self.current_folder = item
            self.btn_add_data.setVisible(True)
            self.edit_parent.setText(item_text)
            self.current_folder = self.treeWidget.currentItem()
            self.populate_table_with_folder_data(self.current_folder)
            self.stackedWidget.setCurrentWidget(self.page_datas)  # Affiche la page de dossier

        elif item_type == "data":
            parent_item = item.parent()
            self.current_folder = parent_item
            self.edit_name.setText(item_text)
            self.edit_parent.setText(self.current_folder.text(0))
            self.edit_value.setText(item.data(1, Qt.DisplayRole))
            self.select_cyfer.setCurrentText(item.data(2, Qt.DisplayRole))
            # self.select_cyfer.setCurrentIndex(item.data(1,Qt.DisplayRole))
            self.stackedWidget.setCurrentWidget(self.page_data)  # Affiche la page de dossier
            self.current_data = item
        else:
            self.btn_add_data.setVisible(False)
            self.populate_list_view()
            self.stackedWidget.setCurrentWidget(self.page_folders)  # Affiche la page de données

    def populate_table_with_folder_data(self, folder_item):
        """
        Remplit la table tableDatas avec les données des enfants du dossier sélectionné.
        """
        # Effacer toutes les données existantes dans la table
        self.tableDatas.clearContents()
        self.tableDatas.setRowCount(0)

        # Parcourir les enfants du dossier sélectionné
        for i in range(folder_item.childCount()):
            child_item = folder_item.child(i)

            if child_item.data(0, Qt.UserRole) == "data":
                # Récupérer les données de chaque enfant (data)
                nom = child_item.text(0)  # Nom de la donnée
                encodage = child_item.text(2)  # Type d'encodage
                valeur = child_item.text(1)  # Valeur de la donnée

                # Ajouter une nouvelle ligne à la table
                row_position = self.tableDatas.rowCount()
                self.tableDatas.insertRow(row_position)

                # Créer des éléments de table pour chaque colonne
                item_nom = QTableWidgetItem(nom)
                item_encodage = QTableWidgetItem(encodage)
                item_valeur = QTableWidgetItem(valeur)

                # Centrer le texte de la colonne encodage
                item_encodage.setTextAlignment(Qt.AlignCenter)
                item_encodage.setFlags(item_encodage.flags() & ~Qt.ItemIsEditable)

                # Ajouter les éléments à la table dans l'ordre correct
                self.tableDatas.setItem(row_position, 0, item_nom)  # Colonne Nom
                self.tableDatas.setItem(row_position, 1, item_valeur)  # Colonne Valeur
                self.tableDatas.setItem(row_position, 2, item_encodage)  # Colonne Encodage

    def populate_list_view(self):
        """
        Remplit la QListView avec tous les dossiers sous 'Coffre-fort'.
        """
        model = self.listView.model()  # Récupère le modèle de la QListView
        if not model:  # Crée un modèle s'il n'existe pas
            model = QStandardItemModel()
            self.listView.setModel(model)

        # Effacer tous les éléments existants dans le modèle
        model.clear()

        # Parcourir les enfants du coffre-fort pour les ajouter à la QListView
        for i in range(self.vault_item.childCount()):
            child_item = self.vault_item.child(i)
            if child_item.data(0, Qt.UserRole) == "folder":
                item = QStandardItem(child_item.text(0))  # Créer un élément de liste avec le nom du dossier
                item.setIcon(self.folder_icon)
                model.appendRow(item)

    def update_tree_item_from_table(self, item):
        """
        Met à jour l'élément correspondant dans le QTreeWidget lorsque les données sont modifiées dans la table.
        """
        # Trouver l'élément parent dans le QTreeWidget (le dossier sélectionné)
        if self.current_folder is None:
            return

        # Trouver l'élément correspondant dans le QTreeWidget
        row = item.row()
        child_item = self.current_folder.child(row)  # Récupérer l'élément enfant à la même position

        # Mettre à jour les données de l'élément enfant
        if item.column() == 0:  # Nom
            child_item.setText(0, item.text())
        elif item.column() == 1:  # Encodage
            child_item.setText(1, item.text())
        elif item.column() == 2:  # Valeur
            child_item.setText(2, item.text())
        # Sauvegarder les modifications dans le cache
        self.save_tree_cache()

    def findItem(self, nom, item):
        existing_item = None
        if item is not None:
            for i in range(item.childCount()):
                child_item = item.child(i)
                if child_item.text(0) == nom:  # Comparer le texte de la première colonne
                    existing_item = child_item
                    break
        return existing_item

    def keyPressEvent(self, event):
        """
        Méthode pour détecter les touches de clavier.
        """
        if event.key() == Qt.Key_F2:
            self.rename_current_item()
        elif event.key() == Qt.Key_Delete:
            self.delete_current_item()

    def rename_current_item(self):
        """
        Mettre l'élément courant en mode édition pour le renommer.
        """
        current_item = self.treeWidget.currentItem()
        if current_item:
            self.treeWidget.editItem(current_item, 0)  # Active le mode édition pour la première colonne
        else:
            print("Aucun élément sélectionné pour le renommage.")

    def delete_current_item(self):
        """
        Supprimer l'élément courant du QTreeWidget après confirmation, sauf si c'est le répertoire racine.
        """
        current_item = self.treeWidget.currentItem()
        if current_item and current_item != self.vault_item:  # Vérifie que l'élément n'est pas le répertoire racine
            self.msg_box.setMessage(f"Êtes-vous sûr de vouloir supprimer '{current_item.text(0)}'?")
            reply = self.msg_box.showModal()

            if reply == QDialog.Accepted:
                parent_item = current_item.parent()
                if parent_item:
                    parent_item.removeChild(current_item)  # Supprimer l'élément du parent
                else:
                    index = self.treeWidget.indexOfTopLevelItem(current_item)
                    if index != -1:
                        self.treeWidget.takeTopLevelItem(index)  # Supprimer l'élément de niveau supérieur
                print("Élément supprimé.")
            else:
                print("Suppression annulée.")
        else:
            print("Impossible de supprimer le répertoire racine ou aucun élément sélectionné.")

    def on_table_cell_double_clicked(self, row, column):
        """
        Méthode appelée lorsque l'utilisateur double-clique sur une cellule de la table.
        Si la colonne est 'Encodage', affiche le formulaire avec les données correspondantes.
        """
        if column == 2:  # Vérifie si la colonne double-cliquée est 'Encodage'
            # Récupère les données de la ligne correspondante
            nom = self.tableDatas.item(row, 0).text()
            valeur = self.tableDatas.item(row, 1).text()
            encodage = self.tableDatas.item(row, 2).text()

            self.current_data = self.findItem(nom, self.current_folder)

            if self.current_data is None:
                return

                # Afficher les données dans le formulaire
            self.edit_name.setText(nom)
            self.edit_value.setText(valeur)
            self.select_cyfer.setCurrentText(encodage)

            # Définir la page du formulaire
            self.stackedWidget.setCurrentWidget(self.page_data)

    def create_hidden_directory(self):
        """
        Crée un répertoire caché pour stocker les données chiffrées au premier lancement de l'application.
        """
        # Définir le chemin du répertoire caché dans le répertoire de l'utilisateur
        self.hidden_dir = os.path.join(os.path.expanduser("~"), ".vaultface")

        # Vérifier si le répertoire existe déjà
        if not os.path.exists(self.hidden_dir):
            os.makedirs(self.hidden_dir)
            print(f"Dossier caché créé à : {self.hidden_dir}")

            # Si l'application est sur Windows, rendre le répertoire caché
            if os.name == 'nt':
                import ctypes
                FILE_ATTRIBUTE_HIDDEN = 0x02
                ctypes.windll.kernel32.SetFileAttributesW(self.hidden_dir, FILE_ATTRIBUTE_HIDDEN)
                print("Dossier caché sous Windows.")

        # Définir le chemin du fichier JSON chiffré
        self.CACHE_FILE = os.path.join(self.hidden_dir, "vault_tree.json.enc")
        print(f"Fichier de cache défini à : {self.CACHE_FILE}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = VaultFace()
    window.show()
    sys.exit(app.exec())
