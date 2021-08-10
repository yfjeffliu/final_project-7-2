import pygame


# controller
class GameControl:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0
                       }
        self.request = None  # response of user input
        self.keep_going = False
        self.fail = False
        self.wait = 5
        self.count = 0
    def update_model(self):
        """update the model and the view here"""
        if self.model.hp == 0:
            self.fail = True
        if self.model.enemies_empty() and self.wait <0:
            self.wait = 5
            self.keep_going = True
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.call_menu()
        self.model.towers_attack()
        self.model.enemies_advance()
        
    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    self.events["keyboard key"] = pygame.K_n
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_hp(self.model.hp,self.model.max_hp)
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_towers(self.model.towers)
        self.view.draw_range(self.model.selected_tower)
        self.view.draw_plots(self.model.plots)
        self.view.draw_money(self.model.money)
        self.view.draw_tower_money(self.model.tower_money)
        #self.view.draw_wave(self.model.wave)
        self.view.draw_main_menu(self.model.get_main_menu(),self.model.mute,self.model.pause,self.model.show_ability)
        
        if self.model.show_notify:
            self.view.draw_notify(self.model.notify)
        self.view.draw_stage(self.model.stage)
        

        """(Q2) Controller request View to render something"""
        if self.model.menu is not None:
            self.view.draw_menu(self.model.menu)
        if self.wait > 0:
            self.view.draw_progress(10,10)
            self.view.draw_wait(self.wait)
            if self.count >= 30:
                self.wait -=1
                self.count = 0
            else:
                self.count += 1
        elif self.wait == 0:
            self.view.draw_wait(self.wait)
            self.model.enemies.add(10,self.model.stage)
            self.model.stage += 1
            self.view.draw_progress(self.model.get_progress,10)
            self.wait -= 1
        else:
            self.view.draw_progress(self.model.get_progress,10)
            pass
    @property
    def quit_game(self):
        return self.events["game quit"]
    


