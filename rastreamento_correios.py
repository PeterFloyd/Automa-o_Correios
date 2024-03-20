import requests
from requests.structures import CaseInsensitiveDict
import json


def main():
    #codigo_objeto = "DG049186230BR"
    codigo_objeto = "LB571181225HK"
    captcha = "fhkge"
    url = f"https://rastreamento.correios.com.br/app/resultado.php?objeto={codigo_objeto}&captcha={captcha}&mqs=S"

    headers = requests.structures.CaseInsensitiveDict()
    headers["Accept"] = "*/*"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Sucesso na requisição: {response.status_code}")
    else:
        print(f"Erro na requisição: {response.status_code}")

    data = json.loads(response.text)

    if data["mensagem"] == "Captcha inválido":
        print(f"Erro no captcha: {data}")


if __name__ == "__main__":
    main()

