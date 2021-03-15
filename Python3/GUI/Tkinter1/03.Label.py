from tkinter import *
root = Tk()
root.title("Tkinter")
root.geometry("400x500+700+80")
root.config(bg="#262626")
root.resizable(False,False)

lbl_title = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="red").pack(fill=X) #font="fimily",size","style"),bg="color",fg="color"
lbl_title2 = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="yellow",fg="red").pack(fill=X,pady=20) #pack(pady=5) (to give margin up&down)
lbl_title3 = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="yellow",fg="red").pack(fill=X,padx=20,pady=5) #pack(padx=5) (to give margin left&right)
lbl_title4 = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="yellow",fg="red",pady=15).pack(fill=X,padx=20) #pady=5 (to give up&down inside margin)
lbl_title5 = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="yellow",fg="red",pady=15,bd=10,relief=RAISED).pack(fill=X) #bd=10,relief=RAISED (to give border)
## relief=RAISED, SUNKEN, GROOVE
lbl_title6 = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="yellow",fg="red",pady=15,bd=10,relief=RAISED).place(x=150,y=300,height=150,width=300)

root.mainloop()