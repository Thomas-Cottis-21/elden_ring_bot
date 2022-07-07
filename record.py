import time
import keyboard
#importing libraries. "time is from python itself and doesn't need to be installed"
#keyboard will need to be installed locally, you can download here -> https://pypi.org/project/keyboard/

#Note that you don't need to be "clicked into" the command line in order to start recording (press 'n')

#program won't proceed unless you press 'n'
keyboard.wait('n')
#Once 'n' is pressed, will give you 2.5 seconds until "go-time"
time.sleep(2.5)
print('go')
#Once go is printed, your key - strokes are being recorded and saved into the variable record until 'm' is pressed
record = keyboard.record(until='m')
print('m was registered...')
#Once 'm' is pressed and "m was registered" are printed to the terminal, the program will wait for you to press 'o'
keyboard.wait('o')
print("looping...")
i = 1
#Once 0 is pressed, your keyboard recording will be iterated 1000 times (or however many times you choose)
while i < 1000:
    keyboard.play(record)
    i += 1
