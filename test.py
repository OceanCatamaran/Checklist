#From https://stackoverflow.com/questions/5446553/tkinter-entry-character-limit

from tkinter import *

Window = Tk()
Window.geometry("200x200+50+50") # heightxwidth+x+y

mainPanel = Canvas(Window, width = 200, height = 200) # main screen
mainPanel.pack()

entry_text = StringVar() # the text in  your entry
entry_widget = Entry(mainPanel, width = 20, textvariable = entry_text) # the entry
mainPanel.create_window(100, 100, window = entry_widget)

def character_limit(entry_text):
    if len(entry_text.get()) > 5:#If greater than set character max...
        entry_text.set(entry_text.get()[:-1])#Will prevent user from typing more characters.

entry_text.trace("w", lambda *args: character_limit(entry_text))
