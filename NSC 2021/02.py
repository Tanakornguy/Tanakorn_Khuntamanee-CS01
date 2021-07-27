
from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf

root = Tk()
root.title('Ok')



button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()


# Set the width and height of our root window.
root.geometry("1000x850")
  
# creating object of ShowPdf from tkPDFViewer.
v1 = pdf.ShowPdf()
  
# Adding pdf location and width and height.
v2 = v1.pdf_view(root,
                 pdf_location = r"GATEng63E.pdf", 
                 width = 75, height = 50)
  
# Placing Pdf in my gui.
v2.pack()
root.mainloop()



