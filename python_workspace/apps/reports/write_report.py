class WriteReport:
    def __init__(self, input_list, predicted_list):
        self.input_list = input_list
        self.predicted_list = predicted_list

    def write_file(self):
        f = open("report.txt", "w")
        for i in range(len(self.input_list)):
            f.write(self.input_list[i] + " : predicted" + self.predicted_list[i])
        f.close()
