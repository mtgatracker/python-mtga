from .models import card, card_set
from .models.card_set import Pool
import xln
import rix
import hou
import akh
import dom
import weird
import kld
import aer
import w17

all_mtga_cards = Pool.from_sets("mtga_cards",
                      sets=[rix.RivalsOfIxalan, xln.Ixalan, hou.HourOfDevastation, akh.Amonkhet, dom.Dominaria,
                            kld.Kaladesh, aer.AetherRevolt, w17.WelcomeDecks2017, weird.WeirdLands])