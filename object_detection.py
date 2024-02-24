import cv2

# Load the image
img = cv2.imread("Images/street.jpg")

# Load class names
classnames = []
classfile = "files/thing.names"
with open(classfile, "rt") as f:
    classnames = f.read().rstrip('\n').split('\n')  # Use split() to get a list of class names

# Load the model
algo = 'files/frozen_inference_graph.pb'
mobile = 'files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
net = cv2.dnn_DetectionModel(algo, mobile)

# Set input size and scale factor
net.setInputSize(320, 230)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Perform object detection
class_ids, confidences, bbox = net.detect(img, confThreshold=0.5)

# Draw bounding boxes and labels
if len(class_ids) > 0:
    for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), bbox):
        label = str(classnames[class_id - 1])
        score = confidence
        x, y, w, h = box

        # Draw bounding box and label
        cv2.rectangle(img,box,color=(0,255,0) , thickness=2) 
         # Place text inside the bounding box
        text = f'{label} {score:.2f}'
        cv2.putText(img, text, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
# Display the image with detected objects
cv2.imshow("Detecting ...", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
