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
        self.blpin = digitalio.DigitalInOut(board.BACKLIGHT)

    # Set keyboard backlight based on a true or false value
    def setBacklight(self, bkl):
        # bkl = self.bkl
        blpin = self.blpin
        try:
            #blpin = digitalio.DigitalInOut(board.BACKLIGHT)
            blpin.direction = digitalio.Direction.OUTPUT
            if bkl is True:
                blpin.value = True
            elif bkl is False:
                blpin.value = False
        except:
            blpin.deinit()
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
                ("sym", "SYM1"),
                ("NULL", "NULL"),
                ("y", Keycode.Y),
                ("i", Keycode.I),
                ("d", Keycode.D),
                ("t", Keycode.T),
                ("bt3", [Keycode.GUI, Keycode.BACKSPACE]),
                ("l_alt", Keycode.LEFT_ALT),
                ("bt4dupe", "NULL"),
                ("b", Keycode.B),
                ("vol", "SYM2"),
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
                ("touch", Keycode.TAB),
                ("w", Keycode.ONE),
                ("bt4", [Keycode.GUI, Keycode.ENTER]),
                ("h", [Keycode.LEFT_SHIFT, Keycode.SEMICOLON]),
                ("l", [Keycode.LEFT_SHIFT, Keycode.QUOTE]),
                ("s", Keycode.FOUR),
                ("g", Keycode.FORWARD_SLASH),
                ("NULL", "NULL"),
                ("q", [Keycode.LEFT_SHIFT, Keycode.THREE]),
                ("bt4dupe", "NULL"),
                ("u", [Keycode.LEFT_SHIFT, Keycode.MINUS]),
                ("o", [Keycode.LEFT_SHIFT, Keycode.EQUALS]),
                ("e", Keycode.TWO),
                ("r", Keycode.THREE),
                ("bt1", [Keycode.ALT, Keycode.TAB]),
                ("mic", Keycode.ZERO),
                ("bt4dupe", "NULL"),
                ("j", Keycode.SEMICOLON),
                ("k", Keycode.QUOTE),
                ("l_shift", Keycode.LEFT_SHIFT),
                ("f", Keycode.SIX),
                ("NULL", "NULL"),
                ("space", Keycode.SPACE),
                ("bt4dupe", "NULL"),
                ("n", Keycode.COMMA),
                ("m", Keycode.PERIOD),
                ("z", Keycode.SEVEN),
                ("c", Keycode.NINE),
                ("bt2", Keycode.GUI),
                ("sym", "SYM1"),
                ("NULL", "NULL"),
                ("y", [Keycode.LEFT_SHIFT, Keycode.ZERO]),
                ("i", Keycode.MINUS),
                ("d", Keycode.FIVE),
                ("t", [Keycode.LEFT_SHIFT, Keycode.NINE]),
                ("bt3", [Keycode.GUI, Keycode.BACKSPACE]),
                ("l_alt", Keycode.LEFT_ALT),
                ("bt4dupe", "NULL"),
                ("b", [Keycode.LEFT_SHIFT, Keycode.ONE]),
                ("vol", "SYM2"),
                ("x", Keycode.EIGHT),
                ("v", [Keycode.LEFT_SHIFT, Keycode.FORWARD_SLASH]),
                ("NULL", "NULL"),
                ("a", [Keycode.LEFT_SHIFT, Keycode.EIGHT]),
                ("bt4dupe", "NULL"),
                ("enter", Keycode.ENTER),
                ("backspace", Keycode.BACKSPACE),
                ("p", [Keycode.LEFT_SHIFT, Keycode.TWO]),
                ("r_shift", Keycode.RIGHT_SHIFT),
            ]
            return keymap[key][index]
        elif kset == 2:
            keymap = [
                ("touch", Keycode.TAB),
                ("w", Keycode.UP_ARROW),
                ("bt4", [Keycode.GUI, Keycode.ENTER]),
                ("h", Keycode.H),
                ("l", Keycode.L),
                ("s", Keycode.DOWN_ARROW),
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
                ("sym", "SYM1"),
                ("NULL", "NULL"),
                ("y", Keycode.Y),
                ("i", Keycode.I),
                ("d", Keycode.RIGHT_ARROW),
                ("t", Keycode.T),
                ("bt3", [Keycode.GUI, Keycode.BACKSPACE]),
                ("l_alt", Keycode.LEFT_ALT),
                ("bt4dupe", "NULL"),
                ("b", Keycode.B),
                ("vol", "SYM2"),
                ("x", Keycode.X),
                ("v", Keycode.V),
                ("NULL", "NULL"),
                ("a", Keycode.LEFT_ARROW),
                ("bt4dupe", "NULL"),
                ("enter", Keycode.ENTER),
                ("backspace", Keycode.DELETE),
                ("p", Keycode.P),
                ("r_shift", Keycode.RIGHT_SHIFT),
            ]
            return keymap[key][index]
