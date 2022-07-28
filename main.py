import os
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import sqlite3
import cv2 as cv

#initial setup
root=Tk()
root.title('ASAP-LOGIN V-1.0.0'.center(400))
root.configure(background='#DDC9FF')
dir1='F:/tkn/final-project/'
root.iconbitmap(dir1+'Logo.ico')
maincolor='#DDC9FF'
mainfont='{tw cen mt}'
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.resizable(True,False)

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=0)
root.rowconfigure(1,weight=2)

frame1=Frame(root,bg='#DDC9FF')
frame2=Frame(root,bg='#DDC9FF')
btnframe = Frame(root,background=maincolor)
btnframe.grid(row=0,column=0,sticky='nw')
for frame in (frame1, frame2):
    frame.grid(row=1,column=0,sticky='nsew',pady=(0,0),padx=0)


def show_frame(frame):
    frame.tkraise()
    

show_frame(frame1)


#btns
frame1_btn=Button(btnframe,text='Main',command=lambda:show_frame(frame1),font='{tw cen mt} 13',relief='groove',activebackground=maincolor)
frame1_btn.grid(row=0,column=0,padx=(0,0))

frame2_btn=Button(btnframe,text='invoices',command=lambda:show_frame(frame2),font='{tw cen mt} 13',relief='groove',activebackground=maincolor)
frame2_btn.grid(row=0,column=1)


#frame1:
#firstrow:
rf1=LabelFrame(frame1,text="Customer Details",font='{tw cen mt} 20',width=900,height=185,bg='#DDC9FF',border=2,relief=SOLID)
rf1.place(x=60,y=0)


#rf1items
billLabel=Label(rf1,text='Bill no.:',font=mainfont+' 15',bg='#DDC9FF')
billLabel.place(x=0,y=0) 


billno=12001
billL=Label(rf1,text=billno,font=mainfont+' 15',bg='#DDC9FF')
billL.place(x=100,y=0) 

dateLabel=Label(rf1,text='Transaction date:',font=mainfont+' 15',bg='#DDC9FF')
dateLabel.place(x=0,y=40)

custLabel=Label(rf1,text='Customer name:',font=mainfont+' 15',bg='#DDC9FF')
custLabel.place(x=0,y=80) 

custNum=Label(rf1,text='Number:',font=mainfont+' 15',bg='#DDC9FF')
custNum.place(x=0,y=120) 

#rntries:
custName=Entry(rf1,font=mainfont+' 15',border=0,bg='#DDC9FF')
custName.place(x=143,y=80)
Frame(rf1,height=2,width=220,bg='black').place(x=143,y=105)

custNumber=Entry(rf1,font=mainfont+' 15',border=0,bg='#DDC9FF')
custNumber.place(x=143,y=115)
Frame(rf1,height=2,width=220,bg='black').place(x=143,y=140)

def nwbill():
    global billno
    billno+=1
    billL.config(text=billno)
    remove_all()
    global count
    count=0

def additemdf(ok):
    conn = sqlite3.connect('F:/tkn/final-project/asapDatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM product where product_id="+ok)
    global records
    records = c.fetchall()
    print(records)
    global addtp
    addtp=Toplevel()
    addtp.title('additem')
    addtp.config(bg=maincolor)
    addtp.geometry('230x200')
    items=LabelFrame(addtp,font=mainfont+' 25',bg=maincolor,text='items')
    items.grid(row=0,column=0)
    ire=Label(items,font=mainfont,bg=maincolor,text='Product_id:')
    ire.grid(row=0,column=0)
    iremcode=Label(items,font=mainfont,bg=maincolor,text=records[0][0])
    iremcode.grid(row=0,column=1)

    irem=Label(items,font=mainfont,bg=maincolor,text='Product_name:')
    irem.grid(row=1,column=0)
    tremname=Label(items,font=mainfont,bg=maincolor,text=records[0][1])
    tremname.grid(row=1,column=1)

    iremc=Label(items,font=mainfont,bg=maincolor,text='rate:')
    iremc.grid(row=2,column=0)
    rate=Label(items,font=mainfont,bg=maincolor,text=records[0][2])
    rate.grid(row=2,column=1)

    iremco=Label(items,font=mainfont,bg=maincolor,text='quantity:')
    iremco.grid(row=3,column=0)

    global quant


    quant=Entry(items)
    quant.grid(row=3,column=1)

    aditembtn=Button(addtp,text='add item',command=add_record)
    aditembtn.grid(row=1,column=0,columnspan=2)
def cammerld():
    img= cv.VideoCapture(0,cv.CAP_DSHOW)
    while True:
        istrue, frame = img.read()
        #ractangle
        cv.rectangle(frame,(150,120),(500,450),(0,0,255),thickness=3)

        #qrcode scanner
        d=cv.QRCodeDetector()
        val,point,straight_qrcode=d.detectAndDecode(frame)
        
        #printing the value and closing the camera
        if val>'':
            print(val,'ok')
            additemdf(val)
            break  
        cv.imshow('webcam',frame)

        #closing the camera
        if cv.waitKey(1) & 0xFF==ord('c'):
            break
    img.release()
    cv.destroyAllWindows()

qr_code=Button(frame1,text="QR CODE MODULE",font=mainfont+' 25',border=2,relief=SOLID,bg='#DDC9FF',command=cammerld)
qr_code.place(x=1000,y=15,height=170,width=350)

def time():
    date=datetime.now().strftime("%m/%d/%Y,%H:%M:%S %p")
    dalabel.config(text=date)
    dalabel.after(1000,time)

dalabel=Label(rf1,font=mainfont+' 15',bg='#DDC9FF')
dalabel.place(x=140,y=40)
time()


rf2=Frame(frame1,bg='white',width=900,height=400,relief=SOLID,border=2)
rf2.place(x=60,y=205)

frameline1=Frame(frame1,bg='black',height=2,width=900)
frameline1.place(x=60,y=604)
frameline2=Frame(frame1,bg='black',height=401,width=2)
frameline2.place(x=960,y=205)
frameline3=Frame(frame1,bg='black',height=401,width=2)
frameline3.place(x=942,y=205)


#style#
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",bg="#D3D3D3",foreground="black",rowheight=30,fieldbackground="#D3D3D3",font='{tw cen mt}')


style.configure("Treeview.Heading", font=('{tw cen mt} 15'),background='#DDC9FF',border=2)
# Change Selected Color
style.map('Treeview',
	background=[('selected', "#FF8080")])
#treesssefaod
tree_prod = Frame(rf2)
tree_prod.place(x=0,y=0)

# Create a Treeview Scrollbar
scroll_prod = Scrollbar(tree_prod)
scroll_prod.pack(side=RIGHT, fill=Y)

# Create The Treeview
prod_tree = ttk.Treeview(tree_prod, yscrollcommand=scroll_prod.set, selectmode="extended")
prod_tree.pack()

# Configure the Scrollbar
scroll_prod.config(command=prod_tree.yview)

# Define Our Columns
prod_tree['columns'] = ("S.no", "product_name", "rate", "quantity",'total')

# Format Our Columns
prod_tree.column("#0", width=0, stretch=NO)
prod_tree.column("S.no", anchor=CENTER, width=150)
prod_tree.column("product_name", anchor=CENTER, width=250)
prod_tree.column("rate", anchor=CENTER, width=150)
prod_tree.column("quantity", anchor=CENTER, width=150)
prod_tree.column("total", anchor=CENTER, width=180)



# Create Headings
prod_tree.heading("#0", text="", anchor=CENTER)
prod_tree.heading("S.no", text="S.no", anchor=CENTER)
prod_tree.heading("product_name", text="Particulars", anchor=CENTER)
prod_tree.heading("rate", text="Rate", anchor=CENTER)
prod_tree.heading("quantity", text="Quantity", anchor=CENTER)
prod_tree.heading("total", text="Amount", anchor=CENTER)


#insertitem:
rf4=LabelFrame(frame1,text="Insert Item",width=350,height=415,bg='#DDC9FF',font='{tw cen mt} 20',relief=SOLID)
rf4.place(x=1000,y=189)




addItem=Label(rf4,text='Product code:',font=mainfont,bg='#DDC9FF')
addItem.place(x=0,y=10)

addEnt=Entry(rf4,font=mainfont+' 15',border=0,bg='#DDC9FF')
addEnt.place(x=120,y=11)
addframe=Frame(rf4,height=2,width=200,bg='black')
addframe.place(x=120,y=35)

# tender_insert=Label(rf4,text='Tender:',font=mainfont,bg='#DDC9FF')
# tender_insert.place(x=0,y=50)

# tender_entry=Entry(rf4,font=mainfont+' 15',border=0,bg='#DDC9FF')
# tender_entry.place(x=120,y=51)
# addframe2=Frame(rf4,height=2,width=200,bg='black')
# addframe2.place(x=120,y=75)
count=1

def add_record():
        prod_tree.tag_configure('evenrow', background='light blue')
        prod_tree.tag_configure('oddrow', background='gray')
        
        global count
        
        if count % 2 == 0:
            prod_tree.insert(parent='', index='end', iid=count, text="", values=(count, records[0][1],records[0][2],quant.get(),records[0][2]*int(quant.get()) ), tags=('evenrow',))
        else:
            prod_tree.insert(parent='', index='end', iid=count, text="", values=(count, records[0][1],records[0][2],quant.get(),records[0][2]*int(quant.get()) ), tags=('oddrow',))

        count += 1
        addtp.destroy()
        addEnt.delete(0,END)

        total_amt.config(text=total())













def additems():
    if addEnt.get()!='':
        try:
            conn = sqlite3.connect('F:/tkn/final-project/asapDatabase.db')
            c = conn.cursor()
            c.execute("SELECT * FROM product where product_id="+addEnt.get())
            global records
            records = c.fetchall()
            print(records)
            global addtp
            addtp=Toplevel()
            addtp.title('additem')
            addtp.config(bg=maincolor)
            addtp.geometry('290x200')
            items=LabelFrame(addtp,font=mainfont+' 25',bg=maincolor,text='items')
            items.place(x=15,y=10)
            ire=Label(items,font=mainfont,bg=maincolor,text='Product_id:')
            ire.grid(row=0,column=0)
            iremcode=Label(items,font=mainfont,bg=maincolor,text=records[0][0])
            iremcode.grid(row=0,column=1)

            irem=Label(items,font=mainfont,bg=maincolor,text='Product_name:')
            irem.grid(row=1,column=0)
            tremname=Label(items,font=mainfont,bg=maincolor,text=records[0][1])
            tremname.grid(row=1,column=1)

            iremc=Label(items,font=mainfont,bg=maincolor,text='rate:')
            iremc.grid(row=2,column=0)
            rate=Label(items,font=mainfont,bg=maincolor,text=records[0][2])
            rate.grid(row=2,column=1)

            iremco=Label(items,font=mainfont,bg=maincolor,text='quantity:')
            iremco.grid(row=3,column=0)
            
            global quant


            quant=Entry(items)
            quant.grid(row=3,column=1)
            
            aditembtn=Button(addtp,text='add item',command=add_record)
            aditembtn.place(x=100,y=170)

        except:
            addtp.destroy()
            messagebox.showerror('warning!!','Item not found!!')
    else:
        messagebox.showerror('warning!!','Please enter a valid input!!')







addBtn=Button(rf4,text='ADD',command=additems,bg='#DDC9FF')
addBtn.place(x=120,y=100,width=200)



conn = sqlite3.connect('F:/tkn/final-project/asapDatabase.db')

# Create a cursor instance
c = conn.cursor()

#Create Table
c.execute("""CREATE TABLE if not exists invoices (
	invoice_no integer,
	customer_name text,
    customer_num integer,
	items text,
	total integer,
    time text
    )
	""")
conn.commit()
conn.close()




def remove_all():
    for record in prod_tree.get_children():
            prod_tree.delete(record)
    custName.delete(0,END)
    custNumber.delete(0,END)
    
def remove_one():
    x=prod_tree.selection()[0]
    prod_tree.delete(x)
    

def nwbill():
    global billno
    billno+=1
    billL.config(text=billno)
    remove_all()
    addToDb.config(state=NORMAL)
    global count
    count=1
    total_amt.config(text='0')


def total():
    no=prod_tree.get_children()
    a=0
    for child in no:
        no=prod_tree.item(child,'value')
        a+=int(no[4])
    return a





def allval(tree):
    no=tree.get_children()
    a=[]
    for child in no:
        a.append(tree.item(child,'value'))
    return a


def savedb():
    if custName.get()!='':
        if len(custNumber.get())==10:
            conn=sqlite3.connect('F:/tkn/final-project/asapDatabase.db')
            c = conn.cursor()
            c.execute("INSERT INTO invoices VALUES (:invoice_no, :customer_name, :customer_num, :items, :total,:time)", 
                {
                'invoice_no':billno,
                'customer_name':custName.get(),
                'customer_num':int(custNumber.get()),
                'items':str(allval(prod_tree)),
                'total':total(),
                'time':datetime.now().strftime("%m/%d/%Y,%H:%M:%S %p")
                })
            messagebox.showinfo('Success!','Added the bill into database sucessfully!')
            conn.commit()
            conn.close()
            addToDb.config(state=DISABLED)
            Print_bill.config(state=NORMAL)
            update_table()



        else:
            messagebox.showwarning('Warning!!','Invalid customer contact Number!!')
    else:
        messagebox.showwarning('Warning!!','Invalid Customer Name!!')
 


newbill=Button(rf4,text='newbill',command=nwbill,bg='pink',relief=SOLID)
newbill.place(x=15,y=140,width=100,height=50)



addToDb=Button(rf4,text='SAVE INVOICE',command=savedb,bg='#DDC9FF')
addToDb.place(x=120,y=125,width=200)


total_amount=Label(frame1,text="Total Amount:",bg='#DDC9FF',font=mainfont+' 18')
total_amount.place(x=700,y=610)

total_amt=Label(frame1,bg='#DDC9FF',text='0',font=mainfont+' 18')
total_amt.place(x=850,y=610)

# tender_label=Label(frame1,text="Tender:",bg='#DDC9FF',font=mainfont+' 18')
# tender_label.place(x=700,y=650)

# change_label=Label(frame1,text='Change:',bg='#DDC9FF',font=mainfont+' 18')
# change_label.place(x=700,y=690)


def query_database3():
	# Create a database or connect to one that exists
	conn = sqlite3.connect('F:/tkn/final-project/asapDatabase.db')

	# Create a cursor instance
	c = conn.cursor()

	c.execute("SELECT *,oid FROM invoices")
	records = c.fetchall()
	#print(records)
	# Add our data to the screen
	global cont
	cont = 0

	for record in records:
		if cont % 2 == 0:
			my_tree.insert(parent='', index='end', iid=cont, text='', values=(record[0], record[1], record[2], record[4], record[5],record[6]), tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=cont, text='', values=(record[0], record[1], record[2], record[4], record[5],record[6]), tags=('oddrow',))
		# increment conter
		cont += 1


	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()



# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=50,
	fieldbackground="#D3D3D3",
    font='{tw cen mt}')


style.configure("Treeview.Heading", font=('{tw cen mt} 15'),
    background='white',
    border=2
)
# Change Selected Color
style.map('Treeview',
	background=[('selected', "#FF8080")])

#frame for tt


# Create a Treeview Frame
tree_frame = LabelFrame(frame2,text="PAST INVOICES",bg='#DDC9FF',font='{tw cen mt} 20')
tree_frame.grid(row=0,column=0)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Billno.", "Customer name", "number", "total",'date')

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Billno.", anchor=W, width=250)
my_tree.column("Customer name", anchor=W, width=250)
my_tree.column("number", anchor=CENTER, width=180)
my_tree.column("total", anchor=CENTER, width=180)
my_tree.column("date", anchor=CENTER, width=200)



# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Billno.", text="Billno.", anchor=W)
my_tree.heading("Customer name", text="Customer name", anchor=W)
my_tree.heading("number", text="Number", anchor=CENTER)
my_tree.heading("total", text="Total", anchor=CENTER)
my_tree.heading("date", text="Date", anchor=CENTER)



# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background=maincolor)

query_database3()

def remove_one_past():
    msg=messagebox.askquestion("Warning!!", "Are you sure you want to delete following product?",icon = 'warning')

    if msg=='yes':

    # Grab the record number

        selected = my_tree.focus()

        dosi = my_tree.item(selected,'values')
        print(dosi)

        # ok=int(selected)+1

        print(dosi[5])

        conn= sqlite3.connect('F:/tkn/final-project/asapDatabase.db')

        c=conn.cursor()

        c.execute('delete from invoices where oid ='+dosi[5])

        print('success','deleted')

        conn.commit()

        conn.close()

        update_table()



frame_commands=LabelFrame(frame2,text='Commands',bg='#DDC9FF',font='{tw cen mt} 20',width=200,height=560)
frame_commands.place(x=1100,y=0)
remove_one_button_past_invoices=Button(frame_commands,text='Remove Selected',command=remove_one_past,bg='#DDC9FF')
remove_one_button_past_invoices.place(x=50,y=20)
def printbill():
    f=open('F:/tkn/final-project/tempf.txt','w')
    f.write('     ASAP Super Store     \n')
    f.write('   Anamnager Kathmandu     \n')
    f.write('Bill no:')
    f.write(str(billno))
    f.write('\ncustomer name:')
    f.write(str(custName.get()))
    f.write('\ncustomer no:')
    f.write(str(custNumber.get()))
    f.write('\npayment mode: cash    \n')
    f.write('*******************************\n')
    f.write('sn   Items   rate qty Amount\n')
    f.write('******************************\n')
    for i in allval(prod_tree): 
        f.write(str(i).replace('(','').replace(')','').replace("'","").replace(',','  '))
        f.write('\n')
    f.write('******************************\n')
    f.write('               total:')
    f.write(str(total()))
    f.write('\n******************************\n')
    f.write('thank you for shopping in ASAP \n super store!!\n')
    f.write('!!See you Again!!')
    f.close()
    os.startfile('F:/tkn/final-project/tempf.txt','print')


def update_table():
    for record in my_tree.get_children():
        my_tree.delete(record)
    query_database3()

Print_bill=Button(rf4,text="PRINT BILL",bg='#DDC9FF',command=printbill)
Print_bill.place(x=120,y=150,width=200)    
Print_bill.config(state=DISABLED)

remove_selected=Button(rf4,text='REMOVE SELECTED',bg='#DDC9FF',command=remove_one)
remove_selected.place(x=120,y=175,width=200)

remove_all_button=Button(rf4,text='REMOVE ALL',bg='#DDC9FF',command=remove_all)
remove_all_button.place(x=120,y=200,width=200)

root.mainloop()