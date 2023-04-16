from sms.smsc_api import *
import random


class MessageHandler:

    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_on_phone(self):
        sms = SMSC()
        sms.send_sms(f'7{self.phone_number}', f'Проверочный код: {self.otp}')


