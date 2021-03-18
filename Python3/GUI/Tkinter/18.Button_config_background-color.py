from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def red():
    root.config(bg="red")
def green():
    root.config(bg="green")

b1 = Button(root, text="Red",font=("times new roman",15,"bold"),bg="red",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=red).place(x=10,y=40,width=150,height=28)

b2 = Button(root, text="Green",font=("times new roman",15,"bold"),bg="green",fg="white",activebackground="blue",activeforeground="red",cursor="hand2")
b2.config(command=green)
b2.place(x=10,y=70,width=150,height=28)


root.mainloop()