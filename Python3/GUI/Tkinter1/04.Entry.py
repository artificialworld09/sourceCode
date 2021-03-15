from tkinter import *
root = Tk()
root.title("Tkinter")
root.geometry("400x500+700+80")
root.config(bg="#262626")
root.resizable(False,False)

lbl_title = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="red").place(x=0,y=0,relwidth=1)
## main topic
text_Entry = Entry(root,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=0,y=70,relwidth=1)
root.mainloop()