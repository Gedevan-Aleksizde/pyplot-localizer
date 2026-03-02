from os import environ
from typing import Optional, get_args

import plotnine

from .core.typing import FontStyles
from .core.updater import update_mpl_fontfamily

style = environ.get("PYTHONFONTSTYLE", "sans-serif")
if style not in get_args(FontStyles):
    style = "sans-serif"
FONT_FAMILY_P9 = update_mpl_fontfamily(style)


class ggplot(plotnine.ggplot):
    def __init__(self, data: Optional = None, mapping: Optional[plotnine.aes] = None):
        super().__init__(data, mapping)
        self.theme += plotnine.theme(text=plotnine.element_text(family=FONT_FAMILY_P9))

    def __show__(self):
        if self.theme.text is None:
            self.theme += plotnine.theme(
                text=plotnine.element_text(family=FONT_FAMILY_P9)
            )
        super().show()


class theme_classic(plotnine.theme_classic):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_538(plotnine.theme_538):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_bw(plotnine.theme_bw):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_dark(plotnine.theme_dark):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_gray(plotnine.theme_gray):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_grey(plotnine.theme_grey):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_light(plotnine.theme_light):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_linedraw(plotnine.theme_linedraw):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_minimal(plotnine.theme_minimal):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_seaborn(plotnine.theme_seaborn):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)


class theme_tufte(plotnine.theme_tufte):
    def __init__(
        self, base_size: int = 11, base_family: Optional[str] = None, ticks: bool = True
    ):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family, ticks)


class theme_void(plotnine.theme_void):
    def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
        if base_family is None:
            base_family = FONT_FAMILY_P9
        super().__init__(base_size, base_family)
