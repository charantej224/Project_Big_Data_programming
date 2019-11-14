tempTxt = ""
# Open if file exists/Create a file to append data
txt = open('Writetweetsdata.txt', 'a+')

with open('Writetweetsdata.csv', newline='') as csvfile:
    for line in csvfile:
        if len(line.split(",")) == 6:
            txt.write(line)
        else:
            print(line + "\n" + str(len(line.split(','))))

txt.close()
