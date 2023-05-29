from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("500x500")
root.resizable(False,False)
root.title("Julie's Party Hire!")

# Creating/Connecting a Database
conn = sqlite3.connect('hires.db')

# Creating a Cursor
c= conn.cursor()

Simple=Label(text="something just a test or something im not too sure tbh").grid(column=2,row=1)

#Code that opens a new 500x500 input window titled Julie's Party Hire
def newpage():

    secondpage = Toplevel(root)
    secondpage.geometry("550x250")
    secondpage.resizable(False,False)
    secondpage.title("Julie's Party Hire!")

#Collecting data and outputting error messages
    def done():



        fullname = name.get()

        if fullname.isalpha() == False:
            messagebox.showerror("Error", "Please Only Input Letters for Name")
            
        try:
            reciept = int(recieptinp.get())
        except: 
            messagebox.showerror("Error", "Please Only Input Numbers for Barcode")

        item = choices.get()

        if item=="...":
            messagebox.showerror("Item Choice", "Please select hired item")

        try:
            numhired = int(hiredamt.get()) 
        except:
            messagebox.showerror("Error","Please Only Input Numbers for Amount Hired")   

#Closes the input page
    def page1done():
        secondpage.destroy()
    
#Labels and Input boxes

    Label(secondpage,
                text="Julie's Party Hire",
                font='bold').place(relx=0.5,rely=0.03,anchor=CENTER)

    Label(secondpage, 
                text="Name:").grid(column=1,row=2, padx=60,pady=30, sticky=W)

    name=Entry(secondpage)
    name.grid(column=1,row=3)

    Label(secondpage,
                text="Barcode No.").grid(column=2,row=2)

    
    recieptinp=Entry(secondpage)
    recieptinp.grid(column=2,row=3)

    #Dropdown box to select what item was hired
    choices= StringVar()
    choices.set("...")

    Label(secondpage, 
                    text="Item Hired").grid(column=3,row=2)

    hired = OptionMenu(secondpage, choices,
                    "...","Spoon","Fork","Plates","Hats","Candles","Confetti").grid(column=3,row=3,padx=30,pady=30)
    
    Label(secondpage,
                    text="Amount Hired").grid(column=4,row=2)
    
    hiredamt=Entry(secondpage)
    hiredamt.grid(column=4,row=3)





    nameprint=Button(secondpage,
                     text="print",
                     command=done).grid(column=2,row=4) 
    
    #Button that input window
    somebutton=Button(secondpage,
                        text="Return!",
                        command=page1done).grid(column=3,row=4)
    
    
#Variable that opens the output window
def threepage(): 
    thirdpage =Toplevel(root)  
    thirdpage.geometry("500x500")

    Label(thirdpage,
                  text="something else").grid(column=1,row=1)

#Buttons that direct to input & output windows



page = Button(text="Heres a button for a page",command=newpage).grid(column=1,row=2)

page2 = Button(text="This is a second page",command=threepage).grid(column=2,row=2)

# Commiting any changes
conn.commit()

# Closing the Database
conn.close()

root.mainloop()

