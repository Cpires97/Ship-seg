# Ship-seg
Method capable of real-time ship segmentation during maritime surveillance missions using onboard cameras.

Method with two stages: Detection and Segmentation.

Detection stage detects possible locations of the ship, and a segmentation stage segments the bounding boxes from the previous stage.

## Detection stage
We use the YOLO network implementation [GitHub Pages] https://github.com/pjreddie/darknet
