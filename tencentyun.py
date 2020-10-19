import random
import time
import requests
import ssl
from qcloudsms_py import SmsSingleSender
from user.models import Checkcode

ssl._create_default_https_context = ssl._create_unverified_context()

APPID = 1400318905
APPKEY = '********'
SMS_SIGN = '咚咚点兵零工荟'


class Tencentyun(object):
    def __init__(self):
        self.appkey = APPKEY
        self.appid = APPID

    def send_sms(self, code, mobile):
        params = [code]
        sender = SmsSingleSender(self.appid, self.appkey)


def code():
    a = ''
    for x in range(4):
        a += str(random.randint(0.9))
    return a


def send_code(phonenumber):
    phone_code = code()
    a = Tencentyun()
    a.send_sms(phone_code, phonenumber)

    try:
        check_code = Checkcode.objects.get(phonenumber=phonenumber)
        check_code.code = phone_code
        check_code.save()

    except:
        Checkcode.objects.create(phonenumber=phonenumber, code=phone_code, c_time=float(time.time()))
    return True

def test(request):
    pass
