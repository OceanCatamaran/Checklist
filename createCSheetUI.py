from tkinter import *
from sizeableList import SizeableList
from EntryReader import EntryReader
from ObjectListBox import ObjectListBox
from clCalendar import CLCalendar

top = Tk()
top.geometry("600x600")

#viewport for category data
catViewport = Frame(top, width = 40, height = 20)

catScrollbar = Scrollbar(catViewport)
catScrollbar.pack(side = RIGHT, fill = Y)

catOLB = ObjectListBox(catViewport, 5, yscrollcommand = catScrollbar.set)
catOLB.pack()

#viewport for date data
datViewport = Frame(top, width = 40, height = 20)

datScrollbar = Scrollbar(datViewport)
datScrollbar.pack(side = RIGHT, fill = Y)

datOLB = ObjectListBox(datViewport, 5, yscrollcommand = datScrollbar.set)
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

#Laying out top window 
catViewport.place(x = 0, y = 0)
datViewport.place(x = 140, y = 0)
catScrollbar.config(command = catOLB.yview())
datScrollbar.config(command = datOLB.yview())
catCFrame.place(x = 0, y = 160)
datCFrame.place(x = 141, y = 160)


#Running
top.mainloop()
