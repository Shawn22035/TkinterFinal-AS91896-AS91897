from tkinter import *

root = Tk()
root.geometry("500x500")

Simple=Label(text="something just a test or something im not too sure tbh").pack()

def newpage():

    secondpage = Toplevel(root)
    secondpage.geometry("500x500")

    something=Label(secondpage,
                    text="something").pack()

    nameinp=Entry(secondpage)
    nameinp.pack()

    def done():
        global namepr
        namepr=nameinp.get()
        print(namepr)

    nameprint=Button(secondpage,
                     text="print",
                     command=done).pack()
                

def threepage():
    thirdpage =Toplevel(root)  
    thirdpage.geometry("500x500")

    another=Label(thirdpage,
                  text="something else").pack()

page1 = Button(text="Heres a button for a page",command=newpage).pack()

page2 = Button(text="This is a second page",command=threepage).pack()


root.mainloop()

