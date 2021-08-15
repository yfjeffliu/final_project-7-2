from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from enemy.enemies import Enemy
    from tower.towers import Tower
import math
from abc import ABC, abstractmethod


def in_range(enemy:Enemy, tower:Tower):
    x1, y1 = enemy.rect.center
    x2, y2 = tower.rect.center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= tower.range:
        return True
    return False


"""
syntax: attack_strategy().attack(tower, enemy_group, cd_count)
It's something like you hire a "Strategist" to decide how to attack the enemy
You can add other ways of attack just by expand this module
"""


class AttackStrategy(ABC):
    """Abstract class of attack method"""
    @ abstractmethod
    def attack(self, enemies, tower, cd_count):
        return "Please implement this method"


class SingleAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies: list, tower:Tower, cd_count:int,bullet_list):
        for en in enemies:
            if in_range(en, tower):
                bullet_list.generate(en,tower,tower.rect.center,en.rect.center)
                cd_count = 0
                return cd_count
        return cd_count


class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies: list, tower:Tower, cd_count:int):
        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage
                cd_count = 0
        return cd_count


class Snipe(AttackStrategy):
    """eliminate an enemy all in once"""
    def attack(self, enemies: list, tower:Tower, cd_count:int):
        for en in enemies:
            if in_range(en, tower):
                en.health = 0
                cd_count = 0
                return cd_count
        return cd_count




