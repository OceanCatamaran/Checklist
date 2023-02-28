from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import tkinter.messagebox as box
import shutil
from FileSearchEngine import search_file
import time
window = Tk()
window.title( 'Select C-Sheet' )

frame = Frame( window )
treeview = ttk.Treeview(frame, column = ("C-Sheets", "Date"), show='headings', height = 30)
treeview.heading('C-Sheets', text = 'C-Sheets')
treeview.heading('Date', text = 'Date')
path = os.getcwd() + "//C-sheet"
search_f = search_file()
def get_all_csheet_name():
    dir_list = os.listdir(path);
    return dir_list

def get_all_csheet_date():
    file_name = get_all_csheet_name()
    named_path = [path+"//"+name  for name in file_name]
    file_date = [time.ctime(os.path.getmtime(p)) for p in named_path]
    return file_date
all_csheet_name = get_all_csheet_name()
all_csheet_date = get_all_csheet_date()
def select_treeview():
    treefocus = treeview.focus()
    treeitem = treeview.item(treefocus)
    if(treeitem.get("values") == ''):
        messagebox.showwarning(title = "C-sheet Not Selected", message = "Please Select a C-sheet.")
        return None
    return treeitem.get("values")[0]

def refresh_csheet_info(csheet_name = all_csheet_name, csheet_date = all_csheet_date):
    for item in treeview.get_children():
        treeview.delete(item)
    for num, name_date in enumerate(zip(csheet_name, csheet_date), 1):
    
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
def search_csheet():
    file_name = []
    file_date = []
    search_f.create_new_index(path)
    text = search_bar.get("1.0", "end-1c")
    search_f.search(text)
    for name in search_f.results:
        file_date.append(time.ctime(os.path.getmtime(name)))
        tmp = name.split("C-sheet/")
        file_name.append(tmp[1])
    refresh_csheet_info(file_name, file_date)
    
refresh_csheet_info()
search_bar = Text(frame, height = 1 ,width = 30)
search_btn = Button( frame, text = "Search", command=search_csheet)
edit_btn = Button( frame, text = 'Edit', command=edit_csheet)
view_btn = Button( frame, text = "View", command=view_csheet)
delete_btn =  Button( frame, text = "Delete", command=delete_csheet)
copy_btn =  Button( frame, text = "Copy", command=copy_csheet)
search_bar.pack(side = TOP, pady = 5, anchor = "w")
search_btn.pack(side = TOP, pady = 5, anchor = "w")
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
