
username = "every_pic_has_its_own_story"
password = "AnkI@1501"
caption = "Your desired caption"
video_path = "Input_Video\chunk_3.mp4"

import requests

def get_long_lived_token(short_lived_token, app_id, app_secret):
    url = f"https://graph.facebook.com/oauth/access_token"
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': short_lived_token,
    }
    response = requests.get(url, params=params)
    return response.json()


import requests
import os

def upload_video_to_instagram(access_token, instagram_account_id, video_path, caption):
    video_url = 'https://graph.facebook.com/v16.0/{instagram_account_id}/media'.format(instagram_account_id=instagram_account_id)
    
    # Step 1: Initiate the video upload session
    params = {
        'media_type': 'VIDEO',
        'video_url': video_path,  # The video file URL should be hosted
        'caption': caption,
        'access_token': access_token
    }

    response = requests.post(video_url, params=params)
    if response.status_code == 200:
        media_id = response.json()['id']
        print(f"Media ID: {media_id}")
        
        # Step 2: Publish the video
        publish_url = 'https://graph.facebook.com/v16.0/{instagram_account_id}/media_publish'.format(instagram_account_id=instagram_account_id)
        publish_params = {
            'creation_id': media_id,
            'access_token': access_token
        }

        publish_response = requests.post(publish_url, params=publish_params)
        if publish_response.status_code == 200:
            print("Video published successfully!")
        else:
            print("Error publishing video:", publish_response.json())
    else:
        print("Error uploading video:", response.json())

# Example usage
access_token = "your_long_lived_access_token"
instagram_account_id = "your_instagram_account_id"
video_path = "https://path_to_your_video.mp4"  # Must be a publicly accessible video URL
caption = "Your desired caption"
upload_video_to_instagram(access_token, instagram_account_id, video_path, caption)
