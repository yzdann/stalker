import os
import time
import filecmp
from pathlib import Path
import requests

home = str(Path.home())
dir_to_save = f'{home}/Pictures/crush_telegram_profile_photos/'
file_name = time.strftime('%Y_%m_%d')
full_file_path = f'{dir_to_save}/{file_name}'
telegram_id = input('Enter your Crush telegram id: ')
profile_photo_url = f'https://t.me/i/userpic/320/{telegram_id}.jpg'

if not os.path.exists(dir_to_save):
    os.mkdir(dir_to_save)

resp = requests.get(profile_photo_url)
status_code = resp.status_code

if status_code == 200:
    with open(full_file_path, 'wb') as f:
        for chunk in resp:
            f.write(chunk)

elif status_code == 404:
    print('No profile picture')

else:
    print('Sth bad happen, {}'.format(status_code))

if len(os.listdir(dir_to_save)) > 1:
    latest_photo = os.listdir(dir_to_save)[-1]
    path_to_latest_photo = f'{dir_to_save}/{latest_photo}'
    if not filecmp.cmp(path_to_latest_photo, full_file_path):
        os.remove(full_file_path)
