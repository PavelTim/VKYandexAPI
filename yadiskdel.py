import requests


class YaDiskDel:

    def __init__(self, token):
        ''' Обряд инициации. Пляски с токеном. '''
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }

    def diskinfo(self, allfields=False):
        ''' Возвращает информацию о диске. '''
        url = 'https://cloud-api.yandex.net/v1/disk'
        if allfields:
            params = {'fields': 'total_space, used_space'}
            res = requests.get(url, headers=self.headers, params=params)
        else:
            res = requests.get(url, headers=self.headers)
        res.raise_for_status()
        if res.status_code == 200:
            print(f'diskinfo Success, allfiels = {allfields}')
        return res.json()

    def dirinfo(self, path, allfields=False):
        ''' Проверяет наличие каталога на яндекс диске.
        Дополнительные поля в принципе не нужны. '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        if not allfields:
            params['fields'] = 'type'
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 404:
            return False
        res.raise_for_status()
        if res.status_code == 200:
            print(f'dirinfo Success, allfiels = {allfields}')
            return True
        print(f'dirinfo Непонятная ошибка, allfiels = {allfields}. status: {res.status_code}')
        return False

    def createdir(self, path):
        ''' создает папку на яндекс диске.
        возвращает True если папка создана или уже существует. '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        res = requests.put(url, headers=self.headers, params=params)
        # не все версии python поддерживают match case
        # match res.status_code:
        if res.status_code == 201:
            # case 201:
            print(f'createdir Success папка создана ')
            return True
        elif res.status_code == 409:
            # case 409:
            print(f'createdir Success папка цже существует ')
            return True
        else:
            # case _:
            res.raise_for_status()
            print(f'createdir Непонятная ошибка. status: {res.status_code}')
            return False

    def linkupload(self, path, overwrite=True):
        ''' Дает url ссылку для загрузки на яндекс диск файла с компьютера пользователя.
        Для наших целей не используется. '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path, 'overwrite': overwrite}
        res = requests.get(url, headers=self.headers, params=params)
        res.raise_for_status()
        if res.status_code == 200:
            print(f'linkupload Success, res.status_code = {res.status_code}')
            return res.json().get('href', "")
        print(f'linkupload Непонятная ошибка. status: {res.status_code}')

    def urlupload(self, url, path, overwrite=True):
        ''' Загружает картинку по ссылки в папку на яндекс диске.
        path - папка на яндекс диске,
        url -  ссылка на картинку в интернете. '''
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path, 'url': url, 'overwrite': overwrite}
        res = requests.post(url_upload, headers=self.headers, params=params)
        res.raise_for_status()

        if res.status_code == 202:
            print(f'linkupload Success, res.status_code = {res.status_code}')
            return res.json().get('href', "")
        print(f'urlupload Непонятная ошибка. status: {res.status_code}')
        return res.json().get('href', "")

    def gedonism(self):
        ''' В каждом классе обязательно есть функция,
        которой никто никогда не пользуется и никто не знает, зачем она нужна.
        Эта функция получает удовольствие сама для себя, просто потому, что она существует. '''
        self.gedonism.message = "Я существую, а следовательно я получаю удовольствие."
        self.gedonism.count = 0
        for i in range(1000):
            self.gedonism.count += 1
            pass


if __name__ == "__main__":
    path1 = '/disk:/testdir/24092022.txt'
    # mydisk = YaDiskDel(yandextoken)