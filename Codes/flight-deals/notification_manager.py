from twilio.rest import Client


from Codes.local_settings import TWILIO_DATA


class NotificationManager:
    def __init__(self):
        self.account_sid = TWILIO_DATA["ACCOUNT_SID"]
        self.auth_token = TWILIO_DATA["AUTH_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)

    def send(self, massage):
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
            body=massage,
            from_=TWILIO_DATA["TWILIO_PHONE_NUMBER"],
            to=TWILIO_DATA["TO_PHONE_NUMBER"],
        )

        print(message.status)
