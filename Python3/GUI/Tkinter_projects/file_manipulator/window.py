from tkinter import*
root = Tk()
root.title("File manipulator")
pt = PhotoImage(file = 'css.png')
root.iconphoto(False, pt)
root.config(bg="olivedrab1")
root.geometry("1080x720+1820+0")
root.minsize(600,300)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.maxsize(width, height)

heading = Label(root, text='File Manipulator', width=36, relief='ridge', bd=4, font=('chiller',40, 'italic bold')).pack()

find = Label(root, text='Find', relief='ridge', bd=4, font=('chiller',16, 'bold'))
find.place(x=10, y=80, width=80, height=40)

e1 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red")
e1.place(x=100,y=80, width=500,height=40)

replace = Label(root, text='Replace', relief='ridge', bd=4, font=('chiller',16, 'bold'))
replace.place(x=10, y=130, width=110, height=40)

e2 = Entry(root, font=('chiller', 16, "bold"), bg="yellow", fg="red")
e2.place(x=130,y=130, width=500,height=40)

b1 = Button(root, text="File rename",font=('chiller', 16, "bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2").place(x=10,y=180,width=160,height=40)

b2 = Button(root, text="Change extension",font=('chiller', 16, "bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2").place(x=10,y=225,width=235,height=40)

b3 = Button(root, text="File manipulation",font=('chiller', 16, "bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2").place(x=10,y=270,width=235,height=40)

b4 = Button(root, text="File name manipulation",font=('chiller', 16, "bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2").place(x=10,y=315,width=300,height=40)

root.mainloop()