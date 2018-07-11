# Python MTGA

MTGA tools & set data for python. Generated with MTGJSON and scryfall, original MTGA grpId's
collected by Fugi & Spencatro.

## Installation

`pip install mtga`

or

`python setup.py install`

## Usage

```python
import mtga_set_data
print(mtga_set_data.all_mtga_cards.find_one("63773"))
# <Card: 'Torrential Gearhulk' ['Blue'] KLD 63773>
```