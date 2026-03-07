#! /usr/bin/env python3
from os import environ

from .core.presets import use_preset_cairo, use_preset_pdf, use_preset_pgf
from .core.updater import update_mpl_fontfamily


def set_graphics_as_pdf(font_style: str = "sans-serif") -> None:
    """
    set default font with PDF settings

    Args
    ----
    style: FontStyles
        specify the default font style, which should be one of `sans-serif`, `serif`, or `monospace`
    """
    _ = update_mpl_fontfamily(font_style)
    use_preset_pdf()


def set_graphics_as_cairo(font_style: str = "sans-serif") -> None:
    """
    set default font with Cairo settings

    Args
    ----
    style: FontStyles
        specify the default font style, which should be one of `sans-serif`, `serif`, or `monospace`
    """
    font_style = (
        environ.get("PYTHONFONT", "sans-serif") if font_style is None else font_style
    )
    _ = update_mpl_fontfamily(font_style)
    use_preset_cairo()


def set_graphics_as_pgf(font_style: str = "sans-serif") -> None:
    """
    set default font with PGF settings

    Args
    ----
    style: FontStyles
        specify the default font style, which should be one of `sans-serif`, `serif`, or `monospace`
    """
    font_style = (
        environ.get("PYTHONFONT", "sans-serif") if font_style is None else font_style
    )
    _ = update_mpl_fontfamily(font_style)
    use_preset_pgf()
