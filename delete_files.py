import os

path = 'curve\\curve3\\'
main_folder = os.listdir(path)

for folder in main_folder:
    folder_location = os.path.join(path, folder)
    #second_folder = os.listdir(folder_location)
    for i in range(9):
        potential_file_location = folder_location + '\\' + str(i) + '.jpg'
        if os.path.exists(potential_file_location):
            os.remove(potential_file_location)
            
        
    