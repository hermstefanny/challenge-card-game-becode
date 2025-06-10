from typing import List


class Symbol:
    """Class Symbol Definition"""

    def __init__(self, color: str, icon: str) -> None:
        self.color = color
        self.icon = icon
        # one of ["♥", "♦", "♣", "♠"]


class Card(Symbol):
    """Class Card definition"""

    def __init__(self, color: str, icon: List[str], value: str) -> None:
        super().__init__(color, icon)
        self.value = value

    def __str__(self) -> str:
        return f" {self.value}({self.icon}) {self.color}"

        # one of ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
