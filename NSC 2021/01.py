from tkinter import *


root = Tk()
root.title('Ok')



button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()