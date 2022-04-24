#######################################
### QTILE CONFIG OF FERDINAND THEIL ###
#
# 88""Yb 88      dP"Yb  888888 8888P 
# 88__dP 88     dP   Yb   88     dP  
# 88""Yb 88  .o Yb   dP   88    dP   
# 88oodP 88ood8  YbodP    88   d8888 
# 
# https://github.com/blotz

####### IMPORTS ######
import os
import subprocess
import re
import socket
from typing import List  # noqa: F401

from libqtile import hook, layout
from libqtile.config import Group, Match
from libqtile.command import lazy
from libqtile.dgroups import simple_key_binder
from libqtile.log_utils import logger

# Local Files
from settings import COLORS
# from keys.keybindings import Mouse,Keybindings
from keys import mouse
from keys import default
from keys import hardwarekeys
from keys import apps

from widgets import MyWidgets
from layouts import Layouts
from groups import CreateGroups

logger.info("Code is running")
###### MAIN ######
if __name__ in ["config", "__main__"]:
    logger.info("Initalising objects")
    # Initializes objects

    # Initializes keybindings
    # Mouse
    obj_widgets       = MyWidgets()
    obj_layouts       = Layouts()
    obj_groups        = CreateGroups()

    # Initializes qtile variables
    keys              = default.init_keybindings()
    keys             += hardwarekeys.init_keybindings()
    keys             += apps.init_keybindings()
    mouse             = mouse.init_keybindings()

    layouts           = obj_layouts.init_layouts()
    floating_layout   = obj_layouts.init_floating_layout()

    groups            = obj_groups.init_groups()

    # Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
    # MOD4 + index Number : Switch to Group[index]
    # MOD4 + shift + index Number : Send active window to another Group
    dgroups_key_binder = simple_key_binder("mod4")

    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

    dgroups_app_rules = []  # type: List
    follow_mouse_focus = True
    bring_front_click = False
    cursor_warp = False



    auto_fullscreen = True
    focus_on_window_activation = "smart"
    reconfigure_screens = True

    # If things like steam games want to auto-minimize themselves when losing
    # focus, should we respect this or not?
    auto_minimize = True
    ### DISPLAYS WIDGETS IN THE SCREEN ####
    ##### DEFAULT WIDGET SETTINGS #####
    widget_defaults = dict(
        font="Ubuntu Bold",
        fontsize=10,
        padding=2,
        background=COLORS[2]
    )
    extension_defaults = widget_defaults.copy()

    screens           = obj_widgets.init_screen()
    main_widgets_list = obj_widgets.init_widgets_list()
    widgets_screen1   = obj_widgets.init_widgets_screen()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
