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

def crop_original_img():
    count = 0
    xi, yi, xf, yf = 180, 650, 1580, 1560
    #box = (xi, yi, xf, yf) # this is the starting point, and the image moves on by increasing (1410, 550) every time
    path = 'new_test_pics/new_test_pics2/Gel_D1/'
    img = Image.open(os.path.join(path, "Gel_D1.jpg"))
    for i in range(3):
        for j in range(3):
            box = (xi, yi, xf, yf) # this is the starting point, and the image moves on by increasing (1410, 550) every time
            new_img = img.crop(box)
            new_img.save(path + str(count) + '.jpg')
            count += 1
            xi += 1430
            xf += 1430
        xi = 180
        xf = 1580
        yi += 930
        yf += 930
    """new_img = img.crop(box)
    new_img.show()
    box = (160+1410, 550, 1570+1410, 1460)
    new_img = img.crop(box)
    new_img.show()"""



if __name__ == "__main__":
    crop_original_img()