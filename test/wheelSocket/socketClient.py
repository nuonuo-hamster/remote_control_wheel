import time
import socket

def dataTransport(ip):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 8889))
    print("connect success")
    try:
        while True:
            data = '0 60 60 60 60\n'
            client_socket.send(data.encode())
            time.sleep(1)  # 间隔 1 秒发送一次
    finally:
        client_socket.close()

def main():
    
    while(True):
        try:
            print("Try to connect server")
            dataTransport(ip='26.120.48.146')
            print("connect end")
        except:
            print("can't connect")

        print("re-connect after 5 sec")
        time.sleep(5)
if __name__ == '__main__':

    main()

    

    
