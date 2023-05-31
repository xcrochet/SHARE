import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import urllib.request
from PIL import Image

def load_texture(url):
    with urllib.request.urlopen(url) as response:
        image = Image.open(response)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image_data = image.convert("RGBA").tobytes()
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.size[0], image.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        glBindTexture(GL_TEXTURE_2D, 0)
        return texture_id

def draw_sphere(radius, lats, longs):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glEnable(GL_TEXTURE_2D)
    for i in range(0, lats):
        lat0 = np.pi * (-0.5 + float(i) / lats)
        z0 = np.sin(lat0)
        zr0 = np.cos(lat0)
        
        lat1 = np.pi * (-0.5 + float(i+1) / lats)
        z1 = np.sin(lat1)
        zr1 = np.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(0, longs + 1):
            lng = 2 * np.pi * float(j) / longs
            x = np.cos(lng)
            y = np.sin(lng)

            glTexCoord2f(float(j) / longs, float(i) / lats)
            glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)

            glTexCoord2f(float(j) / longs, float(i+1) / lats)
            glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
        glEnd()
    glDisable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, 0)

def main():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    global texture_id
    texture_url = "2560px-Large_World_Topo_Map_2.png"
    texture_id = load_texture("./2560px-Large_World_Topo_Map_2.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_sphere(2, 50, 50)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
