import os, argparse
import tokenize_word
import word2vector
import logistic


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A QA system of NLP")
    parser.add_argument("--train", dest="train_filename", type=str, default="train.data",
                        help="Input the name of the file that you want to operate.\n"
                             "IT MUST IN THE FILE OF FOLDER NAME DATA!!!")
    parser.add_argument("--method", dest="method", type=int, default=0,
                        help="Input one number to do something\n"
                             "0: quit\n"
                             "1: tokenize_word one file\n"
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
                    tokenize_word.tokenize_word(fin, fout)
    elif args.method == 2:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path + args.train_filename
            output_file_name = data_path + args.train_filename.split(".")[0] + "_remove_stop_word.data"
            with open(input_file_name, "r") as fin:
                with open(output_file_name, "w") as fout:
                    tokenize_word.remove_stop_word(fin, fout)
    elif args.method == 3:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path + args.train_filename
            output_file_name = data_path + args.train_filename.split(".")[0] + "_remove_stop_word_and_ans.data"
            with open(input_file_name, "r") as fin:
                with open(output_file_name, "w") as fout:
                    tokenize_word.remove_stop_word_and_ans(fin, fout)
    elif args.method == 4:
        if args.train_filename == "":
            pass
        else:
            input_file_name = data_path + args.train_filename
            output_file_name = data_path + args.train_filename.split(".")[0] + ".model"
            word2vector.build_glossary(input_file_name, output_file_name)
    elif args.method == 5:
        model_name = data_path + 'training_remove_stop_word_and_ans.model'
        input_file_name = data_path + args.train_filename
        output_file_name = data_path + 'dev.data'
        word2vector.get_sentence_vector(model_name, input_file_name, output_file_name)
    elif args.method == 6:
        train_file = data_path + 'train.data'
        test_file = data_path + 'dev.data'
        result_file = data_path + 'score'
        logistic.train_model(train_file, test_file, result_file)
