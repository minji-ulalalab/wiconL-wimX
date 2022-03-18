#wimX에 보내기전 테스트 단계의 testserver
#정보가 제대로 전송 되는지 확인하기 위한 용도-wimX라고 가정하고 테스트
#wimX로 보내기전 확인받을 필요있음(전송이 제대로 되었는지 확인하는 루트)
#tcp소켓통신을 이용해서 wicon(WF-1412)의 정보값을 1초단위로 wimX(현재의 testclient)에게 전송
import threading
from module_package import receiving_m, socket_m
import socket

if __name__ == "__main__":
    port = 9090
    ip = socket.gethostbyname('tcp.wim-x.kr')

    connect_socket = socket_m.Connect(ip, port)
    connectionSock = connect_socket.server()

    receiver = threading.Thread(target=receiving_m.receive, args=(connectionSock,))
    
    #스레드 실행
    receiver.start()