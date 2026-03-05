from os import environ
from typing import get_args

from ..core.typing import FontStyles
from ..core.updater import update_mpl_fontfamily

style = environ.get("PYTHONFONTSTYLE", "sans-serif")
if style not in get_args(FontStyles):
    style = "sans-serif"
_ = update_mpl_fontfamily(style)


from matplotlib.pyplot import *
