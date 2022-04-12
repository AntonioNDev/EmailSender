from dotenv import load_dotenv
from email.message import EmailMessage
from pathlib import Path
from tkinter import messagebox as mb
import os
import smtplib
import imghdr

#Load_dotenv will load our env file
load_dotenv()
EMAIL_ADDR = os.environ.get('EMAIL')
EMAIL_PW = os.environ.get('APP_PW')




class emailApp:
   def __init__(self, subject, body, receiver, attach):
      self.subject = subject
      self.body = body
      self.receiver = receiver
      self.attach = attach

      self.msg = EmailMessage()
      self.msg['Subject'] = subject
      self.msg['From'] = EMAIL_ADDR
      self.msg['To'] = receiver
      self.msg.set_content(body)

      #Check if there's an attachment
      if len(attach) != 0:
         for file in attach:
            with open(file, 'rb') as f:
               file_data = f.read()
               file_type = Path(file).suffix
               file_name = Path(file).name
            self.msg.add_attachment(file_data, maintype='file', subtype=file_type, filename=file_name)

      else:
         pass

      self.sendEmail()

   def sendEmail(self):
      #Make a SSL connection
      try: 
         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDR, EMAIL_PW)

            smtp.send_message(self.msg)
            mb.showinfo('Info', 'The email was successfully sent!.')
      except:
         mb.showerror('Error', 'Something went wrong, please try again!.')

