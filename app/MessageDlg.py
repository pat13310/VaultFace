from PySide6.QtGui import QColor
from PySide6.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from ui.Ui_Dialog import Ui_Dialog  # Assurez-vous que le chemin d'importation est correct


class MessageDlg(QDialog, Ui_Dialog):
    def __init__(self):
        super(MessageDlg, self).__init__()
        self.setupUi(self)

        # Supprimer la barre de titre pour un effet "Frameless"
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Connecter les boutons à leurs fonctions respectives
        self.btn_OK.clicked.connect(self.accept)  # Ferme la boîte de dialogue avec acceptation
        self.btn_cancel.clicked.connect(self.reject)  # Ferme la boîte de dialogue avec rejet

        # Ajouter ici d'autres personnalisations si nécessaire
        self.lbl_message.setText("Ceci est un message personnalisé.")

    def showModal(self):
        # Affiche la boîte de dialogue de manière modale
        return self.exec()  # exec() rend la boîte de dialogue modale

    def setMessage(self, param):
        self.lbl_message.setText(param)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dialog = MessageDlg()
    result = dialog.showModal()  # Appel modale
    if result == QDialog.Accepted:
        print("L'utilisateur a accepté.")
    else:
        print("L'utilisateur a annulé.")
    sys.exit(0)
