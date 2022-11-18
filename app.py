# Capture an image of a slide and save into local drive.
# Using a cell phones camera, capture the slide via a Wi-Fi streaming app.
# Rotate and crop the image to fit the slide's form factor
# Advance the slide projector by sending a command to a USB - relay PCB.

import multiprocessing

import cv2

# import ChangeSlide
import PySimpleGUI as sg

sg.theme("Black")
# Setup user interface
layout = [
    [
        sg.Image(
            filename="",
            key="-IMAGE-",
            tooltip="Right click for exit menu",
            size=(800, 640),
        )
    ],
    [
        sg.Text("Folder for images"),
        sg.Input(key="folder", default_text="c:\\temp"),
        sg.FolderBrowse(),
    ],
    [sg.Text("Last slide number in carousel"), sg.Input(key="slideCount")],
    [sg.Exit(), sg.Button("Start taking photos")],
]

window = sg.Window("Slide photo capture", layout=layout)

url = "http://192.168.1.180/billed.jpg"
video_capture_device_index = 0


def imageDisplay(state):

    while True:
        webcam = cv2.VideoCapture(video_capture_device_index)
        ret, frame = webcam.read()  # Read image from capture device (camera)
        # imgbytes = cv2.imencode(".ppm", frame)[
        #     1
        # ].tobytes()  # can also use png.  ppm found to be more efficient

        # window["-IMAGE-"].update(data=imgbytes)
        cv2.imshow("image", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


t = multiprocessing.Process(target=imageDisplay, args=(True,))


# setup main UI loop
while True:
    event, values = window.read(timeout=500)

    # imgbytes = cv2.imencode(".png", frame)[
    #     1
    # ].tobytes()  # Convert the image to PNG Bytes

    # frame = cv2.imread(
    #     url,
    #     flags=cv2.IMREAD_COLOR,
    # )

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "Start taking photos":
        t.start()
        print("Take Photos now, for slide count:" + values["slideCount"])
        # print("store in folder:" + values["folder"] + "\\image1.png")
        # cv2.imwrite(values["folder"] + "\\image1.png", imgbytes)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# t.stop()

window.close()


# start taking photos
