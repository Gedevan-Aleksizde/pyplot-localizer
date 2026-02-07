#! /usr/bin/env python3

import matplotlib
from matplotlib import rcParams

from .core import update_mpl_fontfamily

update_mpl_fontfamily()

# PDF mode
# PNG などのラスタ画像もこれでよい
rcParams["pdf.fonttype"] = 42
matplotlib.use("cairo")

print("matplotlib-japreset Cairo mode")
