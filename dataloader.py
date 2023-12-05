import os
import torch
import cv2
from torch.utils.data import Dataset
import pandas as pd




class VLSurg(Dataset):
    def __init__(self,root_dir,patient_id,annotation_dir,transform=None,task = "label"):
        #training and testing list/folders
        self.train_list = [2,3,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,49,50,51,52,53,55,57,58,59,60]
        self.test_list =  [1,4,10,20,22,40,45,48,54,56]

        self.train_folders = ["VLSurg-{}".format(i) for i in self.train_list]
        self.test_folders = ["VLSurg-{}".format(i) for i in self.test_list]
        #root dir for all the dir
        self.root_dir = root_dir
        self.patient_id = patient_id
        if patient_id in self.train_list:
            self.is_train = True
        else:
            self.is_train = False

        folder_name = "VLSurg-"+str(patient_id)
        self.folder_path = os.path.join(root_dir,folder_name)
        self.imgs_list = os.listdir(self.folder_path)
        self.lens = len(self.imgs_list)

        #preprocess transformation for the images
        self.transform = transform
        #annotation folder 
        self.annotation_dir = annotation_dir

        self.task = task

    def __getitem__(self, idx):
        
        img_name = self.imgs_list[idx]
        img_path = os.path.join(self.folder_path,img_name)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        annotation_name = "VLSurg-"+str(self.patient_id)+".csv"
        annotation_path = os.path.join(self.annotation_dir,annotation_name)
        df = pd.read_csv(annotation_path)
        label = self.get_label(df,img_name,self.task)


        return img,label
            

    def get_train_test(self,folder_name):
        patient_id = folder_name.split("-")[1]
        if int(patient_id) in self.train_list:
            return "train"
        else:
            return "test"
        
    def get_label(self,df,img_name,task):
        _,patient_id,is_TG,vid,sec,frame = img_name.split("-")
        #determine which substage/stage of the current frame
        file_name = "VLSurg-"+patient_id+"-"+is_TG+"-"+vid
        sub_df = df[df["filename"] == file_name]
        sec = int(sec)
        for row in range(len(sub_df)):
            if sub_df["start_sec"].iloc[row]<=sec and sub_df["end_sec"].iloc[row]>=sec:
                return sub_df[task].iloc[row]

    def preprocess(self,img):
        return self.transform(img)

    
    def filter(self,img_name):
        pass
    
    
    def __len__(self):
        return self.lens
