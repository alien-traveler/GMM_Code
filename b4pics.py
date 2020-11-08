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

# check the folder dir
def check_folder_dir():
    path = 'new_test_pics/new_test_pics2/'
    folder_name_list = []
    for filename in os.listdir(path):
        folder_name_list.append(filename)
    print(folder_name_list)



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


if __name__ == "__main__":
    """check_folder_dir()"""
    name = "Gel_C5"
    x, y = 920, 430    # 这是首坐标，第一张要切的小图在大图中的（左上角）坐标
    crop_original_img(name, x, y)