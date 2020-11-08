from PIL import Image, ImageDraw
import os


# copy and paste a white block to the top right corner of each image in the file 11.6.20
def cover_img_w_block():
    folder_list = ['Gel_A1', 'Gel_A2', 'Gel_A3', 'Gel_A4', 'Gel_A5', 
        'Gel_A6', 'Gel_A7', 'Gel_B1', 'Gel_B2', 'Gel_B3', 'Gel_B4', 
        'Gel_B5', 'Gel_C1', 'Gel_C2', 'Gel_C3', 'Gel_C4', 'Gel_C5', 
        'Gel_C6', 'Gel_C7', 'Gel_C8', 'Gel_C9', 'Gel_D1']

    path = 'new_test_pics\\new_test_pics2\\'
    path2 = 'after_change_pics\\after_change_pics3\\'
    for foldername in folder_list:
        # each foler under the new_test_pics2
        folder_path = path + foldername + '\\'
        folder_path2 = path2 + foldername + '\\'
        for file_name in os.listdir(folder_path):
            # each img under the folder (ex. \\Gel_A1)
            image = Image.open(os.path.join(folder_path, file_name))
            white_block = Image.open('big_grayblock.jpg')
            image_copy = image.copy()
            position = ((image_copy.width - white_block.width), 0)
            image_copy.paste(white_block, position)
            image_copy.save(os.path.join(folder_path2, file_name))


# Draw a 290*100 light gray block 11.6.20
def draw_gray_block():
    blank_image = Image.new('RGB', (1170, 400), (240, 241, 246))
    img_draw = ImageDraw.Draw(blank_image)
    blank_image.save('big_grayblock.jpg')

if __name__ == "__main__":
    #draw_gray_block()
    cover_img_w_block()