import cv2 as cv
import shutil
import os
import sys

INPUT_DIR = 'crawled'
OUTPUT_BASE = 'labeled'
WINDOW_NAME = 'Pig? (y/*)'

MAX_HEIGHT = 500
MAX_WIDTH = 500

def main():

    with open('links.txt', 'r') as f:
            lista = f.readlines()

    # print(lista)

    cv.namedWindow(WINDOW_NAME)

    output_dir = os.path.join(OUTPUT_BASE, 'pig')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for name in sorted(os.listdir(INPUT_DIR)):
        input_path = os.path.join(INPUT_DIR, name)
        int_name = int(name.split(".")[0])
        link = lista[int_name - 1]

        image = cv.imread(input_path)

        image = cv.putText(
        img = image,
        text = link,
        org = (200, 200),
        fontFace = cv.FONT_HERSHEY_DUPLEX,
        fontScale = 3.0,
        color = (0, 0, 0),
        thickness = 3
        )

        height, width, _ = image.shape
        ratio = height / width

        if height > width:
            new_width = round(MAX_HEIGHT / ratio)
            resized_image = cv.resize(image, (new_width, MAX_HEIGHT))
        else:
            new_height = round(MAX_WIDTH * ratio)
            resized_image = cv.resize(image, (MAX_WIDTH, new_height))

        cv.imshow(WINDOW_NAME, resized_image)

        while True:
            if cv.getWindowProperty(WINDOW_NAME, cv.WND_PROP_VISIBLE):
                key = cv.waitKey(1000) # um segundo
            else:
                key = ord('q')

            if key != -1:
                break

        if key == ord('q'):
            break

        if key == ord('y'):
            output_path = os.path.join(output_dir, name)
            shutil.copy(input_path, output_path)

    cv.destroyWindow(WINDOW_NAME)
    return 0

if __name__ == '__main__':
    sys.exit(main())
