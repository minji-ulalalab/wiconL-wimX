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



class test_sending:
    checkflag = 0

    def wiconsend(self, sock, q):
        while True:
            utc_time = datetime.datetime.now(pytz.timezone('UTC')).strftime("%y%m%d%H%M%S")
            prox = q.get()#count 스레드에서 사용한 number를 전달받은 이름만 같고 다른 변수
            try:
                wiconsendData = "%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(device_ID, utc_time, device_ver, cons, RSSI, temp, humi, prox, vibr)
                sock.send(wiconsendData.encode('utf-8'))
                time.sleep(1) #1초 마다
                test_sending.checkflag = 1
            except:
                print("데이터전송실패")
                test_sending.checkflag = 0
                break

    def wimxsend(self, sock):
        while True:
            utc_time = datetime.datetime.now(pytz.timezone('UTC')).strftime("%y%m%d%H%M%S")
            wimxsendData = "TIME=%s"%utc_time
            if test_sending.checkflag == 1:
                sock.send(wimxsendData.encode('utf-8'))
                time.sleep(1) #1초 마다
                test_sending.checkflag = 0

            else:
                print("데이터가 오지 않았습니다.")
                checkflag = 0

            



    