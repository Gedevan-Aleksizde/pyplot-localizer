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
    errors: Literal["ignore", "warn", "raise"] = "warn",
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
    if errors not in ["ignore", "warn", "raise"]:
        warnings.warn(
            f"argument `erros` should be one of `ignore`, `warn`, `raise`, but {errors} is specified.",
            stacklevel=2,
        )
    if font_name not in get_args(FontStyles) and not check_font_exists(font_name):
        if errors == "warn":
            warnings.warn(
                f"font `{font_name}` cannot be detected by matplotlib.font_manager"
            )
        elif errors == "raise":
            raise ValueError(
                f"font `{font_name}` cannot be detected by matplotlib.font_manager"
            )
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
