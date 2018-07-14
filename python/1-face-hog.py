import sys
import cv2
import dlib
import os
from skimage import feature
from skimage import exposure

# Please download the trained face detection model on
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# (the file is too big, so I can't add it in the repo)
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Taking the image from cli param
file_path = sys.argv[1]

# Getting just the image name and extension
file_name = os.path.basename(file_path)

output_path = "output/hogProcess/"

# Loading the image object
original_image = cv2.imread(file_path)

# Converting to greyscale
greyscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Saving the greyscale image
cv2.imwrite(output_path + "greyscale-" + file_name, greyscale_image)

# Generating histogram of oriented gradients
(H, hog_image) = feature.hog(greyscale_image,
                            orientations=9,
                            pixels_per_cell=(8, 8),
                            cells_per_block=(2, 2),
                            transform_sqrt=True,
                            visualise=True)
hog_image = exposure.rescale_intensity(hog_image, out_range=(0, 255))
hog_image = hog_image.astype('uint8')

# Saving the hog image
cv2.imwrite(output_path + "hog-" + file_name, hog_image)

face_detector = dlib.get_frontal_face_detector()

# Detecting faces in the hog
detected_faces = face_detector(original_image, 1)

# Drawing squares on the faces
for item in detected_faces:
    cv2.rectangle(hog_image, (item.left(), item.top()), (item.right(), item.bottom()), (255, 0, 0), 2)

# Saving the hog image with the face detection
cv2.imwrite(output_path + "hog-with-faces-" + file_name, hog_image)

print("The generated images are stored in " + output_path)
