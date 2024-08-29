# CRUD de NPaciente - cadastro de NPaciente - lista
# C - Create - insere um Paciente no cadastro
# R - Read - lê os NPaciente cadastrados
# U - Update - atualiza os dados de um Paciente
# D - Delete - remove um Paciente do cadastro
from datetime import datetime, date
# vamos precisar desses dois para a data de nascimento e operações extras
import json
# vamos precisar dele para criar o banco de dados

# Modelo
class Paciente:
  def __init__(self, id: int, nome: str, fone: int, nasc: date):
    # Privando os atributos do código com "__", portanto não poderão ser acessados diretamente
    self.__id = 0
    self.__nome = "nome"
    self.__fone = 0
    self.__nasc = None
    self.set_id(id)
    self.set_nome(nome)
    self.set_fone(fone)
    self.set_nasc(nasc)
  def set_id(self, id: int):
    # Setando o id e garantindo que além de inteiro ele seja maior do que 0.
    if id > 0:
      self.__id = id
    else:
      raise ValueError("ID inválido, tente novamente")
  def get_id(self):
    return self.__id
  def set_nome (self, n: str):
    # Setando o nome como string e garantindo que ela não esteja vazia
    if n != "":
      self.__nome = n
    else:
      raise ValueError("Preencha todos os campos e digite seu nome, por favor")
  def get_nome(self):
    return self.__nome
  def set_fone(self, fone: int):
    # Setando o telefone e garantindo que ele seja maior do que 0
    # OBS: dependendo do seu nível de paciência daria para garantir que ele também tivesse um tamanho mínimo usando:
    # 
    if fone > 0:
      self.__fone = fone
    else:
      raise ValueError("Preencha todos os campos e digite um número para entrarmos em contato caso necessário, por favor")
  def get_fone(self):
    return self.__fone
  def set_nasc(self, nasc: str):
    # Setando a data de nacimento e garantindo que ela esteja no formato adequado para poder fazer a operação de garantir 
    # ser menor do que a atual
    try:
      # Converte a string de data no formato "dd/mm/aaaa" para um objeto date
      data_nascimento = datetime.strptime(nasc, "%d/%m/%Y").date()
      data_hoje = date.today()
      # Esta função é para obter a data de hoje e permitir a comparação abaixo, já que você não pdoeria registrar 
      # um paciente que ainda não nasceu
      if data_nascimento < data_hoje:
          self.__nasc = data_nascimento
      else:
        raise ValueError("Insira uma data válida e anterior ao dia atual")
    except ValueError:
            raise ValueError("Formato de data inválido. Use o formato dd/mm/aaaa")
    # Explicando o "try" e "except": 
    #   - Inicialmente ele vai analizar a parte do "try", conferir se está vindo como uma string para então ser convertido
    #     como "date" graças a função: 'datetime.strptime(nasc, "%d/%m/%Y").date()'. Depois ele compara se a data de naci-
    #     mento é anterior ao dia atual, caso contrário será mostrado ao usuário: "Insira uma data válida e anterior ao 
    #     dia atual"
    #   - Então, se houver qualquer falha relaciona a conversão das datas por não estarem no medo "dd/mm/aaaa" ou por dias
    #     impossíveis estarem sendo digitados ele irá para o bloco "except" e mostrará ao usuário a seguinte mensagem:
    #     "Formato de data inválido. Use o formato dd/mm/aaaa".
    # OBS:
    #   * Se ainda for necessário um exemplo de dia impossível: "31/02/2023", fevereiro tem no máximo 29 dias.
    #   * O uso de "try" e "except" foi preferível para evitar cair em inúmeras verificações para cada forma de ValueError
    #     primeiramente precisando verificar se o formato estava certo, mesmo utilizando o:
    #     'datetime.strptime(nasc, "%d/%m/%Y").date()'
    #     Podendo ser da seguinte maneira:
    #            # Verificar se o formato básico está correto
    #            if len(nasc.split('/')) == 3:
    #               dia, mes, ano = nasc.split('/')
    #               # Verifica se todos os componentes da data são números
    #               if dia.isdigit() and mes.isdigit() and ano.isdigit():
    #     E ainda seria necessário filtrar dias impossíveis, portanto a primeira parte do split possuísse um número maior
    #     do que 31 cairia em um outro else e ainda teríamos que conferir os dias de fevereiro de forma diferente verifi-
    #     cando se é ou não um ano bissexto para ter 29 dias, caso contrário o erro não cairia da forma de desejamos
  def get_nasc(self):
    return self.__nasc
  def to_json(self):
        dic = {}                                          # Cria um dicionário vazio
        dic["id"] = self.__id                             # Adiciona o atributo 'id' ao dicionário
        dic["nome"] = self.__nome                         # Adiciona o atributo 'nome' ao dicionário
        # Lembrando que ele estava como date para poder ser feita a comparação de ser anterior ao dia atual lá em cima
        dic["nasc"] = self.__nasc.strftime('%d/%m/%Y')    # Converte a data de nascimento para string e adiciona ao dicionário
        dic["fone"] = self.__fone                         # Adiciona o atributo 'fone' ao dicionário

        return dic                                        # Retorna o dicionário
        # É válido lembrar que as chaves desse dicionário são os nomes dentro do colchete ao lado de dic e os valores os
        # respectivos "self.__" encapsulados
  def __str__(self):
    return f"{self.get_id()} - {self.get_nome()} - {self.get_fone()} - {self.__nasc.strftime('%d/%m/%Y')} "
    # É o que vai aparecer no listar para o usuário, deixe essa parte tão bonita quando preferir

# Classe de Persistência de Objetos
class NPaciente:
  objetos = []  # atributo estático
  @classmethod
  def inserir(cls, obj):
    # método Inserir: insere um objeto na lista;
    # Lembrando: métodos são aqueles relacionados a uma única classe, já que não poderiam ser utilizados para nadas que 
    # não fossem elas ou pertencentes a elas.
    cls.abrir()
    # Essa função ainda vai ser criada lá embaixo, então eu vou explicar melhor por lá.

    # Uma recomendação pessoal: se você ainda não se acostumou com objetos para se referir a algo da vida real, use o nome
    # do que você está abstraindo mesmo. Exemplo: aqui você poderia usar 'cls.paciente' desde que mudasse lá embaxio tam-
    # bém, no 'cls.objetos.append(obj)' e colocasse: 'cls.paciente.append(obj)'
    max_id = max((c.get_id() for c in cls.objetos), default=0)
    # Ele compara todos os id já criados, pega o maior deles com a função "max()", então ele filtra apenas o id com o 
    # "c.get_id()" e o "for c in cls.objetos" é para pegar cada paciente dentro da classe. Caso ela esteja vazia é aí on-
    # de o "default=0" opera, ele assume o max como 0.
    obj.set_id(max_id + 1)
    # Aqui ele seta o id e vai conferir lá em cima se ele é realmente maior do que 0, o que deveria acontecer já que, gra-
    # ças ao default quando vazia a lista é 0, então 0 + 1 = 1 e depois ele vai pegando o maior e somando um. É tipo o la-
    # ço x+=1 para classes
    cls.objetos.append(obj)
    # É para adicionar um objeto a classe quando excutar a função inserir lá embaixo. Em resumo, ele adiciona mais um pa-
    # ciente a lista de pacientes
    cls.salvar()
    # Essa função ainda vai ser criada lá embaixo, então eu vou explicar melhor por lá.
  @classmethod
  def listar(cls):
    # Método Listar: retorna os objetos na lista;
    cls.abrir()
    # Essa função ainda vai ser criada lá embaixo, então eu vou explicar melhor por lá.
    return cls.objetos
    # Ele vai retornar cada objeto adicionado a classe separadamente, não usamos um "for c in cls.objetos" por ele ser mais
    # recomendado quando seu desejo é filtrar ou manipular algo imediatamente. Exemplo: filtrar os ids como fizemos.

    # Além de que o usuário não teria acesso a essa classe, então nos ainda vamos utilizar ao parecido na UI para que ele
    # realmente tenha acesso a essa função.
  @classmethod
  def listar_id(cls, id):
    # método Listar_Id: retornar o objeto com um determinado id;
    cls.abrir()
    # Essa função ainda vai ser criada lá embaixo, então eu vou explicar melhor por lá.
    for c in cls.objetos:
      if c.get_id() == id: 
        return c
    # Ele confere o id, em linhas gerais, o "for" é para procurar por cada paciente/objeto dentro da classe. o c.get_id() é
    # para filtrar e pegar somente o id dentro das inúmeras classes. Então ele tá comparando todos os objetos com o "for",
    # procurando o certo com a comparação, já que o "id" ali em cima vai ser fornecido pelo usuário para as ações de:
    #     - Atualizar -> o Uptade do CRUD
    #     - Excluir -> o Delete do CRUD
    # Por fim, ele retorna o OBJETO inteiro, a ficha INTEIRA do paciente.
    return None 
  @classmethod
  def atualizar(cls, obj):
    # Método Atualizar: atualizar os dados de um objeto;
    c = cls.listar_id(obj.get_id()) 
    # Como expliquei, ele excuta a função de cima para filtrar em qual paciente/objeto ele vai alterar e não a todos
    if c != None:
        # Se realmente houver um paciente com esse id ele excuta a função abaixo, já que na função de cima se ele não
        # encontrar nada, ele fica "sem retorno", por falta de um termo melhor
        c.set_nome(obj.get_nome())
        c.set_fone(obj.get_fone())
        c.set_nasc(obj.get_nasc().strftime('%d/%m/%Y')) #convertendo para string novamente para então salvar sem erros
    cls.salvar()
    # Essa função ainda vai ser criada lá embaixo, então eu vou explicar melhor por lá.
  @classmethod
  def excluir(cls, obj):
    # Método Excluir, para excluir um objeto da lista;
    c = cls.listar_id(obj.get_id())  
    # Como expliquei, ele excuta a função de cima para filtrar em qual paciente/objeto ele vai alterar e não a todos
    if c is not None:
        # Um outro método para fazer a mesma coisa do atualizar, coloquei os dois para ter uma maior variabilidade
        cls.objetos.remove(c)
        # remove o OBJETO, a ficha INTEIRA do paciente.
        cls.salvar()
        # Essa função ainda vai ser criada lá embaixo, então eu vou explicar melhor por lá.
  @classmethod
  def abrir(cls):
    # Método Abrir: recuperar a lista de objetos de um arquivo JSON;
    cls.objetos = []
    # Isso é para criar uma lista vazia e/ou limpa-a para que o python possa pegar somente as informações já salvas no 
    # JSON e tranferir para essa lista antes de enviar novamente com as alterações que o usuário quiser.

    # é tipo uma parada intermediária
    try: 
      with open("NPaciente.json", mode = "r" ) as arquivo:   # r = read
        # Basicamente é dizendo para abrir o aquivo "NPaciente.json" em um modo onde ele não pode escrever, somente ler 
        # informações
        texto = json.load(arquivo)
        # lê o conteúdo do arquivo JSON e converte em um objeto python com o "json.load"
        for obj in texto:
          # Percorre cada itém que a gente transformou em objeto python, lembrando que cada um é um dicionário do paciente
          c = Paciente(obj["id"], obj["nome"], obj["fone"], obj["nasc"])
          cls.objetos.append(c)                     # dicionário
          # Basicamente nas duas linhas de cima ele vai pegar o dicionário, transformar em algo que possa ser adicionado
          # na lsita criada lá no início para poder excutar as operações que o usuário quiser
    except FileNotFoundError:
      # Leia-se: se não encontrar o arquivo, pula essa parte
      pass
  @classmethod
  def salvar(cls):  
    # Método Salvar: salvar a lista de objetos em um arquivo JSON;
    with open("NPaciente.json", mode = "w") as arquivo:   # w = write
        # Basicamente é dizendo para abrir o aquivo "NPaciente.json" em um modo onde ele pode escrever nele automáticamente
        # O with é para que ele feche após excutar a operação e diminua a quantidade de erros vindo de fechar um código com
        # um documentoa aberto
        
        # Portanto você pode ler essa linha assim: você pode escrever no arquivo "NPaciente.json", mas depois você fecha 
        # quando terminar para garantir que ele não seja corrompido ou algo ruim aconteça e a gente perca tudo

        json.dump(cls.objetos, arquivo, default = Paciente.to_json) 
        #  - json.dump -> converte um objeto python para uma string JSON e escreve no arquivo automaticamente.
        #                OBS: json.dumps é diferente ele converte em string e você manualmente quem escreveria no arquivo
        #  - cls.objetos -> é a lista de objetos que ele vai converter em string e escrever no arquivo automaticamente.
        #                OBS: no nosso caso, ele vai escrever e sobrescrever cada vez que algum dos métodos com o 
        #                     "cls.salvar" forem executados e toda a lista de objetos que por eles passou ou está passando
        #  - default = Paciente.to_json -> em resumo se tiver algo que não poderia ser covnertido diretamente em string 
        #                JSON ele vai pegar e passar toda lista de objetos a ser adicionada pelo método "to_json" da classe
        #                paciente. Onde ele transforma em um dicionário primeiro colocando as chaves e tudo bonitinho para
        #                então ele voltar pra cá e tranformar na string JSON. Isso se fez necessário quando descobrimos que
        #                ele não é capaz de converter datas de nascimento automáticamente e escrever. Então, basicamente, 
        #                tivemos o dobro de trabalho lá em cima criando um método para para transformar um data em STR.
        #                OBS: não é somente para isso, mas é o jeito mais fácil de pensar.
        #  - "as arquivo" e "arquivo" -> são basicamente para nomear o "("NPaciente.json", mode = "w")", ou seja, o arquivo
        #                "NPaciente.json" no modo onde o nosso sisteminha possa abrir e escrever nele:
        #                o modo writer/escritor
        #                Tornar isso mais fácil e não ficar repetindo toda hora.

        # Portanto, em linhas gerais, leia-se: escreve essas fichas de pacientes nesse arquivo aqui onde eu deixei você como
        # ADM para mim? Se tiver algo em um idioma que você não compreende usa essa meu tradutor aqui.
  @classmethod
  def Aniversariantes(cls, mes):  
    # Método Aniversariante: retornar a lista de pacientes que aniversariam no mês informado.
    return [p for p in cls.objetos if p.get_nasc().month == mes]
    # Aqui não tem muito segredo, ele pega cada paciente, procura pelo mes de nascimento regristrado com o 
    # "p.get_nasc().month" e compara com o mes fornecido, aqueles que baterem ele retorna. Lembrando que o 'p.get_nasc()'
    # só filtra a data de nascimento dentro da classe e o que pega o mês é o ".month"

    # Isso também poderia ser feito assim:
    # aniversariantes = []
    # for p in cls.objetos:
    #   if p.get_nasc().month == mes:
    #       aniversariantes.append(p)
    # return aniversariantes

    


# Visão
class UI:
  @staticmethod
  def menu():
    # Método Menu: 
    # - informar as operações que o usuário pode realizar no sistema
    # - listar, inserir, atualizar, excluir pacientes e listar os aniversariantes do mês
    # - Além da operação de finalizar a aplicação.
    print("MENU DO PACIENTE \n1 - Inserir Paciente \n2 - listar Pacientes \n3 - atualizar Paciente \n4 - excluir Paciente \n5 - Listar Aniversariantes do Mês")
    print("0 - Fim")
    # Imagine isso acima como uma telinha informativa
    return int(input("Informe uma opção: "))
    # E esse o teclado ou menu interativo
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

    # id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    nasc = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    fone = int(input("Informe o fone: "))
    c = Paciente(0, nome, fone, nasc)
    # Passe pela verificação da primeira classe, se estão todos corretamente setados e retorna da forma correta
    NPaciente.inserir(c)
    # Apena insere a objeto inteiro na classe de lista dos pacientes "NPaciente"
  @staticmethod
  def Paciente_listar():
    # Método Listar: listar os pacientes cadastrados;
    for c in NPaciente.listar():
      # Leia-se para capa paciente em "NPaciente" liste-o conforme o retorno que você configurou na __str__ já que o 
      # método listar da ui está listando os objetos, portanto indo direto para a __str__
      print(c)
      # Mostre o objeto completo
  @staticmethod
  def Paciente_atualizar():
    # Método Atualizar: atualizar os dados de um paciente;
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser atualizado: "))
    # pega o id para poder entrar naquela comparação configurada no "listar_id" e devolver que objeto/paciente devemos
    # modificar
    nome = input("Informe o nome: ")
    nasc = input("Informe a sua data de nascimento (dd/mm/aaaa): ")  # Mudança aqui
    fone = int(input("Informe o fone: "))
    c = Paciente(id, nome, fone, nasc)
    # Passa as novas informações pela classe modelo para ver se tudo está de acordo
    # Percebeu que o id não é 0 agora? Pois é, porque precisamos buscar com um com o id que o usuário vai fornecer, então
    # se colocarmos como 0 autormaticamente ele não vai funcionar graças ao filtro do encapsulamente e segundo que ele 
    # mudaria sempre o mesmo objeto/paciente.

    # Se ficar muito difícil de compreender, mude o nome do "listar_id" para "procurar_paciente" ou "Localizar_paciente"
    NPaciente.atualizar(c)
    # Coloca no método atualizar fora da UI, onde ele vai pegar essa informações e salvar no banco de dados para que quan-
    # do você volte ainda estejam lá as informações. Afinal, quando você parar o código o que foi salvo na lista de paci-
    # entes se perderia

    # Por fim ele atualiza o OBJETO/FICHA DO PACIENTE inteiro, segundo o que foi digitado
  @staticmethod
  def Paciente_excluir():
    # Método Excluir: excluir um paciente;
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser excluído: "))
    paciente = NPaciente.listar_id(id)
    # Usamos NPaciente.listar_id(id) para encontrar o paciente com o id especificado.
    if paciente:
        # Leia-se: se tu encontrar um paciente com o id fornecido, pode alterar aí
        NPaciente.excluir(paciente)
        # Se o paciente for encontrado, o método NPaciente.excluir(paciente) é chamado para remover o paciente da lista 
        # e salvar a alteração.
        print("Paciente excluído com sucesso.")
    else:
        # Leia-se: se tu não encontrar faz isso daqui:
        print("Paciente não encontrado.")
    pass
    # Não coloquei essa parte bonitinha no de cima por preguiça, mas tem como sim
  @staticmethod
  def Paciente_aniversariantes():
    # Método Aniversariantes: listar os aniversariantes do mês informado pelo usuário;
    mes = int(input("Informe o mês para listar aniversariantes (1-12): "))
    aniversariantes = NPaciente.Aniversariantes(mes)
    # Isso é pra conferir se tem algum paciente registrado no mês fornecido.
    # Caso tiver ele executa o bloco if e printa todos que tiverem
    if aniversariantes:
        for c in aniversariantes:
            print(c)

    # Caso não tenha ele executa o bloco else e printa a frase abaixo
    else:
        print("Nenhum paciente encontrado para o mês informado.")

UI.main()    




# Em resumo: não encapsulem e privem coisas, só vai te dar dor de cabeça
