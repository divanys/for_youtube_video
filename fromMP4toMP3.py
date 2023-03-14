"""
Работать должно и на дистрибутивах линукс, и на виндовс. 
Установка в fedora: sudo dnf install ffmpeg

Вводить можно относительный путь к файлу .mp4, преобразование довольно быстрое
"""


import subprocess

command = f"ffmpeg -i '{input('Введите название видео: ')}.mp4' -b:a 320k '{input('Введите желаемое название аудио: ')}.mp3'"
subprocess.call(command, shell=True)