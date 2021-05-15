from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+50")
root.config(bg="#262626")
root.resizable(False,False)

## main topic
"""
showerror
showinfo
showwarning
"""
def message():
    messagebox.showerror("Error","This is an error messageBox...")
def message2():
    messagebox.showinfo("Information","This is an information messageBox...")
def message3():
    messagebox.showwarning("Warning","This is a warning messageBox...")
btn1 = Button(root,text="Message1",command=message).place(x=50,y=50,width=100,height=40)
btn2 = Button(root,text="Message2",command=message2).place(x=160,y=50,width=100,height=40)
btn3 = Button(root,text="Message3",command=message3).place(x=270,y=50,width=100,height=40)

root.mainloop()