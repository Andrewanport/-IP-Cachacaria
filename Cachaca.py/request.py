import requests

def request_conselhos(qtd):
    """Obtém uma quantidade específica de conselhos da Advice Slip API."""

    if not isinstance(qtd, int) or qtd <= 0:
        raise ValueError("A quantidade de conselhos deve ser um número inteiro positivo.")

    conselhos = []

    for _ in range(qtd):

        try:
            resposta = requests.get("https://api.adviceslip.com/advice")

            if resposta.status_code == 200:
                dados = resposta.json()
                conselhos.append((dados['slip']['id'], dados['slip']['advice']))

        except Exception as e:
            print(f"Erro ao acessar a API: {e}")
    return conselhos
