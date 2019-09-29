""" dynamic.py: this file pulls cards from live .json files in the arena installation (so that e.g. MTGATracker
 doesn't have to update everytime a new set drops).

 This file adapted from generate_set_map.py """
import json
import os
import re
from mtga.models.card import Card
from mtga.models.card_set import Set

def _get_data_location():
    root = os.environ.get(
        "ProgramFiles(x86)",
        os.environ.get(
            "ProgramFiles",
            r"C:\Program Files (x86)"
        )
    )
    return os.path.join(root, "Wizards of the Coast", "MTGA", "MTGA_Data", "Downloads", "Data")

COLOR_ID_MAP = {1: "W", 2: "U", 3: "B", 4: "R", 5: "G"}
RARITY_ID_MAP = {0: "Token", 1: "Basic", 2: "Common", 3: "Uncommon", 4: "Rare", 5: "Mythic Rare"}

dynamic_set_tuples = []

data_location = _get_data_location()

json_filepaths = {"enums": "", "cards": "", "abilities": "", "loc": ""}

for filename in os.listdir(data_location):
    key = filename.split("_")[1]
    if key in json_filepaths.keys() and filename.endswith("mtga"):
        # print("setting {} to {}".format(key, filename))
        json_filepaths[key] = os.path.join(data_location, filename)

with open(json_filepaths["cards"], "r", encoding="utf-8") as card_in:
    cards = json.load(card_in)

with open(json_filepaths["loc"], "r", encoding="utf-8") as loc_in:
    loc = json.load(loc_in)

with open(json_filepaths["enums"], "r", encoding="utf-8") as enums_in:
    enums = json.load(enums_in)

listed_cardsets = list(set([card["set"] for card in cards]))

for set_name in listed_cardsets:
    used_classnames = []
    set_name_class_cased = re.sub('[^0-9a-zA-Z_]', '', set_name)
    all_abilities = {}

    loc_map = {}
    en = list(filter(lambda x: x["langkey"] == "EN", loc))[0]
    for obj in en["keys"]:
        # if obj["id"] in loc_map.keys():
        #     print("WARNING: overwriting id {} = {} with {}".format(obj["id"], loc_map[obj["id"]], obj["text"]))
        loc_map[obj["id"]] = obj["text"]
    loc_map = {obj["id"]: obj["text"] for obj in en["keys"]}
    enum_map = {obj["name"]: {inner_obj["id"]: inner_obj["text"] for inner_obj in obj["values"]} for obj in enums}
    set_cards = [card for card in cards if card["set"].upper() == set_name.upper()]
    assert set_cards, "No cards found in set {}. Double check your nomenclature, and ensure the input files contain your set!"

    token_count = 1

    # print("translating {} cards from set {}".format(len(set_cards), set_name))
    output_lines = []
    set_card_objs = []
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
                if card["CollectorNumber"].startswith("GR") or card["CollectorNumber"].startswith("GP"):
                    set_number = int(card["CollectorNumber"][2]) * 1000
                else:
                    set_number = int(card["CollectorNumber"])

            grp_id = card["grpid"]
            abilities = []

            abilities_raw = card["abilities"]
            for ability in abilities_raw:
                aid = ability["abilityId"]
                textid = ability["textId"]
                text = loc_map[textid].encode("ascii", errors="ignore").decode()
                abilities.append(aid)
                all_abilities[aid] = text

            new_card_obj = Card(name=card_name_snake_cased, pretty_name=card_title, cost=cost,
                                color_identity=color_identity, card_type=card_types, sub_types=sub_types,
                                abilities=abilities, set_id=set_id, rarity=rarity, collectible=collectible,
                                set_number=set_number, mtga_id=grp_id)
            set_card_objs.append(new_card_obj)

        except Exception:
            print("hit an error on {} / {} / {}".format(card["grpid"], loc_map[card["titleId"]],
                                                        card["CollectorNumber"]))
            raise
    card_set_obj = Set(set_name_class_cased, cards=set_card_objs)
    dynamic_set_tuples.append((card_set_obj, all_abilities))

