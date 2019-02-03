
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


BlindingRadiance = Card(name="blinding_radiance", pretty_name="Blinding Radiance", cost=['2', 'W'],
                        color_identity=['W'], card_type="Sorcery", sub_types="",
                        abilities=[121583], set_id="ANA", rarity="Uncommon", collectible=False, set_number=2,
                        mtga_id=68766)
SpiritualGuardian = Card(name="spiritual_guardian", pretty_name="Spiritual Guardian", cost=['3', 'W', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Spirit",
                         abilities=[88604], set_id="ANA", rarity="Common", collectible=True, set_number=11,
                         mtga_id=68767)
TacticalAdvantage = Card(name="tactical_advantage", pretty_name="Tactical Advantage", cost=['W'],
                         color_identity=['W'], card_type="Instant", sub_types="",
                         abilities=[121584], set_id="ANA", rarity="Common", collectible=True, set_number=12,
                         mtga_id=68769)
FeralRoar = Card(name="feral_roar", pretty_name="Feral Roar", cost=['1', 'G'],
                 color_identity=['G'], card_type="Sorcery", sub_types="",
                 abilities=[1031], set_id="ANA", rarity="Common", collectible=False, set_number=46,
                 mtga_id=68771)
ShorecomberCrab = Card(name="shorecomber_crab", pretty_name="Shorecomber Crab", cost=['U'],
                       color_identity=['U'], card_type="Creature", sub_types="Crab",
                       abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=18,
                       mtga_id=68772)
GoblinBruiser = Card(name="goblin_bruiser", pretty_name="Goblin Bruiser", cost=['1', 'R', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                     abilities=[], set_id="ANA", rarity="Uncommon", collectible=False, set_number=39,
                     mtga_id=68773)
ZephyrGull = Card(name="zephyr_gull", pretty_name="Zephyr Gull", cost=['U'],
                  color_identity=['U'], card_type="Creature", sub_types="Bird",
                  abilities=[8], set_id="ANA", rarity="Common", collectible=False, set_number=23,
                  mtga_id=68776)
SoulhunterRakshasa = Card(name="soulhunter_rakshasa", pretty_name="Soulhunter Rakshasa", cost=['3', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Cat Demon",
                          abilities=[86476, 121581], set_id="ANA", rarity="Rare", collectible=False, set_number=35,
                          mtga_id=68782)
RagingGoblin = Card(name="raging_goblin", pretty_name="Raging Goblin", cost=['R'],
                    color_identity=['R'], card_type="Creature", sub_types="Goblin Berserker",
                    abilities=[9], set_id="ANA", rarity="Common", collectible=False, set_number=43,
                    mtga_id=68784)
ConfronttheAssault = Card(name="confront_the_assault", pretty_name="Confront the Assault", cost=['4', 'W'],
                          color_identity=['W'], card_type="Instant", sub_types="",
                          abilities=[121586, 17708], set_id="ANA", rarity="Uncommon", collectible=True, set_number=3,
                          mtga_id=68786)
TakeVengeance = Card(name="take_vengeance", pretty_name="Take Vengeance", cost=['1', 'W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[1385], set_id="ANA", rarity="Common", collectible=False, set_number=13,
                     mtga_id=68787)
KnightsPledge = Card(name="knights_pledge", pretty_name="Knight's Pledge", cost=['1', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 2018], set_id="ANA", rarity="Common", collectible=False, set_number=6,
                     mtga_id=68788)
LoxodonLineBreaker = Card(name="loxodon_line_breaker", pretty_name="Loxodon Line Breaker", cost=['2', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Elephant Soldier",
                          abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=7,
                          mtga_id=68789)
VolcanicDragon = Card(name="volcanic_dragon", pretty_name="Volcanic Dragon", cost=['4', 'R', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Dragon",
                      abilities=[8, 9], set_id="ANA", rarity="Uncommon", collectible=False, set_number=45,
                      mtga_id=68790)
RisefromtheGrave = Card(name="rise_from_the_grave", pretty_name="Rise from the Grave", cost=['4', 'B'],
                        color_identity=['B'], card_type="Sorcery", sub_types="",
                        abilities=[2159], set_id="ANA", rarity="Uncommon", collectible=False, set_number=34,
                        mtga_id=68791)
Waterknot = Card(name="waterknot", pretty_name="Waterknot", cost=['1', 'U', 'U'],
                 color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                 abilities=[1027, 89789, 88178], set_id="ANA", rarity="Common", collectible=False, set_number=22,
                 mtga_id=68792)
SerraAngel = Card(name="serra_angel", pretty_name="Serra Angel", cost=['3', 'W', 'W'],
                  color_identity=['W'], card_type="Creature", sub_types="Angel",
                  abilities=[8, 15], set_id="ANA", rarity="Uncommon", collectible=False, set_number=9,
                  mtga_id=68793)
ChaosMaw = Card(name="chaos_maw", pretty_name="Chaos Maw", cost=['5', 'R', 'R'],
                color_identity=['R'], card_type="Creature", sub_types="Hellion",
                abilities=[103805], set_id="ANA", rarity="Rare", collectible=False, set_number=36,
                mtga_id=68794)
MiasmicMummy = Card(name="miasmic_mummy", pretty_name="Miasmic Mummy", cost=['1', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Zombie Jackal",
                    abilities=[3861], set_id="ANA", rarity="Common", collectible=False, set_number=29,
                    mtga_id=68795)
OverflowingInsight = Card(name="overflowing_insight", pretty_name="Overflowing Insight", cost=['4', 'U', 'U', 'U'],
                          color_identity=['U'], card_type="Sorcery", sub_types="",
                          abilities=[116816], set_id="ANA", rarity="Mythic Rare", collectible=False, set_number=16,
                          mtga_id=68796)
Earthquake = Card(name="earthquake", pretty_name="Earthquake", cost=['X', 'R'],
                  color_identity=['R'], card_type="Sorcery", sub_types="",
                  abilities=[88501], set_id="ANA", rarity="Rare", collectible=False, set_number=38,
                  mtga_id=68797)
AmbitionsCost = Card(name="ambitions_cost", pretty_name="Ambition's Cost", cost=['3', 'B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[1713], set_id="ANA", rarity="Uncommon", collectible=False, set_number=25,
                     mtga_id=68798)
ReaveSoul = Card(name="reave_soul", pretty_name="Reave Soul", cost=['1', 'B'],
                 color_identity=['B'], card_type="Sorcery", sub_types="",
                 abilities=[61990], set_id="ANA", rarity="Common", collectible=False, set_number=32,
                 mtga_id=68799)
Divination = Card(name="divination", pretty_name="Divination", cost=['2', 'U'],
                  color_identity=['U'], card_type="Sorcery", sub_types="",
                  abilities=[23607], set_id="ANA", rarity="Common", collectible=False, set_number=14,
                  mtga_id=68800)
RumblingBaloth = Card(name="rumbling_baloth", pretty_name="Rumbling Baloth", cost=['2', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Beast",
                      abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=47,
                      mtga_id=68801)
GoblinGrenade = Card(name="goblin_grenade", pretty_name="Goblin Grenade", cost=['R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[92793, 4801], set_id="ANA", rarity="Uncommon", collectible=False, set_number=41,
                     mtga_id=68802)
RenegadeDemon = Card(name="renegade_demon", pretty_name="Renegade Demon", cost=['3', 'B', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Demon",
                     abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=33,
                     mtga_id=68803)
SanctuaryCat = Card(name="sanctuary_cat", pretty_name="Sanctuary Cat", cost=['W'],
                    color_identity=['W'], card_type="Creature", sub_types="Cat",
                    abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=8,
                    mtga_id=68804)
FortressCrab = Card(name="fortress_crab", pretty_name="Fortress Crab", cost=['3', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Crab",
                    abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=15,
                    mtga_id=68805)
AltarsReap = Card(name="altars_reap", pretty_name="Altar's Reap", cost=['1', 'B'],
                  color_identity=['B'], card_type="Instant", sub_types="",
                  abilities=[1275, 23607], set_id="ANA", rarity="Common", collectible=False, set_number=24,
                  mtga_id=68806)
FleshbagMarauder = Card(name="fleshbag_marauder", pretty_name="Fleshbag Marauder", cost=['2', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Zombie Warrior",
                        abilities=[89023], set_id="ANA", rarity="Uncommon", collectible=False, set_number=28,
                        mtga_id=68807)
Goblin = Card(name="goblin", pretty_name="Goblin", cost=[],
              color_identity=[], card_type="Creature", sub_types="Goblin",
              abilities=[], set_id="ANA", rarity="Token", collectible=False, set_number=10001,
              mtga_id=68808)
Spirit = Card(name="spirit", pretty_name="Spirit", cost=[],
              color_identity=[], card_type="Creature", sub_types="Spirit",
              abilities=[8], set_id="ANA", rarity="Token", collectible=False, set_number=10002,
              mtga_id=68809)
CruxofFate = Card(name="crux_of_fate", pretty_name="Crux of Fate", cost=['3', 'B', 'B'],
                  color_identity=['B'], card_type="Sorcery", sub_types="",
                  abilities=[101832], set_id="ANA", rarity="Rare", collectible=False, set_number=27,
                  mtga_id=68810)
SeismicRupture = Card(name="seismic_rupture", pretty_name="Seismic Rupture", cost=['2', 'R'],
                      color_identity=['R'], card_type="Sorcery", sub_types="",
                      abilities=[96294], set_id="ANA", rarity="Uncommon", collectible=False, set_number=44,
                      mtga_id=68811)
Twincast = Card(name="twincast", pretty_name="Twincast", cost=['U', 'U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[1246], set_id="ANA", rarity="Rare", collectible=False, set_number=21,
                mtga_id=68812)
Murder = Card(name="murder", pretty_name="Murder", cost=['1', 'B', 'B'],
              color_identity=['B'], card_type="Instant", sub_types="",
              abilities=[26818], set_id="ANA", rarity="Uncommon", collectible=False, set_number=30,
              mtga_id=68813)
Doublecast = Card(name="doublecast", pretty_name="Doublecast", cost=['R', 'R'],
                  color_identity=['R'], card_type="Sorcery", sub_types="",
                  abilities=[119092], set_id="ANA", rarity="Uncommon", collectible=False, set_number=37,
                  mtga_id=68814)
AngelicReward = Card(name="angelic_reward", pretty_name="Angelic Reward", cost=['3', 'W', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 8812], set_id="ANA", rarity="Uncommon", collectible=True, set_number=1,
                     mtga_id=69108)
HallowedPriest = Card(name="hallowed_priest", pretty_name="Hallowed Priest", cost=['2', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                      abilities=[103130], set_id="ANA", rarity="Uncommon", collectible=False, set_number=4,
                      mtga_id=69109)
InspiringCommander = Card(name="inspiring_commander", pretty_name="Inspiring Commander", cost=['4', 'W', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                          abilities=[121578], set_id="ANA", rarity="Rare", collectible=True, set_number=5,
                          mtga_id=69110)
ShrineKeeper = Card(name="shrine_keeper", pretty_name="Shrine Keeper", cost=['W', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                    abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=10,
                    mtga_id=69111)
RiversFavor = Card(name="rivers_favor", pretty_name="River's Favor", cost=['U'],
                   color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                   abilities=[1027, 3974], set_id="ANA", rarity="Common", collectible=False, set_number=17,
                   mtga_id=69112)
TitanicPelagosaur = Card(name="titanic_pelagosaur", pretty_name="Titanic Pelagosaur", cost=['3', 'U', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[], set_id="ANA", rarity="Uncommon", collectible=False, set_number=19,
                         mtga_id=69113)
TrappedinaWhirlpool = Card(name="trapped_in_a_whirlpool", pretty_name="Trapped in a Whirlpool", cost=['3', 'U'],
                           color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                           abilities=[1027, 88178], set_id="ANA", rarity="Common", collectible=False, set_number=20,
                           mtga_id=69114)
CruelCut = Card(name="cruel_cut", pretty_name="Cruel Cut", cost=['1', 'B'],
                color_identity=['B'], card_type="Instant", sub_types="",
                abilities=[30246], set_id="ANA", rarity="Common", collectible=False, set_number=26,
                mtga_id=69115)
NimblePilferer = Card(name="nimble_pilferer", pretty_name="Nimble Pilferer", cost=['1', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Human Rogue",
                      abilities=[7], set_id="ANA", rarity="Common", collectible=False, set_number=31,
                      mtga_id=69116)
GoblinGangLeader = Card(name="goblin_gang_leader", pretty_name="Goblin Gang Leader", cost=['2', 'R', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                        abilities=[96140], set_id="ANA", rarity="Uncommon", collectible=False, set_number=40,
                        mtga_id=69117)
OgrePainbringer = Card(name="ogre_painbringer", pretty_name="Ogre Painbringer", cost=['3', 'R', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Ogre",
                       abilities=[121351], set_id="ANA", rarity="Rare", collectible=False, set_number=42,
                       mtga_id=69118)
TreetopWarden = Card(name="treetop_warden", pretty_name="Treetop Warden", cost=['1', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Warrior",
                     abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=48,
                     mtga_id=69119)
AncientCrab = Card(name="ancient_crab", pretty_name="Ancient Crab", cost=['1', 'U', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Crab",
                   abilities=[], set_id="ANA", rarity="Common", collectible=False, set_number=49,
                   mtga_id=69441)
HiredBlade = Card(name="hired_blade", pretty_name="Hired Blade", cost=['2', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Human Assassin",
                  abilities=[7], set_id="ANA", rarity="Common", collectible=False, set_number=50,
                  mtga_id=69442)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="ANA", rarity="Basic", collectible=False, set_number=51,
              mtga_id=69443)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="ANA", rarity="Basic", collectible=False, set_number=52,
              mtga_id=69444)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="ANA", rarity="Basic", collectible=False, set_number=53,
             mtga_id=69445)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="ANA", rarity="Basic", collectible=False, set_number=54,
                mtga_id=69446)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="ANA", rarity="Basic", collectible=False, set_number=55,
              mtga_id=69447)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
ArenaExclusives = Set("ana", cards=clsmembers)

set_ability_map = {7: 'Flash',
 8: 'Flying',
 9: 'Haste',
 15: 'Vigilance',
 1027: 'Enchant creature',
 1031: 'Target creature gets +4/+4 until end of turn.',
 1246: 'Copy target instant or sorcery spell. You may choose new targets for '
       'the copy.',
 1275: 'As an additional cost to cast this spell, sacrifice a creature.',
 1385: 'Destroy target tapped creature.',
 1713: 'You draw three cards and you lose 3 life.',
 2018: 'Enchanted creature gets +2/+2.',
 2159: 'Put target creature card from a graveyard onto the battlefield under '
       'your control. That creature is a black Zombie in addition to its other '
       'colors and types.',
 3861: 'When Miasmic Mummy enters the battlefield, each player discards a '
       'card.',
 3974: 'Enchanted creature gets +1/+1.',
 4801: 'Goblin Grenade deals 5 damage to any target.',
 8812: 'Enchanted creature gets +3/+3 and has flying.',
 17708: 'Create three 1/1 white Spirit creature tokens with flying.',
 23607: 'Draw two cards.',
 26818: 'Destroy target creature.',
 30246: 'Destroy target creature with power 2 or less.',
 61990: 'Destroy target creature with power 3 or less.',
 86476: "Soulhunter Rakshasa can't block.",
 88178: "Enchanted creature doesn't untap during its controller's untap step.",
 88501: 'Earthquake deals X damage to each creature without flying and each '
        'player.',
 88604: 'When Spiritual Guardian enters the battlefield, you gain 4 life.',
 89023: 'When Fleshbag Marauder enters the battlefield, each player sacrifices '
        'a creature.',
 89789: 'When Waterknot enters the battlefield, tap enchanted creature.',
 92793: 'As an additional cost to cast this spell, sacrifice a Goblin.',
 96140: 'When Goblin Gang Leader enters the battlefield, create two 1/1 red '
        'Goblin creature tokens.',
 96294: 'Seismic Rupture deals 2 damage to each creature without flying.',
 101832: 'Choose one   Destroy all Dragon creatures.  Destroy all non-Dragon '
         'creatures.',
 103130: 'When Hallowed Priest enters the battlefield, create a 1/1 white '
         'Spirit creature token with flying.',
 103805: 'When Chaos Maw enters the battlefield, it deals 3 damage to each '
         'other creature.',
 116816: 'Target player draws seven cards.',
 119092: 'When you cast your next instant or sorcery spell this turn, copy '
         'that spell. You may choose new targets for the copy.',
 121351: 'When Ogre Painbringer enters the battlefield, it deals 3 damage to '
         'each player.',
 121578: 'Whenever another creature with power 2 or less enters the '
         'battlefield under your control, you gain 1 life and draw a card.',
 121581: 'When Soulhunter Rakshasa enters the battlefield, it deals 5 damage '
         'to target opponent.',
 121583: 'Tap all creatures your opponents control with toughness 2 or less.',
 121584: 'Target blocking or blocked creature you control gets +2/+2 until end '
         'of turn.',
 121586: 'Cast this spell only if a creature is attacking you.'}
