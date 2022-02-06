import cv2
import numpy as np
import glob
import os

# 画像のパスを取得する関数
def get_imgpath(origin_path):
    #oringin_pathディレクトリの全てのファイルを開く
    path_list = glob.glob(origin_path + "/*")

    for img_path in path_list:
        base_name = os.path.basename(img_path)
        name, ext = os.path.splitext(base_name)

        if (ext != '.jpg') and (ext != '.jpeg') and (ext != '.png'):
            print("not a picture")
            continue
        
        yield img_path

coord_list = [i for i in range(230, 400, 30)]
for i in get_imgpath('./input_image'):
    img = cv2.imread(i, 0)
    img = cv2.resize(img, (1280, 720))
    
    for j in coord_list:
        cut_img = img[99 : 99 + 36, j : j + 30]
        cv2.imwrite(f'./number_template_img_color/{i[-6:]}_{j}.png', cut_img)
        ret, cut_bin_img = cv2.threshold(cut_img, 245, 255, cv2.THRESH_BINARY)
        cv2.imwrite(f'./number_template_img_bin/{i[-6:]}_{j}.png', cut_bin_img)

    