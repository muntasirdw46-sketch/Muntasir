import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ================= KUBUS 3D RGB =================
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

colors = (
    (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (1,0,1), (0,1,1)
)

def draw_cube():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

# ================= PERSEGI 2D =================
def draw_square():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 1)
    glVertex2f(-0.4, -0.4)
    glVertex2f( 0.4, -0.4)
    glVertex2f( 0.4,  0.4)
    glVertex2f(-0.4,  0.4)
    glEnd()

# ================= PROGRAM UTAMA =================
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Kubus 3D RGB & Persegi 2D Lengkap")

    gluPerspective(45, display[0]/display[1], 0.1, 50)

    # Transformasi Kubus
    cube_x, cube_y, cube_z = -2, 0, -8
    cube_rot = 0
    cube_scale = 1

    # Transformasi Persegi
    sq_x, sq_y = 2, 0
    sq_rot = 0
    sq_scale = 1
    shear_x = 0
    shear_y = 0
    reflect_x = 1
    reflect_y = 1

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # ===== KONTROL KUBUS 3D =====
        if keys[K_w]: cube_y += 0.05
        if keys[K_s]: cube_y -= 0.05
        if keys[K_a]: cube_x -= 0.05
        if keys[K_d]: cube_x += 0.05
        if keys[K_q]: cube_z += 0.05
        if keys[K_e]: cube_z -= 0.05
        if keys[K_z]: cube_rot += 1
        if keys[K_x]: cube_rot -= 1
        if keys[K_c]: cube_scale -= 0.01
        if keys[K_v]: cube_scale += 0.01

        # ===== KONTROL PERSEGI 2D (PANAH) =====
        if keys[K_UP]:    sq_y += 0.05
        if keys[K_DOWN]:  sq_y -= 0.05
        if keys[K_LEFT]:  sq_x -= 0.05
        if keys[K_RIGHT]: sq_x += 0.05
        if keys[K_u]: sq_rot += 1
        if keys[K_o]: sq_rot -= 1
        if keys[K_n]: sq_scale -= 0.01
        if keys[K_m]: sq_scale += 0.01
        if keys[K_1]: shear_x += 0.01
        if keys[K_2]: shear_y += 0.01
        if keys[K_3]: reflect_x = -1
        if keys[K_4]: reflect_y = -1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        # ===== RENDER KUBUS =====
        glPushMatrix()
        glTranslatef(cube_x, cube_y, cube_z)
        glRotatef(cube_rot, 1, 1, 1)
        glScalef(cube_scale, cube_scale, cube_scale)
        draw_cube()
        glPopMatrix()

        # ===== RENDER PERSEGI =====
        glPushMatrix()
        glTranslatef(sq_x, sq_y, -5)
        glRotatef(sq_rot, 0, 0, 1)
        glScalef(sq_scale * reflect_x, sq_scale * reflect_y, 1)

        shear_matrix = [
            1, shear_y, 0, 0,
            shear_x, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]
        glMultMatrixf(shear_matrix)

        draw_square()
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
