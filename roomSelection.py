import tkinter
from PIL import Image, ImageTk
import sys
import queries as q
# import MainWin2 as mw2
from tkinter import messagebox
import LBPH as lbph
import securityDashboard as sd

li = []

listbox = None

top = None

ad = {}

name = ""

def back():
    top.destroy()
    sd.loadSecurityForm()

def pasto():
    try:
        ind = listbox.get(listbox.curselection())
        # top.destroy()
        #mw2.cal3(ad[ind],name)
        lbph.prediction(0)


    except Exception as e:
        print(e)
        messagebox.showerror('Error', 'Select Any Room')
    

def loadRoomSelection():
    global li, listbox, ad, top, name

    # name = va

    li.clear()

    ad.clear()

    for i in q.getRooms():
        li.append(i[0])  #(i[0])
        ad[i[0]] = i[1] #ip camera value

    top = tkinter.Tk()

    top.title("Room Selection")

    top.resizable(False, False)

    top.geometry("500x600+500+50")

    bards = Image.open("images/stu.png")
    bards = bards.resize((200, 200))
    bardejovs = ImageTk.PhotoImage(bards)

    label1s = tkinter.Label(top, image=bardejovs)
    label1s.place(x=140, y=20)

    listbox = tkinter.Listbox(top, width=75, height=18, selectforeground='white')
    listbox.place(x=20, y=290)

    for item in li:
        listbox.insert(tkinter.END, item)

    button = tkinter.Button(top,
                            text="Next",
                            fg="red",
                            width=25,
                            command=pasto
                            )

    button.place(x=142, y=230)
    
    button1 = tkinter.Button(top,
                            text="Go Back",
                            fg="red",
                            width=25,
                            command=back
                            )

    button1.place(x=142, y=250)
    

    top.mainloop()
