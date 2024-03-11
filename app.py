
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
    


    def informacoes_tarefa(self):
        while True:
            titulo = input(f'\nDigite o titulo da tarefa: ')
            if titulo.strip():
                break
            else:
                print('\nDigite um titulo!')
        descricao = input(f'\nDigite a descrição da tarefa: ')
        data = datetime.now().strftime("%Y-%m-%d")
        status = 'Pendente'
        while True:
            funcionario = input(f'\nDigite o nome do funcionario: ')
            if not self.user_validation(funcionario):
                break
            else:
                print('\nFuncionario nao encontrado!')

        while True:
            escolha = input(f'\nEscolha a prioridade ta tarefa: \n1.Alta \n2.Média \n3.Baixa ')
            if escolha == '1':
                prioridade = 'Alta'
                break
            elif escolha == '2':
                prioridade = 'Media'  
                break              
            elif escolha == '3':
                prioridade = 'Baixa'
                break
            else:
                print('\nEscolha uma opção válida!')

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
    def titulo_lista_status(self,tipoStatus):
        #verificando qual titulo colocar para a lista com base na escolha do usuario
        if tipoStatus == 1 and self.verificarTarefasCompletadas():
            print('\nLista de Tarefas Completadas')
        elif tipoStatus == 2 and self.verificarTarefasPendentes():
            print('\n Lista de Tarefas Pendentes')
        elif tipoStatus == 3 and self.verificarTarefasPendentesAtraso():
            print('\n Lista de Tarefas Pendentes com Atraso')
        elif tipoStatus == 4 and self.verificarTarefasCanceladas():
            print('\n Lista de Tarefas Canceladas')
        
    #verificando se existem valores na lista
    def verificarListaCheia(self):
        if len(self.__listaTarefas):
            return True
        else: 
            print('\nNão existem tarefas na lista, Adicione novas tarefas para poder visualizar!')
        
    #adicionar tarefas a lista
    def adicionar_tarefa(self):
        titulo, descricao, data, status, funcionario, prioridade = self.informacoes_tarefa()
        tarefa = Tarefa(titulo,descricao,data,status, funcionario, prioridade)
        self.__listaTarefas.append(tarefa)
        print('\n------------------------------------------------------------------')
        print('\nTarefa Adicionada com Sucesso!')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')

    #exibir as tarefas da lista
    def exibir_tarefa(self):
        #verificando se existem tarefas na lista
        if self.verificarListaCheia():
            print('\nLista de Tarefas')
            for index, tarefa in enumerate(self.__listaTarefas):
                print(f'\nTarefa N{index+1}. {tarefa.get_titulo()}')
                print(f'Descrição: {tarefa.get_descricao()}')
                print(f'Criada em: {tarefa.get_data_criacao()}')
                print(f'Status: {tarefa.get_status()}')
                print(f'Atribuída ao funcionário: {tarefa.get_funcionario()}')
                print(f'Prioridade: {tarefa.get_prioridade()}')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')

    #filtrando a lista de tarefas pelo status 
    def tarefas_status(self):
        #verificando se existe algum valor na lista
        if self.verificarListaCheia():
            while True:
                try:
                    #perguntando qual o filtro o usuario deseja utilizar
                    tipoStatus = int(input('\n1. Completada \n2. Pendente \n3. Pendente com atraso \n4. Cancelada \n: '))
                    print('\n------------------------------------------------------------------')
                    break
                except:
                    print('\nOpção invalida! Digitte novamente.')
            self.titulo_lista_status(tipoStatus)            
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
                            print(f'\nTarefa N{index+1}. {titulo}')
                            print(f'Descrição: {descricao}')
                            print(f'Criada em: {data}')
                            print(f'Status: {status}')
                            print(f'Funcionario: {funcionario}')
                            print(f'Prioridade: {prioridade}')
                    else: 
                        print('\nNão existem tarefas Completadas!')

                elif tipoStatus == 2:
                    # verificando se existem tarefas pendentes na lista
                    if self.verificarTarefasPendentes():
                        #exibindo as tarefas que estao pendentes
                        if status == 'Pendente':
                            print(f'\nTarefa N{index+1}. {titulo}')
                            print(f'Descrição: {descricao}')
                            print(f'Criada em: {data}')
                            print(f'Status: {status}')
                            print(f'Funcionario: {funcionario}')
                            print(f'Prioridade: {prioridade}')
                    else: 
                        print('\nNão existem tarefas Pendentes!')

                elif tipoStatus == 3:
                    # verificando se existem tarefas pendentes na lista
                    if self.verificarTarefasPendentesAtraso():
                        #exibindo as tarefas que estao pendentes com atraso
                        if status == 'Pendente com atraso':
                            print(f'\nTarefa N{index+1}. {titulo}')
                            print(f'Descrição: {descricao}')
                            print(f'Criada em: {data}')
                            print(f'Status: {status}')
                            print(f'Funcionario: {funcionario}')
                            print(f'Prioridade: {prioridade}')
                    else: 
                        print('\nNão existem tarefas Pendentes com Atraso!')

                elif tipoStatus == 4:
                    # verificando se existem tarefas canceladas na lista
                    if self.verificarTarefasCanceladas():
                        #exibindo as tarefas que estao canceladas
                        if status == 'Cancelada':
                            print(f'\nTarefa N{index+1}. {titulo}')
                            print(f'Descrição: {descricao}')
                            print(f'Criada em: {data}')
                            print(f'Status: {status}')
                            print(f'Funcionario: {funcionario}')
                            print(f'Prioridade: {prioridade}')
                    else: 
                        print('\nNão existem tarefas Canceladas!')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')

    #atualizando o status da tarefa
    def atualizarStatus(self):
        if self.verificarListaCheia():
            self.exibir_tarefa()
            while True:               
                try: 
                    escolha = int(input('\nDigite qual tarefa deseja atualizar: '))-1
                    if self.__listaTarefas[escolha]:
                        break
                except:
                    print('\nOpção invalida, selecione um valor valido!')
            print(f'\nQual status deseja colocar na tarefa {escolha+1}')
            statusesc = input('\n1. Completada \n2. Pendente \n3. Pendente com atraso \n4. Cancelada \n: ')

            if statusesc == '1':
                status = 'Completada'
            elif statusesc == '2':
                status = 'Pendente'
            elif statusesc == '3':
                status = 'Pendente com atraso'
            elif statusesc == '4':
                status = 'Cancelada'

            tarefa = self.__listaTarefas[escolha]
            tarefa.set_status(status)
            print('\nStatus atualizado com sucesso!')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')
    
    #filtrando tarefas
    def buscarTarefas(self):
        if self.verificarListaCheia():
            i = 0
            busca = input('\nDigite a palavra chave ou titulo da tarefa: ')
            for index, tarefa in enumerate(self.__listaTarefas):
                titulo = tarefa.get_titulo()
                if busca in titulo.split():
                    print(f'\nTarefa N{index+1}. {titulo}')
                    print(f'Descrição: {tarefa.get_descricao()}')
                    print(f'Criada em: {tarefa.get_data_criacao()}')
                    print(f'Status: {tarefa.get_status()}')
                    print(f'Funcionario: {tarefa.get_funcionario()}')
                    print(f'Prioridade: {tarefa.get_prioridade()}')
                    i += 1
            if i == 0:
                print('\nNenhuma tarefa encontrada!')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')

    #editando tarefas existentes
    def editarTarefas(self):
        if self.verificarListaCheia():
            self.exibir_tarefa()
            while True: 
                try:
                    escolha = int(input('\nQual tarefa deseja editar: '))-1
                    tarefa = self.__listaTarefas[escolha]
                    break
                except:
                    print('\nOpção invalida, digite novamente: ')
            while True:               
                try:
                    opcaoAtualizar = int(input('\n1. Atualizar o titulo \n2. Atualizar a descrição \n3. Atualizar a data \n4. Atualizar o status \n5. Atualizar o funcionario \n6. Atualizar prioridade \n7. Atualizar todas as informações \n: '))
                    if opcaoAtualizar > 0 and opcaoAtualizar < 8:
                        break
                except:
                    print('\nEscolha uma opção valida!')
            if opcaoAtualizar == 1:
                while True:
                    titulo = input(f'\nDigite o titulo da tarefa: ')
                    if titulo.strip():
                        break
                    else:
                        print('\nDigite um titulo!')
                tarefa.set_titulo(titulo)
                print('\nTitulo atualizado com sucesso!')

            elif opcaoAtualizar == 2:
                descricao = input(f'\nDigite a descrição da tarefa: ')
                tarefa.set_descricao(descricao)
                print('\nDescrição atualizada com sucesso!')

            elif opcaoAtualizar == 3:
                data = datetime.now().strftime("%Y-%m-%d")
                tarefa.set_data(data)
                print('\nData atualizada com sucesso!')

            elif opcaoAtualizar == 4:
                print(f'\nQual status deseja colocar na tarefa {escolha+1}')
                statusesc = input('\n1. Completada \n2. Pendente \n3. Pendente com atraso \n4. Cancelada \n: ')

                if statusesc == '1':
                    status = 'Completada'
                elif statusesc == '2':
                    status = 'Pendente'
                elif statusesc == '3':
                    status = 'Pendente com atraso'
                elif statusesc == '4':
                    status = 'Cancelada'
                tarefa.set_status(status)
                print('\nStatus atualizado com sucesso!')

            elif opcaoAtualizar == 5:
                funcionario = input(f'\nDigite o funcionario: ')
                tarefa.set_funcionario(funcionario)
                print('\nFuncionario atualizado com sucesso!')

            elif opcaoAtualizar == 6:
                while True:
                    escolha = input(f'\nEscolha a prioridade ta tarefa: \n1.Alta \n2.Média \n3.Baixa ')
                    if escolha == '1':
                        prioridade = 'Alta'
                        break
                    elif escolha == '2':
                        prioridade = 'Media'  
                        break              
                    elif escolha == '3':
                        prioridade = 'Baixa'
                        break
                    else:
                        print('\nEscolha uma opção válida!')
                tarefa.set_prioridade(prioridade)
                print('\nPrioridade atualizada com sucesso!')

            elif opcaoAtualizar == 7:
                while True:
                    titulo = input(f'\nDigite o titulo da tarefa: ')
                    if titulo.strip():
                        break
                    else:
                        print('\nDigite um titulo!')
                descricao = input(f'\nDigite a descrição da tarefa: ')
                data = datetime.now().strftime("%Y-%m-%d")
                print(f'\nQual status deseja colocar na tarefa {escolha+1}')
                statusesc = input('\n1. Completada \n2. Pendente \n3. Pendente com atraso \n4. Cancelada \n: ')

                if statusesc == '1':
                    status = 'Completada'
                elif statusesc == '2':
                    status = 'Pendente'
                elif statusesc == '3':
                    status = 'Pendente com atraso'
                elif statusesc == '4':
                    status = 'Cancelada'

                funcionario = input(f'\nDigite o funcionario: ')

                while True:
                    escolha = input(f'\nEscolha a prioridade ta tarefa: \n1.Alta \n2.Média \n3.Baixa ')
                    if escolha == '1':
                        prioridade = 'Alta'
                        break
                    elif escolha == '2':
                        prioridade = 'Media'  
                        break              
                    elif escolha == '3':
                        prioridade = 'Baixa'
                        break
                    else:
                        print('\nEscolha uma opção válida!')
                
                tarefa.set_prioridade(prioridade)
                tarefa.set_funcionario(funcionario)
                tarefa.set_titulo(titulo)
                tarefa.set_descricao(descricao)
                tarefa.set_data(data)
                tarefa.set_status(status)
                print('\nDados atualizados com sucesso!')

        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')

    #excluindo tarefas
    def excluirTarefa(self):
        if self.verificarListaCheia():
            self.exibir_tarefa()
        while True: 
            try:
                escolha = int(input('\nQual tarefa deseja excluir: '))-1
                tarefa = self.__listaTarefas[escolha]
                break
            except:
                print('\nNão existe essa tarefa na lista, digite novamente: ')
        self.__listaTarefas.remove(tarefa)
        print('\nTarefa excluida com sucesso!')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')

    def alterar_prioridade(self):

        if self.verificarListaCheia():
            self.exibir_tarefa()
            while True: 
                try:
                    escolha = int(input('\nQual tarefa deseja editar: '))-1
                    tarefa = self.__listaTarefas[escolha]
                    break
                except:
                    print('\nOpção invalida, digite novamente: ')
            while True:
                escolha = input(f'\nEscolha a prioridade ta tarefa: \n1.Alta \n2.Média \n3.Baixa ')
                if escolha == '1':
                    prioridade = 'Alta'
                    break
                elif escolha == '2':
                    prioridade = 'Media'  
                    break              
                elif escolha == '3':
                    prioridade = 'Baixa'
                    break
                else:
                    print('\nEscolha uma opção válida!')
            tarefa.set_prioridade(prioridade)
            print('\nPrioridade atualizada com sucesso!')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')

    def atribuir_funcionario(self):
        if self.verificarListaCheia():
            self.exibir_tarefa()
            while True: 
                try:
                    escolha = int(input('\nQual tarefa deseja editar: '))-1
                    tarefa = self.__listaTarefas[escolha]
                    break
                except:
                    print('\nOpção invalida, digite novamente: ')
            while True:
                funcionario = input(f'\nDigite o nome do funcionario: ')
                if not self.user_validation(funcionario):
                    break
                else:
                    print('\nFuncionario nao encontrado!')
            tarefa.set_funcionario(funcionario)
            print('\nFuncionario atribuido com sucesso!')
        print('\n------------------------------------------------------------------')
        input('\nPressione ENTER para continuar...\n')





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
            print(choice)
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
                        self.adicionar_tarefa()
                    elif choice == '/Editar':
                        self.editarTarefas()
                    elif choice == '/Visualizar':
                        self.exibir_tarefa()
                    elif choice == '/Excluir':
                        self.excluirTarefa()
                    elif choice == '/Alterar':
                        self.alterar_prioridade()
                    elif choice == '/Filtrar':
                        self.tarefas_status()
                    elif choice == '/Buscar':
                        self.buscarTarefas()
                    elif choice == '/Atribuir':
                        self.atribuir_funcionario()
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






