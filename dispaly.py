from tkinter import *
from PIL.Image import ID
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

db=sqlite3.connect("database.db") 
cur=db.cursor()




class Dispaly(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)
        self.geometry("580x600+300+100")
        self.title("Display People")
        self.resizable(False,False)
        

        # ::::::::::::::::::::::::::::UPDATE DATABASE ::::::::::::::::::::
        query="SELECT * FROM emp WHERE person_id ={}".format(person_id)
        cur.execute(query)
        self.person_id=person_id
        result=cur.fetchone()
        first_name=result[1]
        last_name=result[2]
        email_person=result[3]
        phone_person=result[4]
        address_person=result[5]

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




        
        icon_APP=PhotoImage(file="dis.png")
        self.iconphoto(False,icon_APP)


        #::::::::::::::::::::::::::Make Frames:::::::::::::::::::::::::::
        self.Top_frame=Frame(self,height=100,bg="orange")
        self.Top_frame.pack(fill=X)

        self.Bottom_frame=Frame(self,height=500,bg="light blue")
        self.Bottom_frame.pack(fill=X)
        self.my_pic=Image.open("dis.png")
            #::::resize picture::
        self.resize_pic=self.my_pic.resize((60,80),Image.ANTIALIAS)

            #:::::Create Image::::::::
        self.new_img=ImageTk.PhotoImage(self.resize_pic)

            #:::::::::::Label Image:::::::::::::::::::
        self.label_Image=Label(self.Top_frame,image=self.new_img)
        self.label_Image.place(x=200,y=10)
            #::::::::::::::Label Text:::::::::::::::::::::
        self.label_Text=Label(self.Top_frame,text='display people',font="verdena 13 bold",bg="orange")
        self.label_Text.place(x=300,y=50)
        
        #   ::::::::::::::::::;;;Labels::::::::::::::::::::::::::::
        # ::::::::::::::::::::::Name Label:::::::::::::::::::::::::::::::::::
        self.firstNamelabel=Label(self.Bottom_frame,text='First Name',font="verdena 11 bold",bg="orange")
        self.firstNamelabel.place(x=17,y=30)

        self.entry1=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry1.insert(0,first_name)
        self.entry1.config(state="disabled")
        self.entry1.place(x=100,y=30)

         # ::::::::::::::::::::::Last Name Label:::::::::::::::::::::::::::::::::::
        self.lastNamelabel=Label(self.Bottom_frame,text='Last Name',font="verdena 11 bold",bg="orange")
        self.lastNamelabel.place(x=17,y=80)

        self.entry2=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry2.insert(0,last_name)
        self.entry2.config(state="disabled")
        self.entry2.place(x=100,y=80)
        
         # ::::::::::::::::::::::Email Label:::::::::::::::::::::::::::::::::::
        self.Emaillabel=Label(self.Bottom_frame,text='Email',font="verdena 11 bold",bg="orange")
        self.Emaillabel.place(x=44,y=130)

        self.entry3=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry3.insert(0,email_person)
        self.entry3.config(state="disabled")
        self.entry3.place(x=100,y=130)

         # ::::::::::::::::::::::phone Label:::::::::::::::::::::::::::::::::::
        self.phonelabel=Label(self.Bottom_frame,text='Phone No.',font="verdena 11 bold",bg="orange")
        self.phonelabel.place(x=17,y=180)

        self.entry4=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry4.insert(0,phone_person)
        self.entry4.config(state="disabled")
        self.entry4.place(x=100,y=180)

        # ::::::::::::::::::::::Address Label:::::::::::::::::::::::::::::::::::
        self.phonelabel=Label(self.Bottom_frame,text='Adrress',font="verdena 11 bold",bg="orange")
        self.phonelabel.place(x=33,y=230)


        # ::::::::::::::::::::;;;WE HAVE TWO WAY TO DO THIS MESSAGE ENTRY::::::::::::
        # ::::::::::::::::::::::::FIRST:::::::::::::::::::;
        # self.entry5=Entry(self.Bottom_frame,width=40,bd=4)
        # self.entry5.insert(0,"Insert You're Adress")
        # self.entry5.place(x=100,y=230)

        # :::::::::::::::::::::::SECOND WAY:::::::::::::::::::::
        self.entry5=Text(self.Bottom_frame,width=30,bd=4,height=10)
        self.entry5.insert(1.0,address_person)
        self.entry5.config(state="disabled")
        self.entry5.place(x=100,y=250)

  
       