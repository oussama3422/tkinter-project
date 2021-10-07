import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
root = tk.Tk()
def change_i():
    if sound_btn.image == new_img1:
        #start_recording()

        sound_btn.config(image=new_img2)
        sound_btn.image = new_img2
    else:
        #stop_recording()

        sound_btn.config(image=new_img1)
        sound_btn.image = new_img1
# ::::::::::::::::::::::::PICTURE 1::::::::::::::::::::::
my_pic=Image.open("phone.png")
resize_pic=my_pic.resize((60,80),Image.ANTIALIAS)
new_img1=ImageTk.PhotoImage(resize_pic)
#:::::::::::::::::::::::::PICTURE 2::::::::::::::::::::::::
my_pic2=Image.open("phonebook.png")
resize_pic2=my_pic2.resize((60,80),Image.ANTIALIAS)
new_img2=ImageTk.PhotoImage(resize_pic2)





sound_btn = tk.Button(root,text="CLICK",image=new_img1, width=70,height=60,relief=FLAT ,command=change_i )
sound_btn.image = new_img1
sound_btn.grid(row=40, column=10)
root.mainloop()




       