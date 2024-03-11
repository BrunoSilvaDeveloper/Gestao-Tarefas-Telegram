
import re
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

  def responder(self, resposta, chat_id):
    #enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)

class Tarefa:
    #criando o objeto tarefa com atributos privados
    def __init__(self, titulo, descricao, dataCriacao, status):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__dataCriacao = dataCriacao
        self.__status = status

    #retornando o titulo da tarefa
    def get_titulo(self):
        return self.__titulo
    
    #retornando a descricao da tarefa
    def get_descricao(self):
        return self.__descricao
    
    #retornando a data da tarefa
    def get_data_criacao(self):
        return self.__dataCriacao
    
    #retornando o status da tarefa
    def get_status(self):
        return self.__status

    #atualizando o titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo

    #atualizando a descricao
    def set_descricao(self, descricao):
        self.__descricao = descricao

    #atualizando a data
    def set_data(self, data):
        self.__dataCriacao = data

    #atualizando o status
    def set_status(self, status):
        self.__status = status 

class User():
    def __init__(self, name, password, office, logado):
        self.__name = name
        self.__password = password
        self.__office = office
        self.__logado = logado

    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password
    
    def get_office(self):
        return self.__office
    
    def get_logado(self):
        return self.__logado
    
    def set_name(self,name):
        self.__name = name
    
    def set_password(self, password):
        self.__password = password
    
    def set_office(self, office):
        self.__office = office

    def set_logado(self, logado):
        self.__logado = logado

class Task():
    def __init__(self, title, description, date, priority, status):
        self.__title = title
        self.__description = description
        self.__date = date
        self.__priority = priority
        self.__status = status

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date
    
    def get_priority(self):
        return self.__priority

    def get_status(self):
        return self.__status
    
    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_date(self, date):
        self.__date = date
    
    def set_priority(self, priority):
        self.__priority = priority

    def set_status(self, status):
        self.__status = status

class Manager():
    def __init__(self):
        self.__usuarios = []
        adm = User('Adm', 'Adm123!', 'administrator', False)
        self.set_users(adm)

    def get_users(self):
        return self.__usuarios
    
    def set_users(self, user):
        self.__usuarios.append(user)

# Cadastrar Usuarios
    def register_employee(self, chat_id, update_id):
        while True:
            resposta = 'Digite o nome do funcionario:'
            self.enviar_mensagem(resposta, chat_id)
            name, chat_id, update_id = self.receber_mensagem(update_id)
            if not self.character_validation(name):
                if self.user_validation(name):
                    break
                else:
                    resposta = 'Este nome de usuário não está disponível!'
                    self.enviar_mensagem(resposta, chat_id)

            else:
                resposta = 'Digite um nome válido, SEM caracteres especiais!'
                self.enviar_mensagem(resposta, chat_id)

        while True:
            resposta = 'Digite uma senha. Ela deve possuir ao menos 6 caracteres, uma letra maiúscula e um caractere especial: '
            self.enviar_mensagem(resposta, chat_id)
            password, chat_id, update_id = self.receber_mensagem(update_id)
            if len(password) < 6:
                resposta = 'A senha deve ter ao menos 6 caracteres!'
                self.enviar_mensagem(resposta, chat_id)
            else:
                if self.character_validation(password):
                    if self.isupper_validation(password, chat_id):
                        break
                else:
                    resposta = 'Digite ao menos um carcatere especial!'
                    self.enviar_mensagem(resposta, chat_id)

        while True:
            resposta = 'Digite a senha novamente:'
            self.enviar_mensagem(resposta, chat_id)
            passwordConfirm, chat_id, update_id = self.receber_mensagem(update_id)
            if password == passwordConfirm:
                break
            else:
                resposta = 'As senhas são diferentes!'
                self.enviar_mensagem(resposta, chat_id)

        while True:
            resposta = '''Qual o cargo operacional do funcionário? 
/Administrador
/Funcionario'''
            self.enviar_mensagem(resposta, chat_id)
            choice, chat_id, update_id = self.receber_mensagem(update_id)
            if choice == '/Administrador':
                office = 'administrator'
                break
            
            elif choice == '/Funcionario':
                office = 'employee'
                break
            
            else: 
                resposta = 'Digite uma opção válida!'
                self.enviar_mensagem(resposta, chat_id)
        logado = False
        employee = User(name, password, office, logado)
        self.__usuarios.append(employee)
        resposta = 'Usuário cadastrado com sucesso!'
        self.enviar_mensagem(resposta, chat_id)

    def character_validation(self, string):
        regex = re.compile(r'[^\w\s]')
        if regex.search(string) is None:
            return False
        else:
            return True
    
    def isupper_validation(self, string, chat_id):
        for char in string:
            if char.isupper():
                return True
            else:
                resposta = 'Digite ao menos uma letra maiúsula!'
                self.enviar_mensagem(resposta, chat_id)
                return False

    def user_validation(self, name):
        for user in self.__usuarios:
            if user.get_name() == name:
                return False
        return True
# Cadastrar tarefas
            
#self.responder(resposta, chat_id)
    
# Exibir menu
    
    def receber_mensagem(self, update_id):
        bot = TelegramBot()
        mensagem, chat_id, update_id = bot.Iniciar(update_id)
        return mensagem, chat_id, update_id

    def enviar_mensagem(self, resposta, chat_id):
        bot = TelegramBot()
        bot.responder(resposta, chat_id)
          
    def exibir_menu(self, chat_id, update_id):
        while True:
            resposta = 'Menu Lista de Tarefas \nO que você deseja fazer? \n/Login \n/Sair'
            self.enviar_mensagem(resposta, chat_id)
            choice, chat_id, update_id = self.receber_mensagem(update_id)
            if choice == '/Login':
                resposta = '''Tela de Login
Digite seu nome de usuário: 
                ''' 
                self.enviar_mensagem(resposta, chat_id)
                name, chat_id, update_id = self.receber_mensagem(update_id)
                office, chat_id, update_id = self.login(name, chat_id, update_id)
                if office:
                    return office, chat_id, update_id
                else:
                    return 'Error', chat_id, update_id
                
            elif choice == '/Sair':
                resposta = 'Finalizando programa!'
                self.enviar_mensagem(resposta, chat_id)
                return False, chat_id, update_id
            else:
                resposta = 'Selecione uma opção válida, clique na opção escolhida!'
                self.enviar_mensagem(resposta, chat_id)

    def login(self, name, chat_id, update_id):
        for user in self.__usuarios:
            if user.get_name() == name:
                tentativas = 3
                while tentativas > 0:
                    resposta = 'Digite sua senha: '
                    self.enviar_mensagem(resposta, chat_id)
                    password, chat_id, update_id = self.receber_mensagem(update_id)

                    if user.get_password() == password:
                        user.set_logado(True)
                        resposta = 'Login realizado com sucesso!'
                        self.enviar_mensagem(resposta, chat_id)
                        office = user.get_office()
                        return office, chat_id, update_id
                    else:
                        resposta = 'Sua senha esta incorreta!'
                        self.enviar_mensagem(resposta, chat_id)
                        tentativas -= 1
                resposta = 'Tentativas esgotadas. Saindo...'
                self.enviar_mensagem(resposta, chat_id)
                return False, chat_id, update_id
        resposta = 'Usuário não encontrado!'
        self.enviar_mensagem(resposta, chat_id)
        return False, chat_id, update_id

    def exibir_menu_adm(self, chat_id, update_id):

        resposta = 'Menu de Adminstrador!'
        self.enviar_mensagem(resposta, chat_id)
        while True:
            resposta = '''O que você deseja fazer? 

/Funcionarios 
/Tarefas 
/Sair'''
            self.enviar_mensagem(resposta, chat_id)
            choice, chat_id, update_id = self.receber_mensagem(update_id)
            print(choice)
            if choice == '/Funcionarios':
                self.register_employee(chat_id, update_id)

            elif choice == '/Tarefas':
                resposta = '''O que você deseja fazer? 
1. Adicionar Tarefas 
2.Editar Tarefas 
3.Visualizar Tarefas 
4.Excluir Tarefas 
5.Tornar Tarefas Prioridade 
6.Retirar Prioridade das tarefas 
7.Sair'''
                self.enviar_mensagem(resposta, chat_id)
                choice, chat_id, update_id = self.receber_mensagem(update_id)
                #continuar aqui
                return False, chat_id, update_id

            elif choice == '/Sair':
                resposta = 'Saindo...'
                self.enviar_mensagem(resposta, chat_id)
                return False, chat_id, update_id
            else:
                resposta = 'Digite uma opção válida!'
                self.enviar_mensagem(resposta, chat_id)

    def exibir_menu_employee(self):
        resposta = 'Menu de Funcionário!'
        self.enviar_mensagem(resposta, chat_id)
        while True:
            resposta = '''O que você deseja fazer? 
/Visualizar tarefas pendentes 
/Marcar tarefas como concluídas 
/Sair'''
            self.enviar_mensagem(resposta, chat_id)
            choice, chat_id, update_id = self.receber_mensagem(update_id)
            if choice == '/Visualizar':
                pass

            elif choice == '/Marcar':
                pass

            elif choice == '/Sair':
                return False, chat_id, update_id
            else:
                resposta = 'Digite uma opção válida!'
                self.enviar_mensagem(resposta, chat_id)

# Looping de execucao
    def looping_execucao(self):
        bot = TelegramBot()
        update_id = None 
        while True:
            mensagem, chat_id, update_id = bot.Iniciar(update_id)
            office, chat_id, update_id = self.exibir_menu(chat_id, update_id)
            if office == 'administrator' or office == 'employee':
                if office == 'administrator':
                    while True:              
                        office, chat_id, update_id = self.exibir_menu_adm(chat_id, update_id) 
                        if office:
                            pass
                        else: break
                        
                elif office == 'employee':
                    while True:
                        office, chat_id, update_id = self.exibir_menu_employee(chat_id, update_id) 
                        if office:
                            pass
                        else: break
                        
                else: 
                    break
            elif office == 'Error': pass
            else: break


init = Manager()
init.looping_execucao()






