from .item import Item
from .managed_item import ManagedItem


class Sulfuras(ManagedItem):
    def __init__(self, item: Item) -> None:
        self._item = item
    
    def update_quality(self) -> None:
        ...
