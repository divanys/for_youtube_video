"""

Работает на винде при установке moviepy (можно в термиинале IDE установить при помощи pip)
Установка в windows 10: pip install moviepy

Вводить можно относительный путь к файлу .mp4, преобразование довольно быстрое, 
нежелательно вводить названия с пробелами или слешами '\ /'
"""

from moviepy.editor import *

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

VIDEO_FILE_PATH = input('Введите название видео: ') + '.mp4'
AUDIO_FILE_PATH = input('Введите желаемое название аудио: ') + '.mp3'

MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)