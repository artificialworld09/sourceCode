from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

##font="fimily", size, "style")
lbl1 = Label(root, text="No font style").place(x=20,y=10)
lbl2 = Label(root,text='font=("times new roman",15)',font=("times new roman",15)).place(x=20,y=35)
lbl3 = Label(root,text='font=("times new roman",15,"bold")',font=("times new roman",15,"bold")).place(x=20,y=65)
lbl4 = Label(root,text='font=("times new roman",25,"bold")',font=("times new roman",25,"bold")).place(x=20,y=95)

root.mainloop()