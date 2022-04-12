from dotenv import load_dotenv
from email.message import EmailMessage
import os
import smtplib
import imghdr

#Load_dotenv will load our env file
load_dotenv()
EMAIL_ADDR = os.environ.get('EMAIL')
EMAIL_PW = os.environ.get('APP_PW')




class emailApp:
   def __init__(self, subject, body, receiver):
      self.subject = subject
      self.body = body
      self.receiver = receiver

      self.msg = EmailMessage()
      self.msg['Subject'] = subject
      self.msg['From'] = EMAIL_ADDR
      self.msg['To'] = receiver
      self.msg.set_content(body)
      #self.msg.add_attachment(file_data, maintype='text', subtype='txt', filename=file_name)

      self.sendEmail()

   def sendEmail(self):
      #Make a SSL connection
      try: 
         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDR, EMAIL_PW)

            #smtp.send_message(self.msg)
            print('Message sucessfully sended.')
      except:
         print('Something went wrong!')

