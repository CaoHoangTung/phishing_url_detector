import requests as req
import inspect

class Crawler():
    def get_html(url="http://abila.tk/fik"):
        r = req.get(url)
        # print(r.text)

        li = inspect.getmembers(r.history[0])
        for elem in li:
            print(elem)
    
Crawler.get_html()
        