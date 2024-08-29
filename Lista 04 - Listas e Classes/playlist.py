from datetime import timedelta

class Musica:
    def __init__(self):
        self.__titulo = ""
        self.__artista = ""
        self.__album = ""
        self.__duracao = timedelta()  # Inicializa com duração zero

    def set_titulo(self, titulo):
        if titulo != "":
            self.__titulo = titulo
        else:
            raise ValueError("Título não deve ser vazio")

    def set_artista(self, artista):
        if artista != "":
            self.__artista = artista
        else:
            raise ValueError("Artista não deve ser vazio")

    def set_album(self, album):
        if album != "":
            self.__album = album
        else:
            raise ValueError("Álbum não deve ser vazio")

    def set_duracao(self, duracao):
        if duracao > timedelta(0):
            self.__duracao = duracao
        else:
            raise ValueError("Digite uma duração válida e maior que zero")

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album

    def get_duracao(self):
        return self.__duracao

    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album} - {self.__duracao}"

class Playlist:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []
        if nome == "":
            raise ValueError("Informe um nome para a Playlist")

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            raise ValueError("Digite um nome para sua playlist")

    def set_descricao(self, descricao):
        if descricao != "":
            self.__descricao = descricao
        else:
            raise ValueError("Descrição não deve ser vazia")

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def inserir(self, m):  # insere um objeto música em um objeto playlist
        if isinstance(m, Musica):
            self.__musicas.append(m)
        else:
            raise ValueError("O item inserido não é uma música")

    def listar(self):
        return self.__musicas[:]

    def tempo_total(self):
        total = timedelta()
        for musica in self.__musicas:
            total += musica.get_duracao()
        return total

    def __str__(self):
        return f"Playlist {self.__nome} - {self.__descricao} tem {len(self.__musicas)} música(s) - Tempo Total: {self.tempo_total()}"

class UI:
    @staticmethod
    def menu():
        print("1-Nova Playlist, 2-Inserir Música, 3-Listar Músicas, 4-Info, 5-Tempo Total, 6-Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():
        print("Bem-vindo(a) ao IF Música")
        op = 0
        p = None
        while op != 6:
            op = UI.menu()
            if op == 1:
                p = UI.nova_playlist()
            elif op == 2:
                UI.inserir_musica(p)
            elif op == 3:
                UI.listar_musica(p)
            elif op == 4:
                UI.info(p)
            elif op == 5:
                UI.tempo_total(p)
        print("Bye")

    @staticmethod
    def nova_playlist():
        nome = input("Informe o nome da playlist: ")
        desc = input("Informe uma descrição para a playlist: ")
        p = Playlist(nome, desc)
        return p

    @staticmethod
    def inserir_musica(p):
        titulo = input("Informe o título da música: ")
        artista = input("Informe o artista: ")
        album = input("Informe o álbum: ")
        duracao = input("Informe a duração da música (formato HH:MM:SS): ")
        h, m, s = map(int, duracao.split(':'))
        d = timedelta(hours=h, minutes=m, seconds=s)
        m = Musica()
        m.set_titulo(titulo)
        m.set_artista(artista)
        m.set_album(album)
        m.set_duracao(d)
        p.inserir(m)
    @staticmethod
    def listar_musica(p):
        print("Músicas inseridas na Playlist")
        for m in p.listar():
            print(m)
    @staticmethod
    def info(p):
        print(p)
    @staticmethod
    def tempo_total(p):
        print(f"Tempo total da Playlist '{p.get_nome()}': {p.tempo_total()}")

UI.main()
