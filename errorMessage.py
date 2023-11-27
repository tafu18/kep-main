import requests

def sendErrorMessage(id, message:str, token):
    url = "https://app.staging.kokpit.app/api/app/areas/{}".format(id)
    #url = "https://app.staging.kokpit.app/api/app/keps/{}".format(id)

    payload = {
        'region_id': message,
    }

    headers = {
    'X-Tenant': 'mgs',
    'Authorization': 'Bearer ' + token
    }

    response = requests.request("PUT", url, headers=headers, json=payload)
    return response