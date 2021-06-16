import os 
import glob 
import cv2

def load_dataset(image_dir):

    image_list = []
    image_types = ["day","night"]

    for image_type in image_types:
        for file in glob.glob(os.path.join(image_dir,image_type,'*.jpg')):
            image = cv2.imread(file)

            if not image is None:
                image_list.append((image,image_type))
    

    return image_list


def standardize_input(img):
    return cv2.resize(img,(1100,600))


def encode(label):

    numerical_val = 0

    if label == 'day':
        numerical_val = 1
    
    return numerical_val


def standardize_list(img_list):
    standard_list = []

    for img,img_type in img_list:
        standardize_img = standardize_input(img)
        binary_label = encode(img_type)

        standard_list.append((standardize_img,binary_label))
    
    return standard_list
