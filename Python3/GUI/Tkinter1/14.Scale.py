from tkinter import*
root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+50")
root.resizable(False,False)
root.config(bg="#262626")

## main topic
'''
from_=50,to=250
orient=VERTICAL (default)
orient=HORIZONTAL
width=700 (place.)
length=700
sliderlength=100
showvalue=FALSE
'''

def get_price(price_):
    result.config(text=str(price_))

price = Scale(root,orient=HORIZONTAL,from_=50,to=250,length=700,showvalue=FALSE,command=get_price)
price.place(x=50,y=50)
result = Label(root,bg="#262626",fg="white")
result.place(x=0,y=100,relwidth=1)

root.mainloop()