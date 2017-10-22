import numpy as np
from datetime import datetime

class UserDatabase:
    class Table:
        URL_IDX = ""
        DATE = ""

    class Keys:
        URL_HISTORY = "url_history"
        IDX = "idx"

    def __init__(self):
        self.database = {}
        self.idx_to_user = {}
        self.user_num = 0
        self.matrix = np.array([[0]])

    def update_matrix(self, userid, url_idx): # TODO: use sparse vector
        user_idx = self.ch_userid_to_idx(userid)
        if user_idx >= self.matrix.shape[0]:
            self.matrix = np.r_[self.matrix, [np.zeros(self.matrix.shape[1])]]
        if url_idx >= self.matrix.shape[1]:
            self.matrix = np.c_[self.matrix, np.zeros(self.matrix.shape[0])]
        self.matrix[user_idx][url_idx] = 1
        print self.matrix

    def push(self, userid, url_idx):
        if not userid in self.database:
            self.__add_new_user(userid)
        self.__add_hist(userid, url_idx)
        self.update_matrix(userid, url_idx)

    def __add_new_user(self, userid):
        self.database[userid] = {}
        self.database[userid][self.Keys.URL_HISTORY] = []
        self.database[userid][self.Keys.IDX] = self.user_num
        self.idx_to_user[self.user_num] = userid
        self.user_num += 1

    def __add_hist(self, userid, url_idx):
        table = self.Table()
        table.URL_IDX = url_idx
        table.DATE = datetime.now()
        self.database[userid][self.Keys.URL_HISTORY].append(table)

    def __show_date(self, table):
        print table.DATE.strftime("%Y/%m/%d %H:%M:%S")
        
    def ch_userid_to_idx(self, userid):
        return self.database[userid][self.Keys.IDX]

    def ch_idx_to_userid(self, user_idx):
        return self.idx_to_user[user_idx]
      
    def show_database(self, site_database=None):
        for userid in sorted(self.database.keys()):
            print userid
            for table in self.database[userid][self.Keys.URL_HISTORY]:
                date = table.DATE.strftime("%Y/%m/%d %H:%M:%S")
                url_idx = table.URL_IDX
                url_info = url_idx
                if not site_database is None:
                    url_info = site_database.ch_idx_to_url(url_idx)
                print "%s: %s" % (date, url_info)
            print ""
