import socket
import threading

from PyQt5 import QtCore, QtWidgets
import sys

import chatroom_ui
import connect_ui


class ChatClient:
    def __init__(self):
        # 1. PyQt5 로 application window 생성
        self.mainWindow = QtWidgets.QMainWindow()

        # add widgets to the application window
        # connectWidget : 닉네임을 치고 접속하는 창.
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)

        # chatWidget : 채팅하는 창
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)

        # connectWidget 이 먼저 나오기 때문에 chatWidget은 숨김.
        self.chatWidget.setHidden(True)

        # chatroom_ui 모듈을 불러와서, 채팅창에서 전송 버튼을 누르면 write() 함수가 호출되도록 연결
        self.chat_ui = chatroom_ui.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        
        # 전송 버튼을 누르거나 엔터키를 누르면 write 함수 호출
        self.chat_ui.pushButton.clicked.connect(self.write)
        self.chat_ui.msgLineEdit.returnPressed.connect(self.write)

        # connect_ui 모듈을 불러와서, 접속 버튼을 누르면 btn_connect_clicked() 함수가 호출되도록 연결
        self.connect_ui = connect_ui.Ui_Dialog()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.connectButton.clicked.connect(self.btn_connect_clicked)

        # window 의  x, y, width, height 설정
        self.mainWindow.setGeometry(QtCore.QRect(1080, 100, 430, 650))

        # window 창 띄우기
        self.mainWindow.show()

        # nickname 과 client attribute 선언
        self.nickname = ''
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 닉네임을 입력하고 접속 버튼 클릭시 채팅 서버에 연결
    def btn_connect_clicked(self):

        self.nickname = self.connect_ui.nicknameTextEdit.toPlainText()

        # Connection Data
        host = self.connect_ui.ipTextEdit.toPlainText()
        port = int(self.connect_ui.portTextEdit.toPlainText())
        print(host, port)

        self.client.connect((host, port))
        self.client.send(self.nickname.encode('UTF-8'))

        # 접속 위젯은 안보이게 하고, 채팅창이 보이게 함
        self.connectWidget.setHidden(True)
        self.chatWidget.setVisible(True)

        # Starting Threads For Listening
        receive_thread = threading.Thread(target=self.receive)

        # daemon property을 변경
        receive_thread.daemon = True
        receive_thread.start()

    # Listening to Server
    # Threading 모듈로 main thread와는 다른 thread에서 동작
    def receive(self):
        while True:
            try:
                # 서버로부터의 메시지를 기다림
                # socket.recv(bufsize) : Receive data from the socket.
                message = self.client.recv(1024).decode('UTF-8')
                self.chat_ui.msgTextBrowser.append(message)

            except Exception as e:
                error = "Unable to receive message '{}'".format(str(e))
                print(error)

                # disconnect when error occurred
                self.client.close()
                break

    # Sending Messages To Server
    def write(self):
        message = '{}: {}'.format(self.nickname, self.chat_ui.msgLineEdit.text())
        try:
            self.client.send(message.encode('UTF-8'))
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print(error)

            # 에러가 생기면 커넥션을 끊음
            self.client.close()

        # 메시지 전송 완료 후 입력창을 비워줌
        self.chat_ui.msgLineEdit.clear()


if __name__ == "__main__":
    # sys.argv : 현재 client.py의 절대 경로
    app = QtWidgets.QApplication(sys.argv)
    c = ChatClient()
    sys.exit(app.exec())
