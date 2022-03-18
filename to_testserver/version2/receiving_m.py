#wicon에서 오는 정보를 받는함수  
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print(recvData.decode('utf-8'))