# -*- coding: utf-8 -*-
import pytest
from gilded_rose.gilded_rose import Item, GildedRose


@pytest.mark.parametrize(
    "initial_quality, initial_sell_in, expected_quality",
    [(10, 10, 9), (0, 10, 0), (10, 0, 8), (10, -2, 8)],
)
def test_basic_quality_degrading(
    initial_quality: int, initial_sell_in: int, expected_quality: int
):
    item = Item("foo", initial_sell_in, initial_quality)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()

    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "initial_sell_in, expected_sell_in", [(10, 9), (0, -1), (-5, -6)]
)
def test_basic_sell_in_degrading(initial_sell_in: int, expected_sell_in: int):
    item = Item("foo", initial_sell_in, 10)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()

    assert item.sell_in == expected_sell_in
