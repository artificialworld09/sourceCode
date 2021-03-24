from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def write():
    data = x.get()
    y.set(data)
    x.set("") #to clear e1 after action perform

x = StringVar()
y = StringVar()
e1 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=x)
e1.place(x=10,y=10, width=150,height=28)

e2 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=y)
e2.place(x=10,y=40, width=150,height=28)

b1 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=write).place(x=10,y=70,width=150,height=28)

root.mainloop()