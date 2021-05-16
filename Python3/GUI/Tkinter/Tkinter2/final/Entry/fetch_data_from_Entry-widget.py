from tkinter import *
root = Tk()
root.title("Tkinter")
root.geometry("400x500+700+80")
root.config(bg="#262626")
root.resizable(False,False)

##print EntryBox data
def get_name():
    data = e1.get()
    print(data)

def write():
    data = e1.get()
    result.config(text=(data), fg='white')
    print(data)
    en1.set("") #to clear e1 after action perform

en1 = IntVar() #to clear event
e1 = Entry(root, textvariable=en1)
e1.place(x=20,y=10,width=150,height=25)

b1 = Button(root, text="Print", command=get_name).place(x=20,y=40,width=150,height=25)
b2 = Button(root, text="Write", command=write).place(x=20,y=70,width=150,height=25)

result = Label(root, bg='#262626')
result.place(x=20,y=100)

root.mainloop()