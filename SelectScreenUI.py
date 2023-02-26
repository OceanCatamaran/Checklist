from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from FileSee import file_info
import os
import tkinter.messagebox as box
import shutil
window = Tk()
window.title( 'Select C-Sheet' )

frame = Frame( window )
treeview = ttk.Treeview(frame, column = ("C-Sheets", "Date"), show='headings', height = 30)
treeview.heading('C-Sheets', text = 'C-Sheets')
treeview.heading('Date', text = 'Date')
file_data = file_info()
def select_treeview():
    treefocus = treeview.focus()
    treeitem = treeview.item(treefocus)
    if(treeitem.get("values") == ''):
        messagebox.showwarning(title = "C-sheet Not Selected", message = "Please Select a C-sheet.")
        return None
    return treeitem.get("values")[0]

def refresh_csheet_info():
    all_csheet_name = file_data.get_all_csheet_name()
    all_csheet_date = file_data.get_all_csheet_date()
    for item in treeview.get_children():
        treeview.delete(item)
    for num, name_date in enumerate(zip(all_csheet_name, all_csheet_date), 1):
    
        treeview.insert('', 'end', text=num,values=(name_date[0], name_date[1], num))

def delete_csheet():
   selected = select_treeview()
   if(selected):
        if("yes" == messagebox.askquestion(title="Delete Confirmation", message = "Are you sure you want to Delete this C-sheet")):        
            os.remove(file_data.path+"//"+selected)
            refresh_csheet_info()
def view_csheet():
    if(selected):
        pass    
def edit_csheet():
    if(selected):
        pass
def copy_csheet():
    selected = select_treeview()
    if(selected):
        file_split = selected.split(".")
        file_split[0] = file_split[0]+"_1"  
        file_copy = ".".join(file_split)
        shutil.copy(file_data.path + "//" + selected, file_data.path+"//"+file_copy)
        refresh_csheet_info()

refresh_csheet_info()
search_bar = Text(frame, height = 1 ,width = 50)
edit_btn = Button( frame, text = 'Edit', command=edit_csheet)
view_btn = Button( frame, text = "View", command=view_csheet)
delete_btn =  Button( frame, text = "Delete", command=delete_csheet)
copy_btn =  Button( frame, text = "Copy", command=copy_csheet)
search_bar.pack(side = TOP, pady = 5, anchor = "w")
edit_btn.pack(side = RIGHT, padx = 5)
view_btn.pack(side = RIGHT, padx = 5)   
delete_btn.pack( side = RIGHT , padx = 5 )
copy_btn.pack( side=RIGHT, padx = 5)

treeview.pack( side = LEFT )
verscrlbar = ttk.Scrollbar(window,
                           orient ="vertical",
                           command = treeview.yview)

verscrlbar.pack(side ='right', fill ='x')
 
# Configuring treeview
treeview.configure(xscrollcommand = verscrlbar.set)
frame.pack( padx = 30, pady = 30 )

window.mainloop()
