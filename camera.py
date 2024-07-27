import cv2

from cam.socketClient import*
# from cam.realsense import*

def initFrame(cameraType):
    # 1.
    if(cameraType=='realsense'):
        print("Try to connect camera")
        connection = getServerStream(ip='192.168.137.103')
        print("camera connect success")
        return connection

    # 2.
    if(cameraType=='webcam'):
        cap = cv2.VideoCapture(0)

    # 3.
    # cap = realsense_init(width=720, height=480)

    return cap

def getFrame(cap, cameraType):
    # 1.
    if(cameraType=='realsense'):
        ret, frame = getServerFrame(connection = cap)

    # 2.
    if(cameraType=='webcam'):
        ret, frame = cap.read()

    # 3.
    # try:
    #     depth_frame, color_image, depth_cm = realsense_run(cap)
    #     ret, frame = True, color_image
    # except:
    #     print("camera error")

    return ret, frame

def capRelease(cap):
    # 1.
    connection = cap
    connection.close()
    
    # 2.3.
    # cap.release()
    