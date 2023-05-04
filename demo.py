import json
from concurrent.futures import ThreadPoolExecutor
from PrSpider_run import *
from functools import partial
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from spider_sqlite import *
from w2 import UiMainTwo
from enc.encryptions import *
from enc.AES_CBC_256 import *
from enc.rsa_model_exponent import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 589)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 762, 526))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.download_num = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.download_num.setProperty("value", 5)
        self.download_num.setObjectName("download_num")
        self.gridLayout.addWidget(self.download_num, 8, 7, 1, 1)
        self.header_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.header_2.setObjectName("header_2")
        self.gridLayout.addWidget(self.header_2, 4, 1, 1, 16)
        self.download_delay = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.download_delay.setProperty("value", 1)
        self.download_delay.setObjectName("download_delay")
        self.gridLayout.addWidget(self.download_delay, 7, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.retry = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.retry.setProperty("value", 3)
        self.retry.setObjectName("retry")
        self.gridLayout.addWidget(self.retry, 5, 4, 1, 1)
        self.url = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.url.setObjectName("url")
        self.gridLayout.addWidget(self.url, 0, 1, 1, 16)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 6, 1, 1)
        self.verify = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.verify.setObjectName("verify")
        self.gridLayout.addWidget(self.verify, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.datas = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.datas.setObjectName("datas")
        self.gridLayout.addWidget(self.datas, 1, 1, 1, 16)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 2, 1, 1)
        self.task = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.task.setText("")
        self.task.setObjectName("task")
        self.gridLayout.addWidget(self.task, 10, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 6, 1, 1)
        self.worker = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.worker.setProperty("value", 1)
        self.worker.setObjectName("worker")
        self.gridLayout.addWidget(self.worker, 8, 4, 1, 1)
        self.encode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.encode.setObjectName("encode")
        self.gridLayout.addWidget(self.encode, 5, 7, 1, 1)
        self.stdout = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.stdout.setObjectName("stdout")
        self.gridLayout.addWidget(self.stdout, 8, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 6, 1, 1)
        self.post = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.post.setObjectName("post")
        self.gridLayout.addWidget(self.post, 7, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.log = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.log.setObjectName("log")
        self.gridLayout.addWidget(self.log, 7, 4, 1, 1)
        self.timeout = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.timeout.setProperty("value", 3)
        self.timeout.setObjectName("timeout")
        self.gridLayout.addWidget(self.timeout, 10, 7, 1, 1)
        self.start = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 11, 4, 1, 1)
        self.check_cookie = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.check_cookie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_cookie.setObjectName("check_cookie")
        self.gridLayout.addWidget(self.check_cookie, 11, 7, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.clearbtn = QtWidgets.QPushButton(self.tab_4)
        self.clearbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearbtn.setObjectName("clearbtn")
        self.gridLayout_3.addWidget(self.clearbtn, 0, 1, 1, 1)
        self.refush = QtWidgets.QPushButton(self.tab_4)
        self.refush.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refush.setObjectName("refush")
        self.gridLayout_3.addWidget(self.refush, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 762, 526))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.getheaders = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.getheaders.setObjectName("getheaders")
        self.gridLayout_4.addWidget(self.getheaders, 0, 0, 1, 2)
        self.addheader = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.addheader.setObjectName("addheader")
        self.gridLayout_4.addWidget(self.addheader, 0, 2, 1, 1)
        self.json_zh = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.json_zh.setObjectName("json_zh")
        self.gridLayout_4.addWidget(self.json_zh, 1, 0, 1, 1)
        self.start_headers = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.start_headers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_headers.setObjectName("start_headers")
        self.gridLayout_4.addWidget(self.start_headers, 1, 1, 1, 2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 762, 526))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pwd = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.pwd.setText("")
        self.pwd.setObjectName("pwd")
        self.gridLayout_5.addWidget(self.pwd, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 3, 1, 1)
        self.en_str = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.en_str.setObjectName("en_str")
        self.gridLayout_5.addWidget(self.en_str, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.iv = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.iv.setObjectName("iv")
        self.gridLayout_5.addWidget(self.iv, 0, 4, 1, 1)
        self.de_str = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.de_str.setObjectName("de_str")
        self.gridLayout_5.addWidget(self.de_str, 2, 4, 1, 1)
        self.encstart = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.encstart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encstart.setObjectName("encstart")
        self.gridLayout_5.addWidget(self.encstart, 3, 1, 1, 1)
        self.decstart = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.decstart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decstart.setObjectName("decstart")
        self.gridLayout_5.addWidget(self.decstart, 3, 4, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "请求参数"))
        self.url.setHtml(_translate("Dialog",
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "下载数"))
        self.verify.setText(_translate("Dialog", "Verify"))
        self.label_3.setText(_translate("Dialog", "请求头"))
        self.label_5.setText(_translate("Dialog", "Retry"))
        self.datas.setHtml(_translate("Dialog",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "线程数"))
        self.label_4.setText(_translate("Dialog", "编码方式"))
        self.encode.setText(_translate("Dialog", "utf-8"))
        self.stdout.setText(_translate("Dialog", "日志重定向"))
        self.label_7.setText(_translate("Dialog", "Timeout"))
        self.post.setText(_translate("Dialog", "Post"))
        self.label_11.setText(_translate("Dialog", "任务名"))
        self.label_10.setText(_translate("Dialog", "下载延迟"))
        self.label_6.setText(_translate("Dialog", "Log"))
        self.label.setText(_translate("Dialog", "请求网站"))
        self.log.setText(_translate("Dialog", "info"))
        self.start.setText(_translate("Dialog", "启动"))
        self.check_cookie.setText(_translate("Dialog", "检测cookie"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "请求测试"))
        self.clearbtn.setText(_translate("Dialog", "清空全部"))
        self.refush.setText(_translate("Dialog", "刷新"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "网站"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "状态码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "请求体"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "响应字节"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "响应内容"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "插入时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "源码查看"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "任务列表"))
        self.json_zh.setText(_translate("Dialog", "JSON转换"))
        self.start_headers.setText(_translate("Dialog", "启动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "headers"))
        self.label_13.setText(_translate("Dialog", "偏移量"))
        self.label_12.setText(_translate("Dialog", "密钥"))
        self.encstart.setText(_translate("Dialog", "加密"))
        self.decstart.setText(_translate("Dialog", "解密"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "加解密"))
        """开始"""
        self.get_data_sqlite()
        self.start.clicked.connect(self.start_btn)
        self.encstart.clicked.connect(self.encstart_btn)
        self.decstart.clicked.connect(self.decstart_btn)
        self.refush.clicked.connect(self.refush_btn)
        self.check_cookie.clicked.connect(self.check_cookie_btn)
        self.clearbtn.clicked.connect(self.clearbtn_btn)
        self.start_headers.clicked.connect(self.start_headers_btn)
        self.tableWidget.cellPressed.connect(self.getPosContent)

    def start_btn(self):
        url = self.url.toPlainText()
        data = self.datas.toPlainText()
        header = self.header_2.toPlainText()
        header = header if header else {}
        encode = self.encode.text()
        retry = self.retry.text()
        log = self.log.text()
        task = self.task.text()
        download_delay = self.download_delay.text()
        download_num = self.download_num.text()
        timeout = self.timeout.text()
        worker = self.worker.text()
        verify = self.verify.isChecked()
        post = self.post.isChecked()
        stdout = self.stdout.isChecked()
        stdout = True if stdout else False
        method = 'POST' if post else 'get'
        if url:
            try:
                ThreadPoolExecutor(3).submit(
                    Spider, url=url,
                    verify=verify, retrytime=retry, method=method, header=header, encode=encode,
                    stdout=stdout, loger=log, timeout=timeout, download_delay=download_delay,
                    download_num=download_num,
                    task=task, worker=worker, data=data
                )
            except Exception as e:
                print(e)

    def check_cookie_btn(self):
        url = self.url.toPlainText()
        data = self.datas.toPlainText()
        header = self.header_2.toPlainText()
        header = header if header else {}
        encode = self.encode.text()
        retry = self.retry.text()
        log = self.log.text()
        task = self.task.text()
        download_delay = self.download_delay.text()
        download_num = self.download_num.text()
        timeout = self.timeout.text()
        worker = self.worker.text()
        verify = self.verify.isChecked()
        post = self.post.isChecked()
        stdout = self.stdout.isChecked()
        stdout = True if stdout else False
        method = 'POST' if post else 'get'
        if url:
            try:
                ThreadPoolExecutor(3).submit(
                    Spider_Cookie, url=url,
                    verify=verify, retrytime=retry, method=method, header=header, encode=encode,
                    stdout=stdout, loger=log, timeout=timeout, download_delay=download_delay,
                    download_num=download_num,
                    task=task, worker=worker, data=data
                )
            except Exception as e:
                print(e)

    def refush_btn(self):
        for rowNum in range(0, self.tableWidget.rowCount())[::-1]:  # 逆序删除，正序删除会有一些删除不成功
            self.tableWidget.removeRow(rowNum)
        self.get_data_sqlite()

    def encstart_btn(self):
        key = self.pwd.text()
        iv = self.iv.text()
        data = self.en_str.toPlainText()
        rjson = {
            'base64': bs64(data),
            'md5': md5(data),
            'sha1': sha1(data),
            'sha256': sha256(data),
            'sha512': sha512(data),
            'url_quote': url_enquote(data),
            'unicode': str(unicode(data), 'utf-8'),
            'timestamp': timestamp(),
            'aes_cbc': aes_cbc_encrypt(text=data, key=key, iv=iv),
            'aes_cbc_256': AesCrypto(key=key, iv=iv).encrypt(text=data),
            'rsa_model_exponent': Encrypt(e=key, m=iv).encrypt(data),
        }
        s = self.js_header(str(rjson))
        self.de_str.setPlainText(s)

    def decstart_btn(self):
        key = self.pwd.text()
        iv = self.iv.text()
        data = self.en_str.toPlainText()
        rjson = {
            'base64': d_bs64(data),
            'unicode': unicode_escape(data),
            'timestamp': d_timestamp(data),
            'url_unquote': url_unquote(data),
            'aes_cbc': aes_cbc(word=data, key=key, offset=iv),
            'aes_cbc_256': AesCrypto(key=key, iv=iv).decrypt(text=data)
        }
        self.de_str.setPlainText('%s' % self.js_header(str(rjson)))

    def clearbtn_btn(self):
        del_data()
        self.refush_btn()

    def start_headers_btn(self):
        json_bool = self.json_zh.isChecked()
        headers = self.getheaders.toPlainText()
        if json_bool:
            try:
                if isinstance(headers, str):
                    try:
                        if headers[0] == '"' or headers[0] == "'":
                            headers = eval(headers)
                        else:
                            headers = f"'{headers}'"
                            headers = eval(headers)
                    except:
                        pass
                    finally:
                        try:
                            json.loads(headers)
                        except:
                            pass
                hstr = self.js_header(headers)
                self.addheader.setPlainText((hstr))
            except Exception as e:
                self.addheader.setPlainText('格式错误 <%s>' % e)
        else:
            hstr = self.func_header(headers)
            self.addheader.setPlainText(hstr)

    def unicode_escape(self, word=None):
        if isinstance(word, bytes):
            word = str(word, 'unicode_escape')
            word = bytes(word, 'unicode_escape')
            return word.decode('unicode_escape')
        if isinstance(word, str):
            word = re.sub(r'(\\u[a-zA-Z0-9]{4})', lambda x: x.group(1).encode("utf-8").decode("unicode-escape"), word)
            word = bytes(word, 'unicode_escape')
            return word.decode('unicode_escape')

    def js_header(self, headers):
        h_str = re.sub('(.*?:.*?,|.*?:.*?})', r'\n\1', headers)
        h_str = self.unicode_escape(h_str)
        return h_str

    def func_header(self, headers):
        h_str = '{\n'
        if headers:
            headers = re.sub(':\s+', ':', headers)
            headers = headers.replace('：', ':').replace(':\n', ':').replace(': ', ':')
            # hdic = {}
            headers = re.findall('(.*?):(.*)', headers)
            for query in headers:
                k = query[0].replace('"', '\\"')
                v = query[1].replace('"', '\\"')
                h_str += f"""  "{k}": "{v}", \n"""
        h_str += '}'
        return h_str

    def start_view(self, row, rol):
        ids = self.tableWidget.item(row, 0).text()
        try:
            data = get_one_data(ids)
            data = data[0][-3]
            data = data if data else '请求失败'
        except Exception as e:
            data = f'请求失败:: {e}'
        self.ui_2 = UiMainTwo(title='源码-' + str(ids), text=data)
        self.ui_2.show()

    def getPosContent(self, row, col):
        try:
            content = self.tableWidget.item(row, col).text()
            print("选中行：" + str(row))
            print("选中列：" + str(col))
            print('选中内容:' + content)
        except:
            pass

    def get_data_sqlite(self):
        for item in get_data():
            ids = item[0]
            url = item[1]
            code = item[2]
            req_headers = item[3].replace('\\', '')
            res_headers = item[4].replace('\\', '')
            res_len = item[5]
            date = item[7]
            row_count = self.tableWidget.rowCount()  # 返回当前行数(尾部)
            self.view_start = QtWidgets.QPushButton('查看')
            self.view_start.clicked.connect(partial(self.start_view, row_count))
            self.tableWidget.insertRow(row_count)
            self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(ids)))
            self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(url))
            self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(code))
            self.tableWidget.setItem(row_count, 3, QtWidgets.QTableWidgetItem(req_headers))
            self.tableWidget.setItem(row_count, 4, QtWidgets.QTableWidgetItem(res_len))
            self.tableWidget.setItem(row_count, 5, QtWidgets.QTableWidgetItem(res_headers))
            self.tableWidget.setItem(row_count, 6, QtWidgets.QTableWidgetItem(date))
            self.tableWidget.setCellWidget(row_count, 7, self.view_start)


class Child(QWidget):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle(content)
