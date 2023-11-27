import os
import requests
from requests.exceptions import RequestException, ConnectionError

def getAccountId():
       
    url = "http://localhost:50001/accounts"

    headers = {
        'Authorization': 'Bearer ' + os.getenv("KEP_ACCESS_TOKEN"),
        'Connection': 'keep-alive',
        'AuthTokenType': '1',
        'AuthToken': '2'
    }
    try:
        response = requests.get(url, headers=headers)

        response_data = response.json()
        selected_user_id = response_data['data']['Accounts'][0]['Id']
        
        if os.getenv('SELECTED_USER_ID') == None:
            with open('.env', 'a') as f:
                f.write(f'\nSELECTED_USER_ID={str(selected_user_id)}\n')
            os.environ['SELECTED_USER_ID'] = str(selected_user_id)
            return os.getenv('SELECTED_USER_ID') 
        else:
            return os.getenv('SELECTED_USER_ID')     
        
    except RequestException as e:
        if type(e) is ConnectionError:
            print("Bağlantı hatası oluştu.")
            return None
        else:
            print(f"Diğer bir hata oluştu: {e}")
            return None
