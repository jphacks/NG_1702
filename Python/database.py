from site_database import  SiteDatabase
from user_database import  UserDatabase

class Database:
    def __init__(self):
        self.user_database = UserDatabase()
        self.site_database = SiteDatabase()

    def push(self, userid, url):
        self.site_database.push(url)
        url_idx = self.site_database.ch_url_to_idx(url)
        self.user_database.push(userid, url_idx)
