from dataclasses import dataclass


@dataclass
class StateInfo:
    Action: str = ""
    Action_Time: int = 0
    TotalSlides: int = 0
    SlideCounter: int = 0
    Folder: str = ""


# class StateMachine:

#     def NowTenthsSecond():
#         return int(time.time_ns() / 100000000)


#     def CheckState():
#     # Sequence of states: (assumes first slide is already in view of camera. )
#     #   Save Photo
#     #   Incrument slide counter, check if done with caroucel
#     # #   Advanced Button Down
#     #   Wait 2 seconds
#     #   Advanced Button Up
#     #   Wait 4 seconds for contrast to stabalize
#     #   Save Photo
#     # If not actions, then default is imageDisplay to update UI

#     Current_Time = NowTenthsSecond()

#     if Current_Time >= Next_State["Action_Time"]:
#         if Next_State["Action"] == "SavePhoto":
#             print("savePhoto(slideCounter)")
#             Next_State["Action"] = "ButtonDown"

#         elif Next_State["Action"] == "ButtonDown":
#             print("Button Down")
#             changeSlide.push_button_down()
#             Next_State["Action_Time"] = Current_Time + 20  # 2 seconds
#             Next_State["Action"] = "ButtonUp"

#         elif Next_State["Action"] == "ButtonUp":
#             print("Button Up")
#             changeSlide.push_button_up()
#             Next_State["Action_Time"] = Current_Time + 60  # 6 seconds
#             Next_State["Action"] = "CheckMorePhotos"

#         elif Next_State["Action"] == "CheckMorePhotos":
#             print("CheckMorePhotos")
#             Next_State["Action"] = "SavePhoto"

#     else:
#         Image_Display()
