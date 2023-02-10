from dataclasses import dataclass
# © SailorScott 2023

@dataclass
class StateInfo:
    Action: str = ""
    Action_Time: int = 0
    TotalSlides: int = 0
    SlideCounter: int = 0
    Folder: str = ""
