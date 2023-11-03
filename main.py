import pygame
# from gpiozero import Button
from pygame.locals import *

# Configurez ici le numéro de pin GPIO auquel votre bouton est connecté
# button_pin = 17
# button = Button(button_pin)

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Modèle 3D avec Pygame et GPIO')

# Couleurs
black = (0, 0, 0)
red = (255, 0, 0)

# Fonction pour afficher un modèle simple (ici un rectangle)
def draw_model():
    screen.fill(black)  # Nettoyer l'écran en le remplissant de noir
    pygame.draw.rect(screen, red, (width//4, height//4, width//2, height//2))  # Dessiner un rectangle rouge
    pygame.display.flip()  # Mettre à jour l'affichage

# Fonction appelée lorsque le bouton est pressé
# def on_button_press():
#     print("Bouton pressé ! Affichage du modèle...")
#     draw_model()

# Attacher l'événement de pression du bouton à la fonction on_button_press
# button.when_pressed = on_button_press

# Boucle principale
draw_model()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()