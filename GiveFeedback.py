from tkinter import *
import webbrowser


feedback = Tk()
feedback.title("Get Help")
feedback.configure(width=600, height=800, bg='white')
feedback.geometry("600x800+735+300")

space_1 = Label(feedback, text = " ",bg="white")
space_1.pack()

label_1 = Label(feedback, text = "Thank you for using our application. We'd appreciate your feedback!")
label_1.configure(bg="white", fg="Black")
label_1.pack()

def callback(url):
   webbrowser.open_new_tab(url)

link = Label(feedback, text="Submit Feedback", fg="blue", bg="white")
link.pack()
link.bind("<Button-1>", lambda e:
callback("https://docs.google.com/forms/d/e/1FAIpQLScuEvr2AQMtrCNNIPkXUklNTnHFp3yuGtwBd_9bNiR_4dECdg/viewform?usp=sf_link"))

space = Label(feedback, text = " ",bg="white")
space.pack()

label_3 = Label(feedback, text = "Frequently Asked Questions:")
label_3.configure(bg="white",fg="black")
label_3.pack()

label_7 = Label(feedback, text = " ",bg="white")
label_7.pack()

q_3 = Label(feedback, text="Q: What is a C-Sheet?",bg="white",fg="black")
q_3.pack()

qa_3 = Label(feedback, text="A:C-Sheet is a checklist that can be tracked overtime.",bg="white",fg="black") 
qa_3.pack()

space_1 = Label(feedback, text = " ",bg="white")
space_1.pack()

label_3 = Label(feedback, text = "Q: How do you create a C-Sheet?")
label_3.configure(bg="white",fg="black")
label_3.pack()

label_4 = Label(feedback, text = "A: Go to Home Page, press Create")
label_4.configure(bg="white",fg="black")
label_4.pack()

label_5 = Label(feedback, text = " ",bg="white")
label_5.pack()

label_6 = Label(feedback, text = "Q: How can you edit your current C-Sheet?")
label_6.configure(bg="white",fg="black")
label_6.pack()

label_6 = Label(feedback, text = "Q: How can you edit your current C-Sheet?")
label_6.configure(bg="white",fg="black")
label_6.pack()


feedback.mainloop()
