from tkinter import*
root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+20")
root.resizable(False,False)
root.config(bg="#262626")

frame1 = Frame(root,bd=2,relief=RIDGE)
frame1.place(x=250,y=50,width=200,height=300)


## main topic
scroll = Scrollbar(frame1,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)

data = Listbox(frame1,font=("times new roman",20),justify=CENTER,yscrollcommand=scroll.set)
data.pack()
scroll.config(command=data.yview) # to drag and scroll
for i in range(0,101):
    data.insert(i,"Data: "+str(i))


root.mainloop()