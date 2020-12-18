import os
from PIL import Image

# rename each img in the file 
def rename_img():
    path = 'new_test_pics/'

    i = 0
    for filename in os.listdir(path):
        os.rename(os.path.join(path, filename), os.path.join(path, 'captured'+str(i)+'.jpg'))
        i = i + 1

# crop gray block img
def crop_size():
    img = Image.open('faf8f9.png')
    box = (0,0,290,100) # we want 290*100
    cropped_image = img.crop(box)
    cropped_image.save('gray_block.png')

# resize img
def resize_img():
    image = Image.open('gray_block.png')
    new_img = image.resize((290, 100))
    new_img.save('large_gray_chunk.png')

# check img size 11.6.20
def check_size():
    path = 'new_test_pics/new_test_pics2/'
    for filename in os.listdir(path):
        image = Image.open(os.path.join(path, filename))
        print(image.size)

# create new folder dir
def create_new_folder_dir():
    path1 = 'new_test_pics\\new_test_pics2\\'
    path2 = 'after_change_pics\\after_change_pics3\\'
    #folder_name_list = []
    for filename in os.listdir(path1):
        #folder_name_list.append(filename)
        newpath = path2 + filename
        if not os.path.exists(newpath):
            os.makedirs(newpath)
    

# crop the image into the size we need
def crop_original_img(name, x1, y1):
    count = 0

    # x1, y1是首坐标，在函数被调用前修改，函数内部不能修改
    

    #xi, xf, yi, yf是每一张小图的斜对角坐标, 函数内move on切图时会改变
    x2 = x1 + 1400
    xi, xf = x1, x2
    yi = y1        # y的首坐标
    yf = yi + 910   # y的初始坐标
    imgname = name + ".jpg"
    path = 'new_test_pics/new_test_pics2/'
    img = Image.open(os.path.join(path, imgname))
    for i in range(3):
        for j in range(3):
            box = (xi, yi, xf, yf) # this is the starting point, and the image moves on by increasing (1400, 910) every time
            new_img = img.crop(box)
            new_img.save(path + name + '/' + str(count) + '.jpg')
            count += 1
            xi += 1430
            xf += 1430
        xi = x1
        xf = x2
        yi += 930
        yf += 930

def swipe_filename():
    i = 1189 - 1
    j = i - 3
    k = j - 3
    count = 0
    path1 = "new_test_pics\\new_test_pics2\\Gel_D1"
    for filename in os.listdir(path1):
        if count >= 0 and count <= 2:    # count = 1,2
            i += 1
            os.rename(os.path.join(path1, filename), os.path.join(path1, str(i)+'.jpg'))
        elif count >= 3 and count <= 5:
            j += 1
            os.rename(os.path.join(path1, filename), os.path.join(path1, str(j)+'.jpg'))
        else:
            k += 1
            os.rename(os.path.join(path1, filename), os.path.join(path1, str(k)+'.jpg'))
        count += 1

def remedy():
    count = 0
    path1 = "new_test_pics\\new_test_pics2\\Gel_C9"
    for filename in os.listdir(path1):
        os.rename(os.path.join(path1, filename), os.path.join(path1, str(count)+'.jpg'))
        count += 1

def remedy2():
    count = 1035
    path1 = "new_test_pics\\new_test_pics2\\Gel_A5"
    for filename in os.listdir(path1):
        os.rename(os.path.join(path1, filename), os.path.join(path1, str(count)+'.jpg'))
        count += 1


if __name__ == "__main__":
    create_new_folder_dir()
    """name = "Gel_C5"
    x, y = 920, 430    # 这是首坐标，第一张要切的小图在大图中的（左上角）坐标
    crop_original_img(name, x, y)"""