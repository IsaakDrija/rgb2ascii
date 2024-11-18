import convert
from PIL import Image, ImageTk #For displaying the image in the Tk Gui
import platform
import os

#The module loaded and, thus, the user can see this
print("Module: UI successfully started.\n")

try:
    import gi

    # Defines the necessary GTK version on the system
    gi.require_version('Gtk', '3.0')

    from gi.repository import Gtk
    # Please refer to https://python-gtk-3-tutorial.readthedocs.io/en/latest/
    # for the PyGTK documentation

    class main_window:
        def __init__(self):
            """Initializes the main window. Usually only called one per execution."""
            template = "./ui/ui_template.glade"

            # Start the builder using the glade .xml file
            self.builder = Gtk.Builder()
            # Adds the main window from the template with all its children
            self.builder.add_from_file(template)

            # Grabs all the objects from the ui file.
            # Only needed when addressing their events or from outside the class itself
            self.window = self.builder.get_object("main_window")
            self.button_check_invert = self.builder.get_object("button_check_invert")

            # Main window and its elements' events
            self.window.connect('destroy', Gtk.main_quit)
            self.button_check_invert.connect('toggled', self.setting_invert)


        def setting_invert(self, widget):
            bInvert = widget.get_active()
            return bInvert

# Fallback version if the Gtk module files to load, meant to Windows users.
except:
    import tkinter as tk
    from tkinter import filedialog
    print("Gtk was not found, falling back to tk")

    class main_window:
        def __init__(self, root):
            root.title("RGB 2 ASCII")
            root.geometry("1280x720")  # Sets a fixed window size

            # Creates the file path text above
            self.label = tk.Label(root, text="No image currently loaded")
            self.label.pack(pady=10)  # Add padding

            # Creates the loading button
            self.load_button = tk.Button(root, text="Select file", command=self.load_button_clicked)
            self.load_button.pack(pady=20)

            self.image_box = tk.Label(root, text="Image")
            self.image_box.pack(pady=80)

            # Needed to keep the reference in memory once the file dialog is closed,
            # refer to the load_button function
            self.displayed_image = None


        def load_button_clicked(self):
            file_name = filedialog.askopenfilename() # Displays the OS file explorer this app is running on
            file_name = os.path.normpath(file_name)
            self.label.config(text=f"Loaded file: {file_name}") # The upper

            if file_name:
                try:
                    image = Image.open(file_name) # Gets the image from the defined path. Might need exhaustive tests.
                    image = convert.resize(image, new_width=300) # This function comes from the convert module
                    self.displayed_image = ImageTk.PhotoImage(image) # Makes this displayable by Tk
                    self.image_box.config(image=self.displayed_image)
                except Exception as e:
                    self.image_box.config(text=f"The image is not valid or could not be opened: {e}.")
