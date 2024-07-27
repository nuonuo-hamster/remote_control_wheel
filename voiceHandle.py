# from voice_translation import detect_voice
import wheelAct

def voice_detect(windowHandler):
    TKRoot = windowHandler.TKRoot
    oldPrediction = None
    opcode = 'p'
    while True:
        if(TKRoot.prediction[0] != oldPrediction):
            oldPrediction = TKRoot.prediction[0]
            # print(TKRoot.prediction[0])
            
            if(TKRoot.prediction[0] == 'background'): opcode = None
            if(TKRoot.prediction[0] == 'stop'): opcode = 'p'
            if(TKRoot.prediction[0] == 'forward'): opcode = 'w'
            if(TKRoot.prediction[0] == 'shiftLeft'): opcode = 'a'
            if(TKRoot.prediction[0] == 'backward'): opcode = 's'
            if(TKRoot.prediction[0] == 'shiftRight'): opcode = 'd'
            if(TKRoot.prediction[0] == 'turnLeft'): opcode = 'q'
            if(TKRoot.prediction[0] == 'turnRight'): opcode = 'e'
            if(TKRoot.prediction[0] == 'speedUp'): opcode = '+'
            if(TKRoot.prediction[0] == 'slowDown'): opcode = '-'
            
            if(opcode == None):
                TKRoot.voice_label.config(text=f'voice detect:  background')
            elif(opcode == '+' or opcode == '-'):
                TKRoot.voice_label.config(text=f'voice detect:  {opcode} ({TKRoot.prediction[0]})')
                # wheelAct.generateSerialText(opcode, windowHandler.ButtomList)
                if opcode == '+' or opcode == 'plus':
                    windowHandler.ButtomList.addLabel('LF', 10)
                    windowHandler.ButtomList.addLabel('RF', 10)
                    windowHandler.ButtomList.addLabel('LB', 10)
                    windowHandler.ButtomList.addLabel('RB', 10)
                elif opcode == '-':
                    windowHandler.ButtomList.subLabel('LF', 10)
                    windowHandler.ButtomList.subLabel('RF', 10)
                    windowHandler.ButtomList.subLabel('LB', 10)
                    windowHandler.ButtomList.subLabel('RB', 10)
            else:
                TKRoot.voice_label.config(text=f'voice detect:  {opcode.upper()} ({TKRoot.prediction[0]})')
                text = wheelAct.generateSerialText(opcode, windowHandler.ButtomList)
                wheelAct.serialSendText(TKRoot, text)
                TKRoot.wheel_label.config(text=f'wheel send: {text}', fg='blue')
                    