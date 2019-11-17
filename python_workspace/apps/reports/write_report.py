class WriteReport:
    def __init__(self, input_list, predicted_list):
        self.input_list = input_list
        self.predicted_list = predicted_list
        self.positive = 0
        self.negative = 0
        self.neutral = 0
        self.length = 0

    def write_file(self):
        f = open("report.txt", "w")
        self.length = len(self.input_list)
        for i in range(self.length):
            if self.predicted_list[i] == 0:
                response = "Negative"
                self.negative += 1
            elif self.predicted_list[i] == 1:
                response = "Neutral"
                self.neutral += 1
            else:
                response = "Positive"
                self.positive += 1
            f.write(self.input_list[i] + " : predicted : " + response + "\n")
        f.write("\nPositive Percentage : " + str((self.positive / self.length) * 100))
        f.write("\nNegative Percentage : " + str((self.negative / self.length) * 100))
        f.write("\nNeutral Percentage : " + str((self.neutral / self.length) * 100))
        f.close()
