from libqtile.config import Key
from libqtile.command import lazy

from settings import MOD as mod


KEYS = [ 
    # Hardware settings
    # Audio
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q set Master 5%+")
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -q set Master 5%-")
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("amixer -q set Master toggle")
        ),
    # Also allow changing volume the old fashioned way.
    Key([mod], "equal", lazy.spawn("amixer -q set Master 2dB+")),
    Key([mod], "minus", lazy.spawn("amixer -q set Master 2dB-")),

    # Brightness
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +2%")
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 2%-")
        ),

    # Music
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous")
        ),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause")
        ),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next")
        ),
    Key([], "Print",
        lazy.spawn("flameshot gui")
        )
]
