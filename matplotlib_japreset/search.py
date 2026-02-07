#! /usr/bin/env python3

import platform

import matplotlib as mpl

family = "sans"
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
}


def detect_default_font() -> str:
    font_name = font_standard[os_version][family]
    try:
        fm.findfont(font_name, fallback_to_default=False)
    finally:
        print(f"{font_name} not found")
    return font_name
