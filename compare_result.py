import os
import numpy as np
import openpyxl
import pickle

excel_path = '12d_array_result\\result3\\Copy of GELCODES_SIFE_Oct20.xlsx'
result_path = '12d_array_result\\result3\\result_ver2.txt'
final_result_path = '12d_array_result\\result3\\result_after_comparison_ver2.txt'

uncertain_info1 = []
uncertain_info2 = []
correct_answer = {}
data_generated = {}
answerkey = {
    "DIFN" : "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]",
    "DGK" : "[1. 1. 0. 0. 0. 0. 0. 1. 0. 0. 1. 0.]",
    "DGL" : "[1. 0. 1. 0. 0. 0. 0. 1. 0. 0. 0. 1.]",
    "DAK" : "[1. 0. 0. 1. 0. 0. 0. 0. 1. 0. 1. 0.]",
    "DAL" : "[1. 0. 0. 0. 1. 0. 0. 0. 1. 0. 0. 1.]",
    "DMK" : "[1. 0. 0. 0. 0. 1. 0. 0. 0. 1. 1. 0.]",
    "DML" : "[1. 0. 0. 0. 0. 0. 1. 0. 0. 1. 0. 1.]",
    "DFK" : "[1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]",
    "DFL" : "[1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]",
    "IgG HC" : "[1. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]",
    "IGM HC" : "[1. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]",
}

answerkey_array = {
    "DIFN" : [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,],
    "DGK" : [1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0.,],
    "DGL" : [1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 1.,],
    "DAK" : [1., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0.,],
    "DAL" : [1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1.,],
    "DMK" : [1., 0., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0.,],
    "DML" : [1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1.,],
    "DFK" : [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,],
    "DFL" : [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,],
    "IgG HC" : [1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,],
    "IGM HC" : [1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,],
}



def extract_info_from_excel(file_location):
    wb = openpyxl.load_workbook(file_location)
    ws = wb['Sheet1']
    for col in ws.iter_rows(min_row=3, max_row=191, min_col=2, max_col=3, values_only=True):      
        correct_answer[col[0]] = col[1]
    
    
def extract_data_from_resulttxt(file_location):
    result_file = open(file_location, 'r')
    lines = result_file.readlines()
    for line in lines:
        if not line.strip():
            continue
        label = line[7:11]
        result = line[16:].strip()
        data_generated[label] = result
        #print(line == answerkey['DIFN'])
    result_file.close()
    
    
def compare_result():
    c_answer_index, data_value = 0, 0
    tcount, uncertain, correct, wrong = 0, 0, 0, 0
    final_result_file = open(final_result_path, 'a')
    for c_answer_index in correct_answer:
        c_answer_value = correct_answer.get(c_answer_index) #find value through key
        answerkey_value = answerkey.get(c_answer_value) #find the array of the correct answer
        if answerkey_value == None:
            uncertain += 1
            # the label from the correct answer key is too complicated, so it does not match with our label
            uncertain_info1.append("Label not matched: "+str(c_answer_index)+"\tLabel: "+c_answer_value)
            continue
        data_value = data_generated.get(str(c_answer_index))
        if data_value == None:
            uncertain += 1
            # the image in the correct answer key does not match any of our image
            uncertain_info2.append("Image not found in our data: "+str(c_answer_index)+"\tLabel: "+c_answer_value)
            continue
        if data_value == answerkey_value:
            correct += 1
        else:
            wrong += 1
            # result is different
            final_result_file.write("Incorrect: "+str(c_answer_index)+"\tLabel: "+c_answer_value+"\t"+answerkey_value+"\tOur value: "+data_value+"\n")
        tcount += 1
    for message in uncertain_info1:
        final_result_file.write(message+"\n")
    for message in uncertain_info2:
        final_result_file.write(message+"\n")
    final_result_file.write("\nTotal (exlcude uncertain ones): "+str(tcount)+"\n")
    final_result_file.write("Correct: "+str(correct)+"\n")
    final_result_file.write("Wrong: "+str(wrong)+"\n")
    final_result_file.write("Uncertain: "+str(uncertain)+"\n")
    final_result_file.close()

def store_label():
    index_file = open('features\\features1_answerkeys\\answerkey_index.pkl', 'wb')
    key_file = open('features\\features1_answerkeys\\answerkey_value.pkl', 'wb')
    answer_index = []
    answer_array_list = []
    for c_answer_index in correct_answer:
        answer_index.append(c_answer_index)
        c_answer_value = correct_answer.get(c_answer_index)
        answerkey_value = answerkey.get(c_answer_value)
        ansarray_value = answerkey_array.get(c_answer_value)
        if answerkey_value == None:
            ansarray_value = [1.] * 12
        answer_array_list.append(ansarray_value)
    answer_index = np.array(answer_index)
    answer_array_list = np.array(answer_array_list)
    pickle.dump(answer_index, index_file)
    pickle.dump(answer_array_list, key_file)

if __name__ == "__main__":
    """extract_info_from_excel(excel_path)
    extract_data_from_resulttxt(result_path)
    compare_result()"""

    extract_info_from_excel(excel_path)
    store_label()
    
    
