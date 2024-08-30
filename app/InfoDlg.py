from PySide6.QtGui import QColor, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import Qt, QRect
from ui.Ui_InfoDialog import Ui_InfoDialog  # Assurez-vous que le chemin d'importation est correct


class InfoDlg(QDialog, Ui_InfoDialog):
    def __init__(self):
        super(InfoDlg, self).__init__()
        self.setupUi(self)

        # Supprimer la barre de titre pour un effet "Frameless"
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint)

        # Définir l'arrière-plan transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Connecter les boutons à leurs fonctions respectives
        self.btn_OK.clicked.connect(self.accept)  # Ferme la boîte de dialogue avec acceptation

        # Personnaliser le texte du message
        self.lbl_message.setText("Ceci est un message personnalisé.")

    def paintEvent(self, event):
        # Créer un QPainter pour dessiner la forme arrondie et la bordure
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)  # Activer l'antialiasing

        # Définir les paramètres du QPainterPath pour créer des coins arrondis
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        radius = 15.0  # Rayon des coins arrondis
        path.addRoundedRect(rect, radius, radius)

        # Remplir l'intérieur du QPainterPath avec la couleur de fond
        painter.fillPath(path, QColor("#2C2C2C"))

        # Dessiner la bordure noire lissée autour du chemin
        pen = QPen(QColor(180, 180, 180), 3)  # Bordure noire avec une épaisseur de 2 pixels
        pen.setCosmetic(True)  # Assure que la bordure reste fine même lors du redimensionnement
        painter.setPen(pen)
        painter.drawPath(path)

        # Appeler la méthode de la classe parente
        super(InfoDlg, self).paintEvent(event)

    def showModal(self):
        # Affiche la boîte de dialogue de manière modale
        return self.exec()  # exec() rend la boîte de dialogue modale

    def setMessage(self, message):
        self.lbl_message.setText(message)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dialog = InfoDlg()
    result = dialog.showModal()  # Appel modale
    if result == QDialog.Accepted:
        print("L'utilisateur a fermé.")

    sys.exit(0)
