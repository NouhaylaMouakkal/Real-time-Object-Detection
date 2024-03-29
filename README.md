# Real-time Object Detection with OpenCV and SSD MobileNet

![Example Image](Result.png)
## Overview
This project implements real-time object detection using the OpenCV library and the SSD MobileNet model. The system loads an image, detects objects within it, and displays bounding boxes along with class labels and confidence scores. The application of this project is practical for security and surveillance purposes.

## Tech Stack
- OpenCV2
- SSD MobileNet

## Instructions

### Installation
1. Install the required libraries using the following command:
    ```bash
    pip install opencv-python
    ```

### Usage
1. Clone the repository.
    ```bash
    git clone https://github.com/NouhaylaMouakkal/Real-time-Object-Detection.git
    cd Real-time-Object-Detection
    ```

2. Ensure you have the necessary model files and class names file in the specified locations:
    - Model files: `files/frozen_inference_graph.pb`, `files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`
    - Class names file: `files/thing.names`

3. Run the script:
    ```bash
    python object_detection.py
    ```

4. The script will load the image specified in the code (`Images/....`), perform object detection, and display the image with bounding boxes around detected objects.

