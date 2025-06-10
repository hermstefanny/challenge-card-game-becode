from typing import List


class Symbol:
    """Class Symbol Definition"""

    def __init__(self, color: str, icon: str) -> None:
        """Class Symbol constructor that assigns the class attributes"""
        self.color = color
        self.icon = icon
        # one of ["♥", "♦", "♣", "♠"]

    def __str__(self) -> str:
        """String that defines the class Symbol"""
        return f"The symbol object has {self.color} {self.icon}"


class Card(Symbol):
    """Class Card definition"""

    def __init__(self, color: str, icon: List[str], value: str) -> None:
        """Class Card constructor that inherits color and icon attributes and adds value attribute"""
        super().__init__(color, icon)
        self.value = value

    def __str__(self) -> str:
        """String that defines the class Card"""
        return f" {self.value}({self.icon}) {self.color}"
