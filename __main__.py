import convert
import ui

try:
    from gi.repository import Gtk
except:
    import tkinter as tk

if __name__ == "__main__":
    print("Hola mundo!") #Just testing haha


    # This will be the backbone of the application. If it closes, the program terminates
    try:
        win = ui.main_window()
        Gtk.main()
    except:
        window = tk.Tk()
        app = ui.main_window(window)
        window.mainloop()
