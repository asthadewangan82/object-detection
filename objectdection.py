import numpy as np
import cv2

image_path = 'roomwithpeople.jpg'
prototxt_path = 'models/MobileNetSSD_deploy.prototxt.txt'
model_path = 'models/MobileNetSSD_deploy.caffemodel'
min_confidence = 0.1

classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair",
           "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa",
           "train", "tvmonitor"]

np.random.seed(543210)
colors = np.random.uniform(0, 255, size=(len(classes), 3))


net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

cap = cv2.VideoCapture(0)

while True:

     _, image = cap.read()

     height, width = image.shape[0], image.shape[1]
     blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

     net.setInput(blob)
     detected_objects = net.forward()

     for i in range(detected_objects.shape[2]):

         confidence = (detected_objects[0][0][i][2])

         if confidence > min_confidence:

            class_index = int(detected_objects[0, 0, i, 1])

            upper_left_x = int(detected_objects[0, 0, i, 3] * width)
            upper_left_y = int(detected_objects[0, 0, i, 4] * height)
            lower_right_x = int(detected_objects[0, 0, i, 5] * width)
            lower_right_y = int(detected_objects[0, 0, i, 6] * height)

            prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
            cv2.rectangle(image, (upper_left_x,upper_left_y),(lower_right_x,lower_right_y), colors[class_index], 3)
            cv2.putText(image, prediction_text, (upper_left_x,
                    upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15),
                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[class_index],2)
            cv2.imshow("Detected Objects", image)
            cv2.waitKey(5)

            cap = cv2.VideoCapture('vtest.avi')

            ret, frame1 = cap.read()
            ret, frame2 = cap.read()

            while cap.isOpened():
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)

                    if cv2.contourArea(contour) < 700:
                        continue
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame1, "Status:movement".format('move'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 3)

                # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

                cv2.imshow("inter", frame1)
                frame1 = frame2
                ret, frame2 = cap.read()
                if cv2.waitKey(40) == 27:

cv2.destroyAllWindows()
cap.release()