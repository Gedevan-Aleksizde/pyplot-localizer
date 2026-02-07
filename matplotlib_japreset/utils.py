from typing import List, Tuple

import matplotlib.font_manager as fm


def show_font_names() -> List[Tuple[str, str]]:
    """
    show the tuples of name and the file path of each all available fonts.
    """
    flist = fm.fontManager.ttflist
    return [(fe.name, fe.fname) for fe in flist]


# TODO: jupyter 上でフォントの表示例を出力する関数
