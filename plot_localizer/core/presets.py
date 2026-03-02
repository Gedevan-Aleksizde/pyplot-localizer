import matplotlib
from matplotlib import rcParams


def use_preset_pdf() -> None:
    # PDF mode
    # PNG などのラスタ画像もこれでよい
    rcParams["pdf.fonttype"] = 42
    matplotlib.use("pdf")

    print("matplotlib-japreset PDF mode")


def use_preset_cairo() -> None:
    # PDF mode
    # PNG などのラスタ画像もこれでよい
    rcParams["pdf.fonttype"] = 42
    matplotlib.use("cairo")

    print("matplotlib-japreset Cairo mode")


def use_preset_pgf() -> None:
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
