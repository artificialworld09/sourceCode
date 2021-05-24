'''
.place(x=20, y=20, width=70, height=25)
.place(relwidth=1)
.place(relheight=.5)

text='This is a Label'
text='newline\nwithout\nwidth&height'

#font="fimily", size, "style")
font=('times new roman', 15)
font=('times new roman', 15, 'bold')
font=('times new roman', 15, 'italic bold')

bg='yellow': Background-color
fg='red': Foreground-color
padx=20: (to give margin left&right)
pady=20: (to give margin up&down)

relief=SUNKEN (SUNKEN, GROOVE, RAISED)
bd=2: (to give border)

activebackground="black": on hover
activeforeground="white": on hover
cursor="hand2": (hand1, hand2)
'''

from tkinter import*
root = Tk()

root.title("Home")
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

btn = Button(root, text='Show', activebackground="black", activeforeground="white", cursor="hand2")
btn.place(x=20, y=20)

root.mainloop()