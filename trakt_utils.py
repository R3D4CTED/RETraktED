import config
from ui_utils import print_line_strip

import requests
import webbrowser
import time

"""
= POST https://api.trakt.tv/oauth/device/code
*:: JSON body with [client_id] as a property. Set the value to your client ID.

= Display [user_code] to user
= Direct user to [verification_url]

= (Every [interval] seconds) GET https://api.trakt.tv/oauth/device/code
*:: If 200, break loop and store access token from body
*:: If not 200, poll again if [interval] is less than [expires_in]
"""

def authorize():
    print("Welcome to the Trakt Authorization Wizard!")
    print_line_strip()
    
    app_url = "https://trakt.tv/oauth/applications/"
    print(f"Please head over to {app_url} and make an application. Redirect URI can be set to the default value given there.")
    print("Please enter Client ID:", end='')
    config.ANILIST_API_CLIENT_ID = input()
    print("Please enter Client Secret:", end='')
    config.TRAKT_CLIENT_SECRET = ""
    
    code_request_url = "https://api.trakt.tv/oauth/device/code"
    try:
        response = requests.post(code_request_url, json={'response_type' : 'application/json' ,'client_id' : config.TRAKT_CLIENT_ID})
    except:
        print("An error occurred. Please try again later.")
        return

    print(f"Authorization code : {response.json()['user_code']}. \n\nPlease go to {response.json()['verification_url']} and enter the code there.")
    
    token_request_url = "https://api.trakt.tv/oauth/device/token"
    device_code = response.json()['device_code']
    interval = int(response.json()['interval'])
    expiry = int(response.json()['expires_in'])
    webbrowser.open_new_tab(response.json()['verification_url'])
    time_elapsed = 0
    while time_elapsed <= expiry:
        try:
            code_response = requests.post(token_request_url, json={'code' : device_code, 'client_id' : config.TRAKT_CLIENT_ID, 'client_secret' : config.TRAKT_CLIENT_SECRET})
        except:
            break

        print(f"Response:{code_response.text}")
        print(f"Status: {code_response.status_code}")
        if(code_response.status_code == 200):
            try:
                config.TRAKT_TOKEN = code_response.json()['access_token']
            except:
                continue
            
            break
        
        time.sleep(interval)
        print(f"Time elapsed: {time_elapsed}")
        time_elapsed += interval

    if (config.TRAKT_TOKEN is None):
        print("Trakt Authorization failed. Please try again.")
        return
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {config.TRAKT_TOKEN}',
        'trakt-api-version': '2',
        'trakt-api-key': config.TRAKT_CLIENT_ID
    }
    response = requests.get('https://api.trakt.tv/users/settings', headers=headers)
    username = response.json()["user"]["username"]
    print(f"Authorization was successful. Logged in as {username}.")

    
authorize()    
    

    



