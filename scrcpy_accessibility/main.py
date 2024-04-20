import sys
from PyQt6.QtWidgets import QApplication

from widget import MainWindow

class QController(QApplication):
    def __init__(self, argv: list):
        super().__init__(argv)
        self.create_widget()
    
    def create_widget(self):
        self.frame = MainWindow()
        self.frame.show()
    
def main():
    app = QController(sys.argv)
    return app.exec()

if __name__ == '__main__':
    sys.exit(main())