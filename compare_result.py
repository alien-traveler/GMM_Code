import os
import numpy as np
import openpyxl

excel_path = '12d_array_result\\result3\\Copy of GELCODES_SIFE_Oct20.xlsx'
result_path = '12d_array_result\\result3\\result.txt'

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

def extract_info_from_excel(file_location):
    wb = openpyxl.load_workbook(file_location)
    ws = wb['Sheet1']
    for col in ws.iter_rows(min_row=3, max_row=193, min_col=2, max_col=3, values_only=True):      
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
    
    
#def compare_result(file_location):
    

if __name__ == "__main__":
    extract_info_from_excel(excel_path)
    extract_data_from_resulttxt(result_path)
