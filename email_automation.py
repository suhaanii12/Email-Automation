import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import imaplib
import email
from email.header import decode_header
import os

# Function to send an email with an attachment
def send_email(smtp_server, port, sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach the file
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(part)
    
    # Login to the server and send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully!')


# Function to read emails and save attachments
def read_emails(imap_server, email_user, email_pass, mailbox="inbox"):
    # Connect to the server and go to its inbox
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_user, email_pass)
    mail.select(mailbox)
    
    # Search for all emails in the inbox
    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()
    
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Decode email sender and subject
                from_ = msg.get('From')
                subject, encoding = decode_header(msg.get('Subject'))[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
                
                print(f'From: {from_}')
                print(f'Subject: {subject}')
                
                # If the email message is multipart
                if msg.is_multipart():
                    for part in msg.walk():
                        content_disposition = part.get("Content-Disposition", "")
                        
                        if "attachment" in content_disposition:
                            filename = part.get_filename()
                            if filename:
                                if decode_header(filename)[0][1]:
                                    filename = decode_header(filename)[0][0].decode(decode_header(filename)[0][1])
                                
                                # Download attachment and save it
                                filepath = os.path.join("downloads", filename)
                                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                                print(f'Attachment {filename} saved successfully.')
    
    mail.logout()


# Example usage
smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
receiver_email = 'receiver_email@gmail.com'
subject = 'Test Subject'
body = 'This is a test email with attachment.'
attachment_path = 'path/to/your/attachment.txt'

send_email(smtp_server, port, sender_email, sender_password, receiver_email, subject, body, attachment_path)

imap_server = 'imap.gmail.com'
email_user = 'your_email@gmail.com'
email_pass = 'your_password'
mailbox = 'inbox'

read_emails(imap_server, email_user, email_pass, mailbox)
