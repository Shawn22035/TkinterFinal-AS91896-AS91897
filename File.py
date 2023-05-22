from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Julie's Party Hire!")

Simple=Label(text="something just a test or something im not too sure tbh").grid(column=2,row=1)

def newpage():

    secondpage = Toplevel(root)
    secondpage.geometry("500x500")
    secondpage.resizable(False,False)
    secondpage.title("Julie's Party Hire!")

    def done():

        fullname = namegrab.get()

        if fullname.isalpha() == False:
            messagebox.showerror("Error", "Please only use numbers in name")
            
        try:
            reciept = int(barcodeinp.get())
        except: 
            messagebox.showerror("Error", "Please Input Numbers for Narcode")

        item = choices.get()

        if item=="...":
            messagebox.showerror("Item Choice", "Please select hired item")       

    def page1done():
        secondpage.destroy()
    

    something=Label(secondpage,
                    text="something",
                    font='bold').grid(column=2,row=1)

    name=Label(secondpage, 
                  text="Name:").grid(column=1,row=2, padx=60,pady=30, sticky=W)

    namegrab=Entry(secondpage).grid(column=1,row=3)

    barcode=Label(secondpage,
                    text="Barcode No.").grid(column=2,row=2)

    
    barcodeinp=Entry(secondpage).grid(column=2,row=3)

    nameprint=Button(secondpage,
                     text="print",
                     command=done).grid(column=1,row=4) 
    
    somebutton=Button(secondpage,
                        text="Return!",
                        command=page1done).grid(column=3,row=4)
    

    choices= StringVar()
    choices.set("...")

    itemhire=Label(secondpage, 
                    text="Item Hired").grid(column=3,row=2)

    hired = OptionMenu(secondpage, choices,
                    "...","Spoon","Fork","Plates","Hats","Candles","Confetti").grid(column=3,row=3,padx=30,pady=30)


    

def threepage(): 
    thirdpage =Toplevel(root)  
    thirdpage.geometry("500x500")

    another=Label(thirdpage,
                  text="something else").grid(column=1,row=1)

#Buttons that direct to input & output windows
page = Button(text="Heres a button for a page",command=newpage).grid(column=1,row=2)

page2 = Button(text="This is a second page",command=threepage).grid(column=2,row=2)


root.mainloop()

