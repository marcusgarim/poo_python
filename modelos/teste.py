
# class Musica:
#     nome = ''
#     artista = ''
#     duracao = int


class Musica:
    def __init__(self, nome: str, artista: str, duracao: int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.artista} ({self.duracao} min)'


musica1 = Musica('Bohemian Rhapsody', 'Queen', 6)
print(musica1)  # Saída: Bohemian Rhapsody - Queen (6 min)
