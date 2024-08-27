# CRUD de Pacientes - cadastro de Pacientes - lista
# C - Create - insere um Paciente no cadastro
# R - Read - lê os Pacientes cadastrados
# U - Update - atualiza os dados de um Paciente
# D - Delete - remove um Paciente do cadastro
from datetime import datetime, date
import json

# Modelo
class Paciente:
  def __init__(self, id, nome, nasc, fone):
    self.__id = 0
    self.__nome = "nome"
    self.__fone = 0
    self.__nasc = None
    self.set_id(id)
    self.set_nome(nome)
    self.set_fone(fone)
    self.set_nasc(nasc)
  def set_id(self, id):
    if id > -1:
      self.__id = id
    else:
      raise ValueError("ID inválido, tente novamente")
  def get_id(self):
    return self.__id
  def set_nome (self, nome):
    if nome != "":
      self.__nome = nome
    else:
      raise ValueError("Preencha todos os campos e digite seu nome, por favor")
  def get_nome(self):
    return self.__nome
  def set_fone(self, fone):
    if fone > 0:
      self.__fone = fone
    else:
      raise ValueError("Preencha todos os campos e digite um número para entrarmos em contato caso necessário, por favor")
  def get_fone(self):
    return self.__fone
  def set_nasc(self, nasc):
    try:
      # Converte a string de data no formato "dd/mm/aaaa" para um objeto date
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
  def __str__(self):
    return f"{self.get_id()} - {self.get_nome()} - {self.get_nasc()} - {self.get_fone()}"

# Persistência
class Pacientes:
  objetos = []  # atributo estático
  @classmethod
  def inserir(cls, obj):
    c = Paciente()
    cls.abrir()
    m = 0                     # cálculo do maior id utilizado - começa com 0
    for c in cls.objetos:     # percorre a lista de Pacientes - c é cada Paciente
      if c.get_id() > m:  m = c.get_id()   # compara o id de c com m (maior)
    c.set_id(int(m + 1)) 
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
      if c.get_id() == id: return c
    return None 
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
       c.set_nome(obj.get_nome())
       c.set_fone(obj.get_fone())
       c.set_nasc(obj.get_nasc())
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.objetos.remove(c)
      cls.salvar()   
  @classmethod
  def salvar(cls):  
    with open("Pacientes.json", mode = "w") as arquivo:   # write
        json.dump([{
                "id": p.get_id(),
                "nome": p.get_nome(),
                "nasc": p.get_nasc().strftime("%d/%m/%Y"),  # formata a data como string
                "fone": p.get_fone()
            } for p in cls.objetos], arquivo, indent=4)
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("Pacientes.json", mode = "r") as arquivo:   # read
        texto = json.load(arquivo)
        for obj in texto:
          c = Paciente(obj["id"], obj["nome"], obj["nasc"], obj["fone"])                     # dicionário
          cls.objetos.append(c)
    except FileNotFoundError:
      pass
    
# Visão
class UI:
  @staticmethod
  def menu():
    print("1 - Inserir Paciente, 2 - listar Pacientes, 3 - atualizar Paciente, 4 - excluir Paciente, 9 - fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 9: 
      op = UI.menu()
      if op == 1: UI.Paciente_inserir()
      if op == 2: UI.Paciente_listar()
      if op == 3: UI.Paciente_atualizar()
      if op == 4: UI.Paciente_excluir()

  @staticmethod
  def Paciente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    nasc = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    fone = int(input("Informe o fone: "))
    c = Paciente(0, nome, nasc, fone)
    Pacientes.inserir(c)

  @staticmethod
  def Paciente_listar():
    for c in Pacientes.listar():
      print(c)

  @staticmethod
  def Paciente_atualizar():
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser atualizado: "))
    nome = input("Informe o nome: ")
    nasc = datetime.date(input("Informe a sua data de nascimento (d/m/aaaa): "))
    fone = int(input("Informe o fone: "))
    c = Paciente(id, nome, nasc, fone)
    Pacientes.atualizar(c)

  @staticmethod
  def Paciente_excluir():
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser excluído: "))
    c = Paciente(id, "", "", "")
    Pacientes.excluir(c)

UI.main()    





  
