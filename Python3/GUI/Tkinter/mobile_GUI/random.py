import os
os.chdir('/storage/emulated/0/Android/data/ru.iiec.pydroid3/files')

import random

fruits = ['Apple', 'Mango', 'Banana', 'Orange']

def ran():
  a = random.choice(fruits)
  lbl.config(text=a)
  lbl.after(1000, ran)

from tkinter import*
root=Tk()
root.title('Home')
root.geometry('1035x2050')

lbl = Label(
  root,
  text='label-2',
  font=('arial', 20, 'italic bold'),
  bg='orange',
  fg='white'
)
lbl.place(relwidth=1)

ran()

root.mainloop()