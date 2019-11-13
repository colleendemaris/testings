#for kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

#for email sending
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase

# from kivy.uix.stacklayout import StackLayout

class FirstKivy(App):
    time_of_day_variable = StringProperty('')
    email_body_variable = StringProperty('')
    subject_variable = StringProperty('')

    def sendemail(self, arg):
        sender_email = "colleen.demaris@maine.edu"
        receiver_email = "cdcoldem99@gmail.com"
        port = 465
        password = "GoldenAss123#"
        context = ssl.create_default_context()

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject_variable
        message["From"] = sender_email
        message["To"] = receiver_email

        splitting = self.email_body_variable
        splitting = splitting.splitlines()
        email = ""
        for item in splitting:
            email = email + item + "<br>"

        signature = """
        Colleen DeMaris<br>
        ACM-W Secretary<br>
        Computer Science '21<br>
        University of Maine<br>
        """

        html = """
        <html>
            <body>
                <p>Good {time_of_day}, everyone!<br><br>
                    {email_body}
                    <br>{signature}<br>
                    <img src = "cid:image1" alt = "acmw-logo" style="width:203px;height:124px;">
                </p>
            </body>
        </html>
        """.format(signature=signature,time_of_day=self.time_of_day_variable,email_body=email)

        part1 = MIMEText(html, "html")
        message.attach(part1)

        fp = open('acmw_logo.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<image1>')
        message.attach(msgImage)

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, message["To"].split(","), message.as_string())

    def saveTime(self, arg):
        self.time_of_day_variable = self.txttime.text
        print("{}".format(self.time_of_day_variable))

    def save_body(self, arg):
        self.email_body_variable = self.email_body_input.text
        print("{}".format(self.email_body_variable))

    def save_sub(self, arg):
        self.subject_variable = self.txtsub.text
        print("{}".format(self.subject_variable))
    
    def build(self):
        self.box1 = BoxLayout(orientation='vertical', spacing = 20)
        self.box2 = BoxLayout(orientation='horizontal', spacing = 20)
        self.box3 = BoxLayout(orientation='horizontal', spacing = 20)
        self.box4 = BoxLayout(orientation='horizontal', spacing = 20)

        self.txtsub = TextInput(hint_text = "Subject", size_hint=(.5, .2), padding = 0)
        self.btn3 = Button(text="Submit", on_press=self.save_sub, size_hint = (.1,.2))
        self.box4.add_widget(self.txtsub)
        self.box4.add_widget(self.btn3)

        self.txttime = TextInput(hint_text = "Time of day", size_hint =(.5, .2), padding = 0)
        self.btn = Button(text="Submit", on_press=self.saveTime, size_hint = (.1, .2))
        self.box2.add_widget(self.txttime)
        self.box2.add_widget(self.btn)

        self.email_body_input = TextInput(hint_text = "Email body", size_hint=(.5, 1), padding = 0)
        self.btn2 = Button(text="Submit", on_press = self.save_body, size_hint=(.1, .2))
        self.box3.add_widget(self.email_body_input)
        self.box3.add_widget(self.btn2)

        self.sendbtn = Button(text="Send Email", on_press=self.sendemail, size_hint=(.1, .2))

        self.box1.add_widget(self.box4)
        self.box1.add_widget(self.box2)
        self.box1.add_widget(self.box3)
        self.box1.add_widget(self.sendbtn)

        return self.box1

FirstKivy().run()