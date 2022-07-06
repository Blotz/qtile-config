#!/usr/bin/env bash 

lxsession &
xautolock -time 10 -locker slock &
dunst &
picom &
volumeicon &
# conky -c $HOME/.config/conky/doomone.conkyrc &
flameshot &

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
xwallpaper --stretch ~/.xwallpaper &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &
