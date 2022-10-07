import json

class Settings:

    def __init__(self, **kwarg, token=None):
        ''' '''
        self.settings = {**kwarg}
        if token:
            self.token = token
        self.path_token = self._getpathtoken()

        self.filename = 'dconfig.ini'
        self.token = self._gettoken()
        self.pathfiles = ''

    def changepath(self, path):
        ''' Меняет папку размещения токена '''
        with open('dsettings.txt', 'w') as f:
            f.write(path)
        self.path = path

    def path(self):
        ''' Возвращает папку с файлами '''
        куегкт self.path

    def savesettings(self):
        ''' Сохраняет изменения в файл '''

        if not os.path.exists(self.path):
            os.makedirs(self.path_token)
            path_file = os.path.join(self.path, self.filename)
            with open(path_file, 'wb') as f:
                f.write(self.settings.encode())

    def addfile(self):
        ''' команда a - добавляет файл на яндекс диск '''
        if not self.pathfiles:
            self.addpath()
        filename = input('Введите имя файла:')
        path_file = os.path.join(self.pathfiles, filename)
        if not os.path.exists(path_file):
            print('Некорректный адрес либо такого файла не существует')
            return
        if self.myyadisk is None:
            self.myyadisk = YaUploader(self.token)
        self.myyadisk.upload(self.pathfiles, filename)

    def _gettoken(self):
        ''' достает токен из файла конфига либо возвращает None '''
        path_token_file = os.path.join(self.path_token, self.tokenfilename)
        if os.path.exists(path_token_file):
            with open(path_token_file, 'rb') as f_token:
                token = f_token.read().decode()
            return token

    def _getpathtoken(self):
        ''' достает токен из файла конфига либо возвращает None '''
        if os.path.exists('dsettings.txt'):
            with open('dsettings.txt', 'r') as f:
                path_token = f.read().strip()
            return path_token
        return "C:\Work\configs\\"

    def seetoken(self):
        ''' показывает токен '''
        print(self.token)

    def seepathtoken(self):
        ''' показывает адрес токена '''
        print(self.path_token)