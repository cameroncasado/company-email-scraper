# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# fromEmail - casadocameron777@gmail.com
# email - passing emails from csv
# subject - Hello
# message - Hi, I really love your company and am kindly asking if you could send me some freebies
Thank you,
Cameron
My address is 4853 Marrieta Street, Jurupa Valley, CA, 91752


def send_email(fromEmail, email, subject, message):
    message = Mail(
        from_email=fromEmail,
        to_emails=email,
        subject=subject,
        html_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


with open('emails.csv', 'r') as emails:
    count = 1
    for email in emails:
        print(str(count) + ': ', email)
        send_email('your-email', email, 'your-subject-line', 'your-message')
        count = count + 1
