#! /usr/bin/env python3
from .core.presets import use_preset_cairo, use_preset_pdf, use_preset_pgf
from .core.updater import update_mpl_fontfamily


def set_graphics_as_pdf() -> None:
    update_mpl_fontfamily()
    use_preset_pdf()


def set_graphics_as_cairo() -> None:
    update_mpl_fontfamily()
    use_preset_cairo()


def set_graphics_as_pgf() -> None:
    update_mpl_fontfamily()
    use_preset_pgf()
