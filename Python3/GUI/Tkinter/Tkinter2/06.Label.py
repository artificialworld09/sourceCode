from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = 'images/css.png')
root.iconphoto(False, pt)
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

lbl = Label(root,text="This is a Label").place(x=20,y=10) #to apply a label in Tkinter

root.mainloop()