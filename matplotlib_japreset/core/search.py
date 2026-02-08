#! /usr/bin/env python3

import platform
import warnings

import matplotlib as mpl

fontstyle = "sans"
fm = mpl.font_manager.fontManager
os_info = platform.uname()
os_version = ""
if os_info.system == "Windows":
    if os_info.release in ["8", "10"]:
        os_version = "win_gt7"
    else:
        os_version = "win_leq7"
elif os_info.system == "Darwin":
    os_version = "mac"
elif os_info.system == "Linux":
    os_version = "linux"

font_standard = {
    "linux": {
        "serif": "Noto Serif CJK JP",
        "sans": "Noto Sans CJK JP",
        "mono": "Noto Sans Mono CJK JP",
    },
    "mac": {"serif": "AppleGothic", "sans": "AppleGothic", "mono": "AppleGothic"},
    "win_gt7": {"serif": "MS Mincho", "sans": "MS Gothic", "mono": "MS Gothic"},
    "win_leq7": {"serif": "MS Mincho", "sans": "MS Gothic", "mono": "MS Gothic"},
    "fallback": {
        "serif": "Noto Serif CJK JP",
        "sans": "Noto Sans CJK JP",
        "mono": "Noto Sans CJK JP",
    },
}


def detect_default_font() -> str:
    """
    return a system-specific default font name.
    """
    fontset = font_standard.get(os_version, dict())
    if fontset == dict():
        warnings.warn("system name is not detected", stacklevel=2)
        fontset = font_standard["fallback"]
    font_name = fontset.get(fontstyle, "")
    if font_name == "":
        warnings.warn(f"font style `{fontstyle}` is not specified correctly.")
        font_name = font_standard["fallback"]["sans"]
    try:
        fm.findfont(font_name, fallback_to_default=False)
    finally:
        if font_name == "" or font_name is None:
            warnings.warn("The system-specific font is not identified.", stacklevel=2)
        else:
            print(f"identified font: {font_name}")
    return font_name
