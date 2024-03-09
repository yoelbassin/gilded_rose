from .managed_item import ManagedItem
from .item import Item


class AgedBrie(ManagedItem):
    def __init__(self, item: Item) -> None:
        self._item = item
        
    def update_quality(self):
        self._item.quality = min(50, self._item.quality + 1)
