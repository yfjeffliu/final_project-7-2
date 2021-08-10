import pygame
from settings import *
from color_settings import *
import math
from event.event_setting import *

class GameView:
    def __init__(self,player):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont("comicsans", 30)
        self.player = player
    def draw_stage(self,stage):
        font = pygame.font.Font(FONT, 22)
        text = font.render('level  ' + str(stage), True, WHITE)
        text_rect = text.get_rect(midright=(300, 535))
        self.win.blit(text, text_rect)
    
    def draw_progress(self,num,total):
        self.win.blit(PROGRESS_LINE,(350,525))
        color = (210, 209, 209)
        pygame.draw.rect(self.win, color, pygame.Rect(350,525, 330*(total-num)/total,25))
        self.win.blit(pygame.transform.scale(ENEMY_IMAGE1[self.player], (40, 50)),((350+330*(total-num)/total)-20,525-30)) #icon
    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE[self.player], (0, 0))
    def draw_wait(self,wait):
        font = pygame.font.Font(FONT, 100)
        text = font.render(  str(wait), True, BROWNGRAY)
        text_rect = text.get_rect()
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        transparency = 120
        pygame.draw.circle(surface, (128, 128, 128, transparency), (512,300),200)
        self.win.blit(surface, (0, 0))
        text_rect.center = (512,300)
        self.win.blit(text, text_rect)

    def draw_notify(self,notify):
        notify_image =  pygame.transform.scale(notify,(180,160))
        notify_image_rect = notify_image.get_rect()
        notify_image_rect.center = (120,475)
        self.win.blit(notify_image,notify_image_rect)
        self.win.blit(notify_image,notify_image_rect)
    def draw_enemies(self, enemies):
        for en in enemies.get():
            self.win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def draw_towers(self, towers):
        # draw tower
        for tw in towers:
            self.win.blit(tw.image, tw.rect)

    def draw_range(self, selected_tower):
        # draw tower range
        if selected_tower is not None:
            tw = selected_tower
            # create a special surface that is able to render semi-transparent image
            surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
            transparency = 120
            pygame.draw.circle(surface, (128, 128, 128, transparency), tw.rect.center, tw.range)
            self.win.blit(surface, (0, 0))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_plots(self, plots):
        for pt in plots:
            self.win.blit(pt.image, pt.rect)

    def draw_money(self, money: int):
        money_menu_image = MONEY_MENU_IMAGE
        money_menu_image_rect = money_menu_image.get_rect()
        money_menu_image_rect.center = (815, 22)
        self.win.blit(money_menu_image, money_menu_image_rect.center)
        # draw money
        font = pygame.font.Font(FONT, 22)
        text = font.render('# ' + str(money), True, BROWNGRAY)
        text_rect = text.get_rect(midright=(960, 46))
        self.win.blit(text, text_rect)
    def draw_tower_money(self, tower_money: int):
        money_menu_image = TOWER_MONEY_MENU_IMAGE
        money_menu_image_rect = money_menu_image.get_rect()
        money_menu_image_rect.center = (615, 22)
        self.win.blit(money_menu_image, money_menu_image_rect.center)
        # draw tower money
        font = pygame.font.Font(FONT, 22)
        text = font.render('* ' + str(tower_money), True, BROWNGRAY)
        text_rect = text.get_rect(midright=(750, 46))
        self.win.blit(text, text_rect)
    
    def draw_main_menu(self,main_menu,mute,pause,ability):
        self.win.blit(main_menu[4].image,main_menu[4].rect)
        self.win.blit(main_menu[5].image,main_menu[5].rect)
        if ability:
            self.win.blit(main_menu[6].image,main_menu[6].rect)
        if mute:
            self.win.blit(main_menu[0].image,main_menu[0].rect)
        else:
            self.win.blit(main_menu[1].image,main_menu[1].rect)
        if pause:
            self.win.blit(main_menu[2].image,main_menu[2].rect)
        else:
            self.win.blit(main_menu[3].image,main_menu[3].rect)
        
    def draw_wave(self, wave: int):
        """(Q2.2)render the wave"""
        text = self.font.render(f"Wave: {wave}", True, (255, 255, 255))
        self.win.blit(text, (5, 15))

    def draw_hp(self, hp,max_hp):
        # draw_lives
        hp_image_rect = HEART_FULL_IMAGE.get_rect()
        for i in range(1,max_hp, 2):
            
            hp_image_rect.center = (20+i*20, 34)
            if i < hp:
                self.win.blit(HEART_FULL_IMAGE, hp_image_rect.center)
            elif i == hp:
                if hp == 0:
                    self.win.blit(HEART_FULL_IMAGE, hp_image_rect.center)
                else:
                    self.win.blit(HEART_HALF_IMAGE, hp_image_rect.center)
            else:
                self.win.blit(HEART_EMPTY_IMAGE, hp_image_rect.center)

