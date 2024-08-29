from datetime import datetime, date
import re
import json

class Paciente:
  def __init__(self, id: int, nome: str, email: str, fone: int, nasc: date):
    self.__id = 0
    self.__nome = "nome"
    self.__email = "teste@gmail.com"
    self.__fone = 0
    self.__nasc = None
    self.set_id(id)
    self.set_nome(nome)
    self.set_email(email)
    self.set_fone(fone)
    self.set_nasc(nasc)
  def set_id(self, id: int):
    if id > -1:
      self.__id = id
    else:
      raise ValueError("ID inválido, tente novamente")
  def get_id(self):
    return self.__id
  def set_nome (self, n: str):
    if n != "":
      self.__nome = n
    else:
      raise ValueError("Preencha todos os campos e digite seu nome, por favor")
  def get_nome(self):
    return self.__nome
  def set_fone(self, fone: int):
    if fone > 0:
      self.__fone = fone
    else:
      raise ValueError("Preencha todos os campos e digite um número para entrarmos em contato caso necessário, por favor")
  def get_fone(self):
    return self.__fone
  def set_nasc(self, nasc: str):
    try:
      data_nascimento = datetime.strptime(nasc, "%d/%m/%Y").date()
      data_hoje = date.today()
      if data_nascimento < data_hoje:
          self.__nasc = data_nascimento
      else:
        raise ValueError("Insira uma data válida e anterior ao dia atual")
    except ValueError:
            raise ValueError("Formato de data inválido. Use o formato dd/mm/aaaa")
  def get_nasc(self):
    return self.__nasc
  def set_email(self, e: str):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, e):
            self.__email = e
        else:
            raise ValueError("E-mail inválido. Digite um e-mail válido.")
  def get_email(self):
     return self.__email
  def to_json(self):
        dic = {}                                          
        dic["id"] = self.__id                             
        dic["nome"] = self.__nome                         
        dic["email"] = self.__email                      
        dic["fone"] = self.__fone                         
        dic["nasc"] = self.__nasc.strftime('%d/%m/%Y')    
        
        return dic                                        
  def __str__(self):
    return f"{self.get_id()} - {self.get_nome()} - {self.get_email()} - {self.get_fone()} - {self.__nasc.strftime('%d/%m/%Y')} "

class NPaciente:
  objetos = []  
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    max_id = max((c.get_id() for c in cls.objetos), default=0)
    obj.set_id(max_id + 1)
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.get_id() == id: 
        return c
    return None 
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.get_id()) 
    if c != None:
        c.set_nome(obj.get_nome())
        c.set_email(obj.get_email())
        c.set_fone(obj.get_fone())
        c.set_nasc(obj.get_nasc().strftime('%d/%m/%Y'))
    cls.salvar()
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())  
    if c is not None:
        cls.objetos.remove(c)
        cls.salvar()

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
        with open("NPaciente.json", mode = "r" ) as arquivo:
          texto = json.load(arquivo)
          for obj in texto:
            c = Paciente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["nasc"])
            cls.objetos.append(c)                     
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):  
    with open("NPaciente.json", mode = "w") as arquivo:  
        json.dump(cls.objetos, arquivo, default = Paciente.to_json) 
  @classmethod
  def Aniversariantes(cls, mes):  

    return [p for p in cls.objetos if p.get_nasc().month == mes]

class UI:
  @staticmethod
  def menu():
    print("MENU DO PACIENTE \n1 - Inserir Paciente \n2 - listar Pacientes \n3 - atualizar Paciente \n4 - excluir Paciente \n5 - Listar Aniversariantes do Mês")
    print("0 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = -1
    while op != 0: 
      op = UI.menu()
      if op == 1: UI.Paciente_inserir()
      if op == 2: UI.Paciente_listar()
      if op == 3: UI.Paciente_atualizar()
      if op == 4: UI.Paciente_excluir()
      if op == 5: UI.Paciente_aniversariantes()
  @staticmethod
  def Paciente_inserir():
    nome = input("Informe o nome: ")
    nasc = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    fone = int(input("Informe o fone: "))
    email = input("Informe um e-mail para contato: ")
    c = Paciente(0, nome, email, fone, nasc)
    NPaciente.inserir(c)
  @staticmethod
  def Paciente_listar():
    for c in NPaciente.listar():
      print(c)

  @staticmethod
  def Paciente_atualizar():
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser atualizado: "))
    nome = input("Informe o nome: ")
    nasc = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    fone = int(input("Informe o fone: "))
    email = input("Informe um e-mail para contato: ")
    c = Paciente(id, nome, email, fone, nasc)
    NPaciente.atualizar(c)

  @staticmethod
  def Paciente_excluir():
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser excluído: "))
    paciente = NPaciente.listar_id(id)
    if paciente:
        NPaciente.excluir(paciente)
        print("Paciente excluído com sucesso.")
    else:
        print("Paciente não encontrado.")
    pass

  @staticmethod
  def Paciente_aniversariantes():
    mes = int(input("Informe o mês para listar aniversariantes (1-12): "))
    aniversariantes = NPaciente.Aniversariantes(mes)
    if aniversariantes:
        for c in aniversariantes:
            print(c)
    else:
        print("Nenhum paciente encontrado para o mês informado.")
UI.main()    
