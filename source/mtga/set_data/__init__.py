from mtga.models.card_set import Pool
from mtga.set_data import xln, w17, akh, hou, dom, aer, weird, kld, rix, m19

all_mtga_cards = Pool.from_sets("mtga_cards",
                                sets=[rix.RivalsOfIxalan, xln.Ixalan, hou.HourOfDevastation, akh.Amonkhet, dom.Dominaria,
                                      kld.Kaladesh, aer.AetherRevolt, w17.WelcomeDecks2017, m19.CoreSet2019,
                                      weird.WeirdLands])
