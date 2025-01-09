import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
load_dotenv()

Chave_api_do_Sendgrid = os.getenv("sendgrid_api_key_segura")

def enviar_email(destinatario, assunto, conteudo):
    message = Mail(
        from_email = "your@gmail.com",
        to_emails = destinatario ,
        subject = assunto,
        html_content = conteudo)

    try:
        sg = SendGridAPIClient(Chave_api_do_Sendgrid)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

enviar_email("your@gmail.com", "Segue o e-mail", "Veja o E-mail, e observe seu conteúdo simples")

#This code is working correctly, for security purposes, it is without the activation email.