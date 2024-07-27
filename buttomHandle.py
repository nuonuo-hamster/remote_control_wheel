import tkinter as tk
import yaml

YAML_PATH = "./configs/wheel_speed.yaml"

def write_yaml(name, value):

    # 讀取YAML文件
    with open(YAML_PATH, 'r') as file:
        data = yaml.safe_load(file)

    # 更改的值
    data[name] = value
    
    # 寫回YAML文件
    with open(YAML_PATH, 'w') as file:
        yaml.dump(data, file, default_flow_style=None, sort_keys=False)

def read_yaml(name):

    # 讀取YAML文件
    with open(YAML_PATH, 'r') as file:
        data = yaml.safe_load(file)

    # 取得值
    location = data[name]

    return location

def placeBottomCfg(buttomList):
    buttomList.wheelSpeed_1.place(x=760, y=330, anchor="center")
    buttomList.pulsCtrl_1.place(x=690, y=300)
    buttomList.minusCtrl_1.place(x=790, y=300)

    buttomList.wheelSpeed_2.place(x=760+200, y=330, anchor="center")
    buttomList.pulsCtrl_2.place(x=690+200, y=300)
    buttomList.minusCtrl_2.place(x=790+200, y=300)

    buttomList.wheelSpeed_3.place(x=760, y=330+100, anchor="center")
    buttomList.pulsCtrl_3.place(x=690, y=300+100)
    buttomList.minusCtrl_3.place(x=790, y=300+100)

    buttomList.wheelSpeed_4.place(x=760+200, y=330+100, anchor="center")
    buttomList.pulsCtrl_4.place(x=690+200, y=300+100)
    buttomList.minusCtrl_4.place(x=790+200, y=300+100)

class buttomCfg:
    
    def addLabel(self, tag, value):
        if tag=='LF': 
            self.Speed_1 += value
            if self.Speed_1 >= 120: self.Speed_1 = 120
            self.wheelSpeed_1.config(text=self.Speed_1, font=("Arial", 24))
            write_yaml("wheelLeftFront", self.Speed_1)

        elif tag=='RF':
            self.Speed_2 += value
            if self.Speed_2 >= 120: self.Speed_2 = 120
            self.wheelSpeed_2.config(text=self.Speed_2, font=("Arial", 24))
            write_yaml("wheelRightFront", self.Speed_2)

        elif tag=='LB':
            self.Speed_3 += value
            if self.Speed_3 >= 120: self.Speed_3 = 120
            self.wheelSpeed_3.config(text=self.Speed_3, font=("Arial", 24))
            write_yaml("wheelLeftBehind", self.Speed_3)

        elif tag=='RB':
            self.Speed_4 += value
            if self.Speed_4 >= 120: self.Speed_4 = 120
            self.wheelSpeed_4.config(text=self.Speed_4, font=("Arial", 24))
            write_yaml("wheelRightBehind", self.Speed_4)

    def subLabel(self, tag, value):
        if tag=='LF': 
            self.Speed_1 -= value
            if self.Speed_1 <= 20: self.Speed_1 = 20
            self.wheelSpeed_1.config(text=self.Speed_1, font=("Arial", 24))
            write_yaml("wheelLeftFront", self.Speed_1)

        elif tag=='RF':
            self.Speed_2 -= value
            if self.Speed_2 <= 20: self.Speed_2 = 20
            self.wheelSpeed_2.config(text=self.Speed_2, font=("Arial", 24))
            write_yaml("wheelRightFront", self.Speed_1)

        elif tag=='LB':
            self.Speed_3 -= value
            if self.Speed_3 <= 20: self.Speed_3 = 20
            self.wheelSpeed_3.config(text=self.Speed_3, font=("Arial", 24))
            write_yaml("wheelLeftBehind", self.Speed_3)

        elif tag=='RB':
            self.Speed_4 -= value
            if self.Speed_4 <= 20: self.Speed_4 = 20
            self.wheelSpeed_4.config(text=self.Speed_4, font=("Arial", 24))
            write_yaml("wheelRightBehind", self.Speed_4)
    
    def __init__(self, TKRoot):
        self.Speed_1 = read_yaml("wheelLeftFront")
        self.Speed_2 = read_yaml("wheelRightFront")
        self.Speed_3 = read_yaml("wheelLeftBehind")
        self.Speed_4 = read_yaml("wheelRightBehind")

        self.wheelSpeed_1 = tk.Label(TKRoot.root, text=self.Speed_1, font=("Arial", 24))
        self.wheelSpeed_2 = tk.Label(TKRoot.root, text=self.Speed_2, font=("Arial", 24))
        self.wheelSpeed_3 = tk.Label(TKRoot.root, text=self.Speed_3, font=("Arial", 24))
        self.wheelSpeed_4 = tk.Label(TKRoot.root, text=self.Speed_4, font=("Arial", 24))

        self.pulsCtrl_1 = tk.Button(TKRoot.root, text='+', width=3, height=3, bg = 'green', font=('Arial',12,'bold'),
                    command= lambda: self.addLabel('LF', 1))
        self.minusCtrl_1 = tk.Button(TKRoot.root, text='-', width=3, height=3, bg = 'red', font=('Arial',12,'bold'),
                    command= lambda: self.subLabel('LF', 1))
        self.pulsCtrl_2 = tk.Button(TKRoot.root, text='+', width=3, height=3, bg = 'green', font=('Arial',12,'bold'),
                    command= lambda: self.addLabel('RF', 1))
        self.minusCtrl_2 = tk.Button(TKRoot.root, text='-', width=3, height=3, bg = 'red', font=('Arial',12,'bold'),
                    command= lambda: self.subLabel('RF', 1))
        self.pulsCtrl_3 = tk.Button(TKRoot.root, text='+', width=3, height=3, bg = 'green', font=('Arial',12,'bold'),
                    command= lambda: self.addLabel('LB', 1))
        self.minusCtrl_3 = tk.Button(TKRoot.root, text='-', width=3, height=3, bg = 'red', font=('Arial',12,'bold'),
                    command= lambda: self.subLabel('LB', 1))
        self.pulsCtrl_4 = tk.Button(TKRoot.root, text='+', width=3, height=3, bg = 'green', font=('Arial',12,'bold'),
                    command= lambda: self.addLabel('RB', 1))
        self.minusCtrl_4 = tk.Button(TKRoot.root, text='-', width=3, height=3, bg = 'red', font=('Arial',12,'bold'),
                    command= lambda: self.subLabel('RB', 1))
            