import os
from PIL import Image

"""# rename each img in the file
path = 'new_test_pics/'

i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path, filename), os.path.join(path, 'captured'+str(i)+'.jpg'))
    i = i + 1"""

"""# check img size
path = 'new_test_pics/'
for filename in os.listdir(path):
    image = Image.open(os.path.join(path, filename))
    print(image.size)"""


"""# crop img
img = Image.open('faf8f9.png')
box = (0,0,290,100) # we want 290*100
cropped_image = img.crop(box)
cropped_image.save('gray_block.png')"""

"""# resize img
image = Image.open('gray_block.png')
new_img = image.resize((290, 100))
new_img.save('large_gray_chunk.png')"""