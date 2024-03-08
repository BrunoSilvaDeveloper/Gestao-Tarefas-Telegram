import requests
import json


class TelegramBot:
  def __init__(self):
    token = '7131800872:AAFj4urFyGBQ9Hv4dbRIFA6dh4Twcg75inA'
    self.url_base = f'https://api.telegram.org/bot{token}/'

  #iniciar o bot
  def Iniciar(self, update_id):
    while True: 
        atualizacao = self.obter_mensagens(update_id)
        mensagens = atualizacao['result']
        if mensagens:
            for mensagem in mensagens:
                update_id = mensagem['update_id']
                chat_id = mensagem['message']['from']['id']
                mensagembot = mensagem['message']['text']
            return mensagembot, chat_id, update_id
          
  #obter mensagens
  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

#criar resposta

  def criar_resposta(self):
    return 'Olá, bem vindo ao nosso bot de consulta de CEP'

  def responder(self, resposta, chat_id):
    #enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)

bot = TelegramBot()
update_id = None 
while True:
  mensagem, chat_id, update_id = bot.Iniciar(update_id)
  if mensagem == 'ola':
    bot.responder(f'ola, sua mensagem foi {mensagem}', chat_id)
