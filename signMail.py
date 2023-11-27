import os
import requests
from requests.exceptions import RequestException, ConnectionError
from errorMessage import sendErrorMessage
from kokpitLogin import login

def postSignMail(id, mimeFile:str):
       
    url = "http://localhost:50001/sign"

    headers = {
        'Authorization': 'Bearer ' + os.getenv("KEP_ACCESS_TOKEN"),
        'Connection': 'keep-alive',
        'AuthTokenType': '1',
        'AuthToken': '2'
    }
    
    data = { 
        "sign_type":"CAdES",
        "cert_serial": os.getenv('CERT_SERIAL'),
        "pin": os.getenv('PIN'),
        "algo": os.getenv('ALGO'),
        "content": mimeFile
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['data']
        
    except RequestException as e:
        if type(e) is ConnectionError:
            kokpit_token = login()
            sendErrorMessage(id, 'connection_error', kokpit_token)
            print("Bağlantı hatası oluştu.")
            return None
        else:
            sendErrorMessage(id, 'sign_error', kokpit_token)
            print(f"Diğer bir hata oluştu: {e}")
            return None
 
