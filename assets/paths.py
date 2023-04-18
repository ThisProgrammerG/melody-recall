from pathlib import Path


DIRECTORIES = ('fonts', 'images', 'musics', 'sounds')
ASSETS_PATH = Path(__file__).parent

def get_path(*, fonts='', images='', musics='', sounds='') -> Path:
    for directory_name in DIRECTORIES:
        if file_name := locals().get(directory_name):
            return ASSETS_PATH / directory_name / file_name

# FONTS

# IMAGES
IMAGE_ICON = 'icon.png'

# MUSICS

# SOUNDS
SOUND_1 = '1.wav'
SOUND_2 = '2.wav'
SOUND_3 = '3.wav'
SOUND_4 = '4.wav'
SOUND_5 = '5.wav'
SOUND_6 = '6.wav'
SOUND_7 = '7.wav'
SOUND_8 = '8.wav'
SOUND_9 = '9.wav'
