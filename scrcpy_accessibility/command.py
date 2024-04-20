import os
from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal, QThread
import subprocess

ADB_DIR = 'C:\\Users\\lombo\\Downloads\\scrcpy-win64-v2.4\\scrcpy-win64-v2.4'

def make_command(cmd: list[str] | str):
    args = [os.path.join(ADB_DIR, 'adb.exe'), 'shell']
    if isinstance(cmd, str):
        cmd = cmd.split(' ')
    args.extend(cmd)
    print("Command is:", ' '.join(args))
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    stdout, stderr = proc.communicate()
    if stderr:
        raise RuntimeError("Error with adb: " + stderr.decode('utf-8'))
    return stdout.decode('utf-8')

def get_dim():
    result = make_command(['wm', 'size'])
    _, _, dims = result.partition(':')
    width, _, height = dims.partition('x')
    width = width.strip()
    height = height.strip()
    return int(width), int(height)

class Commander(QObject):
    command_succeeded = pyqtSignal(str, str)
    command_failed = pyqtSignal(str, str)

    @pyqtSlot(str, str)
    def command(self, command_name: str, command: str):
        try:
            result = make_command(command)
        except RuntimeError as re:
            self.command_failed.emit(command_name, re.args[0])
        else:
            self.command_succeeded.emit(command_name, result)

class CommandMaker(QObject):
    command_signal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.get_dim()
        self.init_commander()

    def init_commander(self):
        self.commander = Commander()
        self.worker_thread = QThread()

        self.command_signal.connect(self.commander.command)
        self.commander.command_succeeded.connect(self.command_succeeded)
        self.commander.command_failed.connect(self.command_failed)

        self.commander.moveToThread(self.worker_thread)
        self.worker_thread.start()

    def get_dim(self):
        width, height = get_dim()
        print("Width:" , width, "Height:", height)
        self.width = width
        self.height = height
    
    @pyqtSlot()
    def wake_phone_up(self):
        self.command_signal.emit('wake up', 'input keyevent KEYCODE_WAKEUP')
    
    @pyqtSlot()
    def swipe_left(self):
        y_pivot = self.height // 2
        x2 = self.width // 10
        x1 = self.width - x2
        self.swipe(x1, y_pivot, x2, y_pivot)

    @pyqtSlot()
    def swipe_right(self):
        y_pivot = self.height // 2
        x1 = self.width // 10
        x2 = self.width - x1
        self.swipe(x1, y_pivot, x2, y_pivot)

    @pyqtSlot()
    def swipe_down(self):
        x_pivot = self.width // 2
        y1 = self.height // 10
        y2 = self.height - y1
        self.swipe(x_pivot, y1, x_pivot, y2)
    
    @pyqtSlot()
    def swipe_up(self):
        x_pivot = self.width // 2
        y2 = self.height // 10
        y1 = self.height - y2
        self.swipe(x_pivot, y1, x_pivot, y2)
    
    @pyqtSlot()
    def open_ez_fare(self):
        self.command_signal.emit('EZ Fare', 'am start -n com.justride.ohioride/io.ionic.starter.MainActivity')
    
    @pyqtSlot()
    def open_wyze(self):
        self.command_signal.emit('WYZE', 'am start -n com.hualai/com.hualai.home.SmartHomeMainActivity')
    
    @pyqtSlot()
    def open_csc_go(self):
        self.command_signal.emit('CSC Go', 'am start -n com.cscsw.cscgo/com.mycscgo.laundry.general.ui.MainActivity')
    
    def swipe(self, x1: int, y1: int, x2: int, y2: int):
        self.command_signal.emit('swipe', f'input touchscreen swipe {x1} {y1} {x2} {y2}')
    
    @pyqtSlot(str, str)
    def command_succeeded(self, cmd_name: str, result: str):
        pass

    @pyqtSlot(str, str)
    def command_failed(self, cmd_name: str, reason: str):
        print(cmd_name, "failed because", reason)
