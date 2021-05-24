'''
lbx.place(x=20, y=10)
lbx.place(relwidth=1, relheight=1)
lbx.place(x=20, y=10, width=200, height=300)

lbx.insert(0,"This is index-1")
lbx.config(yscrollcommand=sbr.set)
sbr.config(command=lbx.yview)

MODES
There are three modes in Listbox:
1. selectmode=BROWSE (default) #to select a single item.
2. selectmode=MULTIPLE #to select multiple items.
3. selectmode=EXTENDED #to select single or multiple items using Ctrl/Shift key.

justify=CENTER: to align list items in center.
get_cursor = lbx.curselection() #to get all cursor selected data in tuple.
'''
from tkinter import*
root = Tk()
root.title("Home")
root.config(bg="olivedrab1")
root.geometry("800x400+1820+0")

lbx = Listbox(root)
lbx.place(x=20, y=10, width=200, height=300)

for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))

##Assigning a Scrollbar
sbr = Scrollbar(root)
sbr.place(x=205, y=12, height=296)

##Configure Listbox and Scrollbar
lbx.config(yscrollcommand=sbr.set)
sbr.config(command=lbx.yview)

def show():
    get_cursor = lbx.curselection() #to get all cursor selected data in tuple.
    for i in get_cursor:
        lbx.delete(get_cursor)

btn = Button(root,text="DELETE", command=show).place(x=20,y=320)

root.mainloop()