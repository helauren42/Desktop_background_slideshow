# Desktop background slideshow"

This program is developed as a desktop background slideshow for gnome.
link to github repo: https://github.com/helauren42/gnome_wallpaper_slider

## Introduction / background story

I had installed a lovely wallpaper slideshow gnome extension on my fedora 41, it was working well except that my laptop's key input would bug everytime the image was updated, as I wanted a differnt image every couple of seconds, it was a real issue. It was big disappointment for me, not to be able to flex my slideshow desktop background to my friends and family. I was desperate for it so I told myself, guess I'm going to have to do it myself! So I built it, and I'm very happy I did because now I don't just have a slideshow desktop background, I have a slideshow desktop background that I BUILT! And that allows me to flex extra hard on my friends!!! :DDD
I know how cool it is to have a background slideshow, even when it's not your own program, it is a very cool flex! So I'm working on an official gnome release so that more people can flex on their friends too :DDDDD <3.

I assume the command "gsettings set org.gnome.desktop.background picture-uri" accepts all format types, even when I tested custom types it worked, but for more convenient usage of this program I have limited the available image types to ("jpeg", "jpg", "png", "gif", "bmp", "tiff", "tif", "webp", "ico", "heif", "heic", "raw"), so that your .txt .json and other file types in your selected image repository can be ignored.

PS: my wallpaper doesn't cause the typing bug I was experiencing with the extension I installed but it does create a noticeable short term spike in cpu usage the moment the wallpaper background is changed. But the experience is mostly smooth, I do notice that my machine is not running as smoothly if I set the time to 1 second so that the wallpaper background is modified every second.

## Usage

### For an overview of the usage of the program here is what the help from "python3 manager.py -h" displays:

usage: manager.py [-h] [-s SET_TIME] [-start] [-stop] [-refresh] [path]

positional arguments:</br>
  Directory path containing images for the slideshow

options:</br>
  -h, --help</br>
  show this help message and exit</br></br>
  -s, --set-time</br>
  set the time between images in seconds, defaults to 30 seconds</br></br>
  -sm, --set-time-minutes</br>
  set the time between images in minutes</br></br>
  -start, --start</br>
  start the slideshow, requires path to be set</br></br>
  -stop, --stop</br>
  stop the slideshow, will stop all instances of the application if multiple are running</br></br>
  -refresh, --refresh</br>
  updates the images for the slideshow when the images directory has been modified</br>

### Usage explanation

Start by defining path argument and optionally set the time.

EX: python3 manager.py -s 10 ~/Pictures/wallpapers

This declares that we want to fetch our background images from "~/Pictures/wallpapers" and that the image will be changed every 10 seconds
This information is stored in a ".data.json" file, so it should be stored between your sessions.

Then you can safely run python3 manager.py -start to launch the slideshow and -stop to interrupt it, which effectively kills the running process.

If you modify the images' directory, while the application is running, the behaviour of this application is undefined.
Although I would expect that if you remove image files, you increase your risk of having a blank screen and if you add images those will not be seen by running application.

To make the application up to date with the images in that directory, you can use the --refresh option or manually stop and restart the application.

You also need to call --refresh when switching from light to dark mode in your gnome appearance settings as there is a different command being executed by the wallpaper slider for both, and your current mode is only evaluated at the application's launch time

The slider is not fetching your current mode (light/dark) and your images continuously for resource optimization purposes.
