from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

class Mappings:
    def __init__(self, kset, key, index):
        self.kset = kset
        self.key = key
        self.index = index

    def get_key(self):
        mset = self.kset
        mkey = self.key
        mindex = self.index
        if mset == 0:
            keymap = [
                ("A1", Keycode.ONE),
                ("A2", Keycode.TWO),
                ("A3", Keycode.THREE),
                ("A4", Keycode.FOUR),
                ("A5", Keycode.FIVE),
                ("B1", "Tog1"),
                ("B2", "Tog2"),
                ("B3", "Tog3"),
                ("B4", "Tog4"),
                ("B5", "Tog5"),
                ("C1", "Tog6"),
                ("C2", Keycode.ESCAPE),
                ("C3", Keycode.UP_ARROW),
                ("C4", Keycode.TAB),
                ("C5", Keycode.FIVE),
                ("D1", [Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.TAB]),
                ("D2", Keycode.LEFT_ARROW),
                ("D3", Keycode.DOWN_ARROW),
                ("D4", Keycode.RIGHT_ARROW),
                ("D5", [Keycode.LEFT_CONTROL, Keycode.TAB]),
                ("E1", Keycode.DELETE),
                ("E2", Keycode.SHIFT),
                ("E3", Keycode.PRINT_SCREEN),
                ("E4", [Keycode.LEFT_CONTROL, Keycode.Z]),
                ("E5", Keycode.ENTER),
            ]
            return keymap[mkey][mindex]
        elif mset == 1:
            keymap = [
                ("A1", Keycode.ONE),
                ("A2", Keycode.TWO),
                ("A3", Keycode.THREE),
                ("A4", Keycode.FOUR),
                ("A5", Keycode.FIVE),
                ("B1", "Tog1"),
                ("B2", "Tog2"),
                ("B3", "Tog3"),
                ("B4", "Tog4"),
                ("B5", "Tog5"),
                ("C1", "Tog6"),
                ("C2", Keycode.ESCAPE),
                ("C3", Keycode.UP_ARROW),
                ("C4", Keycode.FOUR),
                ("C5", [Keycode.LEFT_CONTROL, Keycode.X]),
                ("D1", [Keycode.LEFT_ALT, Keycode.SHIFT, Keycode.TAB]),
                ("D2", Keycode.LEFT_ARROW),
                ("D3", Keycode.DOWN_ARROW),
                ("D4", Keycode.RIGHT_ARROW),
                ("D5", [Keycode.LEFT_ALT, Keycode.TAB]),
                ("E1", Keycode.BACKSPACE),
                ("E2", [Keycode.LEFT_CONTROL, Keycode.A]),
                ("E3", [Keycode.LEFT_CONTROL, Keycode.C]),
                ("E4", [Keycode.LEFT_CONTROL, Keycode.Y]),
                ("E5", [Keycode.LEFT_CONTROL, Keycode.V]),
            ]
            return keymap[mkey][mindex]
        elif mset == 2:
            keymap = [
                ("A1", Keycode.ONE),
                ("A2", Keycode.TWO),
                ("A3", Keycode.THREE),
                ("A4", Keycode.FOUR),
                ("A5", Keycode.FIVE),
                ("B1", "Tog1"),
                ("B2", "Tog2"),
                ("B3", "Tog3"),
                ("B4", "Tog4"),
                ("B5", "Tog5"),
                ("C1", "Tog6"),
                ("C2", Keycode.TWO),
                ("C3", Keycode.THREE),
                ("C4", Keycode.FOUR),
                ("C5", Keycode.FIVE),
                ("D1", Keycode.ONE),
                ("D2", Keycode.TWO),
                ("D3", Keycode.THREE),
                ("D4", Keycode.FOUR),
                ("D5", Keycode.FIVE),
                ("E1", Keycode.ONE),
                ("E2", Keycode.TWO),
                ("E3", Keycode.THREE),
                ("E4", Keycode.FOUR),
                ("E5", Keycode.FIVE),
            ]
            return keymap[mkey][mindex]
        elif mset == 3:
            keymap = [
                ("A1", Keycode.ONE),
                ("A2", Keycode.TWO),
                ("A3", Keycode.THREE),
                ("A4", Keycode.FOUR),
                ("A5", Keycode.FIVE),
                ("B1", "Tog1"),
                ("B2", "Tog2"),
                ("B3", "Tog3"),
                ("B4", "Tog4"),
                ("B5", "Tog5"),
                ("C1", "Tog6"),
                ("C2", Keycode.TWO),
                ("C3", Keycode.THREE),
                ("C4", Keycode.FOUR),
                ("C5", Keycode.FIVE),
                ("D1", Keycode.ONE),
                ("D2", Keycode.TWO),
                ("D3", Keycode.THREE),
                ("D4", Keycode.FOUR),
                ("D5", Keycode.FIVE),
                ("E1", Keycode.ONE),
                ("E2", Keycode.TWO),
                ("E3", Keycode.THREE),
                ("E4", Keycode.FOUR),
                ("E5", Keycode.FIVE),
            ]
            return keymap[mkey][mindex]
        elif mset == 4:
            keymap = [
                ("A1", Keycode.ONE),
                ("A2", Keycode.TWO),
                ("A3", Keycode.THREE),
                ("A4", Keycode.FOUR),
                ("A5", Keycode.FIVE),
                ("B1", "Tog1"),
                ("B2", "Tog2"),
                ("B3", "Tog3"),
                ("B4", "Tog4"),
                ("B5", "Tog5"),
                ("C1", "Tog6"),
                ("C2", Keycode.TWO),
                ("C3", Keycode.THREE),
                ("C4", Keycode.FOUR),
                ("C5", Keycode.FIVE),
                ("D1", Keycode.ONE),
                ("D2", Keycode.TWO),
                ("D3", Keycode.THREE),
                ("D4", Keycode.FOUR),
                ("D5", Keycode.FIVE),
                ("E1", Keycode.ONE),
                ("E2", Keycode.TWO),
                ("E3", Keycode.THREE),
                ("E4", Keycode.FOUR),
                ("E5", Keycode.FIVE),
            ]
            return keymap[mkey][mindex]
        elif mset == 5:
            keymap = [
                ("A1", Keycode.ONE),
                ("A2", Keycode.TWO),
                ("A3", Keycode.THREE),
                ("A4", Keycode.FOUR),
                ("A5", Keycode.FIVE),
                ("B1", "Tog1"),
                ("B2", "Tog2"),
                ("B3", "Tog3"),
                ("B4", "Tog4"),
                ("B5", "Tog5"),
                ("C1", "Tog6"),
                ("C2", Keycode.TWO),
                ("C3", Keycode.THREE),
                ("C4", Keycode.FOUR),
                ("C5", Keycode.FIVE),
                ("D1", Keycode.ONE),
                ("D2", Keycode.TWO),
                ("D3", Keycode.THREE),
                ("D4", Keycode.FOUR),
                ("D5", Keycode.FIVE),
                ("E1", Keycode.ONE),
                ("E2", Keycode.TWO),
                ("E3", Keycode.THREE),
                ("E4", Keycode.FOUR),
                ("E5", Keycode.FIVE),
            ]
            return keymap[mkey][mindex]
