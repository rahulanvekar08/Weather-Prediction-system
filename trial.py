from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import sqlite3


connection= sqlite3.connect("weather.db")
cursor= connection.cursor()

#cursor.execute("drop table trial")

q1= '''CREATE TABLE if not exists trial(
        Time text,
        City text,
        Temperature text,
        pressure text,
        humidity text,
        wind text,
        description text);'''
cursor.execute(q1)

root = Tk()
root.title("Weather Application")
root.geometry("900x500+200+100")
root.resizable(False,False)

def getWeather():
    
    city=textfield.get().lower()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4647637b5be210234574483616f9c3da"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]['main']
    description = json_data["weather"][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°",))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    w.config(text= wind)
    h.config(text= humidity)
    d.config(text= description)
    p.config(text= pressure)

    cursor.execute("INSERT into trial VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(current_time, city, temp,pressure,humidity,wind,description))

    connection.commit()

    
    
    
                   
                

    

l = Label(root,text="Weather Prediction System",justify="center",font=("poppins",25,"bold"))
l.place(x=230,y=20)


#search box
Search_image=PhotoImage(file="search.png")
myimage = Label(image = Search_image)
myimage.place(x=210,y=80)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=250,y=100)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon = Button(image = Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=590,y=93)

#logo
Logo_image=PhotoImage(file="logo.png")
logo = Label(image = Logo_image)
logo.place(x=30,y=150)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage = Label(image = Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=300,y=170)
clock=Label(root,font=("Helvetica",20))
clock.place(x=300,y=210)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=400,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t= Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=600,y=250)
c=Label(font=("arial",15,"bold"))
c.place(x=600,y=350)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=250,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=400,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=650,y=430)


def on_entera(e):
    myButton2['background'] = 'white'#ffcc66
    myButton2['foreground']= '#F1C40F'  
def on_leavea(e):
    myButton2['background'] = '#F1C40F'
    myButton2['foreground']='white'

def wet1():
    root.destroy()
    import loginabc

    
myButton2 = Button(root,text='B A C K',
                   width=15,
                   height=2,
                   fg='white',
                   border=0,
                   bg='#F1C40F',
                   activeforeground='#994422',
                   activebackground='white',command= wet1)
myButton2.bind("<Enter>", on_entera)
myButton2.bind("<Leave>", on_leavea)
myButton2.place(x=700,y=100)

connection.commit()
root.mainloop()
