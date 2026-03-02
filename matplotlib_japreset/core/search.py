#! /usr/bin/env python3

import platform
import warnings
from typing import Dict, List

from matplotlib import font_manager

from .typing import FontPreset


def detect_os():
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
    return os_version


font_standard: Dict[str, FontPreset] = {
    "linux": {
        "serif": [
            "Takao PMincho",
            "VL PMincho",
            "Ume P Micho",
            "Ume Mincho",
            "Saznami Gothic",
            "Source Han Sans",
            "Noto Serif CJK JP",
            "Haranoaji Mincho",  # こんな名前?
            "IPA ExMincho",
            "IPA PMincho",
            "IPA Mincho",
        ],
        "sans-serif": [
            "Takao PGothic",
            "VL PGothic",
            "Ume P Gothic",
            "Ume Gothic",
            "Saznami Mincho",
            "Source Han Sans",
            "Noto Sans CJK JP",
            "Haranoaji Gothic",
            "IPA ExGothic",
            "IPA PGothic",
            "IPA Gothic",
        ],
        "monospace": [
            "Noto Sans Mono CJK JP",
        ],
    },
    "mac": {
        "serif": ["Hiragino Mincho ProN", "YuMincho +36p Kana"],
        "sans-serif": [
            "Hiragino Sans",
            "Hiragino Maru Gothic Pro",
            "Tsukushi A Round Gothic",
            "Tsukushi B Round Gothic",
            "YuGothic",
            "Osaka",
            "AppleGothic",
        ],
        "monospace": ["Osaka"],
    },
    "win_gt7": {
        "serif": ["Yu Gothic", "BIZ UDPMincho", "MS PMincho"],
        "sans-serif": ["Yu Gothic", "Meiryo", "BIZ UDPGothic", "MS PGothic"],
        "monospace": ["MS Gothic"],
    },
    "win_leq7": {
        "serif": ["MS Mincho"],
        "sans-serif": ["MS Gothic"],
        "monospace": ["MS Gothic"],
    },
    "SHARED": {
        "serif": ["Noto Serif CJK JP"],
        "sans-serif": ["Noto Sans CJK JP"],
        "monospace": [
            "mplus",
            "Mgenplus",
            "Ricty Discord",
            "Ricty",
            "Iosevka Term",
            "Iosevka Fixed",
            "Ricty Discord Diminished",
            "Ricty Diminished",
        ],
    },
}


def detect_font_preset() -> FontPreset:
    """
    return a system-specific default font namepreset.
    """
    fontset = font_standard.get(detect_os(), {})
    if fontset == dict():
        warnings.warn("system name is not detected", stacklevel=2)
        fontset = font_standard["SHARED"]
    else:
        fontset = {
            style: font_standard["SHARED"][style] + fontlist
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
