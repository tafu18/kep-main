import requests

def login():
    url = "https://app.staging.kokpit.app/api/portal/auth/email-check"

    payload = {
        'email': 'super-admin@app.staging.kokpit.site',
        'type': 'email'
    }

    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    url = "https://app.staging.kokpit.app/api/app/auth/login"

    payload = {
        'device_name': 'samsung',
        'email': 'super-admin@app.staging.kokpit.site',
        'password': 'password',
        'type': 'email'
    }

    headers = {
    'X-Tenant': 'mgs',
    'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()

    return data['data']['token']


def getUnsentMail(token:str):


    url = "https://app.staging.kokpit.app/api/app/not-started-patrol-tickets" 
    #url = "https://app.staging.kokpit.app/api/app/keps/get-unsent-mails" #tüm kep mail taslaklarını çek

    headers = {
    'X-Tenant': 'mgs',
    'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()


    
