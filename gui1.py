

import os
import sqlite3
from tkinter import *
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk


#initial setup
root=Tk()
root.title('ASAP-LOGIN V-1.0.0'.center(400))
root.iconbitmap('F:/tkn/final-project/logo.ico')
root.configure(background='#DDC9FF')
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#setting tkinter root size
root.geometry("%dx%d" % (width, height))
root.resizable(True,False)
# root.maxsize(height=700,width=900)
# root.minsize(height=700,width=900)
# root.geometry('900x700')

frame1=Frame(root,bg='#DDC9FF')
frame2=Frame(root,bg='#DDC9FF')
frame3=Frame(root,bg='#DDC9FF')
for frame in (frame1, frame2, frame3):
    frame.grid(row=1,column=1,sticky='nsew',pady=10,padx=10)

def show_frame(frame):
    frame.tkraise()

show_frame(frame1)


#image
myimag=(Image.open('F:/tkn/final-project/pooza.png'))
ok=myimag.resize((250,290))
conimg=ImageTk.PhotoImage(ok)
my_label=Label(frame1,image=conimg,bg='#DDC9FF')
my_label.grid(row=0,column=0,columnspan=1,pady=(300,0),padx=(380,10))
img1=PhotoImage(file='F:/tkn/final-project/rec.png')

#Entry
frame=LabelFrame(frame1,padx=25,pady=10,highlightbackground="black", highlightthickness=3,background='white',border=0)
frame.grid(row=0,column=2,pady=(195,0))
signup=Label(frame, text='Cashier Login',bg='white',font='{Tw cen mt} 25 bold')#rockwell #Tw Cen MT #condensed #century gothic
signup.grid(row=0,column=0,sticky=W)
name=Label(frame,text="Username",bg='white',justify='right',font='{Tw cen mt} 15')
name.grid(row=1,column=0,sticky=W,pady=(5,0))

#img for entry#inside try
img=PhotoImage(file='F:/tkn/final-project/rec.png')
img_open=PhotoImage(file='F:/tkn/final-project/open.png')
img_close=PhotoImage(file='F:/tkn/final-project/close.png')
#entry1
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=2,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e3=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e3.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))




passWord=Label(frame,text="Password",bg='white',justify='right',font='{Tw cen mt} 15',anchor=W)
passWord.grid(row=3,column=0,sticky=W)



a=0
def showpass():
    global a
    a=a+1
    if a%2==0:
        e2.config(show='*')
        showPass.config(image=img_close)
    else:
        e2.config(show='')
        showPass.config(image=img_open)





fm=Frame(frame,border=0,relief='solid')
fm.grid(row=4,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e2=Entry(fm,border=0,width=22,relief="solid",font=50,background='white',show='*')
e2.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))
showPass=Button(fm,image=img_close,bg='white',relief='solid',cursor='hand2',activebackground='white',border=0,command=showpass)
showPass.grid(row=0,column=1,sticky=W,pady=(0,17))


btn_frame=Frame(frame,width=241,height=50,background='#BFBFBF')
btn_frame.place(x=20,y=269)

#btn
def login1():
    if e3.get()=='' or e2.get()=='' :
        messagebox.showwarning('Failed!!','Please enter all fields!!')
    else:
        try:
            cen=sqlite3.connect('F:/tkn/final-project/asapDatabase.db')
            c=cen.cursor()
            c.execute('select *,oid from userd')
            record=c.fetchall()
            print(record)
            for i in range(len(record)):
                if record[i][2]==e3.get():
                    if record[i][4]==e2.get():
                        msh=messagebox.showinfo('success!!','sucessfully loggedin!!')
                        if msh=='ok':
                            root.withdraw()
                            os.system('python F:/tkn/final-project/main.py')
                            root.deiconify()
                    else:
                        messagebox.showwarning('Failed!!','Invalid password!!')
            else:
                messagebox.showwarning('Failed!!','Invalid username!!')
        except:
            messagebox.showwarning('Failed!!','Invalid username!!')

        cen.commit()
        cen.close()







btn=Button(frame,command=login1,text='Sign In',relief="solid",bd=3,bg='#FF7676',font='{Tw cen mt} 13 bold ',width=26,height=2,activebackground='#FF7676',cursor='hand2')
btn.grid(row=5,column=0,pady=(15,12),padx=(1,5))
btn1=Button(frame,text='Create a new user',relief="flat",bg='white',font='{Tw cen mt} 11 underline',activebackground='white',bd=0,cursor='hand2',command=lambda:show_frame(frame2))
btn1.grid(row=6,column=0,pady=(5,0))
btn3=Button(frame,text='admin login',relief="flat",bg='white',font='{Tw cen mt} 11',activebackground='white',bd=0,cursor='hand2',command=lambda:show_frame(frame3))
btn3.grid(row=7,column=0,pady=(5,0))

#signup
frame=LabelFrame(frame2,padx=35,pady=10,highlightbackground="black", highlightthickness=3,background='white',border=0)
frame.grid(row=0,column=2,padx=(350,0),pady=80)
signup=Label(frame, text='Create a new User',bg='white',font='{Tw cen mt} 25 bold')#rockwell #Tw Cen MT #condensed #century gothic
signup.grid(row=0,column=0,sticky=W)

arrow=PhotoImage(file='F:/tkn/arrow.png')
backbtn=Button(frame2,image=arrow,bg='#DDC9FF',font=50,bd=0,relief='solid',highlightcolor='#DDC9FF',command=lambda: show_frame(frame1))
backbtn.grid(row=0,column=0,pady=(0,700))


#label
name=Label(frame,text="Firstname",bg='white',justify='right',font='{Tw cen mt} 15')
name.grid(row=1,column=0,sticky=W,pady=(5,0),padx=0)

#entry1
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=2,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e4=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e4.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))

#label2
name2=Label(frame,text="Lastname",bg='white',justify='right',font='{Tw cen mt} 15')
name2.grid(row=1,column=1,sticky=W,pady=(5,0),padx=(20,0))

#entry2
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=2,column=1,padx=(20,0))
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e5=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e5.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))


#label3
name=Label(frame,text="address",bg='white',justify='right',font='{Tw cen mt} 15')
name.grid(row=3,column=0,sticky=W,pady=(5,0),padx=0)

#entry3
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=4,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e6=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e6.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))

#label3
name=Label(frame,text="Username",bg='white',justify='right',font='{Tw cen mt} 15')
name.grid(row=5,column=0,sticky=W,pady=(5,0),padx=0)

#entry4
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=6,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e7=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e7.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))



#label4
name=Label(frame,text="Password",bg='white',justify='right',font='{Tw cen mt} 15')
name.grid(row=7,column=0,sticky=W,pady=(5,0),padx=0)

#entry4
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=8,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e8=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e8.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))

#label5
name2=Label(frame,text="Confirm Password",bg='white',justify='right',font='{Tw cen mt} 15')
name2.grid(row=7,column=1,sticky=W,pady=(5,0),padx=(20,0))

#entry5
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=8,column=1,padx=(20,0))
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e9=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e9.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))

def signup():
    if e4.get()=='' or e5.get()=='' or e6.get()==''or e7.get()=='' or e8.get()==''or e9.get()=='':
        messagebox.showwarning('Failed!!','Please enter all fields!!')
    elif e8.get()!=e9.get():
        messagebox.showwarning('Failed!!','Password and Confirm Password did not match!!')
    else:
        conn= sqlite3.connect('F:/tkn/final-project/asapDatabase.db')
        c=conn.cursor()
        c.execute('''insert into userd values(:first_name,:last_name,:username,:address,:password)''',{'first_name':e4.get(),'last_name':e5.get(),'username':e7.get(),'address':e6.get(),'password':e8.get()})
        msg=messagebox.showinfo('success','User created successfully!')
        if msg=='ok':
            show_frame(frame1)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
        conn.commit()
        conn.close()
    
btn=Button(frame,command=signup,text='Create user',relief="solid",bd=3,bg='#FF7676',font='{Tw cen mt} 13 bold ',width=26,height=2,activebackground='#FF7676',cursor='hand2')
btn.grid(row=9,column=0,pady=(25,12),padx=(1,5),columnspan=2)





#admin-
#Entry
adframe=LabelFrame(frame3,padx=25,pady=10,highlightbackground="black", highlightthickness=3,background='white',border=0)
adframe.grid(row=0,column=2,pady=(105,0),padx=(500,0))

backbtn=Button(frame3,image=arrow,bg='#DDC9FF',font=50,bd=0,relief='solid',highlightcolor='#DDC9FF',command=lambda: show_frame(frame1))
backbtn.grid(row=0,column=0,pady=(0,700))

signup=Label(adframe, text='Admin Login',bg='white',font='{Tw cen mt} 25 bold')#rockwell #Tw Cen MT #condensed #century gothic
signup.grid(row=0,column=0,sticky=W)
name=Label(adframe,text="Username",bg='white',justify='right',font='{Tw cen mt} 15')
name.grid(row=1,column=0,sticky=W,pady=(5,0))


#entry
fg=Frame(adframe,border=0,relief='solid')
fg.grid(row=2,column=0)
lb1=Label(fg,image=img,background='white',compound='center',justify=CENTER)
lb1.grid(row=0,column=0,columnspan=2)
ade3=Entry(fg,border=0,width=22,relief="solid",font=50,background='white')
ade3.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))




passWord=Label(adframe,text="Password",bg='white',justify='right',font='{Tw cen mt} 15',anchor=W)
passWord.grid(row=3,column=0,sticky=W)



b=0
def showpassd():
    global b
    b=b+1
    if b%2==0:
        ade2.config(show='*')
        showPss.config(image=img_close)
    else:
        ade2.config(show='')
        showPss.config(image=img_open)





fs=Frame(adframe,border=0,relief='solid')
fs.grid(row=4,column=0)
lb2=Label(fs,image=img,background='white',compound='center',justify=CENTER)
lb2.grid(row=0,column=0,columnspan=2)
ade2=Entry(fs,border=0,width=22,relief="solid",font=50,background='white',show='*')
ade2.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))
showPss=Button(fs,image=img_close,bg='white',relief='solid',cursor='hand2',activebackground='white',border=0,command=showpassd)
showPss.grid(row=0,column=1,sticky=W,pady=(0,17))



def adminlogin():
    if ade2.get()=='' or ade3.get()=='':
        messagebox.showerror('warning!!','invalid input!!')
    else:
        if ade3.get()=='shishirxd' and ade2.get()=='hello123':
            root.withdraw()
            os.system('python F:/tkn/final-project/admindashboard.py')
            root.deiconify()
        else:
            messagebox.showwarning('Authentication failed','Invalid username or password')


btn_frame=Frame(adframe,width=241,height=50,background='#BFBFBF')
btn_frame.place(x=20,y=269)
btn=Button(adframe,text='Sign In',relief="solid",bd=3,bg='#FF7676',font='{Tw cen mt} 13 bold ',width=26,height=2,activebackground='#FF7676',cursor='hand2',command=adminlogin)
btn.grid(row=5,column=0,pady=(15,12),padx=(1,5))








root.mainloop()