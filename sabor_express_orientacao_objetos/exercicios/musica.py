class Musica:
    musicas = []

    def __init__(self, nome='', artista='', duracao=0.00):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica('Bohemian Rhapsody', 'Queen', 3.55)
musica2 = Musica('Imagine', 'John Lennon', 1.83)
musica3 = Musica('Shape of You', 'Ed Sheeran', 2.34)

#print(f'{dir(musica_nova)})\n{vars(musica_nova)}')
#print(musica1)
#print()
Musica.listar_musicas()