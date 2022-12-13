from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtWidgets
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd()+"/UI")))

form_class = uic.loadUiType("exit.ui")[0]

class ExitWindow(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.noButtton.clicked.connect(self.noBtnClick)
        self.yesButton.clicked.connect(self.yesBtnClick)

    def noBtnClick(self):
        QtCore.QCoreApplication.instance().quit()
    
    def yesBtnClick(self):
        pass
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OneCard = QtWidgets.QMainWindow()
    ui = ExitWindow()
    ui.setupUi(OneCard)
    OneCard.show()
    sys.exit(app.exec_())
