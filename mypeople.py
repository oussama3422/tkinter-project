from tkinter import *
from PIL import ImageTk, Image
# import sqlite3
import datetime
from addpeople import AddPeoaple
from tkinter import messagebox
import  sqlite3
from UpdatePeople import Update
from dispaly import Dispaly

time=datetime.datetime.now().date()
time=str(time)
# con=sqlite3.connect("database.db")
# con.cursor()
conn=sqlite3.connect("database.db")
cur=conn.cursor()
class Mypeople(Toplevel):
    def addpeople(self):
         people=AddPeoaple()
         self.destroy()
    # ::::::::::::::::::::::::::::UPDATE FUNCTION:::::::::::::::::::::::::
    def updateFunction(self):
        selected_Item=self.listBox.curselection()
        people=self.listBox.get(selected_Item)
        person_id=people.split(".")[0]
        # ::::::::::::::::::WE PASS person_id variable With UPADTE CLASS::::::::::::::::::::::
        Update_Page=Update(person_id)

    def DisplayFunc(self):
        selected_Item=self.listBox.curselection()
        people=self.listBox.get(selected_Item)
        person_id=people.split(".")[0]

        Display_Var=Dispaly(person_id)
    def  Delete_Func(self):
        selected_Item=self.listBox.curselection()
        people=self.listBox.get(selected_Item)
        person_id=people.split(".")[0]

        query='DELETE FROM emp Where person_id = "{}" '.format(person_id)
        message=messagebox.askquestion("warning","are you sure you wanna delete ?")
        if message == "yes":
            try:
                cur.execute(query) 
                conn.commit()
                messagebox.showinfo("Success","Employe Has been deleted Successfully")

            except Exception as e:
                messagebox.showerror("Error",str(e))

    

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("580x620+300+100")
        self.title("myPeople")
        self.resizable(False,False)
     

        icon_APP=PhotoImage(file="man.png")
        self.iconphoto(False,icon_APP)


        #::::::::::::::::::::::::::Make Frames:::::::::::::::::::::::::::
        self.Top_frame=Frame(self,height=100,bg="orange")
        self.Top_frame.pack(fill=X)

        self.Bottom_frame=Frame(self,height=500,bg="light blue")
        self.Bottom_frame.pack(fill=X)
        self.my_pic=Image.open("man.png")
        #::::resize picture::
        self.resize_pic=self.my_pic.resize((60,80),Image.ANTIALIAS)

        #:::::Create Image::::::::
        self.new_img=ImageTk.PhotoImage(self.resize_pic)

        #:::::::::::Label Image:::::::::::::::::::
        self.label_Image=Label(self.Top_frame,image=self.new_img)
        self.label_Image.place(x=200,y=10)
        #::::::::::::::Label Text:::::::::::::::::::::
        self.label_Text=Label(self.Top_frame,text='my people',font="verdena 13 bold",bg="orange")
        self.label_Text.place(x=300,y=50)
        #::::::::::::::::::::Label For timing::::::::::::::
        self.label_Time=Label(self.Top_frame,text="date : "+time,font="verdena 12 bold",bg="orange")
        self.label_Time.place(x=437,y=10)

        self.listBox=Listbox(self.Bottom_frame,width=50,height=35)
        self.listBox.grid(row=0,column=0,padx=(10,0),pady=5)
        

        self.scroll_bar=Scrollbar(self.Bottom_frame,orient=VERTICAL)
        self.scroll_bar.grid(row=0,sticky=N+S,column=1)
        # :::::::::::::::::Here in the next Command We Will Linked ScrollBar With ListBox:::::::::::::::

        self.scroll_bar.config(command=self.listBox.yview)
       

        # :::::::::::::::::::::::database::::::::::::::::::::::::::::::::::
        
      
        cur.execute("select * from emp ")
        result=cur.fetchall()
        counter=0
        for i in result:
            self.listBox.insert(counter,str(i[0])+ ". " +i[1]+" "+i[2])
            counter+=1  
         
            
        
        
        
         # :::::::::::::::::Here in the next Command We Will Linked Listbox With ScroolBar:::::::::::::::
        self.listBox.config(yscrollcommand=self.scroll_bar.set)
            


        #::::::::::::::::::Button:::::::::::::::::::::

        # ::::::::::::::::::ADD BUTTON:::::::::::
        self.add_Button=Button(self.Bottom_frame,text="Add",width=10,height=2,bg="#727272",relief=FLAT,command=self.addpeople)
        self.add_Button.grid(row=0,column=2,sticky=N,pady=20,padx=90)
         # ::::::::::::::::::UPDATE BUTTON:::::::::::
        self.update_Button=Button(self.Bottom_frame,text="Update",width=10,height=2,bg="#727272",relief=FLAT,command=self.updateFunction)
        self.update_Button.grid(row=0,column=2,sticky=N,pady=90,padx=90)
         # ::::::::::::::::::DISPLAY BUTTON:::::::::::
        self.Dispaly_Button=Button(self.Bottom_frame,text="Display",width=10,height=2,bg="#727272",relief=FLAT,command=self.DisplayFunc)
        self.Dispaly_Button.grid(row=0,column=2,sticky=N,pady=160,padx=90)
         # ::::::::::::::::::DELETE BUTTON:::::::::::
        self.delete_Button=Button(self.Bottom_frame,text="Delete",width=10,height=2,bg="#727272",relief=FLAT,command=self.Delete_Func)
        self.delete_Button.grid(row=0,column=2,sticky=N,pady=230,padx=90)





        

