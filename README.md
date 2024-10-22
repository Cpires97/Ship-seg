# Ship-seg: Cascade model for segmenting maritime images
Method capable of real-time ship segmentation during maritime surveillance missions using onboard cameras.

Method with two stages: Detection and Segmentation.

Detection stage detects possible locations of the ship, and a segmentation stage segments the bounding boxes from the previous stage.

Addition of a post-processing technique, CRFs, to improve the segmentation.

## Detection stage
We use the YOLO network implementation [YOLOv3] https://github.com/pjreddie/darknet

## Segmentation stage
We implement the U-Net network with a pre-trained model from here [Segmentation-model] https://github.com/qubvel/segmentation_models 

## Conditional Random Fields
We use a python implementation of the dense CRFs from here https://github.com/lucasb-eyer/pydensecrf

## Datasets
To train and test the cascade model we used two dasasets:
- Seagull dataset http://vislab.isr.ist.utl.pt/seagull-dataset/
- Airbus Ship Detection Challenge https://www.kaggle.com/c/airbus-ship-detection/data 
### Clips from Seagull
- 2015-04-22-16-05-15_jai_eo
- 2015-04-23-14-09-25_jai_eo 
- 2015-06-02-13-44-14_gobi 
- bigShipHighAlt
- GP020175
- GP030175
- GP050027
- GP060027
- GP070027
- lanchaArgos
- smallBoatMoving
- smallBoatStopped

## Results
Results on the Airbus Ship Detection Challenge: 
Method | #Score | #Time/image [s] |
--- | --- | --- | 
Full image segmentation | 0.71 | 1.47 |
Full image segmentation + CRF| 0.76 | 6.1 |
Cascade Model | 0.82 | 0.09 |
Cascade Model + CRF | 0.82 | 0.13 |

<img src="https://github.com/Cpires97/Ship-seg/blob/main/segmentation/results/ex_1/00a3ab3cc.jpg" width="300" /> <img src="https://github.com/Cpires97/Ship-seg/blob/main/segmentation/results/ex_1/bb.png" width="400" />
<img src="https://github.com/Cpires97/Ship-seg/blob/main/segmentation/results/ex_1/Figure_2.png" width="700" />



