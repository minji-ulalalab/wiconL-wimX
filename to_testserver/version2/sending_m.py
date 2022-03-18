import time
import datetime
import pytz
from queue import Queue

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