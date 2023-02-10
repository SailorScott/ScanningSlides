"""
Review of images, selection of the best. With capture took 2 or 3 exposures, and this form is to allow review and selecting of best.
Display the photos side by side, and then click the corresponding keep button. The other 1 or 2 get sent to Attic folder.
Optional functions to flip the photo if backwards.
Loops through the folder getting the images.

© SailorScott 2023
"""

import io
import os
import shutil

import PySimpleGUI as sg
from PIL import Image

sg.theme("Material1")

IMAGE_WIDTH = 1088
IMAGE_HEIGHT = 816

slideCount = 0
# Setup user interface
col1 = [
    [
        sg.Button("Flip 1"), sg.Button("Rotate 1"),
        sg.Image(
            filename="",
            key="-IMAGE1-",
            tooltip="Right click for exit menu",
            size=(IMAGE_WIDTH, IMAGE_HEIGHT),
            enable_events=True,
        ),
    ]
]
col2 = [
    [
        sg.Button("Flip 2"), sg.Button("Rotate 2"),
        sg.Image(
            filename="",
            key="-IMAGE2-",
            tooltip="Right click for exit menu",
            size=(IMAGE_WIDTH, IMAGE_HEIGHT),
            enable_events=True,
        ),
    ]
]
col3 = [
    [
        sg.Button("Flip 3"), sg.Button("Rotate 3"),
        sg.Image(
            filename="",
            key="-IMAGE3-",
            tooltip="Right click for exit menu",
            size=(IMAGE_WIDTH, IMAGE_HEIGHT),
            enable_events=True,
        ),
    ]
]

layout = [
    [
        sg.Text("Folder for images"),
        # sg.Input(size=(25, 1), key="-FILE-", default_text="C:\\ScottsProjects\\Slides\\car3\\Slide-1-1.png"),
        sg.Input(key="-FOLDER-", default_text="C:\\ScottsProjects\\Slides"),
        sg.FolderBrowse(),
        sg.Button("Load Images"),
    ],
    # [sg.Text("Last slide number in carousel"), sg.Input(key="slideCount")],
    [sg.Text(key="-STATUS-", text="Status...")],
    [
        sg.Exit(),
        sg.Button("Delete All Images"),
        sg.Button("Next Image"),
    ],
    [sg.Column(col1), sg.Column(col2), sg.Column(col3)],
]
window = sg.Window("Slide photo capture", layout=layout)


# Take one slide refence and build up the 3 exposures
def nextImages(slideCount):
    folder = values["-FOLDER-"]
    loadImage(folder, slideCount, 1)
    loadImage(folder, slideCount, 2)
    loadImage(folder, slideCount, 3)
    window["-STATUS-"].update("Slide" + str(slideCount))


# load a file into the image viewer.
def loadImage(folderName, slideNum, exposureNum):
    filename = folderName + "\\Slide-" + str(slideNum) + "-" + str(exposureNum) + ".png"
    if os.path.exists(filename):
        image = Image.open(filename)
        image.thumbnail((IMAGE_WIDTH, IMAGE_HEIGHT))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE" + str(exposureNum) + "-"].update(data=bio.getvalue())
    else:
        window["-IMAGE" + str(exposureNum) + "-"].update(None)

def FlipImage(slideNum, exposureNum):
    TransposeImage(slideNum, exposureNum, Image.Transpose.FLIP_LEFT_RIGHT)
    
def RotateImage(slideNum, exposureNum):
    TransposeImage(slideNum, exposureNum, Image.Transpose.ROTATE_90)

def TransposeImage(slideNum, exposureNum, transpose):
    folderName = values["-FOLDER-"]
    source = (
            folderName + "\\Slide-" + str(slideNum) + "-" + str(exposureNum) + ".png"
        )
    print("Transpose:", source)
    image = Image.open(source)
    out = image.transpose(transpose)
    out.save(source)

def SaveThisOne(slideNum, saveExposureNum):
    print("SaveThisOne:", saveExposureNum)
    folderName = values["-FOLDER-"]

    for exposureNum in range(1, 4):
        if int(saveExposureNum) != exposureNum:
 
            source = (
                folderName + "\\Slide-" + str(slideNum) + "-" + str(exposureNum) + ".png"
            )
            if os.path.exists(source):
                destination = (
                    folderName
                    + "\\Attic\\Slide-"
                    + str(slideNum)
                    + "-"
                    + str(exposureNum)
                    + ".png"
                )
                shutil.move(source, destination)


# setup main UI loop
slideCount = 1
while True:
    event, values = window.read(timeout=1000)

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "Load Images":
        window["-STATUS-"].update("loading..")
        slideCount = 1
        folder = values["-FOLDER-"] 
        if not os.path.exists(folder + "\\Attic"):
            os.mkdir(folder + "\\Attic")
        nextImages(slideCount)

    if event in ("-IMAGE1-", "-IMAGE2-", "-IMAGE3-"):
        image2Save = event[6:7]
        SaveThisOne(slideCount, image2Save)
        slideCount += 1
        nextImages(slideCount)

    if event in ("Flip 1", "Flip 2", "Flip 3"):
        image2Save = event[5:6]
        FlipImage(slideCount, image2Save)
        nextImages(slideCount)

    if event in ("Rotate 1", "Rotate 2", "Rotate 3"):
        image2Save = event[7:8]
        RotateImage(slideCount, image2Save)
        nextImages(slideCount)

    if event == "Next Image":
        slideCount += 1
        nextImages(slideCount)

    if event == "Delete All Images":
       SaveThisOne(slideCount, 0)
       slideCount += 1
       nextImages(slideCount)


    # if event == "Start taking photos":
    #     # check/create folder
    #     folder = values["folder"] + "\\"
    #     if not os.path.exists(folder):
    #         os.mkdir(folder)

    #     # check we have values for slide count
    #     slideCount = values["slideCount"].strip()
    #     if len(slideCount) == 0:
    #         sg.popup("please enter a slide count")
    #     else:
    #         print("Take Photos now, for slide count:" + slideCount)
    #         print("store in folder:" + values["folder"] + "\\image1.png")
    #         stateInfo.TotalSlides = int(slideCount)
    #         stateInfo.Folder = values["folder"] + "\\"
    #         stateInfo.Action_Time = NowTenthsSecond()
    #         stateInfo.SlideCounter = 0
    #         stateInfo.Action = "CheckMorePhotos"
    #         window["-STATUS-"].update("Starting..")

window.close()
