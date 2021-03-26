from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def show(op):
    a = x.get()
    b = y.get()
    if (op==1):
        c = a+b
        z.set(c)
    if (op==2):
        c = a-b
        z.set(c)
    if (op==3):
        c = a*b
        z.set(c)

x = IntVar()
y = IntVar()
z = IntVar()

e1 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=x)
e1.place(x=10,y=10, width=150,height=28)

e2 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=y)
e2.place(x=10,y=40, width=150,height=28)

result = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=z)
result.place(  x=10,y=70,width=150,height=28)

b1 = Button(root, text="+",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(1))
b1.place(x=10,y=100,width=28,height=28)

b1 = Button(root, text="-",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(2))
b1.place(x=40,y=100,width=28,height=28)

b1 = Button(root, text="*",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(3))
b1.place(x=70,y=100,width=28,height=28)

root.mainloop()