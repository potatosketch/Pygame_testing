from tkinter import *
import tkinter.messagebox

#>exercise8< (using class)
#class BuckysButton:
    #def __init__(self,master):
        #frame = Frame(master)
        #frame.pack()

        #self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        #self.printButton.pack(side=LEFT)

        #self.quitButton = Button(frame, text="Quit", command=frame.quit)
        #self.quitButton.pack(side=LEFT)

    #def printMessage(self):
        #print("Wow")

#>exercise9 (creating menu)
def doNothing():
    print("ok ok I won't...")

def answer():
    answer = tkinter.messagebox.askquestion('Question1', 'ya mama gay?')
    if answer == 'yes':
         print(':o')


root = Tk()
#>exercise1<
#theLabel = Label(root, text="This is too easy")
#theLabel.pack()

#>exercise2<
#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side = BOTTOM)

#button1 = Button(topFrame, text = "button 1", fg = "red")
#button2 = Button(topFrame, text = "button 2", fg = "blue")
#button3 = Button(topFrame, text = "button 3", fg = "green")
#button4 = Button(bottomFrame, text = "button 4", fg = "purple")

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=BOTTOM)

#>exercise3<
#one = Label(root, text = "One", bg = "red", fg="white")
#one.pack()
#two = Label(root, text = "Two", bg = "green", fg="black")
#two.pack(fill = X)
#three = Label(root, text = "Three", bg = "blue", fg="white")
#three.pack(side = LEFT, fill = Y)

#>exercise4< (using Grid Layout)
#label_1 = Label(root, text="Name")
#label_2 = Label(root, text="Password")
#entry_1 = Entry(root)
#entry_2 = Entry(root)

#label_1.grid(row=0)
#label_2.grid(row=1)

#entry_1.grid(row=0, column=1)
#entry_2.grid(row=1, column=1)

#>exercise5< (sticky and checkbox)
#label_1 = Label(root, text="Name")
#label_2 = Label(root, text="Password")
#entry_1 = Entry(root)
#entry_2 = Entry(root)

#label_1.grid(row=0, sticky=E)
#label_2.grid(row=1, sticky=E)

#entry_1.grid(row=0, column=1)
#entry_2.grid(row=1, column=1)

#c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2, sticky=W)

#>exercise5< (binding function)
#def printName(event):
    #print("Chello my name is Bucky")

#button_1 = Button(root, text="Print my name")
#button_1.bind("<Button-1>", printName)
#button_1.pack()

#>exercise6< (command call up)
#def printName():
    #print("Chello my name is Bucky")

#button_1 = Button(root, text="Print my name", command = printName)
#button_1.pack()

#>exercise7< (different mouse clicking)
#def leftClick(event):
    #print("Left")

#def middleClick(event):
    #print("Middle")

#def rightClick(event):
    #print("Right")

#frame = Frame(root, width=300, height=300)
#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)
#frame.pack()

#>exercise8< (using class)
#b = BuckysButton(root)

#>exercise9< (creating menu)
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)

subMenu1 = Menu(menu)
menu.add_cascade(label="Edit", menu=subMenu1)
subMenu1.add_command(label="Redo",command=doNothing)

#>exercise10< (building toolbar)
# ****** tool bar *******
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side = LEFT, padx=10, pady=10)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side = LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#self exercise#
butt1 = Button(root, text="click it!", command = answer)
butt1.pack(side=TOP)
if answer == 'yes':
    print(':o')

canvas = Canvas(root, width =200, height=100)
canvas.pack(side=TOP)

blackline = canvas.create_line(0,0,200,50)
redline = canvas.create_line(0,100,200,50,fill = "red")
greenBox = canvas.create_rectangle(25, 25,130,60,fill="green")
#blueBox = canvas.create_rectangle(25, 0,25,25,fill="blue"
canvas.delete(redline)
#canvas.delete(ALL)

photo = PhotoImage(file="pika.png")
label = Label(root, image=photo)
label.pack()
#>exercise11< (building statue bar)
# ****** Status Bar ********
status = Label(root, text="Preparing to do no nothing...",bd = 10,relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#>exercise12< (message box)
#tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years.')
#answer = tkinter.messagebox.askquestion('Question1', 'ya mama gay?')

#if answer == 'yes':
    #print(':o')


root.mainloop()
