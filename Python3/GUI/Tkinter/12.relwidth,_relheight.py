from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

# X=Left to Right,Y=Up to Down) place(relwidth=1) (0-1)
lbl1 = Label(root,text="No relwidth",font=("times new roman", 15)).place(x=0,y=10)
lbl1 = Label(root,text='.place(x=0, y=40, relwidth=1)', font=("times new roman", 15)).place(x=0, y=40, relwidth=1)
lbl1 = Label(root,text='.place(x=0, y=70, relheight=.5)', font=("times new roman", 15)).place(x=0, y=70, relheight=.5)

root.mainloop()