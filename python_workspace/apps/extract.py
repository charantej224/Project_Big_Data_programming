import re

tempTxt = ""
# Open if file exists/Create a file to append data
txt = open('Writetweetsdata.txt', 'a+')

with open('Writetweetsdata.csv', newline='') as csvfile:
    for line in csvfile:
        tempTxt = ""
        extractedData = re.findall(r'[#@][^\s#@]+', line)
        extractedData += re.findall("(?P<url>https?://[^\s]+)", line)
        print("extracting under process")
        for data in extractedData:
            tempTxt += " " + data
            txt.write(tempTxt)

print("Sucessfully extracted")
# close file
txt.close()
