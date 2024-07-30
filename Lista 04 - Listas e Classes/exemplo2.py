class Musica:
    def __init__(self) -> None:
        self.__titulo = ""
        self._artista = ""
        self.__album = ""
    def set__titulo(self, titulo):
        if titulo != "":
            self.__dict__titulo = titulo
        else:
            raise ValueError("Título não deve ser vazio")
    def set__artista(self, artista):
        if artista != "":
            self.__artista = artista
        else:
            raise ValueError("Artista não deve ser vazio")
    def set__album(self, album):
        if album != "":
            self.__album = album
        else:
            raise ValueError("Álbum não deve ser vazio")
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    def __str__(self) -> str:
        return f"{self.__titulo} - {self.__artista} - {self.__album}"