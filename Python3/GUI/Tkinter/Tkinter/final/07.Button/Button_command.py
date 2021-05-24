'''
command=root.destroy: to close the app.
'''

from tkinter import*
root = Tk()

root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def show():
    print("Hello world")
    
b1 = Button(root, text="Print", command=show).place(x=10,y=10,width=150,height=50)
b2 = Button(root, text="Exit", command=root.destroy).place(x=10,y=65,width=150,height=50)

root.mainloop()