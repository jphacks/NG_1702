"""
Calculate similarity of vectors between a target user and others.
The feature vector consist of user url histori and Cos sim is used for similarity.
When user1 have visited url1 and url2, and the others have visited some of those and url3 so far,
then the vector is represented as follows.
user1 [1, 1, 0]
user2 [1, 0, 1]
user3 [0, 1, 1]
...
When a user visits a new site, then new column will be added by the database,
same process runs for a new users.
Now, it's binary (visited or not) but weighted one by visits time is also ok.

Others vectors are sampled with uniform.
"""

import numpy as np

def normes(arr):
    """
    Return magnitudes of each row.
    """
    axis = 0 if arr.ndim == 1 else 1
    return np.power(np.power(arr, 2).sum(axis), 0.5)

def normed(arr):
    """
    Return normed vectors for each row.
    """
    axis = 0 if arr.ndim == 1 else 1
    return arr / np.expand_dims(normes(arr), axis)

def sample_table(table, num):
    """
    Samples from table to reduce calculation cost.
    """
    if num >= table.shape[0]:
        return table
    sample_idx = np.arange(num)
    np.random.shuffle(sample_idx)
    sampled_table = table[sample_idx]
    return sampled_table

def simple_recommendation_binary(table, target_user_idx, top_k, sample_num=100):
    """
    Simple collaborative filtering generation algorithm.
    Just calculate cos.
    """
    target_user_table = table[target_user_idx]
    normed_target_user_table = normed(target_user_table)
    sampled_table = sample_table(table, sample_num)
    normed_sampled_table = normed(sampled_table)
    matched_result = (normed_sampled_table * normed_target_user_table).sum(1)
    matched_users = matched_result.argsort()[::-1][:top_k]
    matched_users_table = sampled_table[matched_users]
    user_items = np.where(target_user_table != 0)[0]
    matched_users_items = np.where(matched_users_table != 0)[1]
    recommended_items = list(set(list(matched_users_items)) - set(list(user_items)))
    return recommended_items
