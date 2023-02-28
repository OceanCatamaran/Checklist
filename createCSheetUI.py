from tkinter import *
from sizeableList import SizeableList
from EntryReader import EntryReader
from ObjectListBox import ObjectListBox
from clCalendar import CLCalendar
from frameSignaler import FrameSignaler
from fileManager import FileManager
from grid import Grid


class CreateCSheetUI:

    @classmethod
    def addFrame(self, window, fsObj):
        #This method adds the screen to the window from UIManager.
        def frameMaker(display = False):

            if display:
                master = Frame(window, width = 800, height = 600, relief = "groove", borderwidth = 2)
                #top groups cat and dat related widgets together.
                top = Frame(master, width = 285, height = 344, relief = "groove", borderwidth = 2)

                ##'''Add Name Label and Name Entry Box here.'''
                nameLabel = Label(master, text = "Name:", relief = "groove", borderwidth = 2)
                nameEntry = Entry(master, width = 50)
                noteLabel = Label(master, text = "Note:", relief = "groove", borderwidth = 2)
                noteText = Text(master, width = 50, height = 5)

                #viewport for category data
                catViewport = Frame(top, width = 40, height = 20)

                catScrollbar = Scrollbar(catViewport)
                catScrollbar.pack(side = RIGHT, fill = Y)

                catOLB = ObjectListBox(catViewport, 0, yscrollcommand = catScrollbar.set)
                catOLB.pack()

                #viewport for date data
                datViewport = Frame(top, width = 40, height = 20)

                datScrollbar = Scrollbar(datViewport)
                datScrollbar.pack(side = RIGHT, fill = Y)

                datOLB = ObjectListBox(datViewport, 0, yscrollcommand = datScrollbar.set)
                datOLB.pack()

                #inputs beneath catViewport
                catCFrame = Frame(top, width = 140, height = 180, relief = "groove", borderwidth = 2)
                    #The C in catCFrame stands for controller (as it controls the cat. data)
                catEntryObj = Entry(catCFrame, width = 15)
                catNumEntryObj = Entry(catCFrame, width = 5)
                catNumEntryObj.insert(0, "1")
                catERObj = EntryReader(catNumEntryObj)

                #inputs beneath dateViewPort
                datCFrame = Frame(top, width = 140, height = 180, relief = "groove", borderwidth = 2)
                datEntryObjBeg = Entry(datCFrame, width = 15)
                datEntryObjEnd = Entry(datCFrame, width = 15)
                datUnit = IntVar()
                '''Need to create specialized EntryReader for dates!
                   Until then, for testing purposes, will have to assume
                   user input will not be incorrect!'''

                #CallBacks for the catCFrame Controls
                def catSelectCallBack():
                    selection = catOLB.selection()
                    if len(selection) == 0:
                        selection = None
                    #.get only retrieves the selected line in the Listbox, and its parallel in
                    # the sizeableList object.
                    if selection != None:
                        catOLB.insertAt(selection[0], catEntryObj.get())
                        print(catOLB.get(selection[0]))

                def decrementCallBack():
                    catOLB.decrement(catERObj.getNumber())

                def incrementCallBack():
                    catOLB.increment(catERObj.getNumber())

                #CallBacks for the datCFrame Controls
                def datSelectCallBack():
                    num = datUnit.get()
                    print(str(num) + " is of type " + str(type(num)))
                    val_1 = datEntryObjBeg.get()
                    val_2 = datEntryObjEnd.get()
                    result = CLCalendar.getColumns(num, val_1, val_2)
                    if result != None:
                        datOLB.overWriteWith(result)
                        print(datOLB.getList())
 
                ##Add Clear, Create, and Back Callbacks here.
                def clearData():
                    catOLB.setSize(0)
                    datOLB.setSize(0)
                    nameEntry.delete(0, END)
                    noteText.delete("0.0", "end")

                def createCSheet():
                    catList = catOLB.getList()
                    datList = datOLB.getList()
                    fileName = nameEntry.get()
                    noteStr = "".join(noteText.get("0.0", "end").split("\n"))

                    gObj = Grid(len(catList), len(datList))
                    gObj.setDates(datList)
                    gObj.setCategories(catList)
                    gObj.setNotes(noteStr)

                    FileManager.createFile(gObj, fileName)

                    for widget in window.winfo_children():
                        widget.destroy()
                    fsObj.setFlag("logCSheetUI")
                    fsObj.setData(fileName)
                    

                def back():
                    for widget in window.winfo_children():
                        widget.destroy()
                    fsObj.setFlag("homepageUI")
                    fsObj.setData("")
                    

                '''
                #mouseCallback taken from this site...
                ##Link: https://www.tutorialspoint.com/mouse-position-in-python-tkinter   
                def mouseCallBack(e):
                ##Helps in placement of widget
                   x= e.x
                   y= e.y
                   print("Pointer is currently at %d, %d" %(x,y))
                ##Commented out below line as it is only used for determining widget placement.
                catCFrame.bind('<Motion>', mouseCallBack)
                '''
                 
                #catCFrame Controls
                catSet = Button(catCFrame, text = "set", command = catSelectCallBack, width = 3, height = 1)
                leftB = Button(catCFrame, text = "-", command = decrementCallBack, width = 2, height = 3)
                rightB = Button(catCFrame, text = "+", command = incrementCallBack, width = 2, height = 3)

                #datCFrame Controls
                datSet = Button(datCFrame, text = "set", command = datSelectCallBack, width = 3, height = 1)
                RB_1 = Radiobutton(datCFrame, text = "DateRange", variable = datUnit, value = 1)
                RB_2 = Radiobutton(datCFrame, text = "YearlessDateRange", variable = datUnit, value = 2)
                RB_3 = Radiobutton(datCFrame, text = "YearRange", variable = datUnit, value = 3)
                RB_4 = Radiobutton(datCFrame, text = "MonthRange", variable = datUnit, value = 4)
                RB_5 = Radiobutton(datCFrame, text = "DayRange", variable = datUnit, value = 5)
                RB_6 = Radiobutton(datCFrame, text = "NumRange", variable = datUnit, value = 6)

                #Clear, Create, and Back Controls
                clearB = Button(master, text = "Clear", command = clearData, width = 8, height = 2)
                createB = Button(master, text = "Create", command = createCSheet, width = 8, height = 2)
                backB = Button(master, text = "Back", command = back, width = 8, height = 2)

                #Laying out catCFrame
                catEntryObj.place(x = 0, y = 3)
                catSet.place(x = 97, y = 0)
                leftB.place(x = 0, y = 40)
                catNumEntryObj.place(x = 50, y = 57)
                rightB.place(x = 110, y = 40)

                #Laying out datCFrame
                datEntryObjBeg.place(x = 0, y = 0)
                datEntryObjEnd.place(x = 0, y = 20)
                datSet.place(x = 97, y = 0)
                RB_1.place(x = 0, y = 40)
                RB_2.place(x = 0, y = 60)
                RB_3.place(x = 0, y = 80)
                RB_4.place(x = 0, y = 100)
                RB_5.place(x = 0, y = 120)
                RB_6.place(x = 0, y = 140)

                ##Add Name, Name Entry box, Clear, Create, and Back Controls here.
                #Laying out top window 
                catViewport.place(x = 0, y = 0)
                datViewport.place(x = 140, y = 0)
                catScrollbar.config(command = catOLB.yview())
                datScrollbar.config(command = datOLB.yview())
                catCFrame.place(x = 0, y = 160)
                datCFrame.place(x = 141, y = 160)
                nameLabel.place(x = 100, y= 0)
                nameEntry.place(x = 150, y = 0)
                clearB.place(x = 650, y = 500)
                createB.place(x = 720, y = 500)
                backB.place(x = 0, y = 0)
                noteLabel.place(x = 150, y = 500)
                noteText.place(x = 200, y = 500)

                #packing top
                top.place(x = 250, y = 100)
                master.place(x = 0, y = 0)
        frameMaker()
        return ["createCSheetUI", frameMaker]

    @classmethod
    def testFrame(self):
        #This method is for testing the screen by itself
        #Note, non-home Screens must use this testFrame code
        #as it is different from the testFrame method in the
        #Home Screen class.
        window = Tk()
        window.geometry("800x600")
        fsObj = FrameSignaler
        temp = self.addFrame(window, fsObj)
        temp[1](True)

        def printFrameSignaler():
            print(fsObj.getFlag())
            print(fsObj.getData())
            window.after(1000, printFrameSignaler)

        printFrameSignaler()

        window.mainloop()

if __name__ == "__main__":
    CreateCSheetUI.testFrame()
