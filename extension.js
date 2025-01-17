import ST from 'gi://ST';
import { Extension } from 'resource:///org/gnome/shell/extensions/extension.js';
import * as PanelMenu from 'resource:///org/gnome/shell/ui/panelMenu.js';
import * as Main from 'resource:///org/gnome/shell/ui/main.js';
import { Gtk } from 'gi://Gtk';

const { Gio } = imports.gi;
const run_script = ['python3', 'manager.py'];

export default class ExampleExtension extends Extension {

    constructor() {
        super();
        this._settingsWindow = null;
    }

    runCommand(args) {
        let cmd = run_script.concat(args);
        let result = Gio.Subprocess.new(
            cmd,
            Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE
        );
        result.communicate_utf8_async(null, null, (result) => {
            let [success, stdout, stderr] = result;
            if (success) {
                log(stdout);
            } else {
                logError(stderr);
            }
        });
    }

    createSettingsWindow() {
        if (this._settingsWindow) {
            return; // If the settings window already exists, do nothing
        }

        this._settingsWindow = new Gtk.Window({
            type: Gtk.WindowType.TOPLEVEL
        });
        this._settingsWindow.set_title('Background Slideshow Settings');
        this._settingsWindow.set_default_size(300, 200);

        // Create a Box to hold the buttons
        let box = new Gtk.Box({
            orientation: Gtk.Orientation.VERTICAL,
            spacing: 10
        });
        this._settingsWindow.add(box);

        // Create a label and a text entry field for the path
        let label = new ST.Label({ label: 'Enter your path:' });
        box.add(label);
        
        // Create the path input field (St.Entry)
        let pathEntry = new ST.Entry({
            hint_text: 'Enter the path here',
            text: ''  // Default empty text
        });
        box.add(pathEntry);

        // Create the button to start the command
        let pathButton = new ST.Button({ label: 'Run with Path' });
        pathButton.connect('clicked', () => {
            let path = pathEntry.get_text();  // Get the entered text from the input field
            if (path) {
                this.runCommand([path]);
            } else {
                logError('No path provided');
            }
        });
        box.add(pathButton);

        // Create the Stop button
        let stopButton = new ST.Button({ label: 'Stop' });
        stopButton.connect('clicked', () => {
            this.runCommand(["-stop"]);
        });
        box.add(stopButton);

        // Show the window
        this._settingsWindow.show_all();
    }

    enable() {
        this.createSettingsWindow();
        this.runCommand(["-start"]);
    }

    disable() {
        this.runCommand(["-stop"]);
    }
}
