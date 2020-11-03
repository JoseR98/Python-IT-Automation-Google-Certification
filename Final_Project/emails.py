#!/usr/bin/python3
"""Email processes module"""
import emails
import os
import email.message
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
  """Create email message"""
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)
  return message


def send_email(message):
  """send email message to a the specified recipient inside the message"""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()

if __name__ == '__main__':
  sender = 'automation@example.com'
  receiver = 'student-00-f0bb1da84e62@example.com'
  subject = 'Upload Completed - Online Fruit Store'
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = '/tmp/processed.pdf'
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)