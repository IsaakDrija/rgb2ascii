import gi

# Defines the necessary GTK version on the system
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# Please refer to https://python-gtk-3-tutorial.readthedocs.io/en/latest/
# for the PyGTK documentation


class main_window():
    def __init__(self):
        """Initializes the main window. Usually only called one per execution."""
        template = "./ui/ui_template.glade"

        # Start the builder using the glade .xml file
        self.builder = Gtk.Builder()
        # Adds the main window from the template with all its children
        self.builder.add_from_file(template)

        # Grabs all the objects from the ui file.
        # Only needed when addressing their events
        self.window = self.builder.get_object("main_window")

        # Main window events
        self.window.connect('destroy', Gtk.main_quit)

    def image_loaded(self, widget):
        """Loads the image after the user has selected one"""
        file_chooser = Gtk.FileChooserDialog()
        print(file_chooser.get_current_folder())


#The module loaded and, thus, you see the window
print("Module: UI successfully started.\n")

win = main_window() # Creates an instance of the window class
Gtk.main() # The main Gtk thread
