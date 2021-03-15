from tkinter import *
root = Tk()
root.title("Tkinter")
root.geometry("400x500+700+80")
root.config(bg="#262626")
root.resizable(False,False)

lbl_title = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="red").place(x=0,y=0,relwidth=1)
text_Entry = Entry(root,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
text_Entry.place(x=0,y=70,relwidth=1)
## main topic
def get_name():
    # print(text_Entry.get())
    result.config(text=str(text_Entry.get()))

btn = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="black",activebackground="blue",activeforeground="white",cursor="hand2",command=get_name).place(x=140,y=105,width=130,height=40)
result = Label(root,text="Hello world!",font=("times new roman",20,"bold"),bg="#262626",fg="white")
result.place(x=0,y=200,relwidth=1)
root.mainloop()