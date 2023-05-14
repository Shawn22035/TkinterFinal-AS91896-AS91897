from tkinter import *

root = Tk()
root.geometry("500x500")

Simple=Label(text="something just a test or something im not too sure tbh")
Simple.pack()

def newpage():

    secondpage = Toplevel(root)

    secondpage.geometry("500x500")

    something=Label(secondpage,
                    text="something").pack()

def threepage():

    thirdpage =Toplevel(root)  
    thirdpage.geometry("500x500")

    another=Label(thirdpage,
                  text="something else").pack()

page1 = Button(text="Heres a button for a page",command=newpage)
page1.pack()

page2 = Button(text="This is a second page",command=threepage)
page2.pack()
root.mainloop()

