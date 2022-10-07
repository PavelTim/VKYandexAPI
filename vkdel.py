import requests
from pprint import pprint

class VKDel:

    url = 'https://api.vk.com/method/'
    def __init__(self, token, version='5.131'):
        ''' Инициация '''
        self.params = {
            'access_token': token,
            'v': version
        }

    def _testresult(self, res, code, message=''):
        ''' Проверяет выполнение задачи и выводит сообщение.
        Можно будет изменить в одном месте либо вообще убрать. '''
        if res.status_code == code:
            print(f'{message} Success, status: {res.status_code}')
            return True
        return False

    def getphotos(self, owner_id, album_id='profile', photo_sizes='1'):
        ''' '''
        url = self.url + 'photos.get'
        params = {
            'owner_id': owner_id,
            'album_id': album_id,
            'photo_sizes': photo_sizes, # 0
            'extended': '1', #  а нужно ли это?
            **self.params
        }
        res = requests.get(url, params=params)
        res.raise_for_status()
        return res.json()

if __name__ == "__main__":
    print('-----------OK----------')
    token = input()
    client_id = input()
    vkdelirium = VKDel(token)
    print(client_id)
    resultvk = vkdelirium.getphotos(client_id)
    pprint(resultvk, sort_dicts=False)