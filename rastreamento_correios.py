import requests
from requests.structures import CaseInsensitiveDict
import json
from bs4 import BeautifulSoup


#Executa a função principal
def main():
    try:
        url_dados_pagina = "https://rastreamento.correios.com.br/app/index.php"
        session = sessao_pagina(url_dados_pagina)
        cookie = cookie_pagina(url_dados_pagina)
        baixar_imagem_captcha()

        #conferir retorno
        print(f"Sessão: {session}")
        print(f"Cookie: {cookie}")

        codigo_objeto = "DG049186230BR"
        captcha = "tykh"
        url = f"https://rastreamento.correios.com.br/app/resultado.php?objeto={codigo_objeto}&captcha={captcha}&mqs=S"

        headers = requests.structures.CaseInsensitiveDict()
        headers["Accept"] = "*/*"
        #headers["Cookie"] = cookie

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(f"Sucesso na requisição: {response.status_code}")
        else:
            print(f"Erro na requisição: {response.status_code}")

        data = json.loads(response.text)

        if data["mensagem"] == "Captcha inválido":
            print(f"Erro no captcha: {data["mensagem"]}")
    
    except:
        print(f"Erro no rastreamento do objeto {codigo_objeto}")


#Retorna a sessão da página
def sessao_pagina(url_dados_pagina):
    try:
        session = requests.session()
        session.get(url_dados_pagina)
        print(f"Sessão ativa: {session}")
        return session
    
    except:
        print("Erro ao criar sessão.")


#Retorna o cookie da página
def cookie_pagina(url_dados_pagina):
    try:
        headers_cookie = requests.structures.CaseInsensitiveDict()
        headers_cookie["Accept"] = "*/*"
        response_cookie = requests.get(url_dados_pagina, headers=headers_cookie)
        cookie = response_cookie.cookies
        print(f"Sucesso ao recuperar cookie: {cookie}")
        return cookie
    
    except:
        print("Erro ao recuperar cookie.")


#Efetua o download da imagem captcha
def baixar_imagem_captcha():
    try:
        f = open("imagem_captcha.php", "wb")
        response_img = requests.get("https://rastreamento.correios.com.br/core/securimage/securimage_show.php")
        f.write(response_img.content)
        f.close()
        print("Download sucessful!")

    except:
        print("Error")


if __name__ == "__main__":
    main()