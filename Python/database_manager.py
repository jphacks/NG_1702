"""
Construct databases for site and user.
Site database will be include site information,
such as index for management, and words extracted from title or its page's entire sentence.
User database includes user information,
such as index, and history user visited (url and date).
DatabaseManager make a instance of Database, so DatabaseManager is used in other programs.
"""

from site_database import  SiteDatabase
from user_database import  UserDatabase
import collaborative_filtering_simple as cf

class Database(object):
    """
    Handle both database.
    """
    def __init__(self):
        self.user_database = UserDatabase()
        self.site_database = SiteDatabase()

    def push(self, userid, url):
        """
        Push data to databases.
        """
        self.site_database.push(url)
        url_idx = self.site_database.ch_url_to_idx(url)
        self.user_database.push(userid, url_idx)

class DatabaseManager(object):
    """
    Handle both database.
    """
    def __init__(self):
        self.database = Database()

    def request(self, data):
        """
        Read requests from server.
        If ac_url is empty, return reccomends for the user.
        else push ac_url to the user's history.
        """
        if data["ac_url"] == "":
            if self.has_userid(data["uid"]):
                return self.get_reccomend(data["uid"])
            return None
        else:
            self.push(data)
            return None

    def get_reccomend(self, userid):
        """
        Return recommended urls.
        """
        target_user_idx = self.ch_userid_to_idx(userid)
        recommended_items_idx = cf.simple_recommendation_binary(self.matrix(),
                                                                target_user_idx,
                                                                top_k=3,
                                                                sample_num=100)
        recommended_items = [self.ch_idx_to_url(i) for i in recommended_items_idx]
        return ", ".join(recommended_items)

    def push(self, data):
        """
        Push ac_url to the user's history who's id is uid.
        """
        self.database.push(data["uid"], data["ac_url"])

    def show_database(self):
        """
        Will show databases contents.
        """
        self.database.user_database.show_database()

    def ch_userid_to_idx(self, userid):
        """
        Convert a user's id to its index.
        """
        return self.database.user_database.ch_userid_to_idx(userid)

    def ch_idx_to_url(self, idx):
        """
        Convert a user's index to its id.
        """
        return self.database.site_database.ch_idx_to_url(idx)

    def matrix(self):
        """
        Return the features.
        """
        return self.database.user_database.matrix

    def has_userid(self, userid):
        """
        Return userid is a new user or not.
        """
        return userid in self.database.user_database.database
