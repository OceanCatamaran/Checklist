from tkinter import *
import webbrowser
my_window = Tk()

my_window.title("Feedback")
my_window.configure(width=600, height=800, bg='white')
my_window.geometry("600x800+735+300")

def callback(url):
    webbrowser.open_new_tab(url)


link = Label(my_window, text="Submit Feedback",fg="blue")
link.pack()
link.bind("<button_1>", lambda e:
callback("https://docs.google.com/forms/d/e/1FAIpQLScuEvr2AQMtrCNNIPkXUklNTnHFp3yuGtwBd_9bNiR_4dECdg/viewform?usp=sf_link"))
          
label_1 = Label(my_window, text = "Thank you for using our application. We'd appreciate your feedback!")
label_1.configure(bg="white")
label_1.pack()

button_1 = Button(my_window, text="Back")
button_1.configure(bg="white")
button_1.pack()

label_2 = Label(my_window, text = " ")
label_2.configure(bg="white")
label_2.pack()

label_3 = Label(my_window, text = "Frequently Asked Questions:")
label_3.configure(bg="white")
label_3.pack()

label_7 = Label(my_window, text = " ")
label_7.configure(bg="white")
label_7.pack()

label_3 = Label(my_window, text = "Q: How do you create a C-Sheet?")
label_3.configure(bg="white")
label_3.pack()

label_4 = Label(my_window, text = "A: Go to Home Page, press Create")
label_4.configure(bg="white")
label_4.pack()

label_5 = Label(my_window, text = " ")
label_5.configure(bg="white")
label_5.pack()

label_6 = Label(my_window, text = "Q: How can you edit your current C-Sheet?")
label_6.configure(bg="white")
label_6.pack()

label_6 = Label(my_window, text = "A: From the Home Page press Select, then press edit.")
label_6.configure(bg="white")
label_6.pack()

button_1.pack()


def link():
    webbrowser.open
