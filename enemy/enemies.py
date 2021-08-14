from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.model import GameModel
import pygame
import math
import os
from settings import PATH, BASE
from color_settings import *
import random
pygame.init()
ENEMY_IMAGE1 = [pygame.image.load(os.path.join("images1/game_page", "enemy_lem1.png"))]
ENEMY_IMAGE2 = [pygame.image.load(os.path.join("images1/game_page", "enemy_lem2.png"))]
ENEMY_IMAGE3 = [pygame.image.load(os.path.join("images1/game_page", "enemy_lem3.png"))]

class Enemy:
    def __init__(self,player:int,stage:int):
        self.path = PATH[player]
        self.path_index = 0
        self.move_count = 0
        self.slow_count = 0
        self.slow_max = 90
        self.slow = False
        # 根據關卡(變數stage=1~5 datatype:int)產生怪物 設定image、血量
        num = random.randint(1, 5*(stage+1))
        if num <= 5:
            self.image = pygame.transform.scale(ENEMY_IMAGE1[player], (40, 50))
            self.health = 10
            self.max_health = 10
            self.stride = 1
            self.level = 1
        elif (num % 2 == 0) & (num <= 17):
            self.image = pygame.transform.scale(ENEMY_IMAGE2[player], (40, 50))
            self.health = 20
            self.max_health = 20
            self.stride = 2
            self.level = 2
        else:
            self.image = pygame.transform.scale(ENEMY_IMAGE3[player], (40, 50))
            self.health = 30
            self.max_health = 30
            self.stride = 3
            self.level = 3
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]

        
    def move(self):
        if self.slow_count < self.slow_max:
            self.slow_count += 1
            if self.slow:
                self.slow = False
                return
            else:
                self.slow = True
        
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]
            
    def clicked(self,x,y):
        if self.rect.collidepoint(x,y):
            return True
        else:
            return False

class EnemyGroup:
    def __init__(self,player:int):
        self.campaign_count = 0
        self.campaign_max_count = 60   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []
        self.count = 0
        self.count2 = 0
        self.player = player
    def advance(self, model:GameModel):
        """Bonus.2"""
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.health <= 0:
                self.retreat(en)
            # delete the object when it reach the base
            if BASE[self.player].collidepoint(en.rect.centerx, en.rect.centery):
                model.hp -= 1
                self.retreat(en)


    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
            self.campaign_max_count = random.randint(30,90)
            self.campaign_progress()
        else:
            self.campaign_count += 1

    def campaign_progress(self):
        self.count2 += 1

    def add(self, num:int,stage:int):
        self.count = num
        self.count2 = 0
        """Generate the enemies for next wave"""
        if self.is_empty():
            self.__reserved_members = [Enemy(self.player,stage) for _ in range(num)]

    def get(self):
        """Get the enemy list"""
        return self.__expedition

    def is_empty(self):
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.__expedition else True

    def retreat(self, enemy:Enemy):
        """Remove the enemy from the expedition"""
        self.count -= 1
        self.__expedition.remove(enemy)





