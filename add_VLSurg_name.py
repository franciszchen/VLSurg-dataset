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

def add_prefix_to_files(folder_path, prefix):
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    for subfolder in subfolders:
        print("# begin case {} ...".format(subfolder))
        files = [f.path for f in os.scandir(subfolder) if f.is_file()]
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            
            
            new_file_name = prefix + file_name.split(os.sep)[-1] + file_ext
            
            
            new_file_path = os.path.join(subfolder, new_file_name)
            
            
            os.rename(file, new_file_path)
            
folder_path = '../image_3fps'
prefix = 'VLSurg-'

add_prefix_to_files(folder_path, prefix)