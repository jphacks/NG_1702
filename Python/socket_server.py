"""
With socket, communicate with a program which handle request from a server.
Run this with the server program.
"""

import socket
from database_manager import DatabaseManager
from generate_fake_database_for_demo import gen_fake_database

def socket_work(database_manager, host='127.0.0.1', port=50007):
    """
    Communicats and returns results for ever.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        print 'Connected by %s' % str(addr)
        uid, ac_url = conn.recv(1024).split(',')
        res = database_manager.request({'uid':uid, 'ac_url':ac_url})
        if not res is None:
            conn.send(res)
        else:
            fake_url = 'https://en.wikipedia.org/wiki/Crepe' # TODO
            conn.send(fake_url)
        conn.close()
        database_manager.show_database()

if __name__ == '__main__':
    database_manager = DatabaseManager()
    gen_fake_database(database_manager)
    socket_work(database_manager)
