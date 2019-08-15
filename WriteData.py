def write_data(data, output_file_name):
    with open(output_file_name,"w",encoding="utf-8") as wr:
        for s in data:
            wr.write(s + "\n")

if __name__ == "__main__":
    data = ['报道', '称', '，', '俄', '政府部门', '已', '将', '切帕', '的', '信函', '副本', '发送给', '政府', '有关', '部门', '及', '阿尔泰', '边疆区', '政府', '进行', '研究', '。']

    write_data(data, "test.txt")