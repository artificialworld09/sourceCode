'''
lbx.place(x=20, y=10)
lbx.place(relwidth=1, relheight=1)
lbx.place(x=20, y=10, width=200, height=300)

lbx.insert(0,"This is index-1")
'''
from tkinter import*
root = Tk()
root.title("Home")
root.config(bg="olivedrab1")
root.geometry("800x400+1820+0")

##basic
lbx = Listbox(root)
lbx.place(x=20, y=10)


##Inserting data into the Listbox
'''
Syntax: (with index)
lbx.insert(index,data)
'''
# lbx.insert(0,"This is index-1")
# lbx.insert(1,"This is index-2")
# lbx.insert(2,"This is index-3")
# lbx.insert(3,"This is index-4")

'''
Syntax: (with loop)
for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))
'''
for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))

root.mainloop()