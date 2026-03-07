import warnings

from packaging.version import Version

from .core.updater import update_mpl_fontfamily

_ = update_mpl_fontfamily()


try:
    import pandas
    from pandas import *
    from pandas import __version__

    __all__ = [*pandas.__all__]  # to enable static analysis

    if Version(__version__) < Version("2.0.0"):
        warnings.warn(
            f"Imported pandas version is version {__version__}, but this plot_localizer requires >= 2.0.0."
        )
except ModuleNotFoundError:
    warnings.warn(
        "failed to import pandas. Please make sure seaborn is installed.",
        stacklevel=2,
    )
