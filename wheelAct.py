# pipenv install pyserial
import time
import serial
from wheelManage import socketClient

def wheelInit():

    try:
        client_socket = socketClient.connectArduino('192.168.137.103')
        return client_socket
    except:
        return None
    # # 串口初始化
    # ser = serial.Serial('/dev/ttyACM0', 115200)  # 请替换为你的 Arduino 串口号和波特率

    # # 等待串口初始化完成
    # time.sleep(1)

    # return ser

def serialSendText(TKRoot, text):

    try:
        socketClient.sendText(TKRoot.client_socket, text)
    except:
        pass

def closeClient(client_socket):

    if(client_socket is not None):
        socketClient.clientClose(client_socket)

def determineKey(keyboardList):
    
    length = len(keyboardList)
    if length != 0:
        index = length-1
        return index
    else:
        return None
    
def modeSwitch(keyboardList, index):
    
    if index is None:
        return 'p'
    else:
        return keyboardList[index]

# def transform_wheel_mode(speed, deflection, shiftlock):

#     if shiftlock == 1:
#         if (deflection > 0): return 3
#         else: return 4
    
#     if -50 < speed < 50:
#         return 0
#     elif speed >= 50:
#         return 1
#     elif speed <= 50:
#         return 2

def generateSerialText(opcode, ButtomList):
    if opcode == 'p': mode = 0
    elif opcode == 'w': mode = 1
    elif opcode == 'a': mode = 3
    elif opcode == 's': mode = 2
    elif opcode == 'd': mode = 4
    elif opcode == 'q': mode = 8
    elif opcode == 'e': mode = 9
    else: 
        if opcode == '+' or opcode == 'plus':
            ButtomList.addLabel('LF', 1)
            ButtomList.addLabel('RF', 1)
            ButtomList.addLabel('LB', 1)
            ButtomList.addLabel('RB', 1)
        elif opcode == '-':
            ButtomList.subLabel('LF', 1)
            ButtomList.subLabel('RF', 1)
            ButtomList.subLabel('LB', 1)
            ButtomList.subLabel('RB', 1)
        return None

    speedArr=[ButtomList.Speed_1,ButtomList.Speed_2,ButtomList.Speed_3,ButtomList.Speed_4]
    return f'{mode} {speedArr[0]} {speedArr[1]} {speedArr[2]} {speedArr[3]}\n'

# def sent_massege(ser, text):
    
#     # 向 Arduino 发送数据
#     # data_to_send = f'1 80 90 90 70\n'
#     data_to_send = text
#     # print(data_to_send)
#     ser.write(data_to_send.encode()) 

def keyboardReact(windowHandler):
    TKRoot = windowHandler.TKRoot
    keyboardList = windowHandler.KBhandle.keysInLabel
    
    index = determineKey(keyboardList)# array index
    operateCode = modeSwitch(keyboardList, index) # p q w e a s d
    text = generateSerialText(operateCode, windowHandler.ButtomList) # arduino command

    if text != None and text != TKRoot.serialText:
        TKRoot.wheel_label.config(text=f'wheel send: {text}', fg='black')
        serialSendText(TKRoot, text)
        # time.sleep(0.1)
        TKRoot.serialText = text
    # else:
        # TKRoot.wheel_label.config(text=f'wheel send: ')
    
if __name__ == '__main__':

    pass
    # ser = wheelInit()
    # sent_massege(ser, f'0 60 60 60 60\n')