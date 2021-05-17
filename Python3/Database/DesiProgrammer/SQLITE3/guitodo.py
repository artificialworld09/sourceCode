from tkinter import *

root = Tk()
root.title('TODO')
root.geometry('500x600')
root.resizable(0, 0)
root.config(bg='#1d1d1d')

Label(
    root,
    text='Task Manager',
    bg = '#1d1d1d',
    fg = '#eeeeee',
    font=('verdana 20')
).pack()

####################################
frame = Frame(
    root,
    bg='#1d1d1d',
).pack()

en = Entry(
    frame,
    font=('verdana'),
    bg = '#eeeeee',
)

btn = Button(
    frame,
    text = 'ADD TASK',
    # command = add,
    bg = '#000000',
    fg = '#eeeeee',
    relief = 'flat',
    font = ('verdana'),
    highlightcolor = '#000000',
    activebackground = '#1d1d1d',
    bd = 0,
    activeforeground = '#eeeeee'
).pack()

## 14:00/32:29

root.mainloop()