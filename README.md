# Python MTGA

MTGA tools & set data for python. Generated with MTGJSON and scryfall, original MTGA grpId's
collected by Fugi & Spencatro.

## Installation

`pip install mtga`

or

`python setup.py install`

## Usage

```python
from mtga.set_data import all_mtga_cards
print(all_mtga_cards.find_one("63773"))
# <Card: 'Torrential Gearhulk' ['Blue'] KLD 63773>
```