import jieba


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
