import jieba
import jieba.posseg as pseg


def tokenize(fin_, fout_):
    passage = fin_.read().split('\n')
    del (passage[-1])
    i = 1
    for line in passage:
        print(i)
        i += 1
        msg = line.split('\t')
        res = []
        content = jieba.cut(msg[0])
        res.append("#".join(content))
        content = jieba.cut(msg[1])
        res.append("#".join(content))
        res.append(msg[2])
        fout_.write("\t".join(res) + '\n')


def remove_stop_word(fin_, fout_):
    left = ['x', 'zg', 'uj', 'ul', 'e', 'd', 'uz', 'y']
    passage = fin_.read().split('\n')
    del (passage[-1])
    i = 1
    for line in passage:
        print(i)
        i += 1
        msg = line.split('\t')
        res = []
        su = []
        content = pseg.cut(msg[0])
        for word, flag in content:
            if flag not in left:
                res.append(word)
        su.append(' '.join(res))
        res = []
        content = pseg.cut(msg[1])
        for word, flag in content:
            if flag not in left:
                res.append(word)
        su.append(' '.join(res))
        su.append(msg[2])
        fout_.write('\t'.join(su)+'\n')
