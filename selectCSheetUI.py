import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from fileManager import FileManager
from frameSignaler import FrameSignaler

class SelectCSheetUI:
    @classmethod
    def addFrame(self, window, fsObj):
        #This method adds the screen to the uiManager
        def frameMaker(display = False):
            if display:
                frame = Frame(window, width = 800, height = 600, relief = "groove", borderwidth = 2, bg = "white")
                treeview = ttk.Treeview(frame, column = ("C-Sheets", "Date"), show='headings', height = 30)
                treeview.heading('C-Sheets', text = 'C-Sheets')
                treeview.heading('Date', text = 'Date')

                #Banner
                bfObj = Frame(window, width = 800, height = 94, bg= "white")
                banner = PhotoImage(file = "BSelectCSheet.gif")
                bannerLabel = Label(bfObj, image = banner)
                bannerLabel.image = banner

                bfObj.pack(fill = "both")
                bannerLabel.pack(fill = "both")

                #Backend functions

                def select_treeview():
                    treefocus = treeview.focus()
                    treeitem = treeview.item(treefocus)
                    if(treeitem.get("values") == ''):
                        messagebox.showwarning(title = "C-sheet Not Selected", message = "Please Select a C-sheet.")
                        return None
                    return treeitem.get("values")[0]

                def refresh_csheet_info(fileName = None, fileDate = None):
                    #Deleting children in tree
                    for item in treeview.get_children():
                        treeview.delete(item)
                    
                    if (fileName != None) and (fileDate != None):
                        treeview.insert('', 'end', text = 1, values = (fileName, fileDate, 1))
                        
                    else:
                        #If at least one arg is None, function assumes
                        #no single fileName and/or fileDate has been passed.
                        fileNames = FileManager.getFileNames()
                        fileDates = FileManager.getFileDates()

                        if (len(fileNames) == 1):
                            treeview.insert('', 'end', text = 1, values = (fileNames[0], fileDates[0], 1))

                        else:
                            #If there is more than one fileName, it is assumed
                            #there are also more than one corresponding fileDates.
                            #Since there are multiple rather than only one cSheets
                            #in the SavedData folder, the tree will display all of them.
                        
                            for num, name_date in enumerate(zip(fileNames, fileDates), 1):
                                treeview.insert('', 'end', text=num,values=(name_date[0], name_date[1], num))

                #GUI functions

                def search_csheet():
                    text = search_bar.get()[0:30]
                    if (text == ""):
                        refresh_csheet_info()
                    else:
                        fileNames = FileManager.getFileNames()
                        fileDates = FileManager.getFileDates()
                        fileNotFound = True
                        for i in range(len(fileNames)):
                            if fileNames[i].lower() == text.lower():

                                refresh_csheet_info(fileNames[i], fileDates[i])
                                fileNotFound = False
                                break
                        if fileNotFound:
                            messagebox.showwarning("", "C-Sheet not Found.")
                               
                def copy_csheet():
                    selected = select_treeview()
                    if(selected):
                        FileManager.copyFile((selected + " - Copy"), selected)
                        refresh_csheet_info()
                        
                def delete_csheet():
                   selected = select_treeview()
                   if(selected):
                        if("yes" == messagebox.askquestion(title="Delete Confirmation", message = "Are you sure you want to Delete this C-sheet")):        
                            FileManager.deleteFile(selected)
                            refresh_csheet_info()
                            messagebox.showwarning("C-Sheet Deleted", "C-Sheet Deleted")

                def destroyScreen():
                    for widget in window.winfo_children():
                        widget.destroy()
                     
                def log_csheet():
                    selected = select_treeview()
                    if(selected):
                        destroyScreen()
                        fsObj.setFlag("logCSheetUI")
                        fsObj.setData(",".join([selected, "selectCSheetUI"]))
                        
                    
                def edit_csheet():
                    selected = select_treeview()
                    if(selected):
                        destroyScreen()
                        fsObj.setFlag("createCSheetUI")
                        fsObj.setData(selected)
                        
                        
                def back():
                    destroyScreen()
                    fsObj.setFlag("homepageUI")
                    fsObj.setData("")
                    

                #Instantiating Widgets
                backB = Button(frame, text = "Back", command = back, width = 8, height = 2)
                search_bar = Entry(frame, width = 30, bd = 2, relief = "groove")
                search_btn = Button(frame, text = "Search", command = search_csheet)
                delete_btn =  Button(frame, text = "Delete", command = delete_csheet)
                copy_btn =  Button(frame, text = "Copy", command = copy_csheet)
                log_btn = Button(frame, text = "Log", command = log_csheet)
                edit_btn = Button(frame, text = 'Edit', command = edit_csheet)
                
                #Packing Widgets
                backB.pack(side = TOP, pady = 5, anchor = "w")
                search_bar.pack(side = TOP, pady = 5, anchor = "w")
                search_btn.pack(side = TOP, pady = 5, anchor = "w")
                delete_btn.pack(side = RIGHT , padx = 5)
                copy_btn.pack(side = RIGHT, padx = 5)
                log_btn.pack(side = RIGHT, padx = 5)
                edit_btn.pack(side = RIGHT, padx = 5)
                treeview.pack(side = LEFT)
                
                # Configuring treeview
                refresh_csheet_info()
                frame.pack(fill = BOTH, expand = True)
        frameMaker()
        return ["selectCSheetUI", frameMaker]

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
    SelectCSheetUI.testFrame()

