from tkinter import *
from tkinter import ttk
from pytube import*
from PIL import Image,ImageTk
import requests
import io

class Youtube_app:
    def __init__(self,root):
        self.root=root
        self.root.title("YouTube Downloader") # to set the title
        self.root.geometry("500x420+300+50") # to set height and width
        self.root.resizable(False,False) # to disable resize window
        self.root.config(bg='white') # to change backgroundcolor

        title=Label(self.root,text=" YouTube Downloader",font=("times new roman",15), bg="#262626",fg="white",anchor="w").pack(side=TOP,fill=X)

        self.var_url = StringVar()
        lbl_url=Label(self.root,text="Video URL",font=("times new roman",15), bg="white").place(x=10,y=50)

        txt_url=Entry(self.root,font=("times new roman",13),textvariable=self.var_url, bg="lightyellow").place(x=120,y=50,width=350)

        lbl_filetype=Label(self.root,text="File Type",font=("times new roman",15), bg="white").place(x=10,y=90)



        self.var_fileType=StringVar()
        self.var_fileType.set("Video")
        video_radio=Radiobutton(self.root,text="Video",variable=self.var_fileType,value="Video",font=("times new roman",15), bg="white",activebackground="white").place(x=120,y=90)

        audio_radio=Radiobutton(self.root,text="Audio",variable=self.var_fileType,value="Audeo",font=("times new roman",15), bg="white",activebackground="white").place(x=220,y=90)



        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15), bg="blue",fg="white").place(x=370,y=90,height=29,width=100)

        frame1=Frame(self.root,bd=2,relief=RIDGE,bg="lightyellow")
        frame1.place(x=10,y=130,width=480,height=180)

        self.video_title=Label(frame1,text="Video Title Here",font=("times new roman",12), bg="lightgray",anchor="w")
        self.video_title.place(x=0,y=0,relwidth=1)

        self.video_image=Label(frame1,text="Video \nImage",font=("times new roman",15), bg="lightgray",bd=2,relief=RIDGE)
        self.video_image.place(x=5,y=30,width=180,height=140)

        lbl_desc=Label(frame1,text="Description",font=("times new roman",15), bg="lightyellow").place(x=190,y=30)

        self.video_desc=Text(frame1,font=("times new roman",12), bg="lightyellow")
        self.video_desc.place(x=190,y=60,width=280,height=110)

        self.lbl_size=Label(self.root,text="Total size: 1525 MB",font=("times new roman",13), bg="white")
        self.lbl_size.place(x=10,y=320)

        self.lbl_percentage=Label(self.root,text="Downloading: 100%",font=("times new roman",13), bg="white")
        self.lbl_percentage.place(x=170,y=320)

        btn_clear=Button(self.root,text="Clear",font=("times new roman",13), bg="gray",fg="white").place(x=320,y=320,height=25,width=70)

        btn_download=Button(self.root,text="Downlaod",font=("times new roman",13), bg="green",fg="white").place(x=400,y=320,height=25,width=90)

        self.prog=ttk.Progressbar(self.root, orient=HORIZONTAL,length=590,mode='determinate')
        self.prog.place(x=10,y=360,width=485,height=20)

        self.lbl_message=Label(self.root,text="Error Messages",font=("times new roman",13), bg="white")
        self.lbl_message.place(x=0,y=385,relwidth=1)

    def search(self):
        url=self.var_url.get()
        yt = YouTube(url)
        video = yt.streams
        video_file=yt.streams.filter(progressive=True).first()
        audio_file=yt.streams.filter(only_audio=True).first()
        thumbnail=yt.thumbnail_url
        ## pip install pillow
        ## pip install requests
        response=requests.get(thumbnail)
        img_byte=io.BytesIO(response.content)
        self.img=Image.open(img_byte)
        self.img=self.img.resize((180,140),Image.ANTIALIAS)
        # self.img=Image.Tk.PhotoImage(self.img)
        self.video_image.config(image=self.img)


        title=yt.title
        desc=yt.description[:200]

        self.video_title.config(text=title)
        self.video_desc.delete('1.0',END)
        self.video_desc.insert(END,desc)


root=Tk()
obj=Youtube_app(root)
root.mainloop()

#3 09:30