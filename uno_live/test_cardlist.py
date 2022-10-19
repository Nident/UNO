import pytest
from uno_live.cardlist import Deck, Hand, Heap
from uno_live.card import Card

from random import seed

RANDOM_SEED = 10


def test_heap():
    heap = Heap(Card('red', 3))
    assert (str(heap.top()) == 'r3')
    assert (str(heap) == 'Top: r3')

    heap.add(Card('red', 7))
    assert (str(heap.top()) == 'r7')
    assert (str(heap) == 'Top: r7')

    heap.add(Card('blue', 7))
    assert (str(heap.top()) == 'b7')
    assert (str(heap) == 'Top: b7')


def test_deck():
    d = Deck.generate(['red', 'blue'], [0, 1, 1, 2, 2])
    assert (str(d) == 'r0 r1 r1 r2 r2 b0 b1 b1 b2 b2')

    seed(RANDOM_SEED)
    d.shuffle()
    # print(d)
    assert(str(d) == 'b0 r1 b1 r1 b2 r2 r2 b1 r0 b2')


def test_deck_create():
    d = Deck.create([
        Card('red', 3),
        Card('green', 5),
        Card('red', 7),
        Card('yellow', 8)
    ])
    assert(str(d) == 'r3 g5 r7 y8')


def test_deck_create_from_string():
    s = 'y6 r3 g2 b0 b5'
    d = Deck.create_from_string(s)
    assert(str(d) == s)


def test_hand_playable_list():
    top = Card('r', 1)

    # MATCH BY COLOR
    f = Card('r', 9)
    s = Card('r', 2)
    t = Card('r', 3)
    h = Hand([f, s, t])
    assert(h.playable_list(top) == [f, s, t])

    # MATCH BY NUMBER
    f = Card('y', 1)
    s = Card('g', 1)
    t = Card('b', 1)
    h = Hand([f, s, t])
    assert (h.playable_list(top) == [f, s, t])

    # DIFFERENCE BY NUMBER AND COLOR
    f = Card('r', 2)
    s = Card('y', 1)
    t = Card('g', 9)
    h = Hand([f, s, t])
    assert (h.playable_list(top) == [f, s])


def test_hand_remove():
    top = Card('r', 1)

    f = Card('y', 2)
    s = Card('g', 1)
    t = Card('b', 1)

    h = Hand([f, s, t])

    card_list = h.playable_list(top)
    removable_card = card_list[0]
    h.remove(removable_card)
    assert str(h) == 'y2 b1'

    top = Card('b', 2)
    h = Hand([f, s, t])
    card_list = h.playable_list(top)
    removable_card = card_list[0]
    h.remove(removable_card)
    assert str(h) == 'g1 b1'

    top = Card('y', 1)
    h = Hand([f, s, t])
    card_list = h.playable_list(top)
    removable_card = card_list[0]
    h.remove(removable_card)
    assert str(h) == 'g1 b1'


