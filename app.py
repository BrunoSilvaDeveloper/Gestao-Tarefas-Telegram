
import re

class User():
    def __init__(self, name, password, office):
        self.__name = name
        self.__password = password
        self.__office = office

    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password
    
    def get_office(self):
        return self.__office
    
    def set_name(self,name):
        self.__name = name
    
    def set_password(self, password):
        self.__password = password
    
    def set_office(self, office):
        self.__office = office

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

class Functions(Task, User):
    def __init__(self):
        self.__usuarios = []

    def get_users(self):
        return self.__usuarios

# Cadastrar Usuarios
    def register_employee(self):
        while True:
            name = input('\nDigite o nome do funcionario: ')
            if not self.character_validation(name):
                break
            else:
                print('\nDigite um noome válido, SEM caracteres especiais!')

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

        employee = User(name, password, office)
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
    
# Cadastrar tarefas
            

        
class Manager(Functions):
    def __init__(self):
        pass

init = Functions()
init.register_employee()