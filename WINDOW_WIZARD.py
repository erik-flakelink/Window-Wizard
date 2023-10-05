from tkinter import * #TKINTER GUI IMPORTS

class Separator(Widget):
    """Ttk Separator widget displays a horizontal or vertical separator
    bar."""

    def __init__(self, master=None, **kw):
        """Construct a Ttk Separator with parent master.

        STANDARD OPTIONS

            class, cursor, style, takefocus

        WIDGET-SPECIFIC OPTIONS

            orient
        """
        Widget.__init__(self, master, "ttk::separator", kw)


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
    global my_window
    global marginX
    global marginY
    global entryX
    global entryY
    global setup2
    marginX = entryX.get()
    if margin_lock == False:
        marginY = entryY.get()
    else:
        marginY = entryX.get()
    try:
        my_window.geometry(f"{marginX}x{marginY}")
        my_window.resizable(False, False)
        my_window.config(bg = custom_bg)
        my_window.title("NewWindow (PREVIEW)")
    except:
        my_window = Tk()
        my_window.geometry(f"{marginX}x{marginY}")
        my_window.resizable(False, False)
        my_window.config(bg = custom_bg)
        my_window.title("NewWindow (PREVIEW)")
    
def refresh():
    global setup2
    global entryX
    global entryY
    try:
        oldX = entryX.get()
        oldY = entryY.get()
    except:
        oldX = "500"
        oldY = "500"

    try:
        setup2.destroy()
    except:
        pass
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
    
    MarginSet = Button(setup2, text="Apply", fg="black", bg=setup.bg, command=Update)
    MarginSet.grid(row=4)
    
    if margin_lock == False:
        lockMargins = Button(setup2, text="🔒", fg="black", bg=setup.bg, command=LockMargins)
        lockMargins.grid(column=1, row=0)
    elif margin_lock == True:
        lockMargins = Button(setup2, text="🔓", fg="black", bg=setup.bg, command=UnlockMargins)
        lockMargins.grid(column=1, row=0)
    global Font
    Font = ("STENCIL", 15)
    LABEL1 = Label(setup2, text="MARGINS", font=Font, bg=setup.bg)
    LABEL1.grid(column=0)
    SEPARATE = Separator(setup2, orient='vertical').grid(column=2, row=0, rowspan=8, sticky='ns')
    SEPARATE2 = Separator(setup2, orient='horizontal').grid(row=8,column=0,columnspan=8, ipadx=57) 
def NewWindow():
    global root
    global Font
    global setup
    global image
    global entryX
    global entryY
    global setup2
    setup1.destroy()
    global oldX
    global oldY
    oldX = "500"
    oldY = "500"
    refresh()
    global my_window
    my_window = Tk()
    global custom_bg
    custom_bg = setup.bg
    my_window.resizable(False, False)
    my_window.config(bg = custom_bg)
    my_window.title("NewWindow (PREVIEW)")
    marginX = oldX
    marginY = oldY
    my_window.geometry(f"{marginX}x{marginY}")

NewWin = Button(setup1, text="New Window", fg="black", bg=setup.bg, command=NewWindow)
NewWin.pack()

setup1.mainloop()
