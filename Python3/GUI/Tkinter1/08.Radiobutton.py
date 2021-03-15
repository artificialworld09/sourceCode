from tkinter import*
root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+80")
root.config(bg="#262626")
root.resizable(False,False)

##main topic
def gender_func():
    print(gender.get())

gender = Label(root,text="SELECT GENDER: ",font=("times new roman",20,"bold"),bg="#262626",fg="white").place(x=100,y=50)

gender = StringVar()
gender.set("male")
male = Radiobutton(root,text="Male",value="male",variable=gender,font=("times new roman",18,"bold"),bg="#262626",fg="white").place(x=100,y=100)
female = Radiobutton(root,text="Female",value="female",variable=gender,font=("times new roman",18,"bold"),bg="#262626",fg="white").place(x=220,y=100)

btn = Button(root,text="SHOW",font=("times new roman",18,"bold"),command=gender_func).place(x=100,y=150)

root.mainloop()
 
# 08. 6:10