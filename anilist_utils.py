import requests
import webbrowser
import time
import config
import traceback

from ui_utils import print_line_strip

def authorize():
    app_url = "https://anilist.co/settings/developer"
    redirect_uri = "https://anilist.co/api/v2/oauth/pin"    
    
    print("Welcome to the AniList authorization wizard!")
    print_line_strip()

    print(f"Please head over to {app_url} and create a new application.")
    print(f"Redirect URI must be set to {redirect_uri}.")
    time.sleep(2)
    webbrowser.open_new_tab(app_url)
    
    print("Please enter AniList API Client ID:", end='')
    config.ANILIST_API_CLIENT_ID = input()
    
    print_line_strip()
    
    auth_url = f"https://anilist.co/api/v2/oauth/authorize?client_id={config.ANILIST_API_CLIENT_ID}&response_type=token"
    print(f"Please head over to {auth_url} and login, and enter the code you receive below.")
    time.sleep(2)
    webbrowser.open_new_tab(auth_url)
    print("Please enter Authorization PIN given:", end='')
    config.ANILIST_API_PIN = input()

    print_line_strip()

    anilist_request_url = "https://graphql.anilist.co"
    
    header = {
        'Authorization' : f"Bearer {config.ANILIST_API_PIN}",
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    #query "viewer" to get the currently authenticated user
    query = '''
    query {
        Viewer {
           name
        }
    }
    '''
    response = requests.post(anilist_request_url, headers=header, json={'query' : query})
    user_name = ""
    
    print_line_strip()
    
    try:
        user_name = response.json()['data']['Viewer']['name']
    
    except:
        print("An error occurred during authorization. Please retry.")
        print_line_strip()
        traceback.print_exc()
        print_line_strip()
        print(response.json()['errors'])
        print_line_strip()
        return
    
    print(f"Authorized as: {user_name}.")
    
    print_line_strip()



    
