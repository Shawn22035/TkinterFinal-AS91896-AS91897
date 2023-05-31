from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image

# Creating the main window
root = Tk()
root.geometry("570x250")
root.resizable(False,False)
root.title("Julie's Party Hire!")

# Creating/Connecting a Database
conn = sqlite3.connect('hires.db')

# Creating a Cursor for Database
c= conn.cursor()

# Creating a Table
'''
c.execute(""" CREATE TABLE hired (
    fullname text,
    reciept integer,
    item text,
    amt integer
    )
    """)
'''

# Main Window Title
logo = Image.open("C:/Users/lee_s/Downloads/logo-PhotoRoom.png")
resize_logo=logo.resize((240,180))
img = ImageTk.PhotoImage(resize_logo)
logo_label = Label(image=img)
logo_label.image = img
logo_label.place(rely=0.0001, relx=0.3)

# Command to terminate program
def kill():
    root.destroy()

# Code that opens a new 500x500 input window titled Julie's Party Hire
def inputpage():
    secondpage = Toplevel(root)
    secondpage.geometry("570x250")
    secondpage.resizable(False,False)
    secondpage.title("Julie's Party Hire!")

    # Bringing input window in front of others
    def lift_s():
        secondpage.lift()
        secondpage.after(1000,lift_s)

# Collecting data and outputting error messages
    def done():

        # Making sure that the name is only a-z & making sure there is a name
        fullname = name.get()
        if fullname == "":
            messagebox.showerror("Error", "Please Input a Name")
            lift_s()
            return
        
        if fullname.isalpha() == False:
            messagebox.showerror("Error", "Please Only Input Letters for Name")
            lift_s()
            return
        
        # Making sure that the reciept number is an integer
        try:
            reciept = int(recieptinp.get())
        except: 
            messagebox.showerror("Error", "Please Only Input Numbers for Barcode")
            lift_s()
            return

        # Making sure that an item is selected in the choice box
        item = choices.get()
        if item=="...":
            messagebox.showerror("Item Choice", "Please select hired item")
            lift_s()
            return

        # Making sure that the amount hired is an integer
        try:
            numhired = int(hiredamt.get()) 
        except:
            messagebox.showerror("Error","Please Only Input Numbers for Amount Hired") 
            lift_s()
            return  
        
        # Connecting to SQLite
        conn = sqlite3.connect('hires.db')
        c= conn.cursor()

        # Inserting values into Database
        c.execute("INSERT INTO hired VALUES (:fullname, :reciept, :item, :numhired)",
                  {
                      "fullname":name.get(),
                      "reciept":recieptinp.get(),
                      "item":choices.get(),
                      "numhired":hiredamt.get()
                  })

        # Cutting Connection from Database
        conn.commit()
        conn.close()

        # Resetting the page for new inputs
        secondpage.destroy()
        inputpage()

# Closes the input page
    def page1done():
        secondpage.destroy()

    # Empty Label to add space from top
    Label(secondpage,
          text="",
          font=("bold",20)).grid(column=1,row=1)
    
    # Label & Input box for name input
    Label(secondpage, 
                text="Name",
                font=("bold",13)).grid(column=1,row=2, padx=40,pady=10, sticky=W)

    name=Entry(secondpage)
    name.grid(column=1,row=3,padx=(10,10))

    # Label & Input box for reciept number
    Label(secondpage,
                text="Reciept Number",
                font=("bold",13),
                padx=20).grid(column=2,row=2)

    recieptinp=Entry(secondpage)
    recieptinp.grid(column=2,row=3)

    # Label & Dropdown box to select what item was hired
    choices= StringVar()
    choices.set("...")

    Label(secondpage, 
                    text="Item Hired",
                font=("bold",13)).grid(column=3,row=2)

    hired = OptionMenu(secondpage, choices,
                    "...","Spoon","Fork","Plates","Hats","Candles","Confetti")
    hired.config(width=6)
    hired.grid(column=3,row=3,padx=(10, 30), pady=30)
    
    # Label & Input box for amount hired
    Label(secondpage,
                    text="Amount Hired",
                    font=("bold",13)).grid(column=4,row=2)
    
    hiredamt=Entry(secondpage)
    hiredamt.grid(column=4,row=3)

    # Button that runs command done, collects information and prints in output page
    nameprint=Button(secondpage,
                     text="Print",
                     command=done,
                     bg="#d1d0cd",
                     width=20, height=2).place(rely=0.8, relx=0.2)
    
    #Button that closes the input window
    somebutton=Button(secondpage,
                        text="Return",
                        command=page1done,
                        bg="#d1d0cd",
                        width=20, height=2).place(rely=0.8, relx=0.6)
    
    
# Command that opens the output window
def outputpage(): 
    thirdpage =Toplevel(root)
    thirdpage.resizable(False, False)  
    thirdpage.geometry("570x250")
   
   # Command that brings output window to front
    def lift_w():
        thirdpage.lift()
        thirdpage.after(1000,lift_w)

    # Deleting data from Database
    def remove():

        # Making sure that the input for Order ID is an integer
        try:
            delete_value = int(delinp.get())
        except:
            messagebox.showerror("Error","Please Only Input Numbers for Order ID") 
            lift_w()
            return   

        # Connecting to SQLite
        conn =sqlite3.connect('hires.db')
        c= conn.cursor()

        # Deleting data from Database using Order ID
        c.execute("DELETE from hired WHERE oid= " + delinp.get())
        delinp.delete(0, END)
        conn.commit()
        conn.close()

        # Refreshes window everytime a row is deleted
        thirdpage.destroy()
        outputpage()

    # Connecting to hires.db in "hired" Database
    conn = sqlite3.connect("hires.db")
    c = conn.cursor()

    # Selecting all information from "hired" Database    
    c.execute("SELECT *, oid FROM hired")

    # Turning Database inputs into tuple
    hirees = c.fetchall()
    
    # Label titles for information table
    Label(thirdpage,text="NAME" + "\t", font=("bold",13),bg="#d1d0cd",relief="raised").grid(column=0,row=0, padx=(10,0))
    Label(thirdpage,text="RECIEPT NUM" + "\t", font=("bold",13),bg="#d1d0cd",relief="raised").grid(column=1,row=0)
    Label(thirdpage,text=" ITEM" + "\t", font=("bold",13),bg="#d1d0cd",relief="raised").grid(column=2,row=0)
    Label(thirdpage,text="       AMOUNT " + "\t" , font=("bold",13),bg="#d1d0cd",relief="raised").grid(column=3,row=0)
    Label(thirdpage,text="ORDER ID", font=("bold",13),bg="#d1d0cd",relief="raised").grid(column=4,row=0)

    # Print each tuple on a page
    print_hirees = ''
    for i, hiree in enumerate(hirees):
        hirer = hiree[0]
        Label(thirdpage, text=str(hiree[0])).grid(column=0, row=i + 1,)
        Label(thirdpage, text=str(hiree[1])).grid(column=1, row=i + 1,)        
        Label(thirdpage, text=str(hiree[2])).grid(column=2, row=i + 1,)
        Label(thirdpage, text=str(hiree[3])).grid(column=3, row=i + 1,)
        Label(thirdpage, text=str(hiree[4])).grid(column=4, row=i + 1,)

    # What order needs to be deleted
    Label(thirdpage, text="Enter Order ID Number",font=("bold",13)).place(rely=0.7, relx= 0.05)

    delinp=Entry(thirdpage,width=20,font=("Arial, 23"))
    delinp.place(rely=0.8,relx=0.05)

    # Runs remove command that deletes row
    delbut=Button(thirdpage, text= "Delete", command=remove, width=20, height=2).place(rely=0.8,relx=0.7)

    printhired = Label(thirdpage, text=print_hirees)
    printhired.grid(column=1, row=1, columnspan=6)

    conn.commit()
    conn.close()

#Buttons that direct to input, output & close windows
page = Button(text="Input Page",command=inputpage, bg="#d1d0cd",width = 20, height= 2).place(rely=0.8, relx=0.1)
page2 = Button(text="Output Page",command=outputpage, bg="#d1d0cd",width = 20, height = 2).place(rely=0.8,relx= 0.375)
close = Button(text="Close Window", command=kill, bg="#d1d0cd",width=20, height = 2).place(rely=0.8, relx= 0.65)

# Commiting any changes
conn.commit()
# Closing the Database
conn.close()

root.mainloop()

