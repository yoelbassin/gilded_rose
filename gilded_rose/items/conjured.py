from .managed_item import ManagedItem


class ConjuredItem(ManagedItem):
    def __init__(self, item: ManagedItem) -> None:
        self._item = item
    
    def update_quality(self) -> None:
        self._item.update_quality()
        self._item.update_quality()