# -*- coding: utf-8 -*-
from typing import Iterable
from gilded_rose.items import BasicItem, Item, AgedBrie, ManagedItem, BackstagePass, Sulfuras


SPECIAL_ITEMS = [
    "Aged Brie",
    "Backstage passes to a TAFKAL80ETC concert",
    "Sulfuras, Hand of Ragnaros",
]


def managed_items_factory(item: Item) -> ManagedItem:
    match item.name:
        case "Aged Brie":
            return AgedBrie(item)
        case "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(item)
        case "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
    return BasicItem(item)


class GildedRose(object):
    def __init__(self, items: Iterable[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if (
                item.name not in SPECIAL_ITEMS
                or item.name == "Aged Brie"
                or item.name == "Backstage passes to a TAFKAL80ETC concert"
                or item.name == "Sulfuras, Hand of Ragnaros"
            ):
                managed_item = managed_items_factory(item)
                managed_item.update_quality()
                if item.sell_in <= 0:
                    managed_item.update_quality()
                item.sell_in -= 1

            else:

                if (
                    item.name != "Aged Brie"
                    and item.name != "Backstage passes to a TAFKAL80ETC concert"
                ):
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                        if item.name == "Backstage passes to a TAFKAL80ETC concert":
                            if item.sell_in < 11:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                            if item.sell_in < 6:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.name != "Aged Brie":
                        if item.name != "Backstage passes to a TAFKAL80ETC concert":
                            if item.quality > 0:
                                if item.name != "Sulfuras, Hand of Ragnaros":
                                    item.quality = item.quality - 1
                        else:
                            item.quality = item.quality - item.quality
                    else:
                        if item.quality < 50:
                            item.quality = item.quality + 1
