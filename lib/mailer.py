import smtplib

from lib.creds import EMAIL, PASSWORD

class Mailer:
    def __init__(self):
        self.EMAIL = EMAIL
        self.PASS = PASSWORD
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, email):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)

        # email to be sent
        SUBJECT = 'ALERT!'
        TEXT = f'People limit exceeded in your building.'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # sending the email
        self.server.sendmail(self.EMAIL, email, message)
        self.server.quit()

