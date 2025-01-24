import numpy as np
import pygame
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 800, 600
GRAVITY = np.array([0, 9.8])
TIMESTEP = 0.1

# Particle class
class Particle:
    def __init__(self, position, velocity):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

    def update(self):
        self.velocity += GRAVITY * TIMESTEP
        self.position += self.velocity * TIMESTEP

# FLIP simulation class
class FLIPSimulation:
    def __init__(self):
        self.particles = []

    def add_particle(self, position, velocity):
        self.particles.append(Particle(position, velocity))

    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(screen, (0, 0, 255), particle.position.astype(int), 3)

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("FLIP Fluid Simulation")
    clock = pygame.time.Clock()

    sim = FLIPSimulation()
    sim.add_particle([400, 300], [0, 0])

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                sim.add_particle(pygame.mouse.get_pos(), [0, 0])

            if keys[pygame.K_SPACE]:
                sim.add_particle(pygame.mouse.get_pos(), [0, 0])

        sim.update()

        screen.fill((255, 255, 255))
        sim.draw(screen)
        pygame.display.flip()
        

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()