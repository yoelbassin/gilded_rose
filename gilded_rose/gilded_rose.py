# -*- coding: utf-8 -*-
from typing import Iterable
from gilded_rose.items import BasicItem, Item


SPECIAL_ITEMS = [
    "Aged Brie",
    "Backstage passes to a TAFKAL80ETC concert",
    "Sulfuras, Hand of Ragnaros",
]


class GildedRose(object):
    def __init__(self, items: Iterable[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if item.name not in SPECIAL_ITEMS:
                managed_item = BasicItem(item)
                managed_item.update_quality()
                managed_item.decrease_sell_in()

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
