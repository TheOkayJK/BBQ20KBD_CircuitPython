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

# I think I need help figuring out the touch sensor.
# This is a little above my level of knowledge
# tp = Mouse(usb_hid.devices)
# i2c = busio.I2C(board.SCL, board.SDA)
# device = I2CDevice(i2c, 0x33)

bbq = BBQ20kbd(True)
# True is a place holder for a future tbd variable

syms = ("SYM1", "SYM2")

def isSym(symcheck):
    if symcheck == "SYM1":
        bbq.setBacklight(False)
        return 1
    elif symcheck == "SYM2":
        bbq.setBacklight(False)
        return 2
    else:
        return 0

bbq.setBacklight(True)
async def keywatcher():
    keys = bbq.keyLayout()
    oset = 0
    while True:
        key_event = keys.events.get()
        if key_event:
            key = BasicMap(oset, key_event.key_number, 1)
            sequence = key.get_key()
            if key_event.pressed and sequence != "NULL":
                print(sequence)
                if sequence in syms and isSym(sequence) != oset:
                    oset = isSym(sequence)
                elif sequence == "SYM1" and oset == 1:
                    oset = 0
                elif sequence == "SYM2" and oset == 2:
                    oset = 0
                else:
                    try:
                        kbd.press(sequence)
                    except:
                        combo = tuple(sequence[0:])
                        kbd.press(*combo)
            if key_event.released and sequence != "NULL":
                bbq.setBacklight(True)
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
