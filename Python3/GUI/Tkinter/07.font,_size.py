from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

lbl = Label(root, text="SoftWaves").place(x=20,y=10)
lbl_title = Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="red").place(x=20,y=32)
lbl = Label(root, text="SoftWaves",font=('C059',15)).place(x=20,y=100) #to change font, size of Label
root.mainloop()