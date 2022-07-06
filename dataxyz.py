from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText #need to import this for ScrolledText
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import sqlite3


connection= sqlite3.connect("weather.db")
cursor= connection.cursor()

root = Tk()
root.title("Database")
root.geometry("900x500+200+100")
root.resizable(False,False)


def lg():
    
    root.destroy()
    #import loginabc
    
l = Label(root,text="Weather Database",justify="center",font=("poppins",25,"bold"))
l.place(x=50,y=20)




a= "Time\t City\t  Temperature   Pressure   Humidity    Wind\tDescription                "

l1=Label(root,text= a,bg='white')
l=('Verdana',13)
l1.config(font=l)
l1.place(x=40,y=80)

i= 10


f1= tk.Frame(root, width= 810, height= 310)
f1.place(x=40, y=120)

st2= ScrolledText(f1, height=19, width= 98)
st2.place(x=0, y=0)

cursor.execute("SELECT * FROM trial")
for row in cursor:
    b= row[0]+"\t  "+row[1]+"\t\t   "+row[2]+"\t          "+row[3]+"\t        "+row[4]+"\t      "+row[5]+"\t\t\t    "+row[6]+"\n"
    

    '''
    l2 = Label(f1,text=b)
    
    l=('Verdana',13)
    l2.config(font=l)
    l2.place(x=1,y=i)
    i= i+30
    '''
    st2.insert(tk.INSERT, b)
    #l=('Verdana',13)
    #st2.config(font=l)
    #st2.place(x=1,y=i)
    #i= i+30
st2.configure(state ='disabled')    


def get1():
    i= 10
    city=textfield.get().lower()

    for widgets in f1.winfo_children():
      widgets.destroy()

    st3= ScrolledText(f1, height=19, width= 98)
    st3.place(x=0, y=0)

    
    cursor.execute("SELECT * FROM trial where City= ?",(city,))
    for row in cursor:
        b= row[0]+"\t "+row[1]+"\t\t    "+row[2]+"\t          "+row[3]+"\t        "+row[4]+"\t      "+row[5]+"\t\t\t    "+row[6]+"\n"
    
        '''
        l2 = Label(f1,text=b)
        #l=('Verdana',13)
        l2.config(font=l)
        l2.place(x=1,y=i)
        i= i+30
        '''
        st3.insert(tk.INSERT, b)
    st3.configure(state ='disabled')



    
Search_image=PhotoImage(file="search.png")
myimage = Label(image = Search_image)
myimage.place(x=400,y=0)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=440,y=20)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon = Button(image = Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=get1)
myimage_icon.place(x=780,y=13)



def on_entera(e):
    myButton2['background'] = 'white'#ffcc66
    myButton2['foreground']= '#F1C40F'  
def on_leavea(e):
    myButton2['background'] = '#F1C40F'
    myButton2['foreground']='white'


    
myButton2 = Button(root,text='E X I T',
                   width=15,
                   height=2,
                   fg='white',
                   border=0,
                   bg='#F1C40F',
                   activeforeground='#994422',
                   activebackground='white',command= lg)
myButton2.bind("<Enter>", on_entera)
myButton2.bind("<Leave>", on_leavea)
myButton2.place(x=400,y=450)

connection.commit()
root.mainloop()
