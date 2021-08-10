from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.model import GameModel
import pygame
from abc import ABC,abstractmethod
from tower.towers import Tower, Vacancy

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""

class Observer(ABC):
    def __init__(self,subject:RequestSubject) -> None:
        subject.register(self)
    @abstractmethod
    def update(self,user_request:str,model:GameModel):
        raise 'Implement this method'
class RequestSubject:
    def __init__(self, model:GameModel):
        self.__observers = []
        self.model = model

    def register(self, observer:Observer):
        self.__observers.append(observer)

    def notify(self, user_request:str):
        for o in self.__observers:
            o.update(user_request, self.model)



class Show_Hide_Notify:
    def __init__(self,subject) -> None:
        subject.register(self)
    def update(self, user_request: str, model):
        if user_request == 'show_notify':
            model.show_notify = not model.show_notify
            
class TowerKiller:
    def __init__(self,):
        pass

    def update(self,model:GameModel):
        for tw in model.towers:
            x,y = tw.rect.center
            model.plots.append(Vacancy(x, y))
            model.towers.remove(tw)
        
        model.selected_tower = None
            


class TowerDeveloper:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model:GameModel):
        if user_request == "upgrade" and model.selected_tower.level < 5:
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data
            
            if model.tower_money >= 1:
                model.tower_money -= 1
                model.selected_tower.level += 1
            pass



class TowerFactory:
    def __init__(self, subject:RequestSubject):
        subject.register(self)
        self.tower_name = ["TV"]

    def update(self, user_request: str, model:GameModel):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                x, y = model.selected_plot.rect.center
                tower_dict = {"TV": Tower.TV(x, y,model.player)}
                new_tower = tower_dict[user_request]
                if model.tower_money > 1:
                    model.tower_money -= 2
                    model.towers.append(new_tower)
                    model.plots.remove(model.selected_plot)
                    model.selected_plot = None


class Music:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model:GameModel):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.mute = not model.mute
            #model.sound.play()


class Muse:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model:GameModel):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.mute = not model.mute
            #model.sound.play()

class Ability:
    def __init__(self,subject:RequestSubject):
        subject.register(self)
    def update(self, user_request: str, model:GameModel):
        if user_request == 'use_ability' and model.show_ability:
            print('use ability')
        if user_request == 'show_ability':
            print('show abiltiy')
            model.show_ability = not model.show_ability
        
        

class Play:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model:GameModel):
        """music on"""
        if user_request == "pause":
            pygame.mixer.music.unpause()
            model.pause = not model.pause
            #model.sound.play()
class Pause:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model:GameModel):
        """music on"""
        if user_request == "continue":
            pygame.mixer.music.unpause()
            model.pause = not model.pause
            #model.sound.play()