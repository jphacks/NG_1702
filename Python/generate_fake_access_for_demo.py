"""
Generate fake access to the server for the demonstration.
This is slow cas the communication program has delay times.
Use generate_fake_database_for_demo.py
"""

from urllib import urlopen

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

def get_fake_data():
    user_num = 20
    fake_data = []
    for user_id in range(1, user_num):
        if user_id == 1:
            continue
        for url in range(3 * (user_id % 3), 3 * (user_id % 3) + 3):
            fake_data.append([user_id, url + 1])
    return fake_data

def make_request(data):
    url = "http://localhost:8000/cgi-bin/sample_1.py?uid=%s&ac_url=%s"
    return [url % (d[0], d[1]) for d in data]

if __name__ == '__main__':
    data = get_fake_data()
    request = make_request(data)
    for r in request:
        response = get_response(r)
