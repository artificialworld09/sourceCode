from tkinter import*
root = Tk()
root.title("Tkinter")
root.geometry("1100x600+150+20")
root.resizable(False,False)
root.config(bg="#262626")

"""
Types of Frames:- 
Frame
LabelFrame
"""
## Frame
window1 = Frame(root,bg="lightgray",bd=10,relief=GROOVE)
window1.place(x=50,y=50,width=450,height=340)

show = Button(window1,text="SHOW").place(x=50,y=50)
show = Button(window1,text="SHOW").place(x=250,y=50)
show = Button(window1,text="SHOW").place(x=50,y=150)

## LabelFrame
window2 = LabelFrame(root,text="StudentDetails",bg="lightgray",bd=10,relief=GROOVE)
window2.place(x=550,y=50,width=450,height=340)

root.mainloop()