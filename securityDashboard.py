import tkinter as tk
from PIL import Image, ImageTk
import sys
import loginWindow as lw
#import MainUI2 as mu
import roomSelection as rs

#Function for watching student
def watching():
    top.destroy()
    #mu.call1()    
    rs.loadRoomSelection()

#Function for go back
def back():
    top.destroy()
    lw.loadForm()


#Function for load security dashboard
def loadSecurityForm():
    global top
    top = tk.Tk()

    top.title("Security Dashboard")
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

    button2 = tk.Button(top,
                             text="Watch",
                             fg="red",
                             width=25,
                              command=watching
                             )

    button2.place(x=72, y=220)

    button4 = tk.Button(top,
                             text="Go Back",
                             fg="red",
                             width=25,
                             command=back
                             )

    button4.place(x=72, y=250)

    top.mainloop()



