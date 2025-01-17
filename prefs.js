import Adw from 'gi://Adw';
import Gdk from 'gi://Gdk';
import Gio from 'gi://Gio';
import GLib from 'gi://GLib';
import GObject from 'gi://GObject';
import Gtk from 'gi://Gtk';

import * as Config from 'resource:///org/gnome/Shell/Extensions/js/misc/config.js';

import {ExtensionPreferences, gettext as _, ngettext} from 'resource:///org/gnome/Shell/Extensions/js/extensions/prefs.js';

var SlideShowPage = GObject.registerClass(
class azWallpaperSlideShowPage extends Adw.PreferencesPage {
    _init(settings) {
        super._init({
            title: _('Slideshow'),
            icon_name: 'emblem-photos-symbolic',
            name: 'HomePage',
        });

    }
});
