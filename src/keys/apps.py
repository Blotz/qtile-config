from libqtile.config import Key
from libqtile.command import lazy

from settings import ALT as alt
from settings import BROWSER as myBrowser
from settings import MUSIC as myMusic
from settings import CHAT as myChat


KEYS = [ 
    Key([alt], "b",
        lazy.spawn(myBrowser),
        desc='Firefox'
    ),
    Key([alt], "m",
        lazy.spawn(myMusic),
        desc='Spotify'
        ),
    Key([alt], "c",
        lazy.spawn(myChat),
        desc='Discord'
        ),
]
