
import cv2 as cv

src = cv.imread("D:/photo/jcb.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)
cv.destroyAllWindows()
print("hi")

#asdasd