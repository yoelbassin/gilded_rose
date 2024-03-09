from .managed_item import ManagedItem
from .item import Item


class BackstagePass(ManagedItem):
    def __init__(self, item: Item) -> None:
        self._item = item
        
    def update_quality(self):
        if self._item.sell_in > 10:
            self._item.quality = min(50, self._item.quality + 1)
        elif self._item.sell_in > 5:
            self._item.quality = min(50, self._item.quality + 2)
        elif self._item.sell_in > 0:
            self._item.quality = min(50, self._item.quality + 3)
        else:
            self._item.quality = 0
