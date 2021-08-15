import pygame
import os

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600
#choose PLAYER size
CHOOSE_PLAYER_ICON_WIDTH = 100
CHOOSE_PLAYER_ICON_HEIGHT = 100
CHOOSE_PLAYER_WORD_WIDTH = 180
CHOOSE_PLAYER_WORD_HEIGHT = 45

CHOOSE_BTN_WIDTH = 800
CHOOSE_BTN_HEIGHT = 130

#heart size
HEART_WIDTH = 28
HEART_HEIGHT = 28

# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)
BROWNGRAY = (80, 61, 50)  # wenchi append
# enemy path
PATH1_gov = [(0, 420), (31, 418), (69, 415), (108, 412), (149, 413), (187, 415), (229, 414), 
        (265, 414), (299, 414), (333, 415), (369, 416), (407, 416), (446, 416), (479, 415), 
        (509, 412), (526, 394), (545, 359), (558, 321), (568, 286), (604, 270), (649, 273), 
        (689, 278), (726, 281), (760, 284), (792, 288), (823, 288), (858, 292), (891, 296), (926, 302)]
PATH2_gov = [(398, 5), (404, 32), (409, 64), (415, 96), (420, 128), (426, 158), (430, 190), (436, 222), 
        (441, 259), (477, 264), (516, 266), (557, 268), (594, 272), (637, 276), (677, 279), (721, 283),
         (760, 287), (794, 289), (824, 293), (860, 297), (890, 299)]             # wenchi append
PATH1 = [PATH1_gov]
PATH2 = [PATH2_gov]
# base
BASE = [pygame.Rect(835, 192, 150, 150)]
#tower position
TOWER_POSITION = [[(75,319),(221,466),(302,71),(374,317),(513,147),(607,418),(737,189)]]
# image
BACKGROUND_IMAGE =  [pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "road3.png")),(WIN_WIDTH,WIN_HEIGHT))]
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images1/game_page/heart_empty.png"), (40, 40))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images1/game_page/heart_full.png"), (40, 40))
MONEY_MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "money_menu.png")), (160, 45))
HEART_FULL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "heart_full.png")), (HEART_WIDTH, HEART_HEIGHT))
HEART_HALF_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "heart_half.png")), (HEART_WIDTH, HEART_HEIGHT))
HEART_EMPTY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "heart_empty.png")), (HEART_WIDTH, HEART_HEIGHT))
FONT = "OtsutomeFont.ttf"     # wenchi append
NOTIFY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "notify.png")), (200, 150))
PROGRESS_LINE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "progress_line.png")), (330, 27))
ENEMY_IMAGE1 = [pygame.image.load(os.path.join("images1/game_page", "enemy_lem1.png"))]
TOWER_MONEY_MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "tower_money_menu.png")), (160, 45))

ALL_PASS_BG = pygame.transform.scale(pygame.image.load(os.path.join("images1/end_page", "ALL_PASS_BG_2.png")),(WIN_WIDTH,WIN_HEIGHT))
WIN_STAGE_BG = pygame.transform.scale(pygame.image.load(os.path.join("images1/end_page", "WIN_BG_2.png")),(WIN_WIDTH,WIN_HEIGHT))
FAIL_BG = pygame.transform.scale(pygame.image.load(os.path.join("images1/end_page", "LOSE_BG_2.png")),(WIN_WIDTH,WIN_HEIGHT))
ABILITY_BTN_IMAGE = [pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "special_skill.png")), (95, 95))]
