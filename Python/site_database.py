"""
Database for site information.
See database_manager.py
"""

def get_tags(url):
    """
    Return tags generated from url as recommend.
    Here, recommendation generation model will be called.
    """
    return ["sample_tag_0", "sample_tag_1"]

class SiteDatabase(object):
    """
    Hold names of urls themself and tags extracted from those pages.
    """
    class Keys(object):
        TAGS = "tags"
        FREQUENCY = "frequency"
        IDX = "idx"

    def __init__(self):
        self.database = {}
        self.idx_to_url = {}
        self.url_num = 0

    def push(self, url):
        if not url in self.database:
            self.__add_new_url(url)
        else:
            self.__succ_frequency(url)

    def __add_new_url(self, url):
        self.database[url] = {}
        self.database[url][self.Keys.TAGS] = self.get_tags(url)
        self.__succ_frequency(url)
        self.database[url][self.Keys.IDX] = self.url_num
        self.idx_to_url[self.url_num] = url
        self.url_num += 1

    def get_tags(self, url):
        tags = get_tags(url)
        return tags

    def __succ_frequency(self, url):
        """
        Increment the visits time of the url.
        """
        fq = self.Keys.FREQUENCY
        if fq in self.database[url]:
            self.database[url][self.Keys.FREQUENCY] += 1
        else:
            self.database[url][self.Keys.FREQUENCY] = 1

    def __show_tags(self, url):
        tags = self.database[url][self.Keys.TAGS]
        print ", ".join(tags)

    def __show_freq(self, url):
        freq = self.database[url][self.Keys.FREQUENCY]
        tense = "" if freq == 1 else "s"
        print "(%s time%s accessed)" % (freq, tense)

    def ch_url_to_idx(self, url):
        return self.database[url][self.Keys.IDX]

    def ch_idx_to_url(self, url_idx):
        return self.idx_to_url[url_idx]

    def show_database(self):
        for k in sorted(self.database.keys()):
            print k
            self.__show_tags(k)
            self.__show_freq(k)
            print ""
