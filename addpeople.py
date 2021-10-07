from os import terminal_size
from tkinter import *
from typing import Sized
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
class AddPeoaple(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("580x600+300+100")
        self.title("Add New People")
        self.resizable(False,False)
     

        icon_APP=PhotoImage(file="add.png")
        self.iconphoto(False,icon_APP)


        #::::::::::::::::::::::::::Make Frames:::::::::::::::::::::::::::
        self.Top_frame=Frame(self,height=100,bg="orange")
        self.Top_frame.pack(fill=X)

        self.Bottom_frame=Frame(self,height=500,bg="light blue")
        self.Bottom_frame.pack(fill=X)
        self.my_pic=Image.open("add.png")
            #::::resize picture::
        self.resize_pic=self.my_pic.resize((60,80),Image.ANTIALIAS)

            #:::::Create Image::::::::
        self.new_img=ImageTk.PhotoImage(self.resize_pic)

            #:::::::::::Label Image:::::::::::::::::::
        self.label_Image=Label(self.Top_frame,image=self.new_img)
        self.label_Image.place(x=200,y=10)
            #::::::::::::::Label Text:::::::::::::::::::::
        self.label_Text=Label(self.Top_frame,text='Add New people',font="verdena 13 bold",bg="orange")
        self.label_Text.place(x=300,y=50)
        
        #   ::::::::::::::::::;;;Labels::::::::::::::::::::::::::::
        # ::::::::::::::::::::::Name Label:::::::::::::::::::::::::::::::::::
        self.firstNamelabel=Label(self.Bottom_frame,text='First Name',font="verdena 11 bold",bg="orange")
        self.firstNamelabel.place(x=17,y=30)

        self.entry1=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry1.insert(0,"Insert You're first Name")
        self.entry1.place(x=100,y=30)

         # ::::::::::::::::::::::Last Name Label:::::::::::::::::::::::::::::::::::
        self.lastNamelabel=Label(self.Bottom_frame,text='Last Name',font="verdena 11 bold",bg="orange")
        self.lastNamelabel.place(x=17,y=80)

        self.entry2=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry2.insert(0,"Insert You're Last Name")
        self.entry2.place(x=100,y=80)
        
         # ::::::::::::::::::::::Email Label:::::::::::::::::::::::::::::::::::
        self.Emaillabel=Label(self.Bottom_frame,text='Email',font="verdena 11 bold",bg="orange")
        self.Emaillabel.place(x=44,y=130)

        self.entry3=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry3.insert(0,"Insert You're Email")
        self.entry3.place(x=100,y=130)

         # ::::::::::::::::::::::phone Label:::::::::::::::::::::::::::::::::::
        self.phonelabel=Label(self.Bottom_frame,text='Phone No.',font="verdena 11 bold",bg="orange")
        self.phonelabel.place(x=17,y=180)

        self.entry4=Entry(self.Bottom_frame,width=40,bd=4)
        self.entry4.insert(0,"Insert You're Phone")
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
        self.entry5.place(x=100,y=250)

        # ::::::::::::::::::::::::::::::::::Button Button:::::::::::::::::::::::::
        add=Button(self.Bottom_frame,text="Add person",bg="#227272",width=20,bd=10,relief=FLAT,command=self.Add)
        add.place(x=150,y=450)
                
    def Add(self):
    
        db=sqlite3.connect("database.db") 
        cur=db.cursor()   

        firstname=self.entry1.get()
        lastname=self.entry2.get()
        email=self.entry3.get()
        phone=self.entry4.get()
        address=self.entry5.get(1.0, 'end-1c')
        if firstname and lastname and email and phone and address !="":

            try:
                # query="CREATE TABLE EMPLOYEE (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),Email CHAR(100), Phone INT,Address CHAR(100) )"
                query2="INSERT INTO emp(fname,lname,email,ph,addrrss)values(?,?,?,?,?)"
                val=(firstname,lastname,email,phone,address)
                cur.execute(query2,val)
                db.commit()
                cur.fetchall()
                messagebox.showinfo("Success","The info Added Successfully!!")
               
            except Exception as e:
                messagebox.showerror("Error",str(e))

            db.close()
               

        else:
            messagebox.showerror("Error","Fill All the Field",icon="error")

         



