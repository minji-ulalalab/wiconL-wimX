from queue import Queue
import time

class Count():
    def run(self, q):
        number = 0
        while True:
            if number > 65535:  #65535가되면 0으로 돌아간다
                number = 0
            q.put(number)
            number += 1 # 1씩 증가
            time.sleep(1) #1초 마다