import socket
import time
import serial

def connectSer():
    # 串口初始化
    ser = serial.Serial('/dev/ttyACM0', 9600)  # 请替换为你的 Arduino 串口号和波特率

    # 等待串口初始化完成
    time.sleep(1)

    return ser

def sent_massege(ser, text):

    # 向 Arduino 发送数据
    data_to_send = text
    # print(data_to_send)
    ser.write(data_to_send.encode()) 

def serverOpen():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8889))
    server_socket.listen(5)
    return server_socket

def dataTransport(server_socket, ser):
    client_socket, addr = server_socket.accept()
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received data: {data}")
            sent_massege(ser, text= data)
    finally:
        client_socket.close()

def main():

    print("open server")
    ser = connectSer()
    server_socket = serverOpen()

    while(True):
        try:
            print("Wait for client...")
            dataTransport(server_socket, ser)
            print("client offline")
        except:
            pass

if __name__ == '__main__':

    main()
