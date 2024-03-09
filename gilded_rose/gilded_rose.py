# -*- coding: utf-8 -*-
from typing import Iterable
from gilded_rose.items import (
    BasicItem,
    Item,
    AgedBrie,
    ManagedItem,
    BackstagePass,
    Sulfuras,
    ConjuredItem,
)

def is_conjured(item: Item):
    return "Conjured" in item.name 

def _create_managed_item(item: Item):
    name = item.name
    if is_conjured(item):
        name = item.name.strip("Conjured ")
    match name:
        case "Aged Brie":
            return AgedBrie(item)
        case "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(item)
        case "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
    return BasicItem(item)


def managed_items_factory(item: Item) -> ManagedItem:
    managed_item = _create_managed_item(item)
    if is_conjured(item):
        return ConjuredItem(managed_item)
    return managed_item


class GildedRose(object):
    def __init__(self, items: Iterable[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            managed_item = managed_items_factory(item)
            managed_item.update_quality()
            if item.sell_in <= 0:
                managed_item.update_quality()
            item.sell_in -= 1
