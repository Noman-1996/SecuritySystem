import tkinter as tk
from PIL import Image, ImageTk
import sys
import studInfo as si
import loginWindow as lw
import LBPH as lbph
#import GetAllStudent as st
#import MainUI as mu


def testing():
    #top.destroy()
    lbph.prediction(0)
    #mu.call1()
    

def studentinfo():
    top.destroy()
    #st.call1()
    

def training():
    top.destroy()
    si.loadStudInfoForm()

def back():
    top.destroy()
    lw.loadForm()



#Function for loading  Admin Dashboard
def loadAdminForm():
    global top
    top = tk.Tk()

    top.title("Admin Dashboard")
    top.iconbitmap("images/icon.ico")

    top.resizable(False, False)

    winWidth = 350
    winHeight = 350

    screenWidth = top.winfo_screenwidth()
    screenHeight = top.winfo_screenheight()

    xPoint = (screenWidth/2) - (winWidth/2)
    yPoint = (screenHeight/2) - (winHeight/2)

    top.geometry("%dx%d+%d+%d" % (winWidth,winHeight,xPoint,yPoint))

    bard = Image.open("images/stu.png")
    bard = bard.resize((100, 100))
    bardejov = ImageTk.PhotoImage(bard)

    label1 = tk.Label(top, image=bardejov)
    label1.place(x=112, y=20)

    button = tk.Button(top,
                            text="Training",
                            fg="red",
                            width=25,
                            command=training
                            )

    button.place(x=72, y=180)

    button2 = tk.Button(top,
                             text="Testing",
                             fg="red",
                             width=25,
                              command=testing
                             )

    button2.place(x=72, y=220)

    button3 = tk.Button(top,
                             text="Get Student",
                             fg="red",
                             width=25,
                             command=studentinfo
                             )

    button3.place(x=72, y=260)

    button4 = tk.Button(top,
                             text="Go Back",
                             fg="red",
                             width=25,
                             command=back
                             )

    button4.place(x=72, y=300)

    top.mainloop()
