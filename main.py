from accounts import getAccountId
from constructMime import postConstructMime
from signMail import postSignMail
from sendMail import postSendSignedMail
from kokpitLogin import getUnsentMail, login
from dotenv import load_dotenv

load_dotenv()

kokpit_token = login()

json_response = getUnsentMail(kokpit_token)

for info in json_response['data']:
    id = info['id']
    body_content = info['body']
    mail_subject = info['subject']
    to_recipients = [info['kep_mail']]
    cc_recipients = []

    mime_file = postConstructMime(id, body_content, mail_subject, to_recipients, cc_recipients)

    if mime_file is not None:
        signed_mime_file = postSignMail(id, mime_file)
        
    if 'signed_mime_file' in locals() and signed_mime_file is not None:
        send_mail = postSendSignedMail(id, mime_file, signed_mime_file)
        print(send_mail)  


