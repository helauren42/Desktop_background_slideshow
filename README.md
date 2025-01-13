# gnome_wallpaper_slider

This program is developed as a wallpaper slideshow creator for gnome, but too make it work on other desktop environments, replacing the gnome commands like "gsettings set org.gnome.desktop.background picture-uri" in the change_wallpaper.sh file with its equivalent in your environment will likely make things work.

the command "gsettings set org.gnome.desktop.background picture-uri" accepts all format types even when I tested custom types it worked, but for more convenient usage of this program I have limited the available image types to "", so that your .txt .json and other file types can be ignored
