import cv2
import sys
if sys.platform=='win64':
    deltax=0
    deltay=0
else:
    deltax=50
    deltay=105

kamera = cv2.VideoCapture(0) 
kamera.set(3,640)
kamera.set(4,480)
while True:
    _, kare = kamera.read()
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (7, 7), 0)
    canny = cv2.Canny(blur, 30, 50)
    canny = cv2.bitwise_not(canny)

    imaj = cv2.bitwise_and(gri, gri, mask=canny)
    cv2.imshow("imaj", imaj)
    cv2.moveWindow('imaj',10,10)
    cv2.imshow("canny", canny)
    cv2.moveWindow('canny',imaj.shape[1]+deltax,10)
    k = cv2.waitKey(1)
    if k == 27 or k == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows