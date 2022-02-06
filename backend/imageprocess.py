import cv2
import numpy as np
import requests
from PIL import Image
# import pyocr
import pytesseract

import io
import re
import os

class image_process:

    def __init__(self):
        self.input_img = None
        self.result_img = None
        self.id_recog_result_img = None
        self.result_img_byte = None
        self.id_recog_result_img_byte = []
        self.leftscore = ''
        self.rightscore = ''
        self.message = ''
        self.player_id = ''
        self.clan_mems = []
        self.clanmem_id = []
        self.flag = False
        self.num_vs = 0
        self.match_result = ''
        self.m = ''

    def image_process(self, img):
        self.input_img = cv2.resize(img, (1920, 1080))
        self.result_img = self.input_img.copy()
        self.judge_battle()
        # self.player_recog()


    def judge_battle(self):
        img = cv2.cvtColor(self.input_img, cv2.COLOR_RGB2GRAY)
        # img = img[80:150, 210:390]
        ret, bin_target = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        bin_target = bin_target[135:210, 300:1200]
        # print(img.shape)
        # cv2.imshow('bin_target.png', bin_target)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        label = []
        label_x_sum = 0 
        lis1 = []
        for i in range(10):
            temp_name = f'./template_image_bin/large{i}.png'
            # temp_name = f'./number_template_img/{i}.png'
            template_ori = cv2.imread(temp_name, 0)
            template_ori = cv2.resize(template_ori, (template_ori.shape[1], template_ori.shape[0]))
            w, h = template_ori.shape[::-1]
            res = cv2.matchTemplate(bin_target, template_ori, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(res >= threshold)
            loc = list(zip(*loc[::-1]))
            loc.sort()
            # print(i, loc)
            cnt = 0
            
            if loc:
                data_num = len(loc)
                x_sum, y_sum = 0, 0
                for j in range(1, data_num):
                    x_pre, y_pre = loc[j - 1]
                    x, y = loc[j]
                    x_sum += x_pre
                    y_sum += y_pre
                    cnt += 1
                    if x - x_pre > 20:
                        average_x = x_sum // cnt
                        average_y = y_sum // cnt
                        lis1.append((average_x, average_y, i))
                        x_sum, y_sum, cnt = 0, 0, 0

                if x_sum != 0:
                    x_sum += x
                    y_sum += y
                    cnt += 1
                    average_x = x_sum // cnt
                    average_y = y_sum // cnt
                    lis1.append((average_x, average_y, i))
                
                else:
                    x, y = loc[data_num - 1]
                    lis1.append((x, y, i))

        if lis1:
            lis1.sort()
            print(lis1)

            idx = 0
            left_score, right_score = '', ''
            right_flag = False
            for i in range(1, len(lis1)):
                x_pre, y_pre, num_pre = lis1[i - 1]
                x, y, num = lis1[i]
                if right_flag:
                    right_score += str(num_pre)
                else:
                    left_score += str(num_pre)
                if x - x_pre > 300:
                    right_flag = True

            right_score += str(num)

            self.leftscore = int(left_score)
            self.rightscore = int(right_score)

            cv2.imwrite("self.result_img.png", self.result_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            if int(self.leftscore) > int( self.rightscore):
                judge = '勝ち～！'
                self.match_result = 'WIN'

            elif int(self.leftscore) < int( self.rightscore):
                judge = '負けちゃったね…'
                self.match_result = 'LOSE'

            else:
                judge = 'めずらしい！引き分けだね'
                self.match_result = 'DRAW'

            self.m = f'{self.leftscore} vs {self.rightscore}で{judge}\n'

        else:            
            self.m = '勝敗がわかりませんでした…\n'
            

    def detect_color(self, img, mode):
        # HSV色空間に変換
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        if mode == 'green':
            hsv_min = np.array([80, 50, 150])
            hsv_max = np.array([140, 255, 255])

        elif mode == 'brown':
            hsv_min = np.array([0, 20, 100])
            hsv_max = np.array([60, 180, 255])

        mask = cv2.inRange(hsv, hsv_min, hsv_max)

        # マスキング処理
        masked_img = cv2.bitwise_and(img, img, mask=mask)

        return mask, masked_img

    def player_recog(self):
        # OCRエンジンを取得
        path=';C:\\Program Files\\Tesseract-OCR'
        os.environ['PATH'] = os.environ['PATH'] + path
        # # os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/5/tessdata"
        # tools = pyocr.get_available_tools()

        # tool = tools[0]
        # print(tool)
        LOC_X = 1525
        LOC_Y = 242
        target_img = self.input_img[LOC_Y:LOC_Y + 323, LOC_X:LOC_X + 300]
        Estimated_players = []
        Estimated_clan_mems = []

        for i in range(6):
            trim_img = target_img[i * (48 //1):(32 // 1) + i * (48//1), :]
            # trim_img = target_img
            participant_img = cv2.cvtColor(trim_img, cv2.COLOR_RGB2GRAY)

            ret, bin_participant_img = cv2.threshold(participant_img, 127, 255, cv2.THRESH_BINARY)
            txt_participants = pytesseract.image_to_string(Image.fromarray(bin_participant_img), lang="eng")
            green_mask, green_masked_img = self.detect_color(trim_img, 'green')
            brown_mask, brown_masked_img = self.detect_color(trim_img, 'brown')
            # green_masked_img = cv2.cvtColor(green_masked_img, cv2.COLOR_BGR2GRAY)
            green_masked_img = cv2.blur(green_masked_img, (1, 1))
            brown_masked_img = cv2.blur(brown_masked_img, (1, 1))
            txt_player = pytesseract.image_to_string(Image.fromarray(green_masked_img), lang="eng")
            txt_player = re.sub(r"[,.!?:;'\s\r\n]", "", txt_player)
            txt_clan = pytesseract.image_to_string(Image.fromarray(brown_masked_img), lang="eng")
            txt_clan = re.sub(r"[,.!?:;'\s\r\n]", "", txt_clan)
            image_size = green_mask.size
            whitePixels_green = cv2.countNonZero(green_mask)
            whitePixels_brown = cv2.countNonZero(brown_mask)

            if txt_player != '':
                Estimated_players.append([txt_player, round(whitePixels_green / image_size, 5), (LOC_X + 300 // 3, LOC_Y + 32 // 3 + i * 48 // 3), green_masked_img])
                self.num_vs += 1

            elif txt_clan != '':
                Estimated_clan_mems.append([txt_clan, round(whitePixels_brown / image_size, 5), (LOC_X + 300 // 3, LOC_Y + 32 // 3 + i * 48 // 3), brown_masked_img])
                self.num_vs += 1
            
            elif txt_participants != '':
                self.num_vs += 1
            
            # print(txt_participants)
            # cv2.imshow('bin', bin_participant_img)

            # cv2.imshow('trim', trim_img)
        
            # cv2.imshow('trim', green_mask)
            # print()
            # cv2.imshow('trim', brown_masked_img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

        if Estimated_players:
            if len(Estimated_players) == 1:
                # player_id = re.sub(r"[,.!?:;' ]", "", Estimated_players[0][0])
                # player_id = re.sub('[\r\n]+$', '', player_id, flags=re.MULTILINE)
                player_id = re.sub(r"[,.!?:;'\s\r\n]", "", Estimated_players[0][0])
                player_id_loc = Estimated_players[0][2]
                self.id_recog_result_img = Estimated_players[0][3]
                # print(file, player_id)

            else:
                es_players = sorted(Estimated_players, key=lambda x: x[1], reverse=True)
                player_id = re.sub(r"[,.!?:;'\s\r\n]", "", es_players[0][0])
                # player_id = re.sub('[\r\n]+$', '', player_id, flags=re.MULTILINE)
                player_id_loc = es_players[0][2]
                self.id_recog_result_img = es_players[0][3]
                # print(sorted(Estimated_players, key=lambda x: x[1]))
                # print(file, player_id)

            self.player_id = player_id
            # print(judge.judge(input_img), player_id)

        if self.player_id:
            self.m += f'プレイヤーのidは {self.player_id} です！\n'
            # cv2.rectangle(self.result_img, (LOC_X, player_id_loc[1] - 32), player_id_loc, (0, 255, 0), 3)

        else:
            self.m += 'プレイヤーのidはわかりませんでした…\n'

        if Estimated_clan_mems:
            self.clan_mems = Estimated_clan_mems.copy()
            self.m += 'クランメンバーのidは…\n'
            for mem in self.clan_mems:
                self.m += f'{mem[0]}\n'
                self.clanmem_id.append(mem[0])
                # cv2.rectangle(self.result_img, (LOC_X, mem[2][1] - 32), mem[2], (0, 0, 255), 3)

            self.m += "です!"

        # ret, img = cv2.imencode('.png', self.result_img)
        # self.result_img_byte = io.BytesIO(img)
        # ret, img = cv2.imencode('.png', self.id_recog_result_img)
        # self.id_recog_result_img_byte.append(io.BytesIO(img))
        # if self.clan_mems:
        #     for mem in self.clan_mems:
        #         ret, img = cv2.imencode('.png', mem[3])
        #         self.id_recog_result_img_byte.append(io.BytesIO(img))
