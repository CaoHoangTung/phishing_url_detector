import requets 

def check_shorten(url):
    while True:
        yield url
        r = requests.head(url)
        # detect rediret
        if 300 < r.status_code < 400:
            url = r.headers['location']
            return 0 
        else:
            return -1

url = 'shorturl.at/BPQT8'
# http://bit.ly/2C72XrW
check_shorten(url)