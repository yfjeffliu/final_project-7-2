from __future__ import annotations
from color_settings import BLUE
from event.event_gov import set_gov
import random
from event.player import *
from event.event_setting import *
from game.game import Game

dict_temp = {}
# 打开文本文件
file = open('dict.txt','r')
# 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
for line in file.readlines():
    line = line.strip()
    k = line.split(' ')[0]
    v = line.split(' ')[1]
    dict_temp[k] = v
# 依旧是关闭文件
file.close()

class Events:
    def __init__(self) :
        self.players=Players(dict_temp['gov'],dict_temp['wfh'])
        self.start_image = START_IMAGE
        self.start_round = START_ROUND
        self.using_player = 0
        self.player=0
        self.event = None
        self.event_list = [0,1,2,3,4,5]
        random.shuffle(self.event_list)
        self.num = 0
        self.buttons = [Buttons('mute',MUTE_IMAGE_BLACK,965,60),Buttons('sound',SOUND_IMAGE_BLACK,965,60),Buttons('play',PLAY_IMAGE_BLACK,920,60)
                        ,Buttons('pause',PAUSE_IMAGE_BLACK,920,60),Buttons('last_page',LAST_PAGE_IMAGE_BLACK,40,520)]
        self.buttons_white = [Buttons('mute',MUTE_IMAGE,965,60),Buttons('sound',SOUND_IMAGE,965,60),Buttons('play',PLAY_IMAGE,920,60)
                        ,Buttons('pause',PAUSE_IMAGE,920,60)]
        self.mute = False
        self.pause = False
        self.using_event=None
        #self.num=random.randint(1, 5)
        self.chosen = []
        self.next=0
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.notify = None
        self.last_page = False
        self.read = False
        pass
    def run(self):
        clock = pygame.time.Clock()
        self.win.blit(BACKGROUND_IMAGE_CHOOSE_PLAYER,(0,0))
        run = True
        while run:
            clock.tick(FPS)
            self.win.blit(BACKGROUND_IMAGE_CHOOSE_PLAYER,(0,0))
            if self.last_page: #上一頁
                return True
            if self.using_player == 0:
                run = self.choose_player()
                self.read = False
                self.using_event = None
                self.num = 0
                self.next = 0
            else:
                while not self.read:
                    quit,last = self.message_page_show()
                    if quit: #press X in message_page
                        return False
                    if last:    #last page
                        self.using_player = 0
                        self.last_page = False
                        run2 = False
                        break
                    else:   #next page
                        run2 = True
                game = Game(self.player)
                while run2 :
                    run2 = self.event_happen()
                    if self.next == 1:
                        print(self.chosen)
                        self.impact_model(game)
                        self.using_event=None
                        game.mute(self.mute)
                        quit=game.run()
                        if quit:
                            return False
                        elif game.all_pass:
                            quit = self.all_pass(game)
                            if quit:
                                return False
                            else:
                                run2 = False
                                run = True
                        elif game.keep_going:
                            
                            quit,exit = self.keep_going(game)
                            if quit:
                                return False
                            else:
                                run2 = True
                                if exit:
                                    self.using_player = 0
                                    run2 = False
                                    run = True
                        elif game.fail:
                            quit = self.game_fail(game)
                            if quit:
                                return False
                            else:
                                run2 = False
                                run = True
                    else:
                        run = False
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    return False
            pygame.display.update()
    def choose_player(self):
        run = True
        self.draw_choose_player()
        self.draw_player_frame()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.get_click_choose_player(x,y)
                self.button_clicked(x,y)
            if event.type == pygame.QUIT:
                    run = False
        return run
    def get_click_choose_player(self,x:int,y:int):
        
        if self.start_image_rect.collidepoint(x,y) and self.player != 0:
            self.using_player = self.player
        get = 0
        for player in self.players.player_btn:
            if player.buy_rect.collidepoint(x,y) and player.show_buy:
                player.unlock = True
                player.show_buy = False
                if int(dict_temp['money']) - player.cost >= 0:
                    dict_temp['money'] = str( int(dict_temp['money']) - player.cost)
                    dict_temp[player.name] = str(1)
                print(dict_temp)
                file = open('dict.txt', 'w') 
                for k,v in dict_temp.items():
	                file.write(str(k)+' '+str(v)+'\n')
                file.close()
            if (player.icon_image_rect.collidepoint(x,y) or player.word_image_rect.collidepoint(x,y)) and player.unlock:
                player.selected = True
                self.player = player.num
                get = player.num
            elif (player.icon_image_rect.collidepoint(x,y) or player.word_image_rect.collidepoint(x,y)) and not player.unlock:
                player.show_buy = True
            else :
                player.show_buy = False
                player.selected = False
            
        if get == 0:
            self.player = 0
    def button_clicked(self,x:int,y:int):
        button_name = ''
        for btn in self.buttons:
            if btn.image_rect.collidepoint(x,y):
                button_name = btn.name
        if button_name == 'sound':
            self.mute = not self.mute
        if button_name =='pause':
            self.pause = not self.pause
        if button_name == 'last_page':
            self.last_page = True
    def draw_choose_player(self):
        self.win.blit(BACKGROUND_IMAGE_CHOOSE_PLAYER,(0,0))
        #icon of player
        for player in self.players.player_btn:
            if player.unlock:
                self.win.blit(player.icon_image, player.icon_image_rect)     #show gov
            else:
                self.win.blit(player.lock_image, player.lock_image_rect)
            if player.show_buy:
                self.win.blit(player.buy,player.buy_rect)
            self.win.blit(player.word_image,player.word_image_rect)
        #start button
        self.start_image_rect = self.start_image.get_rect() 
        self.start_image_rect.center = (512,500)
        self.win.blit(self.start_image,self.start_image_rect)
        #back money
        bank_image = BACK_MENU
        self.win.blit(bank_image,(20,25))
        font = pygame.font.Font(FONT, 22)
        text = font.render('$ ' + str(dict_temp['money']), True, BROWNGRAY)
        self.win.blit(text, (130,75))
        
        self.draw_button_black()
    def message_page_show(self):
        self.win.blit(BACKGROUND_IMAGE_MESSAGE,(0,0))
        self.draw_button_black()
        read_button = Buttons('read',READ_BUTTON,555,490)
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                return True,False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.button_clicked(x,y)
                if read_button.image_rect.collidepoint(x,y):
                    self.read = True
                for btn in self.buttons:
                    if btn.image_rect.collidepoint(x,y):
                        button_name = btn.name
                        if button_name == 'last_page':
                            return False,True
        pygame.display.update()
        return False,False
    def draw_player_frame(self):
        for btn in self.players.player_btn:
            if btn.selected :
                pygame.draw.rect(self.win, BLACK, btn.frame, 10)
    def event_happen(self):
        run2 = True
        if self.using_event == None:
            self.set_using_event()
        self.events_draw()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.make_decision(x,y)
                self.button_clicked(x,y)
            if event.type == pygame.QUIT:
                    run2 = False
        return run2
    def events_draw(self):
        self.win.blit(BACKGROUND_IMAGE_EVENT,(0,0)) #色碼,X點、Y點、寬、高
        self.win.blit(self.using_event.question.image, self.using_event.question.image_rect)     #show choose player
        self.win.blit(self.using_event.select1.image, self.using_event.select1.image_rect)     #show gov
        self.win.blit(self.using_event.select2.image, self.using_event.select2.image_rect)     #show wfh
        self.win.blit(self.using_event.select3.image, self.using_event.select3.image_rect)     #show wfh
        self.start_round_rect = self.start_round.get_rect()
        self.start_round_rect.center = (365,520)
        self.win.blit(self.start_round,self.start_round_rect)
        self.draw_event_frame()
        level_image_rect = LEVEL1.get_rect()
        level_image_rect.center= (105,50)
        if self.num == 1:
            level_image = LEVEL1
        elif self.num == 2:
            level_image = LEVEL2
        elif self.num == 3:
            level_image = LEVEL3
        elif self.num == 4:
            level_image = LEVEL4
        elif self.num == 5:
            level_image = LEVEL5
        self.win.blit(level_image,level_image_rect)
        self.draw_button_white()
        pygame.display.update()
        pass
    def draw_event_frame(self):
        
        if self.using_event.select1.selected:
            pygame.draw.rect(self.win, BLACK, self.using_event.select1.frame, 10)
        if self.using_event.select2.selected:
            pygame.draw.rect(self.win, BLACK, self.using_event.select2.frame, 10)
        if self.using_event.select3.selected:
            pygame.draw.rect(self.win, BLACK, self.using_event.select3.frame, 10)
    def set_using_event(self):
        
        self.using_event=get_using_event(self.using_player,self.event_list[self.num])
        self.chosen = []
        self.num += 1
    def make_decision(self,x:int,y:int):
        if self.start_round_rect.collidepoint(x,y) and self.chosen != []:
            self.next=1
            self.using_event.select1.selected = False
            self.using_event.select2.selected = False
            self.using_event.select3.selected = False
            return
        if self.using_event.select1.image_rect.collidepoint(x,y):
            self.using_event.select1.selected = True
            self.using_event.select2.selected = False
            self.using_event.select3.selected = False
            self.notify = self.using_event.select1.notify
            self.chosen = self.using_event.select1.impact
        elif self.using_event.select2.image_rect.collidepoint(x,y):
            self.using_event.select1.selected = False
            self.using_event.select2.selected = True
            self.using_event.select3.selected = False
            self.notify = self.using_event.select2.notify
            self.chosen = self.using_event.select2.impact
        elif self.using_event.select3.image_rect.collidepoint(x,y):
            self.using_event.select1.selected = False
            self.using_event.select2.selected = False
            self.using_event.select3.selected = True
            self.chosen = self.using_event.select3.impact
            self.notify = self.using_event.select3.notify
        else:
            self.using_event.select1.selected = False
            self.using_event.select2.selected = False
            self.using_event.select3.selected = False
            self.chosen = []
    def draw_button_black(self):
        self.win.blit(self.buttons[4].image,self.buttons[4].image_rect)
        if self.mute:
            self.win.blit(self.buttons[0].image,self.buttons[0].image_rect)
            pygame.mixer.music.pause()
        else:
            self.win.blit(self.buttons[1].image,self.buttons[1].image_rect)
            pygame.mixer.music.unpause()
        if self.pause:
            self.win.blit(self.buttons[2].image,self.buttons[2].image_rect)
        else:
            self.win.blit(self.buttons[3].image,self.buttons[3].image_rect)
    def draw_button_white(self):
        if self.mute:
            self.win.blit(self.buttons_white[0].image,self.buttons_white[0].image_rect)
            pygame.mixer.music.pause()
        else:
            self.win.blit(self.buttons_white[1].image,self.buttons_white[1].image_rect)
            pygame.mixer.music.unpause()
        if self.pause:
            self.win.blit(self.buttons_white[2].image,self.buttons_white[2].image_rect)
        else:
            self.win.blit(self.buttons_white[3].image,self.buttons_white[3].image_rect)
    def impact_model(self,game:Game):
        money_get = random.randint(self.chosen[1],self.chosen[0])
        blood_get = random.randint(self.chosen[3],self.chosen[2])
        tower_upgrade = random.randint(self.chosen[5],self.chosen[4])+5
        game.game_model.money += money_get
        game.game_model.max_hp += blood_get
        game.game_model.hp += blood_get
        game.game_model.notify = self.notify
        game.game_model.tower_money += tower_upgrade
    def keep_going(self,game:Game):
        self.next = 0
        self.chosen = []
        percentage = [0,10,20,40,60,100]
        while True:
            #print('keep going',stage,money)
            self.win.blit(WIN_STAGE_BG,(0,0))
            text = '*' + str(game.game_model.tower_money) #塔防幣
            show_text(self.win,text,30,556,470)
            text = '#' + str(game.game_model.money) #金錢
            show_text(self.win,text,30,727,470)
            text = str(int(game.game_model.money * percentage[game.game_model.stage] / 100))
            show_text(self.win,text,50,500,350) #中間遊戲幣
            text = str( percentage[game.game_model.stage])+'%'
            show_text(self.win,text,30,248,95,(99, 78, 66))#左上目前%數
            text = str( percentage[game.game_model.stage+1])+'%'
            show_text(self.win,text,30,574,400,(64, 155, 163))#下一關%數
            draw_hp(self.win, game.game_model.hp,game.game_model.max_hp)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 86<x<86+186 and 379<y<379+55:
                        dict_temp['money'] = str(int(dict_temp['money'])+int(game.game_model.money * percentage[game.game_model.stage]))
                        file = open('dict.txt', 'w') 
                        for k,v in dict_temp.items():
	                        file.write(str(k)+' '+str(v)+'\n')
                        file.close()
                        return False,True
                    elif 750<x<750+186 and 379<y<379+55:
                        return False,False
                if event.type == pygame.QUIT:
                    return True,True
    def all_pass(self,game:Game):
        self.using_player=0
        while True:
            self.win.blit(ALL_PASS_BG,(0,0))
            text = '*' + str(game.game_model.tower_money)#塔防幣
            show_text(self.win,text,30,550,470)
            text = '#' + str(game.game_model.money)#金錢
            show_text(self.win,text,30,735,470)
            text = str(int(game.game_model.money))#中間遊戲幣
            show_text(self.win,text,50,500,329)
            draw_hp(self.win, game.game_model.hp,game.game_model.max_hp)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 750<x<750+186 and 364<y<364+55:
                        dict_temp['money'] = str(int(dict_temp['money'])+int(game.game_model.money))
                        file = open('dict.txt', 'w') 
                        for k,v in dict_temp.items():
	                        file.write(str(k)+' '+str(v)+'\n')
                        file.close()
                        return False              
    def game_fail(self,game:Game):
        self.using_player=0
        percentage = [0,10,20,40,60,100]
        while True:
            self.win.blit(FAIL_BG,(0,0))
            text = '*' + str(game.game_model.tower_money)#塔防幣
            show_text(self.win,text,30,550,470)
            text = '#' + str(game.game_model.money) #金錢
            show_text(self.win,text,30,735,470)
            text = str(int(game.game_model.money * percentage[game.game_model.stage-1] / 100))
            show_text(self.win,text,50,500,329)#中間遊戲幣
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 750<x<750+186 and 379<y<379+55:
                        dict_temp['money'] = str(int(dict_temp['money'])+int(game.game_model.money * percentage[game.game_model.stage-1]/100))
                        file = open('dict.txt', 'w') 
                        for k,v in dict_temp.items():
	                        file.write(str(k)+' '+str(v)+'\n')
                        file.close()
                        return False
                if event.type == pygame.QUIT:
                    return True
def get_using_event(player:int,num:int):
    if player == 1:
        return set_gov(num)
    pass
def show_text(win:pygame.Surface,text:str,size:int,x:int,y:int,color:tuple = BROWNGRAY):
    font = pygame.font.Font(FONT, size)
    text = font.render(text, True, color)
    
    win.blit(text, (x, y))
def draw_hp(win:pygame.Surface, hp:int,max_hp:int):
    # draw_lives
    hp_image_rect = HEART_FULL_IMAGE.get_rect()
    for i in range(1,max_hp, 2):
        hp_image_rect.center = (200+i*18, 480)
        if i < hp:
            win.blit(HEART_FULL_IMAGE, hp_image_rect.center)
        elif i == hp:
            if hp == 0:
                win.blit(HEART_FULL_IMAGE, hp_image_rect.center)
            else:
                win.blit(HEART_HALF_IMAGE, hp_image_rect.center)
        else:
            win.blit(HEART_EMPTY_IMAGE, hp_image_rect.center)
