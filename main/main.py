import os
import argparse
from tokenize import tokenize
from tokenize import remove_stop_word


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A QA system of NLP")
    parser.add_argument("--train", dest="train_filename", type=str, default="train.data",
                        help="Input the name of the file that you want to operate.\n"
                             "IT MUST IN THE FILE OF FOLDER NAME DATA!!!")
    parser.add_argument("--method", dest="method", type=int, default=0,
                        help="Input one number to do something\n"
                             "0: quit\n"
                             "1: tokenize one file\n"
                             "2: remove stop word\n")
    args = parser.parse_args()
    data_path = os.path.abspath('.') + '/data/'
    if args.method == 0:
        pass
    elif args.method == 1:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path+args.train_filename
            output_file_name = data_path+args.train_filename.split(".")[0]+"_tokenize.data"
            with open(input_file_name, "r") as fin:
                with open(output_file_name, "w") as fout:
                    tokenize(fin, fout)
    elif args.method == 2:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path+args.train_filename
            output_file_name = data_path+args.train_filename.split(".")[0]+"_remove_stop_word.data"
            with open(input_file_name, "r") as fin:
                with open(output_file_name, "w") as fout:
                    remove_stop_word(fin, fout)
