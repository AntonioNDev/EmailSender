from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from main import emailApp
import re

window = Tk()
window.title('Email sender')


class AppGUI:
   def __init__(self):
      global txtArea, subjectInp, emailEntry, numOfAddedAttach, addedAttachments, bottomFrame
      #App width and height 
      width = 680
      height = 350
 
      #Getting the width and the height of the screen so we can
      #place the app window in the center
      screen_w = window.winfo_screenwidth()
      screen_h = window.winfo_screenheight()

      x = (screen_w / 2) - (width) + 300
      y = (screen_h / 2) - (height) + 100
      
      window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
      
      #This list will save the path of added attachments so later we can send them all together
      addedAttachments = []

      #Top frame where all the buttons and settings will be
      TopFrame = Frame(window, relief='sunken', border=3, height=150, highlightthickness=3, bg="#adc178")
      TopFrame.pack(anchor=CENTER, fill=X)

      TopFrame.config(highlightbackground='#718355', highlightcolor='#718355')
      
      leftSide = Frame(TopFrame, border=1, height=150, bg="#adc178")
      leftSide.grid(row=0, column=0, ipady=10, ipadx=40)

      rightSide = Frame(TopFrame, border=1, height=150, bg="#adc178")
      rightSide.grid(row=0, column=1, ipady=10, ipadx=85)

      #In top entry we'll write the address that we want to send an email
      topLabel = Label(leftSide, text='Send email to: ', bg="#adc178", font=('Lucida Bright', 18))
      topLabel.pack(anchor=NW, padx=10, pady=15)

      emailEntry = Entry(leftSide, font=('DaunPenh', 13), relief='sunken', highlightthickness=3, bg="#97a97c", border=2)
      #emailEntry.insert(0, '@gmail.com')
      emailEntry.pack(anchor=NW, ipadx=15, ipady=5, padx=10, pady=3)
      emailEntry.config(highlightbackground='#718355', highlightcolor='#718355')

      #Add attacment button
      addAttch = Button(rightSide, text='Add attachment', bg="#adc178", font=('Rockwell', 10), highlightthickness=3, border=3, relief='ridge', command=self.addAttach)
      addAttch.config(highlightbackground='#adc178', highlightcolor='#adc178')
      addAttch.pack(anchor=E, ipadx=25, ipady=4, padx=4, pady=15)

      #Send button
      sendButton = Button(rightSide, text='Send email', bg="#adc178", font=('Rockwell', 10), highlightthickness=3, border=3, relief='ridge', command=lambda: self.sendEmail(txtArea.get('1.0', 'end-1c'), subjectInp.get(), emailEntry.get()))
      sendButton.config(highlightbackground='#adc178', highlightcolor='#adc178')
      sendButton.pack(anchor=E, ipadx=40, ipady=4, padx=4)

      #Bottom frame
      bottomFrame = Frame(window, bg="#adc178")
      bottomFrame.pack(side=BOTTOM, fill=BOTH, ipady=100)

      #text area
      txtArea = Text(bottomFrame, height=50, width=55, bg='#cfe1b9', relief='sunken', border=4, font=('Arial', 13))
      txtArea.config(highlightbackground='#718355', highlightcolor='#718355')
      txtArea.pack(side=LEFT)

      #Subject input and label
      subjectLabel = Label(bottomFrame, text='Subject: ', font=('Lucida Bright', 15), bg="#adc178")
      subjectLabel.pack(anchor=CENTER, padx=10, pady=5)

      subjectInp = Entry(bottomFrame,  highlightthickness=3, bg='#cfe1b9', border=2, font=('Arial', 12))
      subjectInp.pack(ipadx=10, ipady=5, padx=10, pady=3)
      subjectInp.config(highlightbackground='#718355', highlightcolor='#718355')

      numOfAddedAttach = Label(bottomFrame, text=f'Added attachments: {len(addedAttachments)}', bg="#adc178", font=('Arial', 10))
      numOfAddedAttach.pack(anchor=CENTER, pady=8, padx=5)

      clearAddedAttchButton = Button(bottomFrame, text='Delete attachments', bg="#adc178", font=('Rockwell', 10), relief='ridge', highlightthickness=3, border=3 , command=self.clearAttach)
      clearAddedAttchButton.pack(anchor=CENTER, pady=8, padx=5, ipadx=10, ipady=10)
      
   def clearAttach(self):
      addedAttachments.clear()
      numOfAddedAttach.config(text=f'Added attachments: {len(addedAttachments)}')


   def addAttach(self):

      selectFilesWindow = filedialog.askopenfilenames(initialdir="C:/", title="Select files", filetypes=(("All files", "*.*"), ("Images", ("*.jpg", "*.png", "*.svg", "*.jpeg")), ("Documents", ("*.doc", "*.html", "*.pdf", "*.txt", "*.hls"))))
      
      #By default selectFilesWindow will return a set of paths from files that we selected
      #So we'll loop through the set and append them in the main addedAttachment list

      if len(selectFilesWindow) != 0:
         for x in range(0, len(selectFilesWindow)):
            addedAttachments.append(selectFilesWindow[x])
            
         numOfAddedAttach.config(text=f'Added attachments: {len(addedAttachments)}')
         

   def sendEmail(self, body, subject, receiver):
      if len(subject) != 0 or len(receiver) != 0:
         #RegEx pattern to check if the email is valid or not.
         if re.search("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{3,3}$", receiver) != None:
            emailApp(subject, body, receiver, addedAttachments)

            
            subjectInp.delete(0, END)
            emailEntry.delete(0, END)
            numOfAddedAttach.config(text='')
            addedAttachments.clear()
            txtArea.delete('1.0', 'end-1c')
         else:
            mb.showerror('Error', 'Invalid email address')
      else:
         mb.showwarning('Warning', 'Empty email address!')
         

AppGUI()

window.bind('<Button>', lambda event: event.widget.focus_set())
window.resizable(False, False)
window.mainloop()
