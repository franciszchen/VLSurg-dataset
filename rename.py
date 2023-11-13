import os
import numpy as np
import time 
from datetime import datetime
import sys

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

def rename_files(folder_path,new_name_list,index):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            new_filename = str(new_name_list[index].split("-")[0])+"-"+"-".join(filename.split("-")[1:])
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)

if __name__ == "__main__":
    # rename following folder's img
    folder_list = ['44-2022-0608-DG',
                    '45-2022-0310-TG',
                    '51-2022-0601-DG',
                    '58-2022-0607-DG',
                    '61-2022-0721-DG',
                    '68-2022-0714-TG',
                    '69-2022-0222-DG',
                    '70-2022-0329-DG',
                    '71-2022-0125-DG',
                    '72-2022-0216-DG',
                    '73-2022-0217-DG',
                    '74-2022-0324-TG',
                    '75-2022-0721-TG',
                    '76-2022-0303-TG',
                    '84-2022-0728-DG',
                    '85-2021-0715-DG',
                    '86-2021-0706-DG',
                    '87-2021-0706-DG',
                    '88-2021-0706-DG',
                    '89-2021-0729-DG',
                    '90-2021-0601-DG',
                    '91-2021-0602-DG',
                    '92-2021-0607-DG',
                    '93-2021-0609-DG',
                    '94-2021-0624-DG',
                    '95-2021-0706-DG',
                    '96-2021-0706-DG',
                    '97-2021-0706-DG',
                    '98-2021-0624-DG',
                    '99-2021-0817-DG',
                    '100-2021-0810-DG'
                    ]
    
    new_name_list = [str(i) for i in range(30,61)]
    source_path = "../image_3fps"
    for index,folder in enumerate(folder_list):
        print("# begin case {} ...".format(folder))
        folder_path = os.path.join(source_path,folder)
        rename_files(folder_path,new_name_list,index)