def read_data(file_name):
    sentence_list = []
    with open(file_name,"r",encoding="UTF-8") as rd:
        for line in rd:
            sentence_list.append(line.strip())
    return sentence_list

if __name__ == "__main__":
    file_name = "Data.txt"
    ss_list = read_data(file_name)
    print(ss_list)

