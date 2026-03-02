#! /usr/bin/env python3

from typing import get_args

import matplotlib
from matplotlib import rcParams

from .search import detect_font_preset, get_top_matched_font_name
from .typing import FontStyles


def update_mpl_fontfamily(
    font_style: FontStyles,
) -> str:
    """
    change matplotlib font family to the operating system specific one.

    Return: str
    -------
    used font family name
    """
    font_preset = detect_font_preset()
    rcParams.update(matplotlib.rcParamsDefault)
    rcParams["font.family"] = font_style
    for style in get_args(FontStyles):
        rcParams[f"font.{style}"] = (
            font_preset.get(style, []) + rcParams[f"font.{style}"]
        )
    selected_font = get_top_matched_font_name(font_preset[font_style])
    return selected_font
