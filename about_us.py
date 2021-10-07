from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("580x600+300+100")
        self.title("About Us")
        self.resizable(False,False)
        

        # :::::::::::::::::::::::::::::::::Icon Image for program::::::::::::::
        icon_APP=PhotoImage(file="user.png")
        self.iconphoto(False,icon_APP)
         #::::::::::::::::::::::::::Make Frames:::::::::::::::::::::::::::
        self.Top_frame=Frame(self,height=600,bg="orange")
        self.Top_frame.pack(fill=BOTH)

        
        self.my_pic=Image.open("user.png")
            #::::resize picture::
        self.resize_pic=self.my_pic.resize((60,80),Image.ANTIALIAS)

            #:::::Create Image::::::::
        self.new_img=ImageTk.PhotoImage(self.resize_pic)

            #:::::::::::Label Image:::::::::::::::::::
        self.label_Image=Label(self.Top_frame,image=self.new_img,bg="orange")
        self.label_Image.place(x=200,y=10)
        # ::::::::::::::::::::::::::::::::
        # :::::::::::::::::::::::button Quit  :::::::::::::::::::::
        self.quit_btn=Button(self.Top_frame,text="Quit",relief=GROOVE,bg="orange",fg="green",font="verdena 11 bold ",command=quit)
        self.quit_btn.place(x=400,y=10)
    
        # :::::::::::::::::::::::::::About us Label:::::::::::::::::::::::::::::
        self.about_us_label=Label(self.Top_frame,text ='''

        We Are Comapny called them self Oussama\nThis company new in Financially thing like the are.\nThe Leader of this Software Company Is Oussama\nhe is A software Engnnier.\nCopyRight 2022 Soon...
        ''',fg="red",bg="orange",font="verdena 14 bold")
        self.about_us_label.place(x=60,y=200)
      
        