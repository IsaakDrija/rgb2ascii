# Copyright (C) 2024  Isaak Drija Medina

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import convert
import ui

try:
    from gi.repository import Gtk
except:
    import tkinter as tk


if __name__ == "__main__":

    # This will be the backbone of the application. If it closes, the program terminates
    try:
        win = ui.main_window()
        Gtk.main()
    except:
        window = tk.Tk()
        app = ui.main_window(window)
        window.mainloop()
