# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from socket import socket

from PyQt5 import QtCore, QtGui, QtWidgets
import resources.messenger as msg
import sys
from socket import *
from threading import Thread


class Server(Thread):
    activeConn: socket
    activeAddr: str
    textChat: QtWidgets.QTextEdit

    def __init__(self, textEdit, ip='127.0.0.1', port=9000):
        Thread.__init__(self)
        self.sock = socket()
        self.sock.bind((ip, port))
        self.sock.listen(1)

        self.textChat = textEdit

    def run(self) -> None:
        while True:
            self.accept()

    def activeAddress(self):
        return self.activeAddr

    def accept(self):
        sock = self.sock
        conn, addr = sock.accept()

        self.activeConn = conn
        self.activeAddr = addr

        res = conn.recv(100)
        while res:
            if res is None:
                print("connection close")
                conn.close()
                return
            else:
                print(f"data = {res.decode('utf-8')}, addr = {addr}")
                self.textChat.append(res.decode('utf-8'))
                conn.send(b"response")

            res = conn.recv(100)

    def close(self):
        self.sock.close()
        print("server socket close")


class Message(object):
    def __init__(self):
        self.conn = socket()

    def connect(self, addr, port):
        self.conn.connect((addr, port))

    def send(self, message):
        conn = self.conn

        conn.send(message.encode())
        data = b""

        tmp = conn.recv(1024)

        while tmp:
            data += tmp
            tmp = conn.recv(1024)

        print(data.decode("utf-8"))

    def close(self):
        self.conn.close()

    def __del__(self):
        close()


class ExampleApp(QtWidgets.QMainWindow, msg.Ui_MainWindow):
    def __init__(self, port=9000):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.connectButton.clicked.connect(self.connect)
        self.sendButton.clicked.connect(self.send)

        self.currentAddr.setText(f"127.0.0.1:{port}")
        self.server = Server(self.chat, '127.0.0.1', port)
        self.server.start()

        self.client = Message()

    def connect(self):
        connectMsg = "Connect"
        disconnectMsg = "Disconnect"

        if self.connectButton.text() == connectMsg:
            self.client.connect(self.addrLn.text(), int(self.portLn.text()))
            # self.server.accept()

            self.connectButton.setText(disconnectMsg)
            self.logLabel.setText("disconnected")

        elif self.connectButton.text() == disconnectMsg:
            self.client.close()
            # self.server.close()

            self.connectButton.setText(connectMsg)
            self.logLabel.setText("connect...")

    def send(self):
        message = self.lineEdit.text()
        emptyMessage = ""

        if message != emptyMessage:
            self.client.send(message)
            self.chat.append(message)
            self.lineEdit.setText(emptyMessage)

    def __del__(self):
        self.server.close()
        self.client.close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication

    port = 9000
    if len(sys.argv) > 1:
        print(sys.argv)
        port = int(sys.argv[1])

    window = ExampleApp(port)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    err = app.exec_()  # и запускаем приложение


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
