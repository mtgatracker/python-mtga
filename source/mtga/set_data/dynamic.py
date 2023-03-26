""" dynamic.py: this file pulls cards from live .json files in the arena installation (so that e.g. MTGATracker
 doesn't have to update everytime a new set drops).

 This file adapted from generate_set_map.py """
import json
import os
import re
import sys
from pathlib import Path
from mtga.models.card import Card
from mtga.models.card_set import Set
from mtga.set_data.sqlite2json import sqlite2json


def _get_data_location_hardcoded():
    root = os.environ.get(
        "ProgramFiles",
        r"C:\Program Files"
    )
    return os.path.join(root, "Wizards of the Coast", "MTGA", "MTGA_Data", "Downloads", "Raw")


COLOR_ID_MAP = {1: "W", 2: "U", 3: "B", 4: "R", 5: "G"}
RARITY_ID_MAP = {0: "Token", 1: "Basic", 2: "Common", 3: "Uncommon", 4: "Rare", 5: "Mythic Rare"}


dynamic_set_tuples = []

def get_data_location():
    current_os = sys.platform
    if current_os not in ["darwin", "win32"]:
        raise

    return {
        "darwin": get_darwin_data_location,
        "win32": get_win_data_location,
    }[current_os]()

def get_darwin_data_location():
    return os.path.join(
        os.path.expanduser("~"),
        "Library/Application Support/com.wizards.mtga/Downloads/Raw",
    )

def get_win_data_location():
    try:
        from winreg import ConnectRegistry, OpenKey, HKEY_LOCAL_MACHINE, QueryValueEx
        registry_connection = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        reg_path = r"SOFTWARE\Wizards of the Coast\MTGArena"
        registry_key = OpenKey(registry_connection, reg_path)
        data_location = QueryValueEx(registry_key, "Path")[0] + r"MTGA_Data\Downloads\Raw"
        print("Found data @ ")
        print(data_location)
    except:
        print("Couldn't locate MTGA from registry, falling back to hardcoded path...")
        data_location = _get_data_location_hardcoded()
    return data_location

# To remove Japanese ruby and Alchemy tags
def del_ruby(s):
    return re.sub("（.+?）", "", re.sub("<.+?>", "", s))

data_location = get_data_location()

json_filepaths = {"CardDatabase": ""}

# A newer file SHOULD be the preference; alpha sort of hashes may be out of order
# Otherwise it will be necessary to find which is really used
for filepath in sorted(Path(data_location).iterdir(), key=os.path.getmtime):
    filename = os.path.basename(filepath)
    # In case of rogue files
    filesplit = filename.split("_")
    if len(filesplit) > 1:
        key = filesplit[1]
    else:
        key = ""
    if key in json_filepaths.keys() and filename.endswith("mtga"):
        # print("setting {} to {}".format(key, filename))
        json_filepaths[key] = filepath

abilities, cards, loc, enums = sqlite2json(json_filepaths["CardDatabase"])

listed_cardsets = list(set([card["ExpansionCode"] for card in cards]))

for set_name in listed_cardsets:
    used_classnames = []
    set_name_class_cased = re.sub('[^0-9a-zA-Z_]', '', set_name)
    all_abilities = {}

    loc_map = {obj["id"]: obj["text"] for obj in loc}
    enum_map = {obj["name"]: {inner_obj["id"]: inner_obj["text"] for inner_obj in obj["values"]} for obj in enums}
    set_cards = [card for card in cards if card["ExpansionCode"].upper() == set_name.upper()]
    assert set_cards, "No cards found in set {}. Double check your nomenclature, and ensure the input files contain your set!"

    token_count = 1

    # print("translating {} cards from set {}".format(len(set_cards), set_name))
    output_lines = []
    set_card_objs = []
    for card in set_cards:
        # TODO: card_name_snake_casedの日本語対応
        try:
            if card["TitleId"]:
                card_title = del_ruby(loc_map[card["TitleId"]])
            else:
                card_title = ""
            card_name_class_cased = re.sub('[^0-9a-zA-Z_]', '', card_title)
            card_name_class_cased_suffixed = card_name_class_cased
            card_suffix = 2

            while card_name_class_cased_suffixed in used_classnames:
                card_name_class_cased_suffixed = card_name_class_cased + str(card_suffix)
                card_suffix += 1
            used_classnames.append(card_name_class_cased_suffixed)

            try:
                card_name_snake_cased = re.sub('[^0-9a-zA-Z_]', '', card_title.lower().replace(" ", "_"))
            except AttributeError:
                card_name_snake_cased = ""

            try:
                cc_raw = card["OldSchoolManaText"]
            except (KeyError, TypeError, AttributeError):
                cc_raw = ""
            
            # cc's look like: o2o(U/B)o(U/B)o3oUoB, want to turn it into ["2", "(U/B)"] etc
            try:
                cost = [cost_part for cost_part in cc_raw.split("o")[1:] if cost_part != "0"]
            except AttributeError:
                cost = []

            try:
                color_identity = card["ColorIdentity"].split(",")
            except (KeyError, TypeError, AttributeError):
                color_identity = []
            try:
                #collectible = card["isCollectible"] # "isCollectible" key is not exist.
                collectible = bool(int(card["CollectorMax"]))
            except (KeyError, TypeError, AttributeError, ValueError):
                collectible = False

            try:
                card_type_ids = [enum_map["CardType"][card_type] for card_type in [int(id) for id in card["Types"].split(",")]]
            except (KeyError, TypeError, AttributeError, ValueError):
                card_type_ids = []
            card_types = " ".join([loc_map[loc_id] for loc_id in card_type_ids])

            try:
                sub_types_ids = [enum_map["SubType"][card_type] for card_type in [int(id) for id in card["Subtypes"].split(",")]]
            except (KeyError, TypeError, AttributeError, ValueError):
                sub_types_ids = []
            sub_types = " ".join([loc_map[loc_id] for loc_id in sub_types_ids])

            try:
                super_types_ids = [enum_map["SuperType"][card_type] for card_type in [int(id) for id in card["Supertypes"].split(",")]]
            except (KeyError, TypeError, AttributeError, ValueError):
                super_types_ids = []
            super_types = " ".join([loc_map[loc_id] for loc_id in super_types_ids])

            set_id = set_name.upper()

            try:
                rarity = RARITY_ID_MAP[card["Rarity"]]
            except (KeyError, TypeError, AttributeError):
                rarity = RARITY_ID_MAP[0]
            
            try:
                is_token = card["IsToken"]
            except (KeyError, TypeError, AttributeError):
                is_token = False
            
            if is_token:
                set_number = token_count + 10000
                token_count += 1
            else:
                if card["CollectorNumber"]:
                    try:
                        if card["CollectorNumber"].startswith("GR") or card["CollectorNumber"].startswith("GP"):
                            set_number = int(card["CollectorNumber"][2]) * 1000
                        else:
                            set_number = int(card["CollectorNumber"])
                    except ValueError:
                        set_number = 0
                else:
                    set_number = 0

            grp_id = card["GrpId"]
            card_abilities = []

            try:
                is_secondary_card = not card["IsPrimaryCard"]
            except (KeyError, TypeError, AttributeError):
                is_secondary_card = False

            try:
                is_rebalanced = card["IsRebalanced"]
            except (KeyError, TypeError, AttributeError):
                is_rebalanced = False
            
            try:
                is_digital_only = card["IsDigitalOnly"]
            except (KeyError, TypeError, AttributeError):
                is_digital_only = False

            try:
                abilities_raw = card["AbilityIds"]
            except (KeyError, TypeError, AttributeError):
                abilities_raw = []
            if abilities_raw:
                for ability in abilities_raw.split(","):
                    aid = ability.split(":")[0]
                    textid = ability.split(":")[1] if len(ability.split(":")) >= 2 else None
                    text = ""
                    try:
                        if textid:
                            text = loc_map[textid].encode("ascii", errors="ignore").decode()
                    except:
                        # TODO: there are multiple loc files now?? something weird is up. I don't really feel like trying to
                        # figure this out right now though.
                        text = "unknown ability id {} / {}".format(aid, textid)
                    card_abilities.append(aid)
                    all_abilities[aid] = text

            try:
                hidden_abilities_raw = card["HiddenAbilityIds"]
            except (KeyError, TypeError, AttributeError):
                hidden_abilities_raw = []
            if hidden_abilities_raw:
                for ability in hidden_abilities_raw.split(","):
                    aid = ability.split(":")[0]
                    textid = ability.split(":")[1] if len(ability.split(":")) >= 2 else None
                    text = ""
                    try:
                        if textid:
                            text = loc_map[textid].encode("ascii", errors="ignore").decode()
                    except:
                        # TODO: there are multiple loc files now?? something weird is up. I don't really feel like trying to
                        # figure this out right now though.
                        text = "unknown ability id {} / {}".format(aid, textid)
                    card_abilities.append(aid)
                    all_abilities[aid] = text

            new_card_obj = Card(name=card_name_snake_cased, pretty_name=card_title, cost=cost,
                                color_identity=color_identity, card_type=card_types, sub_types=sub_types, super_types=super_types, 
                                abilities=card_abilities, set_id=set_id, rarity=rarity, collectible=collectible,
                                set_number=set_number, mtga_id=grp_id, 
                                is_token=is_token, is_secondary_card=is_secondary_card, is_rebalanced=is_rebalanced, is_digital_only=is_digital_only)
            set_card_objs.append(new_card_obj)

        except Exception:
            print("hit an error on GrpId: {}".format(card["GrpId"]))
            raise
    card_set_obj = Set(set_name_class_cased, cards=set_card_objs)
    dynamic_set_tuples.append((card_set_obj, all_abilities))
