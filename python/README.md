# Face recognition demo

Hi all! Here you'll find a few python scripts to demonstrate the initial steps of the process of recognizing a face.

## Setup

To run this project, you'll need to instal:

- Python (I'm using 2.7, but you can use 3.5 too)
- OpenCV
- dlib
- scikit image
- OpenFace
- A X11 client (I'm using XQuartz for macOS, but feel free to use any other one)

Also don't forget to download the trained face recognition model on http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 and save it on the project root

## Running the files

To run any file in this project, you'll need to execute:

```
python [name-of-the-file] [path-of-the-image]
```

The generated images (if there's any, the second step only renders the image on the X11 client) are located on the `output` folder

The result of each step is independant, in other words, if you wanna skip straight to the face projection, you don't need to execute any of the other steps. They're just practical applications of the process involved in each part involved in recognizing a face using Machine Learning.

Happy hacking!

