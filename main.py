import cv2


def show_image_opencv(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('Press any key to close the viewer', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_image_opencv("./data/sample_image.jpg")
