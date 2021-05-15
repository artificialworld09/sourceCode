from tkinter import*
root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+80")
root.resizable(False,False)

## Main topic
def get_data():
    print(chk_var.get())

# chk_var = IntVar()
# chk_var.set(0)
# chk = Checkbutton(root,text="Accept/Not?",onvalue=1,offvalue=0,variable=chk_var,font=("times new roman",20,"bold")).place(x=260,y=150)

chk_var = StringVar()
chk_var.set("Off")
chk = Checkbutton(root,text="Accept/Not?",onvalue="On",offvalue="Off",variable=chk_var,font=("times new roman",20,"bold")).place(x=260,y=150)
btn = Button(root,text="SHOW",font=("times new roman",18,"bold"),bg="lightgray",command=get_data).place(x=260,y=200)

root.mainloop()