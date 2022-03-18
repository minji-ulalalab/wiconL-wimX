#wimX에 보내기전 테스트 단계의 testserver
#정보가 제대로 전송 되는지 확인하기 위한 용도-wimX라고 가정하고 테스트
#wimX로 보내기전 확인받을 필요있음(전송이 제대로 되었는지 확인하는 루트)
#tcp소켓통신을 이용해서 wicon(WF-1412)의 정보값을 1초단위로 wimX(현재의 testclient)에게 전송

import threading
from socket import *


#wicon에서 오는 정보를 받는함수  
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print(recvData.decode('utf-8'))
        
        

if __name__ == "__main__":

    
    port = 50300
    Host = socket.gethostbyname('tcp.wim-x.kr')

    serverSock = socket(AF_INET, SOCK_STREAM)#AF_INEF -> IP4v, SOCK_STREAM -> TCP 
    serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSock.bind(('', port))
    serverSock.listen(1)

    print('%d번 포트로 접속 대기중...'%port)

    #client에서 접속할때까지 대기
    connectionSock, addr = serverSock.accept()#새로운소켓, 상대방의 AF
    #client에서 접속하면 접속한 주소 출력 되면서 연결
    print(str(addr), '에서 접속되었습니다.')
    #스레드 생성(target = 실행할함수, args= 전달할인자)
    receiver = threading.Thread(target=receive, args=(connectionSock,))

    #스레드 실행
    receiver.start()