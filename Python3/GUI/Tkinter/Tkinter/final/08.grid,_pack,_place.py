'''
There are 3 ways to insert widgets in Tkinter
1. Grid System (Row,Colum,pady,padx,sticky)
grid(row=0,column=1, sticky=W)
sticky=W, E, N, S
columnspan=2

2. Pack (Expand,fill,side)
fill=Y/X (X=Left to Right,  Y=Up to Down)
side=LEFT/RIGHT/BOTTOM/TOP
pack(pady=5) (to give margin up&down)
pack(padx=5) (to give margin left&right)

3. Place (x,y,relwidth,relheight)
x=(Left to Right)
y=(Up to Down)
relwidth=(Left to Right)
relheight=(Top to Down)
place(relwidth=1) (0-1)
'''

from tkinter import*
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

# #-------GRID SYSTEM--------
# lbl = Label(root,text="GRID SYSTEM").grid(row=0,column=0)
# lbl = Label(root,text="GRID SYSTEM").grid(row=1,column=0)
# lbl = Label(root,text="GRID SYSTEM").grid(row=2,column=0)

# #-------Pack SYSTEM--------
## pack(fill=X/fill=Y)


# lbl = Label(root,text="pack(fill=X)").pack(fill=X)
# lbl = Label(root,text="pack(side=LEFT)").pack(side=LEFT)
# lbl = Label(root,text="pack()").pack()

#-------Place SYSTEM--------
lbl = Label(root,text="place(x=0,y=0)").place(x=0,y=0)
lbl = Label(root,text="place(x=400,y=400)").place(x=400,y=300)
lbl = Label(root,text="place(x=200,y=200)").place(x=200,y=200)

root.mainloop()