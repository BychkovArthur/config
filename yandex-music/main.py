from yandex_music import Client
from datetime import datetime
from dotenv import load_dotenv
from time import sleep
from os import getenv


load_dotenv()


VALID_BITRATE = [320, 192]
YANDEX_MUSIC_TOKEN_ENV_VAR_NAME = 'YANDEX_MUSIC_TOKEN'

client = Client(getenv(YANDEX_MUSIC_TOKEN_ENV_VAR_NAME)).init()


print('\n\n\n--------------------------------------------------------------')
print(datetime.now())

def build_artists(track_info):
    return ', '.join(track_info.artistsName())

def build_artists_decomposed(track_info):
    result = ''
    for artist in track_info.artists:
        if artist.decomposed is None:
            continue

        for i in range(0, len(artist.decomposed), 2):
            
            result += artist.decomposed[i]
            result += artist.decomposed[i + 1]['name']

    return result

total_tracks = len(client.users_likes_tracks())

start_from = 887
current_num = start_from

for track in client.users_likes_tracks()[start_from - 1:]:
    track_info = track.fetch_track()
    track_name = f'{build_artists(track_info)}{build_artists_decomposed(track_info)} | {track_info.title}'
    if track_info.version is not None:
        track_name += ' | ' + track_info.version
    track_name = track_name.replace('/', '\\')

    print(f'Скачиваю {current_num}/{total_tracks}')
    print(track_name)

    name_with_dir = f'./music/{track_name}'
    try:
        track_info.downloadCover(f'{name_with_dir}.png')
    except:
        print('[ERROR] Не удалось скачать изображение...')

    for bitrate in VALID_BITRATE:
        try:
            print(f'Загружаю с {bitrate=}')
            track_info.download(filename=f'{name_with_dir}.mp3', codec='mp3', bitrate_in_kbps=bitrate)
            break
        except:
            print(f'[ERROR] Не получилось загрузить с {bitrate=}')
    print('\n\n')

    current_num += 1
    sleep(10)
