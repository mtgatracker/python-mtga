#!/usr/bin/env python3

import mtga

all_styles = [set(card.styles) for card in mtga.all_mtga_cards.cards]
print(set().union(*all_styles))
