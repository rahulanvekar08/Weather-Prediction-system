from tkinter import *
from tkinter import messagebox

w=Tk()
#w.geometry('350x500')
w.title(' L O G I N ')
w.geometry("900x500+200+100")
w.resizable(False,False)

global  message;
message=StringVar()

#Making gradient frame
j=0
r=10
for i in range(100):
    c=str(222222+r)
    Frame(w,width=10,height=500,bg="#"+c).place(x=j,y=0)   
    j=j+10                                                  
    r=r+1

f1=Frame(w,width=300,height=400,bg='white')
f1.place(x=500,y=50)


l1=Label(w,text='Welcome Weather Enthusiast!',bg='white')
l=('Verdana',13)
l1.config(font=l)
l1.place(x=520,y=200)

#e1 entry for username entry
e1=Entry(w,width=20,border=0)
l=('Consolas',13)
e1.config(font=l)
e1.place(x=550,y=230)


e2=Entry(w,width=20,border=0,textvariable=message)
e2.config(font=l)
e2.place(x=550,y=310)

l2=Label(w,text='Enter your Name:',bg='white')
l=('Consolas',13)
l2.config(font=l)
l2.place(x=550,y=280)


###lineframe on entry

f=Frame(w,width=180,height=2,bg='#141414')
f.place(x=550,y=332)
#Frame(w,width=180,height=2,bg='#141414').place(x=530,y=252)

from PIL import ImageTk,Image



imagea=Image.open("log.png")
imageb= ImageTk.PhotoImage(imagea)

label1 = Label(image=imageb,
               border=0,
               
               justify=CENTER)


label1.place(x=585, y=50)

def wet():
    w.destroy()
    import trial
    
    

def db():
    w.destroy()
    import dataxyz
    
    

def cmd():
    '''
    label1.destroy()
    l1.destroy()
    e1.destroy()
    e2.destroy()
    l2.destroy()
    myButton1.destroy()
    f.destroy()
    f1.destroy()
    '''

    if message.get():
        for widgets in f1.winfo_children():
            widgets.destroy()
        f.destroy()
        f1.destroy()  
        #Making gradient frame
        j=0
        r=10
        for i in range(100):
            c=str(222222+r)
            Frame(w,width=10,height=500,bg="#"+c).place(x=j,y=0)
            j=j+10
            r=r+1
        Frame(w,width=600,height=400,bg='white').place(x=150,y=50)
        lab1=Label(w,text="",bg='white')
        lab=('Verdana',13)
        lab1.config(font=lab)
        lab1.place(x=520,y=200)

        l=message.get()
        mes="Hello "+l+"\n Would you like to??"

        lab3=('Verdana',20)
        lab2=Label(w,text=mes,bg='white')
        lab2.config(font=lab3)
        lab2.place(x=310,y=100)

        def on_entera(e):
            myButton2['background'] = 'white'#ffcc66
            myButton2['foreground']= '#994422'  #000d33
        def on_leavea(e):
            myButton2['background'] = '#994422'
            myButton2['foreground']='white'
        myButton2 = Button(w,text='C H E C K  W E A T H E R',
                   width=40,
                   height=2,
                   fg='white',
                   border=0,
                   bg='#994422',
                   activeforeground='#994422',
                   activebackground='white',command=wet)

        myButton2.bind("<Enter>", on_entera)
        myButton2.bind("<Leave>", on_leavea)
        myButton2.place(x=300,y=250)

        def on_entera1(e):
            myButton3['background'] = 'white'#ffcc66
            myButton3['foreground']= '#994422'  #000d33
        def on_leavea1(e):
            myButton3['background'] = '#994422'
            myButton3['foreground']='white'
    
        myButton3 = Button(w,text='C O N N E C T  D A T A B A S E',
                   width=40,
                   height=2,
                   fg='white',
                   border=0,
                   bg='#994422',
                   activeforeground='#994422',
                   activebackground='white', command=db)
        myButton3.bind("<Enter>", on_entera1)
        myButton3.bind("<Leave>", on_leavea1)
        myButton3.place(x=300,y=300)
        
    else:
        messagebox.showwarning(title='Warning', message='Please Enter Name!!!')
        
    
    
   

#Button_with hover effect

def on_entera(e):
    myButton1['background'] = 'white'#ffcc66
    myButton1['foreground']= '#994422'  #000d33

def on_leavea(e):
    myButton1['background'] = '#994422'
    myButton1['foreground']='white'

myButton1 = Button(w,text='L O G I N',
                   width=20,
                   height=2,
                   fg='white',
                   border=0,
                   bg='#994422',
                   activeforeground='#994422',
                   activebackground='white',
                       command=cmd)
                  
myButton1.bind("<Enter>", on_entera)
myButton1.bind("<Leave>", on_leavea)

myButton1.place(x=570,y=375)


w.mainloop()

