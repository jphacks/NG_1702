"""
Test to generate fake access to the server.
"""

from urllib import urlopen
import numpy as np
import BeautifulSoup

def get_headers():
    """
    Set headers to prevent denyings.
    """
    headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    return headers

def get_response(url):
    headers = get_headers()
    response = urlopen(url, None, headers)
    return response

def get_soup(response):
    return BeautifulSoup.BeautifulSoup(response)

def get_title(soup):
    """
    Returns title string of a page which has the url.
    """
    return soup.title.string

def get_fake_data():
    """
    Get pairs [user, url].
    """
    fake_topics = open("data/fake_topics.txt", "r").read().split("\n")
    user_num = 200
    fake_data = []
    for _ in range(user_num):
        user_id = np.random.randint(1000)
        for _ in range(np.random.randint(10)):
            url = np.random.choice(fake_topics)
            fake_data.append([user_id, url])
    return fake_data

def make_request(data):
    """
    Access to the server.
    """
    wiki_url = "https://ja.wikipedia.org/wiki/%s"
    url = "http://localhost:8000/cgi-bin/sample_1.py?uid=%s&ac_url=%s"
    return [url % (d[0], wiki_url % d[1]) for d in data]

if __name__ == '__main__':
    data = get_fake_data()
    request = make_request(data)
    for r in request:
        response = get_response(r)
