from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.mcp23017 import MCP23017
from kmk.keys import KC

keyboard = KMKKeyboard()

# Nothing on MCU directly
keyboard.col_pins = []
keyboard.row_pins = []

keyboard.diode_orientation = DiodeOrientation.COL2ROW

mcp = MCP23017(
    i2c=None,  
    address=0x20,
    mcp_rows=[0, 1, 2, 3, 4],     
    mcp_cols=[8, 9, 10, 11, 12, 13, 14, 15, 6, 7, 5, 3, 2, 1],  
)

keyboard.modules.append(mcp)

keyboard.keymap = [
    [
        KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, KC.NO, KC.NO,
        KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.ENT, KC.NO, KC.NO,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.NO, KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()
