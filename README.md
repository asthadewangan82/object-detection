Overview of the Project
-This project is created using Python and OpenCV. It detects objects like people or faces in an image. When the image is run through the program, it highlights the detected objects by drawing boxes around them. This project is great for beginners who want to learn about computer vision.

About the Files
-There are two main Python files in this project. The main.py file is the starting point of the program. It loads the image and calls the detection function. The second file is objectdetection.py, which contains the object detection logic using OpenCV. Along with these files, there are some sample images such as room.jpg, roomwithpeople.jpg, and street.jpg that are used for testing.

How to Run the Project?
-First, make sure Python is installed on your system. It's better to use Python version 3.6 or above. Then, install the required libraries by running the command:
-pip install opencv-python numpy
-Once the setup is done, you can run the program by using this command:
  . python main.py

What You Will See in the Output?
-After running the program, one of the sample images will open in a new window. If any object is detected in the image, a box will appear around it. You will see the output image with highlighted objects.

How to Change the Image?
-If you want to test a different image, open the main.py file and change the following line:
image = cv2.imread("roomwithpeople.jpg")
You can replace it with "room.jpg" or "street.jpg" as per your choice.

Future Ideas?
-You can improve this project in many ways. You can add real-time object detection using a webcam or work with video files. You can also use deep learning models like YOLO for more accurate and faster detection.

About the Creator
-This project is created by Astha Dewangan, a final-year Computer Science student. She built this project to explore the basics of computer vision and object detection using OpenCV.

