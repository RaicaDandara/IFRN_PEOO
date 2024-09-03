import json
from datetime import datetime, date, timedelta

class Avaliacao:
  def __init__(self, id: int, d: str, l: str, dt: str):
    self.id = id
    self.disciplina = d
    self.local = l
    self.data = dt
  def __str__(self):
    return f"{self.id} - {self.disciplina} - {self.local} - {self.data.strftime('%d/%m/%Y')}"
  def to_json(self):
    dic = {}
    dic["id"] = self.id
    dic["disciplina"] = self.disciplina
    dic["local"] = self.local
    dic["data"] = datetime.strftime(self.data, "%d/%m/%Y")

    return(dic)

class Avaliacoes:
  Avaliacoes = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for p in cls.Avaliacoes:
      if p.id > m: m = p.id
    obj.id = m + 1
    cls.Avaliacoes.append(obj)
    cls.salvar()
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for p in cls.Avaliacoes:
      if p.id == id: return p
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    h = cls.listar_id(obj.id)
    if h != None:
      h.disciplina = obj.disciplina
      h.local = obj.local
      h.data = obj.data
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    p = cls.listar_id(obj.id)
    if p != None:
      cls.Avaliacoes.remove(p)
    cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.Avaliacoes
  @classmethod
  def salvar(cls):
    with open("Avaliacoes.json", mode="w") as arquivo:
      json.dump(cls.Avaliacoes, arquivo, default = Avaliacao.to_json)
  @classmethod
  def abrir(cls):
    cls.Avaliacoes = []
    try:
      with open("Avaliacoes.json", mode="r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:   
          p = Avaliacao(obj["id"], obj["disciplina"], obj["local"], datetime.strptime(obj["data"], "%d/%m/%Y"))
          cls.Avaliacoes.append(p)
    except FileNotFoundError:
      pass
  def ProximosDias(cls, obj):
    cls.abrir()
    Avalicao_ProximosDias = []
    hoje = datetime.now()
    tempo = timedelta(days = obj)
    intervalodetempo = hoje + tempo
    for p in cls.Avaliacoes:
        if p.data <= intervalodetempo and p.data >= hoje:
            Avalicao_ProximosDias.append(p)
        else:
            pass
    if len(Avalicao_ProximosDias) != 0:
        pass
    else: 
        Avalicao_ProximosDias.append("Não há avaliação nos próximos dias. ")
    return Avalicao_ProximosDias

class UI:
  @staticmethod
  def menu():
    print("1 - Inserir Avaliação, 2 - Listar Avaliação, 3 - atualizar Avaliação, 4 - excluir Avaliação, 5 - Avaliações Futuras, 6 - fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 6:
      op = UI.menu()
      if op == 1: UI.Inserir()
      if op == 2: UI.Listar()
      if op == 3: UI.Atualizar()
      if op == 4: UI.Excluir()
      if op == 5: UI.ProximosDias()

  @staticmethod
  def Inserir():
    #id = int(input("Informe o id: "))
    disciplina = input("Informe o disciplina: ")
    local = input("Informe o local: ")
    data = input("Informe a data de dataimento (dd/mm/aaaa): ")
    data = datetime.strptime(data, "%d/%m/%Y")
    p = Avaliacao(0, disciplina, local, data)
    Avaliacoes.inserir(p)

  @staticmethod
  def Listar():  
    for p in Avaliacoes.listar():
      print(p)

  @staticmethod
  def Atualizar():
    UI.Listar()
    id = int(input("Informe o id do Avaliacao a ser atualizado: "))
    disciplina = input("Informe o novo disciplina: ")
    local = input("Informe o novo local: ")
    data = input("Informe a nova data de dataimento (dd/mm/aaaa): ")
    data = datetime.strptime(data, "%d/%m/%Y")
    p = Avaliacao(id, disciplina, local, data)
    Avaliacoes.atualizar(p)

  @staticmethod
  def Excluir():
    UI.Listar()
    id = int(input("Informe o id do Avaliacao a ser excluído: "))
    p = Avaliacao(id, "", "", "")
    Avaliacoes.excluir(p)
  @staticmethod
  def ProximosDias():
    dias = int(input("Até quando deseja filtrar: "))
    a = Avaliacoes.ProximosDias(Avaliacoes, dias)
    for x in a:
      print(x)

UI.main()
