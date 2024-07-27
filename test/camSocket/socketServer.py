import cv2
import socket
import pickle
import struct

def serverOpen():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    return server_socket

def dataTransport(server_socket):
    client_socket, addr = server_socket.accept()
    connection = client_socket.makefile('wb')
    try:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            data = pickle.dumps(frame)
            size = struct.pack('!I', len(data))
            connection.write(size)
            connection.write(data)
            # cv2.imshow('Server', frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
    finally:
        connection.close()
        client_socket.close()

def main():

    print("open server")
    server_socket = serverOpen()

    while(True):
        try:
            print("Try to connect client")
            dataTransport(server_socket)
            print("client offline")
        except:
            pass

if __name__ == '__main__':

    main()