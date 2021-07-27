import tkinter as tk

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

root.mainloop()