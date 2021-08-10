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
PATH = [[(17, 366), (77, 367), (132, 374), (181, 372), (248, 373), (313, 374),
        (362, 374), (420, 374), (433, 327), (443, 288), (457, 260), (512, 261),
        (552, 261), (605, 261), (651, 266), (699, 262), (748, 264), (775, 264), (805, 264)]]
PATH2 = [(5, 223), (39, 222), (70, 222), (115, 222), (163, 222), (208, 222),
         (228, 222), (227, 277), (271, 277), (310, 277), (350, 277), (406, 277),
         (464, 276), (467, 324), (465, 359), (467, 391), (467, 421), (524, 433),
         (562, 435), (601, 441), (648, 446), (698, 450), (735, 455), (786, 462),
         (786, 408), (787, 357), (788, 310), (789, 265), (790, 228),(791, 200),(792, 180),(793, 160),(794, 140),(795, 120)]             # wenchi append
# base
BASE = [pygame.Rect(805, 264, 195, 130)]

# image
BACKGROUND_IMAGE =  [pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "road1.png")),(WIN_WIDTH,WIN_HEIGHT))]
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images1/game_page/heart_empty.png"), (40, 40))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images1/game_page/heart_full.png"), (40, 40))
MONEY_MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "money_menu.png")), (160, 45))
HEART_FULL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "heart_full.png")), (28, 28))
HEART_HALF_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "heart_half.png")), (28, 28))
HEART_EMPTY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "heart_empty.png")), (28, 28))
FONT = "OtsutomeFont.ttf"     # wenchi append
NOTIFY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "notify.png")), (200, 150))
PROGRESS_LINE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "progress_line.png")), (330, 27))
ENEMY_IMAGE1 = [pygame.image.load(os.path.join("images1/game_page", "enemy_lem1.png"))]
TOWER_MONEY_MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "tower_money_menu.png")), (160, 45))

ALL_PASS_BG = pygame.transform.scale(pygame.image.load(os.path.join("images1/end_page", "ALL_PASS_BG_2.png")),(WIN_WIDTH,WIN_HEIGHT))
WIN_STAGE_BG = pygame.transform.scale(pygame.image.load(os.path.join("images1/end_page", "WIN_BG_2.png")),(WIN_WIDTH,WIN_HEIGHT))
FAIL_BG = pygame.transform.scale(pygame.image.load(os.path.join("images1/end_page", "LOSE_BG_2.png")),(WIN_WIDTH,WIN_HEIGHT))
ABILITY_BTN_IMAGE = [pygame.transform.scale(pygame.image.load(os.path.join("images1/game_page", "special_skill.png")), (95, 95))]
