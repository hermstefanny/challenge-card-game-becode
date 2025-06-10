from typing import List


class Symbol:
    """Class Symbol Definition"""

    def __init__(self, color: str, icon: List[str]) -> None:
        self.color = color
        self.icon = ["♥", "♦", "♣", "♠"]


class Card(Symbol):
    """Class Card definition"""

    def __init__(self, color: str, icon: List[str], value: List[str]) -> None:
        super().__init__(color, icon)
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
