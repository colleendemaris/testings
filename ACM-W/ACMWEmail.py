import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase

def sendemail(time_of_day, email_body):
    sender_email = "colleen.demaris@maine.edu"
    receiver_email = "cdcoldem99@gmail.com"
    port = 465
    password = "GoldenAss123#"
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "ACM-W Test"
    message["From"] = sender_email
    message["To"] = receiver_email

    time_of_day = "morning"

    signature = """
    Colleen DeMaris<br>
    ACM-W Secretary<br>
    Computer Science '21<br>
    University of Maine<br>
    """

    html = """\
    <html>
        <body>
            <p>Good {time_of_day}!<br>
                Body here: <br>
                
                <br><br>{signature}<br>
                <img src = "cid:image1" alt = "acmw-logo" style="width:203px;height:124px;">
            </p>
        </body>
    </html>
    """.format(signature=signature,time_of_day=time_of_day)

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


sendemail()