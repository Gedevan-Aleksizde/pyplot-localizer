#! /usr/bin/env python3
from os import environ
from typing import get_args

from ..core.presets import use_preset_pgf
from ..core.typing import FontStyles
from ..core.updater import update_mpl_fontfamily

style = environ.get("PYTHONFONTSTYLE", "sans-serif")
if style not in get_args(FontStyles):
    style = "sans-serif"

update_mpl_fontfamily(style)
use_preset_pgf()
