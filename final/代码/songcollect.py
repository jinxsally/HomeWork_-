import requests
from bs4 import BeautifulSoup

headers={
       'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
       'Accept-Encoding':'gzip, deflate, br',
       'Accept-Language':'zh-CN,zh;q=0.9',
       'Cookie':'NMTID=00OKiM5AleCcl9oBE2wgXajAYYgdI0AAAGMa9VfUA; _iuqxldmzr_=32; _ntes_nnid=4fe8b153d326c20e7b90a52e605e82f9,1702616196411; _ntes_nuid=4fe8b153d326c20e7b90a52e605e82f9; WM_TID=0OzEGt8zsjhEAEUAFRbU9CzL5mJ4kY%2BX; WEVNSM=1.0.0; WNMCID=rzkbtq.1702616199069.01.0; sDeviceId=YD-qTgAPi1VZkdERwUQEEfQiWfINTgfJ8J7; ntes_utid=tid._.UwwPDBmKFWJBVwVUEVLE8S3a8iI6Ur19._.0; __snaker__id=wop53xd25WnWgsGW; MUSIC_U=006906B03ECA33496E872CA5199896AA74FA6AC9357879BF45304A82C347B20ECFE66C75DA8530FF0B13D274FA383508E04B1019A2E93C96B35E7DE5BC98FA21FBFC85390FE54A220E7E2E3044449027EF45F68A74745FA27CD221DE1E6182D73C61983BD3902EFE95B69CF2308F5BC2A925BE340DC143C7BF3C74B72B1AA0C3FB23F4E84E88BD73613A96B0CAF3E79612F802E32FAA373D451EC92F9B32C3E8F3DFC638A3CB8BC23C417DB28487396101B645E0C1B546D14E1B27CAF89B38E414D70B92C786DDDACF3486ABB48240C30902428B24268BABDED99A24902E5F23EBA69544B006ED627260F9830D8C04E9B7005294E1B5B5704B39531298071699FBF4E4B8AC0EFD76D9C54588D56A840CDA99D358B88B7291DCABE08637D317654D59BD3F7FE36C2FC071E441A1DD301A2F5920A188744855FDFA4C71C5586550888FF642CF3EEBD54B8BCD1AF05539BD005B98A2F2987FE18A9E746C02B5F69E773456F8B0EC2983C7ADA403B718AB2C67; ntes_kaola_ad=1; __csrf=741c8b6b62a261a4f0219ac1cda4f3b7; __csrf=741c8b6b62a261a4f0219ac1cda4f3b7; WM_NI=m7qG7oG0CpInk0Z6NhGCzJ1qCGpvanIs6AZYhGARGx56M%2FwnEwqbLDcSfCyQGRdjTCGt4xDwUwz6Kjn6Kt9gVpP8yUbSxJX7rE%2Bl2tj8HbUzlpUCdjds5YDCllL%2FW5X3Ylg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eedae9548387fbabc847e98a8ab3d85a969a8f86d87cf4988fa7f15ca3eefaabb62af0fea7c3b92aafe9bfa8b66585f08d91cc66a9f096d7cd64859db6abb47b8199c097e4668badfaa2d953ac998fb3c674f7ea83d0f66687a9bf83cf50a18daaa4fc5b858eac8bd74985acfc99c77d97a9b6d7ca62aeea8595bc6d96b0a0d9fc5fa28db8abdb3db29be58db180aae88883d872b0b09ba4e762a8adfbbac749b0b484d0d63f9ced978de637e2a3; JSESSIONID-WYYY=XkGVKOOgEVNwRy%2BT6e%2FuU1qgYom8yxx%2BnfByfUhGb8mc%2BDPVZJ6vdtBkWVbpTF95JGW73V3gDhTakPXThOnmvGuQUcbCO7Y%2FXO6AE4e06lrP7ywlR1NojkXEl8TivPknkl3JAaIhntUiRY6f26yxntVa5oe%5C5Yj8D9KAySYnK3%2BEWe%5Cn%3A1705302306952',
       'Referer':'https://music.163.com/',
       'Upgrade-Insecure-Requests':'1',
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# def songdata(href):
#     r = requests.get(href, headers=headers)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     count = soup.find('span',id_='cnt_comment_count')
#     return count

def songcollect(href):
    r = requests.get(href,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    listt = soup.find('ul',class_='f-hide').find_all('li')
    for x in listt:
        songName = x.find('a').text
        id = x.find('a')['href'].replace('/song?id=',"")
        herf = 'http://music.163.com/#'+x.find('a')['href']
        with open('music_song.csv', 'a', encoding='utf-8-sig') as f:
            f.write(songName + ',' + id + ','+ href + '\n')
        f.close()
        # count = songdata(href)
        print(songName,herf,id)


url = 'https://music.163.com/artist/album?id=188565&limit=200'
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
listt = soup.find('ul', class_="m-cvrlst m-cvrlst-alb4 f-cb").find_all('li')
for x in listt:
        albumName = x.find('div',class_='u-cover u-cover-alb3')['title']
        href = 'http://music.163.com'+x.find('a',class_='msk')['href']
        songcollect(href)

