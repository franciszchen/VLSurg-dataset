# VLSurg DATASET

The official codes for [**VLSurg: A Versatile Laparoscopic Surgical Video Dataset Bridges General AI and Modern Operating Room**](linktopaper)

## Introduction 

Laparoscopic radical gastrectomy is widely employed for gastric cancer surgery. Understanding and assessing the surgical
videos hold paramount importance in enhancing surgical skills and improving patient outcomes. In modern operating rooms
(OR), AI algorithms can be integrated to assist surgical phase recognition, surgical skill assessment, and surgical description
generation. These three tasks are crucial for improving surgical efficiency, enhancing surgical skills, and reducing administrative
burden. In spite of some existing datasets and AI algorithms, there lack of a laparoscopic surgical video dataset with
comprehensive annotations for the three tasks, which limits the development of general AI in the surgical AI field. To bridge
the advanced techniques in general AI and the requirements of modern OR, we develop a large-scale Versatile Laparoscopic
Surgical video dataset, VLSurg, with surgical videos from 60 patients. This dataset contains comprehensive annotations for
surgical phases, surgical skill assessment, and surgical descriptions, offering opportunities for developing versatile and general
AI algorithms that can support surgical decision-making and patient care.
![avatar](/imgs/img_1.png)


## Link to DATASET

VLSurg Dataset [Link](https://www.scidb.cn/en/anonymous/TkJiMml5) on Science DB

## Structure of the dataset

training and testing splitting:  

training:[2,3,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,49,50,51,52,53,55,57,58,59,60] 

testing:[1,4,10,20,22,40,45,48,54,56]

```
VLSurg  

└───VLSurg_Annotation/
│    └───VLSurg_1.csv
|    └───VLSurg_2.csv 
│    └───...  
│       
|
└───train
│     └───VLSurg_2
│          └───VLSurg_2.zip
│     └───VLSurg_3
│          └───VLSurg_3.zip
|     └───...
└───test
|    └───VLSurg_1
|         └───VLSurg_1.zip
|    └───VLSurg_4
|         └───VLSurg_4.zip
|    └───...

CSV files are annotations for the corresponding VLSurg patient videos.
zip files are frames/images for each VLSurg patient video.
```


## Frame name explanation
```
Explanation for the frame name in the zip files:  

frame_name : {ID}-{DG/TG}-{Vid}-{Sec}-{Frame}.jpg  
frame_name =   
{  
"ID": patient_id,   
"TG/DG": TG or DG,  # TG stands for Total Gastrectomy, DG stands for Distal Gastrectomy
"Vid":video_id,   # The whole surgical video of the patient is divided into multiple index-ordered videos 
"Sec": current second in video,  
"Frame": frame_index (default 3 fps)  #0, 1 or 2 
}
```

## Metadata
												
#### Explanation for the annotation CSV file

|column_name|Explanation|
|--|:--:|
folder name	| video's folder name
filename|video's file name
start_sec|start second of the sub-stage
end_sec|end second of the sub-stage
label|label of the stage
sub_stage|label of the substage
Perfect|The surgeon can accurately direct instruments in the correct plane to the target, expertly use both hands to provide optimal exposure, organize movements as planned, handle tissues well, and able to complete task independently
ImPerfect|The surgeon missed some of the targets and caused occasional unnecessary bleeding
Depth perception|Global operation assessment of laparoscopic skills (GOALS)
Bimanual dexterity|Global operation assessment of laparoscopic skills (GOALS)
Efficiency|Global operation assessment of laparoscopic skills (GOALS)
Tissue handling|Global operation assessment of laparoscopic skills (GOALS)
Autonomy|Global operation assessment of laparoscopic skills (GOALS)
description| Nature Language Description of the sub_stage

## DataLoader Example
An example of PyTorch DataLoader

```
cd path/to/VLSurg_zip_file  
unzip VLSurg_zip_file  
```
```
dataloader code
```



## Link to Phase Detection Methods


## Cite
```
   
citation   
   
```
