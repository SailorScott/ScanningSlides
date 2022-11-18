import multiprocessing

import cv2

video_capture_device_index = 0


def imageDisplay(state):
    print("imageDisplay")
    while True:
        webcam = cv2.VideoCapture(video_capture_device_index)
        ret, frame = webcam.read()  # Read image from capture device (camera)
        # imgbytes = cv2.imencode(".ppm", frame)[
        #     1
        # ].tobytes()  # can also use png.  ppm found to be more efficient

        # window["-IMAGE-"].update(data=imgbytes)
        cv2.imshow("image", frame)
        print("frame")
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == "__main__":
    # creating processes for each of the functions
    t = multiprocessing.Process(target=imageDisplay, args=(True,))
    t.start()
