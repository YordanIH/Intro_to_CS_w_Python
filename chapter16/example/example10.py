import tkinter

window = tkinter.Tk()

# The model.
counter = tkinter.IntVar()
counter.set(0)

#One controller with parameters.
def click(variable, value):
    variable.set(variable.get() + value)

# The views.
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=lambda: click(counter, 1))
button.pack()
button = tkinter.Button(frame, text='Down', command=lambda: click(counter, -1))
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()

window.mainloop()