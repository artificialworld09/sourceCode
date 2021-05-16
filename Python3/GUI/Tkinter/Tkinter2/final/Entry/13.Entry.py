from tkinter import*
root = Tk()
root.title("Home")
#pt = PhotoImage(file = 'images/css.png')
#root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

# en1 = Entry(root).place(x=20,y=10) #Basic EntryBox

# en1 = Entry(root, font=("times new roman", 15)).place(x=20,y=10) #EntryBox with font

# en2 = Entry(root, font=("times new roman", 15, "bold")).place(x=20,y=40) #with bold style

# en3 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red").place(x=20,y=70) #with bg="yellow", fg="red"

en4 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", show="*").place(x=20,y=100) #to hide text with '*' symbol

root.mainloop()