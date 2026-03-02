from typing import List, Literal, TypedDict

FontStyles = Literal["sans-serif", "serif", "monospace"]

FontPreset = TypedDict(
    "FontPreset",
    {"serif": List[str], "sans-serif": List[str], "monospace": List[str]},
)
