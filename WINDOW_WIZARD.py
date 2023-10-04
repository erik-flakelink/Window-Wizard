from tkinter import * #TKINTER GUI IMPORTS

class Setup:
    def __init__(self):
        self.title = "WINDOW WIZARD"
        self.bg = "#abcdef"

Font = ("Candara", 80)

setup = Setup()
setup1 = Tk()
setup1.config(bg = setup.bg)
setup1.title(setup.title)
setup1.state('zoomed')

setup1_txt = Label(setup1, text="WINDOW WIZARD", bg = setup.bg, font=Font)
setup1_txt.pack()

Font = ("Comic Sans MS", 40)

setup1_txt = Label(setup1, text="By 'Joe'", bg = setup.bg, font=Font)
setup1_txt.pack()

image = PhotoImage(file="wizard.png") 
setup1.iconphoto(False, image)

margin_lock = False

Font = ("Candara", 20)
setup1_txt = Label(setup1, text="______________________________________________________________________", bg = setup.bg, font=Font)
setup1_txt.pack()

canvas = Canvas(setup1, width = 500, height = 600, bg = setup.bg, highlightthickness=0)      
canvas.pack()
canvas.create_image(0,0, anchor=NW, image=image)

def set_text(e, text):
    e.delete(0,END)
    e.insert(0,text)
    return

def LockMargins():
    global entryX
    global entryY
    global setup2
    global margin_lock
    margin_lock = True
    refresh()

def UnlockMargins():
    global entryX
    global entryY
    global setup2
    global margin_lock
    margin_lock = False
    refresh()

def Update():
    global marginX
    global marginY
    global entryX
    global entryY
    marginX = entryX.get()
    if margin_lock == False:
        marginY = entryY.get()
    else:
        marginY = entryX.get()
    global my_window
    try:
        my_window.geometry(f"{marginX}x{marginY}")
    except:
        my_window = Tk()
        marginX = entryX.get()
        if margin_lock == False:
            marginY = entryY.get()
        else:
            marginY = entryX.get()
        my_window.geometry(f"{marginX}x{marginY}")
    
def refresh():
    global setup2
    global entryX
    global entryY
    oldX = entryX.get()
    oldY = entryY.get()
    setup2.destroy()
    
    setup2 = Tk()
    setup2.geometry("790x520")
    setup2.config(bg = setup.bg)
    setup2.title(setup.title)
    
    
    entryX = Entry(setup2, width=4)
    set_text(entryX,oldX)
    entryX.grid()

    if margin_lock == False:
        entryY = Entry(setup2, width=4)
        set_text(entryY, oldY)
        entryY.grid()
    else:
        entryY = Entry(setup2, state=DISABLED, width=4)
        entryY.grid()
    
    MarginSet = Button(setup2, text="Set Margins", fg="black", bg=setup.bg, command=Update)
    MarginSet.grid(row=4)
    
    if margin_lock == False:
        lockMargins = Button(setup2, text="🔒", fg="black", bg=setup.bg, command=LockMargins)
        lockMargins.grid(column=1, row=0)
    elif margin_lock == True:
        lockMargins = Button(setup2, text="🔓", fg="black", bg=setup.bg, command=UnlockMargins)
        lockMargins.grid(column=1, row=0)
    
def NewWindow():
    global root
    global Font
    global setup
    global image
    global entryX
    global entryY
    global setup2
    setup1.destroy()
    setup2 = Tk()
    setup2.geometry("790x520")
    setup2.config(bg = setup.bg)
    setup2.title(setup.title)
    global my_window
    my_window = Tk()
    global custom_bg
    custom_bg = setup.bg
    my_window.resizable(False, False)
    my_window.config(bg = custom_bg)
    my_window.title("NewWindow (PREVIEW)")
    marginX = "500"
    marginY = "500"
    my_window.geometry(f"{marginX}x{marginY}")
    
    entryX = Entry(setup2, width=4)
    entryX.grid()
    
    entryY = Entry(setup2, width=4)
    entryY.grid()
    
    MarginSet = Button(setup2, text="Set Margins", fg="black", bg=setup.bg, command=Update)
    MarginSet.grid(row=4)
    
    lockMargins = Button(setup2, text="🔒", fg="black", bg=setup.bg, command=LockMargins)
    lockMargins.grid(column=1, row=0)
    

NewWin = Button(setup1, text="New Window", fg="black", bg=setup.bg, command=NewWindow)
NewWin.pack()

setup1.mainloop()
