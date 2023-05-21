from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import random

allData = []

def submitData():
    
    # Data Validation

    while True:

    # * Checking that Customer's Name doesn't include Numbers

        FirstName = firstName.get()
        LastName = lastName.get()

        if FirstName.isalpha() == False or LastName.isalpha() == False:

            messagebox.showerror(title="Name Error", message="Name must only include letters from a-z")
            break
    
    # * Asking if the User Input can be converted into an int if not throw Error

        try:
            reciept = int(recieptNumber.get())
        except:
            messagebox.showerror(title="Reciept Number Error", message="Receipt Number must only include numbers")
            break

    # * Checking that item has been changed from orignally set Value

        item = itemHiredVar.get()

        if item == "...":
            messagebox.showerror(title="Item Hired Error", message="Select an Item which has been Hired")
            break
    
    # * Asking if the User Input can be converted into an int if not throw Error

        try:
            itemHired = int(numberHired.get())
        except:
            messagebox.showerror(title="Number Hired Error", message="Number Hired must only include numbers")
            break

        if itemHired <= 0 or itemHired > 500:
            messagebox.showerror(title="Number Hired Error", message=f"You can only hire between 1 - 500 items")
            break

    # * New Entry Creation

        userEntry = dict(
            CustomerFirstName = FirstName, 
            CustomerLastName = LastName,
            RecieptNumber = reciept, 
            ItemHired = item,
            NumberHired = itemHired,
            id = random.random()
            )
        
        allData.append(userEntry)
        displayData()

    # * Clearing Entry Boxes

        for widget in main.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, END)
            itemHiredVar.set("...")

        break

def deleteEntry(id):

    # * Delete function 

    if messagebox.askyesno(message="Do you want to delete this Entry?", title="Delete Confirmation"):

        global allData
        newArr = []

        for item in allData:
            if item.get("id") != id:
                newArr.append(item)

        allData = newArr
        displayData()

def displayData():
    
    # Clearing Previous Data in Data Window

    for widget in dataWindow.winfo_children():
      if isinstance(widget, Widget):
        widget.destroy()

    # Display Header for Data 

    Label(dataWindow, font=dataFont, text="First Name").grid(pady=5, padx=10,column=0, row=0, sticky=W)
    Label(dataWindow, font=dataFont, text="Last Name").grid(pady=5, padx=10,column=1, row=0, sticky=W)
    Label(dataWindow, font=dataFont, text="Reciept Number").grid(pady=5, padx=10,column=2, row=0, sticky=W)
    Label(dataWindow, font=dataFont, text="Item Hired").grid(pady=5, padx=10,column=3, row=0, sticky=W)
    Label(dataWindow, font=dataFont, text="Number Hired").grid(pady=5, padx=10,column=4, row=0, sticky=W)
    Button(dataWindow, font=dataFont, bg="black", fg="white", text="Hide Window", command=lambda: hideWindow(dataWindow)).grid(pady=5, padx=10, column=5, row=0, sticky=W)

    # Revealing Data Window

    dataWindow.deiconify()

    row = 1

    # Printing Data for allData
    for obj in allData:
        Label(dataWindow, font=dataFont, bg="ivory3" if row % 2 == 1 else "ghost white", text=obj.get("CustomerFirstName").capitalize()).grid(pady=5, ipady=3,column=0, row=row, sticky="WE")
        Label(dataWindow, font=dataFont, bg="ivory3" if row % 2 == 1 else "ghost white", text=obj.get("CustomerLastName").capitalize()).grid(pady=5, ipady=3,column=1, row=row, sticky="WE")
        Label(dataWindow, font=dataFont, bg="ivory3" if row % 2 == 1 else "ghost white", text=obj.get("RecieptNumber")).grid(pady=5, ipady=3,column=2, row=row, sticky="WE")
        Label(dataWindow, font=dataFont, bg="ivory3" if row % 2 == 1 else "ghost white", text=obj.get("ItemHired")).grid(pady=5, ipady=3,column=3, row=row, sticky="WE")
        Label(dataWindow, font=dataFont, bg="ivory3" if row % 2 == 1 else "ghost white", text=obj.get("NumberHired")).grid(pady=5, ipady=3,column=4, row=row, sticky="WE")
        Button(dataWindow, font=dataFont, bg="black", fg="white", text="Delete", command=lambda d=obj.get('id'): deleteEntry(d)).grid(ipady=2, padx=10, column=5, row=row, sticky="WE")
        row += 1

# Get window as a parameter to make function more reusable

def hideWindow(window):
    window.withdraw()

# Avaliable Items for Rental

items = [
    "Spoon",
    "Knife",
    "Fork",
    "Cup",
    "Plate",
]

# Main Window
main = Tk()
main.title("Julie Party Hire")

# Data Window
dataWindow = Toplevel()

# Hiding Data Window
hideWindow(dataWindow)

# Font

labelFont = Font(
    family="Helvetica",
    weight="bold",
    slant="italic",
    size=12
)

buttonFont = Font(
    family="Helvetica",
    weight="bold",
    slant="italic",
    size=16
)

dataFont = Font(
    family="Helvetica",
    slant="italic",
    size=8
)

entryFont = Font(
    family="Helvetica",
    size=10
)

# Window Geometry 
main.geometry("550x450")
dataWindow.geometry("650x450")

Label(main, text="First Name", font=labelFont).grid(pady=10, padx=10, sticky=W, column=0, row=0)
firstName = Entry(main, width=30, font=entryFont, bg="ivory3", borderwidth=0)
firstName.grid(padx=20, column=0, row=1, ipady=6)

Label(main, text="Last Name", font=labelFont).grid(pady=10, padx=10, sticky=W, column=1, row=0)
lastName = Entry(main, width=30, font=entryFont, bg="ivory3", borderwidth=0)
lastName.grid(padx=20, column=1, row=1, ipady=6)

# Recipt Number
Label(main, text="Receipt Number", font=labelFont).grid(pady=10, padx=10, sticky=W, column=0, row=2)
recieptNumber = Entry(main, width=30, font=entryFont, bg="ivory3", borderwidth=0)
recieptNumber.grid(padx=20, column=0, row=3, ipady=6)

# Item Hired
itemHiredVar = StringVar()
itemHiredVar.set("...")

itemHiredDropDown = OptionMenu(main, itemHiredVar, *items)
itemHiredDropDown.configure(width=26, borderwidth=0, bg="ivory3")
Label(main, text="Item Hired", font=labelFont).grid(pady=10, padx=10, column=1, row=2, sticky=W)
itemHiredDropDown.grid(padx=20, column=1, row=3, ipady=4, ipadx=8)

# Number Hired
Label(main, text="Number Hired", font=labelFont).grid(pady=10, padx=10, column=0, row=4, sticky=W)
numberHired = Entry(main, width=30, font=entryFont, bg="ivory3", borderwidth=0)

numberHired.grid(padx=20, column=0, row=5, ipady=6)

# Quit Button

Button(main, text="QUIT", font=labelFont, fg="white", bg="black", borderwidth=0, command=main.quit).grid(padx=30, column=1, row=5, sticky=W, ipadx=74, ipady=1)

# Show Data & Add Data

Button(main, text="Show Entries", font=buttonFont, height=1, bg='black', fg='white', width=20, 
       command=displayData).grid(columnspan=2, pady=20, column=0, row=6)

Button(main, text="Submit Entry", font=buttonFont, height=1, bg="black", fg="white", width=20,
       command=submitData).grid(columnspan=2, column=0, row=7)

main.mainloop()