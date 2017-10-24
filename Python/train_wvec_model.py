"""
Train wvec model.
"""

import numpy as np
import tensorflow as tf
from wvec_model import Model

def add_train_data(self, url, tags):
    print "update_tags"

def push(url, tags):
    add_train_data(url, tags)

def train_wvec():
    print "train_wvec"

def make_session(gpu_id='0', allow_growth=True):
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = allow_growth
    config.gpu_options.visible_device_list = gpu_id
    sess = tf.Session(config=config)
    sess.run(tf.global_variables_initializer())
    return sess

def build_model(cfg):
    np.random.seed(123)
    tf.set_random_seed(123)

    model = Model(cfg.vocab_size, cfg.dim_embed)
    model.build()
    train_op = tf.train.AdamOptimizer(cfg.learning_rate).minimize(mdl.loss)
    saver = tf.train.Saver(max_to_keep=cfg.max_to_keep)
    sess = make_session(cfg.gpu_id)
