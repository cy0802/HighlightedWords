import cv2
import numpy as np
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 去除奇怪符號要用的


def f(n):
    m = ord(n)
    if((m >= 65 and m <= 90) or (m >= 97 and m <= 122) or n == ' ' or n == '\n'):
        return 1
    else:
        return 0


def not_empty(s):
    return s and s.strip()


def ImgToStr(path):
    # 讀圖片進來
    img = cv2.imread(path)
    # 轉hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 選取螢光筆區域
    Mask = cv2.inRange(hsv, (25, 60, 100), (35, 255, 230))

    # 找螢光筆區域的邊界
    contours, hi = cv2.findContours(
        Mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 找螢光筆區域邊界外的最小長方形
    for bbox in contours:
        [x, y, w, h] = cv2.boundingRect(bbox)
        # 填成白色 -1是填滿的意思
        cv2.rectangle(Mask, (x, y), (x + w, y + h), 255, -1)
    # mask和原圖and起來
    masked = cv2.bitwise_and(img, img, mask=Mask)

    # 轉灰階
    gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    # 將黑色部分填成白色
    gray[gray == 0] = 255

    # 找ROI中的最大最小值平均
    Min, Max, Min_p, Max_p = cv2.minMaxLoc(gray, mask=Mask)
    avg = (Min+Max)/2
    # 二值化
    ret, th1 = cv2.threshold(gray, avg, 255, cv2.THRESH_BINARY)

    #cv2.namedWindow('th1', cv2.WINDOW_NORMAL)
    # cv2.imshow('original',img)
    # cv2.imshow('mask',Mask)
    # cv2.imshow('th1',th1)

    # OCR
    ocr = pytesseract.image_to_string(th1, lang="eng")

    # 過濾奇怪符號
    filtered = filter(f, ocr)
    string = ''.join(list(filtered))
    # 切割字串
    Str = string.split()
    # print(Str)

    # 將list中空字串過濾掉
    words = list(filter(not_empty, Str))
    # print(words)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return words


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
    words = ImgToStr(r'img_testdata\141491.jpg')
    print(words)
