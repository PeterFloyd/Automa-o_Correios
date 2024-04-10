import requests
from requests.structures import CaseInsensitiveDicts
import json
import os


#Executa a função principal
def main():
    try:
        url_dados_pagina = "https://rastreamento.correios.com.br/app/index.php"
        session = sessao_pagina(url_dados_pagina)
        baixar_imagem_captcha(session)

        #Requisição objeto
        codigo_objeto = "DG049186230BR"
        captcha = str(input("Informe o captcha: "))
        url = f"https://rastreamento.correios.com.br/app/resultado.php?objeto={codigo_objeto}&captcha={captcha}&mqs=S"

        headers = requests.structures.CaseInsensitiveDict()
        headers["Accept"] = "*/*"

        response = session.get(url, headers=headers)

        if response.status_code == 200:
            print(f"Sucesso na requisição: {response.status_code}")
        else:
            print(f"Erro na requisição: {response.status_code}")

        data = json.loads(response.text)

        if data["mensagem"] == "Captcha inválido":
            print(f"Erro no captcha: {data["mensagem"]}")
        else:
            print(f"Sucesso no captcha: {data["mensagem"]}")

    except:
        print(f"Erro no rastreamento do objeto {codigo_objeto}")


#Retorna a sessão da página
def sessao_pagina(url_dados_pagina):
    try:
        session = requests.session()
        session.get(url_dados_pagina)
        return session
    
    except:
        print("Erro ao criar sessão.")


#Efetua o download da imagem captcha
def baixar_imagem_captcha(session):
    try:
        #Captcha antigo
        if os.path.exists("imagem_captcha.php"):
            print("Deletando imagem captcha antiga.")
            os.remove("imagem_captcha.php")
        else:
            print("Não existe imagem captcha antiga.")

        #Captcha novo
        f = open("imagem_captcha.php", "wb")
        response_img = session.get("https://rastreamento.correios.com.br/core/securimage/securimage_show.php")
        f.write(response_img.content)
        f.close()
        print("Download sucessful!")

    except:
        print("Error")


if __name__ == "__main__":
    main()