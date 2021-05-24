from tkinter import*
root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

# def show():
#     b1.config(text='Come')

def show():
    b1["text"] = "Hello world!"

b1 = Button(root, text="Go", command=show)
b1.place(x=10,y=40,width=160,height=28)

root.mainloop()