from socket import *

class Connect():
    def __init__(self, Host, port):
        self.port = port
        self.Host = Host

    def server(self):
        serverSock = socket(AF_INET, SOCK_STREAM)#AF_INEF -> IP4v, SOCK_STREAM -> TCP 
        serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSock.bind(('', self.port))
        serverSock.listen(5)

        print('%d번 포트로 접속 대기중...'%self.port)

        #client에서 접속할때까지 대기
        connectionSock, addr = serverSock.accept()#새로운소켓, 상대방의 AF
        #client에서 접속하면 접속한 주소 출력 되면서 연결
        print(str(addr), '에서 접속되었습니다.')
        #스레드 생성(target = 실행할함수, args= 전달할인자)

        return connectionSock

    def client(self):        
        clientSock = socket(AF_INET, SOCK_STREAM)
        clientSock.connect((self.Host, self.port))
        print('접속 완료')

        return clientSock

