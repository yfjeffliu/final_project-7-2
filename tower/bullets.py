from color_settings import BLACK
import pygame
import os
import math
class BulletGroup():
    def __init__(self) -> None:
        self.bullet_list = []

        pass
    def generate(self,enemy,start,end):
        self.bullet_list.append(Bullet(enemy,start,end))
    def get(self):
        return self.bullet_list
    def update(self):
        for bullet in self.bullet_list:
            bullet.move(self)
    def remove(self,bullet):
        self.bullet_list.remove(bullet)
BULLET_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "newspaper.png")), (20, 20))
class Bullet():
    def __init__(self,enemy,start,end) -> None:
        self.enemy = enemy
        self.start = start
        self.end = end
        self.image = BULLET_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = start
        self.move_count = 0
        pass
    def move(self,bullet_list):
        x1,y1 = self.start
        x2,y2 = self.end
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / 10)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * 10 * self.move_count
        delta_y = unit_vector_y * 10 * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.enemy.health -= 1
            bullet_list.remove(self)