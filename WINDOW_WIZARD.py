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

Font = ("Candara", 20)
setup1_txt = Label(setup1, text="______________________________________________________________________", bg = setup.bg, font=Font)
setup1_txt.pack()

canvas = Canvas(setup1, width = 500, height = 600, bg = setup.bg, highlightthickness=0)      
canvas.pack()
canvas.create_image(0,0, anchor=NW, image=image)

def NewWindow():
    global root
    global Font
    global setup
    setup1.destroy()
    setup2 = Tk()
    setup2.config(bg = setup.bg)
    setup2.title(setup.title)
    setup2.state('zoomed')
    image = PhotoImage(file="wizard.png")
    setup2.iconphoto(False, image)

NewWin = Button(setup1, text="New Window", fg="black", bg=setup.bg, command=NewWindow)
NewWin.pack()
