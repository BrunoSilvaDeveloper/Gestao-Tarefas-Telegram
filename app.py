
import re
import requests
import json
from datetime import datetime

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
    def __init__(self, titulo, descricao, dataCriacao, status, funcionario, prioridade):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__dataCriacao = dataCriacao
        self.__status = status
        self.__funcionario = funcionario
        self.__prioridade = prioridade

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
    
    #retornando o status da tarefa
    def get_funcionario(self):
        return self.__funcionario
    
    #retornando o status da tarefa
    def get_prioridade(self):
        return self.__prioridade

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

     #atualizando o status
    def set_funcionario(self, funcionario):
        self.__funcionario = funcionario

    #atualizando o status
    def set_prioridade(self, prioridade):
        self.__prioridade = prioridade


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
        self.__listaTarefas = []
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
    
# Funcoes tarefas -------------------------------------------------------------
    

    def informacoes_tarefa(self, chat_id, update_id):
        while True:
            resposta = 'Digite o titulo da tarefa:'
            self.enviar_mensagem(resposta, chat_id)
            titulo, chat_id, update_id = self.receber_mensagem(update_id)
            if titulo.strip():
                break
            else:
                resposta = 'Digite um titulo!'
                self.enviar_mensagem(resposta, chat_id)

        resposta = 'Digite a descrição da tarefa:'
        self.enviar_mensagem(resposta, chat_id)
        descricao, chat_id, update_id = self.receber_mensagem(update_id)

        data = datetime.now().strftime("%Y-%m-%d")

        status = 'Pendente'

        while True:
            resposta = 'Digite o nome do funcionario:'
            self.enviar_mensagem(resposta, chat_id)
            funcionario, chat_id, update_id = self.receber_mensagem(update_id)
            if not self.user_validation(funcionario):
                break
            else:
                resposta = 'Funcionario nao encontrado!'
                self.enviar_mensagem(resposta, chat_id)

        while True:
            resposta = '''Escolha a prioridade ta tarefa:
/Alta
/Media
/Baixa'''
            self.enviar_mensagem(resposta, chat_id)
            escolha, chat_id, update_id = self.receber_mensagem(update_id)
            if escolha == '/Alta':
                prioridade = 'Alta'
                break
            elif escolha == '/Media':
                prioridade = 'Media'  
                break              
            elif escolha == '/Baixa':
                prioridade = 'Baixa'
                break
            else:
                resposta = 'Escolha uma opção válida!'
                self.enviar_mensagem(resposta, chat_id)

        return titulo, descricao, data, status, funcionario, prioridade

   #verificando se existem tarefas completadas
    def verificarTarefasCompletadas(self):
        for tarefa in self.__listaTarefas:
            if tarefa.get_status() == 'Completada':
                return True
    
    #verificando se existem tarefas pendentes na lista
    def verificarTarefasPendentes(self):
        for tarefa in self.__listaTarefas:
            if tarefa.get_status() == 'Pendente':
                return True

    #verificando se existem tarefas pendentes na lista        
    def verificarTarefasPendentesAtraso(self):
        for tarefa in self.__listaTarefas:
            if tarefa.get_status() == 'Pendente com atraso':
                return True
            
    #verificando se existem tarefas canceladas na lista
    def verificarTarefasCanceladas(self):
        for tarefa in self.__listaTarefas:
            if tarefa.get_status() == 'Cancelada':
                return True

    #mudando o titulo da lista de acordo com o status
    def titulo_lista_status(self,tipoStatus, chat_id):
        #verificando qual titulo colocar para a lista com base na escolha do usuario
        if tipoStatus == '/Completada' and self.verificarTarefasCompletadas():
            resposta = 'Lista de Tarefas Completadas'
            self.enviar_mensagem(resposta, chat_id)

        elif tipoStatus == '/Pendente' and self.verificarTarefasPendentes():
            resposta = 'Lista de Tarefas Pendentes'
            self.enviar_mensagem(resposta, chat_id)

        elif tipoStatus == '/Atrasada' and self.verificarTarefasPendentesAtraso():
            resposta = 'Lista de Tarefas Atrasadas'
            self.enviar_mensagem(resposta, chat_id)

        elif tipoStatus == '/Cancelada' and self.verificarTarefasCanceladas():
            resposta = 'Lista de Tarefas Canceladas'
            self.enviar_mensagem(resposta, chat_id)

        
    #verificando se existem valores na lista
    def verificarListaCheia(self, chat_id):
        if len(self.__listaTarefas):
            return True
        else: 
            resposta = 'Não existem tarefas na lista, Adicione novas tarefas para poder visualizar!'
            self.enviar_mensagem(resposta, chat_id)
        
    #adicionar tarefas a lista
    def adicionar_tarefa(self, chat_id, update_id):
        titulo, descricao, data, status, funcionario, prioridade = self.informacoes_tarefa(chat_id, update_id)
        tarefa = Tarefa(titulo,descricao,data,status, funcionario, prioridade)
        self.__listaTarefas.append(tarefa)
        resposta = 'Tarefa Adicionada com Sucesso!'
        self.enviar_mensagem(resposta, chat_id)

    #exibir as tarefas da lista
    def exibir_tarefa(self, chat_id, update_id):
        #verificando se existem tarefas na lista
        if self.verificarListaCheia(chat_id):
            resposta = 'Lista de Tarefas'
            self.enviar_mensagem(resposta, chat_id)

            for index, tarefa in enumerate(self.__listaTarefas):

                resposta = f'''Tarefa /{index+1}. {tarefa.get_titulo()}
Descrição: {tarefa.get_descricao()}
Criada em: {tarefa.get_data_criacao()}
Status: {tarefa.get_status()}
Atribuída ao funcionário: {tarefa.get_funcionario()}
Prioridade: {tarefa.get_prioridade()} '''
                self.enviar_mensagem(resposta, chat_id)

    #filtrando a lista de tarefas pelo status 
    def tarefas_status(self, chat_id, update_id):
        #verificando se existe algum valor na lista
        if self.verificarListaCheia(chat_id):
            while True:
                try:
                    #perguntando qual o filtro o usuario deseja utilizar
                    resposta = '''/Completada
/Pendente
/Atrasada
/Cancelada'''
                    self.enviar_mensagem(resposta, chat_id)
                    tipoStatus, chat_id, update_id = self.receber_mensagem(update_id)
                    break
                except:
                    resposta = 'Opção invalida! Digitte novamente.'
                    self.enviar_mensagem(resposta, chat_id)
            self.titulo_lista_status(tipoStatus, chat_id)            
            #exibindo a lista
            for index, tarefaStatus in enumerate(self.__listaTarefas):
                titulo = tarefaStatus.get_titulo()
                descricao = tarefaStatus.get_descricao()
                data = tarefaStatus.get_data_criacao()
                status = tarefaStatus.get_status()
                funcionario = tarefaStatus.get_funcionario()
                prioridade = tarefaStatus.get_prioridade()
                
                if tipoStatus == 1:
                    # verificando se existem tarefas completadas na lista
                    if self.verificarTarefasCompletadas(): 
                        #exibindo as tarefas que estao completadas
                        if status == 'Completada':
                            resposta = f'''Tarefa N{index+1}. {titulo}
Descrição: {descricao}
Criada em: {data}
Status: {status}
Atribuída ao funcionário: {funcionario}
Prioridade: {prioridade} '''
                            self.enviar_mensagem(resposta, chat_id)
                    else: 
                        resposta = 'Não existem tarefas Completadas!'
                        self.enviar_mensagem(resposta, chat_id)

                elif tipoStatus == 2:
                    # verificando se existem tarefas pendentes na lista
                    if self.verificarTarefasPendentes():
                        #exibindo as tarefas que estao pendentes
                        if status == 'Pendente':
                            resposta = f'''Tarefa N{index+1}. {titulo}
Descrição: {descricao}
Criada em: {data}
Status: {status}
Atribuída ao funcionário: {funcionario}
Prioridade: {prioridade} '''
                            self.enviar_mensagem(resposta, chat_id)
                    else: 
                        resposta = 'Não existem tarefas Pendentes!'
                        self.enviar_mensagem(resposta, chat_id)

                elif tipoStatus == 3:
                    # verificando se existem tarefas pendentes na lista
                    if self.verificarTarefasPendentesAtraso():
                        #exibindo as tarefas que estao pendentes com atraso
                        if status == 'Pendente com atraso':
                            resposta = f'''Tarefa N{index+1}. {titulo}
Descrição: {descricao}
Criada em: {data}
Status: {status}
Atribuída ao funcionário: {funcionario}
Prioridade: {prioridade} '''
                            self.enviar_mensagem(resposta, chat_id)
                    else: 
                        resposta = 'Não existem tarefas Atrasadas!'
                        self.enviar_mensagem(resposta, chat_id)

                elif tipoStatus == 4:
                    # verificando se existem tarefas canceladas na lista
                    if self.verificarTarefasCanceladas():
                        #exibindo as tarefas que estao canceladas
                        if status == 'Cancelada':
                            resposta = f'''Tarefa N{index+1}. {titulo}
Descrição: {descricao}
Criada em: {data}
Status: {status}
Atribuída ao funcionário: {funcionario}
Prioridade: {prioridade} '''
                            self.enviar_mensagem(resposta, chat_id)
                    else: 
                        resposta = 'Não existem tarefas Canceladas!'
                        self.enviar_mensagem(resposta, chat_id)

    #atualizando o status da tarefa
    def atualizarStatus(self, chat_id, update_id):
        if self.verificarListaCheia(chat_id):
            self.exibir_tarefa(chat_id, update_id)
            while True:               
                try: 
                    resposta = 'Escolha qual tarefa deseja atualizar:'
                    self.enviar_mensagem(resposta, chat_id)
                    escolha, chat_id, update_id = self.receber_mensagem(update_id)
                    escolha = int(escolha)-1
                    if self.__listaTarefas[escolha]:
                        break
                except:
                    resposta = 'Opção invalida, selecione um valor valido!'
                    self.enviar_mensagem(resposta, chat_id)

            resposta = f'''Qual status deseja colocar na tarefa {escolha+1}
/Completada
/Pendente
/Atrasada
/Cancelada'''
            self.enviar_mensagem(resposta, chat_id)
            statusesc, chat_id, update_id = self.receber_mensagem(update_id)
            if statusesc == '/Completada':
                status = 'Completada'
            elif statusesc == '/Pendente':
                status = 'Pendente'
            elif statusesc == '/Atrasada':
                status = 'Pendente com atraso'
            elif statusesc == '/Cancelada':
                status = 'Cancelada'

            tarefa = self.__listaTarefas[escolha]
            tarefa.set_status(status)
            resposta = 'Status atualizado com sucesso!'
            self.enviar_mensagem(resposta, chat_id)

    
    #filtrando tarefas
    def buscarTarefas(self, chat_id, update_id):
        if self.verificarListaCheia(chat_id):
            i = 0
            resposta = 'Digite a palavra chave ou titulo da tarefa:'
            self.enviar_mensagem(resposta, chat_id)
            busca, chat_id, update_id = self.receber_mensagem(update_id)

            for index, tarefa in enumerate(self.__listaTarefas):
                titulo = tarefa.get_titulo()
                if busca in titulo.split():
                    resposta = f'''Tarefa N{index+1}. {tarefa.get_titulo()}
Descrição: {tarefa.get_descricao()}
Criada em: {tarefa.get_data_criacao()}
Status: {tarefa.get_status()}
Atribuída ao funcionário: {tarefa.get_funcionario()}
Prioridade: {tarefa.get_prioridade()} '''
                    self.enviar_mensagem(resposta, chat_id)

                    i += 1
            if i == 0:
                resposta = 'Nenhuma tarefa encontrada!'
                self.enviar_mensagem(resposta, chat_id)


    #editando tarefas existentes
    def editarTarefas(self, chat_id, update_id):
        if self.verificarListaCheia(chat_id):
            self.exibir_tarefa(chat_id, update_id)
            while True: 
                try:
                    resposta = 'Qual tarefa deseja editar:'
                    self.enviar_mensagem(resposta, chat_id)
                    escolha, chat_id, update_id = self.receber_mensagem(update_id)
                    escolha = int(escolha)-1
                    tarefa = self.__listaTarefas[escolha]
                    break
                except:
                    resposta = 'Opção invalida, digite novamente:'
                    self.enviar_mensagem(resposta, chat_id)

            while True:                              
                resposta = '''O que deseja atualizar?
/Titulo
/Descricao
/Data
/Status
/Funcionario
/Prioridade
/Todas as informacoes'''
                self.enviar_mensagem(resposta, chat_id)
                opcaoAtualizar, chat_id, update_id = self.receber_mensagem(update_id)
                    
                if opcaoAtualizar == '/Titulo':
                    while True:
                        resposta = 'Digite o titulo da tarefa:'
                        self.enviar_mensagem(resposta, chat_id)
                        titulo, chat_id, update_id = self.receber_mensagem(update_id)

                        if titulo.strip():
                            break
                        else:
                            resposta = 'Digite um titulo!'
                            self.enviar_mensagem(resposta, chat_id)

                    tarefa.set_titulo(titulo)
                    resposta = 'Titulo atualizado com sucesso!'
                    self.enviar_mensagem(resposta, chat_id)
                    break

                elif opcaoAtualizar == '/Descricao':
                    resposta = 'Digite a descrição da tarefa:'
                    self.enviar_mensagem(resposta, chat_id)
                    descricao, chat_id, update_id = self.receber_mensagem(update_id)

                    tarefa.set_descricao(descricao)
                    resposta = 'Descrição atualizada com sucesso!'
                    self.enviar_mensagem(resposta, chat_id)
                    break

                elif opcaoAtualizar == '/Data':
                    data = datetime.now().strftime("%Y-%m-%d")
                    tarefa.set_data(data)
                    resposta = 'Data atualizada com sucesso!'
                    self.enviar_mensagem(resposta, chat_id)
                    break

                elif opcaoAtualizar == '/Status':
                    resposta = f'Qual status deseja colocar na tarefa {escolha+1}'
                    self.enviar_mensagem(resposta, chat_id)

                    resposta = '''/Completada
/Pendente
/Atrasada
/Cancelada'''
                    self.enviar_mensagem(resposta, chat_id)
                    statusesc, chat_id, update_id = self.receber_mensagem(update_id)

                    if statusesc == '/Completada':
                        status = 'Completada'
                    elif statusesc == '/Pendente':
                        status = 'Pendente'
                    elif statusesc == '/Atrasada':
                        status = 'Pendente com atraso'
                    elif statusesc == '/Cancelada':
                        status = 'Cancelada'

                    tarefa.set_status(status)

                    resposta = 'Status atualizado com sucesso!'
                    self.enviar_mensagem(resposta, chat_id)
                    break

                elif opcaoAtualizar == '/Funcionario':
                    resposta = 'Digite o funcionario:'
                    self.enviar_mensagem(resposta, chat_id)
                    funcionario, chat_id, update_id = self.receber_mensagem(update_id)
                    tarefa.set_funcionario(funcionario)
                    resposta = 'Funcionario atualizado com sucesso!'
                    self.enviar_mensagem(resposta, chat_id)
                    break

                elif opcaoAtualizar == '/Prioridade':
                    while True:
                        resposta = '''Escolha a prioridade da tarefa:
/Alta
/Media
/Baixa'''
                        self.enviar_mensagem(resposta, chat_id)
                        escolha, chat_id, update_id = self.receber_mensagem(update_id)

                        if escolha == '/Alta':
                            prioridade = 'Alta'
                            break
                        elif escolha == '/Media':
                            prioridade = 'Media'  
                            break              
                        elif escolha == '/Baixa':
                            prioridade = 'Baixa'
                            break
                        else:
                            resposta = 'Escolha uma opção válida!'
                            self.enviar_mensagem(resposta, chat_id)

                    tarefa.set_prioridade(prioridade)
                    resposta = 'Prioridade atualizada com sucesso!'
                    self.enviar_mensagem(resposta, chat_id)
                    break

                elif opcaoAtualizar == '/Todas':
                    while True:
                        resposta = 'Digite o titulo da tarefa:'
                        self.enviar_mensagem(resposta, chat_id)
                        titulo, chat_id, update_id = self.receber_mensagem(update_id)

                        if titulo.strip():
                            break
                        else:
                            resposta = 'Digite um titulo!'
                            self.enviar_mensagem(resposta, chat_id)

                    resposta = 'Digite a descrição da tarefa:'
                    self.enviar_mensagem(resposta, chat_id)
                    descricao, chat_id, update_id = self.receber_mensagem(update_id)

                    data = datetime.now().strftime("%Y-%m-%d")

                    resposta = f'Qual status deseja colocar na tarefa {escolha+1}'
                    self.enviar_mensagem(resposta, chat_id)

                    resposta = '''/Completada
/Pendente
/Atrasada
/Cancelada'''
                    self.enviar_mensagem(resposta, chat_id)
                    statusesc, chat_id, update_id = self.receber_mensagem(update_id)

                    if statusesc == '/Completada':
                        status = 'Completada'
                    elif statusesc == '/Pendente':
                        status = 'Pendente'
                    elif statusesc == '/Atrasada':
                        status = 'Pendente com atraso'
                    elif statusesc == '/Cancelada':
                        status = 'Cancelada'


                    resposta = 'Digite o funcionario:'
                    self.enviar_mensagem(resposta, chat_id)
                    funcionario, chat_id, update_id = self.receber_mensagem(update_id)

                    while True:
                        resposta = '''Escolha a prioridade da tarefa:
/Alta
/Media
/Baixa'''
                        self.enviar_mensagem(resposta, chat_id)
                        escolha, chat_id, update_id = self.receber_mensagem(update_id)

                        if escolha == '/Alta':
                            prioridade = 'Alta'
                            break
                        elif escolha == '/Media':
                            prioridade = 'Media'  
                            break              
                        elif escolha == '/Baixa':
                            prioridade = 'Baixa'
                            break
                        else:
                            resposta = 'Escolha uma opção válida!'
                            self.enviar_mensagem(resposta, chat_id)
                    
                    tarefa.set_prioridade(prioridade)
                    tarefa.set_funcionario(funcionario)
                    tarefa.set_titulo(titulo)
                    tarefa.set_descricao(descricao)
                    tarefa.set_data(data)
                    tarefa.set_status(status)
                    resposta = 'Dados atualizados com sucesso!'
                    self.enviar_mensagem(resposta, chat_id)
                    break


    #excluindo tarefas
    def excluirTarefa(self, chat_id, update_id):
        if self.verificarListaCheia(chat_id):
            self.exibir_tarefa(chat_id, update_id)
        while True: 
            try:
                resposta = 'Qual tarefa deseja excluir:'
                self.enviar_mensagem(resposta, chat_id)
                escolha, chat_id, update_id = self.receber_mensagem(update_id)
                escolha = int(escolha)-1
                tarefa = self.__listaTarefas[escolha]
                break
            except:
                resposta = 'Não existe essa tarefa na lista, digite novamente:'
                self.enviar_mensagem(resposta, chat_id)

        self.__listaTarefas.remove(tarefa)
        resposta = 'Tarefa excluida com sucesso!'
        self.enviar_mensagem(resposta, chat_id)

    def alterar_prioridade(self, chat_id, update_id):

        if self.verificarListaCheia(chat_id):
            self.exibir_tarefa(chat_id, update_id)
            while True: 
                try:
                    resposta = 'Qual tarefa deseja editar:'
                    self.enviar_mensagem(resposta, chat_id)
                    escolha, chat_id, update_id = self.receber_mensagem(update_id)
                    escolha = int(escolha)-1
                    tarefa = self.__listaTarefas[escolha]
                    break
                except:
                    resposta = 'Opção invalida, digite novamente:'
                    self.enviar_mensagem(resposta, chat_id)

            while True:
                resposta = '''Escolha a prioridade ta tarefa:
/Alta
/Media
/Baixa'''
                self.enviar_mensagem(resposta, chat_id)
                escolha, chat_id, update_id = self.receber_mensagem(update_id)
                if escolha == '/Alta':
                    prioridade = 'Alta'
                    break
                elif escolha == '/Media':
                    prioridade = 'Media'  
                    break              
                elif escolha == '/Baixa':
                    prioridade = 'Baixa'
                    break
                else:
                    resposta = 'Escolha uma opção válida!'
                    self.enviar_mensagem(resposta, chat_id)

            tarefa.set_prioridade(prioridade)
            resposta = 'Prioridade atualizada com sucesso!'
            self.enviar_mensagem(resposta, chat_id)


    def atribuir_funcionario(self, chat_id, update_id):
        if self.verificarListaCheia(chat_id):
            self.exibir_tarefa(chat_id, update_id)
            while True: 
                try:
                    resposta = 'Qual tarefa deseja editar:'
                    self.enviar_mensagem(resposta, chat_id)
                    escolha, chat_id, update_id = self.receber_mensagem(update_id)
                    escolha = int(escolha)-1
                    tarefa = self.__listaTarefas[escolha]
                    break
                except:
                    resposta = 'Opção invalida, digite novamente:'
                    self.enviar_mensagem(resposta, chat_id)

            while True:
                resposta = 'Digite o nome do funcionario:'
                self.enviar_mensagem(resposta, chat_id)
                funcionario, chat_id, update_id = self.receber_mensagem(update_id)
                if not self.user_validation(funcionario):
                    break
                else:
                    resposta = 'Funcionario nao encontrado!'
                    self.enviar_mensagem(resposta, chat_id)

            tarefa.set_funcionario(funcionario)
            resposta = 'Funcionario atribuido com sucesso!'
            self.enviar_mensagem(resposta, chat_id)





# Funcoes tarefas -------------------------------------------------------------
   
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
            if choice == '/Funcionarios':
                self.register_employee(chat_id, update_id)

            elif choice == '/Tarefas':
                while True:
                    resposta = '''O que você deseja fazer? 
/Adicionar Tarefas 
/Editar Tarefas 
/Visualizar Tarefas 
/Excluir Tarefas 
/Alterar prioridade das Tarefas 
/Filtrar Tarefas
/Buscar Tarefas
/Atribuir funcionario
/Sair'''
                    self.enviar_mensagem(resposta, chat_id)
                    choice, chat_id, update_id = self.receber_mensagem(update_id)
                    
                    if choice == '/Adicionar':
                        self.adicionar_tarefa(chat_id, update_id)
                    elif choice == '/Editar':
                        self.editarTarefas(chat_id, update_id)
                    elif choice == '/Visualizar':
                        self.exibir_tarefa(chat_id, update_id)
                    elif choice == '/Excluir':
                        self.excluirTarefa(chat_id, update_id)
                    elif choice == '/Alterar':
                        self.alterar_prioridade(chat_id, update_id)
                    elif choice == '/Filtrar':
                        self.tarefas_status(chat_id, update_id)
                    elif choice == '/Buscar':
                        self.buscarTarefas(chat_id, update_id)
                    elif choice == '/Atribuir':
                        self.atribuir_funcionario(chat_id, update_id)
                    elif choice == '/Sair':
                        break
                    else:
                        resposta = 'Escolha uma opção válida'
                        self.enviar_mensagem(resposta, chat_id)
                        choice, chat_id, update_id = self.receber_mensagem(update_id)

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






