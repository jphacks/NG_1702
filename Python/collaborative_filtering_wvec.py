"""
Just calculate cos similarities.
Load vectors generated from wvec model.
"""

import numpy as np

def load_url_feats(path="url_feats.npy"):
    return np.load(path)

def load_keys(path="url_keys.npy"):
    return np.load(path)

def sample_table(table, num):
    if num >= table.shape[0]:
        return table
    sample_idx = np.arange(num)
    np.random.shuffle(sample_idx)
    sampled_table = table[sample_idx]
    return sampled_table

def recommendation_wordvec(target_url_idx, top_k, sample_num=10):
    feats = load_url_feats()
    target_feats = feats[target_url_idx]
    sampled_feats = sample_table(feats, sample_num)
    matched_result = (sampled_feats * target_feats).sum(1)
    matched_url = matched_result.argsort()[::-1][:top_k]
    recommended_items = list(set(matched_url) - set([target_url_idx]))
    return recommended_items
