import requests

try:
    response = requests.get("https://www.pudim.com.br")
    print("Conexão bem-sucedida!")
except requests.RequestException as e:
    print(f"Erro ao tentar conectar: {e}")