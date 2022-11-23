from gensim.models import KeyedVectors
import sys
import io
import numpy as np


def load_vec(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    data = {}
    i = 0
    for line in fin:
        i += 1
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = np.array([float(val) for val in tokens[1:]])
        data[tokens[0]] /= np.linalg.norm(data[tokens[0]])
        if i > 10:
            break
    print(data)


load_vec('/home/code/NLP/Summary-Text/fasttext-vi/cc.vi.300.vec')
