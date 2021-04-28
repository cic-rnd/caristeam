import socket
import threading

# Sending Messages To All Connected Clients
# socket.send(bytes[, flags])
# Send data to the socket. The socket must be connected to a remote socket.
def broadcast(*args):

    message = args[0]

    # users
    clients = users.keys()

    # 스레드가 살아있는 client에만 메시지 전송 
    for client in clients:
        if users_thread[client].is_alive():
            client.send(message)


# Handling Messages From Clients
def handle(client):

    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)

        except Exception as e:
            print("handle Exception")
            print(e)
            print(type(e))

            # 소켓정보를 key 값으로 nickname 을 찾음.
            nickname = users[client]
            broadcast('{} 님이 채팅방을 나가셨습니다.'.format(nickname).encode('UTF-8'))

            # 접속 종료
            client.close()

            # 전체 이용자 목록에서 나간 이용자 삭제
            del users[client]

            break

# 새로운 클라이언트를 받음
# 클라이언트의 메시지를 처리하는 handle 함수를 실행하는 쓰레드를 생성
def receive():
    while True:
        # Accept Connection
        print("Server.py receive thread!!!")

        # accept connections from outside
        # 접속을 기다림
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        # 연결된 클라이언트의 소켓정보를 key 값으로 사용자 닉네임을 저장
        nickname = client.recv(1024).decode('UTF-8')
        users[client] = nickname

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        # client.send('채팅에 접속하셨습니다.\n'.encode('UTF-8'))


        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))

        users_thread[client] = thread
        thread.start()
        broadcast("{} 님이 채팅에 접속하셨습니다".format(nickname).encode('UTF-8'))



if __name__ == "__main__":

    print("Server is listening...")

    # Connection Data
    host = '192.168.19.212'
    port = 55555

    # Starting Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a public host, and a well-known port
    # serversocket.bind((socket.gethostname(), 80))
    server.bind((host, port))
    # we used socket.gethostname() so that the socket would be visible to the outside world. If we had used s.bind(('localhost', 80)) or s.bind(('127.0.0.1', 80)) we would still have a “server” socket, but one that was only visible within the same machine. s.bind(('', 80)) specifies that the socket is reachable by any address the machine happens to have.

    # become a server socket
    server.listen()

    # Lists For Clients socket information and Their Nicknames
    users = {}
    users_thread = {}

    # 새로운 클라이언트를 받음
    receive()
