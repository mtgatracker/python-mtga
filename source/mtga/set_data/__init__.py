from mtga.models.card_set import Pool
from mtga.set_data import xln, dom, rix, m19, ana, grn, rna, war, m20, eld, akh, arenasup, bfz, mi, roe, rtr

all_mtga_abilities = {**rix.set_ability_map, **xln.set_ability_map, **dom.set_ability_map, **m19.set_ability_map,
                      **ana.set_ability_map, **grn.set_ability_map, **rna.set_ability_map, **war.set_ability_map,
                      **m20.set_ability_map, **eld.set_ability_map, **akh.set_ability_map, **arenasup.set_ability_map,
                      **bfz.set_ability_map, **mi.set_ability_map, **roe.set_ability_map, **rtr.set_ability_map}

all_mtga_cards = Pool.from_sets("mtga_cards",
                                sets=[rix.RivalsOfIxalan, xln.Ixalan, dom.Dominaria, m19.CoreSet2019,
                                      ana.ArenaExclusives, grn.GuildsOfRavnica, rna.RavnicaAllegiance,
                                      war.WarOfTheSpark, m20.CoreSet2020, eld.ThroneOfEldraine, akh.Amonkhet,
                                      arenasup.ArenaSup, bfz.BattleForZendikar, mi.Mirage, roe.RiseOfEldrazi,
                                      rtr.ReturnToRavnica],
                                abilities=all_mtga_abilities)

