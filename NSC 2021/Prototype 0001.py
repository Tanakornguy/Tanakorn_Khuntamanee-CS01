#นำเข้า tkinter เพื่อสร้าง gui ใน python
#นำเข้า library tkPDFViewer เพื่อวางไฟล์ pdf ใน gui
from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf

#ใส่ title แอพ
root = Tk()
root.title('ข้อสอบ GAT ENG 63')

#ปุ่มออกจากหน้าทำข้อสอบ
button_quit = Button(root, text='Exit Test', command=root.quit)
button_quit.pack()

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