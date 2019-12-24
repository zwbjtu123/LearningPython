import jieba
from ReadData import read_data
from WriteData import write_data

def cut(data_list):
    cut_data_list = []
    for s in data_list:
        word_list = jieba.lcut(s)
        cut_data_list.append("/".join(word_list))
        print(s)
        print(word_list)
    return cut_data_list

def main(file_name,output_name):
    data_list = read_data(file_name)
    write_data(cut(data_list), output_name)


if __name__ == "__main__":
    main("NLPTest/Data.txt", "NLPTest/Data2.txt")