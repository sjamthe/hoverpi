Detailed Steps
STEP 1: LOGIN TO YOUR PI
Replace HOSTNAME with the hostname of your Pi.

$ ssh pi@HOSTNAME.local
STEP 2: UPDATE THE OPERATING SYSTEM
$ sudo apt-get update
STEP 3: ENABLE THE CAMERA
Launch raspi-config:

$ sudo raspi-config
From the menu options:

Select: 6. Enable Camera
Click: Yes
Click: OK
Click: Finish
STEP 4: CREATE A PROJECT FOLDER
$ mkdir projects
$ cd projects/
STEP 5: DOWNLOAD MJPG-STREAMER
To download the project you will need a source control system called git. It may not be installed on a fresh image. I know it's not on the lite image. So you may need to install it. Not sure? Type git, hit return and see what happens.

$ sudo apt-get install git
Now that you have git installed, use it to clone a copy of the mjpg-streamer to your Pi.

$ git clone https://github.com/jacksonliam/mjpg-streamer.git
If you aren't familiar with it, git is a very handy tool used by most developers. When I start discussing code I will likely mention git a lot. Most people start with the free online book: Pro Git.

STEP 6: COMPILE MJPG-STREAMER
If you aren't familiar with compilers, don't panic. Just follow these steps and hopefully you won't see any errors in the output.

$ cd mjpg-streamer/
$ cd mjpg-streamer-experimental/
$ sudo apt-get install cmake
$ sudo apt-get install python-imaging
$ sudo apt-get install libjpeg-dev
$ make CMAKE_BUILD_TYPE=Debug
$ sudo make install
STEP 7: SET AN ENVIRONMENT VARIABLE
This is so the program can know where to find the libraries that it needs. You will always need to run this first or you can learn how to make the setting permanent. That's beyond the scope of this article. Don't forget the period ('.') at the end of the command.

$ export LD_LIBRARY_PATH=.
STEP 8: RUN MJPG-STREAMER
$ ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
Note that this worked fine on the Pi Zero. But on the Pi 3 the image was reversed and I had to add the -hf flag:

$ ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -hf"
STEP 9: BROWSE TO THE PI FROM ANOTHER COMPUTER
On another machine (like a Mac using Chrome) browse to (replacing HOSTNAME with your Pi hostname):

http://HOSTNAME.local:8080
NOTE: If you get a page error, wait a minute and see if it refreshes.

Click on the Stream tab on the left to see the image.

Or:

http://HOSTNAME.local:8080/?action=stream
If the image is backwards, see my note above about the -hf flag.

You can also try:

$ ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 1280 -y 720 -fps 15 -ex night"
Or if it's backwards, add the -hf flag:

$ ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 1280 -y 720 -fps 15 -ex night -hf"
To stop it from running: place your focus in the terminal window and press Ctr-C.

If you get error 'mmal error ENOSPC' then camera may be in use by another app.
https://www.raspberrypi.org/forums/viewtopic.php?t=198665

