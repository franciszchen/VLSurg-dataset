# VLSurg DATASET

The official codes for [**VLSurg: A Versatile Laparoscopic Surgical Video1 Dataset Bridges General AI and Modern Operating2Room**](linktopaper)

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

## Link to DATASET

scienceDB dataset link

## Structure of the dataset

- /VLSurg
  - /VLSurg_Annotation
    - VLSurg_1.csv
    - VLSurg_1.csv
    - ...
  - /VLSurg_1
    - VLSurg_1.zip
  - /VLSurg_2
    - VLSurg_2.zip
  - /VLSurg_3
    - VLSurg_3.zip
  - ......
## Metadata
												

|column|Explanation|
|--|:--:|
folder name	| ...
filename|...
start_sec|start second of the sub stage
end_sec|end second of the sub stage
label|label of the stage
sub_stage|label of the substage
Perfect|
ImPerfect|
Depth perception|
Bimanual dexterity|
Efficiency|
Tissue handling|
Autonomy|
description|

## DataLoader Example


## 
