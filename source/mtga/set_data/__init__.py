from mtga.models.card_set import Pool
import logging


def get_all_mtga_cards_dynamic():
    from mtga.set_data import dynamic
    dynamic_sets = []
    all_mtga_abilities = {}

    for cardset, ability_map in dynamic.dynamic_set_tuples:
        for ability_key in ability_map.keys():
            all_mtga_abilities[ability_key] = ability_map[ability_key]
        dynamic_sets.append(cardset)

        all_mtga_cards = Pool.from_sets("mtga_cards",
                                        sets=[*dynamic_sets],
                                        abilities=all_mtga_abilities)
    return all_mtga_cards, all_mtga_abilities


try:
    all_mtga_cards, all_mtga_abilities = get_all_mtga_cards_dynamic()
except Exception as e:
    logging.error("Could not dynamically generate card sets. Do you have Arena installed?")
    raise Exception("FATAL ERROR: could not dynamically generate card sets. Arena must be installed.")

