
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


FactoryofMomirVig = Card(name="factory_of_momir_vig", pretty_name="Factory of Momir Vig", cost=[],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[121336], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                         mtga_id=68326)
MaelstromNexusEmblem = Card(name="maelstrom_nexus_emblem", pretty_name="Maelstrom Nexus Emblem", cost=[],
                            color_identity=[], card_type="Artifact", sub_types="",
                            abilities=[133330], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                            mtga_id=69746)
OmniscienceEmblem = Card(name="omniscience_emblem", pretty_name="Omniscience Emblem", cost=[],
                         color_identity=['W', 'U', 'B', 'R', 'G'], card_type="Artifact", sub_types="",
                         abilities=[19205, 133323], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                         mtga_id=69761)
TreasureTokenFactory = Card(name="treasure_token_factory", pretty_name="Treasure Token Factory", cost=[],
                            color_identity=[], card_type="Artifact", sub_types="",
                            abilities=[133370], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                            mtga_id=69769)
PandemoniumEmblem = Card(name="pandemonium_emblem", pretty_name="Pandemonium Emblem", cost=[],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[133366], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                         mtga_id=69775)
Treasure = Card(name="treasure", pretty_name="Treasure", cost=[],
                color_identity=[], card_type="Artifact", sub_types="Treasure",
                abilities=[183], set_id="ARENASUP", rarity="Token", collectible=False, set_number=10001,
                mtga_id=69776)
GiantMonstersEmblem = Card(name="giant_monsters_emblem", pretty_name="Giant Monsters Emblem", cost=[],
                           color_identity=[], card_type="Artifact", sub_types="",
                           abilities=[133367], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                           mtga_id=69777)
OverflowingCounters = Card(name="overflowing_counters", pretty_name="Overflowing Counters", cost=[],
                           color_identity=[], card_type="Artifact", sub_types="",
                           abilities=[136374], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                           mtga_id=70146)
ZombieArmy = Card(name="zombie_army", pretty_name="Zombie Army", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Zombie Army",
                  abilities=[], set_id="ARENASUP", rarity="Token", collectible=False, set_number=10002,
                  mtga_id=70469)
LandfallSatchel = Card(name="landfall_satchel", pretty_name="Landfall Satchel", cost=[],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[136492], set_id="ARENASUP", rarity="Mythic Rare", collectible=False, set_number=1,
                       mtga_id=70500)
Plant = Card(name="plant", pretty_name="Plant", cost=[],
             color_identity=[], card_type="Creature", sub_types="Plant",
             abilities=[], set_id="ARENASUP", rarity="Token", collectible=False, set_number=10003,
             mtga_id=70511)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
ArenaSup = Set("arenasup", cards=clsmembers)

set_ability_map = {183: '{oT}, Sacrifice this artifact: Add one mana of any color.',
 19205: 'You may cast spells from your hand without paying their mana costs.',
 121336: "{oX}, Discard a Card: Create a token that's a copy of a random "
         'creature card with converted mana cost X. Activate this ability only '
         'any time you could cast a sorcery and only once each turn.',
 133323: '{o0}: Add {oWoUoBoRoG}. Activate this ability only once each turn.',
 133330: 'Whenever you cast your first spell each turn, exile cards from the '
         'top of your library until you exile a nonland card with converted '
         "mana cost less than that spell's. You may cast that card without "
         "paying its mana cost. Then put the exiled cards that weren't cast "
         'this way on the bottom of that library in a random order.',
 133366: 'Whenever a creature enters the battlefield under your control, this '
         "emblem deals damage equal to that creature's power to target "
         'creature an opponent controls.',
 133367: 'Whenever you cast a creature spell with converted mana cost 4 or '
         'greater, draw a card.',
 133370: 'At the beginning of your upkeep, create a colorless Treasure '
         'artifact token with "{oT}, Sacrifice this artifact: Add one mana of '
         'any color."',
 136374: 'At the beginning of your end step, put a +1/+1 counter on each '
         'creature you control with a +1/+1 counter on it and a loyalty '
         'counter on each planeswalker you control. If you control no '
         'creatures with +1/+1 counters on them and you control no '
         'planeswalkers, amass 1.',
 136492: '<i>Landfall</i>  Whenever a land enters the battlefield under your '
         'control, exile the top card of your library. If that card is a land '
         'card, put it into your hand. If that card is a creature card, put '
         'that card on the bottom of your library and create a 1/1 green Plant '
         'creature token. If that card is a noncreature, nonland card, put '
         'that card on the bottom of your library, each opponent loses 1 life, '
         'and you gain 1 life.'}
