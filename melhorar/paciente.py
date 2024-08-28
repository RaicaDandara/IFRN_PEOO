# CRUD de NPaciente - cadastro de NPaciente - lista
# C - Create - insere um Paciente no cadastro
# R - Read - lê os NPaciente cadastrados
# U - Update - atualiza os dados de um Paciente
# D - Delete - remove um Paciente do cadastro
from datetime import datetime, date
import json

# Modelo
class Paciente:
  def __init__(self, id, nome, fone, nasc):
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
  def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["nome"] = self.__nome
        dic["nasc"] = self.__nasc.strftime('%d/%m/%Y')
        dic["fone"] = self.__fone

        return dic
  def __str__(self):
    return f"{self.get_id()} - {self.get_nome()} - {self.get_fone()} - {self.__nasc.strftime('%d/%m/%Y')} "

# Classe de Persistência de Objetos
class NPaciente:
  objetos = []  # atributo estático
  @classmethod
  def inserir(cls, obj):
    # método Inserir: insere um objeto na lista;
    cls.abrir()
    max_id = max((c.get_id() for c in cls.objetos), default=0)
    obj.set_id(max_id + 1)
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    # Método Listar: retorna os objetos na lista;
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    # método Listar_Id: retornar o objeto com um determinado id;
    cls.abrir()
    for c in cls.objetos:
      if c.get_id() == id: return c
    return None 
  @classmethod
  def atualizar(cls, obj):
    # Método Atualizar: atualizar os dados de um objeto;
    c = cls.listar_id(obj.get_id())  # Corrigido para usar get_id()
    if c != None:
        c.set_nome(obj.get_nome())
        c.set_fone(obj.get_fone())
        c.set_nasc(obj.get_nasc().strftime('%d/%m/%Y'))
    cls.salvar()
  @classmethod
  def excluir(cls, obj):
    # Método Excluir, para excluir um objeto da lista;
    c = cls.listar_id(obj.get_id())  # Corrigido para usar get_id()
    if c is not None:
        cls.objetos.remove(c)
        cls.salvar()
  @classmethod
  def abrir(cls):
    # Método Abrir: recuperar a lista de objetos de um arquivo JSON;
    cls.objetos = []
    try: 
      with open("NPaciente.json", mode = "r") as arquivo:   # read
        texto = json.load(arquivo)
        for obj in texto:
          c = Paciente(obj["id"], obj["nome"], obj["fone"], obj["nasc"])
          cls.objetos.append(c)                     # dicionário
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):  
    # Método Salvar: salvar a lista de objetos em um arquivo JSON;
    with open("NPaciente.json", mode = "w") as arquivo:   # write
        json.dump(cls.objetos, arquivo, default = Paciente.to_json) 
  @classmethod
  def Aniversariantes(cls, mes):  
    # Método Aniversariante: retornar a lista de pacientes que aniversariam no mês informado.
    return [p for p in cls.objetos if p.get_nasc().month == mes]
    


# Visão
class UI:
  @staticmethod
  def menu():
    # Método Menu: informar as operações que o usuário pode realizar no sistema: listar, inserir, atualizar e excluir pacientes; listar os aniversariantes do mês, além da operação de finalizar a aplicação;
    print("MENU DO PACIENTE \n1 - Inserir Paciente \n2 - listar Pacientes \n3 - atualizar Paciente \n4 - excluir Paciente \n5 - Listar Aniversariantes do Mês")
    print("0 - Fim")
    return int(input("Informe uma opção: "))
  @staticmethod
  def main():
    # Método Main: manter um laço de iteração com o usuário até uma opção de finalização ser escolhida;
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
    # Método Inserir: ler os dados de um paciente e inserir na respectiva lista;
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    nasc = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    fone = int(input("Informe o fone: "))
    c = Paciente(0, nome, fone, nasc)
    NPaciente.inserir(c)
    datastr = input("Informe a data e o horário no formato dd/mm/aaaa hh:mm: ")
    data = datetime.strptime(datastr, "%d/%m/%Y %H:%M")
    c = Horario(0, data)
    Horarios.inserir(c)
  @staticmethod
  def Paciente_listar():
    # Método Listar: listar os pacientes cadastrados;
    for c in NPaciente.listar():
      print(c)
  @staticmethod
  def Paciente_atualizar():
    # Método Atualizar: atualizar os dados de um paciente;
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser atualizado: "))
    nome = input("Informe o nome: ")
    nasc = input("Informe a sua data de nascimento (dd/mm/aaaa): ")  # Mudança aqui
    fone = int(input("Informe o fone: "))
    c = Paciente(id, nome, fone, nasc)
    NPaciente.atualizar(c)
  @staticmethod
  def Paciente_excluir():
    # Método Excluir: excluir um paciente;
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser excluído: "))
    paciente = NPaciente.listar_id(id)
    # Usamos NPaciente.listar_id(id) para encontrar o paciente com o id especificado.
    if paciente:
        NPaciente.excluir(paciente)
        # Se o paciente for encontrado, o método NPaciente.excluir(paciente) é chamado para remover o paciente da lista e salvar a alteração.
        print("Paciente excluído com sucesso.")
    else:
        print("Paciente não encontrado.")
    pass
  @staticmethod
  def Paciente_aniversariantes():
    # Método Aniversariantes: listar os aniversariantes do mês informado pelo usuário;
    mes = int(input("Informe o mês para listar aniversariantes (1-12): "))
    aniversariantes = NPaciente.Aniversariantes(mes)
    if aniversariantes:
        for c in aniversariantes:
            print(c)
    else:
        print("Nenhum paciente encontrado para o mês informado.")

UI.main()    
