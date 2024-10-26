class Musica:
    nome = ''
    artista = ''
    duracao = float

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 3.55

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 1.83

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 2.34

musica_nova = Musica()
musica_nova.nome = 'Chá com bolacha'
musica_nova.artista = 'Café da tarde'
musica_nova.duracao = 3.36

print(f'{dir(musica_nova)})\n{vars(musica_nova)}')