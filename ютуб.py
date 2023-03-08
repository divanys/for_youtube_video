
'''

В написании кода помог сайт https://codeby.net
В настоящее время код работает
Использование библиотек youtube_dl и pytube выдаёт ошибки и работает некорректно  
  
'''
import os.path
import time
import requests
from tqdm import tqdm


def playlist_item(url):
   

    params = {
        'url': url,
        'nextPageToken': '',
    }

    response = requests.get('https://api.youtubemultidownloader.com/playlist', params=params).json()
    list_items = []
    for item in range(0, len(response['items'])):
        list_items.append(response['items'][item]['id'])
    return list_items


def get_channel_name(vid_id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.141 Safari/537.36',
        'accept': '*/*',
    }

    params = {
        'prettyPrint': 'false',
    }

    json_data = {
        'videoId': vid_id,
        'context': {
            'client': {
                'hl': 'ru',
                'gl': 'RU',
                'deviceMake': '',
                'deviceModel': '',
                'visitorData': 'CgtrdUNhZ3U2VGNEOCiDndSTBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/98.0.4758.141 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20220502.01.00',
                'osVersion': '10.0',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CIOd1JMGELiLrgUQmN79EhCUj64FEOqQrgUQw_KtBRCY6q0FELfLrQUQ8IKuBRC7ka4FENSDrgUQ6JCu'
                                      'BRCw7q0FEK_yrQUQgub9EhCR-PwSENi-rQU%3D',
                },
                'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                'browserName': 'Chrome',
                'browserVersion': '98.0.4758.141',
                'screenWidthPoints': 1137,
                'screenHeightPoints': 870,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': 360,
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '8000000',
                'playerType': 'UNIPLAYER',
                'tvAppInfo': {
                    'livingRoomAppMode': 'LIVING_ROOM_APP_MODE_UNSPECIFIED',
                },
                'clientScreen': 'WATCH_FULL_SCREEN',
            },
            'user': {
                'lockedSafetyMode': False,
            },
            'request': {
                'useSsl': True,
                'internalExperimentFlags': [],
                'consistencyTokenJars': [],
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1651838604229',
                    },
                    {
                        'key': 'flash',
                        'value': '0',
                    },
                    {
                        'key': 'frm',
                        'value': '0',
                    },
                    {
                        'key': 'u_tz',
                        'value': '360',
                    },
                    {
                        'key': 'u_his',
                        'value': '5',
                    },
                    {
                        'key': 'u_h',
                        'value': '1080',
                    },
                    {
                        'key': 'u_w',
                        'value': '1920',
                    },
                    {
                        'key': 'u_ah',
                        'value': '1032',
                    },
                    {
                        'key': 'u_aw',
                        'value': '1920',
                    },
                    {
                        'key': 'u_cd',
                        'value': '24',
                    },
                    {
                        'key': 'bc',
                        'value': '31',
                    },
                    {
                        'key': 'bih',
                        'value': '870',
                    },
                    {
                        'key': 'biw',
                        'value': '1121',
                    },
                    {
                        'key': 'brdim',
                        'value': '43,12,43,12,1920,0,1708,991,1137,870',
                    },
                    {
                        'key': 'vis',
                        'value': '1',
                    },
                    {
                        'key': 'wgl',
                        'value': 'true',
                    },
                    {
                        'key': 'ca_type',
                        'value': 'image',
                    },
                ],
            },
        },
        'playbackContext': {
            'contentPlaybackContext': {
                'html5Preference': 'HTML5_PREF_WANTS',
                'lactMilliseconds': '2979',
                'signatureTimestamp': 19117,
                'autonavState': 'STATE_OFF',
                'autoCaptionsDefaultOn': False,
                'mdxContext': {},
                'playerWidthPixels': 647,
                'playerHeightPixels': 364,
            },
        },
        'cpn': 'pwy4NMkpT8PY63hl',
        'captionParams': {
            'deviceCaptionsOn': True,
        },
        'attestationRequest': {
            'omitBotguardData': True,
        },
    }

    print('\n[+] Получаю название канала...')
    channel_name = str(requests.post('https://www.youtube.com/youtubei/v1/player', params=params, headers=headers,
                                     json=json_data).json()['videoDetails']['author'])

    for m in ["?", '"', "/", ":", "#", "|", ",", " ?", "?!", "?!", "? ", " / ", " | "]:
        channel_name = channel_name.replace(m, " ")
    print(f'[+] Название канала получено: "{channel_name}"')
    return channel_name


def get_video_download(vid_id, channel_name):
    headers = {
        'authority': 'downloader.freemake.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Yandex";v="22"',
        'dnt': '1',
        'x-cf-country': 'RU',
        'sec-ch-ua-mobile': '?0',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36',
        'x-analytics-header': 'UA-18256617-1',
        'x-request-attempt': '1',
        'x-user-id': '94119398-e27a-3e13-be17-bbe7fbc25874',
        'origin': 'https://www.freemake.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.freemake.com/ru/free_video_downloader/',
        'accept-language': 'ru,en;q=0.9,uk;q=0.8',
    }

    print(f'[+] Получаю название и ссылку на видео')
    response = requests.get(f'https://downloader.freemake.com/api/videoinfo/{vid_id}', headers=headers).json()
    if response['qualities'][0]['qualityInfo']['itag'] == 22:
        video_title = str(response['metaInfo']['title'])
        for m in ["?", '"', "'", "/", ":", "#", "|", ",", " | "]:
            video_title = video_title.replace(m, "")
        url = response['qualities'][0]['url']
        print(f'[+] Название и ссылка получены. Начинаю загрузку: "{video_title}"')
        if not os.path.isdir(f'{channel_name}'):
            os.mkdir(f'{channel_name}')
            print(f'[+] Создаю папку для сохранения видео\n')
        else:
            print(f'[+] Папка для сохранения существует\n')
        req = requests.get(url=url, headers=headers, stream=True)
        total = int(req.headers.get('content-length', 0))
        with open(f'{os.path.join(channel_name, f"{video_title}.mp4")}', 'wb') as file, tqdm(
                desc=f"{video_title[0:int(len(video_title) / 2)]}...",
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in req.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
        print(f'\n[+] Видео сохранено в папку: "{channel_name}".\n[+] Загрузка завершена.\n')
    else:
        user_change = input('\n[+] Нет видео в качестве 720р\n[+] Загрузить в доступном качестве?:\n'
                            '\t[1]: Да\n\t[2]: Нет\n\t>>> ') 
        if user_change == "1":
            video_title = str(response['metaInfo']['title'])
            for m in ["?", '"', "'", "/", ":", "#", "|", ",", " | "]:
                video_title = video_title.replace(m, "")
            url = response['qualities'][0]['url']
            print(f'[+] Название и ссылка получены. Начинаю загрузку: "{video_title}"')
            if not os.path.isdir(f'{channel_name}'):
                os.mkdir(f'{channel_name}')
                print(f'[+] Создаю папку для сохранения видео\n')
            else:
                print(f'[+] Папка для сохранения существует\n')
            req = requests.get(url=url, headers=headers, stream=True)
            total = int(req.headers.get('content-length', 0))
            with open(f'{os.path.join(channel_name, f"{video_title}.mp4")}', 'wb') as file, tqdm(
                    desc=f"{video_title[0:int(len(video_title) / 2)]}",
                    total=total,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
            ) as bar:
                for data in req.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
            print(f'\n[+] Видео сохранено в папку: "{channel_name}".\n[+] Загрузка завершена.\n')
        elif user_change == "2":
            main()
            return
        else:
            print('[-] Ошибка или неверный ввод. Закрываю программу')
            exit(0)


def get_target_path(user_input):
    if user_input == "1":
        vid_id = input('\t[+] Введите ссылку на видео в виде:\n'
                           '\n\t\thttps://www.youtube.com/watch?v=[...]\n\n\t[+] Для выхода в меню введите: ex\n\n\t>>> ')
        if vid_id == 'ex':
            main()
            return
        while "https://www.youtube.com" not in vid_id:
            print()
            print('\t[-] Вы ввели ссылку с ошибкой. Попробуйте снова\n')
            vid_id = input('\t[+] Введите ссылку на видео в виде:\n'
                           '\n\t\thttps://www.youtube.com/watch?v=[...]\n\n\t[+] Для выхода в меню введите: ex\n\n\t>>> ')
            if vid_id == 'ex':
                main()
                return
        if '&list' in vid_id:
            vid_id = vid_id.split("&")[0].split("=")[-1]
        else:
            vid_id = vid_id.split("=")[-1]
        channel_name = get_channel_name(vid_id)
        get_video_download(vid_id, channel_name)
        main()
    elif user_input == "2":
        vid_id = input('\t[+] Введите ссылку на плейлист в виде:\n'
                       '\n\t\thttps://youtube.com/playlist?list=[...]\n\n\t[+] Для выхода в меню введите: ex\n\n\t>>> ')
        if vid_id == 'ex':
            main()
            return
        while "https://youtube.com/playlist" not in vid_id:
            print()
            print('\t[-] Вы ввели ссылку с ошибкой. Попробуйте снова\n')
            vid_id = input('\t[+] Введите ссылку на плейлист в виде:\n'
                       '\n\t\thttps://youtube.com/playlist?list=[...]\n\n\t[+] Для выхода в меню введите: ex\n\n\t>>> ')
            if vid_id == 'ex':
                main()
                return
        list_items = playlist_item(vid_id)
        print(f'[+] Видео в плейлисте: {len(list_items)}\n[+] Загружаю плейлист')
        for item in list_items:
            channel_name = get_channel_name(item)
            time.sleep(0.3)
            get_video_download(item, channel_name)
            time.sleep(0.3)
        main()
    elif user_input == "3":
        exit(0)
    else:
        main()


def main():
    get_target_path(input(f'\n[+] Выберите варианты загрузки:\n\t[1] Загрузить видео\n'
                          f'\t[2] Загрузить плейлист\n\t[3] Выход\n\t>>> '))


if __name__ == "__main__":
    main()

'''
старые способы скачивания)))
'''

# youtube_dl


# import youtube_dl
# import os.path
# def download_mp4(url):
#     info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
#     file_name = f"{info['title']}.mp4"
#     options = {
#         'format': 'best',
#         'outtmpl': file_name,
#     }
#     if os.path.exists(f'{file_name}'):
#         os.remove(f'{file_name}')
#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([url])
#
# media = input()
#
# download_mp4(media)
#


# pytube


# from pytube import YouTube
#
# yt = YouTube('https://www.youtube.com/watch?v=[...]') #ссылка на видео.
# fn = yt.videos
# path = ''
# fn.download(path)

