from PIL import Image, ImageDraw
import os


# copy and paste a white block to the top right corner of each image in the file 11.6.20
def cover_img_w_block():
    path = 'new_test_pics/new_test_pics2/Gel_D1/'
    path2 = 'after_change_pics/after_change_pics2/Gel_D1/'
    for filename in os.listdir(path):
        image = Image.open(os.path.join(path, filename))
        white_block = Image.open('big_grayblock.jpg')
        image_copy = image.copy()
        position = ((image_copy.width - white_block.width), 0)
        image_copy.paste(white_block, position)
        image_copy.save(os.path.join(path2, filename))


# Draw a 290*100 light gray block 11.6.20
def draw_gray_block():
    blank_image = Image.new('RGB', (1170, 400), (240, 241, 246))
    img_draw = ImageDraw.Draw(blank_image)
    blank_image.save('big_grayblock.jpg')

if __name__ == "__main__":
    draw_gray_block()
    cover_img_w_block()