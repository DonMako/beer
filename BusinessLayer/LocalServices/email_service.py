from email.headerregistry import Address
import smtplib, ssl
from utils.singleton import Singleton


class EMailService(metaclass=Singleton):

    def check_valid_email(email: str) -> bool:
        adress = Address(display_name= email)
        if adress.username is None:
            return False
        else:
            return ("@gmail.com" in email)
    
    def send_email_modification(email_user: str, info_changed: str):
        smtp_server = "smtp.gmail.com"
        port = 465
        sender = "projectbiere@gmail.com"
        password = "823M458dXAgNNsr"
        addressee = email_user
        message = "Subject: Your BIERE account changed. \n\n Warning, your" + info_changed + """ just has been changed.
                   \nIf you're not at the origin of this modification, please warn us."""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, addressee, message)

    def send_email_deletion(email_user: str):
        smtp_server = "smtp.gmail.com"
        port = 465
        sender = "projectbiere@gmail.com"
        password = "823M458dXAgNNsr"
        addressee = email_user
        message = """Subject: Your BIERE account has been deleted. \n\n We're sorry to hear that you are leaving the BIERE project.
                     \nIf you're not at the origin of the deletion, please warn us."""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, addressee, message)