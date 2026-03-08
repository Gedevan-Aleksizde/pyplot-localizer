#! /usr/bin/env python3

import warnings
from os import environ
from typing import Literal, Optional, get_args

import matplotlib
from matplotlib import rcParams

from .search import check_font_exists, detect_font_preset, get_top_matched_font_name
from .typing import FontStyles


def update_mpl_fontfamily(
    font_style: Optional[str] = None,
    errors: Literal["ignore", "warn", "raise", "fallback"] = "warn",
) -> str:
    """
    change matplotlib font family to the operating system specific one.

    Args
    ------
    font_style: str
        font style (`sans-serif`, `sans`, or `monospace`) or family name.

    Return: str
    -------
    used font family name
    """

    font_name = (
        environ.get("PYTHONFONT", "sans-serif") if font_style is None else font_style
    )
    del font_style
    if errors not in ["ignore", "warn", "raise", "fallback"]:
        warnings.warn(
            f"Argument `erros` should be one of `ignore`, `warn`, `raise`, but {errors} is specified.",
            stacklevel=2,
        )
    if font_name not in get_args(FontStyles) and not check_font_exists(font_name):
        if errors == "warn":
            warnings.warn(
                f"Font `{font_name}` cannot be detected by matplotlib.font_manager",
                stacklevel=2,
            )
        elif errors == "raise":
            raise ValueError(
                f"Font `{font_name}` cannot be detected by matplotlib.font_manager"
            )
        elif errors == "fallback":
            warnings.warn(
                f"Font `{font_name}` cannot be detected by matplotlib.font_manager. `sans-serif` used instead.",
                stacklevel=2,
            )
            font_name = "sans-serif"
        else:
            pass

    font_preset = detect_font_preset()
    rcParams.update(matplotlib.rcParamsDefault)
    rcParams["font.family"] = font_name
    for style in get_args(FontStyles):
        rcParams[f"font.{style}"] = (
            font_preset.get(style, []) + rcParams[f"font.{style}"]
        )
    for style in ["fantasy", "cursive"]:
        rcParams[f"font.{style}"] = (
            font_preset.get("sans-serif", []) + rcParams[f"font.{style}"]
        )
    selected_font = get_top_matched_font_name(
        font_preset[font_name] if font_name in get_args(FontStyles) else [font_name]
    )
    if selected_font == "":
        selected_font = "sans-serif"
    return selected_font
