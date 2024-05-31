import sys
import os
from fontTools.ttLib import TTFont

ttFont = TTFont(sys.argv[1])

print("Fixing names for", os.path.basename(sys.argv[1]))


def get_name(ID):
    for name in ttFont["name"].names:
        if name.nameID == ID:
            return name.toUnicode()
    return None


def set_name(nameID, value):
    print(f"Setting name ID {nameID} to {value}")
    ttFont["name"].setName(value, nameID, 1, 0, 0)
    ttFont["name"].setName(value, nameID, 3, 1, 0x409)


def delete_name(ID):
    ttFont["name"].names = [name for name in ttFont["name"].names if name.nameID != ID]


# Get family name
familyName = get_name(16) or get_name(1)

# Get style name
styleName = get_name(17) or get_name(2)

# OS/2.fsSelection bit 7 (USE_TYPO_METRICS)
fsSelection = ttFont["OS/2"].fsSelection
fsSelection |= 1 << 7
ttFont["OS/2"].fsSelection = fsSelection


# Set matrics
ttFont["OS/2"].usWinDescent = 449

# Set copyright
set_name(
    0,
    "Copyright 2024 The Beiruti Project Authors (https://github.com/googlefonts/beiruti)",
)

# Set license
set_name(
    13,
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org",
)
set_name(
    14,
    "https://openfontlicense.org",
)

ttFont.save(sys.argv[1])
