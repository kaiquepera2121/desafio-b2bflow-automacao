from supabase import create_client
import os

def get_contacts():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase = create_client(url, key)

    response = supabase.table("clientes").select("numero, nome").limit(3).execute()

    if not response.data:
        print("Erro ou nenhum dado retornado:", response)
        return []

    return response.data