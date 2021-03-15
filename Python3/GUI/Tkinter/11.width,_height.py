from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

lbl1 = Label(root,text="No width",font=("times new roman", 15)).place(x=20,y=10)
lbl2 = Label(root,text='width="15"',font=("times new roman", 15), width="15").place(x=20,y=40) #width="15" (approximate 15 charecter)
lbl3 = Label(root,text='width="15",\nheight="2"', font=("times new roman", 15), width="15", height="2").place(x=20,y=70) #height="2" (2 lines)
lbl4 = Label(root,text="newline\nwithout\nwidth&height", font=("times new roman", 15)).place(x=20,y=125)

root.mainloop()