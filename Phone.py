from tkinter import *
from PIL import ImageTk, Image
import datetime
from mypeople import Mypeople
from addpeople import AddPeoaple
import sqlite3
from about_us import AboutUs


time=datetime.datetime.now().date()
time=str(time)


class PHONEBOOK(object):
    # :::::::::::::::::Function Recursive in mypeople Class::::::::
    def mypeople(self):
            people=Mypeople()
     # ::::::::::::::::Function Recursivlly in addpeople Class::::::::
    def addpeople(self):
         people=AddPeoaple()
    
    def aboutus(self):
        ABOUT_US=AboutUs()
    def __init__(self,root):
        self.root=root
        self.icon_APP=PhotoImage(file="phonebook.png")
        self.root.iconphoto(False,self.icon_APP)


        #::::::::::::::::::::::::::Make Frames:::::::::::::::::::::::::::
        self.Top_frame=Frame(self.root,height=100,bg="orange")
        self.Top_frame.pack(fill=X)

        self.Bottom_frame=Frame(self.root,height=500,bg="light blue")
        self.Bottom_frame.pack(fill=X)

        # self.image=PhotoImage(file='phone.png')
        self.my_pic=Image.open("phone.png")
        #::::resize picture::
        self.resize_pic=self.my_pic.resize((60,80),Image.ANTIALIAS)

        #:::::Create Image::::::::
        self.new_img=ImageTk.PhotoImage(self.resize_pic)

        #:::::::::::Label Image:::::::::::::::::::
        self.label_Image=Label(self.Top_frame,image=self.new_img)
        self.label_Image.place(x=200,y=10)
        #::::::::::::::Label Text:::::::::::::::::::::
        self.label_Text=Label(self.Top_frame,text='my address Book',font="verdena 13 bold",bg="orange")
        self.label_Text.place(x=300,y=50)
        #::::::::::::::::::::Label For timing::::::::::::::
        self.label_Time=Label(self.Top_frame,text="date  : "+time,font="verdena 12 bold",bg="orange")
        self.label_Time.place(x=437,y=10)

        #::::::::::::::The Next Step Inchaalh Is Make Button:::::::::::::::
        
        #::::::::::Add_Button:::::::::::::::::::
        self.photo1=PhotoImage(file="man.png")
        self.photo_image1=self.photo1.subsample(30,30)
        #::::::
        self.add_btn=Button(self.Bottom_frame,text="My People",relief=FLAT,bg="purple",compound=TOP,image=self.photo_image1,width=100,height=40,command=self.mypeople)
        self.add_btn.place(x=260,y=44)
        #:::::::::View_Button::::::::::::::
        self.photo2=PhotoImage(file="add.png")
        self.photo_image2=self.photo2.subsample(30,30)
        # :::::::::::::::
        self.view_Button=Button(self.Bottom_frame,text="Add People",relief=FLAT,compound=TOP,image=self.photo_image2,bg="purple",width=100,height=40,command=self.addpeople)
        self.view_Button.place(x=260,y=100)
        #::::::::::::::About Us Button ::::::::::::::::::::::::::
        self.photo3=PhotoImage(file="information.png")
        self.photo_image3=self.photo3.subsample(30,30)

        self.about_us=Button(self.Bottom_frame,height=40,width=100,text="About Us",compound=TOP,image=self.photo_image3,relief=FLAT,bg="purple",command=self.aboutus)
        self.about_us.place(x=260,y=160)




       
        



def main():
    root=Tk()
    app=PHONEBOOK(root)
    root.geometry("580x600+300+100")
    root.title("PHONE-BOOK")
    root.resizable(False,False)
    root.mainloop()
    






if __name__=="__main__":
    main()