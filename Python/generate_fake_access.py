import numpy as np
from urllib import urlopen

def get_headers():
    headers = { "User-Agent" :  "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)" }
    return headers
    
def get_response(url):
    headers = get_headers()
    response = urlopen(url, None, headers)
    return response

def get_soup(response):
    return BeautifulSoup.BeautifulSoup(response)

def get_title(soup):
    return soup.title.string

def get_fake_data():
    fake_topics = open("data/fake_topics.txt", "r").read().split("\n")
    user_num = 200
    fake_data = []
    for i in range(user_num):
        user_id = np.random.randint(1000)
        for j in range(np.random.randint(10)):
            url = np.random.choice(fake_topics)
            fake_data.append([user_id, url])
    return fake_data

def make_request(data):
    wiki_url = "https://ja.wikipedia.org/wiki/%s"
    url = "http://localhost:8000/cgi-bin/sample_1.py?uid=%s&ac_url=%s"
    return [url % (d[0], wiki_url % d[1]) for d in data]

data = get_fake_data()
request = make_request(data)
for r in request:
    response = get_response(r)
