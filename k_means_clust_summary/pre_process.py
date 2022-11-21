import numpy as np
import underthesea
import pickle
from gensim.models import KeyedVectors

def get_contents(path):
    filepath = open(path, 'rb')
    contents = pickle.load(filepath)
    contents_parsed = []
    for content in contents:
        contents_parsed.append(content.lower())
    return contents_parsed


def tokenize(path):
    sents_list = []
    contents = get_contents(path)[0]
    for sentence in underthesea.sent_tokenize(contents):
        wordlist = []
        for word in underthesea.word_tokenize(sentence):
            wordlist.append(word)
        sents_list.append(wordlist)
    return sents_list

def change2vec(path):

file = '/home/code/NLP/summary_text/Vietnamese_doc_summarization_basic/neg.pkl'