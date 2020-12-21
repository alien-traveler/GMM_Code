import os
import numpy as np
import openpyxl

excel_path = '12d_array_result\\result3\\Copy of GELCODES_SIFE_Oct20.xlsx'
result_path = '12d_array_result\\result3\\result.txt'

correct_answer = {}

answerkey = {
    "DIFN" : "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]",
    "DGK" : "[1. 1. 0. 0. 0. 0. 0. 1. 0. 0. 1. 0.]",
}

def extract_info_from_excel(file_location):
    wb = openpyxl.load_workbook(file_location)
    ws = wb['Sheet1']
    for col in ws.iter_rows(min_row=3, max_row=193, min_col=2, max_col=3, values_only=True):      
        correct_answer[col[0]] = col[1]
    print(correct_answer)
    

def compare_result(file_location):
    result_file = open(file_location, 'r')
    
    while True:
        line = result_file.readline()
        
        if not line.strip():
            continue
        line = line[13:].strip()
        print(line == answerkey['DIFN'])
        
        break

if __name__ == "__main__":
    extract_info_from_excel(excel_path)
