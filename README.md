# Email-Automation

The code is organized into two main functions: one for sending emails and one for reading emails. This combined code allows you to send emails with attachments and read incoming emails while saving their attachments.

Sending Emails:

    1. MIMEMultipart: Used to create a multipart message.

    2. MIMEText: Adds the email body as plain text.

    3. MIMEBase: Used to attach files.

    4. encoders.encode_base64: Encodes the attachment in base64.

    5. smtplib.SMTP: Creates an SMTP session for sending the email.

    6. server.starttls(): Secures the connection.

    7. server.login(): Logs into the SMTP server.

    8. server.sendmail(): Sends the email.



Reading Emails:

    1. imaplib.IMAP4_SSL: Connects to the IMAP server using SSL.

    2. mail.login(): Logs into the email account.

    3. mail.select(): Selects the mailbox (default is 'inbox').

    4. mail.search(): Searches for all emails in the inbox.

    5. mail.fetch(): Fetches the email data.

    6. email.message_from_bytes(): Parses the email content.

    7. decode_header(): Decodes the email subject and attachment filename.

    8. msg.is_multipart(): Checks if the email is multipart.

    9. msg.walk(): Iterates through the email parts.

    10. part.get_filename(): Retrieves the attachment filename.

    11. os.path.join(): Joins directory and filename to create the full file path.

    12. os.makedirs(): Creates directories if they do not exist.

    13. part.get_payload(decode=True): Decodes the attachment payload and saves it.
