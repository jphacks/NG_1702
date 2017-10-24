"""
Word Vector Model.
Use keywords extracted from sites pages.
"""
import tensorflow as tf

class Model(object):
    def __init__(self, vocab_size, dim_embed):
        self.vocab_size = vocab_size
        self.dim_embed = dim_embed
        self.embeddings = tf.Variable(tf.random_uniform([vocab_size, dim_embed],
                                                        -1.0,
                                                        1.0), name='embeddings')

    def build(self):
        """
        x: Pairs of words indexes.
        labels: 1 or -1, Represent the pair words are related or not.
        """
        x = tf.placeholder(tf.int64, [None, 2])
        labels = tf.placeholder(tf.int64, [None])
        emb = tf.nn.embedding_lookup(self.embeddings, x)
        w_sim = tf.reduce_mean(tf.multiply(emb[0], emb[1]))
        self.loss = w_sim * tf.cast(labels, tf.float32) + tf.nn.l2_loss(emb)
