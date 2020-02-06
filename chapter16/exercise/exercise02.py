import tkinter

window = tkinter.Tk()

counter = tkinter.IntVar()
counter.set(0)

def click(var):
    var.set(var.get() + 1)

frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, textvariable = counter, command=lambda: click(counter))
button.pack()

window.mainloop()