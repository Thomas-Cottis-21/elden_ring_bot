import time
import keyboard

def set_record():
    keyboard.wait('n')
    time.sleep(2.5)
    print('go')
    record = keyboard.record(until='m')
    print('m was registered...')
    keyboard.wait('o')
    print("looping...")
    i = 1
    while i < 1000:
        keyboard.play(record)
        i += 1

set_record()