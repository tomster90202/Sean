from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

from command import CommandMaker

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.command_maker = CommandMaker()
        self.populate_window()

    def populate_window(self):
        layout = QVBoxLayout()

        label = QLabel("scrcpy Accessibility")
        layout.addWidget(label)

        button = QPushButton("Wake Phone Up")
        button.clicked.connect(self.command_maker.wake_phone_up)
        layout.addWidget(button)
        button = QPushButton("Swipe Up")
        button.clicked.connect(self.command_maker.swipe_up)
        layout.addWidget(button)
        button = QPushButton("Swipe Down")
        button.clicked.connect(self.command_maker.swipe_down)
        layout.addWidget(button)
        button = QPushButton("Swipe Left")
        button.clicked.connect(self.command_maker.swipe_left)
        layout.addWidget(button)
        button = QPushButton("Swipe Right")
        button.clicked.connect(self.command_maker.swipe_right)
        layout.addWidget(button)
        button = QPushButton("Open EZ Fare")
        button.clicked.connect(self.command_maker.open_ez_fare)
        layout.addWidget(button)
        button = QPushButton("Open WYZE")
        button.clicked.connect(self.command_maker.open_wyze)
        layout.addWidget(button)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("scrcpy Accessibility")
        self.setGeometry(100, 100, 640, 480)
        self.setCentralWidget(MainWidget())
    
   