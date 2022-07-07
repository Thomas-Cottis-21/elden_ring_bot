# elden_ring_bot

Used at the Mohgwyn Palace - Palace Approach Ledge Road site of grace.

This program will record your keyboard input (must be keyboard), then repeat it.

Currently set to loop 1000 times, can be easily changed in the code itself.

NOTE - In order for this to work efficiently, it is recommended to have equipped the Sacred Relic Sword +10 in order to kill enemies in one swoop. The farm would take significantly longer if it wasn't +10.

NOTE - Dual monitors not required, but recommended.

NOTE - PREFERRED SETTINGS {
  CAMERA AUTO WALL RECOVERY - OFF
  RESET CAMERA Y-AXIS - OFF
  (you basically want to lock your camera because wherever your camera is pointed, your character is moving)
}

Steps from scratch:

1. Install Python -> https://www.python.org/downloads/

2. Clone or download elden_ring_bot file

3. Install the python keyboard library from pypi in the elden_ring_bot project directory. It's already being imported in the code, it just must be downloaded locally (on your machine). See here for library documentation and install -> https://pypi.org/project/keyboard/

4. Navigate in the command line to the directory where you have saved elden_ring_bot

5. Open Elden Ring and navigate to the Palace Approach Ledge Road Site of grace. 

6. Back to the command line, run python record.py (this will run the program)

7. The program will wait for you to press 'n'. Once 'n' is pressed it will give you 2.5 seconds until 'go' is printed. Once 'go' is printed, the program is recording your keyboard inputs

8. Once you have effectively farmed once and rested (or however you want to complete your loop), press 'm'. Pressing 'm' will end the recording of your keyboard inputs. Once 'm' is pressed, 'm was registered' will print to the terimal

9. Once your recording is recorded, press 'o'. Pressing 'o' will iterate your recorded keyboard commands to your keyboard, thus re-doing your loop that you first did. 

THINGS TO BE CAUTIOUS ABOUT

Please read -> 

PROBLEM

By using the special ability that the Sacred Relic Sword has, your character will take a step forward, thus moving the entire loop up and up until your character is unable to rest at the site of grace, thus killing your ability to farm and sending your character further into the group of enemies resulting in his / her death. 

SOLUTION

When setting your keyboard recording, run up to the preferred spot to use the special ability. When running back, you must run past the site of grace and into the rocks behind it in order to "reset" your characters paces, if not, your character will keep advancing forward until he is no longer able to rest at the site of grace and eventually being killed. Basically, your loop will run perfectly if and only if your character rests at the site of grace in the same exact spot every time. In order to ensure this, your character must run into the rocks behind the site of grace, then to the site of grace itself. (Confusing, but you'll get what I mean)

PROBLEM

Even though this is an autonomous program running your character, you can still run the risk of losing millions of runes if your camera angle changes, resulting in the sad event of your character running off of the cliff to the left. 

SOLUTION

Be mindful of your mouse and refer to the preferred setting noted in this documentation
