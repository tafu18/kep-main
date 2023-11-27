import os
import requests
from requests.exceptions import RequestException, ConnectionError
from typing import List
from errorMessage import sendErrorMessage
from kokpitLogin import login

def postConstructMime(id, body: str, subject: str, to: List[str], cc: List[str]):
    """Constructs a MIME file using the KEP API.

    Args:
        body: The body of the email.
        subject: The subject of the email.
        to: A list of email addresses to send the email to.
        cc: A list of email addresses to CC on the email.

    Returns:
        The MIME file, as a string.
    """

    url = "http://localhost:50001/construct-mime"

    headers = {
        'Authorization': 'Bearer ' + os.getenv("KEP_ACCESS_TOKEN"),
        'Connection': 'keep-alive',
        'AuthTokenType': '1',
        'AuthToken': '2'
    }

    data = {
        "Attachments": [],
        "BodyContent": body,
        "IletiDetay": "",
        "RemAddressesCc": cc,
        "RemAddressesTo": to,
        "Subject": subject,
        "SelectedAccountId": os.getenv('SELECTED_USER_ID')
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Check for HTTP error status

        response_data = response.json()

        # Check if the `MimeFile` key exists in the response data
        if "MimeFile" in response_data['data']:
            mime_file = response_data['data']['MimeFile']
            return mime_file

    except RequestException as e:
        if type(e) is ConnectionError:
            kokpit_token = login()
            sendErrorMessage(id, 'connection_error', kokpit_token)
            print("Bağlantı hatası oluştu.")
            return None
        else:
            sendErrorMessage(id, 'error', kokpit_token)
            print(f"Diğer bir hata oluştu: {e}")
            return None
 

