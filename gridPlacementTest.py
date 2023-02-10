#This py file was taken from the below website...
#Link: https://www.tutorialspoint.com/how-do-i-change-button-size-in-python-tkinter
#I modified the above file to experiment with tkinter's grid placement.

#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("600x800")

win.resizable(False, False)

#Add buttons and set their placement on root.
Button(win, text="Button-1",height= 5, width=10).place(x = 0, y = 0)
Button(win, text="Button-2",height=8, width=15).place(x = 100, y = 0)
Button(win, text= "Button-3",height=10, width=30).place(x = 0, y = 150)

win.mainloop()
