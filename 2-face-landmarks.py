import sys
import dlib
from skimage import io

# Please download the trained face detection model on
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# (the file is too big, so I can't add it in the repo)
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Creating a histogram of oriented gradients detector
face_detector = dlib.get_frontal_face_detector()
face_angle_predictor = dlib.shape_predictor(predictor_model)

# Getting the X11 window (download XQuartz if you're using mac)
win = dlib.image_window()

# Taking the image from cli param
file_name = sys.argv[1]

# Loading the image object
image = io.imread(file_name)

# Running the HOG face detector on the image we just loaded
faces_on_picture = face_detector(image, 1)

print("Found {} faces in this image {}".format(len(faces_on_picture), file_name))

# Open X11 window with the image with detected faces
win.set_image(image)

# Iterate over the faces we found
for i, face_rect in enumerate(faces_on_picture):

	# Adding a border to each face
	win.add_overlay(face_rect)

	# Calculating each face's landmarks
	pose_landmarks = face_angle_predictor(image, face_rect)

	# Drawing the landmarks over the image
	win.add_overlay(pose_landmarks)

dlib.hit_enter_to_continue()