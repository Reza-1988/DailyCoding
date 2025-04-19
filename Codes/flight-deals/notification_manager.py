import ssl

from twilio.rest import Client
import smtplib


from Codes.local_settings import TWILIO_DATA, SMTP_DATA


class NotificationManager:
    def __init__(self):
        self.account_sid = TWILIO_DATA["ACCOUNT_SID"]
        self.auth_token = TWILIO_DATA["AUTH_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)
        self.email = SMTP_DATA["EMAIL"]
        self.password = SMTP_DATA["PASSWORD"]
        self.smtp_server = SMTP_DATA["SMTP_SERVER"]
        self.connection = smtplib.SMTP(self.smtp_server, 587)

    def send_sms(self, body_message):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            body=body_message,
            from_=TWILIO_DATA["TWILIO_PHONE_NUMBER"],
            to=TWILIO_DATA["TO_PHONE_NUMBER"],
        )
        print(message.status)

    def send_email(self, email_list, email_body):
        # SET EMAIL AND PASSWORD
        # first turn on two-step verification from https://myaccount.google.com/
        # this password is coming -> https://myaccount.google.com/ -> Security -> App Password ->
        # Select give your app a name e.g., Python Mail and click create. COPY THE PASSWORD -
        # This is the only time you will ever see the password. It is 16 characters with no spaces.
        # Use this App password in your Python code instead of your normal password.

        # SMTP is stood for simple mail transfer control, it contains rules that how email can be sent around the internet.
        with self.connection:  # make a new smtp object
            # TLS stand for transport layer security & it's way to securing our connection to our email server with encrypt messages.
            self.connection.starttls()
            self.connection.login(user=self.email, password=self.password)
            for email in email_list:
                self.connection.sendmail(
                from_addr=self.email,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
            )
            print("Email sent")
