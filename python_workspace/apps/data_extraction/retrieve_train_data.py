def train_data():
    f = open("/tmp/part-r-00000", "r")
    write_file = open("data_set/train_data.csv", "w")
    write_file.write("comment,sentiment\n")
    i = 0
    while i < 20000:
        line = f.readline()
        split = line.split(",")
        if len(split) == 7:
            feature = split[5]
            if int(split[6]) < 0:
                feature += ",0"
            elif int(split[6]) > 0:
                feature += ",2"
            else:
                feature += ",1"

        write_file.write(feature+"\n")
        i += 1


train_data()
