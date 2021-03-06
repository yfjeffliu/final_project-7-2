import pygame
import os
wfh_problem = [pygame.image.load(os.path.join("event/wfh_img", "Q1.png")),
                pygame.image.load(os.path.join("event/wfh_img", "Q2.png")),
                pygame.image.load(os.path.join("event/wfh_img", "Q3.png")),
                pygame.image.load(os.path.join("event/wfh_img", "Q4.png")),
                pygame.image.load(os.path.join("event/wfh_img", "Q5.png")),
                pygame.image.load(os.path.join("event/wfh_img", "Q6.png"))]

wfh_decision_problem1 = [pygame.image.load(os.path.join("event/wfh_img", "Q1_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_C.png"))]
wfh_notify_problem1 = [ pygame.image.load(os.path.join("event/wfh_img", "M1_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M1_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M1_C.png"))]
wfh_notify2_problem1 = [ pygame.image.load(os.path.join("event/wfh_img", "M1_A2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M1_B2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M1_C2.png"))]
wfh_hint_problem1 =    [pygame.image.load(os.path.join("event/wfh_img", "Q1_A_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_B_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_C_HINT.png"))]
wfh_text_problem1 = [pygame.image.load(os.path.join("event/wfh_img", "Q1_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_C.png"))]
wfh_message1_problem1 =    [pygame.image.load(os.path.join("event/wfh_img", "Q1_A_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_B_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_C_hint1.png"))]
wfh_message2_problem1 =    [pygame.image.load(os.path.join("event/wfh_img", "Q1_A_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_B_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q1_C_hint2.png"))]
wfh_impact_problem1 = [[-10,-15,4,2,5,3],[20,10,-1,-3,0,0],[-5,-15,3,1,5,3]]
wfh_impact2_problem1 = [[0,0,-1,-3,0,0],[-5,-10,0,0,-1,-2],[-5,-10,0,0,0,0]]

wfh_decision_problem2 = [pygame.image.load(os.path.join("event/wfh_img", "Q2_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_C.png"))]
wfh_notify_problem2 = [ pygame.image.load(os.path.join("event/wfh_img", "M2_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M2_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M2_C.png"))]
wfh_notify2_problem2 = [ pygame.image.load(os.path.join("event/wfh_img", "M2_A2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M2_B2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M2_C2.png"))]
wfh_hint_problem2 =   [ pygame.image.load(os.path.join("event/wfh_img", "Q2_A_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_B_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_C_HINT.png"))]
wfh_text_problem2 = [pygame.image.load(os.path.join("event/wfh_img", "Q2_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_C.png"))]
wfh_message1_problem2 =   [ pygame.image.load(os.path.join("event/wfh_img", "Q2_A_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_B_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_C_hint1.png"))]
wfh_message2_problem2 =   [ pygame.image.load(os.path.join("event/wfh_img", "Q2_A_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_B_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q2_C_hint2.png"))]
wfh_impact_problem2 = [[-5,-10,0,0,0,0],[0,0,4,2,0,0], [0,0,0,0,5,3]]
wfh_impact2_problem2 = [[0,0,0,0,5,3],[0,0,0,0,4,2], [0,0,-2,-5,0,0]]

wfh_decision_problem3 = [pygame.image.load(os.path.join("event/wfh_img", "Q3_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_C.png"))]
wfh_notify_problem3 = [ pygame.image.load(os.path.join("event/wfh_img", "M3_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M3_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M3_C.png"))]
wfh_notify2_problem3 = [ pygame.image.load(os.path.join("event/wfh_img", "M3_A2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M3_B2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M3_C2.png"))]
wfh_hint_problem3 = [   pygame.image.load(os.path.join("event/wfh_img", "Q3_A_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_B_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_C_HINT.png"))]
wfh_text_problem3 = [pygame.image.load(os.path.join("event/wfh_img", "Q3_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_C.png"))]
wfh_message1_problem3 = [   pygame.image.load(os.path.join("event/wfh_img", "Q3_A_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_B_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_C_hint1.png"))]
wfh_message2_problem3 = [   pygame.image.load(os.path.join("event/wfh_img", "Q3_A_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_B_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q3_C_hint2.png"))]
wfh_impact_problem3 = [[-5,-10,4,2,0,0],[20,10,0,0,0,0], [0,0,0,0,-1,-3]]
wfh_impact2_problem3 = [[0,0,0,0,4,2],[0,0,-1,-3,0,0], [15,5,3,1,0,0]]

wfh_decision_problem4 = [pygame.image.load(os.path.join("event/wfh_img", "Q4_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_C.png"))]
wfh_notify_problem4 = [ pygame.image.load(os.path.join("event/wfh_img", "M4_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M4_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M4_C.png"))]
wfh_notify2_problem4 = [ pygame.image.load(os.path.join("event/wfh_img", "M4_A2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M4_B2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M4_C2.png"))]
wfh_hint_problem4 = [   pygame.image.load(os.path.join("event/wfh_img", "Q4_A_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_B_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_C_HINT.png"))]
wfh_text_problem4 = [pygame.image.load(os.path.join("event/wfh_img", "Q4_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_C.png"))]
wfh_message1_problem4 = [   pygame.image.load(os.path.join("event/wfh_img", "Q4_A_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_B_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_C_hint1.png"))]
wfh_message2_problem4 = [   pygame.image.load(os.path.join("event/wfh_img", "Q4_A_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_B_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q4_C_hint2.png"))]
wfh_impact_problem4 =[[15,10,0,0,0,0],[-10,-20,0,0,0,0], [0,0,0,0,5,2]]
wfh_impact2_problem4 =[[0,0,0,0,-1,-3],[0,0,3,2,5,3], [0,0,-1,-3,0,0]]

wfh_decision_problem5 = [pygame.image.load(os.path.join("event/wfh_img", "Q5_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_C.png"))]
wfh_notify_problem5 = [ pygame.image.load(os.path.join("event/wfh_img", "M5_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M5_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M5_C.png"))]
wfh_notify2_problem5 = [ pygame.image.load(os.path.join("event/wfh_img", "M5_A2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M5_B2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M5_C2.png"))]
wfh_hint_problem5 =  [  pygame.image.load(os.path.join("event/wfh_img", "Q5_A_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_B_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_C_HINT.png"))]
wfh_text_problem5 = [pygame.image.load(os.path.join("event/wfh_img", "Q5_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_C.png"))]
wfh_message1_problem5 =  [  pygame.image.load(os.path.join("event/wfh_img", "Q5_A_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_B_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_C_hint1.png"))]
wfh_message2_problem5 =  [  pygame.image.load(os.path.join("event/wfh_img", "Q5_A_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_B_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q5_C_hint2.png"))]
wfh_impact_problem5 =[[0,0,-1,-3,0,0],[20,10,0,0,0,0], [0,0,0,0,5,3]]
wfh_impact2_problem5 =[[20,10,4,2,4,2],[0,0,-1,-3,0,0], [0,0,1,0,-1,-2]]

wfh_decision_problem6 = [pygame.image.load(os.path.join("event/wfh_img", "Q6_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_C.png"))]
wfh_notify_problem6 = [ pygame.image.load(os.path.join("event/wfh_img", "M6_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M6_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M6_C.png"))]
wfh_notify2_problem6 = [ pygame.image.load(os.path.join("event/wfh_img", "M6_A2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M6_B2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "M6_C2.png"))]
wfh_hint_problem6 =  [  pygame.image.load(os.path.join("event/wfh_img", "Q6_A_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_B_HINT.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_C_HINT.png"))]
wfh_text_problem6 = [pygame.image.load(os.path.join("event/wfh_img", "Q6_A.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_B.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_C.png"))]
wfh_message1_problem6 =  [  pygame.image.load(os.path.join("event/wfh_img", "Q6_A_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_B_hint1.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_C_hint1.png"))]
wfh_message2_problem6 =  [  pygame.image.load(os.path.join("event/wfh_img", "Q6_A_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_B_hint2.png")),
                        pygame.image.load(os.path.join("event/wfh_img", "Q6_C_hint2.png"))]
wfh_impact_problem6 =[[0,0,-1,-3,-2,-4],[-10,-20,0,0,0,0], [-5,-10,0,0,5,3]]
wfh_impact2_problem6 =[[0,0,4,2,5,3],[0,0,4,2,0,0], [-5,-10,-1,-3,0,0]]

wfh_decision = [wfh_decision_problem1,wfh_decision_problem2,wfh_decision_problem3,wfh_decision_problem4,wfh_decision_problem5,wfh_decision_problem6]
wfh_impact = [wfh_impact_problem1,wfh_impact_problem2,wfh_impact_problem3,wfh_impact_problem4,wfh_impact_problem5,wfh_impact_problem6]
wfh_impact2 = [wfh_impact2_problem1,wfh_impact2_problem2,wfh_impact2_problem3,wfh_impact2_problem4,wfh_impact2_problem5,wfh_impact2_problem6]

wfh_hint = [wfh_hint_problem1,wfh_hint_problem2,wfh_hint_problem3,wfh_hint_problem4,wfh_hint_problem5,wfh_hint_problem6]
wfh_notify = [wfh_notify_problem1,wfh_notify_problem2,wfh_notify_problem3,wfh_notify_problem4,wfh_notify_problem5,wfh_notify_problem6]
wfh_notify2 = [wfh_notify2_problem1,wfh_notify2_problem2,wfh_notify2_problem3,wfh_notify2_problem4,wfh_notify2_problem5,wfh_notify2_problem6]
wfh_text = [wfh_text_problem1,wfh_text_problem2,wfh_text_problem3,wfh_text_problem4,wfh_text_problem5,wfh_text_problem6]
wfh_message1 = [wfh_message1_problem1,wfh_message1_problem2,wfh_message1_problem3,wfh_message1_problem4,wfh_message1_problem5,wfh_message1_problem6]
wfh_message2 = [wfh_message2_problem1,wfh_message2_problem2,wfh_message2_problem3,wfh_message2_problem4,wfh_message2_problem5,wfh_message2_problem6]
HINT_BACK = pygame.image.load(os.path.join("images1/notify_message", "HINT_back.png"))
'''
wfh_problem = ['Q???????????????delta???????????????????????????','Q??????????????????????????????????????????????????????????????????','Q?????????????????????????????????????????????????????????','Q???????????????????????????20????????? ????????????????????????','Q??????????????????????????????????????????']
wfh_decision_problem1 = ['A????????????????????????????????????','B????????????????????????','C??????????????????????????????']
wfh_impact_problem1 = [[10,0,5,3,4,2],[50,30,4,2,2,0],[40,20,2,0,4,2]]
wfh_decision_problem2 = ['A??????????????????????????????????????????','B??????????????????????????????????????????????????????????????????????????????????????????','C????????????????????????????????????????????????????????????????????????']
wfh_impact_problem2 = [[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
wfh_decision_problem3 = ['A?????????????????????????????????????????????????????????????????????','B????????????????????????????????????????????????','C???????????????????????????????????????????????????']
wfh_impact_problem3 = [[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
wfh_decision_problem4 = ['A???????????????????????????????????? ?????????','B??????????????? ????????????????????????????????????','C?????????????????????????????????????????????????????????????????????']
wfh_impact_problem4 =[[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
wfh_decision_problem5 = ['A??????????????????????????????','B????????????????????????','C??????????????????????????????????????????']
wfh_impact_problem5 =[[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
'''
