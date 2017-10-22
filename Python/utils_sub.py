# -*- coding: utf-8 -*-

def __get_sample_url():
    sample_url = "https://ja.wikipedia.org/wiki/クレープ"
    return sample_url

def __get_sample_userid():
    sample_userid = "123456"
    return sample_userid

def __get_sample_data():
    return __get_sample_url(), __get_sample_userid()

def __get_sample_tags():
    sample_tags = ["クレープ", "スイーツ"]
    return sample_tags

def __generate_fake_freq_table(num_user=10, num_obj=30):
    max_freq = 5
    table = np.random.randint(0,
            max_freq,
            num_user * num_obj
            ).reshape([num_user, num_obj])
    return table

def __generate_fake_binary_table(num_user=10, num_obj=30):
    table = np.random.randint(0,
            2,
            num_user * num_obj
            ).reshape([num_user, num_obj])
    return table

def __get_random_sample_url():
    sample_url = "https://example.com/%s" % np.random.randint(1000)
    return sample_url

def __get_random_sample_userid(max_user_num=1000):
    sample_userid = "id" + ("000" + str(np.random.randint(max_user_num)))[-len(str(max_user_num)):]
    return sample_userid

def __get_random_sample_data():
    return __get_random_sample_url(), __get_random_sample_userid()


def __sample_site_database_action():
    user_database = UserDatabase()
    site_database = SiteDatabase()

    url, userid = __get_sample_data()
    site_database.push(url)
    url_idx = site_database.ch_url_to_idx(url)

    for i in range(2):
        user_database.push(userid, url_idx)
        user_database.show_database(site_database)

def __sample_user_database_action():
    site_database = SiteDatabase()
    url = __get_sample_url()
    for i in range(2):
        site_database.push(url)
        site_database.show_database()

def __sample_database_action():
    from database import Database
    database = Database()
    for i in range(10):
        userid = __get_random_sample_userid()
        for j in range(10):
            url = __get_random_sample_url()
            database.push(userid, url)

def __sample_simple_recommendation_binary():
    table = __generate_fake_binary_table(4, 6)
    target_user_id = 1
    top_k = 3
    recommended_items = simple_recommendation_binary(table, target_user_id, top_k)
    print target_user_id
    print table
    print recommended_items
