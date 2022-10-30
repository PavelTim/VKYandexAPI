import json
import datetime as dd

from yadiskdel import YaDiskDel
from vkdel import VKDel

def main():
    ''' Попытка '''

    client_id = input('Введите client_id:')
    token = input('Введите token Вконтакте:')
    yandextoken = input('Введите token Яндекса:')

    vkdelirium = VKDel(token)

    resultvk = vkdelirium.getphotos(client_id)

    if 'error' in resultvk:
        print(f'Некорректный VK ID: {client_id}')
        return

    print('Всего получено фотографий:', resultvk['response']['count'])
    n_photos = int(input('Введите количество загружаемыъ фото:'))

    mydisk = YaDiskDel(yandextoken)

    path = '/vkprofilephotos'
    # print(mydisk.dirinfo(path))
    mydisk.createdir(path)

    list_log = []
    names = set()

    for index_, item in enumerate(resultvk['response']['items']):

        if index_ >= n_photos:
            break

        name = str(item['likes']['count']) + str(index_)

        if name in names:
            name += str(dd.datetime.fromtimestamp(item['date']).strftime("%d.%B.%Y"))
            name += str(item['date'])

        names.add(name)

        image_max = max(item['sizes'], key=lambda x: x['height'])

        url_image = image_max['url']
        size_image = image_max['type']

        print(path + '/' + name + ".jpg")
        yanuploadresult = mydisk.urlupload(url=url_image, path=path + '/' + name + ".jpg")
        dict_log = {"file_name": name + ".jpg", "size": size_image, "response": yanuploadresult}
        list_log.append(dict_log)

    with open('logfile.json', 'w') as f:
        json.dump(list_log, f)


if __name__ == '__main__':
    main()
