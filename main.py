# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from socket import socket

from PyQt5 import QtCore, QtGui, QtWidgets
import resources.messenger as msg
import sys
import datetime as time
import pickle
import os

from PIL import Image as image

from socket import *
from threading import Thread


class Message():
    baseMessage: str
    extension: str
    fileName: str
    lenMsg: int
    isEnd: bool

    def __init__(self, msg, ext='msg', fileName='', isEnd=True):
        self.baseMessage = msg
        self.extension = ext
        self.isEnd = isEnd
        self.fileName = fileName
        self.lenMsg = len(msg)


def addImageToChat(chat: QtWidgets.QTextEdit, name: str, image: str):
    chat.append(name)
    # str = "<img src = \"" + image + "\" width=\"350\"/>"
    chat.append("<!doctype html><html><img src="+image+"></html>")

    #chat.verticalScrollBar().setValue(chat.verticalScrollBar().maximum())


def addMessageToChat(chat: QtWidgets.QTextEdit, message: str):
    chat.append(message)
    chat.append("")
    chat.verticalScrollBar().setValue(chat.verticalScrollBar().maximum())


def addFileMessageToChat(chat: QtWidgets.QTextEdit, message: str):
    chat.setFontItalic(True)
    addMessageToChat(chat, message)
    chat.setFontItalic(False)


class tempFile():
    isOpen: bool
    file: None
    filename: str

    def __init__(self):
        self.isOpen = False


# Тот кто принимает сообщения и подключения
class Server(Thread):
    activeConn: socket
    activeAddr: str
    textChat: QtWidgets.QTextEdit
    folder: str

    def __init__(self, textEdit, ip='127.0.0.1', port=9000):
        Thread.__init__(self)
        self.sock = socket()
        self.sock.bind((ip, port))
        self.sock.listen(1)

        self.textChat = textEdit

        self.folder = os.path.join(os.getcwd(), "files")
        try:
            os.stat(self.folder)
        except:
            os.mkdir(self.folder)

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

        res: bytes

        temp = tempFile()

        try:
            res = conn.recv(1024)
            while res:
                if res is None:
                    break
                try:
                    msg = pickle.loads(res)
                    print(f"data = {msg.extension}, addr = {addr}")

                    if msg.extension == "msg":
                        addMessageToChat(self.textChat, "from some client: " + msg.baseMessage)

                    if msg.extension == "file":
                        if not temp.isOpen:
                            temp.isOpen = True
                            temp.filename = os.path.join(self.folder, msg.fileName)
                            temp.file = open(temp.filename, 'wb')

                        temp.file.write(msg.baseMessage)

                        if msg.isEnd:
                            temp.file.close()
                            temp.isOpen = False
                            temp.file = None

                            addFileMessageToChat(self.textChat, "from some client -> file: " + msg.fileName)

                    if msg.extension == "img":
                        if not temp.isOpen:
                            temp.isOpen = True
                            temp.filename = os.path.join(self.folder, msg.fileName)
                            temp.file = open(temp.filename, 'wb')

                        temp.file.write(msg.baseMessage)

                        if msg.isEnd:
                            temp.file.close()
                            temp.isOpen = False
                            temp.file = None

                            addImageToChat(self.textChat, "from some client -> image: ", temp.filename)

                    res = conn.recv(1024)
                except:
                    e = sys.exc_info()[0]
                    print("long message ", e)
                    res += conn.recv(1024)
        except:
            print("cannot receive")
            return

        resp = conn.send(b"response")
        print("conn.send ", resp)

    def __del__(self):
        try:
            self.sock.close()
        except:
            print("some exception in close connection")
        finally:
            print("server socket close")


# тот кто отправляет сообщения
class Client(object):
    def __init__(self):
        self.conn = socket()

    def connect(self, addr, port):
        try:
            self.conn.connect((addr, int(port)))
        except:
            print("cannot connect!")

    def sendFile(self, file, filename):
        conn = self.conn

        msg = Message(file)
        msg.fileName = filename
        msg.extension = 'file'

        msg_string = pickle.dumps(msg)
        try:
            conn.send(msg_string)
        except:
            print("not connected")

    def sendImage(self, file, filename):
        conn = self.conn

        msg = Message(file)
        msg.fileName = filename
        msg.extension = 'img'

        msg_string = pickle.dumps(msg)
        try:
            conn.send(msg_string)
        except:
            print("not connected")

    def sendMessage(self, msg: Message):
        conn = self.conn

        msg_string = pickle.dumps(msg)
        try:
            conn.send(msg_string)
        except:
            e = sys.exc_info()[0]
            print(e)

    def send(self, message, ext='msg'):
        conn = self.conn

        msg = Message(message)
        msg.extension = ext

        msg_string = pickle.dumps(msg)
        try:
            conn.send(msg_string)
        except:
            print("not connected")

    def close(self):
        self.conn.close()

    def __del__(self):
        self.conn.close()


class ExampleApp(QtWidgets.QMainWindow, msg.Ui_MainWindow):
    def __init__(self, port=9000):
        super().__init__()
        self.setupUi(self)
        self.connectButton.clicked.connect(self.connect)
        self.sendButton.clicked.connect(self.send)
        self.fileButton.clicked.connect(self.showFileDialog)
        self.chat.textChanged.connect(self.changeText)
        self.logEdit.setFontItalic(True)
        self.logEdit.setStyleSheet("QTextEdit {color:#822E1C}")

        self.currentAddr.setText(f"127.0.0.1:{port}")
        self.server = Server(self.chat, '127.0.0.1', port)
        self.server.start()

        self.client = Client()

    def changeText(self):
        print('h')

    def connect(self):
        connectMsg = "Connect"
        disconnectMsg = "Disconnect"

        # если нажали на коннект
        if self.connectButton.text() == connectMsg:
            self.client.connect(self.addrLn.text(), self.portLn.text())

            self.connectButton.setText(disconnectMsg)
            self.logLabel.setText("Connected")

            self.addrLn.setDisabled(True)
            self.portLn.setDisabled(True)

        # если нажали на Дисконнект
        elif self.connectButton.text() == disconnectMsg:
            self.client.close()

            self.connectButton.setText(connectMsg)
            self.logLabel.setText("Disconnected")

            self.addrLn.setEnabled(True)
            self.portLn.setEnabled(True)

            self.chat.clear()

    def send(self):
        message = self.lineEdit.text()
        emptyMessage = ""

        if message != emptyMessage:
            try:
                self.client.send(message)
            except:
                message += " (cannot send!)"
                self.logEdit.append(time.datetime.now().strftime("%H:%M:%S") + ": " + message)
            finally:
                addMessageToChat(self.chat, "me: " + message)

                self.lineEdit.setText(emptyMessage)

    def showFileDialog(self):
        dialog = QtWidgets.QFileDialog(self, 'Open File', '/Users/yapivov2/')
        if dialog.exec_() != QtWidgets.QDialog.Accepted:
            return

        fullname = dialog.selectedFiles()[0]
        fname, ext = os.path.splitext(fullname)
        basename = os.path.basename(fullname)

        if ext == '.png' or ext == '.jpg' or ext == '.jpeg':
            try:
                img = open(fullname, 'rb')
                while True:
                    strng = img.read()
                    if not strng:
                        self.client.sendMessage(Message(b'1', 'img', basename , True))
                        break

                    self.client.sendMessage(Message(strng, 'img', basename, True))

                img.close()
                addImageToChat(self.chat, "me: " + fname, fname)

            except UnicodeDecodeError:
                e = sys.exc_info()[0]
                print(f"cannot open selected file{fullname}: ", e)
                self.logEdit.append("cannot open selected file: " + fullname)

            except OSError:
                self.logEdit.append("cannot connect")
        else:
            addFileMessageToChat(self.chat, "me -> file: " + fname)

            try:
                f = open(fullname, 'rb')

                with f:
                    data = f.read()
                    self.client.sendMessage(Message(data, 'file', basename, True))

                f.close()

            except UnicodeDecodeError:
                self.logEdit.append("cannot open selected file")

            except IOError:
                self.logEdit.append("cannot connect")

    def __del__(self):
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
