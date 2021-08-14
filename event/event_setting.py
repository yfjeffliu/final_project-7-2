from __future__ import annotations
import pygame
import os
from settings import *
import pygame.freetype
from event.data import FIRST_NOTIFY
class an_event:
    def __init__(self,question:an_question,select1:an_decision,select2:an_decision,select3:an_decision) -> None:
        self.question = question
        self.select1 = select1
        self.select2 = select2
        self.select3 = select3
        pass


class an_decision():
    def __init__(self, num:int,image:pygame.Surface,  impact:list,notify_image:pygame.Surface,first_notify = FIRST_NOTIFY) -> None:
        self.impact = impact
        self.notify =notify_image
        if image.get_height()>350:
            self.image = pygame.transform.scale(image, (424, 84))
            self.first_notify = pygame.transform.scale(first_notify, (300, 84))
            self.frame = pygame.Rect(165 + 200 - 212, 200 + (num - 1) * 95 + 25 - 40, 424, 84)
        else:
            self.image = pygame.transform.scale(image, (424, 53))
            self.first_notify = pygame.transform.scale(first_notify, (300, 53))
            self.frame = pygame.Rect(165 + 200 - 212, 200 + (num - 1) * 95 + 25 - 26, 424, 53)
        self.first_notify_rect = self.first_notify.get_rect()
        self.first_notify_rect.center = (165+250, 200 + (num - 1) * 95 + 25)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (165+200, 200+(num-1)*95+25)

        self.selected = None
        self.move_count = 0
        self.move_max = 15
        
class an_question:
    def __init__(self,num:int,image:pygame.Surface) -> None:
        if image.get_height()>300:
            self.image = pygame.transform.scale(image, (round(((80 / image.get_height()) * image.get_width())), 80))
        else:
            self.image = pygame.transform.scale(image, (round(((38 / image.get_height()) * image.get_width())), 38))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (380, 134)
        pass

class Buttons:
    def __init__(self,name:str,image:pygame.Surface,x:int,y:int) -> None:
        self.name = name
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.center = x,y
    def is_clicked(self,x:int,y:int):
        return True if self.image_rect.collidepoint(x,y)  else False
#images
BACKGROUND_IMAGE_CHOOSE_PLAYER = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "choose_character.png")), (WIN_WIDTH, WIN_HEIGHT))
BACKGROUND_IMAGE_EVENT = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "make_a_choice.png")), (WIN_WIDTH, WIN_HEIGHT))
START_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "yes.png")), (150, 60))
START_ROUND = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "start_round.png")), (200, 60))
LEVEL1 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level1.png")), (140, 40))
LEVEL2 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level2.png")), (140, 40))
LEVEL3 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level3.png")), (140, 40))
LEVEL4 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level4.png")), (140, 40))
LEVEL5 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level5.png")), (140, 40))
MUTE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "mute.png")), (30, 30))
SOUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "sound.png")), (30, 30))
PAUSE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "pause.png")), (25, 25))
PLAY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "play.png")), (25, 25))
LAST_PAGE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "return.png")), (25, 25))
MUTE_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "mute_black.png")), (30, 30))
SOUND_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "sound_black.png")), (30, 30))
PAUSE_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "pause_black.png")), (25, 25))
PLAY_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "play_black.png")), (25, 25))
LAST_PAGE_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "return_black.png")), (25, 25))
BACK_MENU = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "bank_menu.png")), (235, 100))
NEXT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "btn_next_page.png")), (20, 20))
BACKGROUND_IMAGE_MESSAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "message_page.png")), (WIN_WIDTH, WIN_HEIGHT))
