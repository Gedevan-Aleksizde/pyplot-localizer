#! /usr/bin/env python3

import platform
import warnings
from typing import List

from matplotlib import font_manager

from .fonts import FONTPRESETS
from .typing import FontPreset


def detect_os():
    os_info = platform.uname()
    os_version = ""
    if os_info.system == "Windows":
        if os_info.release in [
            "2000",
            "2003Server",
            "post2003",
            "XP",
            "2008Serve",
            "2008ServerR2",
            "Vista",
            "7",
        ]:
            os_version = "win_leq7"
        else:
            os_version = "win_gt7"
    elif os_info.system == "Darwin":
        os_version = "mac"
    elif os_info.system == "Linux":
        os_version = "linux"
    return os_version


def detect_font_preset() -> FontPreset:
    """
    return a system-specific default font namepreset.
    """
    fontset = FONTPRESETS.get(detect_os(), {})
    if fontset == dict():
        warnings.warn("system name is not detected", stacklevel=2)
        fontset = FONTPRESETS["SHARED"]
    else:
        fontset = {
            style: FONTPRESETS["SHARED"][style] + fontlist
            for style, fontlist in fontset.items()
        }
    return fontset


def get_top_matched_font_name(font_families: List[str]) -> str:
    fm = font_manager.fontManager
    picked_font = ""
    for name in font_families:
        try:
            font_path = fm.findfont(name, fallback_to_default=False)
        except ValueError:
            font_path = None
        if font_path != "" and font_path is not None:
            print(f"identified font: {name}")
            picked_font = name
            break
    if picked_font == "":
        warnings.warn("no available font!", stacklevel=2)
    return picked_font


def check_font_exists(font_name: str) -> bool:
    """
    check if specified font name is found in matplotlib ttf list.
    """
    flist = font_manager.fontManager.ttflist
    detected = [(fe.name, fe.fname) for fe in flist if fe.name == font_name]
    return len(detected) > 0
