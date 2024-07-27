import cv2
import socket
import pickle
import struct

import realsense

def serverOpen():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    return server_socket

def dataTransport(server_socket):
    client_socket, addr = server_socket.accept()
    connection = client_socket.makefile('wb')
    try:
        pipe = realsense.realsense_init(width=640, height=480)
        while True:
            depth_frame, color_image, depth_cm = realsense.realsense_run(pipe)
            data = pickle.dumps(color_image)
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