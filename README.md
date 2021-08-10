# Hand-gesture-recogniton-for-recognised-faces

Run Details:
1)capturing images and setting up the face recognition part
2)Run web.py


3.DESIGN

3.1. WEB BUTTON
The GUI onclick button has been implemented with the help of tkinter library. Tkinter
is Python’s standard GUI (Graphical User Interface) package. It is one of the most
commonly used packages for GUI applications which comes with Python itself.

3.2. FACE RECOGNITION
Initially taking the input data using ‘FaceCapturing.py’. In this file, the input will be
taken in the form 100 images through camera. Those images will be cropped for the
faces using haarcascade_frontalface_default.xml. Those cropped images will be stored
in a folder ‘images’ which was created by me as the output with labelling 1 to 100. Then
we created out own datasets which contains ‘Train’ and ‘Test’ folders, which are filled
with the data saved in the images folder. After that building a face recognition model
followed by training and testing the model using the datasets created by us using
‘FaceRecognizing.py’ file. Finally running the loaded model with the real time input
through camera. If the recognized faces are identified then it will display the name of
face and go with gesture recognition. If no face is identified then it will display the
statement no face found using ‘IdentifyingFaces.py’.

3.3. GESTURE RECOGNITION
The module gesture recognition has been implemented mainly using the OpenCV
library. After capturing through video, the image is processed using various OpenCV
functions. The hand gestures in the project are recognized using the contours and
convexity defect concept. These defects are found out with the help of cosine function.
Based on the defect count we have added the respective gesture functions using
PyAutoGUI library.

4.Implmentation

4.1. Language:
• Python
4.2. Tools:
• PyCharm IDE
• Atom
4.3. Libraries:
• Tkinter
• Os
• OpenCv
• Numpy
• Keras
• Matplotlib.pyplot
• Glob
• Io
• Json
• Random
• Base64
• Pyautogui
4.4. Modules:
• Face_extractor() :- This module detects faces and returns cropped faces. If no
face is found, returns the input image.
