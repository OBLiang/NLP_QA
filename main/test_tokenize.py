import jieba
if __name__ == '__main__':
    fw = open('develop.data', 'w')
    with open('/home/makeztc/Documents/NLP/data/develop.data', 'r') as f:
        passage = f.read().split('\n')
        del(passage[-1])
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
            fw.write("\t".join(res)+'\n')
    fw.close()
