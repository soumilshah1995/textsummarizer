import requests
from bs4 import BeautifulSoup

class Metaclass(type):

    _instance ={}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(Metaclass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class Webcrawler(object):

    def __init__(self, text):
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',}
        self.url = 'https://resoomer.com/controllers/AjaxFrontControllers.php?action=sendText'
        self.text = text
        self.data = {
            "contentText": self.text,
            "langSite": "en",}

    def get(self):
        r = requests.post(url=self.url, headers=self.headers, data=self.data)
        return r

    def scrapper(self):
        """

        :return: String
        """
        r = self.get()
        soup = BeautifulSoup(r.text, 'html.parser')
        NewText = []

        for x in soup.find_all('div', id='conteneurTextAuto'):
            NewText.append(x.text)

        dd = ''.join(NewText)
        return dd


class TextSummarizer(metaclass=Metaclass):

    def __init__(self, text):

        """ Constructor """

        self.text = text
        self._crawler = Webcrawler(text=self.text)


    @property
    def get(self):
        """

        :return: String
        """
        data = self._crawler.scrapper()
        return data

# #
# if __name__ == "__main__":
#     text = """
#     The United States of America (USA), commonly known as the United States (U.S. or US) or simply America, is a country comprising 50 states, a federal district, five major self-governing territories, and various possessions.[i] At 3.8 million square miles (9.8 million km2), the United States is the world's third or fourth largest country by total area[d] and is slightly smaller than the entire continent of Europe. With a population of over 327 million people, the U.S. is the third most populous country. The capital is Washington, D.C., and the most populous city is New York City. Most of the country is located contiguously in North America between Canada and Mexico.
#
#     """
#     obj = TextSummarizer(text=text)
#     print(obj.get)
