import cv2
import threading

import camera
import wheelAct
import buttomHandle
import voiceHandle
from keyboardHandle import keyBoardInfo
from voice_translation import detect_voiceV2
from TKEssential import*

class WindowHandler:
    def __init__(self):
        self.TKRoot = TKInfo(cameraType='webcam' ,arduinoOpen=0)
        self.KBhandle = keyBoardInfo()
        self.ButtomList = buttomHandle.buttomCfg(self.TKRoot)

def main():
    
    windowHandler = WindowHandler()
    TKRoot = windowHandler.TKRoot

    # 1.keyboard detect
    put_keyboard_label(windowHandler)
    keyboard_thread = threading.Thread(target=detect_keyboard_input, args=(windowHandler,) ,daemon=True)
    keyboard_thread.start()

    # 2.cam
    update_frame(TKRoot)

    # 3.speech to instruction
    voiceProcess = multiprocessing.Process(target=detect_voiceV2.main, args=(TKRoot.prediction, TKRoot.lock))
    voiceProcess.start()
    voice_thread = threading.Thread(target=voiceHandle.voice_detect, args=(windowHandler,) ,daemon=True)
    voice_thread.start()
    
    # 3. buttom
    buttomList = windowHandler.ButtomList
    buttomHandle.placeBottomCfg(buttomList)

    # TK loop
    TKRoot.root.mainloop()

    # end
    TKRoot.prediction[1] = True
    voiceProcess.join()
    if(TKRoot.capType=='realsense'): camera.capRelease(TKRoot.cap)
    wheelAct.closeClient(TKRoot.client_socket)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()