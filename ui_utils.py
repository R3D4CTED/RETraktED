import progressbar
import shutil

def print_line_strip():
    columns, rows = shutil.get_terminal_size()
    i = 0
    while i<columns:
        print("*", end='')
        i+=1
   
    print()

def print_logo():
    print_line_strip()
    logo = """
 _____    ________ _________                __     ___    ______   _____
 |  __ \  |  ____| |__   __|                | |    | |   |  ____| |  __ \\ 
 | |__) | | |__       | |     _ __    __ _  | | __ | |_  | |__    | |  | |
 |  _  /  |  __|      | |    | '__|  / _` | | |/ / | __| |  __|   | |  | |
 | | \ \  | |____     | |    | |    | (_| | |   <  | |_  | |____  | |__| |
 |_|  \_\ |______|    |_|    |_|     \__,_| |_|\_\  \__| |______| |_____/ 
                                                                          
    """
    print(logo)
    print_line_strip()

def print_desc():
    desc = """
    A simple script to sync AniList to Trakt. This application comes with NO WARRANTY. Use at your own risk.

    This is free software, made with love by [REDACTED].
    """
    print(desc)
    print_line_strip()

def print_credits():
    credits = """
    AniList and Trakt for their APIs. Snaacky, Subby and Stalker for their mentoring and guidance. ScreX and Unlockr for requesting me to make this.
    
    Dedicated to the FOSS community.
    """
    print(credits)
    print_line_strip()
