import tkinter



def convert(out_data, temp_data):
    f=temp_data.get()
    out_data.set((f - 32) * 5/9)

def quit(root):
    root.destroy()

window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

out_data = tkinter.StringVar()
temp_data = tkinter.DoubleVar()

label = tkinter.Label(window, text = 'Temperature in Fahrenheit:')
label.pack()

text = tkinter.Entry(window, textvar = temp_data)
text.pack()

label = tkinter.Label(window, textvar = out_data)
label.pack()

button = tkinter.Button(window, text = 'Convert', command = lambda: convert(out_data, temp_data))
button.pack()

button = tkinter.Button(window, text = 'Quit', command= lambda: quit(window))
button.pack()



window.mainloop()