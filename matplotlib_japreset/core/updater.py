#! /usr/bin/env python3

import matplotlib
from matplotlib import rcParams

from .search import detect_default_font


def update_mpl_fontfamily() -> None:
    """
    change matplotlib font family to the operating system specific one.
    """
    f = detect_default_font()
    rcParams.update(matplotlib.rcParamsDefault)
    rcParams["font.family"] = f
    print(f"selected font: {f}")
