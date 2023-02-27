import smtplib, ssl
from utils.singleton import Singleton


class EMailService(metaclass=Singleton):
    def send_email(email_user: str, info_changed: str):
        smtp_server = "smtp.gmail.com"
        port = 465
        sender = "projectbiere@gmail.com"
        password = "823M458dXAgNNsr"
        addressee = email_user
        message = "Warning, your " + info_changed + " just has been changed.\nIf you're not at the origin of this modification, please warn us."
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, addressee, message) 