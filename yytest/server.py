#coding=utf-8
import Tkinter as tk
import ttk
import urllib2

win = tk.Tk()
win.title("TV Check the picture")           # 添加标题

def creatLabel(column, row, columnspan = None, text = None, wraplength = None):
    # 创建一个标签，text：显示表现的内容
    aLabel = ttk.Label(win, text=text, wraplength=wraplength)
    # 显示的列为 column ;行为 row
    aLabel.grid(column=column, row=row, columnspan=columnspan)
    return aLabel

def creatTextBox(column, row):
    nameEntered = ttk.Entry(win, width=12)      # 创建一个文本框，定义长度为12个字符长度
    nameEntered.grid(column=column, row=row)
    return nameEntered

def creatButton(column, row, text, command):
    # 创建一个按钮，text:显示按钮上面显示的文字，command：当这个按钮被点击之后会调用command函数
    action = ttk.Button(win, text = text, command = command)
    action.grid(column = column, row = row)
    return action

def clickMe():          # 当控键被点击时，该函数则生效
    # 获取数据
    vendingid = nameEntered_EquipmentID.get()
    # 修改标签的内容
    aLabel_DataText["text"] = requestData(vendingid)

def requestData(vendingid):
    url_save = "http://store.51efan.com/api/v1/menu/menuPictureList?vendingid=" + vendingid
    with request.urlopen(url_save) as f:
        pictureData = f.read().decode('utf-8')
        print(f.read().decode('utf-8'))
    return pictureData


equipmentIDText = "设备ID："
column_span = None
aLabel_EquipmentID = creatLabel(0, 0, column_span, equipmentIDText)

text = None
wrapLength = 325
aLabel_DataText = creatLabel(0, 1, 3, text, wrapLength)

nameEntered_EquipmentID = creatTextBox(1, 0)

buttonText = "确定"
determineButton = creatButton(2, 0, buttonText, clickMe)

win.mainloop()

