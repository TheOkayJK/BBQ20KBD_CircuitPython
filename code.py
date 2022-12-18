import time
import board
import digitalio
import usb_hid
import keypad
import busio
import touchio
import analogio
import asyncio
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from bbq20kbd import BBQ20kbd
from bbq20kbd import BasicMap

kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)


'''
i2c = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(i2c, 0x33)
'''

# I think I need help figuring out the touch sensor.
# This is a little above my level of knowledge
# tp = Mouse(usb_hid.devices)

bbq = BBQ20kbd(True)

'''
mods = ("mod1", "mod2", "Tog3", "Tog4", "Tog5", "Tog6")


def getMods(mod):
    if mod == "Tog1":
        return 1
    elif mod == "Tog2":
        return 0
    elif mod == "Tog3":
        return 0
    elif mod == "Tog4":
        return 0
    elif mod == "Tog5":
        return 0
    elif mod == "Tog6":
        return 0
'''

async def keywatcher():
    bbq.setBacklight(True)
    keys = bbq.keyLayout()
    oset = 0
    while True:
        key_event = keys.events.get()
        if key_event:
            key = BasicMap(oset, key_event.key_number, 1)
            sequence = key.get_key()
            if key_event.pressed and sequence != "NULL":
                print(sequence)
                try:
                    kbd.press(sequence)
                except:
                    combo = tuple(sequence[0:])
                    kbd.press(*combo)
            if key_event.released and sequence != "NULL":
                # only if it wasn't keycode which was already released automatically
                try:
                    kbd.release(sequence)
                except:
                    try:
                        combo = tuple(sequence[0:])
                        kbd.release(*combo)
                    except:
                        continue
                    continue
        await asyncio.sleep(0)

async def main():
    keywatch = asyncio.create_task(keywatcher())
    await asyncio.gather(keywatch)


asyncio.run(main())
