from .item import Item
from .managed_item import ManagedItem


class BasicItem(ManagedItem):
    def __init__(self, item: Item) -> None:
        self._item = item
        
    def _update_quality_once(self):
        self._item.quality = max(0, self._item.quality - 1)
                
    def update_quality(self) -> None:
        if self._item.sell_in <= 0:
            self._update_quality_once()
        self._update_quality_once()

    def decrease_sell_in(self) -> None:
        self._item.sell_in -= 1
        
