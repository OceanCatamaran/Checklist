from tkinter import *
import webbrowser
from frameSignaler import FrameSignaler

class GiveFeedbackUI:
   @classmethod
   def addFrame(self, window, fsObj):
      #This method adds the screen to the window from UIManager.
      def frameMaker(display = False):
         if display:
            feedback = Frame(window, relief = "groove", borderwidth = 2, bg = "white")
##            feedback.title("Get Help")
##            feedback.configure(width=600, height=800, bg='white')
##            feedback.geometry("600x800+735+300")

            def destroyScreen():
               for widget in window.winfo_children():
                        widget.destroy()

            def back():
               destroyScreen()
               fsObj.setFlag("homepageUI")
               fsObj.setData("")

            backB = Button(feedback, text = "Back", command = back, width = 8, height = 2)
            backB.place(x = 0, y = 0)

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

            label_6 = Label(feedback, text = "A: From the Home Page press Select, then press edit.")
            label_6.configure(bg="white",fg="black")
            label_6.pack()
            feedback.pack(fill = BOTH, expand = True)
      frameMaker()
      return ["feedbackUI", frameMaker]
   
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
    GiveFeedbackUI.testFrame()

