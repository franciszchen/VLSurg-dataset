import numpy as np
import pandas as pd

import os



substage_map = {'Digestive tract reconstruction(Digestive tract reconstruction)': 'G-3',
 'Digestive tract reconstruction(Reinforced anastomosis)':'G-4',
 'Digestive tract reconstruction(Section the distal stomach)': "G-2",
 'Digestive tract reconstruction(Section the proximal stomach)': 'G-1',
 'Dissect the superior margin of pancreas (Dissect NO.7,8,9 group lymph nodes)': "E-0",
 'Dissect the superior margin of pancreas(Dissect NO.11p group lymph nodes)':"E-1",
 'End of operation':  "H-0",
 'Preparation(Insert trocar)': "A-0",
 'Preparation(Liver suspension)':  "A-1",
 'Preparation(Peritoneal exploration)':  "A-2",
 'Separate the distal stomach(Dissection of the duodenum)':"C-0",
 'Separate the distal stomach(Separate the distal stomach)':'C-1',
 'Separate the distal stomach(Sever the distal stomach)': "C-2",
 'Separate the greater gastric curvature(Clear the subpyloric area)': "B-3",
 'Separate the greater gastric curvature(Dissect No.4sb group lymph nodes)': "B-5",
 'Separate the greater gastric curvature(Dissociate the greater omentum to the left)':"B-1",
 'Separate the greater gastric curvature(Dissociate the greater omentum to the right)': "B-2",
 'Separate the greater gastric curvature(Sever the gastrocolic ligament)':"B-0",
 'Separate the proximal stomach (Dissect NO.1,3 group lymph nodes)': 'F-0',
 'none': 'none',
 'Separate the less gastric curvature (Dissect NO.5,12 group lymph nodes)': 'D-0',
 'Separate the proximal stomach(Sever the proximal stomach)': 'F-2',
 'Separate the greater gastric curvature(Severing the gastrocolic ligament)': 'B-0',
 'Digestive tract reconstruction(Pre-reconstruction preparation)': 'G-0',
 'Separate the proximal stomach (Dissect NO.11d group lymph nodes)': 'F-1',
 'Separate the greater gastric curvature(Dissect No.4sa group lymph nodes)': 'B-4'}




def init_dict(label_list,is_list=False):
    dictionary = {}
    for label in label_list:
        if is_list:
            dictionary[label] = {
                "Depth perception":[],
                "Bimanual dexterity":[],
                "Efficiency":[],
                "Tissue handling":[],
                "Autonomy":[],
                "ESSQS":[]
            }
        else:
            dictionary[label] = 0
    
    return dictionary

def duration_single_csv(csv_file,dictionary):

    csv = csv_file.copy()
    csv.dropna(subset=["end_sec","start_sec"],inplace=True)
    duration = csv.end_sec-csv.start_sec
    indexes = duration.index
    for i in indexes:
        label = csv.label.loc[i]
        label_dur = duration.loc[i]
        if label!=label:
            continue
        else:
            dictionary[str(label)] += label_dur

        
def phase_count_single_csv(csv_file,dictionary):
    labels = np.unique(csv_file.label.dropna())
    for label in labels:
        dictionary[label] +=1


def index_single_csv(csv_file,dictionary):
    label_subset = ["label","Depth perception","Bimanual dexterity","Efficiency","Tissue handling","Autonomy","ESSQS"]
    subset = ["Depth perception","Bimanual dexterity","Efficiency","Tissue handling","Autonomy","ESSQS"]
    csv = csv_file[label_subset].dropna(subset = ["Depth perception","Bimanual dexterity","Efficiency","Tissue handling","Autonomy","ESSQS"],how="all")
    indexes = csv.index
    for i in indexes:
        label = csv.loc[i].label
        if label!=label:
            print("no_label")
            label = "A"
            #continue
        for score in subset:
            if csv.loc[i][score] != csv.loc[i][score]:
                continue
            else:
                dictionary[label][score].append(csv.loc[i][score])


def count_substage(csv_file,dictionary):
    labels = np.unique(csv_file.sub_stage.dropna())
    for label in labels:
        if label in dictionary.keys():
            dictionary[label] +=1
        else:
            dictionary[label] = 1



def phase_count_single_csv(csv_file,dictionary):
    labels = np.unique(csv_file.label)
    for label in labels:
        dictionary[label] +=1



def index_single_csv(csv_file,index_list,dictionary):
    csv = csv_file[["Depth perception","Bimanual dexterity","Efficiency","Tissue handling","Autonomy","ESSQS"]].dropna(how="all")
    indexes = csv.index
    for i in indexes:
        row = csv_file.loc[i]
        label = row.label
        for ind in index_list:
            score = row[ind]
            dictionary[label][ind].append(score)




def get_all_csv(dir_path,label_list,index_list):
    csv_list = os.listdir(dir_path)

    dur_dictionary = init_dict(label_list)
    phase_count_dictionary = init_dict(label_list)
    index_dictionary = init_dict(label_list,is_list=True)

    for csv_path in csv_list:
        csv_path = os.path.join(dir_path,csv_path)
        print(csv_path)
        csv_file = pd.read_csv(csv_path)
        index_single_csv(csv_file,index_list,index_dictionary)
        duration_single_csv(csv_file,dur_dictionary)
        phase_count_single_csv(csv_file,phase_count_dictionary)

    return dur_dictionary,phase_count_dictionary,index_dictionary

"""
#for single file
label_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#index_list = ["Depth perception","Bimanual dexterity","Efficiency","Tissue handling","Autonomy","ESSQS"]
file = pd.read_csv("VLSurg-1.csv")
dur_dictionary = init_dict(label_list)
phase_count_dictionary = init_dict(label_list)
index_dictionary = init_dict(label_list,is_list=True)
substage_dictionary = init_dict([])
index_single_csv(file,index_dictionary)
duration_single_csv(file,dur_dictionary)
phase_count_single_csv(file,phase_count_dictionary)
count_substage(file,substage_dictionary)
"""


def search_content(csv_folder_path,content,target_column):
    csv_folder = csv_folder_path
    all_csv_files = os.listdir(csv_folder)
    content = content
    target_column = target_column
    for file in all_csv_files:
        file_path = os.path.join(csv_folder,file)
        
        csv_file = pd.read_csv(file_path)
        for i,row in enumerate(csv_file[target_column]):
            if content == row:
                print(file_path,"  ",i+2)


def caption_to_substage(csv_path,substage_map):
    csv_folder = csv_path
    all_csv_files = os.listdir(csv_folder)
    for file in all_csv_files:
        file_path = os.path.join(csv_folder,file)
        
        csv_file = pd.read_csv(file_path)
        csv_file['caption'] = csv_file['caption'].map(substage_map)
        return csv_file

def remove_column(csv_path,col_name):
    csv_folder = csv_path
    all_csv_files = os.listdir(csv_folder)
    for file in all_csv_files:
        file_path = os.path.join(csv_folder,file)
        
        csv_file = pd.read_csv(file_path)
        csv_file = csv_file.drop([col_name],axis=1)
        return csv_file
    



if __name__ == "__main__":

    #for all videos
    csv_folder_path = "csv_folder_path"
    csv_folder = csv_folder_path
    #main
    label_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    #index_list = ["Depth perception","Bimanual dexterity","Efficiency","Tissue handling","Autonomy","ESSQS"]
    dur_dictionary = init_dict(label_list)
    phase_count_dictionary = init_dict(label_list)
    index_dictionary = init_dict(label_list,is_list=True)
    substage_count_dictionary = init_dict([])
    all_csv_files = os.listdir(csv_folder)
    for file in all_csv_files:
        file_path = os.path.join(csv_folder,file)
        print(file_path)
        csv_file = pd.read_csv(file_path)
        #ffill tha labels
        csv_file.label= csv_file.label.ffill()
        duration_single_csv(csv_file,dur_dictionary)
        phase_count_single_csv(csv_file,phase_count_dictionary)
        count_substage(csv_file,substage_count_dictionary)
        #index_single_csv(csv_file,index_dictionary)


    import json

    with open("sub_stage_count.txt","w") as f:
        f.write(json.dumps(substage_count_dictionary))

    with open("dur_dictionary.txt","w") as f:
        f.write(json.dumps(dur_dictionary))

    with open("phase_count_dictionary.txt","w") as f:
        f.write(json.dumps(phase_count_dictionary))


    with open("index_dictionary.txt","w") as f:
        f.write(json.dumps(index_dictionary))


