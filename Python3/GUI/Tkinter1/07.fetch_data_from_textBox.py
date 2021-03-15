from tkinter import*
root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+80")
root.config(bg="#262626")
root.resizable(False,False)

def show():
    print(txt_field.get(1.0,END))


## main topic
btn = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="white",cursor="hand2",command=show).place(x=10,y=170,width=130,height=40)

txt_field=Text(root)
txt_field.place(x=10,y=0,width=400,height=150)

root.mainloop()