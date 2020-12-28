from ui_utils import print_line_strip
import menu_utils

def menu():
    print_line_strip()
    print("Main Menu.")
    while True:
        i = 1
        while i<=len(menu_utils.MENU_UI_MAPPINGS):
            print(f"{i}. {menu_utils.MENU_UI_MAPPINGS[str(i)]}")
            i+=1
        
        print("Please select an option:", end='')
        try:
            menu_utils.MENU_METHOD_MAPPINGS[input()]()
        except KeyError:
            print("Invalid Input.")

