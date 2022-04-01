import requests
import browsercookie

def cookiesR():

    cj = browsercookie.chrome()
    r = requests.get('www.bitbucket.com', cookies=cj)
    get_title(r.content)

