import anilist_utils
import trakt_utils
from ui_utils import print_credits, print_line_strip


def one():
    anilist_utils.authorize()
    #ONE

def two():
    trakt_utils.authorize()
    #TWO

def three():
    print("Three.")
    #THREE

def four():
    print_credits()
    #FOUR

def five():
    exit()

MENU_UI_MAPPINGS = {
    '1' : "Setup AniList Authorization(REQUIRED).",
    '2' : "Setup Trakt Authorization(REQUIRED).",
    '3' : "RETraktED.",
    '4' : "Credits.",
    '5' : "EXIT."
}


MENU_METHOD_MAPPINGS = {
    '1' : one,
    '2' : two,
    '3' : three,
    '4' : four,
    '5' : five
}
