#wimX에 보내기전 테스트 단계의 testserver
#정보가 제대로 전송 되는지 확인하기 위한 용도-wimX라고 가정하고 테스트
#wimX로 보내기전 확인받을 필요있음(전송이 제대로 되었는지 확인하는 루트)
#tcp소켓통신을 이용해서 wicon(WF-1412)의 정보값을 1초단위로 wimX(현재의 testclient)에게 전송
#모듈화 후

from queue import Queue
from module_package import socket_m, count_m, sending_m, receiving_m
import threading
import socket

if __name__=="__main__":
    port = 9090
    ip = '192.168.55.65'

    queue = Queue()
    counting = count_m.Count()
    sending = sending_m.test_sending()
    receiving = receiving_m.test_receiving()

    connect_socket = socket_m.Connect(ip, port)
    clientSock = connect_socket.client()

    #스레드 생성(target = 실행할함수, args= 전달할인자)
    counting_thread = threading.Thread(target=counting.run, args=(queue, ))
    sending_thread = threading.Thread(target=sending.wiconsend, args=(clientSock, queue))
    receiving_thread = threading.Thread(target=receiving.recv, args=(clientSock, ))
    #스레드 실행
    counting_thread.start()
    sending_thread.start()
    receiving_thread.start()




        