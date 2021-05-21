from tkinter import*
root = Tk()
root.title("Home")
# pt = PhotoImage(file = '../images/css.png')
# root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

'''
"<Control_L><y>": to left CTRL+r
"<Control_R><b>": to right CTRL+b
"<Return>": to Enter

'''

def red(r):
    root.config(bg="red")
def yellow(y):
    root.config(bg="yellow")
def blue(b):
    root.config(bg="blue")

l = Label(
    root,
    text = "r to Red\nCtrl+y to Yellow\nCtrl+b to Blue",
    font = ('consolas', 14)
)
l.place(x=20, y=20)

root.bind("r", red)
root.bind("<Return>", yellow)
root.bind("<Control_R><b>", blue)


root.mainloop()