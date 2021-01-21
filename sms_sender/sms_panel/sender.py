from django.http import JsonResponse
from Base.credentials import API_KEY
import requests
class Sender(object):
    @staticmethod
    def sender(receptor , message):
        url = f'https://api.kavenegar.com/v1/{API_KEY}/sms/send.json'
        data = {
            "message" : message , 
            "receptor" : receptor,
        }
        req = requests.post(url , data)
        print(req.status_code)
        if req.status_code != 200:
            return 'something is wrong!'
        else :
            return 'everythings right!'
        
    