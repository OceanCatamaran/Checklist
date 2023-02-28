#From https://stackoverflow.com/questions/5446553/tkinter-entry-character-limit

from tkinter import *

Window = Tk()
Window.geometry("200x200+50+50") # heightxwidth+x+y

mainPanel = Canvas(Window, width = 200, height = 200) # main screen
mainPanel.pack()

eObjVar = StringVar() # the text in  your entry
eObj = Entry(mainPanel, width = 20, textvariable = eObjVar) # the entry
mainPanel.create_window(100, 100, window = eObj)

def character_limit(eObjVar):
    if len(eObjVar.get()) > 50:#If greater than set character max...
        eObjVar.set(eObjVar.get()[:-1])#Will prevent user from typing more characters.

eObjVar.trace("w", lambda *args: character_limit(eObjVar))
