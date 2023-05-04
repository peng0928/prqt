import sys
import ctypes
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from demo import Ui_Dialog

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 实例化一个应用对象
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)  # 初始化窗口：吧Qt设计器设计的内容画出来，定义的信号和槽建立起来。（画界面和写程序的桥梁）
    MainWindow.setWindowTitle("penr测试工具")  # 标题
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    MainWindow.setWindowIcon(QIcon("./util/logo.png"))
    # 显示最小化和最大化按钮|显示关闭按钮
    MainWindow.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
    # MainWindow.setWindowFlags(Qt.WindowCloseButtonHint)  #
    MainWindow.show()  # 显示窗口
    sys.exit(app.exec_())  # 程序循环,等待安全退出
