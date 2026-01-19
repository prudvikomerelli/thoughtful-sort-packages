from typing import Union

Number = Union[int, float]

def sort(width: Number, height: Number, length: Number, mass: Number) -> str:
    """
    Sort a package into STANDARD, SPECIAL, or REJECTED.

    Dimensions: centimeters
    Mass: kilograms
    """
    for name, value in [("width", width), ("height", height), ("length", length), ("mass", mass)]:
        if value is None:
            raise ValueError(f"{name} cannot be None")
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
        if value < 0:
            raise ValueError(f"{name} must be non-negative")

    volume = width * height * length
    bulky = (volume >= 1_000_000) or (max(width, height, length) >= 150)
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
