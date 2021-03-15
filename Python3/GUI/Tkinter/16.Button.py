from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def show():
    data = e1.get()
    print(data)
def write():
    data = e1.get()
    result.config(text=(data))

e1 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red")
e1.place(x=10,y=10, width=150,height=28)

b1 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=show).place(x=10,y=40,width=150,height=28)

b2 = Button(root, text="Write",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=write).place(x=10,y=70,width=150,height=28)

result = Label(root,font=("times new roman",25,"bold"),bg="#262626",fg="white")
result.place(x=10,y=100)

root.mainloop()