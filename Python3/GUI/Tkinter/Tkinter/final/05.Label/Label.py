'''
text='This is a Label'
font=('times new roman', 15),
font=('times new roman', 15, 'bold'),
font=('times new roman', 15, 'italic bold'),
bd=2,
bg='yellow',
fg='red',
padx=20, pady=20,
ipadx=20, ipady=5,
relief=SUNKEN, (SUNKEN, GROOVE)
width=150, height=200,
'''

from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

lbl = Label(root,text="This is a Label")
lbl.place(x=20,y=10)

root.mainloop()