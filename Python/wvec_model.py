import tensorflow as tf
import numpy as np

def add_train_data(self, url, tags):
    print "update_tags"

def push(url, tags):
    self.add_train_data(url, tags)
    
def train_wvec():
    print "train_wvec"

class Model:
    def __init__(self, vocab_size, dim_embed):
        self.vocab_size = vocab_size
        self.dim_embed = dim_embed
        self.embeddings = tf.Variable(tf.random_uniform([vocab_size, dim_embed], -1.0, 1.0), name='embeddings')

    def build_model(self):
        x = tf.placeholder(tf.int64, [None, 2])
        emb = tf.nn.embedding_lookup(self.embeddings, x)
        self.loss = -tf.reduce_mean(tf.dot(emb[0], emb[1])) / tf.get_shape(x)[0] + tf.nn.l2_loss(emb)
