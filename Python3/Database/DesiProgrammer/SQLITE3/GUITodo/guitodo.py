from tkinter import *
import dbhelper3

def add():
    pass

def populate():
    lbx.delete(0, END)
    for rows in dbhelper3.show():
        lbx.insert(END, rows[1])

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
).pack(pady=10)

####################################
frame = Frame(
    root,
    bg='#1d1d1d',
).pack()

en = Entry(
    frame,
    font=('verdana'),
    bg = '#eeeeee',
).pack(ipadx=20, ipady=5, pady=5)

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
).pack(padx=20, ipadx=20, ipady=5)

Label(
    root,
    text='Your Tasks',
    bg='#1d1d1d',
    fg='#eeeeee',
    font=('Calibri', 18)
).pack(pady=10)

taskframe = Frame(
    root,
    # bg='#1d1d1d'
    bg='blue'
)
taskframe.pack(fill=BOTH, expand=300)

scrollbar = Scrollbar(taskframe)
scrollbar.pack(side=RIGHT, fill=Y)

lbx = Listbox(
    taskframe,
    font=('Verdana 18 bold'),
    bg='#1d1d1d',
    fg='#eeeeee'
)
lbx.pack(fill=BOTH, expand=300)
lbx.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbx.yview)

populate()

Label(
    root,
    text='TIP: Double click on a Task to delete',
    bg='#1d1d1d',
    fg='#FFEB3B',
    font=('Calibri 18')
).pack(side=BOTTOM, pady=10)

## 23:00/32:29

root.mainloop()