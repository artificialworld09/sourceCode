from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

##bd=10,relief=RAISED (to give border)
##relief=RAISED, SUNKEN, GROOVE
lbl1 = Label(root,text='font=("times new roman", 15), bg="white", fg="red", padx=20',font=("times new roman", 15), bg="white", fg="red", padx=20).place(x=20,y=10)
lbl2 = Label(root,text='font=("times new roman", 15), bg="white", fg="red", padx=20, bd=10, relief=RAISED',font=("times new roman", 15), bg="white", fg="red", padx=20, bd=10, relief=RAISED).place(x=20,y=50)
lbl3 = Label(root,text='font=("times new roman", 15), bg="white", fg="red", padx=20, bd=10, relief=SUNKEN',font=("times new roman", 15), bg="white", fg="red", padx=20, bd=10, relief=SUNKEN).place(x=20,y=100)
lbl4 = Label(root,text='font=("times new roman", 15), bg="white", fg="red", padx=20, bd=10, relief=GROOVE',font=("times new roman", 15), bg="white", fg="red", padx=20, bd=10, relief=GROOVE).place(x=20,y=150)

root.mainloop()