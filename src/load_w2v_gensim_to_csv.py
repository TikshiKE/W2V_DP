import gensim
from gensim.models import KeyedVectors

location = "GoogleNews-vectors-negative300.bin.gz"
wv = KeyedVectors.load_word2vec_format(location, binary=True, limit=1000000)
wv.save_word2vec_format('vectors.csv')

