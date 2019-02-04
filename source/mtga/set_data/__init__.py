from mtga.models.card_set import Pool
from mtga.set_data import xln, dom, rix, m19, ana, grn, rna

all_mtga_abilities = {}
for set_abilities in (rix.set_ability_map, xln.set_ability_map, dom.set_ability_map, m19.set_ability_map,
                      ana.set_ability_map, grn.set_ability_map, rna.set_ability_map):
    all_mtga_abilities.update(set_abilities)

all_mtga_cards = Pool.from_sets("mtga_cards",
                                sets=[rix.RivalsOfIxalan, xln.Ixalan, dom.Dominaria, m19.CoreSet2019,
                                      ana.ArenaExclusives, grn.GuildsOfRavnica, rna.RavnicaAllegiance],
                                abilities=all_mtga_abilities)

