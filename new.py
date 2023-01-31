import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

img = cv.imread("2.PNG")

# code = decode(img)
# cap = cv.VideoCapture(0)

with open('data.text') as f:
    myDataList = f.read().splitlines()

print(myDataList)

color = (0,255,255)
# print(code)
while True:
    # Success, frame = cap.read()

    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode("utf-8")
        print(myData)

        if myData in myDataList:
            print("Authorized Person")
            color = (0,255,0)
        else:
            print("Unauthorized Person")
            color = (0,0,255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img, [pts], True, color, 2)

        pts2 = barcode.rect

        cv.putText(img, myData, (pts2[0], pts2[1]), cv.FONT_HERSHEY_SIMPLEX,
                    0.6, color, 2)

    cv.imshow("QR Reader", img)
    
    key = cv.waitKey(1)

    if key == ord("q"):
        # cap.release()
        cv.destroyAllWindows()
        break

# cap.release()
cv.destroyAllWindows()