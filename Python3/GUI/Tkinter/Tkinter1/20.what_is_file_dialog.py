from tkinter import*
from tkinter import filedialog

root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+20")
root.resizable(False,False)
root.config(bg="#262626")

def open():
    op = filedialog.asksaveasfile(title="Select file",filetypes=(("text file",".txt"),("all files","*"))) #to open popup window to save file.
    print(op) 

"""
## filedialog
op = filedialog.askdirectory(title="Select folder") #to open popup window to select any folder.

op = filedialog.askopenfile(title="Select file") #to open popup window to select any file in object format.

op = filedialog.askopenfile(title="Select file") #to open popup window to select any file in object format.
print(op.name) #to fetch only file path.

op = filedialog.askopenfilename(title="Select file") #to open popup window to select any file.

op = filedialog.askopenfilename(title="Select file") #to open popup window to select any file.
print(op.split("/")[-1]) #to split only file name.

op = filedialog.askopenfilenames(title="Select file") #to open popup window to select multiple files.

op = filedialog.askopenfiles(title="Select file") #to open popup window to select multiple files in object format.

op = filedialog.asksaveasfile(title="Select file") #to open popup window to save file.

op = filedialog.asksaveasfile(title="Select file",filetypes=(("text file",".txt"),("all files","*"))) #to open popup window to save file with availabled extensions.

op = filedialog.asksaveasfilename(title="Select file",filetypes=(("text file",".txt"),("all files","*"))) #to open popup window to save file.

10:00
"""
btn = Button(root,text="fileDialog",command=open).place(x=50,y=50)

root.mainloop()