import gi

# Defines the necessary GTK version on the system
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# Please refer to https://python-gtk-3-tutorial.readthedocs.io/en/latest/
# for the PyGTK documentation


class main_window(Gtk.Window):
    def __init__(self):
        """Initializes the main window. Usually only called one per execution."""
        super().__init__(title = "RGB 2 ASCII")

        # The bigger box, parent of the other widgets
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.main_box)

        # Another box, so as to arrange thing either vertically (append to main)
        # or horizontally (append to this one)
        self.secondary_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        # TODO: Make this useable!
        self.load_button = Gtk.FileChooserButton()
        self.load_button.connect('file-set', self.image_loaded)

        #The left side panel with all of its elements
        self.left_panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # The central image to load
        self.main_image = Gtk.Image()

        # The right side panel with all of its contents
        self.right_panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)


        # Finally, adding the elements to the window
        self.main_box.pack_start(self.load_button, True, True, 0)
        self.main_box.pack_end(self.secondary_box, True, True, 0)
        self.secondary_box.pack_start(self.left_panel, True, True, 0)
        self.secondary_box.pack_start(self.main_image, True, True, 0)
        self.secondary_box.pack_end(self.right_panel, True, True, 0)


    def image_loaded(self, widget):
        """Loads the image after the user has selected one"""
        # TODO: Have this make something, probably customizing the chooser instance
        print("Module: UI, Image loaded successfully")
        self.main_image.set_from_file("./apurao.jpg")

#The module loaded and, thus, you see the window
print("Module: UI successfully started.\n")

win = main_window() # Creates an instance of the window class
win.show_all() # Shows the window's instance
win.connect('destroy', Gtk.main_quit) # If the window closes, quit
Gtk.main() # The main Gtk thread


