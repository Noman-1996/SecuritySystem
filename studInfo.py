import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import queries as q
import adminDashboard as ad
#import MainUI2 as ui
import LBPH as lbph
import os


id = name = degree = semister = status = None
top = None

def studentTrainingExist(filePath):
    exists = os.path.isfile(filePath)
    if exists:        
        return True
    else:
        os.makedirs(filePath)
        return False

#Function for inserting student
def insert():
    exists = studentTrainingExist("TrainingData/" + id.get())
    if exists == False:
        if id.get() != '' and name.get() != '' and degree.get() != '' and semister.get() != '' and status.get() != '':
            if q.insertData(id.get(), name.get(), degree.get(), semister.get(), status.get()) is not None:
                studID = id.get()
                top.destroy()
                lbph.trainStudent(studID)
                #ui.call1(mat)
            else:
                messagebox.showerror('Error', 'Data Insertion Failed2')
        else:        
            messagebox.showerror('Error', 'Some feilds are empty')    
    else:
        messagebox.showerror('Error', 'Training Exist of the same ID')    


#Function for going back
def back():
    top.destroy()
    ad.loadAdminForm()


def loadStudInfoForm():
    global id, name, degree, semister, status, top

    top = tkinter.Tk()

    id = tkinter.StringVar(top)
    name = tkinter.StringVar(top)
    degree = tkinter.StringVar(top)
    semister = tkinter.StringVar(top)
    status = tkinter.StringVar(top)

    top.title("Student Information Form")

    top.resizable(False, False)

    
    winWidth = 350
    winHeight = 500

    screenWidth = top.winfo_screenwidth()
    screenHeight = top.winfo_screenheight()

    xPoint = (screenWidth/2) - (winWidth/2)
    yPoint = (screenHeight/2) - (winHeight/2)

    top.geometry("%dx%d+%d+%d" % (winWidth,winHeight,xPoint,yPoint))

    top.iconbitmap("images/icon.ico")    

    bard = Image.open("images/user.png")
    bard = bard.resize((100, 100))
    bardejov = ImageTk.PhotoImage(bard)

    label1 = tkinter.Label(top, image=bardejov)
    label1.place(x=112, y=20)

    button = tkinter.Button(top,
                            text="Next",
                            fg="red",
                            width=27,
                            command=insert
                            )
    idLabel = tkinter.Label(top, text = 'ID:', font = {'Helvetica',10})
    idLabel.place(x=70, y=130)
    tx = tkinter.Entry(top, width=32, textvariable=id)
    tx.place(x=70, y=150)    

    nameLabel = tkinter.Label(top, text = 'Name:', font = {'Helvetica',10})
    nameLabel.place(x=70, y=180)
    tx2 = tkinter.Entry(top, width=32, textvariable=name)
    tx2.place(x=70, y=200)
    
    degreeLabel = tkinter.Label(top, text = 'Degree:', font = {'Helvetica',10})
    degreeLabel.place(x=70, y=230)
    tx3 = tkinter.Entry(top, width=32, textvariable=degree)
    tx3.place(x=70, y=250)    

    semiLabel = tkinter.Label(top, text = 'Semister:', font = {'Helvetica',10})
    semiLabel.place(x=70, y=280)
    tx4 = tkinter.Entry(top, width=32, textvariable=semister)
    tx4.place(x=70, y=300)
    
    statusLabel = tkinter.Label(top, text = 'Status:', font = {'Helvetica',10})
    statusLabel.place(x=70, y=330)
    tx5 = tkinter.Entry(top, width=32, textvariable=status)
    tx5.place(x=70, y=350)


    button.place(x=70, y=400)

    button1 = tkinter.Button(top,
                            text="Go Back",
                            fg="red",
                            width=27,
                            command=back
                            )

    button1.place(x=70, y=430)

    top.mainloop()


