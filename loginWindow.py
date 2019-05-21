import tkinter
from PIL import Image, ImageTk
import queries as q
import adminDashboard as ad
from tkinter import messagebox
import securityDashboard as sd

#Function for autentication user
def check():
    result = q.auth(name.get(), pas.get())
    if result is not None:            
        if result[3] == "admin":
            top.destroy()
            ad.loadAdminForm()
        elif result[3] == "security":
            top.destroy()
            sd.loadSecurityForm()
    else:
        messagebox.showerror('Error', 'Login Failed')        

#Function for loading login form
def loadForm():

    global name, pas, top
    top = tkinter.Tk()
    
    name = tkinter.StringVar(top)
    pas = tkinter.StringVar(top)

    top.title("Login")
    top.iconbitmap("images/icon.ico")
    top.resizable(False, False)

    winWidth = 350
    winHeight = 350

    screenWidth = top.winfo_screenwidth()
    screenHeight = top.winfo_screenheight()

    xPoint = (screenWidth/2) - (winWidth/2)
    yPoint = (screenHeight/2) - (winHeight/2)

    top.geometry("%dx%d+%d+%d" % (winWidth,winHeight,xPoint,yPoint))

    bard = Image.open("images/user.png")
    bard = bard.resize((100, 100))
    bardejov = ImageTk.PhotoImage(bard)

    label1 = tkinter.Label(top, image=bardejov)
    label1.place(x=112, y=20)

    button = tkinter.Button(top,
                            text="Login",
                            fg="red",
                            width=27,
                            command=check
                            )
    userLabel = tkinter.Label(top, text = 'ID:', font = {'Helvetica',10})
    userLabel.place(x=70, y=130)
    tx = tkinter.Entry(top, width=32, textvariable=name)
    tx.place(x=70, y=150)

    passLabel = tkinter.Label(top, text = 'Pasword:', font = {'Helvetica',10})
    passLabel.place(x=70, y=180)
    tx2 = tkinter.Entry(top, width=32, show='*', textvariable=pas)
    tx2.place(x=70, y=200)
    button.place(x=70, y=250)

    top.mainloop()


#Starting Point
if __name__ == '__main__':
    loadForm()