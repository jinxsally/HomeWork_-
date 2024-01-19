import requests
from lxml import etree
import simplejson
import re

headers = {
        'Host': 'music.163.com',
        'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
}


def get_url_json(url):
    with requests.Session() as session:
        response = session.get(url, headers=headers)
        text = response.text
        text_json = simplejson.loads(text)
        print(text_json)
    return text_json

def parse_lyric( text_json):
        try:
            lyric = text_json.get('lrc').get('lyric')
            if lyric is None:
              print('None')
              return
            else:
                regex = re.compile(r'\[.*\]')
                final_lyric = re.sub(regex, '', lyric).strip()
                print(final_lyric)
                return final_lyric
        except AttributeError as k:
            print(k)
            pass

def get_all_song_lyric():
        all_song_ids = ['2094118217','1998355620','1314438112','1467135593','421137682','28188434','1465162316','28188425','30352891','504686859']
        all_song_names = ['canghaifeichen','meinanbian','liuguangji','huayujiu','bulaomeng','jinlichao','liuli','luguxunmeng','qiansixi','shifengdong']
        for song_id, song_name in zip(all_song_ids, all_song_names):
            url_song = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
            json_text = get_url_json(url_song)
            print(song_id,song_name)
            try:
                with open('D:/'+str(song_name)+".txt", 'w+') as f:
                    f.write(parse_lyric(json_text))
                    print(song_name)
                    parse_lyric(json_text)
                    print('-' * 30)
            except Exception as e:
                print('error')
                pass



get_all_song_lyric()