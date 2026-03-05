from os import environ
from typing import get_args

from ..core.typing import FontStyles
from ..core.updater import update_mpl_fontfamily

style = environ.get("PYTHONFONTSTYLE", "sans-serif")
if style not in get_args(FontStyles):
    style = "sans-serif"
_ = update_mpl_fontfamily(style)


import matplotlib
from matplotlib.pyplot import *

__all__ = [*matplotlib.__all__]  # to enable static analysis
