import tkinter

window = tkinter.Tk()

# The model.
counter = tkinter.IntVar()
counter.set(0)

#One controller with parameters.
def click(variable, value):
    variable.set(variable.get()+value)

# Two controllers
def click_up():
    click(counter, 1)
def click_down():
    click(counter, -1)

# The views.
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=click_up)
button.pack()
button = tkinter.Button(frame, text='Down', command=click_down)
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()

window.mainloop()

