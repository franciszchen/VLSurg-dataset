# VLSurg DATASET

The official codes for [**VLSurg: A Versatile Laparoscopic Surgical Video Dataset Bridges General AI and Modern Operating Room**](linktopaper)

## Introduction 

Surgical phase recognition is crucial to providing surgery understanding in smart operating rooms. Despite great progress in automatic surgical phase recognition, most existing methods are still restricted by two problems. First, these methods cannot capture discriminative visual features for each frame and motion information with simple 2D networks. Second, the frame-by-frame recognition paradigm degrades the performance due to unstable predictions within each phase, termed as phase shaking. To address these two challenges, we propose a Surgical Phase LocAlization Network, named SurgPLAN, to facilitate a more accurate and stable surgical phase recognition with the principle of temporal detection. Specifically, we first devise a Pyramid SlowFast (PSF) architecture to serve as the visual backbone to capture multi-scale spatial and temporal features by two branches with different frame sampling rates. Moreover, we propose a Temporal Phase Localization (TPL) module to generate the phase prediction based on temporal region proposals, which ensures accurate and consistent predictions within each surgical phase. Extensive experiments confirm the significant advantages of our SurgPLAN over frame-by-frame approaches in terms of both accuracy and stability.

## Method


## Cite
```
   
@article{luo2023surgplan,
  title={SurgPLAN: Surgical Phase Localization Network for Phase Recognition},
  author={Luo, Xingjian and Pang, You and Chen, Zhen and Wu, Jinlin and Zhang, Zongmin and Lei, Zhen and Liu, Hongbin},
  journal={arXiv preprint arXiv:2311.09965},
  year={2023}
}   
   
```
