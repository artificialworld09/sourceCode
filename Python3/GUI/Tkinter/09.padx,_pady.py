from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

##pady=5 (to give margin up&down)
##padx=5 (to give margin left&right)
lbl1 = Label(root,text='font=("times new roman", 15), bg="white", fg="red"',font=("times new roman", 15), bg="white", fg="red").place(x=20,y=10)
lbl2 = Label(root,text='font=("times new roman", 15), bg="white", fg="red", padx=20',font=("times new roman", 15), bg="white", fg="red", padx=20).place(x=20,y=40)
lbl3 = Label(root,text='font=("times new roman", 15), bg="white", fg="red", padx=20, pady=20)',font=("times new roman", 15), bg="white", fg="red", padx=20, pady=20).place(x=20,y=70)

root.mainloop()