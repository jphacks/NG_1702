"""
This communicates with the server (thru cgi) and recommendation program (with socket).
Dir tree:
server_1
    - cgi-bin
        - sample.py (this)
Run below in the dir /server_1.
    python -m CGIHTTPServer 8000
Access like these from the server.
    # to request to add history
    http://localhost:8000/cgi-bin/sample_1.py?uid=123&ac_url=456
    # to get recommends
    http://localhost:8000/cgi-bin/sample_1.py?uid=123
"""

import cgi
import socket
import datetime
import json

def get_html_body():
    html_body = """
    <html><body>
    <p>
    {0.year:d}/{0.month:d}/{0.day:d} {0.hour:d}:{0.minute:d}:{0.second:d}
    </p>
    <p>
    uid = %s
    <br>
    ac_url = %s
    </p>
    </body></html>"""
    return html_body

if __name__ == '__main__':
    show_html = False

    form = cgi.FieldStorage()
    uid = form.getvalue('uid', "")
    ac_url = form.getvalue('ac_url', "")
    send_data = ",".join([uid, ac_url])

    print "Content-type: text/html\n"

    if show_html:
        html_body = get_html_body()
        now = datetime.datetime.now()
        print (html_body % (uid, ac_url)).format(now)

    HOST = '127.0.0.1'
    PORT = 50007
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send(send_data)
    if ac_url == "":
        data = sock.recv(1024)
        if show_html:
            print data
        else:
            jsn = json.dumps({i:v for i, v in enumerate(data.split(","))})
            print jsn
    sock.close()
