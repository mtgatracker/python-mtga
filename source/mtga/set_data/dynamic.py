""" dynamic.py: this file pulls cards from live .json files in the arena installation (so that e.g. MTGATracker
 doesn't have to update everytime a new set drops).

 This file adapted from generate_set_map.py """
import json
import locale
import os
import re
import sys
from pathlib import Path
from mtga.models.card import Card
from mtga.models.card_set import Set


def _get_data_location_hardcoded():
    root = os.environ.get(
        "ProgramFiles",
        r"C:\Program Files"
    )
    return os.path.join(root, "Wizards of the Coast", "MTGA", "MTGA_Data", "Downloads", "Data")


COLOR_ID_MAP = {1: "W", 2: "U", 3: "B", 4: "R", 5: "G"}
RARITY_ID_MAP = {0: "Token", 1: "Basic", 2: "Common", 3: "Uncommon", 4: "Rare", 5: "Mythic Rare"}
ISO_CODE_MAP = {
    "English": "en-US",
    "French": "fr-FR",
    "Italian": "it-IT",
    "German": "de-DE",
    "Spanish": "es-ES",
    "Japanese": "ja-JP",
    "Portuguese": "pt-BR",
    "Russian": "ru-RU",
    "Korean": "ko-KR",
}

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
        "Library/Application Support/com.wizards.mtga/Downloads/Data",
    )

def get_win_data_location():
    try:
        from winreg import ConnectRegistry, OpenKey, HKEY_LOCAL_MACHINE, QueryValueEx
        registry_connection = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        reg_path = r"SOFTWARE\Wizards of the Coast\MTGArena"
        registry_key = OpenKey(registry_connection, reg_path)
        data_location = QueryValueEx(registry_key, "Path")[0] + r"MTGA_Data\Downloads\Data"
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

json_filepaths = {"enums": "", "cards": "", "abilities": "", "loc": ""}

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

with open(json_filepaths["cards"], "r", encoding="utf-8") as card_in:
    cards = json.load(card_in)

with open(json_filepaths["loc"], "r", encoding="utf-8") as loc_in:
    loc = json.load(loc_in)

with open(json_filepaths["enums"], "r", encoding="utf-8") as enums_in:
    enums = json.load(enums_in)

listed_cardsets = list(set([card["set"] for card in cards]))

# To generate 'CardDictionary.csv' for ゆかりねっとコネクター NEO
CARD_DICTIONARY_FILENAME = "CardDictionary.csv"
card_dictionary_csv = []

for set_name in listed_cardsets:
    used_classnames = []
    set_name_class_cased = re.sub('[^0-9a-zA-Z_]', '', set_name)
    all_abilities = {}

    try:
        iso_code = ISO_CODE_MAP.get(locale.getlocale()[0].split("_")[0])
    except:
        iso_code = ISO_CODE_MAP.get("English")
    loc_map = {}
    try:
        lang = list(filter(lambda x: x["isoCode"] == iso_code, loc))[0]
    except:
        lang = loc[0]
    for obj in lang["keys"]:
        # if obj["id"] in loc_map.keys():
        #     print("WARNING: overwriting id {} = {} with {}".format(obj["id"], loc_map[obj["id"]], obj["text"]))
        loc_map[obj["id"]] = obj["text"]
    loc_map = {obj["id"]: obj["text"] for obj in lang["keys"]}
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

            # To generate 'CardDictionary.csv' for ゆかりねっとコネクター NEO
            card_name = del_ruby(card_title)
            line = card_name + "," + card_name + "\n"
            if line not in card_dictionary_csv:
                card_dictionary_csv.append(line)

            while card_name_class_cased_suffixed in used_classnames:
                card_name_class_cased_suffixed = card_name_class_cased + str(card_suffix)
                card_suffix += 1
            used_classnames.append(card_name_class_cased_suffixed)

            card_name_snake_cased = re.sub('[^0-9a-zA-Z_]', '', card_title.lower().replace(" ", "_"))
            try:
                cc_raw = card["castingcost"]
            except KeyError:
                cc_raw = ""
            # cc's look like: o2o(U/B)o(U/B)o3oUoB, want to turn it into ["2", "(U/B)"] etc
            cost = [cost_part for cost_part in cc_raw.split("o")[1:] if cost_part != "0"]
            try:
                color_identity = [COLOR_ID_MAP[color_id] for color_id in card["colorIdentity"]]
            except KeyError:
                color_identity = []
            try:
                collectible = card["isCollectible"]
            except KeyError:
                collectible = False

            try:
                card_type_ids = [enum_map["CardType"][card_type] for card_type in card["types"]]
            except KeyError:
                card_type_ids = []
            card_types = " ".join([loc_map[loc_id] for loc_id in card_type_ids])

            try:
                sub_types_ids = [enum_map["SubType"][sub_type] for sub_type in card["subtypes"]]
            except KeyError:
                sub_types_ids = []
            sub_types = " ".join([loc_map[loc_id] for loc_id in sub_types_ids])

            set_id = set_name.upper()

            try:
                rarity = RARITY_ID_MAP[card["rarity"]]
            except KeyError:
                rarity = RARITY_ID_MAP[0]
            
            try:
                is_token = card["isToken"]
            except KeyError:
                is_token = False
            
            if is_token:
                set_number = token_count + 10000
                token_count += 1
            else:
                try:
                    if card["collectorNumber"].startswith("GR") or card["collectorNumber"].startswith("GP"):
                        set_number = int(card["collectorNumber"][2]) * 1000
                    else:
                        set_number = int(card["collectorNumber"])
                except ValueError:
                    set_number = card["grpid"]

            grp_id = card["grpid"]
            abilities = []

            try:
                abilities_raw = card["abilities"]
            except KeyError:
                abilities_raw = []
            for ability in abilities_raw:
                aid = ability["Id"]
                textid = ability["TextId"]
                try:
                    text = loc_map[textid].encode("ascii", errors="ignore").decode()
                except:
                    # TODO: there are multiple loc files now?? something weird is up. I don't really feel like trying to
                    # figure this out right now though.
                    text = "unknown ability id {} / {}".format(aid, textid)
                abilities.append(aid)
                all_abilities[aid] = text

            try:
                hidden_abilities_raw = card["hiddenAbilities"]
            except KeyError:
                hidden_abilities_raw = []
            for ability in hidden_abilities_raw:
                aid = ability["Id"]
                textid = ability["TextId"]
                try:
                    text = loc_map[textid].encode("ascii", errors="ignore").decode()
                except:
                    # TODO: there are multiple loc files now?? something weird is up. I don't really feel like trying to
                    # figure this out right now though.
                    text = "unknown ability id {} / {}".format(aid, textid)
                abilities.append(aid)
                all_abilities[aid] = text

            new_card_obj = Card(name=card_name_snake_cased, pretty_name=card_title, cost=cost,
                                color_identity=color_identity, card_type=card_types, sub_types=sub_types,
                                abilities=abilities, set_id=set_id, rarity=rarity, collectible=collectible,
                                set_number=set_number, mtga_id=grp_id)
            set_card_objs.append(new_card_obj)

        except Exception:
            print("hit an error on {} / {} / {}".format(card["grpid"], loc_map[card["titleId"]],
                                                        card["collectorNumber"]))
            # raise
    card_set_obj = Set(set_name_class_cased, cards=set_card_objs)
    dynamic_set_tuples.append((card_set_obj, all_abilities))

# To generate 'CardDictionary.csv' for ゆかりねっとコネクター NEO
card_dictionary_csv.sort(reverse=True)
with open(CARD_DICTIONARY_FILENAME, "w", encoding="utf-8") as f:
    for line in card_dictionary_csv:
        f.write(line)
    print(os.path.abspath(CARD_DICTIONARY_FILENAME) + " was generated")
