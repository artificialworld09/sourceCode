from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

c=1
def show(b):
    global c
    c += 1
    if (c%2==0):
        if (b["text"]==""):
            b["text"] = "0"
    else:
        if (b["text"]==""):
            b["text"] = "X"

b1 = Button(root, font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(b1))
b1.place(x=10,y=40)
b2 = Button(root, font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(b2))
b2.place(x=40,y=40)

root.mainloop()