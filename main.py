import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from demo import Ui_Dialog

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 实例化一个应用对象
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)  # 初始化窗口：吧Qt设计器设计的内容画出来，定义的信号和槽建立起来。（画界面和写程序的桥梁）
    MainWindow.setWindowTitle("penr测试工具")  # 标题
    MainWindow.show()  # 显示窗口
    sys.exit(app.exec_())  # 程序循环,等待安全退出