import os 
import json
import requests
from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES 

def listarIdiomas():
    lista = ["Idiomas suportados: (código | nome)"]
    for nome, codigo in GOOGLE_LANGUAGES_TO_CODES.items():
        lista.append(f"{codigo} : {nome.title()}")

    return "\n".join(lista)

def processarMensagem(texto):
        comando = texto.lower().strip()

        match comando:
             case 'sair':
                  return "saindo..."
             case 'idiomas':
                  return listarIdiomas()
             case texto if texto.startswith('traduzir'):
                  partes = texto.split()
                  if len(partes) < 3:
                       return 'Formato incorreto.'
                  idioma = partes[1]
                  textoinput = " ".join(partes[2:])
                  try:
                       traducao = GoogleTranslator(source='auto', target=idioma).translate(textoinput)
                       return f"{idioma}: {traducao}"
                  except Exception as e:
                       return f"Erro: {e}"
                  
             case _:
                  return "Envie uma mensagem no formato: \n"
                  "'traduzir [codigo do idioma] [frase] (ignorar os [])"

app = Flask(__name__)

TOKENVERIFICACAO = ""
TOKENACESSOWPP = ""
IDNUMEROTELEFONE = ""


def requisicaoMensagem (textooutput, numero):
     url = f"https://graph.facebook.com/v20.0/{IDNUMEROTELEFONE}/messages"
     headers = {"Authorization": f"Bearer {TOKENACESSOWPP}", "Content-Type": "application/json"}
     data = {"messaging_product": "whatsapp", "to": numero, "text": {"body": textooutput}}
     try: 
          response = requests.post(url, headers=headers, data=json.dumps(data))
          response.raise_for_status()
          print(f"Resposta enviada para {numero}: {response.status_code}")
     except requests.exceptions.RequestException as e:
          print(f"Erro: {e}")

def requisicaoMensagem(textooutput, numero):
    url = f"https://graph.facebook.com/v20.0/{IDNUMEROTELEFONE}/messages"
    headers = {"Authorization": f"Bearer {TOKENACESSOWPP}", "Content-Type": "application/json"}
    data = {"messaging_product": "whatsapp", "to": numero, "text": {"body": textooutput}}
    
    try: 
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(f"Resposta enviada para {numero}: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        if e.response is not None:
            print(f"Resposta da API: {e.response.text}")

@app.route("/webhook", methods=["GET", "POST"])
def webhook_whatsapp():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == TOKENVERIFICACAO:
            return request.args.get("hub.challenge"), 200
        return "Erro de autenticação", 403

    if request.method == "POST":
        dados = request.get_json()
        try:
            mensageminfo = dados["entry"][0]["changes"][0]["value"]["messages"][0]
            numerousuario = mensageminfo["from"]
            textousuario = mensageminfo["text"]["body"]
            print(f"Mensagem de {numerousuario}: {textousuario}")
            
            respostabot = processarMensagem(textousuario)
            requisicaoMensagem(respostabot, numerousuario)
        except (KeyError, IndexError, TypeError) as e:
            print(f"{e}")
            pass
        return "OK", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
