
import requests
import os
import random
import string
from requests.exceptions import RequestException, ConnectionError
from errorMessage import sendErrorMessage
from kokpitLogin import login

def generateKepToken(length = 30):
    characters = string.ascii_letters + string.digits
    kep_token = "kep_" + ''.join(random.choice(characters) for i in range(length))
    return kep_token

def postSendSignedMail(id, mimeFile:str, signedMimeFile:str):
       
    url = "http://localhost:50001/send_mail_with_signed_constructed_mime"

    headers = {
        'Authorization': 'Bearer ' + os.getenv("KEP_ACCESS_TOKEN"),
        'Connection': 'keep-alive',
        'AuthTokenType': '1',
        'AuthToken': '2'
    }
    
    data = { 
        "ConstructedMimeMessage": mimeFile,
        "Signature": signedMimeFile,
        "IntegratorMailId": generateKepToken(),
        "SelectedAccountId" : os.getenv('SELECTED_USER_ID')
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        
        data = response.json()
        return data  
    
    except RequestException as e:
        if type(e) is ConnectionError:
            kokpit_token = login()
            sendErrorMessage(id, 'connection_error', kokpit_token)
            print("Bağlantı hatası oluştu.")
            return None
        else:
            sendErrorMessage(id, 'send_error', kokpit_token)
            print(f"Diğer bir hata oluştu: {e}")
            return None

        