# -*- coding: utf-8 -*-

from gilded_rose.gilded_rose import Item, GildedRose



def test_regular_item():
    item = Item("foo", 10, 10)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    
    assert item.quality == 9
    assert item.sell_in == 9