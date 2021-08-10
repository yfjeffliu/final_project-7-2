import pygame
import os
from color_settings import *
from event.event_setting import *
from event.data import gov_problem,gov_decision,gov_impact
   
def set_gov(num:int):
    event_img = gov_problem[num-1]
    event_select_img = gov_decision[num-1]
    event_impact = gov_impact[num-1]
    event_question = an_question(0,event_img)
    event_decision = [an_decision(1,event_select_img[0],event_impact[0],event_select_img[3]),an_decision(2,event_select_img[1],event_impact[1],event_select_img[4]),an_decision(3,event_select_img[2],event_impact[2],event_select_img[5])]
    return an_event(event_question,event_decision[0],event_decision[1],event_decision[2])
    



