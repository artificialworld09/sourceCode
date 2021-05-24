from tkinter import*
root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def show():
    b1["text"] = "Hello world!"
    b1["bg"] = "black"
    b1["fg"] = "white"
    b1["width"] = 30
    b1["height"] = 10

b1 = Button(root, text="Go", command=show)
b1.place(x=10,y=40)

root.mainloop()