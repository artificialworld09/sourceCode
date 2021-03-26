from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def show():
    b1["text"] = "Hello world!"
    b1["bg"] = "black"
    b1["fg"] = "white"
    b1["width"] = 30
    b1["height"] = 10

b1 = Button(root, text="Go",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=show)
b1.place(x=10,y=40)

root.mainloop()