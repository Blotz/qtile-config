import os
from libqtile import bar, widget, qtile
from libqtile.command import lazy
from libqtile.config import Screen

from custom_widgets.vpn_checker import ConnectionStatus

from settings import COLORS
from settings import TERM as myTerm
#from config import qtile

# Background wallpaper
# wallpaper_mode = "stretch"

def init_widgets_list():
    '''
    Function that returns the desired widgets in form of list
    '''
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=COLORS[2],
            background=COLORS[0]
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm)}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=COLORS[2],
            background=COLORS[0]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=COLORS[2],
            inactive=COLORS[7],
            rounded=False,
            highlight_color=COLORS[1],
            highlight_method="line",
            this_current_screen_border=COLORS[6],
            this_screen_border=COLORS[4],
            other_current_screen_border=COLORS[6],
            other_screen_border=COLORS[4],
            foreground=COLORS[2],
            background=COLORS[0]
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=COLORS[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser(
                "~/.config/qtile/icons")],
            foreground=COLORS[2],
            background=COLORS[0],
            padding=0,
            scale=0.7
        ),
        widget.CurrentLayout(
            foreground=COLORS[2],
            background=COLORS[0],
            padding=5
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=COLORS[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.WindowName(
            foreground=COLORS[6],
            background=COLORS[0],
            padding=0
        ),
        widget.Systray(
            background=COLORS[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=COLORS[0],
            background=COLORS[0]
        ),

        # Right hand side systray
        # CPU
        widget.TextBox(
            text='',
            background=COLORS[0],
            foreground=COLORS[6],
            padding=0,
            fontsize=37
        ),
        widget.CPU(
            foreground=COLORS[1],
            background=COLORS[3],
            #fmt='CPU: {}GHz {}%',
            mouse_callbacks={
                'Button1': lambda: lazy.spawncmd("htop")
            },
            padding=5
        ),
        # Thermals
        widget.ThermalSensor(
            foreground=COLORS[1],
            background=COLORS[3],
            threshold=90,
            fmt='Temp: {}',
            padding=5
        ),

        ### NETWORKING
        # Networking
        widget.Net(
            interface="wlan0",
            format='Net: {down} ↓↑ {up}',
            foreground=COLORS[1],
            background=COLORS[4],
            padding=5
        ),
        # Wifi
        widget.Wlan(
            interface='wlan0',
            format='{essid} {percent:2.0%}',
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('connman_dmenu')},
            padding=5,
            foreground=COLORS[1],
            background=COLORS[4],
        ),

        # RAM
        widget.Memory(
            foreground=COLORS[1],
            background=COLORS[5],
            fmt='MEM: {}',
            padding=5
        ),

        # Battery
        widget.Battery(
            energy_now_file="charge_now",
            energy_full_file="charge_full",
            power_now_file="current_now",
            update_delay=6,
            foreground=COLORS[1],
            background=COLORS[6],
            charge_char=u'↑',
            discharge_char=u'↓',
        ),

        # Volume
        widget.Volume(
            foreground=COLORS[1],
            background=COLORS[7],
            fmt='Vol: {}',
            padding=5
        ),

        # VPN
        ConnectionStatus(
            foreground=COLORS[1],
            background=COLORS[8],
            name="torronto",
            fmt='vpn: {}',
            padding=5
        ),

        # Keyboard
        widget.KeyboardLayout(
            foreground=COLORS[1],
            background=COLORS[9],
            configured_keyboards=["gb","us"],
            fmt='Keyboard: {}',
            padding=5
        ),


        # Date
        widget.Clock(
            foreground=COLORS[1],
            background=COLORS[3],
            format="%A, %B %d - %H:%M "
        ),
    ]
    return widgets_list

def init_widgets_screen():
    '''
    Function that returns the widgets in a list.
    It can be modified so it is useful if you  have a multimonitor system
    '''
    widgets_screen = init_widgets_list()
    return widgets_screen

def init_widgets_screen2():
    '''
    Function that returns the widgets in a list.
    It can be modified so it is useful if you  have a multimonitor system
    '''
    widgets_screen2 = init_widgets_screen()
    # Remove Systray from second screens
    del widgets_screen2[9]

    return widgets_screen2

def init_screen():
    '''
    Init the widgets in the screen
    '''
    return [Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(
                widgets=init_widgets_screen2(), opacity=1.0, size=20))
            ]
