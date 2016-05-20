import qzliu_util as qzl
import sys


def list_to_dict(l):
    cnt=0
    word2idx={}
    idx2word={}
    for word in l:
        word2idx[word]=cnt
        idx2word[cnt]=word
        cnt+=1
    return word2idx,idx2word
if __name__=='__main__'
