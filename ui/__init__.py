import gi

# Defines the necessary GTK version on the system
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class main_window(Gtk.Window):
    def __init__(self):
        """Initializes the main window. Usually only called one per execution."""
        super().__init__(title = "RGB 2 ASCII")

        self.main_box = Gtk.Box(spacing=6)
        self.add(self.main_box)

        self.menu_bar = Gtk.MenuBar()
        self.main_box.pack_start(self.menu_bar, True, True, 0)

        self.button1 = Gtk.Button(label="Botón 1")
        self.main_box.pack_start(self.button1, True, True, 0)
        #self.menu = Gtk.MenuBar()
        #self.add(self.menu)
        #self.load_button = Gtk.FileChooserButton()
        # self.load_button.connect('clicked', self.load_image_clicked)
        #self.add(self.load_button)

    def load_image_clicked(self, widget):
        """Opens the OS file explorer"""
        print("Apurao")

#The module loaded and, thus, you see the window
print("Module: UI successfully started.\n")

win = main_window() # Creates an instance of the window class
win.show_all() # Shows the window's instance
win.connect('destroy', Gtk.main_quit) # If the window closes, quit
Gtk.main() # The main Gtk thread


