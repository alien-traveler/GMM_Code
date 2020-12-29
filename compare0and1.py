import os

path = "12d_array_result\\result3\\result_after_comparison.txt"


def compare0and1(filepath):
    number1_in_correct_label, number1_in_our_result = 0, 0
    resultfile = open(filepath, 'r')
    for i in range(92):
        line = resultfile.readline()
        correct_label_section = line[28:64]
        number1_in_correct_label += correct_label_section.count("1")
        our_result_section = line[77:113]
        number1_in_our_result += our_result_section.count("1")
    print("correct 1s: " + str(number1_in_correct_label))
    print("our 1s: " + str(number1_in_our_result))

if __name__ == "__main__":
    compare0and1(path)