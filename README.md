# Gnome background slideshow

This program is developed as a desktop background slideshow for gnome.
link to github repo: https://github.com/helauren42/gnome_wallpaper_slider

The install.sh integrates the bg-slideshow application into the appman application I built, it is a linux session manager allowing me too easily manage and launch linux apps at launch time.
https://github.com/helauren42/appman

I did not integrate it to the official gnome Extensions application, I had built this in python, it was working and then I didn't feel like rebuilding the same thing in javascript while also runnning a lot less subprocesses. I did not know Gnome was this strict in their rules on how to build extensions, I assume that if I built it following the official Gnome extensions' rules, I probabaly would have developed the same bugs I found on the official background slideshow application.
So yeah since then I also built an application to "replace" the Gnome Extensions app, but this time it gives users the freedom to develop their application however they want the constraints to integrate an application to appman are minimal and it is not limited to gnome customizations

# Installation

- Install appman https://github.com/helauren42/appman.
- Clone this bg-slideshow repository "git clone https://github.com/helauren42/bg-slideshow/"
- Run the install.sh file inside the repo.
The executable will be located in ~/.local/appman/run/ and the application files in ~/.local/appman/run/bg-slideshow/.
To remove the application you can run the uninstall.sh from ~/.local/appman/run/bg-slideshow/.
It is safe to delete the cloned repo after the installation is done.

### Dependencies

You will need python3 and if you're python3 version is < 3.5 then you will need to manually install the typing module via pip, all other modules used are in the standard library.

# Usage

### For an overview of the usage of the program here is what the help from "bg-slideshow -h" displays:

usage: bg-slideshow [-h] [-s SET_TIME] [-activate] [-deactivate] [-refresh] [path]

positional arguments:</br>
  Directory path containing images for the slideshow

options:</br>
  -h, --help</br>
  show this help message and exit</br></br>
  -s, --set-time</br>
  set the time between images in seconds, defaults to 30 seconds</br></br>
  -sm, --set-time-minutes</br>
  set the time between images in minutes</br></br>
  -activate, --activate</br>
  activate the slideshow, requires path to be set</br></br>
  -deactivate, --deactivate</br>
  deactivate the slideshow, will deactivate all instances of the application if multiple are running</br></br>
  -refresh, --refresh</br>
  updates the images for the slideshow when the images directory has been modified</br>
  --uninstall</br>
  uninstals the background slideshow application and all the application's components</br>

### Usage explanation

activate by defining path argument and optionally set the time.

EX: bg-slideshow -s 10 ~/Pictures/wallpapers

This declares that we want to fetch our background images from "~/Pictures/wallpapers" and that the image will be changed every 10 seconds
This information is stored in a "./bg-slideshow/data.json" file, so it should be stored between your sessions.

Then you can safely run bg-slideshow --activate to launch the slideshow and --deactivate to interrupt it, which effectively kills the running process.
Or from appman run "appman$> activate bg-slideshow" or "appman$> deactivate bg-slideshow"

If you modify the images' directory, while the application is running, the behaviour of this application is undefined.
It's untested but I would expect that if you remove image files, you increase your risk of having a blank screen and if you add images those will not be seen by running application.

To make the application up to date with the images in that directory, you can use the --refresh option or manually deactivate and reactivate the application.

You also need to call --refresh when switching from light to dark mode in your gnome appearance settings.

# background story

I had installed a lovely wallpaper slideshow gnome extension on my fedora 41, it was working well except that my laptop's key input would bug everytime the image was updated, as I wanted a differnt image every couple of seconds, it was a real issue. It was big disappointment for me, not to be able to flex my slideshow desktop background to my friends and family. I was desperate for it so I told myself, guess I'm going to have to do it myself! So I built it, and I'm very happy I did because now I don't just have a slideshow desktop background, I have a slideshow desktop background that I BUILT! And that allows me to flex extra hard on my friends!!! :DDD
I know how cool it is to have a background slideshow, even when it's not your own program, it is a very cool flex! So I'm working on an official gnome release so that more people can flex on their friends too :DDDDD <3.

I assume the command "gsettings set org.gnome.desktop.background picture-uri" accepts all format types, even when I tested custom types it worked, but for more convenient usage of this program I have limited the available image types to ("jpeg", "jpg", "png", "gif", "bmp", "tiff", "tif", "webp", "ico", "heif", "heic", "raw"), so that your .txt .json and other file types in your selected image repository can be ignored.

PS: my wallpaper doesn't cause the typing bug I was experiencing with the extension I installed but it does create a noticeable short term spike in cpu usage the moment the wallpaper background is changed. But the experience is mostly smooth, I do notice that my machine is not running very smoothly if I set the time to 1 second so that the wallpaper background is modified every second.
