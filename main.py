from dotenv import load_dotenv
from supabase_clientes import get_contacts
from zapi_clientes import send_message
import os

load_dotenv()

def main():
    contacts = get_contacts()
    
    if not contacts:
        print("Nenhum contato encontrado para enviar mensagens.")
        return

    for contact in contacts:
        nome = contact['nome']
        numero = contact['numero']
        mensagem = f"Olá {nome}, tudo bem com você?"
        send_message(numero, mensagem)

if __name__ == "__main__":
    main()