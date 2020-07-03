# Python MTGA
MTGA tools & set data for python. Original cardset generated with MTGJSON and scryfall,
with initial set of  MTGA grpId's collected by Fugi & Spencatro.
(Now we just use the data already present in your MTGA installation.)
## Installation
`pip install mtga`
or
`python setup.py install`
## Usage
```python
from mtga.set_data import all_mtga_cards
print(all_mtga_cards.find_one("Mangara"))
# <Card: 'Mangara, the Diplomat' ['White'] M21 71809>
print(all_mtga_cards.find_one(71809))
# <Card: 'Mangara, the Diplomat' ['White'] M21 71809>
print(all_mtga_cards.find_one("71809"))
# <Card: 'Mangara, the Diplomat' ['White'] M21 71809>
```
## Deploying
Because I always forget:
```bash
python setup.py sdist bdist_wheel
twine upload dist/MTGA-<version>*
```