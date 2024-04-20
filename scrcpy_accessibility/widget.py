from PyQt6.QtWidgets import QGridLayout, QMainWindow, QPushButton, QWidget

from command import CommandMaker

class SwiperWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.command_maker = CommandMaker()
        self.populate_widget()
    
    def populate_widget(self):
        layout = QGridLayout()

        button = QPushButton("Swipe Up")
        button.clicked.connect(self.command_maker.swipe_up)
        layout.addWidget(button, 0, 1)
        button = QPushButton("Swipe Down")
        button.clicked.connect(self.command_maker.swipe_down)
        layout.addWidget(button, 2, 1)
        button = QPushButton("Swipe Left")
        button.clicked.connect(self.command_maker.swipe_left)
        layout.addWidget(button, 1, 0)
        button = QPushButton("Swipe Right")
        button.clicked.connect(self.command_maker.swipe_right)
        layout.addWidget(button, 1, 2)

        self.setLayout(layout)


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
        self.setCentralWidget(MainWidget())
    
   