from typing import Dict

from .typing import FontPreset

FONTPRESETS: Dict[str, FontPreset] = {
    "linux": {
        "serif": [
            "Takao PMincho",
            "VL PMincho",
            "Ume P Micho",
            "Ume Mincho",
            "Saznami Gothic",
            "Source Han Sans",
            "Noto Serif CJK JP",
            "Haranoaji Mincho",
            "IPA ExMincho",
            "IPA PMincho",
            "IPA Mincho",
        ],
        "sans-serif": [
            "Takao PGothic",
            "VL PGothic",
            "Ume P Gothic",
            "Ume Gothic",
            "Saznami Mincho",
            "Source Han Sans",
            "Noto Sans CJK JP",
            "Haranoaji Gothic",
            "IPA ExGothic",
            "IPA PGothic",
            "IPA Gothic",
        ],
        "monospace": [
            "Noto Sans Mono CJK JP",
        ],
    },
    "mac": {
        "serif": ["Hiragino Mincho ProN", "YuMincho +36p Kana"],
        "sans-serif": [
            "Hiragino Sans",
            "Hiragino Maru Gothic Pro",
            "Tsukushi A Round Gothic",
            "Tsukushi B Round Gothic",
            "YuGothic",
            "Osaka",
            "AppleGothic",
        ],
        "monospace": ["Osaka"],
    },
    "win_gt7": {
        "serif": ["Yu Gothic", "BIZ UDPMincho", "MS PMincho"],
        "sans-serif": ["Yu Gothic", "Meiryo", "BIZ UDPGothic", "MS PGothic"],
        "monospace": ["MS Gothic"],
    },
    "win_leq7": {
        "serif": ["MS Mincho"],
        "sans-serif": ["MS Gothic"],
        "monospace": ["MS Gothic"],
    },
    "SHARED": {
        "serif": ["Noto Serif CJK JP", "Harano Aji Mincho"],
        "sans-serif": ["Noto Sans CJK JP", "Harano Aji Gothic", "Mgen+ 2cp"],
        "monospace": [
            "M PLUS 1 Code",
            "Ricty Discord",
            "Ricty",
            "Iosevka Term",
            "Iosevka Fixed",
            "Ricty Discord Diminished",
            "Ricty Diminished",
        ],
    },
}
