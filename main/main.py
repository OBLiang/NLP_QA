import os
import argparse
from tokenize import tokenize
from tokenize import remove_stop_word
from tokenize import remove_stop_word_and_ans
from word2vector import build_glossary
from word2vector import get_sentence_vector
# from logistic import train_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A QA system of NLP")
    parser.add_argument("--train", dest="train_filename", type=str, default="train.data",
                        help="Input the name of the file that you want to operate.\n"
                             "IT MUST IN THE FILE OF FOLDER NAME DATA!!!")
    parser.add_argument("--method", dest="method", type=int, default=0,
                        help="Input one number to do something\n"
                             "0: quit\n"
                             "1: tokenize one file\n"
                             "2: remove stop word\n"
                             "3: get the QA file without answer\n"
                             "4: build glossary and get word vector\n")
    args = parser.parse_args()
    data_path = os.path.abspath('.') + '/data/'
    if args.method == 0:
        pass
    elif args.method == 1:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path + args.train_filename
            output_file_name = data_path + args.train_filename.split(".")[0] + "_tokenize.data"
            with open(input_file_name, "r") as fin:
                with open(output_file_name, "w") as fout:
                    tokenize(fin, fout)
    elif args.method == 2:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path + args.train_filename
            output_file_name = data_path + args.train_filename.split(".")[0] + "_remove_stop_word.data"
            with open(input_file_name, "r") as fin:
                with open(output_file_name, "w") as fout:
                    remove_stop_word(fin, fout)
    elif args.method == 3:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path + args.train_filename
            output_file_name = data_path + args.train_filename.split(".")[0] + "_remove_stop_word_and_ans.data"
            with open(input_file_name, "r") as fin:
                with open(output_file_name, "w") as fout:
                    remove_stop_word_and_ans(fin, fout)
    elif args.method == 4:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path + args.train_filename
            output_file_name = data_path + args.train_filename.split(".")[0] + ".model"
            build_glossary(input_file_name, output_file_name)
    elif args.method == 5:
        model_name = data_path + 'training_remove_stop_word_and_ans.model'
        input_file_name = data_path + args.train_filename
        output_file_name = data_path + 'dev.data'
        get_sentence_vector(model_name, input_file_name, output_file_name)
    elif args.method == 6:
        train_file = data_path + 'train.data'
        test_file = data_path + 'dev.data'
        result_file = data_path + 'score'
        # train_model(train_file, test_file, result_file)
