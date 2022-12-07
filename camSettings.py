# Capture an image of a slide and save into local drive.
# Using a low cost usb camera, capture the slide and save.
# Rotate the image to fit the slide's form factor
# Advance the slide projector by sending a command to a USB - relay PCB.

import time

import cv2
import PySimpleGUI as sg

cvDictionay = {
    "CAP_PROP_BRIGHTNESS": cv2.CAP_PROP_BRIGHTNESS,
    "CAP_PROP_CONTRAST": cv2.CAP_PROP_CONTRAST,
    "CAP_PROP_SATURATION": cv2.CAP_PROP_SATURATION,
    "CAP_PROP_HUE": cv2.CAP_PROP_HUE,
    "CAP_PROP_GAIN": cv2.CAP_PROP_GAIN,
    "CAP_PROP_GAMMA": cv2.CAP_PROP_GAMMA,
    "CAP_PROP_SHARPNESS": cv2.CAP_PROP_SHARPNESS,
    "CAP_PROP_EXPOSURE": cv2.CAP_PROP_EXPOSURE,
    "CAP_PROP_AUTO_EXPOSURE": cv2.CAP_PROP_AUTO_EXPOSURE,
}

sg.theme("Black")
# Setup user interface
layout = [
    [
        sg.Text("Folder for images"),
        sg.Input(key="folder", default_text="C:\\Slides"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("CAP_PROP_BRIGHTNESS (default 0"),
        sg.Input(key="CAP_PROP_BRIGHTNESS"),
        sg.Button("Change CAP_PROP_BRIGHTNESS"),
    ],
    [
        sg.Text("CAP_PROP_CONTRAST (default 32"),
        sg.Input(key="CAP_PROP_CONTRAST"),
        sg.Button("Change CAP_PROP_CONTRAST"),
    ],
    [
        sg.Text("CAP_PROP_SATURATION (default 75"),
        sg.Input(key="CAP_PROP_SATURATION"),
        sg.Button("Change CAP_PROP_SATURATION"),
    ],
    [
        sg.Text("CAP_PROP_HUE (default 0"),
        sg.Input(key="CAP_PROP_HUE"),
        sg.Button("Change CAP_PROP_HUE"),
    ],
    [
        sg.Text("CAP_PROP_GAIN (default 0"),
        sg.Input(key="CAP_PROP_GAIN"),
        sg.Button("Change CAP_PROP_GAIN"),
    ],
    [
        sg.Text("CAP_PROP_GAMMA (default 0"),
        sg.Input(key="CAP_PROP_GAMMA"),
        sg.Button("Change CAP_PROP_GAMMA"),
    ],
    [
        sg.Text("CAP_PROP_SHARPNESS (default 3)"),
        sg.Input(key="CAP_PROP_SHARPNESS"),
        sg.Button("Change CAP_PROP_SHARPNESS"),
    ],
    [
        sg.Text("CAP_PROP_EXPOSURE (default -7?)"),
        sg.Input(key="CAP_PROP_EXPOSURE"),
        sg.Button("Change CAP_PROP_EXPOSURE"),
    ],
    [
        sg.Text("CAP_PROP_AUTO_EXPOSURE (default -1?)"),
        sg.Input(key="CAP_PROP_AUTO_EXPOSURE"),
        sg.Button("Change CAP_PROP_AUTO_EXPOSURE"),
    ],
    [sg.Text(key="-STATUS-", text="Status...")],
    [sg.Exit(), sg.Button("Start taking photos")],
    [
        sg.Image(
            filename="",
            key="-IMAGE-",
            tooltip="Right click for exit menu",
            size=(1280, 720),
        )
    ],
]
window = sg.Window("Slide photo capture", layout=layout, location=(0, 0))

WEBCAM = 2
webcam = cv2.VideoCapture(WEBCAM, cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)


def NowTenthsSecond():
    return int(time.time_ns() / 100000000)


def Image_Display():
    # Update the visual display in the UI.
    ret, frame = webcam.read()
    if ret:
        imgbytes = cv2.imencode(".ppm", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)


def SavePhoto(pathFileName):
    ret, frame = webcam.read()
    flipped = cv2.flip(frame, 1)
    cv2.imwrite(pathFileName, flipped)


def propLookup(propName: str):
    return cvDictionay[propName]


# setup main UI loop
while True:
    event, values = window.read(timeout=50, timeout_key="StateMachine")

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "StateMachine":
        Image_Display()

    if event == "Start taking photos":
        # check we have values for slide count
        SavePhoto(values["folder"])

    if event.startswith("Chang"):
        prop = event[7:]
        print("Prop:", prop)

        if values[prop]:
            print("Value", values[prop])
            print("Enum:", propLookup(prop))
            webcam.set(propLookup(prop), float(values[prop]))
        else:
            print("NO VALUE!!")
window.close()
