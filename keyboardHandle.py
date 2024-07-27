import keyboard

def trigger(TKRoot, KBhandle):
    # key = keyboard.read_key()
    # TKRoot.key_label.config(text=f"按下的按键: {key}")
    # hotkey = keyboard.get_hotkey_name()
    # if hotkey:
    #     TKRoot.key_label.config(text=f'组合键 {hotkey} 同时被按下')
    key = keyboard.get_hotkey_name()
    keys = key.split('+')
    TKRoot.key_label.config(text=f'KEYBOARD: '+ ",".join(keys)+' '*10)
    
    if key == 'esc':  # 当按下 'esc' 键时退出循环
        TKRoot.root.quit()

    for key in keys:
        for idex, ListKey in enumerate(KBhandle.ctlList):
            
            if ListKey == key and key not in KBhandle.keysInLabel:
                KBhandle.keysInLabel.append(key)
                if idex <= 5:
                    KBhandle.labelArr[idex].config(text=f"{key.upper()}", font=("Arial", 20), fg='red')
                    # KBhandle.labelArr[idex] = tk.Label(TKRoot.root, text=f"{key.upper()}", font=("Arial", 24), fg='red')
                    # KBhandle.labelArr[idex].place(x=KBhandle.labelPlaceX[idex], y=KBhandle.labelPlaceY[idex])
                break
    
    for pressedKey in KBhandle.keysInLabel: 
        if pressedKey not in keys:
            KBhandle.keysInLabel.remove(pressedKey)
            index = KBhandle.ctlList.index(pressedKey)
            if index <= 5:
                KBhandle.labelArr[index].config(text=f"{pressedKey.upper()}", font=("Arial", 24), fg='black')
            # KBhandle.labelArr[KBhandle.ctlList.index(pressedKey)].destroy()

    # if 'q' in keys and 'q' not in KBhandle.arr:
    #     KBhandle.arr.append('q')
    #     KBhandle.labelArr[0] = tk.Label(TKRoot.root, text=f"{KBhandle.arr}", font=("Arial", 16))
    #     KBhandle.labelArr[0].place(x=600, y=50)
    #     # KBhandle.label = tk.Label(TKRoot.root, text=f"{KBhandle.arr}", font=("Arial", 16))
    #     # KBhandle.label.pack()
    # if 'q' not in keys and 'q' in KBhandle.arr:
    #     KBhandle.labelArr[0].destroy()
    #     KBhandle.arr.remove('q')
        
class keyBoardInfo:
    def __init__(self):
        self.ctlList = ['q','w','e','a','s','d', 'plus', '+', '-']
        self.keysInLabel = []
        self.labelArr = [None]*6
        self.labelPlaceX = [750,850,950,750,850,950]
        self.labelPlaceY = [ 50, 50, 50,100,100,100]
