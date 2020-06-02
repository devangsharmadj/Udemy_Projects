import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'First Last'
email['subject'] = 'Test'

email.set_content('Testing...')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.send_message(email)
    print('All done')
