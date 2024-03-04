
import re

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
    def register_employee(self):
        while True:
            name = input('\nDigite o nome do funcionario: ')
            if not self.character_validation(name):
                if self.user_validation(name):
                    break
                else:
                    print('\nEste nome de usuário não está disponível!')

            else:
                print('\nDigite um nome válido, SEM caracteres especiais!')

        while True:
            password = input('\nDigite uma senha. Ela deve possuir ao menos 6 caracteres, uma letra maiúscula e um caractere especial: ') 
            if len(password) < 6:
                print('\nA senha deve ter ao menos 6 caracteres!')
            else:
                if self.character_validation(password):
                    if self.isupper_validation(password):
                        break
                else:
                    print('\nDigite ao menos um carcatere especial!')

        while True:
            passwordConfirm = input('\nDigite a senha novamente: ') 
            if password == passwordConfirm:
                break
            else:
                print('\nAs senhas são diferentes!')

        while True:
            choice = input('\nQual o cargo operacional do funcionário? \n1.Administrador \n2.Funcionário \n: ')
            if choice == '1':
                office = 'administrator'
                break
            
            elif choice == '2':
                office = 'employee'
                break
            
            else: 
                print('\nDigite uma opção válida!')
        logado = False
        employee = User(name, password, office, logado)
        self.__usuarios.append(employee)
        print('\nUsuário cadastrado com sucesso!')

    def character_validation(self, string):
        regex = re.compile(r'[^\w\s]')
        if regex.search(string) is None:
            return False
        else:
            return True
    
    def isupper_validation(self, string):
        for char in string:
            if char.isupper():
                return True
            else:
                print('\nDigite ao menos uma letra maiúsula!')
                return False

    def user_validation(self, name):
        for user in self.__usuarios:
            if user.get_name() == name:
                return False
        return True
# Cadastrar tarefas
            

# Exibir menu
            
    def exibir_menu(self):
        while True:
            print('\nMenu Lista de Tarefas \nO que você deseja fazer? \n1.Login \n2.Sair')
            choice = input(': ')
            if choice == '1':
                print('\nTela de Login\n')
                name = input('\nDigite seu nome de usuário: ')
                office = self.login(name)
                if office:
                    return office
                else:
                    return 'Error'
                
            elif choice == '2':
                print('Finalizando programa!')
                return False
            else:
                print('Selecione uma opção válida!')

    def login(self, name):
        for user in self.__usuarios:
            if user.get_name() == name:
                tentativas = 3
                while tentativas > 0:
                    password = input('\nDigite sua senha: ')
                    if user.get_password() == password:
                        user.set_logado(True)
                        print('\nLogin realizado com sucesso!')
                        return user.get_office()
                    else:
                        print('\nSua senha esta incorreta!')
                        tentativas -= 1
                print('\nTentativas esgotadas. Saindo...')
                return False
        print('\nUsuário não encontrado!')
        return False

    def exibir_menu_adm(self):
        print('\nMenu de Adminstrador!\n\n')
        while True:
            choice = input('\nO que você deseja fazer? \n1.Funcionários \n2.Tarefas \n3.Sair \n: ')
            if choice == '1':
                choice = input('\nO que você deseja fazer? \n1.Cadastrar Funcionários \n2.Excluir Funcionários \n3.Visualizar Funcionários \n4.Sair \n: ')
                if choice == '1': self.register_employee()
                elif choice == '2': pass
                elif choice == '3': pass
                elif choice =='4': pass
                else: print('\nDigite uma opção válida!')


            elif choice == '2':
                choice = input('\nO que você deseja fazer? \n1. Adicionar Tarefas \n2.Editar Tarefas \n3.Visualizar Tarefas \n4.Excluir Tarefas \n5.Tornar Tarefas Prioridade \n6.Retirar Prioridade das tarefas \n7.Sair')
                break

            elif choice == '3':
                return False
            else:
                print('\nDigite uma opção válida!')
       
# Looping de execucao
    def looping_execucao(self):
        while True:
            office = self.exibir_menu()
            print(office)
            if office == 'administrator' or office == 'employee':
                while True:
                    if office == 'administrator':
                        office = self.exibir_menu_adm() 
                        if office:
                            pass
                        else: break
                        
                    elif office == 'employee':
                        pass
                        
                    else: 
                        break
            elif office == 'Error': pass
            else: break


init = Manager()
init.looping_execucao()
