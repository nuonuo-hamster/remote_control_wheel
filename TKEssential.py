import cv2
import tkinter as tk
from PIL import Image, ImageTk

import multiprocessing
import camera
import keyboardHandle
import wheelAct

def put_keyboard_label(windowHandler):
    TKRoot = windowHandler.TKRoot
    KBhandle = windowHandler.KBhandle

    for idex, key in enumerate(KBhandle.ctlList):
        if idex <= 5:
            KBhandle.labelArr[idex] = tk.Label(TKRoot.root, text=f"{key.upper()}", font=("Arial", 24))
            KBhandle.labelArr[idex].place(x=KBhandle.labelPlaceX[idex], y=KBhandle.labelPlaceY[idex])
    
def detect_keyboard_input(windowHandler):
    TKRoot = windowHandler.TKRoot
    KBhandle = windowHandler.KBhandle
    
    while True:
        try:
            keyboardHandle.trigger(TKRoot, KBhandle)
            wheelAct.keyboardReact(windowHandler)
        except:
            pass
            # break

def update_frame(TKRoot):
    ret, frame = camera.getFrame(TKRoot.cap, TKRoot.capType)
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        TKRoot.video_label.imgtk = imgtk
        TKRoot.video_label.config(image=imgtk)
    TKRoot.video_label.after(10, update_frame, TKRoot)

class TKInfo:
    def __init__(self, cameraType='webcam' ,arduinoOpen=0):

        self.root = tk.Tk()
        self.root.title("Cam and Keyboard")
        self.root.geometry("1080x520")

        self.video_label = tk.Label(self.root)
        self.video_label.pack(side=tk.LEFT)

        self.key_label = tk.Label(self.root, text="按下的按键: ")
        self.key_label.pack(side=tk.RIGHT)
        
        self.wheel_label = tk.Label(self.root, text=f"send wheel: ", font=("Arial", 18))
        self.wheel_label.place(x=670, y=150)

        self.voice_label = tk.Label(self.root, text=f"voice detect: ", font=("Arial", 18))
        self.voice_label.place(x=670, y=190)

        self.cap = camera.initFrame(cameraType)
        self.capType = cameraType

        self.prediction = multiprocessing.Manager().list(['',False]) # predict, end
        self.lock = multiprocessing.Lock()

        if(arduinoOpen):
            self.client_socket = wheelAct.wheelInit()
        else:
            self.client_socket = None
        self.serialText = ''