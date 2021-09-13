import requests


class YaUploader:

    def __init__(self, token):
        self.token = token
        self.path_to_yandex = 'Test'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, disk_file_path):
        path_to_yandex = self.path_to_yandex + '\\'.join(disk_file_path.split('\\')[:2:-1])
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": path_to_yandex, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href', '')
        response = requests.put(href, data=open(disk_file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    path_to_file = 'C:\\VSCode\\Netology\\fortest.py'
    token = ''
    path_to_yandex = 'Test'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)