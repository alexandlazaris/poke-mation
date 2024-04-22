# poke-mation
Combining automation tools with playing pokemon

Below is a list of tools I've attempted automating playthroughs for Pokemon Firered so far.

### Maestro

Maestro is a test automation tool that provides easy interaction with mobile devices. Interaction is driven by commands written in YAML. 

#### Requires
- android studio, adb

Review: https://alexander.ghost.io/a-wild-automation-challenge-appeared/

### Skyemu

Skyemu is a GBA emulator that allows a local server to receive input commands sent by code. Using this method, we can send a sequence of commands to perform game actions. These commands are written in python.

#### Requires
- https://github.com/skylersaleh/SkyEmu
- python for running local server & sending commands to emulator