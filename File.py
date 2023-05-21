from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Julie's Party Hire!")

Simple=Label(text="something just a test or something im not too sure tbh").grid(column=2,row=1)

def newpage():

    secondpage = Toplevel(root)
    secondpage.geometry("500x500")
    secondpage.resizable(False,False)
    secondpage.title("Julie's Party Hire!")

    def page1done():
        secondpage.destroy()
    

    something=Label(secondpage,
                    text="something",
                    font='bold').grid(column=2,row=1)

    name=Label(secondpage, 
                text="Name:").grid(column=1,row=2, padx=60,pady=30, sticky=W)

    nameinp=Entry(secondpage).grid(column=2,row=2)

    barcodeinp=Entry(secondpage).grid(column=3,row=3)
                
    def done():
        global namepr
        namepr=nameinp.get()
        print(namepr)

    nameprint=Button(secondpage,
                     text="print",
                     command=done).grid(column=1,row=4) 
    
    somebutton=Button(secondpage,
                        text="Return!",
                        command=page1done).grid(column=3,row=4)

    invalid=Message("text didnt work")
    


def threepage(): 
    thirdpage =Toplevel(root)  
    thirdpage.geometry("500x500")

    another=Label(thirdpage,
                  text="something else").grid(column=1,row=1)

page = Button(text="Heres a button for a page",command=newpage).grid(column=1,row=2)

page2 = Button(text="This is a second page",command=threepage).grid(column=2,row=2)


root.mainloop()

