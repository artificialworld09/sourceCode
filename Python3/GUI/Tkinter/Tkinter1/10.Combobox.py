from tkinter import*
from tkinter import ttk
root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+80")
root.resizable(False,False)

## main topic
def get_data():
    print(language.get())

## You can't change fg and bg color in comboBox property
'''
state="readonly": to disable type property.
justify=CENTER: to centerized selected item.
language.current(0): to select "2 index's item" by default.
language.set("Select languages"): to give 'select languages' hints.
'''
language = ttk.Combobox(root,values=("HTML","CSS","PHP","Python","Flask"),font=("times new roman",20,"bold"),state="readonly",justify=CENTER)
language.place(x=100,y=50,width=200,height=25)
language.current(2) #to select "2 index's item" by default.
language.set("Select languages") #to give 'select languages' hints.

btn = Button(root, text="SHOW",command=get_data).place(x=100,y=100)

root.mainloop()