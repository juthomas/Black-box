import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def calculate_normal(v1, v2, v3):
    a = np.array(v2) - np.array(v1)
    b = np.array(v3) - np.array(v1)
    return np.cross(a, b)

# Charger votre modèle .obj ici
def load_obj(filename):
    vertices = []
    faces = []

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('v '):
                _, x, y, z = line.split()
                vertices.append((float(x), float(y), float(z)))
            elif line.startswith('f '):
                _, *vertex_indices = line.split()
                face = [int(vertex_index.split('/')[0]) - 1 for vertex_index in vertex_indices]
                faces.append(face)

    return vertices, faces

# def draw_model(vertices, faces):
#     glBegin(GL_TRIANGLES)
#     for face in faces:
#         for vertex_index in face:
#             glVertex3fv(vertices[vertex_index])
#     glEnd()

def draw_model(vertices, faces):
    glBegin(GL_TRIANGLES)
    for i, face in enumerate(faces):
        # Définir une couleur différente pour chaque face
        glColor3f(i % 3 * 0.5, (i + 1) % 3 * 0.5, (i + 2) % 3 * 0.5)
        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])
    glEnd()

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, -1, 0])  # Lumière directionnelle
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])  # Couleur blanche

def main():
    pivot_x, pivot_y, pivot_z = [-2.0, 5.0, 0.0]  # Exemple de point de pivot
    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(25, (display[0] / display[1]), 0.1, 50)
    # glTranslatef(2.0, -7.0, -26)
        # Positionnez la caméra plus bas et regardez vers le haut
    glTranslatef(2.0, -5.0, -26)  # Déplacez la caméra plus bas
    glRotatef(30, 1, 0, 0)  # Inclinez la caméra pour regarder vers le haut
    glTranslatef(pivot_x, pivot_y, pivot_z)
    glRotatef(90, 0, 0, 1)
    glRotatef(90, 0, 1, 0)
    glTranslatef(-pivot_x, -pivot_y, -pivot_z)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    vertices, faces = load_obj('VoitureSTLv4.obj')
    # setup_lighting()

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 18)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glTranslatef(pivot_x, pivot_y, pivot_z)
        glRotatef(2, 0, 0, 1)
        glTranslatef(-pivot_x, -pivot_y, -pivot_z)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Dessiner le modèle ici
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_model(vertices, faces)
        # draw_text("Votre texte ici", font, 10, 20)
        glColor3f(0, 1, 0)  # Rouge = 0, Vert = 0, Bleu = 1
        glWindowPos2d(10, display[1] - 20)
        for char in "JUJU Mobile":
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()