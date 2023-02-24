from tkinter import *
from tkinter import messagebox
#from tkinter.tkk import *

global DEBUG_MODE
DEBUG_MODE = True


def openPopup():
    if DEBUG_MODE:
        print("DEBUG: Open Popoup")
    messagebox.showwarning("C-Sheet Deleted", "C-Sheet Deleted")


if __name__ == "__main__":
    if DEBUG_MODE:
        print("DEBUG: Program start")

    # Create the Main Window of the application named root
    global root
    root = Tk()

    root.title("Window Title")
    root.geometry("400x400")

    
    label = Label(root, text = "Clicking This Button Will Activate Popup").pack()
    # what does pack do

    activate_popup =  Button(root, text="Click Me!", command=openPopup).pack()


    root.mainloop()