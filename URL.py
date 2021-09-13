import requests

url = "https://superheroapi.com/api/2619421814940190/search/"
list = ['Hulk', 'Captain America', 'Thanos']


def max_intelligence(list, url):
    url_list = []
    heroes_dict = {}
    for name in list:
        url_list.append(url + name)
    for url_character in url_list:
        response = requests.get(url_character)
        names = response.json()['results'][0]['name']
        intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
        heroes_dict[names] = intelligence
    print(f'Самый умный персонаж {max(heroes_dict)}')

max_intelligence(list, url)

