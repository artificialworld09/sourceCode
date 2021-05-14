from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'css.png')
root.iconphoto(False, pt)
#root.config(bg="olivedrab1")

##set size of windows
root.geometry("800x400+1820+0")
root.minsize(600,300) #to set minimum size of window
##to set maximum size of window
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.maxsize(width, height)


##Assigning a Listbox
##basic
# lbx = Listbox(
#     root,
#     font=('Verdana', 16)
# )
# lbx.pack()

lbx = Listbox(
    root,
    font=('Verdana', 16)
)
lbx.place(relwidth=1, relheight=1)


##Inserting data into the Listbox
'''
Syntax: (with index)
lbx.insert(index,data)
'''
# lbx.insert(0,"This is index-1")
# lbx.insert(1,"This is index-2")
# lbx.insert(2,"This is index-3")
# lbx.insert(3,"This is index-4")

##Inserting data into the Listbox (with loop)
'''
Syntax:

for i in range(50):
    lbx.insert(i,'This is index-'+str(i))

for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))

for i in range(1,51):
    lbx.insert(i,'This is index-'+str(i))
'''
for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))


##Assigning a Scrollbar(Basic)
# sbr = Scrollbar(
#     root,
# )
# sbr.pack(side=RIGHT, fill='y')

##Assigning a Scrollbar
sbr = Scrollbar(
    root,
)
sbr.pack(side=RIGHT, fill='y')


##configure Scrollbar with Listbox
sbr.config(command=lbx.yview)


##configure Listbox with Scrollbar
lbx.config(yscrollcommand=sbr.set)


root.mainloop()

##09:55/13:17