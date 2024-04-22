import requests
import time

# "/Applications/SkyEmu.app/Contents/MacOS/SkyEmu" http_server 8080 "/Users/Alex/Downloads/Pokemon - FireRed Version (USA, Europe) (Rev 1).gba"
delayBetweenStairs = 1.5
delayToExitBuilding = 2

buttons = ["Up", "Down", "Left", "Right", "A", "B", "X", "Y", "L", "R", "ZL", "ZR", "Minus", "Plus", "Home", "Capture"]

# TODO: have a dedicated navigation input method
def pressButton(buttonKey):
    url = f"http://localhost:8080/input?{buttonKey}=1"
    response = requests.get(url)
    print(response.url + " - " + response.text)
    time.sleep(0.2)
    releaseAll(buttonKey)

def releaseAll(buttonKey):
    url = f"http://localhost:8080/input?{buttonKey}=0"
    response = requests.get(url)
    print(response.url + " - " + response.text)
    time.sleep(0.2)

def navigate_roomStart_to_downstairs():
    print(navigate_roomStart_to_downstairs.__name__)
    pressButton("Right")
    pressButton("Right")
    pressButton("Right")
    pressButton("Right")
    pressButton("Right")
    pressButton("Up")
    pressButton("Up")
    pressButton("Up")
    pressButton("Up")
    pressButton("Left")
    pressButton("Left")
    time.sleep(delayBetweenStairs)

def navigate_exit_home():
    print(navigate_exit_home.__name__)
    pressButton("Down")
    pressButton("Down")
    pressButton("Down")
    pressButton("Down")
    pressButton("Down")
    pressButton("Down")
    pressButton("Left")
    pressButton("Left")
    pressButton("Left")
    pressButton("Left")
    pressButton("Left")
    pressButton("Left")
    pressButton("Down")

def navigate_from_home_to_first_grass():
    print(navigate_from_home_to_first_grass.__name__)
    time.sleep(delayToExitBuilding)
    pressButton("Right")
    pressButton("Right")
    pressButton("Right")
    pressButton("Right")
    pressButton("Right")
    pressButton("Up")
    pressButton("Up")
    pressButton("Up")
    pressButton("Up")
    pressButton("Up")
    pressButton("Up")
    pressButton("Right")
    pressButton("Up")
    pressButton("Up")

def dialogBox(button):
    time.sleep(3)
    pressButton(button)

# add 0.5s delay after each dialog box to finish reading
def dialogue_first_professor():
    dialogBox("A")
    # wait for professor to finish walking to grass
    time.sleep(4)
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")

def firstLabDialogue():
    # walk back to lab and join Gary
    time.sleep(7)
    #  need to add checkpoints to the below button presses
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    # now A
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")

def selectStarterSequence():
    pressButton("Down")
    pressButton("Down")
    pressButton("Right")
    pressButton("Right")
    pressButton("Up")
    pressButton("Up")
    # talk to ball
    dialogBox("A") 
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("A")
    dialogBox("K")
    # gary chooses ball
    dialogBox("A") 
    dialogBox("A") 
    # walk to lab mid
    pressButton("Left")
    pressButton("Down")
    pressButton("Down")
    pressButton("Down")
    dialogBox("A") 
    dialogBox("A") 
    # time for first battle to begin
    time.sleep(7)
    

if __name__ == "__main__":
    navigate_roomStart_to_downstairs()
    navigate_exit_home()
    navigate_from_home_to_first_grass()
    dialogue_first_professor()
    firstLabDialogue()
    selectStarterSequence()

# response = requests.get(url)
# print(response.text)
