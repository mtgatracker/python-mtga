
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="ROE", rarity="Basic", collectible=True, set_number=229,
              mtga_id=36786)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="ROE", rarity="Basic", collectible=True, set_number=242,
                mtga_id=36788)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="ROE", rarity="Basic", collectible=True, set_number=245,
              mtga_id=36802)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="ROE", rarity="Basic", collectible=True, set_number=237,
             mtga_id=36812)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="ROE", rarity="Basic", collectible=True, set_number=235,
              mtga_id=36818)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
RiseOfEldrazi = Set("roe", cards=clsmembers)

set_ability_map = {}
