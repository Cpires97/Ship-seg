# Ship-seg: Cascade model for segmenting maritime images
Method capable of real-time ship segmentation during maritime surveillance missions using onboard cameras.

Method with two stages: Detection and Segmentation.

Detection stage detects possible locations of the ship, and a segmentation stage segments the bounding boxes from the previous stage.

## Detection stage
We use the YOLO network implementation [YOLOv3] https://github.com/pjreddie/darknet

## Segmentation stage
We implement the U-Net network with a pre-trained model from here [Segmentation-model] https://github.com/qubvel/segmentation_models 

## Datasets
To train and test the cascade model we used two dasasets:
- Seagull dataset http://vislab.isr.ist.utl.pt/seagull-dataset/
- Airbus Ship Detection Challenge https://www.kaggle.com/c/airbus-ship-detection/data 


![Image](segmentation/results/ex_1/00a3ab3cc.jpg?raw=true | width=100) 
