# Email-Automation

The code is organized into two main functions: one for sending emails and one for reading emails. This combined code allows you to send emails with attachments and read incoming emails while saving their attachments.

Sending Emails:

MIMEMultipart: Used to create a multipart message.

MIMEText: Adds the email body as plain text.

MIMEBase: Used to attach files.

encoders.encode_base64: Encodes the attachment in base64.

smtplib.SMTP: Creates an SMTP session for sending the email.

server.starttls(): Secures the connection.

server.login(): Logs into the SMTP server.

server.sendmail(): Sends the email.


Reading Emails:

imaplib.IMAP4_SSL: Connects to the IMAP server using SSL.

mail.login(): Logs into the email account.

mail.select(): Selects the mailbox (default is 'inbox').

mail.search(): Searches for all emails in the inbox.

mail.fetch(): Fetches the email data.

email.message_from_bytes(): Parses the email content.

decode_header(): Decodes the email subject and attachment filename.

msg.is_multipart(): Checks if the email is multipart.

msg.walk(): Iterates through the email parts.

part.get_filename(): Retrieves the attachment filename.

os.path.join(): Joins directory and filename to create the full file path.

os.makedirs(): Creates directories if they do not exist.

part.get_payload(decode=True): Decodes the attachment payload and saves it.
