from tkinter import *
from datetime import datetime

root = Tk()
root.title('Time')

def update_time():
    format = '%H:%M:%S'
    now = (datetime.now()).strftime(format)
    s2 = '7:23:25'
    str = datetime.strptime(s2, format) - datetime.strptime(now, format)
    print(str)

l = Label(root, font=('calibri',50))
l.pack()

update_time()