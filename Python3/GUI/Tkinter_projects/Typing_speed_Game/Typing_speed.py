from tkinter import *

##########################################################Root_Method################################################
root = Tk()
root.geometry('800x600+400+100')
root.config(bg='powder blue')
root.title('Typing speed Game')
pt = PhotoImage(file = 'css.png')
root.iconphoto(False, pt)

##########################################################Label_Methods################################################
font = Label(
    root,
    text='Welcome to Typing speed Game...',
    font=('arial', 25, 'italic bold'),
    bg='powder blue',
    fg='red'
)
font.place(x=10, y=10)

word = Label(
    root,
    text='Mango',
    font=('arial', 40, 'italic bold'),
    bg='powder blue',
    fg='red'
)
word.place(x=350, y=200)

##########################################################Entry_Methods################################################
wEntry = Entry(
    root,
    font=('arial', 25, 'italic bold'),
    justify='center', #to start typing from center
    bd=5
)
wEntry.place(x=220, y=300)
wEntry.focus_set() #to start typing without click in entrybox

root.mainloop()