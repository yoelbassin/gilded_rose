from .item import Item
from .managed_item import ManagedItem


class BasicItem(ManagedItem):
    def __init__(self, item: Item) -> None:
        self._item = item
        
    def update_quality(self):
        self._item.quality = max(0, self._item.quality - 1)
