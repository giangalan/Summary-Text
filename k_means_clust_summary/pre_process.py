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


def tokenize_1_content(path, index):
    sents_list = []
    contents = get_contents(path)[index]
    for sentence in underthesea.sent_tokenize(contents):
        wordlist = []
        for word in underthesea.word_tokenize(sentence):
            wordlist.append(word)
        sents_list.append(wordlist)
    return sents_list


# def change2vec(path):
<<<<<<< HEAD
#     X = []
#     for item in tokenize(path):
#         print(item)
#         input()
#         sent2vec = np.zeros(100)


file = '/home/code/NLP/Summary-Text/Vietnamese_doc_summarization_basic/neg.pkl'
tokenize(file)
print()
# change2vec(file)
=======

file = '/home/code/NLP/Summary-Text/Vietnamese_doc_summarization_basic/neg.pkl'


def write_data_2_txt(path, number):
    for i in range(0, number):
        data = tokenize_1_content(file, i)
        f = open('/home/code/NLP/Summary-Text/data.txt', "a+")
        for sent in data:
            for word in sent:
                # print(word)
                # print()
                f.writelines(word)
                f.writelines("\n")
            f.writelines("\n")
            # print()
        f.writelines("end\n")
        print("data[", i, "] finished")


write_data_2_txt(file, 3)
>>>>>>> 891bb662a2e7787d56da02af50b97c5369020bcf
