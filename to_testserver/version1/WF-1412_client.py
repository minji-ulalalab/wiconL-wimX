#wimX에 보내기전 테스트 단계의 testserver
#정보가 제대로 전송 되는지 확인하기 위한 용도-wimX라고 가정하고 테스트
#wimX로 보내기전 확인받을 필요있음(전송이 제대로 되었는지 확인하는 루트)
#tcp소켓통신을 이용해서 wicon(WF-1412)의 정보값을 1초단위로 wimX(현재의 testclient)에게 전송
#모듈화하기 전

from queue import Queue
from socket import *
from count import Count
import threading
import time
import datetime
import pytz

device_ID = 'WF-001412'
device_ver = 'v0.0.1'
RSSI = '-99'
cons = '001'
temp = '23.5'
humi = '60'
vibr = '0'


def send(sock, q):
    while True:
        #now = datetime.now()
        #시간계산
        prox = q.get()#count 스레드에서 사용한 number를 전달받은 이름만 같고 다른 변수
        utc_time = datetime.datetime.now(pytz.timezone('UTC')).strftime("%y%m%d%H%M%S")

        #1초마다 정해진 정보대로 전송
        sendData = "%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(device_ID, utc_time, device_ver, RSSI, cons, temp, humi, prox, vibr)
        sock.send(sendData.encode('utf-8'))

        time.sleep(1) #1초 마다

if __name__=="__main__":
    port = 50300
    Host = socket.gethostbyname('tcp.wim-x.kr')
    

    queue = Queue()
    counting = Count()  

    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((Host, port))
    print('접속 완료')
    

    #스레드 생성(target = 실행할함수, args= 전달할인자)
    counting_thread = threading.Thread(target = counting.run, args=(queue, ))
    sending_thread = threading.Thread(target=send, args=(clientSock, queue))

    #스레드 실행
    counting_thread.start()
    sending_thread.start()

    #sender.join()
    #receiver.join()

    #프로그램이 꺼지지 않도록
    #while True:
    #    time.sleep(1)#무한루프를 쉬어가게 하는 용도
    #    pass
        