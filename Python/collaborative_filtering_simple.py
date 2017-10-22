import numpy as np

def normes(arr):
    axis = 0 if arr.ndim == 1 else 1
    return np.power(np.power(arr, 2).sum(axis), 0.5)

def normed(arr):
    axis = 0 if arr.ndim == 1 else 1
    return arr / np.expand_dims(normes(arr), axis)

def sample_table(table, num):
    if num >= table.shape[0]:
        return table
    sample_idx = np.arange(num)
    np.random.shuffle(sample_idx)
    sampled_table = table[sample_idx]
    return sampled_table

def simple_recommendation_binary(table, target_user_idx, top_k, sample_num=100):
    target_user_table = table[target_user_idx]
    normed_target_user_table = normed(target_user_table)
    sampled_table = sample_table(table, sample_num)
    normed_sampled_table = normed(sampled_table)
    num_user_item_kind = target_user_table.sum()
    matched_result = (normed_sampled_table * normed_target_user_table).sum(1)
    matched_users = matched_result.argsort()[::-1][:top_k]
    matched_users_table = sampled_table[matched_users]
    user_items = np.where(target_user_table != 0)[0]
    matched_users_items = np.where(matched_users_table != 0)[1]
    recommended_items = list(set(list(matched_users_items)) - set(list(user_items)))
    return recommended_items
