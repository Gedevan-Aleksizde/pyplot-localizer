#! /usr/bin/env python3

import matplotlib
from matplotlib import rcParams

from .core import update_mpl_fontfamily

update_mpl_fontfamily()

# PGF mode
# TeX がインストールされてるか確認し, なければ警告する

rcParams["pgf.texsystem"] = "xelatex"
rcParams["mathtext.fontset"] = "cm"  # TODO: 数式フォントまで勝手に変えるのは蛇足か?
# TODO: 主要な拡張数式パッケージは全部カバーできているか?
rcParams["pgf.preamble"] = (
    r"\usepackage{amsmath,amssymb,mathrsfs,cancel,esint,mathdots,mathtools}\usepackage{metalogo}"
)
matplotlib.use("pgf")
print("matplotlib-japreset PGF mode")
