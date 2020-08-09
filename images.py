import requests
import datetime
import pprint


BASE_URL = 'http://interview.agileengine.com'
API_KEY = '23567b218376f79d9415'
UPDATE_INTERVAL = 600  # in seconds


class Images:
    def __init__(self):
        self.img_cache = {}
        self.update_time = None
        self.load_images()

    def get_token(self):
        r = requests.post(
            BASE_URL + '/auth',
            json={'apiKey': API_KEY}
        )
        self.token = r.json().get('token')

    def get_page(self, page_num=None):
        # get current page
        payload = {'page': page_num} if page_num else {}
        r = requests.get(
            BASE_URL + '/images',
            headers={'Authorization': 'Bearer ' + self.token},
            params=payload
        )
        # store page content to img_cache
        r = r.json()
        pictures = r.get('pictures')
        next_page = r.get('hasMore')
        for pic in pictures:
            self.img_cache[pic['id']] = {'cropped_picture': pic['cropped_picture']}
        # process next page if exists
        if next_page:
            page_num = page_num + 1 if page_num else 2
            self.get_page(page_num)

    def get_image_details(self):
        for img_id in self.img_cache:
            r = requests.get(
                BASE_URL + '/images/' + img_id,
                headers={'Authorization': 'Bearer ' + self.token}
            )
            r = r.json()
            del r['id']
            self.img_cache[img_id] = r

    def load_images(self):
        now = datetime.datetime.now()
        if self.update_time is None or (now - self.update_time).seconds > UPDATE_INTERVAL:
            self.img_cache = {}  # clear cache
            self.get_token()
            self.get_page()
            self.get_image_details()
            self.update_time = now


if __name__ == '__main__':
    imgs = Images()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(imgs.img_cache)
