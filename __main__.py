#Just import your libraries or whatever the heck you desire here
import convert
import ui

from gi.repository import Gtk


if __name__ == "__main__":
    print("Hola mundo!") #Just testing haha

    win = ui.main_window()
    print(ui.main_window.setting_invert(win, win.button_check_invert))
    # This will be the backbone of the application. If it closes, the program terminates
    Gtk.main()
