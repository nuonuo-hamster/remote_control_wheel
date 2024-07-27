import cv2
import time
import socket
import pickle
import struct

def dataTransport(ip):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 8888))
    print("connect success")
    connection = client_socket.makefile('rb')
    try:
        while True:
            size = struct.unpack('!I', connection.read(struct.calcsize('!I')))[0]
            data = connection.read(size)
            frame = pickle.loads(data)
            cv2.imshow('Client', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    finally:
        connection.close()
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

    

    
