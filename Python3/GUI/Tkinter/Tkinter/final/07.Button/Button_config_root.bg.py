from tkinter import*
root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def red():
    root.config(bg="red")
def green():
    root.config(bg="green")

b1 = Button(root, text="Red", command=red).place(x=10,y=10,width=150,height=28)

b2 = Button(root, text="Green")
b2.place(x=10,y=40,width=150,height=28)
b2.config(command=green)


root.mainloop()