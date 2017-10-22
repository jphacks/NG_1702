import socket
import threading
import time
import datetime
from database import Database
import collaborative_filtering_simple as cf
from generate_fake_database_for_demo import gen_fake_database

HOST = '127.0.0.1'
PORT = 50007
 
def socket_work(database_manager):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
 
    while True:
        conn, addr = sock.accept()
        print 'Connected by %s' % str(addr)
        uid, ac_url = conn.recv(1024).split(",")
        res = database_manager.request({"uid":uid, "ac_url":ac_url})
        if not res is None:
            conn.send(res)
        else:
            fake_url = "https://en.wikipedia.org/wiki/Crepe" # TODO
            conn.send(fake_url)
        conn.close()
        database_manager.show_database()

class DatabaseManager:
    def __init__(self):
        self.database = Database()

    def request(self, data):
        if data["ac_url"] == "":
            if self.has_userid(data["uid"]):
                return self.get_reccomend(data["uid"])
            return None
        else:
            self.push(data)
            return None

    def get_reccomend(self, userid):
        target_user_idx = self.ch_userid_to_idx(userid)
        recommended_items_idx = cf.simple_recommendation_binary(self.matrix(), target_user_idx, top_k=3, sample_num=100)
        recommended_items = [self.ch_idx_to_url(i) for i in recommended_items_idx]
        return ", ".join(recommended_items)

    def push(self, data):
        self.database.push(data["uid"], data["ac_url"])

    def show_database(self):
        self.database.user_database.show_database()

    def ch_userid_to_idx(self, userid):
        return self.database.user_database.ch_userid_to_idx(userid)

    def ch_idx_to_url(self, idx):
        return self.database.site_database.ch_idx_to_url(idx)

    def matrix(self):
        return self.database.user_database.matrix

    def has_userid(self, userid):
        return userid in self.database.user_database.database

if __name__ == '__main__':
    database_manager = DatabaseManager()
    gen_fake_database(database_manager)
    socket_work(database_manager)
