import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

# api_url = 'https://api.telegram.org/6176884644:AAE8459aNh1EWgxVSU1YZL9R5EpIc_K79bc/getMe'

class Get_dog:

    def __init__(self):
        self.url = 'https://random.dog/woof.json'

    # неудачная попытка получить файл не json с https://random.dog/
    # это вообще как то можно сделать без сохранения на на комп? потому что это было бы логичнее
    # не всегда же есть возможность получить с сайта именно json файл (наверное?)
    # def get_file(self):
    #     response = requests.get(self.url)
    #     #print(response.status_code) # check if the connection is set
    #     # get the necessary html string (not type string) for jpg, png, webp, gif, etc.
    #
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     tag = soup.find('img')
    #     # if mp4
    #     if tag == None:
    #         tag = soup.find('source')
    #
    #     # get filename
    #     img_src = tag.get('src')
    #     filename = urljoin(self.url, img_src) # https://random.dog/<imagename>.<format>
    #
    #     return filename


    def get_file_json(self):
        response = requests.get(self.url)
        return response.json().get('url')

#new_dog = Get_dog()
#new_dog.get_file()