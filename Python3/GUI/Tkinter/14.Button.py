from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

b1 = Button(root, text="Show",font=("times new roman",15,"bold")).place(x=10,y=10,width=150,height=50)
b2 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white").place(x=10,y=65,width=150,height=50)
b3 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue").place(x=10,y=120,width=150,height=50)
b4 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red").place(x=10,y=175,width=150,height=50)
b5 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2").place(x=10,y=230,width=150,height=50)

root.mainloop()