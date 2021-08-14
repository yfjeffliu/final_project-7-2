from typing import Tuple
import pygame
import os

from pygame.mixer import pause
from tower.towers import Tower, Vacancy
from tower.bullets import BulletGroup
from enemy.enemies import EnemyGroup
from menu.menus import Menu, UpgradeMenu, BuildMenu, MainMenu
from game.user_request import RequestSubject, TowerFactory,  TowerDeveloper, TowerKiller,  Music,Show_Hide_Notify,Ability,Play
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE


class GameModel:
    def __init__(self,player:int):
        self.player = player
        # data
        self.bg_image = pygame.transform.scale(BACKGROUND_IMAGE[0], (WIN_WIDTH, WIN_HEIGHT))
        self.__towers = []
        self.__enemies = EnemyGroup(self.player)
        self.__menu = None
        self.__main_menu = MainMenu()
        plot = [[Vacancy(283, 307), Vacancy(500, 200),Vacancy(600, 330)]]
        self.__plots = plot[player]
        self.__bullet = BulletGroup()
        # selected item
        self.selected_plot = None
        self.selected_tower = None
        self.touched_tower = None
        self.selected_button = None
        # apply observer pattern
        self.subject = RequestSubject(self)
        self.play_req = Play(self.subject)
        self.seller = TowerKiller()
        self.developer = TowerDeveloper(self.subject)
        self.factory = TowerFactory(self.subject)

        #self.muse = Muse(self.subject)
        self.music = Music(self.subject)
        self.ctrl_notify = Show_Hide_Notify(self.subject)
        self.ability = Ability(self.subject)
        #
        self.wave = 0
        self.money = 0
        self.tower_money = 0
        self.max_hp = 10
        self.hp = self.max_hp
        self.sound = pygame.mixer.Sound(os.path.join("sound", "sound.flac"))
        self.notify = None
        self.show_notify = True
        self.mute = False
        self.pause = False
        self.stage = 0
        self.show_ability = False
        
        
    def user_request(self, user_request: str):
        """ add tower, sell tower, upgrade tower"""
        self.subject.notify(user_request)

    def get_request(self, events: dict) -> str:
        """get keyboard response or button response"""
        # initial
        self.selected_button = None
        # key event
        if events["keyboard key"] is not None:
            return "start new wave"
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)

            if self.selected_button is not None:
                return self.selected_button.response
            return "nothing"
        
        x,y = events["mouse move"]
        self.touch_tower(x,y)
            
        return "nothing"
    def touch_tower(self,x,y):
        for tw in self.__towers:
            if tw.touched(x, y):
                self.touched_tower = tw
                return
        self.touched_tower = None
    def select(self, mouse_x: int, mouse_y: int) -> None:
        """change the state of whether the items are selected"""
        # if the item is clicked, select the item
        for tw in self.__towers:
            if tw.clicked(mouse_x, mouse_y):
                self.selected_tower = tw
                self.selected_plot = None
                return
        for pt in self.__plots:
            if pt.clicked(mouse_x, mouse_y):
                self.selected_tower = None
                self.selected_plot = pt
                return
        for en in self.enemies.get():
            if en.clicked(mouse_x,mouse_y):
                en.slow_count = 0
                print('slow')
                break
        # if the button is clicked, get the button response.
        # and keep selecting the tower/plot.
        if self.__menu is not None:
            for btn in self.__menu.buttons:
                if btn.clicked(mouse_x, mouse_y):
                    self.selected_button = btn
            if self.selected_button is None:
                self.selected_tower = None
                self.selected_plot = None
        # menu btn
        for btn in self.__main_menu.buttons:
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn

    def call_menu(self):
        if self.selected_tower is not None:
            x, y = self.selected_tower.rect.center
            self.__menu = UpgradeMenu(x, y)
        elif self.selected_plot is not None:
            x, y = self.selected_plot.rect.center
            self.__menu = BuildMenu(x, y)
        else:
            self.__menu = None
    def get_main_menu(self):
        return self.__main_menu.buttons
        

    def towers_attack(self,bullet_list):
        for tw in self.__towers:
            tw.attack(self.__enemies.get(),bullet_list)

    def enemies_advance(self):
        self.__enemies.advance(self)
    def enemies_empty(self):
        return True if self.enemies.is_empty() else False
    def bullets_update(self):
        self.bullets.update()
    @property
    def enemies(self):
        return self.__enemies
    @property
    def bullets(self):
        return self.__bullet
    @property
    def towers(self):
        return self.__towers

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, new_menu:Menu):
        self.__menu = new_menu

    @property
    def plots(self):
        return self.__plots

    @property
    def get_progress(self):
        return self.__enemies.count2
    











