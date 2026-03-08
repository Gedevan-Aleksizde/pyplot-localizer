from os import environ

from ..core.updater import update_mpl_fontfamily

style = environ.get("PYTHONFONT", "sans-serif")
_ = update_mpl_fontfamily(style)


import matplotlib
from matplotlib.pyplot import *

__all__ = [*matplotlib.__all__]  # to enable static analysis
