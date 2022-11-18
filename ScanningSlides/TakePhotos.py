# given the number of slides in the carousel and folder name etc, 
# cycle through the slides and save them to the folder.


from pyclbr import Class
import string


class TakePhotos():



    def __init__(self, folder, imageNamePrefix):
        self.folder = folder
        self.imageNamePrefix = imageNamePrefix

    

    def takePhoto(self, slideNumber):
        # read image from phone and save, then crop and rotate as needed.