import os

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
imgBackground = cv2.imread("Resources/background.jpg")
folderModePath = "Resources/Modes"
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame")
        break
    imgBackground[125:125+480 , 145:145+640] = img
    imgBackground[115:115+490 , 820:820+340] = imgModeList[3]
    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
