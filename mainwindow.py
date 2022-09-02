from PyQt5 import uic, QtWidgets


class Principal():
    def __init__(self):

        self.app = QtWidgets.QApplication([])
        self.window = uic.loadUi(r'qt\Agestor.ui')

        self.window.show()
    
    

if __name__ == "__main__":
    P = Principal()
    P.app.exec_()
