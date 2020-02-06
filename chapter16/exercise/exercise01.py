import tkinter

def quit(root):
    root.destroy()


window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Goodbye', command=lambda: quit(window))
button.pack()

window.mainloop()

