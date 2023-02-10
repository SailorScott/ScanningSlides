# Capture an image of a slide and save into local drive.
# Using a low cost usb camera, capture the slide and save.
# Rotate the image to fit the slide's form factor
# Advance the slide projector by sending a command to a USB - relay PCB.
# © SailorScott 2023


import os
import time

import ChangeSlide as changeSlide
import cv2
import PySimpleGUI as sg
import StateMachine as states

sg.theme("Black")
# Setup user interface
layout = [
    [
        sg.Text("Folder for images"),
        sg.Input(key="folder", default_text="C:\\Slides"),
        sg.FolderBrowse(),
    ],
    [sg.Text("Last slide number in carousel"), sg.Input(key="slideCount")],
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
window = sg.Window("Slide photo capture", layout=layout)

######### Webcamera setup #############
WEBCAM = 1
webcam = cv2.VideoCapture(WEBCAM, cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 3264)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2448)


stateInfo = states.StateInfo()


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


def State_Machine():
    # Sequence of states: (assumes first slide is already in view of camera. )
    #   Save Photo
    #   Incrument slide counter, check if done with caroucel
    # #   Advanced Button Down
    #   Wait 2 seconds
    #   Advanced Button Up
    #   Wait 4 seconds for contrast to stabalize
    #   Check if more, then go to Save Photo
    #

    Current_Time = NowTenthsSecond()

    if Current_Time >= stateInfo.Action_Time:
        if stateInfo.Action == "SavePhoto":
            print("savePhoto(slideCounter)")
            webcam.set(cv2.CAP_PROP_EXPOSURE, float(-6))
            time.sleep(2.0)
            pathFileName = (
                stateInfo.Folder + "Slide-{}-1".format(stateInfo.SlideCounter) + ".png"
            )
            SavePhoto(pathFileName)
            stateInfo.Action_Time = Current_Time + 1  # 0.1 seconds
            stateInfo.Action = "SavePhoto-1"

        elif stateInfo.Action == "SavePhoto-1":
            print("savePhoto(slideCounter)")
            webcam.set(cv2.CAP_PROP_EXPOSURE, float(-7))
            time.sleep(2.0)
            pathFileName = (
                stateInfo.Folder + "Slide-{}-2".format(stateInfo.SlideCounter) + ".png"
            )
            SavePhoto(pathFileName)
            stateInfo.Action_Time = Current_Time + 3  # 0.1 seconds
            stateInfo.Action = "SavePhoto-2"

        elif stateInfo.Action == "SavePhoto-2":
            print("savePhoto(slideCounter)")
            webcam.set(cv2.CAP_PROP_EXPOSURE, float(-8))
            time.sleep(2.0)
            pathFileName = (
                stateInfo.Folder + "Slide-{}-3".format(stateInfo.SlideCounter) + ".png"
            )
            SavePhoto(pathFileName)
            stateInfo.Action_Time = Current_Time + 3  # 0.1 seconds
            stateInfo.Action = "ButtonDown"

        elif stateInfo.Action == "ButtonDown":
            print("Button Down")
            changeSlide.push_button_down()
            stateInfo.Action_Time = Current_Time + 3  # 0.1 seconds
            stateInfo.Action = "ButtonUp"

        elif stateInfo.Action == "ButtonUp":
            print("Button Up")
            changeSlide.push_button_up()
            stateInfo.Action_Time = Current_Time + 60  #  tenths seconds
            stateInfo.Action = "CheckMorePhotos"

        elif stateInfo.Action == "CheckMorePhotos":
            print("CheckMorePhotos")
            stateInfo.SlideCounter += 1
            if stateInfo.SlideCounter <= stateInfo.TotalSlides:
                window["-STATUS-"].update("Slide {}".format(stateInfo.SlideCounter))
                stateInfo.Action = "SavePhoto"
            else:
                stateInfo.Action = "Done"

        elif stateInfo.Action == "Done":
            print("Done")
            stateInfo.Action = ""
            window["-STATUS-"].update("DONE!!")


# setup main UI loop
while True:
    event, values = window.read(timeout=100, timeout_key="StateMachine")

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "StateMachine":
        State_Machine()
        Image_Display()

    if event == "Start taking photos":
        # check/create folder
        folder = values["folder"] + "\\"
        if not os.path.exists(folder):
            os.mkdir(folder)

        # check we have values for slide count
        slideCount = values["slideCount"].strip()
        if len(slideCount) == 0:
            sg.popup("please enter a slide count")
        else:
            print("Take Photos now, for slide count:" + slideCount)
            print("store in folder:" + values["folder"] + "\\image1.png")
            stateInfo.TotalSlides = int(slideCount)
            stateInfo.Folder = values["folder"] + "\\"
            stateInfo.Action_Time = NowTenthsSecond()
            stateInfo.SlideCounter = 0
            stateInfo.Action = "CheckMorePhotos"
            window["-STATUS-"].update("Starting..")

window.close()
