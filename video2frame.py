import cv2
import os
import numpy as np
#import PIL
#from PIL import Image
import time 
import re
from datetime import datetime

import sys
import time

class Logger(object):
    def __init__(self, filename="Default"):
        self.terminal = sys.stdout
        self.filename = filename + ' ' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
        self.log = open(self.filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

sys.stdout = Logger('TestLog')

def video2frame(
    source_path, 
    save_path,
    case_folder,
):
    file_list = os.listdir(
        os.path.join(source_path, case_folder))   
    print("# begin case {} ...".format(case_folder))
    # file_list = os.listdir(
    #     os.path.join(source_path, case_folder))
    for filename in file_list:
        if '.mp4' in filename or '.MP4' in filename: # 部分视频文件的后缀改变
            print(" * begin video {} ...".format(filename))
        frame_num = 0
        if not os.path.exists(
                os.path.join(save_path, str(case_folder))
            ):
            os.makedirs(os.path.join(save_path, str(case_folder))) 
        cap = cv2.VideoCapture(
            os.path.join(
                source_path,
                case_folder,
                filename
            )
        )
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            fps = cap.get(cv2.CAP_PROP_FPS)
            sampling_list = [0,8,17] #需要采样的frame
            #print(fps) #25
            remainder = frame_num % fps

            #处理特殊名字的视频文件
            Vn = filename.split(".")[1] 
            if Vn == "mp4":
                Vn = 0

            if remainder in sampling_list: # 只保留特定的frame
                filename_dic = {
                "ID":filename.split("-")[0], #patient_id
                "TGDG":re.split("\.|-",filename)[3], #TG or DG
                "Vn":Vn, #video_id
                "Sec":int(frame_num/fps), #second
                "Frame":sampling_list.index(remainder) #frame
                }
                imgname = "VLSurg-{ID}-{TGDG}-{Vn}-{Sec}-{Frame}.jpg".format(
                    **filename_dic
                )
                img_save_path = os.path.join(
                    save_path,
                    case_folder,
                    imgname
                )
                
                blurred_1 = frame[73:127,14:213] = cv2.blur(frame[73:127,14:213],(23,23)) #左上角recordor模糊
                blurred_2 = frame[1021:1048,7:357] = cv2.blur(frame[1021:1048,7:357],(23,23)) #左下角日期模糊
                blurred_3 = frame[1020:1054,1688:1763] = cv2.blur(frame[1020:1054,1688:1763],(23,23)) #右下角S3D模糊
                
                # print("crop shape: ", cropped.shape)
                #resized = cv2.resize(cropped, (448, 256))
                # resized = cv2.resize(cropped, (700, 400))
                #
                if not os.path.exists(img_save_path):
                    cv2.imwrite(img_save_path, frame) # cv2.imwrite(img_save_path, frame)
                # print(img_save_path)
            frame_num = frame_num+1
    cap.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

 

if __name__ == "__main__":

        
    source_path = "../current_data"
    save_path = "../image_3fps"  # save path

    case_folder_list = ['68-2022-0714-TG', '69-2022-0222-DG',
              '7-2022-0409-DG', '70-2022-0329-DG', '71-2022-0125-DG', '72-2022-0216-DG', '73-2022-0217-DG',
                '74-2022-0324-TG', '75-2022-0721-TG', '76-2022-0303-TG', 
                '8-2022-0409-DG',  '84-2022-0728-DG', 
                '85-2021-0715-DG', '86-2021-0706-DG', '87-2021-0706-DG', '88-2021-0706-DG', '89-2021-0729-DG', '9-2022-0428-DG', '90-2021-0601-DG',
                  '91-2021-0602-DG', '92-2021-0607-DG', '93-2021-0609-DG', '94-2021-0624-DG', '95-2021-0706-DG', '96-2021-0706-DG', '97-2021-0706-DG',
                    '98-2021-0624-DG', '99-2021-0817-DG']
    current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    log_file = current_time+"_log.txt"
    
    start_time = time.time()
    for case_folder in case_folder_list:
        video2frame(
            source_path=source_path, 
            save_path=save_path,
            case_folder = case_folder,
        )
        print("current time: {:.1f} min".format((time.time()-start_time)/60.0))
    print("Finish time: {:.1f} min".format((time.time()-start_time)/60.0))