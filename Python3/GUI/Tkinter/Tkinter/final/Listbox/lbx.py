from tkinter import*
root = Tk()
root.title("Home")
root.config(bg="olivedrab1")
root.geometry("800x400+1820+0")

class List:
    __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

    def lbx(self, x=10, y=10, w=100, h=200):
        frm = Frame(root, bg='Gray')
        frm.place(x=20, y=10, width=w, height=h)

        nm = Listbox(frm)
        nm.place(relwidth=1, relheight=1)
                      
        sbr = Scrollbar(frm)
        sbr.place(x=w-12, y=2, height=h)

        nm.config(yscrollcommand=sbr.set)
        sbr.config(command=nm.yview)
# l1 = lbx()

l2 = lbx(120, 10, 100, 200)
for i in range(50):
    l2.insert(i,'This is index-'+str(i+1))

root.mainloop()