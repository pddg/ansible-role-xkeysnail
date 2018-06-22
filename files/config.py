# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

define_keymap(None, {
    K('C-h'): Key.LEFT,
    K('C-j'): Key.DOWN,
    K('C-k'): Key.UP,
    K('C-l'): Key.RIGHT,
}, "Vim-like cursor")

define_multipurpose_modmap({
    # SandS
    Key.SPACE: [Key.SPACE, Key.LEFT_SHIFT],
})
