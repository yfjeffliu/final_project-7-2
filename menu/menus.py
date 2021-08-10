import pygame
import os
from event.event_setting import MUTE_IMAGE,PLAY_IMAGE,SOUND_IMAGE,PAUSE_IMAGE
pygame.init()
MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "green_space.png")), (125, 65))
UPGRADE_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "upgrade.png")), (125, 65))
NOTIFY_IMAGE_SHOW = pygame.transform.scale(pygame.image.load(os.path.join("images1/notify_message", "message_shrink.png")),(180,18))
BUY_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "buy.png")), (125, 65))

ABILITY_MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "ability_menu_icon.png")), (100, 100))
ABILITY_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "special_skill.png")), (130, 120))
muse_button_image = pygame.transform.scale(MUTE_IMAGE, (34, 29))
music_button_image = pygame.transform.scale(SOUND_IMAGE, (34, 29))
continue_button_image = pygame.transform.scale(PLAY_IMAGE, (17, 24))
pause_button_image = pygame.transform.scale(PAUSE_IMAGE, (17, 24))

TV1_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "tower_tv1.png")), (40, 40))
TV2_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "tower_tv2.png")), (40, 40))
TV3_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "tower_tv3.png")), (40, 40))
class Button:
    def __init__(self, image, name: str, x: int, y: int):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    @property
    def response(self):
        return self.name


class Menu:
    def __init__(self, x: int, y: int,image = MENU_IMAGE):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x-100, y)
        self._buttons = []

    @property
    def buttons(self):
        return self._buttons



class BuildMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(BUY_BTN_IMAGE, "TV", self.rect.centerx, self.rect.centery)
        ]


class MainMenu:
    def __init__(self):
        self._buttons = [Button(muse_button_image, "mute", 753, 540),
                        Button(music_button_image, "music", 753, 540),
                         Button(continue_button_image, "continue", 720, 540),
                         Button(pause_button_image, "pause", 720, 540),
                         Button(NOTIFY_IMAGE_SHOW,"show_notify", 120, 560),
                         Button(ABILITY_MENU_IMAGE,"show_ability",935,510),
                         Button(ABILITY_BTN_IMAGE,"use_ability",935,385)]

    @property
    def buttons(self):
        return self._buttons
class UpgradeMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(UPGRADE_BTN_IMAGE, "upgrade", self.rect.centerx, self.rect.centery )
                         ]






