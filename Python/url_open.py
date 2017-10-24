"""
Access to the page of the url and get its title or entire sentences
to generate tags, and another program generates the url's features from them.
"""

from urllib import urlopen
import BeautifulSoup

def __get_sample_url():
    sample_url = "https://ja.wikipedia.org/wiki/クレープ"
    return sample_url

def __test_sample_url_code():
    sample_url = __get_sample_url()
    print sample_url

def __get_html(response):
    html = response.read()
    return html

def __write_html(html, name="sample"):
    path = "out/"
    open(path + name + ".html", "w").write(html)

def get_headers():
    headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    return headers

def get_response(url):
    headers = get_headers()
    response = urlopen(url, None, headers)
    return response

def get_soup(response):
    return BeautifulSoup.BeautifulSoup(response)

def get_title(soup):
    return soup.title.string

def __sample_headder_getter():
    url = __get_sample_url()
    response = get_response(url)
    soup = BeautifulSoup.BeautifulSoup(response)
    print soup.title.string
