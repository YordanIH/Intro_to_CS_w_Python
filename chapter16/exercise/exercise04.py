import tkinter



def count(text, output):
    data = text.get('0.0', tkinter.END)
    count={}
    for char in 'ATCG':
        count[char]=data.count(char)
    output.set('Num As: {0} Num Ts: {1} Num Cs {2} Num Gs: {3}'.format(count['A'],count['T'],count['C'],count['G']))

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
output = tkinter.StringVar()
text = tkinter.Text(window, height=10, width=40)
text.pack()
button = tkinter.Button(window, text = 'Count', command = lambda: count(text, output))
button.pack()

label = tkinter.Label(window, textvar = output)
label.pack()

window.mainloop()