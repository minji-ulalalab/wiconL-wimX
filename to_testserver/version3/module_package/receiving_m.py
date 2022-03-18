#wicon에서 오는 정보를 받는함수  
class test_receiving:
    def recv(sock):
        while True:
            try:
                recvData = sock.recv(1024)

                print(recvData.decode('utf-8'))

            except:
                print("연결 안됨")
                break

    

        
        

        