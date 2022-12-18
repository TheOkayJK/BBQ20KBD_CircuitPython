import keypad
import board
import digitalio
import microcontroller

# The following imports are only needed for the keymap
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Library made with love by JK at OUR.HAUS (https://our.haus)
# The bbq20kbd was made by the geniuses at Solder Party (https://solder.party) in Sweden
# Availble to purchase at:
# https://www.tindie.com/products/arturo182/bb-q20-keyboard-with-trackpad-usbi2cpmod/
# https://www.lectronz.com/products/bb-q20-keyboard-with-trackpad-usb-i2c-pmod
# Documentation is still WIP but you can find an example in the examples folder
# This is an unofficial library (I am not Solder Party)
# Feel free to create issues, forks, PRs, etc. as needed!
# Lastly, have fun with your project, whatever it may be!
class BBQ20kbd:
    def __init__(self, touch):
        self.touch = touch

    # Set keyboard backlight based on a true or false value
    def setBacklight(self, bkl):
        # bkl = self.bkl
        try:
            blpin = digitalio.DigitalInOut(board.BACKLIGHT)
            blpin.direction = digitalio.Direction.OUTPUT
            if bkl is True:
                blpin.value = True
            elif bkl is False:
                blpin.value = False
        except:
            print("Something went wrong, that's odd")

    # Return the pin for the backlight
    def getBacklight(self):
        return board.BACKLIGHT

    # Return the pins for the keyboard's rows
    def getRows(self):
        return (
            board.ROW1,
            board.ROW2,
            board.ROW3,
            board.ROW4,
            board.ROW5,
            board.ROW6,
            board.ROW7,
        )

    # Return the pins for the keyboard's columns
    def getCols(self):
        return (
            board.COL1,
            board.COL2,
            board.BTN1,
            board.COL6,
            board.COL5,
            board.COL4,
            board.COL3,
        )

    # Return a keypad matrix
    def keyLayout(self):
        keys = keypad.KeyMatrix(
            row_pins=(
                board.ROW1,
                board.ROW2,
                board.ROW3,
                board.ROW4,
                board.ROW5,
                board.ROW6,
                board.ROW7,
            ),
            column_pins=(
                board.COL1,
                board.COL2,
                board.BTN1,
                board.COL6,
                board.COL5,
                board.COL4,
                board.COL3,
            ),
            columns_to_anodes=True,
        )
        return keys

    # Return all of the boards pins
    # This is intended only to be used for advanced customization/tweaking
    def getAllPins(self):
        pins = dir(board)
        return pins


# A couple basic keymaps
# Specify the desired set by passing the kset variable as the desired mapping (0, 1, 2, etc.)
# Feel free to use as-is or as a starting point for your own customized mapping
# BT4, the end call button has a bunch of duplicates,
# I have no idea why, so make sure to filter out the extras
class BasicMap(BBQ20kbd):
    # Inherit main class's variables. Not sure why yet, may remove but did it just in case I want it later
    def __init__(self, kset, key, index):
        # super().__init__(rows, cols, bkl, touch)
        self.kset = kset
        self.key = key
        self.index = index

    def get_key(self):
        kset = self.kset
        key = self.key
        index = self.index
        if kset == 0:
            keymap = [
                ("touch", Keycode.TAB),
                ("w", Keycode.W),
                ("bt4", [Keycode.GUI, Keycode.ENTER]),
                ("h", Keycode.H),
                ("l", Keycode.L),
                ("s", Keycode.S),
                ("g", Keycode.G),
                ("NULL", "NULL"),
                ("q", Keycode.Q),
                ("bt4dupe", "NULL"),
                ("u", Keycode.U),
                ("o", Keycode.O),
                ("e", Keycode.E),
                ("r", Keycode.R),
                ("bt1", [Keycode.ALT, Keycode.TAB]),
                ("mic", Keycode.LEFT_CONTROL),
                ("bt4dupe", "NULL"),
                ("j", Keycode.J),
                ("k", Keycode.K),
                ("l_shift", Keycode.LEFT_SHIFT),
                ("f", Keycode.F),
                ("NULL", "NULL"),
                ("space", Keycode.SPACE),
                ("bt4dupe", "NULL"),
                ("n", Keycode.N),
                ("m", Keycode.M),
                ("z", Keycode.Z),
                ("c", Keycode.C),
                ("bt2", Keycode.GUI),
                ("sym", Keycode.RIGHT_CONTROL),
                ("NULL", "NULL"),
                ("y", Keycode.Y),
                ("i", Keycode.I),
                ("d", Keycode.D),
                ("t", Keycode.T),
                ("bt3", [Keycode.GUI, Keycode.BACKSPACE]),
                ("l_alt", Keycode.LEFT_ALT),
                ("bt4dupe", "NULL"),
                ("b", Keycode.B),
                ("vol", Keycode.RIGHT_ALT),
                ("x", Keycode.X),
                ("v", Keycode.V),
                ("NULL", "NULL"),
                ("a", Keycode.A),
                ("bt4dupe", "NULL"),
                ("enter", Keycode.ENTER),
                ("backspace", Keycode.BACKSPACE),
                ("p", Keycode.P),
                ("r_shift", Keycode.RIGHT_SHIFT),
            ]
            return keymap[key][index]
        elif kset == 1:
            keymap = [
                ("B5", "0"),
                ("A1", "1"),
                ("A2", "2"),
                ("A3", "3"),
                ("A4", "4"),
                ("A5", "5"),
                ("B1", "6"),
                ("B2", "7"),
                ("B3", "8"),
                ("B4", "9"),
                ("B5", "10"),
                ("A1", "11"),
                ("A2", "12"),
                ("A3", "13"),
                ("bt1", "1"),
                ("A5", "15"),
                ("B1", "16"),
                ("B2", "17"),
                ("B3", "18"),
                ("B4", "19"),
                ("B5", "20"),
                ("A1", "21"),
                ("A2", "22"),
                ("A3", "23"),
                ("A4", "24"),
                ("A5", "25"),
                ("B1", "26"),
                ("B2", "27"),
                ("B3", "28"),
                ("B4", "29"),
                ("B5", "30"),
                ("A1", "31"),
                ("A2", "32"),
                ("A3", "33"),
                ("A4", "34"),
                ("A5", "35"),
                ("B1", "36"),
                ("B2", "37"),
                ("B3", "38"),
                ("B4", "39"),
                ("B5", "40"),
                ("B5", "41"),
                ("B5", "42"),
                ("B5", "43"),
                ("B5", "44"),
                ("B5", "45"),
                ("B5", "46"),
                ("B5", "47"),
                ("B5", "48"),
            ]
            return keymap[key][index]
        elif kset == 2:
            keymap = [
                ("touch", "3"),
                ("w", "7"),
                ("bt4", "5"),
                ("h", "21"),
                ("l", "24"),
                ("s", "17"),
                ("g", "20"),
                ("NULL", "NULL"),
                ("q", "6"),
                ("bt4dupe", "NULL"),
                ("u", "12"),
                ("o", "14"),
                ("e", "8"),
                ("r", "9"),
                ("bt1", "1"),
                ("mic", "37"),
                ("bt4dupe", "NULL"),
                ("j", "22"),
                ("k", "23"),
                ("l_shift", "36"),
                ("f", "19"),
                ("NULL", "NULL"),
                ("space", "38"),
                ("bt4dupe", "NULL"),
                ("n", "32"),
                ("m", "33"),
                ("z", "27"),
                ("c", "29"),
                ("bt2", "2"),
                ("sym", "39"),
                ("NULL", "NULL"),
                ("y", "11"),
                ("i", "13"),
                ("d", "18"),
                ("t", "10"),
                ("bt3", "4"),
                ("l_alt", "26"),
                ("bt4dupe", "NULL"),
                ("b", "31"),
                ("vol", "34"),
                ("x", "28"),
                ("v", "30"),
                ("NULL", "NULL"),
                ("a", "16"),
                ("bt4dupe", "NULL"),
                ("enter", "35"),
                ("backspace", "25"),
                ("p", "15"),
                ("r_shift", "40"),
            ]
            return keymap[key][index]
