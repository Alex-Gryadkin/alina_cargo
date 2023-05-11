from SMS.smsc_api import *
import random
from . models import OTPStorage
import datetime



def send_otp(username):
    try:
        otp_session = OTPStorage.objects.get(phone=username)
    except OTPStorage.DoesNotExist:
        otp_session = None

    if otp_session:

        otp_session_created = otp_session.date_added
        now = datetime.datetime.now(otp_session_created.tzinfo)
        time_delta = datetime.datetime.timestamp(now) - datetime.datetime.timestamp(otp_session_created)

        if time_delta < 60:
            return 'LATER'
        out_otp = random.randint(100000, 999999)
        otp_session.date_added = now
        otp_session.otp = out_otp

    else:
        out_otp = random.randint(100000, 999999)
        otp_session = OTPStorage(phone=username, otp=out_otp)

    otp_session.save()
    sms = SMSC()
    sms.send_sms(f'7{username}', f'WINWIN Cargo | Проверочный код: {out_otp}')
    return 'SUCCESS'
