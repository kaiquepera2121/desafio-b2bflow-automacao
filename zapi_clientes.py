import requests
import os

def send_message(numero, mensagem):
    instance = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    client_token = os.getenv("ZAPI_CLIENT_TOKEN") 

    url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"

    headers = {
        "Content-Type": "application/json",
        "Client-Token": client_token
    }

    payload = {
        "phone": numero, 
        "message": mensagem
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print(f"Mensagem para {numero} enviada com sucesso!")
    else:
        print(f"Erro ao enviar mensagem para {numero}. Status: {response.status_code}. Resposta: {response.text}")