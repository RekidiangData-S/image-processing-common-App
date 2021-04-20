import cv2


def read_file(filename):
    img = cv2.imread(filename)
    # cv2_imshow(img)
    return img
