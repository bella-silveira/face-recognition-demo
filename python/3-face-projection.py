import sys
import os
import dlib
import cv2
import openface

# Please download the trained face detection model on
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# (the file is too big, so I can't add it in the repo)
predictor_model = "shape_predictor_68_face_landmarks.dat"
output_path = "output/alignedFaces/"

# Creating a histogram of oriented gradients detector
face_detector = dlib.get_frontal_face_detector()
face_angle_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

# Taking the image from cli param
file_path = sys.argv[1]

# Getting just the image name and extension
file_name = os.path.basename(file_path)

# Loading the image object
image = cv2.imread(file_path)

# Running the HOG face detector on the image we just loaded
detected_faces = face_detector(image, 1)

print("Found {} faces in this image {}".format(len(detected_faces), file_path))

# Iterate over the faces we found
for i, face_rect in enumerate(detected_faces):

	# Calculating each face's landmarks
	pose_landmarks = face_angle_predictor(image, face_rect)

	# Calculating and applying alignment on each face
	alignedFace = face_aligner.align(534, image, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

	# Saving aligned faces to the alignedFaces folder
	cv2.imwrite(output_path + "aligned-face-" + str(i) + "-" + file_name, alignedFace)

print("The generated images are stored in " + output_path)