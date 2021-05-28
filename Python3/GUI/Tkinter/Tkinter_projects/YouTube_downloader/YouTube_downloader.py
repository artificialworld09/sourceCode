from tkinter import *
from tkinter.ttk import Progressbar

root=Tk()
root.title('YouTube Downloader')
root.geometry('780x500')
root.config(bg='olivedrab1')
root.resizable(0, 0)
pt = PhotoImage(file='css.png')
root.iconphoto(False, pt)

########################################Labels############################
introlabel=Label(
    root,
    text='Welcome to YouTube Downloader',
    relief='ridge',
    bd=4,
    font=('Chiller', 30, 'italic bold'),
    fg='red'
).place(x=2, y=20)

downloading_size=Label(
    root,
    text='Total: ',
    font=('arial', 15, 'italic bold'),
    bg='olivedrab1'
)
downloading_size.place(x=525, y=240)

downloading_label=Label(
    root,
    text='Recieved: ',
    font=('arial', 15, 'italic bold'),
    bg='olivedrab1'
)
downloading_label.place(x=525, y=290)

downloading_time=Label(
    root,
    text='Time Left: ',
    font=('arial', 15, 'italic bold'),
    bg='olivedrab1'
)
downloading_time.place(x=525, y=340)

pbl=Label(
    root,
    text='',
    width=36,
    font=('chiller', 40, 'italic bold'),
    fg='red',
    bg='olivedrab1',
    relief='raised')
pbl.place(x=20, y=445)


downloading_size2=Label(
    root,
    text='',
    font=('arial', 15, 'italic bold'),
    bg='olivedrab1'
)
downloading_size2.place(x=650, y=240)

downloading_label2=Label(
    root,
    text='',
    font=('arial', 15, 'italic bold'),
    bg='olivedrab1'
)
downloading_label2.place(x=650, y=290)

downloading_time2=Label(
    root,
    text='',
    font=('arial', 15, 'italic bold'),
    fg='green',
    bg='olivedrab1'
)
downloading_time2.place(x=650, y=340)

downloading=Label(
    root,
    text='Downloading...',
    font=('chiller', 23, 'italic bold'),
    fg='red',
    bg='olivedrab1'
)
downloading.place(x=500, y=445)


########################################Listbox############################
lbx=Listbox(
    root,
    font=('arial', 12, 'italic bold'),
    relief='ridge',
    bd=2,
    highlightcolor='blue',
    highlightbackground='orange',
    highlightthickness=2
)
lbx.place(x=20, y=227, width=500, height=200)

#######################################Scrollbar###########################
scrollbar=Scrollbar(root)
scrollbar.place(x=505, y=230, height=195)

######################################Configure Listbox and Scrollbar####################
lbx.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbx.yview)

######################################Progressbar##########################
progress=Progressbar()

######################################Entry################################
urltxt=StringVar()
url=Entry(
    root,
    font=('arial', 20, 'italic bold'), textvariable=urltxt
)
url.place(x=20, y=150, width=500)

##################################Progressbar############################
pb=Progressbar(
    pbl,
    orient=HORIZONTAL,
    value=0,
    length=100
)
pb.grid(row=0, column=0, ipadx=185, ipady=3)

################################Button###################################
btn=Button(
    root,
    text='Enter url and Click',
    font=('arial', 10, 'italic bold'),
    bg='green',
    fg='red',
    activebackground='blue',
    width=23,
    bd=4,
    #command=VideoUrl
)
btn.place(x=530, y=150)

root.mainloop()


# vid-2: 02:48/46:30