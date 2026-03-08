import warnings

from packaging.version import Version

from .core.updater import update_mpl_fontfamily

_ = update_mpl_fontfamily()


try:
    from seaborn import *
    from seaborn import __version__

    if Version(__version__) < Version("0.13.2"):
        warnings.warn(
            f"Imported seaborn version is version {__version__}, but plot_localizer requires >= 0.13.2."
        )
except ModuleNotFoundError:
    warnings.warn(
        "failed to import seaborn. Please make sure seaborn is installed.",
        stacklevel=2,
    )
