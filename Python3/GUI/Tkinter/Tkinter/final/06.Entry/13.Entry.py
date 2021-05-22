'''
.place(x=20, y=20, width=150, height=25)
.place(relwidth=1)
.place(relheight=.5)

font=('times new roman', 15)
font=('times new roman', 15, 'bold')
font=('times new roman', 15, 'italic bold')
bg='yellow'
fg='red'
relief=SUNKEN (SUNKEN, GROOVE, RAISED)
bd=2
width=150, height=200
show="*": to hide text with '*' symbol
'''

from tkinter import*
root = Tk()

root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

en1 = Entry(root, show="$")
en1.place(x=20, y=20)

root.mainloop()