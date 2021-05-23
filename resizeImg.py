import cv2


def resize(path):
    src = cv2.imread(path)
    if src.shape[0] > 500 or src.shape[1] > 500:
        if(src.shape[0] > src.shape[1]):
            percent = src.shape[0] / 500
        else:
            percent = src.shape[1] / 500

        width = int(src.shape[1] / percent)
        height = int(src.shape[0] / percent)

        dsize = (width, height)
        output = cv2.resize(src, dsize)
        cv2.imwrite(path, output)


if __name__ == "__main__":
    resize("static/upload/93987.jpg")
    test = cv2.imread("static/upload/93987.jpg")
    print(test.shape)
