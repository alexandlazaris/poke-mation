# poke-mation
Combining automation tools with playing pokemon

Below is a list of tools I've attempted automating playthroughs for Pokemon Firered so far.

### Maestro

Maestro is a test automation tool that provides easy interaction with mobile devices. Interaction is driven by commands written in YAML. Prelaunch an android GBA emulator with the game running. 

#### Requires
- android studio, adb

Review: https://alexander.ghost.io/a-wild-automation-challenge-appeared/

### SkyEmu

Skyemu is a GBA emulator that allows a local server to receive input commands sent by code. Using this method, we can send a sequence of commands to perform game actions. These commands are written in python.

#### Requires
- https://github.com/skylersaleh/SkyEmu
- python for running local server & sending commands to emulator
- required modifying ssl library that Python uses. Initial error: `3.9/lib/python/site-packages/urllib3/__init__.py:34: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'`
- requires `requests` library: `python3 -m pip install requests`

#### Start server 

https://github.com/skylersaleh/SkyEmu/blob/dev/docs/HTTP_CONTROL_SERVER.md

`../../../../Applications/SkyEmu.app/Contents/MacOS/SkyEmu http_server 8080 <path-to-gba-rom>`

Once server has started, run SkyEmu app and launch your game. At this point, the python script is ready to be run. 

