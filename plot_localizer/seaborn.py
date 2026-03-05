import warnings
from os import environ
from typing import get_args

from packaging.version import Version

from .core.typing import FontStyles
from .core.updater import update_mpl_fontfamily

style = environ.get("PYTHONFONTSTYLE", "sans-serif")
if style not in get_args(FontStyles):
    style = "sans-serif"
_ = update_mpl_fontfamily(style)


try:
    from seaborn import *
    from seaborn import __version__

    if Version(__version__) < Version("0.13.2"):
        warnings.warn(
            f"Imported seaborn version is version {__version__}, but this package requires >= 0.13.2."
        )
except ModuleNotFoundError:
    warnings.warn(
        "failed to import seaborn. Please make sure seaborn is installed.",
        stacklevel=2,
    )
