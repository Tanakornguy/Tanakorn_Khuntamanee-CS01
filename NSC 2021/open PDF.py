#นำเข้า tkinter เพื่อสร้าง gui ใน python
#นำเข้า library tkPDFViewer เพื่อวางไฟล์ pdf ใน gui
from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf
import tkinter as tk

#ใส่ title แอพ
root = Tk()
root.title('ข้อสอบ GAT ENG 63')

#ปุ่มออกจากหน้าทำข้อสอบ
button_quit = Button(root, text='Exit Test', command=root.quit)
button_quit.pack()

score = 0

def false():
    root = tk.Tk()
    root.title("test")
    root.minsize(width = 100 , height = 100)
    title_label = tk.Label( master = root , text = ' False ' , font=("SukhumvitSet-SemiBold" , 24))
    title_label.pack()
    root.mainloop()

def true():
    root = tk.Tk()
    root.title("test")
    root.minsize(width = 100 , height = 100)
    title_label = tk.Label( master = root , text = ' True ' , font=("SukhumvitSet-SemiBold" , 24))
    global score 
    score += 1
    title_label.pack()
    root.mainloop()

def end():
    root = tk.Tk()
    root.title("test")
    root.minsize(width = 100 , height = 100)
    title_label = tk.Label( master = root , text = ' score = '+str(score) , font=("SukhumvitSet-SemiBold" , 24))
    title_label.pack()
    root.mainloop()

print("ready")

root = tk.Tk()
root.title("test")
root.minsize(width = 400 , height = 400)

title_label = tk.Label( master = root , text = ' True Or False ' , font=("SukhumvitSet-SemiBold" , 24))
title_label.pack()

ok_button = tk.Button( master = root , text = "One" , command = false)
ok_button.pack()

ok_button = tk.Button( master = root , text = "Two" , command = false)
ok_button.pack()

ok_button = tk.Button( master = root , text = "Three" , command = true )
ok_button.pack()

ok_button = tk.Button( master = root , text = "Four" , command = false)
ok_button.pack()

ok_button = tk.Button( master = root , text = "End" , command = end)
ok_button.pack()

#กำหนดความกว้างและความสูงของหน้าต่างแอพ
root.geometry("1920x1080")

#สร้าง object ที่เอาไว้แสดง PDF 
v1 = pdf.ShowPdf()
#ระบุตำแหน่งไฟล์ PDF และความกว้างและความสูงข้อไฟล์
v2 = v1.pdf_view(root,
                 pdf_location = r"GATEng63E.pdf", 
                 width = 75, height = 50)
v2.pack()

root.mainloop()