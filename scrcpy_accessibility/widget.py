from PyQt6.QtWidgets import QGridLayout, QLabel, QMainWindow, QPushButton, QWidget
from PyQt6.QtCore import Qt

from command import CommandMaker

class SwiperWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.command_maker = CommandMaker()
        self.populate_widget()
    
    def populate_widget(self):
        layout = QGridLayout()
        
        button = QPushButton()
        button.setFixedSize(70, 65)
        self.create_label_in_button(button, "Swipe Up", "↑")
        button.clicked.connect(self.command_maker.swipe_up)
        layout.addWidget(button, 0, 1, Qt.AlignmentFlag.AlignCenter)

        button = QPushButton()
        button.setFixedSize(100, 65)
        self.create_label_in_button(button, "Swipe Down", "↓")
        button.clicked.connect(self.command_maker.swipe_down)
        layout.addWidget(button, 2, 1, Qt.AlignmentFlag.AlignCenter)

        button = QPushButton()
        button.setFixedSize(100, 65)
        self.create_label_in_button(button, "Swipe Right", "→")
        button.clicked.connect(self.command_maker.swipe_right)
        layout.addWidget(button, 1, 2, Qt.AlignmentFlag.AlignCenter)

        button = QPushButton()
        button.setFixedSize(90, 65)
        self.create_label_in_button(button, "Swipe Left", "←")
        button.clicked.connect(self.command_maker.swipe_left)
        layout.addWidget(button, 1, 0, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
    
    @staticmethod
    def create_label_in_button(button: QPushButton, text: str, arrow: str):
        label = QLabel(button)
        label.setText(f"<font size=5>{text}</font><br><b><font size=10>{arrow}</font></b>")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.command_maker = CommandMaker()
        self.populate_widget()

    def populate_widget(self):
        layout = QGridLayout()

        # label = QLabel("scrcpy Accessibility")
        # layout.addWidget(label)

        button = QPushButton("Wake Phone Up")
        button.clicked.connect(self.command_maker.wake_phone_up)
        layout.addWidget(button, 0, 0)
        layout.addWidget(SwiperWidget(), 0, 1, 1, 2)
        button = QPushButton("Open EZ Fare")
        button.clicked.connect(self.command_maker.open_ez_fare)
        layout.addWidget(button)
        button = QPushButton("Open WYZE")
        button.clicked.connect(self.command_maker.open_wyze)
        layout.addWidget(button)
        button = QPushButton("Open CSC Go")
        button.clicked.connect(self.command_maker.open_csc_go)
        layout.addWidget(button)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("scrcpy Accessibility")
        self.move(0, 0)
        self.setCentralWidget(MainWidget())
    
   