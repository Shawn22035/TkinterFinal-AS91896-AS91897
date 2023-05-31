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
Label(text="Julie's Party Hire", font='bold').grid(column=2,row=0)

# Code that opens a new 500x500 input window titled Julie's Party Hire
def inputpage():
    secondpage = Toplevel(root)
    secondpage.geometry("570x250")
    secondpage.resizable(False,False)
    secondpage.title("Julie's Party Hire!")

# Collecting data and outputting error messages
    def done():
        conn = sqlite3.connect('hires.db')
        c= conn.cursor()

        # 
        c.execute("INSERT INTO hired VALUES (:fullname, :reciept, :item, :numhired)",
                  {
                      "fullname":name.get(),
                      "reciept":recieptinp.get(),
                      "item":choices.get(),
                      "numhired":hiredamt.get()
                  })

        
        conn.commit()
        conn.close()

        # Making sure that the name is only a-z
        fullname = name.get()
        if fullname.isalpha() == False:
            messagebox.showerror("Error", "Please Only Input Letters for Name")
            return
            
        # Making sure that the reciept number is an integer
        try:
            reciept = int(recieptinp.get())
        except: 
            messagebox.showerror("Error", "Please Only Input Numbers for Barcode")
            return

        # Making sure that an item is selected in the choice box
        item = choices.get()
        if item=="...":
            messagebox.showerror("Item Choice", "Please select hired item")
            return

        # Making sure that the amount hired is an integer
        try:
            numhired = int(hiredamt.get()) 
        except:
            messagebox.showerror("Error","Please Only Input Numbers for Amount Hired") 
            return  

        # Resetting the page for new inputs
        secondpage.destroy()
        inputpage()

# Closes the input page
    def page1done():
        secondpage.destroy()

    # Label & Input box for name input
    Label(secondpage, 
                text="Name:").grid(column=1,row=2, padx=60,pady=30, sticky=W)

    name=Entry(secondpage)
    name.grid(column=1,row=3)

    # Label & Input box for reciept number
    Label(secondpage,
                text="Reciept No.").grid(column=2,row=2)

    recieptinp=Entry(secondpage)
    recieptinp.grid(column=2,row=3)

    # Label & Dropdown box to select what item was hired
    choices= StringVar()
    choices.set("...")

    Label(secondpage, 
                    text="Item Hired").grid(column=3,row=2)

    hired = OptionMenu(secondpage, choices,
                    "...","Spoon","Fork","Plates","Hats","Candles","Confetti")
    hired.config(width=6)
    hired.grid(column=3,row=3,padx=30, pady=30)
    
    # Label & Input box for amount hired
    Label(secondpage,
                    text="Amt Hired").grid(column=4,row=2)
    
    hiredamt=Entry(secondpage)
    hiredamt.grid(column=4,row=3)

    # Button that runs command done, collects information and prints in output page
    nameprint=Button(secondpage,
                     text="print",
                     command=done).grid(column=2,row=4) 
    
    #Button that closes the input window
    somebutton=Button(secondpage,
                        text="Return!",
                        command=page1done).grid(column=3,row=4)
    
    
# Command that opens the output window
def outputpage(): 
    thirdpage =Toplevel(root)
    thirdpage.resizable(False, False)  
    thirdpage.geometry("570x250")
   
    # Command that deletes row from Database
    def remove():
        conn =sqlite3.connect('hires.db')
        c= conn.cursor()
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
    
    Label(thirdpage, text="Julie's Party Hire", font='bold').place(relx=0.5,rely=0.03,anchor=CENTER)
    
    # Label titles for information table
    Label(thirdpage,text="NAME" + "\t", font=("bold",13)).grid(column=0,row=0, padx=(10,0))
    Label(thirdpage,text="RECIEPT NUM" + "\t", font=("bold",13)).grid(column=1,row=0)
    Label(thirdpage,text=" ITEM" + "\t", font=("bold",13)).grid(column=2,row=0)
    Label(thirdpage,text="       AMOUNT " + "\t" , font=("bold",13)).grid(column=3,row=0)
    Label(thirdpage,text="ORDER ID", font=("bold",13)).grid(column=4,row=0)

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
    Label(thirdpage, text="Enter Order ID Number").grid(column=1, row=i+4,sticky=W)

    delinp=Entry(thirdpage)
    delinp.grid(column=1,row=i+5)

    # Runs remove command that deletes row
    delbut=Button(thirdpage, text= "Delete", command=remove).grid(column=3, row=i+5, sticky=E)

    printhired = Label(thirdpage, text=print_hirees)
    printhired.grid(column=1, row=1, columnspan=6)

    conn.commit()
    conn.close()

#Buttons that direct to input & output windows
logo = Image.open("C:/Users/lee_s/Downloads/logo-PhotoRoom.png")
resize_logo=logo.resize((170,150))
img = ImageTk.PhotoImage(resize_logo)
logo_label = Label(image=img)
logo_label.image = img
logo_label.grid(column=2, row=1,pady=(10,0), padx=(0,20))

page = Button(text="Input Page",command=inputpage, width = 20, height= 2).grid(column=1,row=2, sticky=W, padx=27)
page2 = Button(text="Output Page",command=outputpage, width = 20, height = 2).grid(column=3,row=2, sticky=E)

# Commiting any changes
conn.commit()
# Closing the Database
conn.close()

root.mainloop()

