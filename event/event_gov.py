import pygame
import os
from color_settings import *
from event.event_setting import *
from event.data import gov_problem,gov_decision,gov_impact,gov_notify,gov_hint,gov_impact2,gov_notify2,gov_hint2
   
def set_gov(num:int):
    event_img = gov_problem[num-1]
    event_select_img = gov_decision[num-1]
    event_notify = gov_notify[num-1]
    event_hint = gov_hint[num-1]
    event_impact = gov_impact[num-1]
    event_notify2 = gov_notify2[num-1]
    event_hint2 = gov_hint2[num-1]
    event_impact2 = gov_impact2[num-1]
    event_question = an_question(0,event_img)
    event_decision = [an_decision(1,event_select_img[0],event_impact[0],event_notify[0],event_hint[0],event_impact2[0],event_notify2[0],event_hint2[0]),
                      an_decision(2,event_select_img[1],event_impact[1],event_notify[1],event_hint[1],event_impact2[1],event_notify2[1],event_hint2[1]),
                      an_decision(3,event_select_img[2],event_impact[2],event_notify[2],event_hint[2],event_impact2[2],event_notify2[2],event_hint2[2])]
    return an_event(event_question,event_decision[0],event_decision[1],event_decision[2])
    



