from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

##bg="color",fg="color"
lbl1 = Label(root,text='font=("times new roman", 15)',font=("times new roman", 15)).place(x=20,y=10)
lbl1 = Label(root,text='font=("times new roman", 15), bg="white"',font=("times new roman", 15), bg="white").place(x=20,y=40)
lbl1 = Label(root,text='font=("times new roman", 15), bg="white", fg="red"',font=("times new roman", 15), bg="white", fg="red").place(x=20,y=70)

root.mainloop()