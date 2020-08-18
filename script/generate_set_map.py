""" generate_set_map.py:

given a cards.json and a loc.json, generate a python-mtga style set map.
cards.json can be obtained from the script in Fugiman/deckmaster:
loc.json can also be obtained with minor modifications: data_loc_ instead of data_cards_

"""

import argparse
import json
import re
import pprint
import string

import os

printable = set(string.printable)

data_loc = r"C:\Program Files (x86)\Wizards of the Coast\MTGA\MTGA_Data\Downloads\Data"

jsons = {"enums": None, "cards": None, "abilities": None, "loc": None}

for filename in os.listdir(data_loc):
    key = filename.split("_")[1]
    if key in jsons.keys():
        print("setting {} to {}".format(key, filename))
        jsons[key] = os.path.join(data_loc, filename)

COLOR_ID_MAP = {1: "W", 2: "U", 3: "B", 4: "R", 5: "G"}
RARITY_ID_MAP = {0: "Token", 1: "Basic", 2: "Common", 3: "Uncommon", 4: "Rare", 5: "Mythic Rare"}


def generate_set_map(loc, cards, enums, set_name):
    """
    :param loc: dict w/ contents of of loc.json
    :param cards: dict w/ contents of cards.json
    :param set: set name (GRN, etc)
    """
    used_classnames = []
    set_name_class_cased = re.sub('[^0-9a-zA-Z_]', '', set_name)
    set_name_snake_cased = re.sub('[^0-9a-zA-Z_]', '', set_name.lower().replace(" ", "_"))
    all_abilities = {}

    loc_map = {}
    en = list(filter(lambda x: x["langkey"] == "EN", loc))[0]
    for obj in en["keys"]:
        if obj["id"] in loc_map.keys():
            print("WARNING: overwriting id {} = {} with {}".format(obj["id"], loc_map[obj["id"]], obj["text"]))
        loc_map[obj["id"]] = obj["text"]
    loc_map = {obj["id"]: obj["text"] for obj in en["keys"]}
    enum_map = {obj["name"]: {inner_obj["id"]: inner_obj["text"] for inner_obj in obj["values"]} for obj in enums}
    set_cards = [card for card in cards if card["set"].upper() == set_name.upper()]
    assert set_cards, "No cards found in set {}. Double check your nomenclature, and ensure the input files contain your set!"

    token_count = 1

    print("translating {} cards from set {}".format(len(set_cards), set_name))
    output_lines = []
    for card in set_cards:
        try:
            card_title = loc_map[card["titleId"]]
            card_name_class_cased = re.sub('[^0-9a-zA-Z_]', '', card_title)
            card_name_class_cased_suffixed = card_name_class_cased
            card_suffix = 2

            while card_name_class_cased_suffixed in used_classnames:
                card_name_class_cased_suffixed = card_name_class_cased + str(card_suffix)
                card_suffix += 1
            used_classnames.append(card_name_class_cased_suffixed)

            card_name_snake_cased = re.sub('[^0-9a-zA-Z_]', '', card_title.lower().replace(" ", "_"))
            cc_raw = card["castingcost"]
            # cc's look like: o2o(U/B)o(U/B)o3oUoB, want to turn it into ["2", "(U/B)"] etc
            cost = [cost_part for cost_part in cc_raw.split("o")[1:] if cost_part != "0"]
            color_identity = [COLOR_ID_MAP[color_id] for color_id in card["colorIdentity"]]
            collectible = card["isCollectible"]

            card_type_ids = [enum_map["CardType"][card_type] for card_type in card["types"]]
            card_types = " ".join([loc_map[loc_id] for loc_id in card_type_ids])

            sub_types_ids = [enum_map["SubType"][sub_type] for sub_type in card["subtypes"]]
            sub_types = " ".join([loc_map[loc_id] for loc_id in sub_types_ids])

            set_id = set_name.upper()

            rarity = RARITY_ID_MAP[card["rarity"]]

            if card["isToken"]:
                set_number = token_count + 10000
                token_count += 1
            else:
                if card["collectorNumber"].startswith("GR") or card["collectorNumber"].startswith("GP"):
                    set_number = int(card["collectorNumber"][2]) * 1000
                else:
                    set_number = int(card["collectorNumber"])

            grp_id = card["grpid"]
            abilities = []

            abilities_raw = card["abilities"]
            for ability in abilities_raw:
                aid = ability["abilityId"]
                textid = ability["textId"]
                text = loc_map[textid].encode("ascii", errors="ignore").decode()
                abilities.append(aid)
                all_abilities[aid] = text
            indentation_length = len("{} = Card(".format(card_name_class_cased_suffixed))
            # params: name,    pretty_name, cost,            color_identity, card_type,  sub_types, set_id, rarity,        set_number, mtga_id
            # ex:     "a_b_c", "A B C",     ['3', 'W', 'W'], ['W'],          "Creature", "Angel",  "AKH",   "Mythic Rare", 1,          64801
            # name, pretty_name, cost, color_identity, card_type, sub_types, set_id, rarity, set_number, mtga_id
            new_card_str = '{} = Card(name="{}", pretty_name="{}", cost={},\n' \
                           '{{}}color_identity={}, card_type="{}", sub_types="{}",\n' \
                           '{{}}abilities={}, set_id="{}", rarity="{}", collectible={}, set_number={},\n' \
                           '{{}}mtga_id={})'.format(
                card_name_class_cased_suffixed,
                card_name_snake_cased,
                card_title,
                cost,
                color_identity,
                card_types,
                sub_types,
                abilities,
                set_id,
                rarity,
                collectible,
                set_number,
                grp_id
            ).format(" "*indentation_length, " "*indentation_length, " "*indentation_length)
            output_lines.append(new_card_str)

        except Exception:
            print("hit an error on {} / {} / {}".format(card["grpid"], loc_map[card["titleId"]], card["collectorNumber"]))
            raise
    header = """
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect
"""

    footer = """
clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
{} = Set("{}", cards=clsmembers)

set_ability_map = {}
""".format(set_name_class_cased, set_name_snake_cased, pprint.pformat(all_abilities))
    with open("{}.py".format(set_name.lower()), "w") as set_file:
        set_file.write("{}\n\n{}\n\n{}".format(header, "\n".join(output_lines), footer))


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-l', '--loc_file')
    arg_parser.add_argument('-c', '--cards_file')
    arg_parser.add_argument('-e', '--enums_file')
    arg_parser.add_argument('-s', '--set')
    args = arg_parser.parse_args()

    with open(args.cards_file or jsons["cards"], "r", encoding="utf-8") as card_in:
        cards = json.load(card_in)

    with open(args.loc_file or jsons["loc"], "r", encoding="utf-8") as loc_in:
        loc = json.load(loc_in)
    with open(args.enums_file or jsons["enums"], "r", encoding="utf-8") as enums_in:
        enums = json.load(enums_in)

    if args.set:
        generate_set_map(loc, cards, enums, args.set)
    else:
        print("generating all sets!")
        known_sets = ["ana", "dar", "grn", "m19", "rix", "xln", "rna",
                      "mi", "roe", "rtr", "bfz", "akh", "arenasup", "g18", "eld"]
        for card_set in known_sets:
            generate_set_map(loc, cards, enums, card_set)