import os
import numpy as np


result_path = '12d_array_result\\result3\\result.txt'

answerkey = {
    "DIFN" : "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]",
    "DGK" : "[1. 1. 0. 0. 0. 0. 0. 1. 0. 0. 1. 0.]",
}



if __name__ == "__main__":
    result_file = open(result_path, 'r')
    
    while True:
        line = result_file.readline()
        
        if not line.strip():
            continue
        line = line[13:].strip()
        print(line == answerkey['DIFN'])
        
        break
