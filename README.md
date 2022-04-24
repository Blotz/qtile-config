# Qtile debugger
A dev enviroment for testing a qtile config.

vscode has been configured to automatically run `src/config.py`

### Requirements
See hacking qtile for libary requirements
http://docs.qtile.org/en/latest/manual/hacking.html

### Setup
1. run `dev.sh`
2. run `Xephyr +extension RANDR -screen 1920x1040 :1 -ac &`
2. go to vscode debugging and click run