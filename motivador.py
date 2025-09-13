import requests

def obter_frase():
    url = "https://api.quotable.io/random"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        return f'"{dados["content"]}" — {dados["author"]}'
    else:
        return "Seja a mudança que você quer ver no mundo. — Gandhi"
