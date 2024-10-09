import pygame
import os

# Inicializa o pygame
pygame.mixer.init()

# Lista as músicas no diretório
def listar_musicas(diretorio):
    return [f for f in os.listdir(diretorio) if f.endswith('.mp3')]

# Reproduz a música escolhida
def reproduzir_musica(musica):
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    print(f'Reproduzindo: {musica}')

def main():
    diretorio_musicas = 'music'
    musicas = listar_musicas(diretorio_musicas)
    
    print("Músicas disponíveis:")
    for idx, musica in enumerate(musicas):
        print(f"{idx + 1}: {musica}")
    
    escolha = int(input("Escolha o número da música para reproduzir: ")) - 1
    
    if 0 <= escolha < len(musicas):
        reproduzir_musica(os.path.join(diretorio_musicas, musicas[escolha]))
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()

