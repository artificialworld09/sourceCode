from tkinter import*
root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+50")
root.resizable(False,False)

## main topic
'''
There are three modes in Listbox:
1. selectmode=BROWSE (default)
2. selectmode=MULTIPLE
3. selectmode=EXTENDED
'''
## insert and select data
# language = Listbox(root,font=("time new roman",12),bg="#262626",justify=CENTER,selectmode=EXTENDED)
# language.place(x=100,y=50,width=150)

# for i in range(0,20):
#     language.insert(i,"Language: "+str(i))

## BROWSE
# def show():
#     # print(language.get(0)) #to show '0 index's data.
#     get_cursor = language.curselection() #to get cursor selected data.
#     # print(get_cursor) #to show cursor selection index.
#     print(language.get(get_cursor)) #to show cursor selected data.

## MULTIPLE
# def show():
#     get_cursor = language.curselection() #to get all cursor selected data in tuple.
#     # print(get_cursor)
#     for i in get_cursor:
#         print(language.get(i))

## EXTENDED
# def show():
#     get_cursor = language.curselection() #to get all cursor selected data in tuple.
#     # print(get_cursor)
#     for i in get_cursor:
#         print(language.get(i))




## Delete data
language = Listbox(root,font=("time new roman",12),bg="#262626",justify=CENTER,selectmode=BROWSE)
language.place(x=100,y=50,width=150)

for i in range(0,20):
    language.insert(i,"Language: "+str(i))

def show():
    get_cursor = language.curselection() #to get all cursor selected data in tuple.
    language.delete(get_cursor)
    for i in get_cursor:
        print(language.get(i))

btn = Button(root,text="SHOW",font=("times new roman",20,),bg="green",command=show).place(x=100,y=280)

root.mainloop()