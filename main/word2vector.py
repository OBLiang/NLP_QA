from gensim.models import word2vec, KeyedVectors
import numpy as np


def build_glossary(in_file_name, out_file_name):
    sentence = word2vec.Text8Corpus(in_file_name)
    model = word2vec.Word2Vec(sentence, size=150, min_count=1, window=5, sg=1)
    model.wv.save_word2vec_format(out_file_name)


def get_sentence_vector(model_name, in_file_name, out_file_name):
    model = KeyedVectors.load_word2vec_format(model_name)
    with open(in_file_name, 'r') as fin:
        with open(out_file_name, 'w') as fout:
            lines = fin.readlines()
            fuck = 0
            for line in lines:
                print(fuck)
                fuck += 1
                [question, answer, label] = line.split('\t')
                q_result = np.array([0]*150)
                a_result = np.array([0]*150)
                num_q = 0
                for q in question:
                    try:
                        q_list = model[q]
                        q_result = q_result+np.array(q_list)
                        num_q += 1
                    except:
                        continue
                if num_q != 0:
                    q_result = q_result/num_q
                num_a = 0
                for a in answer:
                    try:
                        a_list = model[a]
                        a_result = a_result + np.array(a_list)
                        num_a += 1
                    except:
                        continue
                if num_a != 0:
                    a_result = a_result/num_a
                q_result=q_result.reshape(1, 150)
                a_result=a_result.reshape(1, 150)
                dist = np.linalg.norm(a_result - q_result)
                dist = 1.0/(1.0+dist)
                num = float(np.dot(q_result, a_result.T))
                denom = np.linalg.norm(q_result)*np.linalg.norm(a_result)
                cos = num/denom
                cos = 0.5+0.5*cos
                fout.write(str(dist)+' '+str(cos)+' '+str(num_a-num_q)+' '+str(label))