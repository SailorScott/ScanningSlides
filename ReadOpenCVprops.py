import cv2

cam = cv2.VideoCapture(2, cv2.CAP_DSHOW)

# showing values of the properties
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(cam.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("CAP_PROP_FPS : '{}'".format(cam.get(cv2.CAP_PROP_FPS)))
print("CAP_PROP_EXPOSURE : '{}'".format(cam.get(cv2.CAP_PROP_EXPOSURE)))
# print("CAP_PROP_POS_MSEC : '{}'".format(cam.get(cv2.CAP_PROP_POS_MSEC)))
# print("CAP_PROP_FRAME_COUNT  : '{}'".format(cam.get(cv2.CAP_PROP_FRAME_COUNT)))
print("CAP_PROP_BRIGHTNESS : '{}'".format(cam.get(cv2.CAP_PROP_BRIGHTNESS)))
print("CAP_PROP_CONTRAST : '{}'".format(cam.get(cv2.CAP_PROP_CONTRAST)))
print("CAP_PROP_SATURATION : '{}'".format(cam.get(cv2.CAP_PROP_SATURATION)))
print("CAP_PROP_HUE : '{}'".format(cam.get(cv2.CAP_PROP_HUE)))
print("CAP_PROP_BACKLIGHT  : '{}'".format(cam.get(cv2.CAP_PROP_BACKLIGHT)))
print("CAP_PROP_SHARPNESS  : '{}'".format(cam.get(cv2.CAP_PROP_SHARPNESS)))
print("CAP_PROP_GAMMA  : '{}'".format(cam.get(cv2.CAP_PROP_GAMMA)))
# print("CAP_PROP_CONVERT_RGB : '{}'".format(cam.get(cv2.CAP_PROP_CONVERT_RGB)))
print("CAP_PROP_AUTO_EXPOSURE : '{}'".format(cam.get(cv2.CAP_PROP_AUTO_EXPOSURE)))
# print("CAP_PROP_ISO_SPEED : '{}'".format(cam.get(cv2.CAP_PROP_ISO_SPEED)))


while True:
    check, frame = cam.read()

    cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == 99:
        print("CAP_PROP_BRIGHTNESS : '{}'".format(cam.get(cv2.CAP_PROP_BRIGHTNESS)))
    elif key == 100:
        cam.set(cv2.CAP_PROP_BRIGHTNESS, 0)

cam.release()
cv2.destroyAllWindows()
