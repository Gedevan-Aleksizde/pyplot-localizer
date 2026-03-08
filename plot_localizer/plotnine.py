import inspect
import warnings
from typing import Optional

from packaging.version import Version

from .core.updater import update_mpl_fontfamily

FONT_FAMILY_P9 = update_mpl_fontfamily()

try:
    import plotnine
    from plotnine import *

    __all__ = [*plotnine.__all__]  # to enable static analysis

    if Version(plotnine.__version__) < Version("0.15.3"):
        warnings.warn(
            f"Imported plotnine version is version {plotnine.__version__}, but plot_localizer requires >= 0.15.3."
        )

    class ggplot(plotnine.ggplot):
        __doc__ = inspect.getdoc(plotnine.ggplot)

        def __init__(
            self, data: Optional = None, mapping: Optional[plotnine.aes] = None
        ):
            super().__init__(data, mapping)
            self.theme += plotnine.theme(
                text=plotnine.element_text(family=FONT_FAMILY_P9)
            )

        def __show__(self):
            if self.theme.text is None:
                self.theme += plotnine.theme(
                    text=plotnine.element_text(family=FONT_FAMILY_P9)
                )
            super().show()

    class theme_classic(plotnine.theme_classic):
        __doc__ = inspect.getdoc(plotnine.theme_classic)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_538(plotnine.theme_538):
        __doc__ = inspect.getdoc(plotnine.theme_538)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_bw(plotnine.theme_bw):
        __doc__ = inspect.getdoc(plotnine.theme_bw)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_dark(plotnine.theme_dark):
        __doc__ = inspect.getdoc(plotnine.theme_dark)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_gray(plotnine.theme_gray):
        __doc__ = inspect.getdoc(plotnine.theme_gray)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_grey(plotnine.theme_grey):
        __doc__ = inspect.getdoc(plotnine.theme_grey)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_light(plotnine.theme_light):
        __doc__ = inspect.getdoc(plotnine.theme_light)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_linedraw(plotnine.theme_linedraw):
        __doc__ = inspect.getdoc(plotnine.theme_linedraw)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_minimal(plotnine.theme_minimal):
        __doc__ = inspect.getdoc(plotnine.theme_minimal)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_seaborn(plotnine.theme_seaborn):
        __doc__ = inspect.getdoc(plotnine.theme_seaborn)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

    class theme_tufte(plotnine.theme_tufte):
        __doc__ = inspect.getdoc(plotnine.theme_tufte)

        def __init__(
            self,
            base_size: int = 11,
            base_family: Optional[str] = None,
            ticks: bool = True,
        ):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family, ticks)

    class theme_void(plotnine.theme_void):
        __doc__ = inspect.getdoc(plotnine.theme_void)

        def __init__(self, base_size: int = 11, base_family: Optional[str] = None):
            if base_family is None:
                base_family = FONT_FAMILY_P9
            super().__init__(base_size, base_family)

except ModuleNotFoundError:
    warnings.warn(
        "failed to import plotnine. Please make sure plotnine is installed.",
        stacklevel=2,
    )
