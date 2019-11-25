
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


AllThatGlitters = Card(name="all_that_glitters", pretty_name="All That Glitters", cost=['1', 'W'],
                       color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                       abilities=[1027, 136335], set_id="ELD", rarity="Uncommon", collectible=True, set_number=2,
                       mtga_id=70149)
ShiningArmor = Card(name="shining_armor", pretty_name="Shining Armor", cost=['1', 'W'],
                    color_identity=['W'], card_type="Artifact", sub_types="Equipment",
                    abilities=[7, 136241, 7610, 1156], set_id="ELD", rarity="Common", collectible=True, set_number=29,
                    mtga_id=70176)
VenerableKnight = Card(name="venerable_knight", pretty_name="Venerable Knight", cost=['W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                       abilities=[136079], set_id="ELD", rarity="Uncommon", collectible=True, set_number=35,
                       mtga_id=70182)
AnimatingFaerie = Card(name="animating_faerie", pretty_name="Animating Faerie", cost=['2', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Faerie",
                       abilities=[8], set_id="ELD", rarity="Uncommon", collectible=True, set_number=38,
                       mtga_id=70185)
CorridorMonitor = Card(name="corridor_monitor", pretty_name="Corridor Monitor", cost=['1', 'U'],
                       color_identity=['U'], card_type="Artifact Creature", sub_types="Construct",
                       abilities=[136084], set_id="ELD", rarity="Common", collectible=True, set_number=41,
                       mtga_id=70188)
FaerieVandal = Card(name="faerie_vandal", pretty_name="Faerie Vandal", cost=['1', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Faerie Rogue",
                    abilities=[7, 8, 136108], set_id="ELD", rarity="Uncommon", collectible=True, set_number=45,
                    mtga_id=70192)
Frogify = Card(name="frogify", pretty_name="Frogify", cost=['1', 'U'],
               color_identity=['U'], card_type="Enchantment", sub_types="Aura",
               abilities=[1027, 136125], set_id="ELD", rarity="Uncommon", collectible=True, set_number=47,
               mtga_id=70194)
RunAwayTogether = Card(name="run_away_together", pretty_name="Run Away Together", cost=['1', 'U'],
                       color_identity=['U'], card_type="Instant", sub_types="",
                       abilities=[136218], set_id="ELD", rarity="Common", collectible=True, set_number=62,
                       mtga_id=70209)
WitchingWell = Card(name="witching_well", pretty_name="Witching Well", cost=['U'],
                    color_identity=['U'], card_type="Artifact", sub_types="",
                    abilities=[100685, 136240], set_id="ELD", rarity="Common", collectible=True, set_number=74,
                    mtga_id=70221)
BakeintoaPie = Card(name="bake_into_a_pie", pretty_name="Bake into a Pie", cost=['2', 'B', 'B'],
                    color_identity=['B'], card_type="Instant", sub_types="",
                    abilities=[136246], set_id="ELD", rarity="Common", collectible=True, set_number=76,
                    mtga_id=70223)
BelleoftheBrawl = Card(name="belle_of_the_brawl", pretty_name="Belle of the Brawl", cost=['2', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Human Knight",
                       abilities=[142, 136248], set_id="ELD", rarity="Uncommon", collectible=True, set_number=78,
                       mtga_id=70225)
FoulmireKnight = Card(name="foulmire_knight", pretty_name="Foulmire Knight", cost=['B'],
                      color_identity=['B'], card_type="Creature", sub_types="Zombie Knight",
                      abilities=[1], set_id="ELD", rarity="Uncommon", collectible=True, set_number=90,
                      mtga_id=70237)
OrderofMidnight = Card(name="order_of_midnight", pretty_name="Order of Midnight", cost=['1', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Human Knight",
                       abilities=[8, 86476], set_id="ELD", rarity="Uncommon", collectible=True, set_number=99,
                       mtga_id=70246)
SmittenSwordmaster = Card(name="smitten_swordmaster", pretty_name="Smitten Swordmaster", cost=['1', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Human Knight",
                          abilities=[12], set_id="ELD", rarity="Common", collectible=True, set_number=105,
                          mtga_id=70252)
SyrKonradtheGrim = Card(name="syr_konrad_the_grim", pretty_name="Syr Konrad, the Grim", cost=['3', 'B', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Human Knight",
                        abilities=[136076, 136077], set_id="ELD", rarity="Uncommon", collectible=True, set_number=107,
                        mtga_id=70254)
CrystalSlipper = Card(name="crystal_slipper", pretty_name="Crystal Slipper", cost=['1', 'R'],
                      color_identity=['R'], card_type="Artifact", sub_types="Equipment",
                      abilities=[136299, 1268], set_id="ELD", rarity="Common", collectible=True, set_number=119,
                      mtga_id=70266)
EmberethShieldbreaker = Card(name="embereth_shieldbreaker", pretty_name="Embereth Shieldbreaker", cost=['1', 'R'],
                             color_identity=['R'], card_type="Creature", sub_types="Human Knight",
                             abilities=[], set_id="ELD", rarity="Uncommon", collectible=True, set_number=122,
                             mtga_id=70269)
BeanstalkGiant = Card(name="beanstalk_giant", pretty_name="Beanstalk Giant", cost=['6', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Giant",
                      abilities=[88259], set_id="ELD", rarity="Uncommon", collectible=True, set_number=149,
                      mtga_id=70296)
KeeperofFables = Card(name="keeper_of_fables", pretty_name="Keeper of Fables", cost=['3', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Cat",
                      abilities=[136258], set_id="ELD", rarity="Uncommon", collectible=True, set_number=163,
                      mtga_id=70310)
RosethornAcolyte = Card(name="rosethorn_acolyte", pretty_name="Rosethorn Acolyte", cost=['2', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                        abilities=[1055], set_id="ELD", rarity="Common", collectible=True, set_number=174,
                        mtga_id=70321)
GarrukCursedHuntsman = Card(name="garruk_cursed_huntsman", pretty_name="Garruk, Cursed Huntsman", cost=['4', 'B', 'G'],
                            color_identity=['B', 'G'], card_type="Planeswalker", sub_types="Garruk",
                            abilities=[136126, 104880, 136128], set_id="ELD", rarity="Mythic Rare", collectible=True, set_number=191,
                            mtga_id=70338)
InspiringVeteran = Card(name="inspiring_veteran", pretty_name="Inspiring Veteran", cost=['R', 'W'],
                        color_identity=['R', 'W'], card_type="Creature", sub_types="Human Knight",
                        abilities=[119104], set_id="ELD", rarity="Uncommon", collectible=True, set_number=194,
                        mtga_id=70341)
MaraleafPixie = Card(name="maraleaf_pixie", pretty_name="Maraleaf Pixie", cost=['G', 'U'],
                     color_identity=['G', 'U'], card_type="Creature", sub_types="Faerie",
                     abilities=[8, 18504], set_id="ELD", rarity="Uncommon", collectible=True, set_number=196,
                     mtga_id=70343)
SavvyHunter = Card(name="savvy_hunter", pretty_name="Savvy Hunter", cost=['1', 'B', 'G'],
                   color_identity=['B', 'G'], card_type="Creature", sub_types="Human Warrior",
                   abilities=[136251, 136147], set_id="ELD", rarity="Uncommon", collectible=True, set_number=200,
                   mtga_id=70347)
Shinechaser = Card(name="shinechaser", pretty_name="Shinechaser", cost=['1', 'W', 'U'],
                   color_identity=['W', 'U'], card_type="Creature", sub_types="Faerie",
                   abilities=[8, 15, 103355, 136148], set_id="ELD", rarity="Uncommon", collectible=True, set_number=201,
                   mtga_id=70348)
SteelclawLance = Card(name="steelclaw_lance", pretty_name="Steelclaw Lance", cost=['B', 'R'],
                      color_identity=['B', 'R'], card_type="Artifact", sub_types="Equipment",
                      abilities=[2512, 136149, 1156], set_id="ELD", rarity="Uncommon", collectible=True, set_number=202,
                      mtga_id=70349)
WintermoorCommander = Card(name="wintermoor_commander", pretty_name="Wintermoor Commander", cost=['W', 'B'],
                           color_identity=['W', 'B'], card_type="Creature", sub_types="Human Knight",
                           abilities=[1, 136151, 136152], set_id="ELD", rarity="Uncommon", collectible=True, set_number=205,
                           mtga_id=70352)
ArcanistsOwl = Card(name="arcanists_owl", pretty_name="Arcanist's Owl", cost=['(W/U)', '(W/U)', '(W/U)', '(W/U)'],
                    color_identity=['W', 'U'], card_type="Artifact Creature", sub_types="Bird",
                    abilities=[8, 136153], set_id="ELD", rarity="Uncommon", collectible=True, set_number=206,
                    mtga_id=70353)
FirebornKnight = Card(name="fireborn_knight", pretty_name="Fireborn Knight", cost=['(R/W)', '(R/W)', '(R/W)', '(R/W)'],
                      color_identity=['R', 'W'], card_type="Creature", sub_types="Human Knight",
                      abilities=[3, 136269], set_id="ELD", rarity="Uncommon", collectible=True, set_number=210,
                      mtga_id=70357)
GoldenEgg = Card(name="golden_egg", pretty_name="Golden Egg", cost=['2'],
                 color_identity=[], card_type="Artifact", sub_types="Food",
                 abilities=[86788, 88207, 136278], set_id="ELD", rarity="Common", collectible=True, set_number=220,
                 mtga_id=70367)
HeraldicBanner = Card(name="heraldic_banner", pretty_name="Heraldic Banner", cost=['3'],
                      color_identity=[], card_type="Artifact", sub_types="",
                      abilities=[88237, 136279, 2374], set_id="ELD", rarity="Uncommon", collectible=True, set_number=222,
                      mtga_id=70369)
ShamblingSuit = Card(name="shambling_suit", pretty_name="Shambling Suit", cost=['3'],
                     color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                     abilities=[1316], set_id="ELD", rarity="Uncommon", collectible=True, set_number=230,
                     mtga_id=70377)
WitchsOven = Card(name="witchs_oven", pretty_name="Witch's Oven", cost=['1'],
                  color_identity=[], card_type="Artifact", sub_types="",
                  abilities=[136178], set_id="ELD", rarity="Uncommon", collectible=True, set_number=237,
                  mtga_id=70384)
TournamentGrounds = Card(name="tournament_grounds", pretty_name="Tournament Grounds", cost=[],
                         color_identity=['W', 'B', 'R'], card_type="Land", sub_types="",
                         abilities=[1152, 136198], set_id="ELD", rarity="Uncommon", collectible=True, set_number=248,
                         mtga_id=70395)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=250,
              mtga_id=70397)
Plains2 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=251,
               mtga_id=70398)
Plains3 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=252,
               mtga_id=70399)
Plains4 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=253,
               mtga_id=70400)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=254,
              mtga_id=70401)
Island2 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=255,
               mtga_id=70402)
Island3 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=256,
               mtga_id=70403)
Island4 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=257,
               mtga_id=70404)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=258,
             mtga_id=70405)
Swamp2 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=259,
              mtga_id=70406)
Swamp3 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=260,
              mtga_id=70407)
Swamp4 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=261,
              mtga_id=70408)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=262,
                mtga_id=70409)
Mountain2 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=263,
                 mtga_id=70410)
Mountain3 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=264,
                 mtga_id=70411)
Mountain4 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=265,
                 mtga_id=70412)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=266,
              mtga_id=70413)
Forest2 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=267,
               mtga_id=70414)
Forest3 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=268,
               mtga_id=70415)
Forest4 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="ELD", rarity="Basic", collectible=True, set_number=269,
               mtga_id=70416)
WindScarredCrag = Card(name="windscarred_crag", pretty_name="Wind-Scarred Crag", cost=[],
                       color_identity=['R', 'W'], card_type="Land", sub_types="",
                       abilities=[76735, 90050, 4247], set_id="ELD", rarity="Common", collectible=True, set_number=308,
                       mtga_id=70421)
ThornwoodFalls = Card(name="thornwood_falls", pretty_name="Thornwood Falls", cost=[],
                      color_identity=['G', 'U'], card_type="Land", sub_types="",
                      abilities=[76735, 90050, 18504], set_id="ELD", rarity="Common", collectible=True, set_number=313,
                      mtga_id=70426)
Goat = Card(name="goat", pretty_name="Goat", cost=[],
            color_identity=[], card_type="Creature", sub_types="Goat",
            abilities=[], set_id="ELD", rarity="Token", collectible=False, set_number=10001,
            mtga_id=70427)
Human = Card(name="human", pretty_name="Human", cost=[],
             color_identity=[], card_type="Creature", sub_types="Human",
             abilities=[], set_id="ELD", rarity="Token", collectible=False, set_number=10002,
             mtga_id=70428)
Knight = Card(name="knight", pretty_name="Knight", cost=[],
              color_identity=[], card_type="Creature", sub_types="Knight",
              abilities=[15], set_id="ELD", rarity="Token", collectible=False, set_number=10003,
              mtga_id=70429)
Mouse = Card(name="mouse", pretty_name="Mouse", cost=[],
             color_identity=[], card_type="Creature", sub_types="PlaceholderSubType2",
             abilities=[], set_id="ELD", rarity="Token", collectible=False, set_number=10004,
             mtga_id=70430)
Faerie = Card(name="faerie", pretty_name="Faerie", cost=[],
              color_identity=[], card_type="Creature", sub_types="Faerie",
              abilities=[8], set_id="ELD", rarity="Token", collectible=False, set_number=10005,
              mtga_id=70431)
Rat = Card(name="rat", pretty_name="Rat", cost=[],
           color_identity=[], card_type="Creature", sub_types="Rat",
           abilities=[], set_id="ELD", rarity="Token", collectible=False, set_number=10006,
           mtga_id=70432)
Dwarf = Card(name="dwarf", pretty_name="Dwarf", cost=[],
             color_identity=[], card_type="Creature", sub_types="Dwarf",
             abilities=[], set_id="ELD", rarity="Token", collectible=False, set_number=10007,
             mtga_id=70433)
Bear = Card(name="bear", pretty_name="Bear", cost=[],
            color_identity=[], card_type="Creature", sub_types="Bear",
            abilities=[], set_id="ELD", rarity="Token", collectible=False, set_number=10008,
            mtga_id=70434)
Boar = Card(name="boar", pretty_name="Boar", cost=[],
            color_identity=[], card_type="Creature", sub_types="Boar",
            abilities=[136165], set_id="ELD", rarity="Token", collectible=False, set_number=10009,
            mtga_id=70435)
Giant = Card(name="giant", pretty_name="Giant", cost=[],
             color_identity=[], card_type="Creature", sub_types="Giant",
             abilities=[], set_id="ELD", rarity="Token", collectible=False, set_number=10010,
             mtga_id=70436)
HumanCleric = Card(name="human_cleric", pretty_name="Human Cleric", cost=[],
                   color_identity=[], card_type="Creature", sub_types="Human Cleric",
                   abilities=[12, 9], set_id="ELD", rarity="Token", collectible=False, set_number=10011,
                   mtga_id=70437)
HumanRogue = Card(name="human_rogue", pretty_name="Human Rogue", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Human Rogue",
                  abilities=[9, 136242], set_id="ELD", rarity="Token", collectible=False, set_number=10012,
                  mtga_id=70438)
HumanWarrior = Card(name="human_warrior", pretty_name="Human Warrior", cost=[],
                    color_identity=[], card_type="Creature", sub_types="Human Warrior",
                    abilities=[14, 9], set_id="ELD", rarity="Token", collectible=False, set_number=10013,
                    mtga_id=70439)
Wolf = Card(name="wolf", pretty_name="Wolf", cost=[],
            color_identity=[], card_type="Creature", sub_types="Wolf",
            abilities=[136216], set_id="ELD", rarity="Token", collectible=False, set_number=10014,
            mtga_id=70440)
Food = Card(name="food", pretty_name="Food", cost=[],
            color_identity=[], card_type="Artifact", sub_types="Food",
            abilities=[197], set_id="ELD", rarity="Token", collectible=False, set_number=10015,
            mtga_id=70441)
Food2 = Card(name="food", pretty_name="Food", cost=[],
             color_identity=[], card_type="Artifact", sub_types="Food",
             abilities=[197], set_id="ELD", rarity="Token", collectible=False, set_number=10016,
             mtga_id=70442)
Food3 = Card(name="food", pretty_name="Food", cost=[],
             color_identity=[], card_type="Artifact", sub_types="Food",
             abilities=[197], set_id="ELD", rarity="Token", collectible=False, set_number=10017,
             mtga_id=70443)
Food4 = Card(name="food", pretty_name="Food", cost=[],
             color_identity=[], card_type="Artifact", sub_types="Food",
             abilities=[197], set_id="ELD", rarity="Token", collectible=False, set_number=10018,
             mtga_id=70444)
MaceoftheValiant = Card(name="mace_of_the_valiant", pretty_name="Mace of the Valiant", cost=['2', 'W'],
                        color_identity=['W'], card_type="Artifact", sub_types="Equipment",
                        abilities=[136349, 136350, 1156], set_id="ELD", rarity="Rare", collectible=True, set_number=314,
                        mtga_id=70447)
FaerieFormation = Card(name="faerie_formation", pretty_name="Faerie Formation", cost=['4', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Faerie",
                       abilities=[8, 136368], set_id="ELD", rarity="Rare", collectible=True, set_number=316,
                       mtga_id=70449)
ShimmerDragon = Card(name="shimmer_dragon", pretty_name="Shimmer Dragon", cost=['4', 'U', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Dragon",
                     abilities=[8, 136352, 136364], set_id="ELD", rarity="Rare", collectible=True, set_number=317,
                     mtga_id=70450)
WorkshopElders = Card(name="workshop_elders", pretty_name="Workshop Elders", cost=['6', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                      abilities=[136353, 136366], set_id="ELD", rarity="Rare", collectible=True, set_number=318,
                      mtga_id=70451)
TasteofDeath = Card(name="taste_of_death", pretty_name="Taste of Death", cost=['4', 'B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[136355], set_id="ELD", rarity="Rare", collectible=True, set_number=320,
                    mtga_id=70453)
SteelbaneHydra = Card(name="steelbane_hydra", pretty_name="Steelbane Hydra", cost=['X', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Turtle Hydra",
                      abilities=[76885, 136369], set_id="ELD", rarity="Rare", collectible=True, set_number=322,
                      mtga_id=70455)
ThornMammoth = Card(name="thorn_mammoth", pretty_name="Thorn Mammoth", cost=['5', 'G', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Elephant",
                    abilities=[14, 136357], set_id="ELD", rarity="Rare", collectible=True, set_number=323,
                    mtga_id=70456)
AlelaArtfulProvocateur = Card(name="alela_artful_provocateur", pretty_name="Alela, Artful Provocateur", cost=['1', 'W', 'U', 'B'],
                              color_identity=['W', 'U', 'B'], card_type="Creature", sub_types="Faerie Warlock",
                              abilities=[8, 1, 12, 121999, 136371], set_id="ELD", rarity="Mythic Rare", collectible=True, set_number=324,
                              mtga_id=70457)
BanishintoFable = Card(name="banish_into_fable", pretty_name="Banish into Fable", cost=['4', 'W', 'U'],
                       color_identity=['W', 'U'], card_type="Instant", sub_types="",
                       abilities=[1389, 136359], set_id="ELD", rarity="Rare", collectible=True, set_number=325,
                       mtga_id=70458)
ChulaneTellerofTales = Card(name="chulane_teller_of_tales", pretty_name="Chulane, Teller of Tales", cost=['2', 'G', 'W', 'U'],
                            color_identity=['W', 'U', 'G'], card_type="Creature", sub_types="Human Druid",
                            abilities=[15, 136373, 1392], set_id="ELD", rarity="Mythic Rare", collectible=True, set_number=326,
                            mtga_id=70459)
KnightsCharge = Card(name="knights_charge", pretty_name="Knights' Charge", cost=['1', 'W', 'B'],
                     color_identity=['W', 'B'], card_type="Enchantment", sub_types="",
                     abilities=[1395, 136361], set_id="ELD", rarity="Rare", collectible=True, set_number=328,
                     mtga_id=70461)
KorvoldFaeCursedKing = Card(name="korvold_faecursed_king", pretty_name="Korvold, Fae-Cursed King", cost=['2', 'B', 'R', 'G'],
                            color_identity=['B', 'R', 'G'], card_type="Creature", sub_types="Dragon Noble",
                            abilities=[8, 136365, 1398], set_id="ELD", rarity="Mythic Rare", collectible=True, set_number=329,
                            mtga_id=70462)
SyrGwynHeroofAshvale = Card(name="syr_gwyn_hero_of_ashvale", pretty_name="Syr Gwyn, Hero of Ashvale", cost=['3', 'R', 'W', 'B'],
                            color_identity=['W', 'B', 'R'], card_type="Creature", sub_types="Human Knight",
                            abilities=[15, 142, 1399, 1400], set_id="ELD", rarity="Mythic Rare", collectible=True, set_number=330,
                            mtga_id=70463)
ArcaneSignet = Card(name="arcane_signet", pretty_name="Arcane Signet", cost=['2'],
                    color_identity=[], card_type="Artifact", sub_types="",
                    abilities=[90126], set_id="ELD", rarity="Common", collectible=True, set_number=331,
                    mtga_id=70464)
TomeofLegends = Card(name="tome_of_legends", pretty_name="Tome of Legends", cost=['2'],
                     color_identity=[], card_type="Artifact", sub_types="",
                     abilities=[136362, 136372, 136363], set_id="ELD", rarity="Rare", collectible=True, set_number=332,
                     mtga_id=70465)
CommandTower = Card(name="command_tower", pretty_name="Command Tower", cost=[],
                    color_identity=[], card_type="Land", sub_types="",
                    abilities=[90126], set_id="ELD", rarity="Common", collectible=True, set_number=333,
                    mtga_id=70466)
BringtoLife = Card(name="bring_to_life", pretty_name="Bring to Life", cost=['2', 'U'],
                   color_identity=['U'], card_type="Sorcery", sub_types="Adventure",
                   abilities=[136488], set_id="ELD", rarity="Uncommon", collectible=False, set_number=38,
                   mtga_id=70477)
ProfaneInsight = Card(name="profane_insight", pretty_name="Profane Insight", cost=['2', 'B'],
                      color_identity=['B'], card_type="Instant", sub_types="Adventure",
                      abilities=[1416], set_id="ELD", rarity="Uncommon", collectible=False, set_number=90,
                      mtga_id=70483)
AlterFate = Card(name="alter_fate", pretty_name="Alter Fate", cost=['1', 'B'],
                 color_identity=['B'], card_type="Sorcery", sub_types="Adventure",
                 abilities=[24122], set_id="ELD", rarity="Uncommon", collectible=False, set_number=99,
                 mtga_id=70485)
CurryFavor = Card(name="curry_favor", pretty_name="Curry Favor", cost=['B'],
                  color_identity=['B'], card_type="Sorcery", sub_types="Adventure",
                  abilities=[136490], set_id="ELD", rarity="Common", collectible=False, set_number=105,
                  mtga_id=70487)
BattleDisplay = Card(name="battle_display", pretty_name="Battle Display", cost=['R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="Adventure",
                     abilities=[22564], set_id="ELD", rarity="Uncommon", collectible=False, set_number=122,
                     mtga_id=70489)
FertileFootsteps = Card(name="fertile_footsteps", pretty_name="Fertile Footsteps", cost=['2', 'G'],
                        color_identity=['G'], card_type="Sorcery", sub_types="Adventure",
                        abilities=[5296], set_id="ELD", rarity="Uncommon", collectible=False, set_number=149,
                        mtga_id=70492)
SeasonalRitual = Card(name="seasonal_ritual", pretty_name="Seasonal Ritual", cost=['G'],
                      color_identity=['G'], card_type="Sorcery", sub_types="Adventure",
                      abilities=[1429], set_id="ELD", rarity="Common", collectible=False, set_number=174,
                      mtga_id=70497)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
ThroneOfEldraine = Set("ThroneOfEldraine", cards=clsmembers)

set_ability_map = {1: 'Deathtouch',
 3: 'Double strike',
 7: 'Flash',
 8: 'Flying',
 9: 'Haste',
 12: 'Lifelink',
 14: 'Trample',
 15: 'Vigilance',
 142: 'Menace',
 197: '{o2}, {oT}, Sacrifice this artifact: You gain 3 life.',
 1027: 'Enchant creature',
 1055: '{oT}: Add one mana of any color.',
 1152: '{oT}: Add {oC}.',
 1156: 'Equip {o3}',
 1268: 'Equip {o1}',
 1316: "Shambling Suit's power is equal to the number of artifacts and/or "
       'enchantments you control.',
 1389: 'When you cast this spell from your hand, copy it if you control an '
       'artifact, then copy it if you control an enchantment. You may choose '
       'new targets for the copies.',
 1392: "{o3}, {oT}: Return target creature you control to its owner's hand.",
 1395: 'Whenever a Knight you control attacks, each opponent loses 1 life and '
       'you gain 1 life.',
 1398: 'Whenever you sacrifice a permanent, put a +1/+1 counter on Korvold and '
       'draw a card.',
 1399: 'Whenever an equipped creature you control attacks, you draw a card and '
       'you lose 1 life.',
 1400: 'Equipment you control have equip Knight {o0}.',
 1416: 'You draw a card and you lose 1 life.',
 1429: 'Add one mana of any color.',
 2374: '{oT}: Add one mana of the chosen color.',
 2512: 'Equipped creature gets +2/+2.',
 4247: '{oT}: Add {oR} or {oW}.',
 5296: 'Search your library for a basic land card, put it onto the '
       'battlefield, then shuffle your library.',
 7610: 'Equipped creature gets +0/+2 and has vigilance.',
 18504: '{oT}: Add {oG} or {oU}.',
 22564: 'Destroy target artifact.',
 24122: 'Return target creature card from your graveyard to your hand.',
 76735: 'Thornwood Falls enters the battlefield tapped.',
 76885: 'Steelbane Hydra enters the battlefield with X +1/+1 counters on it.',
 86476: "Order of Midnight can't block.",
 86788: 'When Golden Egg enters the battlefield, draw a card.',
 88207: '{o1}, {oT}, Sacrifice Golden Egg: Add one mana of any color.',
 88237: 'As Heraldic Banner enters the battlefield, choose a color.',
 88259: "Beanstalk Giant's power and toughness are each equal to the number of "
        'lands you control.',
 90050: 'When Thornwood Falls enters the battlefield, you gain 1 life.',
 90126: "{oT}: Add one mana of any color in your commander's color identity.",
 100685: 'When Witching Well enters the battlefield, scry 2.',
 103355: 'Shinechaser gets +1/+1 as long as you control an artifact.',
 104880: '-3: Destroy target creature. Draw a card.',
 119104: 'Other Knights you control get +1/+1.',
 121999: 'Other creatures you control with flying get +1/+0.',
 136076: 'Whenever another creature dies, or a creature card is put into a '
         'graveyard from anywhere other than the battlefield, or a creature '
         'card leaves your graveyard, Syr Konrad, the Grim deals 1 damage to '
         'each opponent.',
 136077: '{o1oB}: Each player puts the top card of their library into their '
         'graveyard.',
 136079: 'When Venerable Knight dies, put a +1/+1 counter on target Knight you '
         'control.',
 136084: 'When Corridor Monitor enters the battlefield, untap target artifact '
         'or creature you control.',
 136108: 'Whenever you draw your second card each turn, put a +1/+1 counter on '
         'Faerie Vandal.',
 136125: 'Enchanted creature loses all abilities and is a blue Frog creature '
         'with base power and toughness 1/1. \n'
         '<i>(It loses all other card types and creature types.)</i>',
 136126: '0: Create two 2/2 black and green Wolf creature tokens with "When '
         'this creature dies, put a loyalty counter on each Garruk you '
         'control."',
 136128: '-6: You get an emblem with "Creatures you control get +3/+3 and have '
         'trample."',
 136147: 'Sacrifice two Foods: Draw a card.',
 136148: 'Shinechaser gets +1/+1 as long as you control an enchantment.',
 136149: 'Equip Knight {o1}',
 136151: "Wintermoor Commander's toughness is equal to the number of Knights "
         'you control.',
 136152: 'Whenever Wintermoor Commander attacks, another target Knight you '
         'control gains indestructible until end of turn.',
 136153: "When Arcanist's Owl enters the battlefield, look at the top four "
         'cards of your library. You may reveal an artifact or enchantment '
         'card from among them and put it into your hand. Put the rest on the '
         'bottom of your library in a random order.',
 136165: 'When this creature dies, create a Food token.',
 136178: '{oT}, Sacrifice a creature: Create a Food token. If the sacrificed '
         "creature's toughness was 4 or greater, create two Food tokens "
         'instead.',
 136198: '{oT}: Add {oR}, {oW}, or {oB}. Spend this mana only to cast a Knight '
         'or Equipment spell.',
 136216: 'When this creature dies, put a loyalty counter on each Garruk you '
         'control.',
 136218: 'Choose two target creatures controlled by different players. Return '
         "those creatures to their owners' hands.",
 136240: '{o3oU}, Sacrifice Witching Well: Draw two cards.',
 136241: 'When Shining Armor enters the battlefield, attach it to target '
         'Knight you control.',
 136242: 'When this creature enters the battlefield, it deals 1 damage to any '
         'target.',
 136246: 'Destroy target creature. Create a Food token.',
 136248: 'Whenever Belle of the Brawl attacks, other Knights you control get '
         '+1/+0 until end of turn.',
 136251: 'Whenever Savvy Hunter attacks or blocks, create a Food token.',
 136258: 'Whenever one or more non-Human creatures you control deal combat '
         'damage to a player, draw a card.',
 136269: '{o(R/W)o(R/W)o(R/W)o(R/W)}: Fireborn Knight gets +1/+1 until end of '
         'turn.',
 136278: '{o2}, {oT}, Sacrifice Golden Egg: You gain 3 life.',
 136279: 'Creatures you control of the chosen color get +1/+0.',
 136299: 'Equipped creature gets +1/+0 and has haste.',
 136335: 'Enchanted creature gets +1/+1 for each artifact and/or enchantment '
         'you control.',
 136349: 'Equipped creature gets +1/+1 for each charge counter on Mace of the '
         'Valiant and has vigilance.',
 136350: 'Whenever a creature enters the battlefield under your control, put a '
         'charge counter on Mace of the Valiant.',
 136352: 'As long as you control four or more artifacts, Shimmer Dragon has '
         'hexproof.',
 136353: 'Artifact creatures you control have flying.',
 136355: 'Each player sacrifices three creatures. You create three Food '
         'tokens.',
 136357: 'Whenever Thorn Mammoth or another creature enters the battlefield '
         'under your control, Thorn Mammoth fights up to one target creature '
         "you don't control.",
 136359: "Return target nonland permanent to its owner's hand. You create a "
         '2/2 white Knight creature token with vigilance.',
 136361: "{o6oWoB}, Sacrifice Knights' Charge: Return all Knight creature "
         'cards from your graveyard to the battlefield.',
 136362: 'Tome of Legends enters the battlefield with a page counter on it.',
 136363: '{o1}, {oT}, Remove a page counter from Tome of Legends: Draw a card.',
 136364: 'Tap two untapped artifacts you control: Draw a card.',
 136365: 'Whenever Korvold, Fae-Cursed King enters the battlefield or attacks, '
         'sacrifice another permanent.',
 136366: 'At the beginning of combat on your turn, you may have target '
         'noncreature artifact you control become a 0/0 artifact creature. If '
         'you do, put four +1/+1 counters on it.',
 136368: '{o3oU}: Create a 1/1 blue Faerie creature token with flying. Draw a '
         'card.',
 136369: '{o2oG}, Remove a +1/+1 counter from Steelbane Hydra: Destroy target '
         'artifact or enchantment.',
 136371: 'Whenever you cast an artifact or enchantment spell, create a 1/1 '
         'blue Faerie creature token with flying.',
 136372: 'Whenever your commander enters the battlefield or attacks, put a '
         'page counter on Tome of Legends.',
 136373: 'Whenever you cast a creature spell, draw a card, then you may put a '
         'land card from your hand onto the battlefield.',
 136488: 'Target noncreature artifact you control becomes a 0/0 artifact '
         'creature. Put four +1/+1 counters on it.',
 136490: 'You gain X life and each opponent loses X life, where X is the '
         'number of Knights you control.'}
