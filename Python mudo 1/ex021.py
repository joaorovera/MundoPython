import pygame
pygame.init()
pygame.mixer.music.load('abc.mp3')
pygame.mixer.music.play()


while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Espera por 10 ms para evitar alta utilização da CPU

print("Reprodução de música concluída.")