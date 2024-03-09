# -*- coding: utf-8 -*-
import pytest
from gilded_rose.gilded_rose import Item, GildedRose


def create_item_and_update_quality(
    name: str = "foo",
    sell_in: int = 10,
    quality: int = 10,
    conjured: bool = False
) -> Item:
    if conjured:
        name = f"Conjured {name}"
    item = Item(name, sell_in, quality)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    return item


@pytest.mark.parametrize(
    "initial_quality, initial_sell_in, expected_quality",
    [(10, 10, 9), (0, 10, 0), (10, 0, 8), (10, -2, 8)],
)
def test_basic_quality_degrading(
    initial_quality: int, initial_sell_in: int, expected_quality: int
):
    item = create_item_and_update_quality(
        sell_in=initial_sell_in, quality=initial_quality
    )
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "initial_sell_in, expected_sell_in", [(10, 9), (0, -1), (-5, -6)]
)
def test_basic_sell_in_degrading(initial_sell_in: int, expected_sell_in: int):
    item = create_item_and_update_quality(sell_in=initial_sell_in)
    assert item.sell_in == expected_sell_in


@pytest.mark.parametrize(
    "initial_quality, initial_sell_in, expected_quality",
    [(10, 10, 11), (50, 10, 50), (10, 0, 12), (50, 0, 50)],
)
def test_aged_brie_quality_degrading(initial_quality: int, initial_sell_in: int, expected_quality: int):
    item = create_item_and_update_quality(
        name="Aged Brie", sell_in=initial_sell_in, quality=initial_quality
    )
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "initial_quality, initial_sell_in, expected_quality",
    [
        (10, 15, 11),
        (10, 10, 12),
        (10, 5, 13),
        (50, 15, 50),
        (50, 10, 50),
        (50, 5, 50),
        (10, 0, 0),
    ],
)
def test_backstage_passes_quality_degrading(
    initial_quality: int, initial_sell_in: int, expected_quality: int
):
    item = create_item_and_update_quality(
        name="Backstage passes to a TAFKAL80ETC concert",
        sell_in=initial_sell_in,
        quality=initial_quality,
    )
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "initial_quality, initial_sell_in, expected_quality", [(10, 5, 10), (10, 0, 10)]
)
def test_sulfuras(initial_quality: int, initial_sell_in: int, expected_quality: int):
    item = create_item_and_update_quality(
        name="Sulfuras, Hand of Ragnaros",
        sell_in=initial_sell_in,
        quality=initial_quality,
    )
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "initial_quality, initial_sell_in, expected_quality",
    [
        (10, 10, 8), (0, 10, 0), (10, 0, 6), (10, -2, 6),
    ],
)
def test_basic_conjured_item(
    initial_quality: int, initial_sell_in: int, expected_quality: int
):
    item = create_item_and_update_quality(
        conjured=True,
        sell_in=initial_sell_in,
        quality=initial_quality,
    )
    assert item.quality == expected_quality 
    