# Scanning Projector Slides
TL;DR Low cost approach to capture slides using a webcam, USB Relay and hacked slide projector. Software to adjust camera, capture slides and pick slide to save.

![Setup of projector, actuating solenoid, camera and laptop](/Setup/IMG_3772.jpg?raw=true "Setup of projector, actuating solenoid, camera and laptop")

Like many, my father took 100s of slides when I was a kid and to get them all digitized is quite expensive. So, this is an approach to capture images using a USB web camera, USB controlled relay to activate the slide projector's advance and Python running on an old laptop to glue it all together.
My fathers projector is a basic unit that did not have an external slide advance remote control, so I had to put a solenoid on the side to actuate. If you have a remote, you could directly wire it to the USB controlled relay. 

I saw a gentleman’s YouTube on how to image slides that he directly imaged a backlite slide. I thought that would be a good approach as it will eliminate any parallax distortion. Like him I used a thin sheet of plastic to reduce the light level coming to the slide.
The low-cost camera - a $79 USB web camera of medium resolution 8MP. It has a low-quality camera lens on it.  I recommend replacing the camera lens with an SLR lens and a camera lens adapter.  eBay has old SLR lens that are 35mm you can get one pretty cheap.  It is all about the lens. Cheap lens and poor looking photos.  For the OEM lens I could not get consistent focus across the image. For the camera listed below I had to add a 5mm spacer to the 35mm lens.  The typical USB web camera has a CS lens body which already has a 5mm offset. If you use a web camera with a C-mount lens you will need an extra 5mm spacer. Adding spacers is one of the tricks for macro photography to turn a regular lens into a macro lens.

Taking photos – My father was not the greatest photographer, I can blame it on the camera tech of the 1970s and 80s – we are so lucky with the cameras on our phones. Many out of focus shots, many more with poor exposures, sometimes under and sometimes over. I could not do much about the out of focus shots, but for the exposure issues, I take 3 shots at different exposures, one normal, one step above and one step below. Then using a 3rd tool, a slide picker, I bring up all three and then chose the best looking. The slide picker can also rotate and flip slides to handle slides in backwards or upside down. 
Materials
* Projector
* USB web camera 
    * Lens 5-50mm Manual Focus Webcam,8MP High Resolution Web Camera 3264x2448 USB Camera with Sony IMX179 Sensor
    * https://www.amazon.com/SVPRO-Resolution-3264x2448-Computer-Windows/dp/B07CSKXB72/
    * The lens has distortion when doing macro photography. Upgrade the lens.
    * Most any of the high-resolution low-cost web cameras would work. 
* Nice lens on cheap web camera – next time I would buy a used 35mm SLR lens from eBay.
    * Use a C mount lens adapter. eBay and B&H Video have them for $30. Search for “Nikon Lens Adapter C Mount”
* You might need a 5mm C or CS mount lens extension. Like 5 dollars from eBay or Amazon.  C and CS mounts are the same thread, just C mount camaras have the lens threads closer to the sensor and you might need 5mm extension to get a total of 45mm. 
* Thin sheet of plastic to mute projector bulb, 0.10” thick, extruded, white.
* USB Controlled Relay – liked this model because it needed only simple commands to actuate.
    * Dual-Channel 2-Channel USB Relay Module 5V Relay Module Onboard CH340 Microcontroller Chip USB https://www.amazon.com/Buying-Dual-Channel-Microcontroller-Intelligent-Overcurrent/dp/B0B64TNS2C/ 2 for $17
* 12V solenoid (need to match power supply)
    * DC 12V 300 mA, Push Pull Type, Force 5N, Travel 10mm, Linear Solenoid
    * https://www.amazon.com/FainWan-Electromagnet-JF-0530B-keepping-Solenoid/dp/B09L6ZXY61/ $13
    * The slide advance was a very light touch and this did a good job. You just need to mount it a bit above the button so that it can overcome inertia and be able to pull in completely.
* 12 VDC power supply that can handle 600mA. $5 on eBay. Old wall bricks could work. 
* Double sided tape – to hold the solenoid to the side of the projector.
* Small wire, coat hanger, that goes true solenoid and pushes buttons. 
* Wire and wire strippers to go between the Power Supply a relay and solenoid.
* Method to hold camera (I used a mid-grade tripod)

## Getting started
* On Windows, download Python from Windows store uses Python, version 3.11 or latest
* Download the files in this project and unzip on your C drive.
* Install a couple dependencies for PySimpleGUI, OpenCV, Pillow see file “Installs.txt” for pip commands.
* Hook up your web cam (Note the WEBCAM number might need changing depending on how many cameras are attached to your PC. Look in “camSettings.py” line 89 and “Capture.py” line 37. 
* Hook up relay module (Note the relay module could appear on a different COM port then mine. Look in Windows “Device Manager” for the Ports. Then edit line 27 of the file ChangeSlide.py. 
* If using a projector without a remote, attach solenoid on to side of projector with double sided tape. Solenoids need to match your power supply. They do not care how they are hooked up (polarity). One wire goes to the power supply ground, the other to the relay common terminal. The positive power supply lead needs to go to the normally open terminal on the relay. When running the Capture.py program it will actuate the relay and it will click, and the solenoid will pull in triggering the projector’s advanced button. On the bottom of the relay module look for NO1 and COM1.
    * If using a remote, I am guessing when you open you will see switches under the buttons. Hopefully you can get to the wires and clip into them. Then one wire goes to Normally Open and the other to Common on the relay.
* Modify projector – add plastic sheet to mute projector bulb. I used a thin 0.010” (0.9mm) thick piece of plastic. It needs to be white and uniform when looking at it. I would guess it was extruded. I tried white plastic from a restaurant food container but the injection stress marks were obvious. You need about a 3” x 2.5” section. As the photo below shows it slides in besides the lens compartment door. 
* Clean the lenes near the bulb.
* Remove the main focus lens, just keep extending with the knob and pull on the lens. Easy to pull out and put back in.
* Place camera on tripod and have about 12” from slide.
* Line up, and set lens aperture to about ½ way.
* Use the “camSettings.py” (or regular camera app) to set focus and alignment.
* Using camSettings, turn off autoexposure and set color balance etc.. to your liking.
    * Note – unplugging camera or switching to MS Camera app will reset the settings.
* Open up “Capture.py” and set a destination directory. Set number of slides in carousel. 
* Start capturing slides.
* After capture use “SlideReview.py” to open a folder and review the 3 captures. 
    * Rotate/flip slide as nessary.
    * Click the slide you want to click and it will put the other 2 in an ‘Attic’ subfolder and advance to next slide.

## Three Python Programs
There are three programs that are used for this project.  The first one ‘camSettings.py’ is used for setting up the camera.  The cheap webcam do not have good profiles and you need to tweak the exposure, color balance and things like that.  My original slides had terrible exposures so I took three fixed exposures I mentioned above.
The second piece of software is “Capture.py”, it allows you to pick the destination folder, set the number of slides in the carousel, and start the capture process.  It assumes the first slide is loaded and illuminated. Under the hood it takes the three different exposure photos, names them, saves them then activates the projector advance button via the solenoid.  The solenoid does not need a very long push just a quarter of a second. After advancing the software sets the exposure and takes a photo in a few seconds. Then switches to the other 2 exposure and repeating. Taking the photos only takes a about 8  seconds so you can roll through the carousel pretty fast. I just start it and walk away.
The last part of the process is to look through all the slides captured using SlideReview.py . Because we took three exposures, we need to pick which one is the best.  There is likely upside down and backwards slides which we can fix. There are buttons to rotate and flip a slide. Then click on the one that you want to keep.  The other two are thrown into an attic sub folder.  Clicking through the slides is pretty quick, a few seconds if you do not get distracted. Program will then load the next slide set.
I still have some more to do, but so far I have captured 873 good slides.  Because they are digital on the cloud and on memory sticks, they are safer and more accessible than ever before. 



![Setup of projector, actuating solenoid, camera and laptop](/Setup/IMG_3795.jpg?raw=true "Setup of projector, actuating solenoid, camera and laptop with high quality lens")

![Close up of the solenoid](/Setup/IMG_3853.jpg?raw=true "Close up of solenoid")

![Gap in light bulb door that thin sheet of plastic slides into.](/Setup/IMG_3854.jpg?raw=true "Gap in light bulb door that thin sheet of plastic slides into.")
