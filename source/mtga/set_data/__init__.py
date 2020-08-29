from mtga.models.card_set import Pool
try:
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
except:
    raise Exception("FATAL ERROR: could not dynamically generate card sets. Arena must be installed.")
