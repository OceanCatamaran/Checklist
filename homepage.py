from tkinter import *

# initialize home page window
home_page = Tk(className="Home")
home_page.geometry("600x600")

# create frame for options
option_frame = Frame(home_page)

# create options buttons for frame
create_page = Button(option_frame, text="Create", width="50")
select_page = Button(option_frame, text="Select", width="50")

create_page.pack(pady=20)
select_page.pack()

option_frame.place(anchor="s")
option_frame.pack(padx=5, pady=20)

#Grid.rowconfigure(option_frame, 0, weight=1)
#Grid.columnconfigure(option_frame, 0, weight=1)


#create_page.grid(row=0, column=0, sticky="NSEW")
#select_page.grid(row=1, column=0, sticky="NSEW")

create_page.grid

option_frame.place(in_=home_page, anchor="c", relx=0.5, rely=0.5)

# loop window
home_page.mainloop()
