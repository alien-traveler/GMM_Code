from PIL import Image, ImageDraw
import os


# copy and paste a white block to the top right corner of each image in the file
def cover_img_w_block():
    path = 'new_test_pics/'
    path2 = 'after_change_pics/'
    for filename in os.listdir(path):
        image = Image.open(os.path.join(path, filename))
        white_block = Image.open('large_gray_chunk.png')
        image_copy = image.copy()
        position = ((image_copy.width - white_block.width), 0)
        image_copy.paste(white_block, position)
        image_copy.save(os.path.join(path2, filename))


# Draw a 290*100 light gray block
def draw_gray_block():
    blank_image = Image.new('RGB', (290, 100), (253, 251, 254))
    img_draw = ImageDraw.Draw(blank_image)
    blank_image.save('grayblock.jpg')