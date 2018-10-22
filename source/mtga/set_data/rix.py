
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


BafflingEnd = Card(name="baffling_end", pretty_name="Baffling End", cost=['1', 'W'],
                   color_identity=['W'], card_type="Enchantment", sub_types="",
                   abilities=[117140, 117141], set_id="RIX", rarity="Uncommon", set_number=1,
                   mtga_id=66619)
BishopofBinding = Card(name="bishop_of_binding", pretty_name="Bishop of Binding", cost=['3', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Vampire Cleric",
                       abilities=[20262, 1009], set_id="RIX", rarity="Rare", set_number=2,
                       mtga_id=66621)
BlazingHope = Card(name="blazing_hope", pretty_name="Blazing Hope", cost=['W'],
                   color_identity=['W'], card_type="Instant", sub_types="",
                   abilities=[117143], set_id="RIX", rarity="Uncommon", set_number=3,
                   mtga_id=66623)
CleansingRay = Card(name="cleansing_ray", pretty_name="Cleansing Ray", cost=['1', 'W'],
                    color_identity=['W'], card_type="Sorcery", sub_types="",
                    abilities=[1013], set_id="RIX", rarity="Common", set_number=4,
                    mtga_id=66625)
DivineVerdict = Card(name="divine_verdict", pretty_name="Divine Verdict", cost=['3', 'W'],
                     color_identity=['W'], card_type="Instant", sub_types="",
                     abilities=[2732], set_id="RIX", rarity="Common", set_number=5,
                     mtga_id=66627)
EverdawnChampion = Card(name="everdawn_champion", pretty_name="Everdawn Champion", cost=['1', 'W', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                        abilities=[90077], set_id="RIX", rarity="Uncommon", set_number=6,
                        mtga_id=66629)
ExultantSkymarcher = Card(name="exultant_skymarcher", pretty_name="Exultant Skymarcher", cost=['1', 'W', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                          abilities=[8], set_id="RIX", rarity="Common", set_number=7,
                          mtga_id=66631)
FamishedPaladin = Card(name="famished_paladin", pretty_name="Famished Paladin", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Vampire Knight",
                       abilities=[86621, 117146], set_id="RIX", rarity="Uncommon", set_number=8,
                       mtga_id=66633)
ForerunneroftheLegion = Card(name="forerunner_of_the_legion", pretty_name="Forerunner of the Legion", cost=['2', 'W'],
                             color_identity=['W'], card_type="Creature", sub_types="Vampire Knight",
                             abilities=[117147, 117148], set_id="RIX", rarity="Uncommon", set_number=9,
                             mtga_id=66635)
ImperialCeratops = Card(name="imperial_ceratops", pretty_name="Imperial Ceratops", cost=['4', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[1229], set_id="RIX", rarity="Uncommon", set_number=10,
                        mtga_id=66637)
LegionConquistador = Card(name="legion_conquistador", pretty_name="Legion Conquistador", cost=['2', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                          abilities=[116758], set_id="RIX", rarity="Common", set_number=11,
                          mtga_id=66639)
LuminousBonds = Card(name="luminous_bonds", pretty_name="Luminous Bonds", cost=['2', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 1083], set_id="RIX", rarity="Common", set_number=12,
                     mtga_id=66641)
MajesticHeliopterus = Card(name="majestic_heliopterus", pretty_name="Majestic Heliopterus", cost=['3', 'W'],
                           color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[8, 116971], set_id="RIX", rarity="Uncommon", set_number=13,
                           mtga_id=66643)
MartyrofDusk = Card(name="martyr_of_dusk", pretty_name="Martyr of Dusk", cost=['1', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                    abilities=[117061], set_id="RIX", rarity="Common", set_number=14,
                    mtga_id=66645)
MomentofTriumph = Card(name="moment_of_triumph", pretty_name="Moment of Triumph", cost=['W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[116975], set_id="RIX", rarity="Common", set_number=15,
                       mtga_id=66647)
PaladinofAtonement = Card(name="paladin_of_atonement", pretty_name="Paladin of Atonement", cost=['1', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Vampire Knight",
                          abilities=[116974, 116996], set_id="RIX", rarity="Rare", set_number=16,
                          mtga_id=66649)
PrideofConquerors = Card(name="pride_of_conquerors", pretty_name="Pride of Conquerors", cost=['1', 'W'],
                         color_identity=['W'], card_type="Instant", sub_types="",
                         abilities=[165, 117033], set_id="RIX", rarity="Uncommon", set_number=17,
                         mtga_id=66651)
RadiantDestiny = Card(name="radiant_destiny", pretty_name="Radiant Destiny", cost=['2', 'W'],
                      color_identity=['W'], card_type="Enchantment", sub_types="",
                      abilities=[165, 76882, 117051], set_id="RIX", rarity="Rare", set_number=18,
                      mtga_id=66653)
RaptorCompanion = Card(name="raptor_companion", pretty_name="Raptor Companion", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[], set_id="RIX", rarity="Common", set_number=19,
                       mtga_id=66655)
SanguineGlorifier = Card(name="sanguine_glorifier", pretty_name="Sanguine Glorifier", cost=['3', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Vampire Cleric",
                         abilities=[102891], set_id="RIX", rarity="Common", set_number=20,
                         mtga_id=66657)
SkymarcherAspirant = Card(name="skymarcher_aspirant", pretty_name="Skymarcher Aspirant", cost=['W'],
                          color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                          abilities=[165, 117060], set_id="RIX", rarity="Uncommon", set_number=21,
                          mtga_id=66659)
SlaughtertheStrong = Card(name="slaughter_the_strong", pretty_name="Slaughter the Strong", cost=['1', 'W', 'W'],
                          color_identity=['W'], card_type="Sorcery", sub_types="",
                          abilities=[117065], set_id="RIX", rarity="Rare", set_number=22,
                          mtga_id=66661)
SnubhornSentry = Card(name="snubhorn_sentry", pretty_name="Snubhorn Sentry", cost=['W'],
                      color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                      abilities=[165, 1036], set_id="RIX", rarity="Common", set_number=23,
                      mtga_id=66663)
SphinxsDecree = Card(name="sphinxs_decree", pretty_name="Sphinx's Decree", cost=['1', 'W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[117077], set_id="RIX", rarity="Rare", set_number=24,
                     mtga_id=66665)
SquiresDevotion = Card(name="squires_devotion", pretty_name="Squire's Devotion", cost=['2', 'W'],
                       color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                       abilities=[1027, 20631, 116788], set_id="RIX", rarity="Common", set_number=25,
                       mtga_id=66667)
SunSentinel = Card(name="sun_sentinel", pretty_name="Sun Sentinel", cost=['1', 'W'],
                   color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                   abilities=[15], set_id="RIX", rarity="Common", set_number=26,
                   mtga_id=66669)
SunCrestedPterodon = Card(name="suncrested_pterodon", pretty_name="Sun-Crested Pterodon", cost=['4', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                          abilities=[8, 117093], set_id="RIX", rarity="Common", set_number=27,
                          mtga_id=66671)
TempleAltisaur = Card(name="temple_altisaur", pretty_name="Temple Altisaur", cost=['4', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                      abilities=[116972], set_id="RIX", rarity="Rare", set_number=28,
                      mtga_id=66673)
TrapjawTyrant = Card(name="trapjaw_tyrant", pretty_name="Trapjaw Tyrant", cost=['3', 'W', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                     abilities=[116973], set_id="RIX", rarity="Mythic Rare", set_number=29,
                     mtga_id=66675)
ZetalpaPrimalDawn = Card(name="zetalpa_primal_dawn", pretty_name="Zetalpa, Primal Dawn", cost=['6', 'W', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Elder Dinosaur",
                         abilities=[8, 3, 15, 14, 104], set_id="RIX", rarity="Rare", set_number=30,
                         mtga_id=66677)
AdmiralsOrder = Card(name="admirals_order", pretty_name="Admiral's Order", cost=['1', 'U', 'U'],
                     color_identity=['U'], card_type="Instant", sub_types="",
                     abilities=[116984, 25846], set_id="RIX", rarity="Rare", set_number=31,
                     mtga_id=66679)
AquaticIncursion = Card(name="aquatic_incursion", pretty_name="Aquatic Incursion", cost=['3', 'U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="",
                        abilities=[117110, 116991], set_id="RIX", rarity="Uncommon", set_number=32,
                        mtga_id=66681)
CraftyCutpurse = Card(name="crafty_cutpurse", pretty_name="Crafty Cutpurse", cost=['3', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                      abilities=[7, 116993], set_id="RIX", rarity="Rare", set_number=33,
                      mtga_id=66683)
CrashingTide = Card(name="crashing_tide", pretty_name="Crashing Tide", cost=['2', 'U'],
                    color_identity=['U'], card_type="Sorcery", sub_types="",
                    abilities=[1048, 22505, 25848], set_id="RIX", rarity="Common", set_number=34,
                    mtga_id=66685)
CuriousObsession = Card(name="curious_obsession", pretty_name="Curious Obsession", cost=['U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 117125, 116998], set_id="RIX", rarity="Uncommon", set_number=35,
                        mtga_id=66687)
DeadeyeRigHauler = Card(name="deadeye_righauler", pretty_name="Deadeye Rig-Hauler", cost=['3', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                        abilities=[117003], set_id="RIX", rarity="Common", set_number=36,
                        mtga_id=66689)
ExpelfromOrazca = Card(name="expel_from_orazca", pretty_name="Expel from Orazca", cost=['1', 'U'],
                       color_identity=['U'], card_type="Instant", sub_types="",
                       abilities=[165, 117009], set_id="RIX", rarity="Uncommon", set_number=37,
                       mtga_id=66691)
FloodofRecollection = Card(name="flood_of_recollection", pretty_name="Flood of Recollection", cost=['U', 'U'],
                           color_identity=['U'], card_type="Sorcery", sub_types="",
                           abilities=[1056], set_id="RIX", rarity="Uncommon", set_number=38,
                           mtga_id=66693)
Hornswoggle = Card(name="hornswoggle", pretty_name="Hornswoggle", cost=['2', 'U'],
                   color_identity=['U'], card_type="Instant", sub_types="",
                   abilities=[117023], set_id="RIX", rarity="Uncommon", set_number=39,
                   mtga_id=66695)
InducedAmnesia = Card(name="induced_amnesia", pretty_name="Induced Amnesia", cost=['2', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="",
                      abilities=[117029, 117032], set_id="RIX", rarity="Rare", set_number=40,
                      mtga_id=66697)
KitesailCorsair = Card(name="kitesail_corsair", pretty_name="Kitesail Corsair", cost=['1', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                       abilities=[117036], set_id="RIX", rarity="Common", set_number=41,
                       mtga_id=66699)
KumenasAwakening = Card(name="kumenas_awakening", pretty_name="Kumena's Awakening", cost=['2', 'U', 'U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="",
                        abilities=[165, 1062], set_id="RIX", rarity="Rare", set_number=42,
                        mtga_id=66701)
MistCloakedHerald = Card(name="mistcloaked_herald", pretty_name="Mist-Cloaked Herald", cost=['U'],
                         color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                         abilities=[62969], set_id="RIX", rarity="Common", set_number=43,
                         mtga_id=66703)
Negate = Card(name="negate", pretty_name="Negate", cost=['1', 'U'],
              color_identity=['U'], card_type="Instant", sub_types="",
              abilities=[1142], set_id="RIX", rarity="Common", set_number=44,
              mtga_id=66705)
NezahalPrimalTide = Card(name="nezahal_primal_tide", pretty_name="Nezahal, Primal Tide", cost=['5', 'U', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Elder Dinosaur",
                         abilities=[120421, 1640, 117046, 117047], set_id="RIX", rarity="Rare", set_number=45,
                         mtga_id=66707)
ReleasetotheWind = Card(name="release_to_the_wind", pretty_name="Release to the Wind", cost=['2', 'U'],
                        color_identity=['U'], card_type="Instant", sub_types="",
                        abilities=[117049], set_id="RIX", rarity="Rare", set_number=46,
                        mtga_id=66709)
RiverDarter = Card(name="river_darter", pretty_name="River Darter", cost=['2', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                   abilities=[117050], set_id="RIX", rarity="Common", set_number=47,
                   mtga_id=66711)
RiverwiseAugur = Card(name="riverwise_augur", pretty_name="Riverwise Augur", cost=['3', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                      abilities=[117053], set_id="RIX", rarity="Uncommon", set_number=48,
                      mtga_id=66713)
SailorofMeans = Card(name="sailor_of_means", pretty_name="Sailor of Means", cost=['2', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                     abilities=[116826], set_id="RIX", rarity="Common", set_number=49,
                     mtga_id=66715)
SeaLegs = Card(name="sea_legs", pretty_name="Sea Legs", cost=['U'],
               color_identity=['U'], card_type="Enchantment", sub_types="Aura",
               abilities=[7, 1027, 117055], set_id="RIX", rarity="Common", set_number=50,
               mtga_id=66717)
SeafloorOracle = Card(name="seafloor_oracle", pretty_name="Seafloor Oracle", cost=['2', 'U', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                      abilities=[117056], set_id="RIX", rarity="Rare", set_number=51,
                      mtga_id=66719)
SecretsoftheGoldenCity = Card(name="secrets_of_the_golden_city", pretty_name="Secrets of the Golden City", cost=['1', 'U', 'U'],
                              color_identity=['U'], card_type="Sorcery", sub_types="",
                              abilities=[165, 117057], set_id="RIX", rarity="Common", set_number=52,
                              mtga_id=66721)
SilvergillAdept = Card(name="silvergill_adept", pretty_name="Silvergill Adept", cost=['1', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                       abilities=[92582, 86788], set_id="RIX", rarity="Uncommon", set_number=53,
                       mtga_id=66723)
SirenReaver = Card(name="siren_reaver", pretty_name="Siren Reaver", cost=['3', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Siren Pirate",
                   abilities=[121046, 8], set_id="RIX", rarity="Uncommon", set_number=54,
                   mtga_id=66725)
SlipperyScoundrel = Card(name="slippery_scoundrel", pretty_name="Slippery Scoundrel", cost=['2', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[165, 117059], set_id="RIX", rarity="Uncommon", set_number=55,
                         mtga_id=66727)
SouloftheRapids = Card(name="soul_of_the_rapids", pretty_name="Soul of the Rapids", cost=['3', 'U', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Elemental",
                       abilities=[8, 10], set_id="RIX", rarity="Common", set_number=56,
                       mtga_id=66729)
SpireWinder = Card(name="spire_winder", pretty_name="Spire Winder", cost=['3', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Snake",
                   abilities=[8, 165, 1080], set_id="RIX", rarity="Common", set_number=57,
                   mtga_id=66731)
SwornGuardian = Card(name="sworn_guardian", pretty_name="Sworn Guardian", cost=['1', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                     abilities=[], set_id="RIX", rarity="Common", set_number=58,
                     mtga_id=66733)
TimestreamNavigator = Card(name="timestream_navigator", pretty_name="Timestream Navigator", cost=['1', 'U'],
                           color_identity=['U'], card_type="Creature", sub_types="Human Pirate Wizard",
                           abilities=[165, 117062], set_id="RIX", rarity="Mythic Rare", set_number=59,
                           mtga_id=66735)
WarkiteMarauder = Card(name="warkite_marauder", pretty_name="Warkite Marauder", cost=['1', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                       abilities=[8, 117063], set_id="RIX", rarity="Rare", set_number=60,
                       mtga_id=66737)
Waterknot = Card(name="waterknot", pretty_name="Waterknot", cost=['1', 'U', 'U'],
                 color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                 abilities=[1027, 89789, 88178], set_id="RIX", rarity="Common", set_number=61,
                 mtga_id=66739)
ArterialFlow = Card(name="arterial_flow", pretty_name="Arterial Flow", cost=['1', 'B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[117064], set_id="RIX", rarity="Uncommon", set_number=62,
                    mtga_id=66741)
CanalMonitor = Card(name="canal_monitor", pretty_name="Canal Monitor", cost=['4', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Lizard",
                    abilities=[], set_id="RIX", rarity="Common", set_number=63,
                    mtga_id=66743)
ChampionofDusk = Card(name="champion_of_dusk", pretty_name="Champion of Dusk", cost=['3', 'B', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Vampire Knight",
                      abilities=[117066], set_id="RIX", rarity="Rare", set_number=64,
                      mtga_id=66745)
DarkInquiry = Card(name="dark_inquiry", pretty_name="Dark Inquiry", cost=['2', 'B'],
                   color_identity=['B'], card_type="Sorcery", sub_types="",
                   abilities=[117067], set_id="RIX", rarity="Common", set_number=65,
                   mtga_id=66747)
DeadMansChest = Card(name="dead_mans_chest", pretty_name="Dead Man's Chest", cost=['1', 'B'],
                     color_identity=['B'], card_type="Enchantment", sub_types="Aura",
                     abilities=[14018, 117069], set_id="RIX", rarity="Rare", set_number=66,
                     mtga_id=66749)
DinosaurHunter = Card(name="dinosaur_hunter", pretty_name="Dinosaur Hunter", cost=['1', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                      abilities=[117070], set_id="RIX", rarity="Common", set_number=67,
                      mtga_id=66751)
DireFleetPoisoner = Card(name="dire_fleet_poisoner", pretty_name="Dire Fleet Poisoner", cost=['1', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[7, 1, 117071], set_id="RIX", rarity="Rare", set_number=68,
                         mtga_id=66753)
DuskCharger = Card(name="dusk_charger", pretty_name="Dusk Charger", cost=['3', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Horse",
                   abilities=[165, 117072], set_id="RIX", rarity="Common", set_number=69,
                   mtga_id=66755)
DuskLegionZealot = Card(name="dusk_legion_zealot", pretty_name="Dusk Legion Zealot", cost=['1', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                        abilities=[88159], set_id="RIX", rarity="Common", set_number=70,
                        mtga_id=66757)
FathomFleetBoarder = Card(name="fathom_fleet_boarder", pretty_name="Fathom Fleet Boarder", cost=['2', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Orc Pirate",
                          abilities=[117074], set_id="RIX", rarity="Common", set_number=71,
                          mtga_id=66759)
ForerunneroftheCoalition = Card(name="forerunner_of_the_coalition", pretty_name="Forerunner of the Coalition", cost=['2', 'B'],
                                color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                                abilities=[117076, 117078], set_id="RIX", rarity="Uncommon", set_number=72,
                                mtga_id=66761)
GoldenDemise = Card(name="golden_demise", pretty_name="Golden Demise", cost=['1', 'B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[165, 117080], set_id="RIX", rarity="Uncommon", set_number=73,
                    mtga_id=66763)
GraspingScoundrel = Card(name="grasping_scoundrel", pretty_name="Grasping Scoundrel", cost=['B'],
                         color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[117081], set_id="RIX", rarity="Common", set_number=74,
                         mtga_id=66765)
GruesomeFate = Card(name="gruesome_fate", pretty_name="Gruesome Fate", cost=['2', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[1099], set_id="RIX", rarity="Common", set_number=75,
                    mtga_id=66767)
Impale = Card(name="impale", pretty_name="Impale", cost=['2', 'B', 'B'],
              color_identity=['B'], card_type="Sorcery", sub_types="",
              abilities=[26818], set_id="RIX", rarity="Common", set_number=76,
              mtga_id=66769)
MastermindsAcquisition = Card(name="masterminds_acquisition", pretty_name="Mastermind's Acquisition", cost=['2', 'B', 'B'],
                              color_identity=['B'], card_type="Sorcery", sub_types="",
                              abilities=[117087], set_id="RIX", rarity="Rare", set_number=77,
                              mtga_id=66771)
MausoleumHarpy = Card(name="mausoleum_harpy", pretty_name="Mausoleum Harpy", cost=['4', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Harpy",
                      abilities=[8, 165, 117088], set_id="RIX", rarity="Uncommon", set_number=78,
                      mtga_id=66773)
MomentofCraving = Card(name="moment_of_craving", pretty_name="Moment of Craving", cost=['1', 'B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[117089], set_id="RIX", rarity="Common", set_number=79,
                       mtga_id=66775)
OathswornVampire = Card(name="oathsworn_vampire", pretty_name="Oathsworn Vampire", cost=['1', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Vampire Knight",
                        abilities=[76735, 117090], set_id="RIX", rarity="Uncommon", set_number=80,
                        mtga_id=66777)
PitilessPlunderer = Card(name="pitiless_plunderer", pretty_name="Pitiless Plunderer", cost=['3', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[117091], set_id="RIX", rarity="Uncommon", set_number=81,
                         mtga_id=66779)
RavenousChupacabra = Card(name="ravenous_chupacabra", pretty_name="Ravenous Chupacabra", cost=['2', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Beast Horror",
                          abilities=[117092], set_id="RIX", rarity="Uncommon", set_number=82,
                          mtga_id=66781)
ReaverAmbush = Card(name="reaver_ambush", pretty_name="Reaver Ambush", cost=['2', 'B'],
                    color_identity=['B'], card_type="Instant", sub_types="",
                    abilities=[62243], set_id="RIX", rarity="Uncommon", set_number=83,
                    mtga_id=66783)
Recover = Card(name="recover", pretty_name="Recover", cost=['2', 'B'],
               color_identity=['B'], card_type="Sorcery", sub_types="",
               abilities=[24122, 25848], set_id="RIX", rarity="Common", set_number=84,
               mtga_id=66785)
SadisticSkymarcher = Card(name="sadistic_skymarcher", pretty_name="Sadistic Skymarcher", cost=['2', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                          abilities=[117094, 8, 12], set_id="RIX", rarity="Uncommon", set_number=85,
                          mtga_id=66787)
TetzimocPrimalDeath = Card(name="tetzimoc_primal_death", pretty_name="Tetzimoc, Primal Death", cost=['4', 'B', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Elder Dinosaur",
                           abilities=[1, 117096, 117097], set_id="RIX", rarity="Rare", set_number=86,
                           mtga_id=66789)
TombRobber = Card(name="tomb_robber", pretty_name="Tomb Robber", cost=['2', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                  abilities=[142, 117098], set_id="RIX", rarity="Rare", set_number=87,
                  mtga_id=66791)
TwilightProphet = Card(name="twilight_prophet", pretty_name="Twilight Prophet", cost=['2', 'B', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Vampire Cleric",
                       abilities=[8, 165, 117099], set_id="RIX", rarity="Mythic Rare", set_number=88,
                       mtga_id=66793)
VampireRevenant = Card(name="vampire_revenant", pretty_name="Vampire Revenant", cost=['3', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Vampire Spirit",
                       abilities=[8], set_id="RIX", rarity="Common", set_number=89,
                       mtga_id=66795)
VonasHunger = Card(name="vonas_hunger", pretty_name="Vona's Hunger", cost=['2', 'B'],
                   color_identity=['B'], card_type="Instant", sub_types="",
                   abilities=[165, 1117], set_id="RIX", rarity="Rare", set_number=90,
                   mtga_id=66797)
VoraciousVampire = Card(name="voracious_vampire", pretty_name="Voracious Vampire", cost=['2', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Vampire Knight",
                        abilities=[142, 117101], set_id="RIX", rarity="Common", set_number=91,
                        mtga_id=66799)
BloodSun = Card(name="blood_sun", pretty_name="Blood Sun", cost=['2', 'R'],
                color_identity=['R'], card_type="Enchantment", sub_types="",
                abilities=[86788, 117102], set_id="RIX", rarity="Rare", set_number=92,
                mtga_id=66801)
Bombard = Card(name="bombard", pretty_name="Bombard", cost=['2', 'R'],
               color_identity=['R'], card_type="Instant", sub_types="",
               abilities=[21773], set_id="RIX", rarity="Common", set_number=93,
               mtga_id=66803)
BrasssBounty = Card(name="brasss_bounty", pretty_name="Brass's Bounty", cost=['6', 'R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[117103], set_id="RIX", rarity="Rare", set_number=94,
                    mtga_id=66805)
BrazenFreebooter = Card(name="brazen_freebooter", pretty_name="Brazen Freebooter", cost=['3', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                        abilities=[116826], set_id="RIX", rarity="Common", set_number=95,
                        mtga_id=66807)
BuccaneersBravado = Card(name="buccaneers_bravado", pretty_name="Buccaneer's Bravado", cost=['1', 'R'],
                         color_identity=['R'], card_type="Instant", sub_types="",
                         abilities=[117105], set_id="RIX", rarity="Common", set_number=96,
                         mtga_id=66809)
ChargingTuskodon = Card(name="charging_tuskodon", pretty_name="Charging Tuskodon", cost=['3', 'R', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[14, 1125], set_id="RIX", rarity="Uncommon", set_number=97,
                        mtga_id=66811)
DaringBuccaneer = Card(name="daring_buccaneer", pretty_name="Daring Buccaneer", cost=['R'],
                       color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                       abilities=[117106], set_id="RIX", rarity="Uncommon", set_number=98,
                       mtga_id=66813)
DireFleetDaredevil = Card(name="dire_fleet_daredevil", pretty_name="Dire Fleet Daredevil", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                          abilities=[6, 117107], set_id="RIX", rarity="Rare", set_number=99,
                          mtga_id=66815)
EtaliPrimalStorm = Card(name="etali_primal_storm", pretty_name="Etali, Primal Storm", cost=['4', 'R', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Elder Dinosaur",
                        abilities=[117108], set_id="RIX", rarity="Rare", set_number=100,
                        mtga_id=66817)
FanaticalFirebrand = Card(name="fanatical_firebrand", pretty_name="Fanatical Firebrand", cost=['R'],
                          color_identity=['R'], card_type="Creature", sub_types="Goblin Pirate",
                          abilities=[9, 117109], set_id="RIX", rarity="Common", set_number=101,
                          mtga_id=66819)
ForerunneroftheEmpire = Card(name="forerunner_of_the_empire", pretty_name="Forerunner of the Empire", cost=['3', 'R'],
                             color_identity=['R'], card_type="Creature", sub_types="Human Soldier",
                             abilities=[116976, 116977], set_id="RIX", rarity="Uncommon", set_number=102,
                             mtga_id=66821)
FormoftheDinosaur = Card(name="form_of_the_dinosaur", pretty_name="Form of the Dinosaur", cost=['4', 'R', 'R'],
                         color_identity=['R'], card_type="Enchantment", sub_types="",
                         abilities=[116978, 116979], set_id="RIX", rarity="Rare", set_number=103,
                         mtga_id=66823)
FrilledDeathspitter = Card(name="frilled_deathspitter", pretty_name="Frilled Deathspitter", cost=['2', 'R'],
                           color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[119063], set_id="RIX", rarity="Common", set_number=104,
                           mtga_id=66825)
GoblinTrailblazer = Card(name="goblin_trailblazer", pretty_name="Goblin Trailblazer", cost=['1', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin Pirate",
                         abilities=[142], set_id="RIX", rarity="Common", set_number=105,
                         mtga_id=66827)
Mutiny = Card(name="mutiny", pretty_name="Mutiny", cost=['R'],
              color_identity=['R'], card_type="Sorcery", sub_types="",
              abilities=[116981], set_id="RIX", rarity="Common", set_number=106,
              mtga_id=66829)
NeedletoothRaptor = Card(name="needletooth_raptor", pretty_name="Needletooth Raptor", cost=['3', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[116982], set_id="RIX", rarity="Uncommon", set_number=107,
                         mtga_id=66831)
OrazcaRaptor = Card(name="orazca_raptor", pretty_name="Orazca Raptor", cost=['2', 'R', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                    abilities=[], set_id="RIX", rarity="Common", set_number=108,
                    mtga_id=66833)
PiratesPillage = Card(name="pirates_pillage", pretty_name="Pirate's Pillage", cost=['3', 'R'],
                      color_identity=['R'], card_type="Sorcery", sub_types="",
                      abilities=[87929, 116983], set_id="RIX", rarity="Uncommon", set_number=109,
                      mtga_id=66835)
RecklessRage = Card(name="reckless_rage", pretty_name="Reckless Rage", cost=['R'],
                    color_identity=['R'], card_type="Instant", sub_types="",
                    abilities=[117111], set_id="RIX", rarity="Uncommon", set_number=110,
                    mtga_id=66837)
RekindlingPhoenix = Card(name="rekindling_phoenix", pretty_name="Rekindling Phoenix", cost=['2', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Phoenix",
                         abilities=[8, 116986], set_id="RIX", rarity="Mythic Rare", set_number=111,
                         mtga_id=66839)
SeeRed = Card(name="see_red", pretty_name="See Red", cost=['1', 'R'],
              color_identity=['R'], card_type="Enchantment", sub_types="Aura",
              abilities=[1027, 116987, 116998], set_id="RIX", rarity="Uncommon", set_number=112,
              mtga_id=66841)
ShaketheFoundations = Card(name="shake_the_foundations", pretty_name="Shake the Foundations", cost=['2', 'R'],
                           color_identity=['R'], card_type="Instant", sub_types="",
                           abilities=[88622, 25848], set_id="RIX", rarity="Uncommon", set_number=113,
                           mtga_id=66843)
Shatter = Card(name="shatter", pretty_name="Shatter", cost=['1', 'R'],
               color_identity=['R'], card_type="Instant", sub_types="",
               abilities=[22564], set_id="RIX", rarity="Common", set_number=114,
               mtga_id=66845)
SilvercladFerocidons = Card(name="silverclad_ferocidons", pretty_name="Silverclad Ferocidons", cost=['5', 'R', 'R'],
                            color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                            abilities=[116988], set_id="RIX", rarity="Rare", set_number=115,
                            mtga_id=66847)
StampedingHorncrest = Card(name="stampeding_horncrest", pretty_name="Stampeding Horncrest", cost=['4', 'R'],
                           color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[117113], set_id="RIX", rarity="Common", set_number=116,
                           mtga_id=66849)
StormFleetSwashbuckler = Card(name="storm_fleet_swashbuckler", pretty_name="Storm Fleet Swashbuckler", cost=['1', 'R'],
                              color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                              abilities=[165, 117114], set_id="RIX", rarity="Uncommon", set_number=117,
                              mtga_id=66851)
SunCollaredRaptor = Card(name="suncollared_raptor", pretty_name="Sun-Collared Raptor", cost=['1', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[14, 117115], set_id="RIX", rarity="Common", set_number=118,
                         mtga_id=66853)
SwaggeringCorsair = Card(name="swaggering_corsair", pretty_name="Swaggering Corsair", cost=['2', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[101552], set_id="RIX", rarity="Common", set_number=119,
                         mtga_id=66855)
TilonallisCrown = Card(name="tilonallis_crown", pretty_name="Tilonalli's Crown", cost=['1', 'R'],
                       color_identity=['R'], card_type="Enchantment", sub_types="Aura",
                       abilities=[1027, 1150, 117116], set_id="RIX", rarity="Common", set_number=120,
                       mtga_id=66857)
TilonallisSummoner = Card(name="tilonallis_summoner", pretty_name="Tilonalli's Summoner", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Human Shaman",
                          abilities=[165, 117117], set_id="RIX", rarity="Rare", set_number=121,
                          mtga_id=66859)
AggressiveUrge = Card(name="aggressive_urge", pretty_name="Aggressive Urge", cost=['1', 'G'],
                      color_identity=['G'], card_type="Instant", sub_types="",
                      abilities=[6906, 25848], set_id="RIX", rarity="Common", set_number=122,
                      mtga_id=66861)
Cacophodon = Card(name="cacophodon", pretty_name="Cacophodon", cost=['3', 'G'],
                  color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                  abilities=[117118], set_id="RIX", rarity="Uncommon", set_number=123,
                  mtga_id=66863)
CherishedHatchling = Card(name="cherished_hatchling", pretty_name="Cherished Hatchling", cost=['1', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                          abilities=[116990], set_id="RIX", rarity="Uncommon", set_number=124,
                          mtga_id=66865)
ColossalDreadmaw = Card(name="colossal_dreadmaw", pretty_name="Colossal Dreadmaw", cost=['4', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[14], set_id="RIX", rarity="Common", set_number=125,
                        mtga_id=66867)
CrestedHerdcaller = Card(name="crested_herdcaller", pretty_name="Crested Herdcaller", cost=['3', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[14, 116783], set_id="RIX", rarity="Uncommon", set_number=126,
                         mtga_id=66869)
DeeprootElite = Card(name="deeproot_elite", pretty_name="Deeproot Elite", cost=['1', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Merfolk Warrior",
                     abilities=[117119], set_id="RIX", rarity="Rare", set_number=127,
                     mtga_id=66871)
EntertheUnknown = Card(name="enter_the_unknown", pretty_name="Enter the Unknown", cost=['G'],
                       color_identity=['G'], card_type="Sorcery", sub_types="",
                       abilities=[117120, 6426], set_id="RIX", rarity="Uncommon", set_number=128,
                       mtga_id=66873)
ForerunneroftheHeralds = Card(name="forerunner_of_the_heralds", pretty_name="Forerunner of the Heralds", cost=['3', 'G'],
                              color_identity=['G'], card_type="Creature", sub_types="Merfolk Scout",
                              abilities=[92594, 116992], set_id="RIX", rarity="Uncommon", set_number=129,
                              mtga_id=66875)
GhaltaPrimalHunger = Card(name="ghalta_primal_hunger", pretty_name="Ghalta, Primal Hunger", cost=['10', 'G', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Elder Dinosaur",
                          abilities=[117121, 14], set_id="RIX", rarity="Rare", set_number=130,
                          mtga_id=66877)
GiltgroveStalker = Card(name="giltgrove_stalker", pretty_name="Giltgrove Stalker", cost=['1', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Merfolk Warrior",
                        abilities=[87941], set_id="RIX", rarity="Common", set_number=131,
                        mtga_id=66879)
HardyVeteran = Card(name="hardy_veteran", pretty_name="Hardy Veteran", cost=['1', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Human Warrior",
                    abilities=[116994], set_id="RIX", rarity="Common", set_number=132,
                    mtga_id=66881)
HunttheWeak = Card(name="hunt_the_weak", pretty_name="Hunt the Weak", cost=['3', 'G'],
                   color_identity=['G'], card_type="Sorcery", sub_types="",
                   abilities=[20207], set_id="RIX", rarity="Common", set_number=133,
                   mtga_id=66883)
JadeBearer = Card(name="jade_bearer", pretty_name="Jade Bearer", cost=['G'],
                  color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                  abilities=[117122], set_id="RIX", rarity="Common", set_number=134,
                  mtga_id=66885)
JadecraftArtisan = Card(name="jadecraft_artisan", pretty_name="Jadecraft Artisan", cost=['3', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                        abilities=[99593], set_id="RIX", rarity="Common", set_number=135,
                        mtga_id=66887)
JadelightRanger = Card(name="jadelight_ranger", pretty_name="Jadelight Ranger", cost=['1', 'G', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Merfolk Scout",
                       abilities=[117124], set_id="RIX", rarity="Rare", set_number=136,
                       mtga_id=66889)
JunglebornPioneer = Card(name="jungleborn_pioneer", pretty_name="Jungleborn Pioneer", cost=['2', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Merfolk Scout",
                         abilities=[116995], set_id="RIX", rarity="Common", set_number=137,
                         mtga_id=66891)
KnightoftheStampede = Card(name="knight_of_the_stampede", pretty_name="Knight of the Stampede", cost=['3', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Human Knight",
                           abilities=[117126], set_id="RIX", rarity="Common", set_number=138,
                           mtga_id=66893)
Naturalize = Card(name="naturalize", pretty_name="Naturalize", cost=['1', 'G'],
                  color_identity=['G'], card_type="Instant", sub_types="",
                  abilities=[120290], set_id="RIX", rarity="Common", set_number=139,
                  mtga_id=66895)
OrazcaFrillback = Card(name="orazca_frillback", pretty_name="Orazca Frillback", cost=['2', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[], set_id="RIX", rarity="Common", set_number=140,
                       mtga_id=66897)
OvergrownArmasaur = Card(name="overgrown_armasaur", pretty_name="Overgrown Armasaur", cost=['3', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[117128], set_id="RIX", rarity="Common", set_number=141,
                         mtga_id=66899)
PathofDiscovery = Card(name="path_of_discovery", pretty_name="Path of Discovery", cost=['3', 'G'],
                       color_identity=['G'], card_type="Enchantment", sub_types="",
                       abilities=[117082], set_id="RIX", rarity="Rare", set_number=142,
                       mtga_id=66901)
Plummet = Card(name="plummet", pretty_name="Plummet", cost=['1', 'G'],
               color_identity=['G'], card_type="Instant", sub_types="",
               abilities=[29759], set_id="RIX", rarity="Common", set_number=143,
               mtga_id=66903)
Polyraptor = Card(name="polyraptor", pretty_name="Polyraptor", cost=['6', 'G', 'G'],
                  color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                  abilities=[117129], set_id="RIX", rarity="Mythic Rare", set_number=144,
                  mtga_id=66905)
StrengthofthePack = Card(name="strength_of_the_pack", pretty_name="Strength of the Pack", cost=['4', 'G', 'G'],
                         color_identity=['G'], card_type="Sorcery", sub_types="",
                         abilities=[117130], set_id="RIX", rarity="Uncommon", set_number=145,
                         mtga_id=66907)
SwiftWarden = Card(name="swift_warden", pretty_name="Swift Warden", cost=['1', 'G', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Merfolk Warrior",
                   abilities=[7, 117131], set_id="RIX", rarity="Uncommon", set_number=146,
                   mtga_id=66909)
TendershootDryad = Card(name="tendershoot_dryad", pretty_name="Tendershoot Dryad", cost=['4', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dryad",
                        abilities=[165, 2640, 117132], set_id="RIX", rarity="Rare", set_number=147,
                        mtga_id=66911)
ThrashingBrontodon = Card(name="thrashing_brontodon", pretty_name="Thrashing Brontodon", cost=['1', 'G', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                          abilities=[89285], set_id="RIX", rarity="Uncommon", set_number=148,
                          mtga_id=66913)
ThunderherdMigration = Card(name="thunderherd_migration", pretty_name="Thunderherd Migration", cost=['1', 'G'],
                            color_identity=['G'], card_type="Sorcery", sub_types="",
                            abilities=[117133, 62342], set_id="RIX", rarity="Uncommon", set_number=149,
                            mtga_id=66915)
WaywardSwordtooth = Card(name="wayward_swordtooth", pretty_name="Wayward Swordtooth", cost=['2', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[165, 13760, 117134], set_id="RIX", rarity="Rare", set_number=150,
                         mtga_id=66917)
WorldShaper = Card(name="world_shaper", pretty_name="World Shaper", cost=['3', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                   abilities=[117135, 117136], set_id="RIX", rarity="Rare", set_number=151,
                   mtga_id=66919)
AngraththeFlameChained = Card(name="angrath_the_flamechained", pretty_name="Angrath, the Flame-Chained", cost=['3', 'B', 'R'],
                              color_identity=['B', 'R'], card_type="Planeswalker", sub_types="Angrath",
                              abilities=[117137, 117138, 117139], set_id="RIX", rarity="Mythic Rare", set_number=152,
                              mtga_id=66921)
AtzocanSeer = Card(name="atzocan_seer", pretty_name="Atzocan Seer", cost=['1', 'G', 'W'],
                   color_identity=['G', 'W'], card_type="Creature", sub_types="Human Druid",
                   abilities=[1055, 117142], set_id="RIX", rarity="Uncommon", set_number=153,
                   mtga_id=66923)
AzortheLawbringer = Card(name="azor_the_lawbringer", pretty_name="Azor, the Lawbringer", cost=['2', 'W', 'W', 'U', 'U'],
                         color_identity=['W', 'U'], card_type="Creature", sub_types="Sphinx",
                         abilities=[8, 117145, 117149], set_id="RIX", rarity="Mythic Rare", set_number=154,
                         mtga_id=66925)
DeadeyeBrawler = Card(name="deadeye_brawler", pretty_name="Deadeye Brawler", cost=['2', 'U', 'B'],
                      color_identity=['U', 'B'], card_type="Creature", sub_types="Human Pirate",
                      abilities=[1, 165, 117048], set_id="RIX", rarity="Uncommon", set_number=155,
                      mtga_id=66927)
DireFleetNeckbreaker = Card(name="dire_fleet_neckbreaker", pretty_name="Dire Fleet Neckbreaker", cost=['2', 'B', 'R'],
                            color_identity=['B', 'R'], card_type="Creature", sub_types="Orc Pirate",
                            abilities=[117073], set_id="RIX", rarity="Uncommon", set_number=156,
                            mtga_id=66929)
ElendatheDuskRose = Card(name="elenda_the_dusk_rose", pretty_name="Elenda, the Dusk Rose", cost=['2', 'W', 'B'],
                         color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire Knight",
                         abilities=[12, 99770, 116997], set_id="RIX", rarity="Mythic Rare", set_number=157,
                         mtga_id=66931)
HadanasClimb = Card(name="hadanas_climb", pretty_name="Hadana's Climb", cost=['1', 'G', 'U'],
                    color_identity=['G', 'U'], card_type="Enchantment", sub_types="",
                    abilities=[117123], set_id="RIX", rarity="Rare", set_number=158,
                    mtga_id=66933)
WingedTempleofOrazca = Card(name="winged_temple_of_orazca", pretty_name="Winged Temple of Orazca", cost=[],
                            color_identity=['U', 'G'], card_type="Land", sub_types="",
                            abilities=[1055, 116999], set_id="RIX", rarity="Rare", set_number=158,
                            mtga_id=66935)
HuatliRadiantChampion = Card(name="huatli_radiant_champion", pretty_name="Huatli, Radiant Champion", cost=['2', 'G', 'W'],
                             color_identity=['G', 'W'], card_type="Planeswalker", sub_types="Huatli",
                             abilities=[117000, 1202, 117002], set_id="RIX", rarity="Mythic Rare", set_number=159,
                             mtga_id=66937)
JourneytoEternity = Card(name="journey_to_eternity", pretty_name="Journey to Eternity", cost=['1', 'B', 'G'],
                         color_identity=['B', 'G'], card_type="Enchantment", sub_types="Aura",
                         abilities=[1886, 117004], set_id="RIX", rarity="Rare", set_number=160,
                         mtga_id=66939)
AtzalCaveofEternity = Card(name="atzal_cave_of_eternity", pretty_name="Atzal, Cave of Eternity", cost=[],
                           color_identity=['B', 'G'], card_type="Land", sub_types="",
                           abilities=[1055, 117005], set_id="RIX", rarity="Rare", set_number=160,
                           mtga_id=66941)
JungleCreeper = Card(name="jungle_creeper", pretty_name="Jungle Creeper", cost=['1', 'B', 'G'],
                     color_identity=['B', 'G'], card_type="Creature", sub_types="Elemental",
                     abilities=[117006], set_id="RIX", rarity="Uncommon", set_number=161,
                     mtga_id=66943)
KumenaTyrantofOrazca = Card(name="kumena_tyrant_of_orazca", pretty_name="Kumena, Tyrant of Orazca", cost=['1', 'G', 'U'],
                            color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Shaman",
                            abilities=[117007, 117008, 117095], set_id="RIX", rarity="Mythic Rare", set_number=162,
                            mtga_id=66945)
LegionLieutenant = Card(name="legion_lieutenant", pretty_name="Legion Lieutenant", cost=['W', 'B'],
                        color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire Knight",
                        abilities=[117100], set_id="RIX", rarity="Uncommon", set_number=163,
                        mtga_id=66947)
MerfolkMistbinder = Card(name="merfolk_mistbinder", pretty_name="Merfolk Mistbinder", cost=['G', 'U'],
                         color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Shaman",
                         abilities=[117011], set_id="RIX", rarity="Uncommon", set_number=164,
                         mtga_id=66949)
PathofMettle = Card(name="path_of_mettle", pretty_name="Path of Mettle", cost=['R', 'W'],
                    color_identity=['R', 'W'], card_type="Enchantment", sub_types="",
                    abilities=[117012, 117013], set_id="RIX", rarity="Rare", set_number=165,
                    mtga_id=66951)
MetzaliTowerofTriumph = Card(name="metzali_tower_of_triumph", pretty_name="Metzali, Tower of Triumph", cost=[],
                             color_identity=['W', 'R'], card_type="Land", sub_types="",
                             abilities=[1055, 117014, 117112], set_id="RIX", rarity="Rare", set_number=165,
                             mtga_id=66953)
ProfaneProcession = Card(name="profane_procession", pretty_name="Profane Procession", cost=['1', 'W', 'B'],
                         color_identity=['W', 'B'], card_type="Enchantment", sub_types="",
                         abilities=[117015], set_id="RIX", rarity="Rare", set_number=166,
                         mtga_id=66955)
TomboftheDuskRose = Card(name="tomb_of_the_dusk_rose", pretty_name="Tomb of the Dusk Rose", cost=[],
                         color_identity=['W', 'B'], card_type="Land", sub_types="",
                         abilities=[1055, 117016], set_id="RIX", rarity="Rare", set_number=166,
                         mtga_id=66957)
ProteanRaider = Card(name="protean_raider", pretty_name="Protean Raider", cost=['1', 'U', 'R'],
                     color_identity=['U', 'R'], card_type="Creature", sub_types="Shapeshifter Pirate",
                     abilities=[117017], set_id="RIX", rarity="Rare", set_number=167,
                     mtga_id=66959)
RagingRegisaur = Card(name="raging_regisaur", pretty_name="Raging Regisaur", cost=['2', 'R', 'G'],
                      color_identity=['R', 'G'], card_type="Creature", sub_types="Dinosaur",
                      abilities=[103433], set_id="RIX", rarity="Uncommon", set_number=168,
                      mtga_id=66961)
RelentlessRaptor = Card(name="relentless_raptor", pretty_name="Relentless Raptor", cost=['R', 'W'],
                        color_identity=['R', 'W'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[15, 117018], set_id="RIX", rarity="Uncommon", set_number=169,
                        mtga_id=66963)
ResplendentGriffin = Card(name="resplendent_griffin", pretty_name="Resplendent Griffin", cost=['1', 'W', 'U'],
                          color_identity=['W', 'U'], card_type="Creature", sub_types="Griffin",
                          abilities=[8, 165, 117127], set_id="RIX", rarity="Uncommon", set_number=170,
                          mtga_id=66965)
SiegehornCeratops = Card(name="siegehorn_ceratops", pretty_name="Siegehorn Ceratops", cost=['G', 'W'],
                         color_identity=['G', 'W'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[117019], set_id="RIX", rarity="Rare", set_number=171,
                         mtga_id=66967)
StormFleetSprinter = Card(name="storm_fleet_sprinter", pretty_name="Storm Fleet Sprinter", cost=['1', 'U', 'R'],
                          color_identity=['U', 'R'], card_type="Creature", sub_types="Human Pirate",
                          abilities=[9, 62969], set_id="RIX", rarity="Uncommon", set_number=172,
                          mtga_id=66969)
StormtheVault = Card(name="storm_the_vault", pretty_name="Storm the Vault", cost=['2', 'U', 'R'],
                     color_identity=['U', 'R'], card_type="Enchantment", sub_types="",
                     abilities=[117020, 117021], set_id="RIX", rarity="Rare", set_number=173,
                     mtga_id=66971)
VaultofCatlacan = Card(name="vault_of_catlacan", pretty_name="Vault of Catlacan", cost=[],
                       color_identity=['U'], card_type="Land", sub_types="",
                       abilities=[1055, 13680], set_id="RIX", rarity="Rare", set_number=173,
                       mtga_id=66973)
ZacamaPrimalCalamity = Card(name="zacama_primal_calamity", pretty_name="Zacama, Primal Calamity", cost=['6', 'R', 'G', 'W'],
                            color_identity=['W', 'R', 'G'], card_type="Creature", sub_types="Elder Dinosaur",
                            abilities=[15, 13, 14, 117022, 117025, 117024, 117034], set_id="RIX", rarity="Mythic Rare", set_number=174,
                            mtga_id=66975)
AwakenedAmalgam = Card(name="awakened_amalgam", pretty_name="Awakened Amalgam", cost=['4'],
                       color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                       abilities=[117026], set_id="RIX", rarity="Rare", set_number=175,
                       mtga_id=66977)
AzorsGateway = Card(name="azors_gateway", pretty_name="Azor's Gateway", cost=['2'],
                    color_identity=[], card_type="Artifact", sub_types="",
                    abilities=[117027], set_id="RIX", rarity="Mythic Rare", set_number=176,
                    mtga_id=66979)
SanctumoftheSun = Card(name="sanctum_of_the_sun", pretty_name="Sanctum of the Sun", cost=[],
                       color_identity=[], card_type="Land", sub_types="",
                       abilities=[117028], set_id="RIX", rarity="Mythic Rare", set_number=176,
                       mtga_id=66981)
CaptainsHook = Card(name="captains_hook", pretty_name="Captain's Hook", cost=['3'],
                    color_identity=[], card_type="Artifact", sub_types="Equipment",
                    abilities=[117043, 117030, 1268], set_id="RIX", rarity="Rare", set_number=177,
                    mtga_id=66983)
GleamingBarrier = Card(name="gleaming_barrier", pretty_name="Gleaming Barrier", cost=['2'],
                       color_identity=[], card_type="Artifact Creature", sub_types="Wall",
                       abilities=[2, 116851], set_id="RIX", rarity="Common", set_number=178,
                       mtga_id=66985)
GoldenGuardian = Card(name="golden_guardian", pretty_name="Golden Guardian", cost=['4'],
                      color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                      abilities=[2, 117031], set_id="RIX", rarity="Rare", set_number=179,
                      mtga_id=66987)
GoldForgeGarrison = Card(name="goldforge_garrison", pretty_name="Gold-Forge Garrison", cost=[],
                         color_identity=[], card_type="Land", sub_types="",
                         abilities=[14619, 117052], set_id="RIX", rarity="Rare", set_number=179,
                         mtga_id=66989)
TheImmortalSun = Card(name="the_immortal_sun", pretty_name="The Immortal Sun", cost=['6'],
                      color_identity=[], card_type="Artifact", sub_types="",
                      abilities=[117054, 1500, 117035, 1456], set_id="RIX", rarity="Mythic Rare", set_number=180,
                      mtga_id=66991)
OrazcaRelic = Card(name="orazca_relic", pretty_name="Orazca Relic", cost=['3'],
                   color_identity=[], card_type="Artifact", sub_types="",
                   abilities=[165, 1152, 117058], set_id="RIX", rarity="Common", set_number=181,
                   mtga_id=66993)
SilentGravestone = Card(name="silent_gravestone", pretty_name="Silent Gravestone", cost=['1'],
                        color_identity=[], card_type="Artifact", sub_types="",
                        abilities=[95477, 117037], set_id="RIX", rarity="Rare", set_number=182,
                        mtga_id=66995)
StriderHarness = Card(name="strider_harness", pretty_name="Strider Harness", cost=['3'],
                      color_identity=[], card_type="Artifact", sub_types="Equipment",
                      abilities=[9144, 1268], set_id="RIX", rarity="Common", set_number=183,
                      mtga_id=66997)
TravelersAmulet = Card(name="travelers_amulet", pretty_name="Traveler's Amulet", cost=['1'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[92632], set_id="RIX", rarity="Common", set_number=184,
                       mtga_id=66999)
ArchofOrazca = Card(name="arch_of_orazca", pretty_name="Arch of Orazca", cost=[],
                    color_identity=[], card_type="Land", sub_types="",
                    abilities=[165, 1152, 117038], set_id="RIX", rarity="Rare", set_number=185,
                    mtga_id=67001)
EvolvingWilds = Card(name="evolving_wilds", pretty_name="Evolving Wilds", cost=[],
                     color_identity=[], card_type="Land", sub_types="",
                     abilities=[88024], set_id="RIX", rarity="Common", set_number=186,
                     mtga_id=67003)
ForsakenSanctuary = Card(name="forsaken_sanctuary", pretty_name="Forsaken Sanctuary", cost=[],
                         color_identity=['W', 'B'], card_type="Land", sub_types="",
                         abilities=[76735, 18472], set_id="RIX", rarity="Uncommon", set_number=187,
                         mtga_id=67005)
FoulOrchard = Card(name="foul_orchard", pretty_name="Foul Orchard", cost=[],
                   color_identity=['B', 'G'], card_type="Land", sub_types="",
                   abilities=[76735, 4407], set_id="RIX", rarity="Uncommon", set_number=188,
                   mtga_id=67007)
HighlandLake = Card(name="highland_lake", pretty_name="Highland Lake", cost=[],
                    color_identity=['U', 'R'], card_type="Land", sub_types="",
                    abilities=[76735, 1039], set_id="RIX", rarity="Uncommon", set_number=189,
                    mtga_id=67009)
StoneQuarry = Card(name="stone_quarry", pretty_name="Stone Quarry", cost=[],
                   color_identity=['R', 'W'], card_type="Land", sub_types="",
                   abilities=[76735, 4247], set_id="RIX", rarity="Uncommon", set_number=190,
                   mtga_id=67011)
WoodlandStream = Card(name="woodland_stream", pretty_name="Woodland Stream", cost=[],
                      color_identity=['G', 'U'], card_type="Land", sub_types="",
                      abilities=[76735, 18504], set_id="RIX", rarity="Uncommon", set_number=191,
                      mtga_id=67013)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="RIX", rarity="Basic", set_number=192,
              mtga_id=67015)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="RIX", rarity="Basic", set_number=193,
              mtga_id=67017)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="RIX", rarity="Basic", set_number=194,
             mtga_id=67019)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="RIX", rarity="Basic", set_number=195,
                mtga_id=67021)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="RIX", rarity="Basic", set_number=196,
              mtga_id=67023)
VraskaSchemingGorgon = Card(name="vraska_scheming_gorgon", pretty_name="Vraska, Scheming Gorgon", cost=['4', 'B', 'B'],
                            color_identity=['B'], card_type="Planeswalker", sub_types="Vraska",
                            abilities=[117068, 102469, 117040], set_id="RIX", rarity="Mythic Rare", set_number=197,
                            mtga_id=67025)
VampireChampion = Card(name="vampire_champion", pretty_name="Vampire Champion", cost=['3', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                       abilities=[1], set_id="RIX", rarity="Common", set_number=198,
                       mtga_id=67027)
VraskasConquistador = Card(name="vraskas_conquistador", pretty_name="Vraska's Conquistador", cost=['1', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                           abilities=[117041], set_id="RIX", rarity="Uncommon", set_number=199,
                           mtga_id=67029)
VraskasScorn = Card(name="vraskas_scorn", pretty_name="Vraska's Scorn", cost=['2', 'B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[117042], set_id="RIX", rarity="Rare", set_number=200,
                    mtga_id=67031)
AngrathMinotaurPirate = Card(name="angrath_minotaur_pirate", pretty_name="Angrath, Minotaur Pirate", cost=['4', 'B', 'R'],
                             color_identity=['B', 'R'], card_type="Planeswalker", sub_types="Angrath",
                             abilities=[117075, 1266, 117079], set_id="RIX", rarity="Mythic Rare", set_number=201,
                             mtga_id=67033)
AngrathsAmbusher = Card(name="angraths_ambusher", pretty_name="Angrath's Ambusher", cost=['2', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Orc Pirate",
                        abilities=[117044], set_id="RIX", rarity="Uncommon", set_number=202,
                        mtga_id=67035)
SwabGoblin = Card(name="swab_goblin", pretty_name="Swab Goblin", cost=['1', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Goblin Pirate",
                  abilities=[], set_id="RIX", rarity="Common", set_number=203,
                  mtga_id=67037)
AngrathsFury = Card(name="angraths_fury", pretty_name="Angrath's Fury", cost=['3', 'B', 'R'],
                    color_identity=['B', 'R'], card_type="Sorcery", sub_types="",
                    abilities=[117045], set_id="RIX", rarity="Rare", set_number=204,
                    mtga_id=67039)
CinderBarrens = Card(name="cinder_barrens", pretty_name="Cinder Barrens", cost=[],
                     color_identity=['B', 'R'], card_type="Land", sub_types="",
                     abilities=[76735, 1211], set_id="RIX", rarity="Common", set_number=205,
                     mtga_id=67041)
Elemental = Card(name="elemental", pretty_name="Elemental", cost=[],
                 color_identity=[], card_type="Creature", sub_types="Elemental",
                 abilities=[116985], set_id="RIX", rarity="Token", set_number=1,
                 mtga_id=67043)
Elemental2 = Card(name="elemental", pretty_name="Elemental", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Elemental",
                  abilities=[], set_id="RIX", rarity="Token", set_number=2,
                  mtga_id=67044)
Saproling = Card(name="saproling", pretty_name="Saproling", cost=[],
                 color_identity=[], card_type="Creature", sub_types="Saproling",
                 abilities=[], set_id="RIX", rarity="Token", set_number=3,
                 mtga_id=67045)
Golem = Card(name="golem", pretty_name="Golem", cost=[],
             color_identity=[], card_type="Artifact Creature", sub_types="Golem",
             abilities=[], set_id="RIX", rarity="Token", set_number=4,
             mtga_id=67046)
CitysBlessing = Card(name="citys_blessing", pretty_name="City's Blessing", cost=[],
                     color_identity=[], card_type="", sub_types="",
                     abilities=[], set_id="RIX", rarity="Token", set_number=6,
                     mtga_id=67082)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
RivalsOfIxalan = Set("rix", cards=clsmembers)

set_ability_map = {1: 'Deathtouch',
 2: 'Defender',
 3: 'Double strike',
 6: 'First strike',
 7: 'Flash',
 8: 'Flying',
 9: 'Haste',
 10: 'Hexproof',
 12: 'Lifelink',
 13: 'Reach',
 14: 'Trample',
 15: 'Vigilance',
 104: 'Indestructible',
 142: 'Menace',
 165: 'Ascend',
 1009: 'Whenever Bishop of Binding attacks, target Vampire gets +X/+X until '
       'end of turn, where X is the power of the exiled card.',
 1013: 'Choose one   Destroy target Vampire.  Destroy target enchantment.',
 1027: 'Enchant creature',
 1036: "Snubhorn Sentry gets +3/+0 as long as you have the city's blessing.",
 1039: '{oT}: Add {oU} or {oR}.',
 1048: 'Crashing Tide has flash as long as you control a Merfolk.',
 1055: '{oT}: Add one mana of any color.',
 1056: 'Return target instant or sorcery card from your graveyard to your '
       'hand. Exile Flood of Recollection.',
 1062: 'At the beginning of your upkeep, each player draws a card. If you have '
       "the city's blessing, instead only you draw a card.",
 1080: "Spire Winder gets +1/+1 as long as you have the city's blessing.",
 1083: "Enchanted creature can't attack or block.",
 1099: 'Each opponent loses 1 life for each creature you control.',
 1117: "Each opponent sacrifices a creature. If you have the city's blessing, "
       'instead each opponent sacrifices half the creatures they control, '
       'rounded up.',
 1125: 'If Charging Tuskodon would deal combat damage to a player, it deals '
       'double that damage to that player instead.',
 1142: 'Counter target noncreature spell.',
 1150: "When Tilonalli's Crown enters the battlefield, it deals 1 damage to "
       'enchanted creature.',
 1152: '{oT}: Add {oC}.',
 1202: '-1: Target creature gets +X/+X until end of turn, where X is the '
       'number of creatures you control.',
 1211: '{oT}: Add {oB} or {oR}.',
 1229: '<i>Enrage</i>  Whenever Imperial Ceratops is dealt damage, you gain 2 '
       'life.',
 1266: '-3: Return target Pirate card from your graveyard to the battlefield.',
 1268: 'Equip {o1}',
 1456: 'Creatures you control get +1/+1.',
 1500: 'At the beginning of your draw step, draw an additional card.',
 1640: 'You have no maximum hand size.',
 1886: 'Enchant creature you control',
 2640: 'At the beginning of each upkeep, create a 1/1 green Saproling creature '
       'token.',
 2732: 'Destroy target attacking or blocking creature.',
 4247: '{oT}: Add {oR} or {oW}.',
 4407: '{oT}: Add {oB} or {oG}.',
 6426: 'You may play an additional land this turn.',
 6906: 'Target creature gets +1/+1 until end of turn.',
 9144: 'Equipped creature gets +1/+1 and has haste.',
 13680: '{oT}: Add {oU} for each artifact you control.',
 13760: 'You may play an additional land on each of your turns.',
 14018: 'Enchant creature an opponent controls',
 14619: '{oT}: Add two mana of any one color.',
 18472: '{oT}: Add {oW} or {oB}.',
 18504: '{oT}: Add {oG} or {oU}.',
 20207: 'Put a +1/+1 counter on target creature you control. Then that '
        "creature fights target creature you don't control.",
 20262: 'When Bishop of Binding enters the battlefield, exile target creature '
        'an opponent controls until Bishop of Binding leaves the battlefield.',
 20631: 'Enchanted creature gets +1/+1 and has lifelink.',
 21773: 'Bombard deals 4 damage to target creature.',
 22505: "Return target creature to its owner's hand.",
 22564: 'Destroy target artifact.',
 24122: 'Return target creature card from your graveyard to your hand.',
 25846: 'Counter target spell.',
 25848: 'Draw a card.',
 26818: 'Destroy target creature.',
 29759: 'Destroy target creature with flying.',
 62243: 'Exile target creature with power 3 or less.',
 62342: 'Search your library for a basic land card, put it onto the '
        'battlefield tapped, then shuffle your library.',
 62969: "Storm Fleet Sprinter can't be blocked.",
 76735: 'Cinder Barrens enters the battlefield tapped.',
 76882: 'As Radiant Destiny enters the battlefield, choose a creature type.',
 86621: "Famished Paladin doesn't untap during your untap step.",
 86788: 'When Blood Sun enters the battlefield, draw a card.',
 87929: 'As an additional cost to cast this spell, discard a card.',
 87941: "Giltgrove Stalker can't be blocked by creatures with power 2 or less.",
 88024: '{oT}, Sacrifice Evolving Wilds: Search your library for a basic land '
        'card, put it onto the battlefield tapped, then shuffle your library.',
 88159: 'When Dusk Legion Zealot enters the battlefield, you draw a card and '
        'you lose 1 life.',
 88178: "Enchanted creature doesn't untap during its controller's untap step.",
 88622: 'Shake the Foundations deals 1 damage to each creature without flying.',
 89285: '{o1}, Sacrifice Thrashing Brontodon: Destroy target artifact or '
        'enchantment.',
 89789: 'When Waterknot enters the battlefield, tap enchanted creature.',
 90077: 'Prevent all combat damage that would be dealt to Everdawn Champion.',
 92582: 'As an additional cost to cast this spell, reveal a Merfolk card from '
        'your hand or pay {o3}.',
 92594: 'When Forerunner of the Heralds enters the battlefield, you may search '
        'your library for a Merfolk card, reveal it, then shuffle your library '
        'and put that card on top of it.',
 92632: "{o1}, Sacrifice Traveler's Amulet: Search your library for a basic "
        'land card, reveal it, put it into your hand, then shuffle your '
        'library.',
 95477: "Cards in graveyards can't be the targets of spells or abilities.",
 99593: 'When Jadecraft Artisan enters the battlefield, target creature gets '
        '+2/+2 until end of turn.',
 99770: 'Whenever another creature dies, put a +1/+1 counter on Elenda, the '
        'Dusk Rose.',
 101552: '<i>Raid</i>  Swaggering Corsair enters the battlefield with a +1/+1 '
         'counter on it if you attacked with a creature this turn.',
 102469: '-3: Destroy target creature.',
 102891: 'When Sanguine Glorifier enters the battlefield, put a +1/+1 counter '
         'on another target Vampire you control.',
 103433: 'Whenever Raging Regisaur attacks, it deals 1 damage to any target.',
 116758: 'When Legion Conquistador enters the battlefield, you may search your '
         'library for any number of cards named Legion Conquistador, reveal '
         'them, put them into your hand, then shuffle your library.',
 116783: 'When Crested Herdcaller enters the battlefield, create a 3/3 green '
         'Dinosaur creature token with trample.',
 116788: "When Squire's Devotion enters the battlefield, create a 1/1 white "
         'Vampire creature token with lifelink.',
 116826: 'When Brazen Freebooter enters the battlefield, create a colorless '
         'Treasure artifact token with "{oT}, Sacrifice this artifact: Add one '
         'mana of any color."',
 116851: 'When Gleaming Barrier dies, create a colorless Treasure artifact '
         'token with "{oT}, Sacrifice this artifact: Add one mana of any '
         'color."',
 116971: 'Whenever Majestic Heliopterus attacks, another target Dinosaur you '
         'control gains flying until end of turn.',
 116972: 'If a source would deal damage to another Dinosaur you control, '
         'prevent all but 1 of that damage.',
 116973: '<i>Enrage</i>  Whenever Trapjaw Tyrant is dealt damage, exile target '
         'creature an opponent controls until Trapjaw Tyrant leaves the '
         'battlefield.',
 116974: 'At the beginning of each upkeep, if you lost life last turn, put a '
         '+1/+1 counter on Paladin of Atonement.',
 116975: 'Target creature gets +2/+2 until end of turn. You gain 2 life.',
 116976: 'When Forerunner of the Empire enters the battlefield, you may search '
         'your library for a Dinosaur card, reveal it, then shuffle your '
         'library and put that card on top of it.',
 116977: 'Whenever a Dinosaur enters the battlefield under your control, you '
         'may have Forerunner of the Empire deal 1 damage to each creature.',
 116978: 'When Form of the Dinosaur enters the battlefield, your life total '
         'becomes 15.',
 116979: 'At the beginning of your upkeep, Form of the Dinosaur deals 15 '
         'damage to target creature an opponent controls and that creature '
         'deals damage equal to its power to you.',
 116981: 'Target creature an opponent controls deals damage equal to its power '
         'to another target creature that player controls.',
 116982: '<i>Enrage</i>  Whenever Needletooth Raptor is dealt damage, it deals '
         '5 damage to target creature an opponent controls.',
 116983: 'Draw two cards and create two colorless Treasure artifact tokens '
         'with "{oT}, Sacrifice this artifact: Add one mana of any color."',
 116984: '<i>Raid</i>  If you attacked with a creature this turn, you may pay '
         "{oU} rather than pay this spell's mana cost.",
 116985: 'At the beginning of your upkeep, sacrifice this creature and return '
         'target card named Rekindling Phoenix from your graveyard to the '
         'battlefield. It gains haste until end of turn.',
 116986: 'When Rekindling Phoenix dies, create a 0/1 red Elemental creature '
         'token with "At the beginning of your upkeep, sacrifice this creature '
         'and return target card named Rekindling Phoenix from your graveyard '
         'to the battlefield. It gains haste until end of turn."',
 116987: 'Enchanted creature gets +2/+1 and has first strike.',
 116988: '<i>Enrage</i>  Whenever Silverclad Ferocidons is dealt damage, each '
         'opponent sacrifices a permanent.',
 116990: 'When Cherished Hatchling dies, you may cast Dinosaur spells this '
         'turn as though they had flash, and whenever you cast a Dinosaur '
         'spell this turn, it gains "When this creature enters the '
         'battlefield, you may have it fight another target creature."',
 116991: "{o3oU}: Target Merfolk can't be blocked this turn.",
 116992: 'Whenever another Merfolk enters the battlefield under your control, '
         'put a +1/+1 counter on Forerunner of the Heralds.',
 116993: 'When Crafty Cutpurse enters the battlefield, each token that would '
         "be created under an opponent's control this turn is created under "
         'your control instead.',
 116994: "As long as it's your turn, Hardy Veteran gets +0/+2.",
 116995: 'When Jungleborn Pioneer enters the battlefield, create a 1/1 blue '
         'Merfolk creature token with hexproof.',
 116996: 'When Paladin of Atonement dies, you gain life equal to its '
         'toughness.',
 116997: 'When Elenda dies, create X 1/1 white Vampire creature tokens with '
         "lifelink, where X is Elenda's power.",
 116998: "At the beginning of your end step, if you didn't attack with a "
         'creature this turn, sacrifice See Red.',
 116999: '{o1oGoU}, {oT}: Target creature you control gains flying and gets '
         '+X/+X until end of turn, where X is its power.',
 117000: '+1: Put a loyalty counter on Huatli, Radiant Champion for each '
         'creature you control.',
 117002: '-8: You get an emblem with "Whenever a creature enters the '
         'battlefield under your control, you may draw a card."',
 117003: '<i>Raid</i>  When Deadeye Rig-Hauler enters the battlefield, if you '
         'attacked with a creature this turn, you may return target creature '
         "to its owner's hand.",
 117004: 'When enchanted creature dies, return it to the battlefield under '
         'your control, then return Journey to Eternity to the battlefield '
         'transformed under your control.',
 117005: '{o3oBoG}, {oT}: Return target creature card from your graveyard to '
         'the battlefield.',
 117006: '{o3oBoG}: Return Jungle Creeper from your graveyard to your hand.',
 117007: 'Tap another untapped Merfolk you control: Kumena, Tyrant of Orazca '
         "can't be blocked this turn.",
 117008: 'Tap three untapped Merfolk you control: Draw a card.',
 117009: "Return target nonland permanent to its owner's hand. If you have the "
         "city's blessing, you may put that permanent on top of its owner's "
         'library instead.',
 117011: 'Other Merfolk you control get +1/+1.',
 117012: 'When Path of Mettle enters the battlefield, it deals 1 damage to '
         "each creature that doesn't have first strike, double strike, "
         'vigilance, or haste.',
 117013: 'Whenever you attack with at least two creatures that have first '
         'strike, double strike, vigilance, and/or haste, transform Path of '
         'Mettle.',
 117014: '{o1oR}, {oT}: Metzali, Tower of Triumph deals 2 damage to each '
         'opponent.',
 117015: '{o3oWoB}: Exile target creature. Then if there are three or more '
         'cards exiled with Profane Procession, transform it.',
 117016: '{o2oWoB}, {oT}: Put a creature card exiled with this permanent onto '
         'the battlefield under your control.',
 117017: '<i>Raid</i>  If you attacked with a creature this turn, you may have '
         'Protean Raider enter the battlefield as a copy of any creature on '
         'the battlefield.',
 117018: 'Relentless Raptor attacks or blocks each combat if able.',
 117019: '<i>Enrage</i>  Whenever Siegehorn Ceratops is dealt damage, put two '
         '+1/+1 counters on it.',
 117020: 'Whenever one or more creatures you control deal combat damage to a '
         'player, create a colorless Treasure artifact token with "{oT}, '
         'Sacrifice this artifact: Add one mana of any color."',
 117021: 'At the beginning of your end step, if you control five or more '
         'artifacts, transform Storm the Vault.',
 117022: 'When Zacama, Primal Calamity enters the battlefield, if you cast it, '
         'untap all lands you control.',
 117023: 'Counter target creature spell. You create a colorless Treasure '
         'artifact token with "{oT}, Sacrifice this artifact: Add one mana of '
         'any color."',
 117024: '{o2oG}: Destroy target artifact or enchantment.',
 117025: '{o2oR}: Zacama deals 3 damage to target creature.',
 117026: "Awakened Amalgam's power and toughness are each equal to the number "
         'of differently named lands you control.',
 117027: '{o1}, {oT}: Draw a card, then exile a card from your hand. If cards '
         'with five or more different converted mana costs are exiled with '
         "Azor's Gateway, you gain 5 life, untap Azor's Gateway, and transform "
         'it.',
 117028: '{oT}: Add X mana of any one color, where X is your life total.',
 117029: 'When Induced Amnesia enters the battlefield, target player exiles '
         'all cards from their hand face down, then draws that many cards.',
 117030: "Whenever Captain's Hook becomes unattached from a permanent, destroy "
         'that permanent.',
 117031: '{o2}: Golden Guardian fights another target creature you control. '
         'When Golden Guardian dies this turn, return it to the battlefield '
         'transformed under your control.',
 117032: 'When Induced Amnesia is put into a graveyard from the battlefield, '
         "return the exiled cards to their owner's hand.",
 117033: 'Creatures you control get +1/+1 until end of turn. If you have the '
         "city's blessing, those creatures get +2/+2 until end of turn "
         'instead.',
 117034: '{o2oW}: You gain 3 life.',
 117035: 'Spells you cast cost {o1} less to cast.',
 117036: "Kitesail Corsair has flying as long as it's attacking.",
 117037: '{o4}, {oT}: Exile Silent Gravestone and all cards from all '
         'graveyards. Draw a card.',
 117038: '{o5}, {oT}: Draw a card. Activate this ability only if you have the '
         "city's blessing.",
 117040: '-10: Until end of turn, creatures you control gain deathtouch and '
         '"Whenever this creature deals damage to an opponent, that player '
         'loses the game."',
 117041: "Whenever Vraska's Conquistador attacks or blocks, if you control a "
         'Vraska planeswalker, target opponent loses 2 life and you gain 2 '
         'life.',
 117042: 'Target opponent loses 4 life. You may search your library and/or '
         'graveyard for a card named Vraska, Scheming Gorgon, reveal it, and '
         'put it into your hand. If you search your library this way, shuffle '
         'it.',
 117043: 'Equipped creature gets +2/+0, has menace, and is a Pirate in '
         'addition to its other creature types.',
 117044: "Angrath's Ambusher gets +2/+0 as long as you control an Angrath "
         'planeswalker.',
 117045: "Destroy target creature. Angrath's Fury deals 3 damage to target "
         'player or planeswalker. You may search your library and/or graveyard '
         'for a card named Angrath, Minotaur Pirate, reveal it, and put it '
         'into your hand. If you search your library this way, shuffle it.',
 117046: 'Whenever an opponent casts a noncreature spell, draw a card.',
 117047: 'Discard three cards: Exile Nezahal. Return it to the battlefield '
         "tapped under its owner's control at the beginning of the next end "
         'step.',
 117048: 'Whenever Deadeye Brawler deals combat damage to a player, if you '
         "have the city's blessing, draw a card.",
 117049: 'Exile target nonland permanent. For as long as that card remains '
         'exiled, its owner may cast it without paying its mana cost.',
 117050: "River Darter can't be blocked by Dinosaurs.",
 117051: 'Creatures you control of the chosen type get +1/+1. As long as you '
         "have the city's blessing, they also have vigilance.",
 117052: '{o4}, {oT}: Create a 4/4 colorless Golem artifact creature token.',
 117053: 'When Riverwise Augur enters the battlefield, draw three cards, then '
         'put two cards from your hand on top of your library in any order.',
 117054: "Players can't activate planeswalkers' loyalty abilities.",
 117055: "Enchanted creature gets +0/+2 as long as it's a Pirate. Otherwise, "
         'it gets -2/-0.',
 117056: 'Whenever a Merfolk you control deals combat damage to a player, draw '
         'a card.',
 117057: "Draw two cards. If you have the city's blessing, draw three cards "
         'instead.',
 117058: '{oT}, Sacrifice Orazca Relic: You gain 3 life and draw a card. '
         "Activate this ability only if you have the city's blessing.",
 117059: "As long as you have the city's blessing, Slippery Scoundrel has "
         "hexproof and can't be blocked.",
 117060: "Skymarcher Aspirant has flying as long as you have the city's "
         'blessing.',
 117061: 'When Martyr of Dusk dies, create a 1/1 white Vampire creature token '
         'with lifelink.',
 117062: '{o2oUoU}, {oT}, Put Timestream Navigator on the bottom of its '
         "owner's library: Take an extra turn after this one. Activate this "
         "ability only if you have the city's blessing.",
 117063: 'Whenever Warkite Marauder attacks, target creature defending player '
         'controls loses all abilities and has base power and toughness 0/1 '
         'until end of turn.',
 117064: 'Each opponent discards two cards. If you control a Vampire, each '
         'opponent loses 2 life and you gain 2 life.',
 117065: 'Each player chooses any number of creatures they control with total '
         'power 4 or less, then sacrifices all other creatures they control.',
 117066: 'When Champion of Dusk enters the battlefield, you draw X cards and '
         'you lose X life, where X is the number of Vampires you control.',
 117067: 'Target opponent reveals their hand. You choose a nonland card from '
         'it. That player discards that card.',
 117068: '+2: Creatures you control get +1/+0 until end of turn.',
 117069: 'When enchanted creature dies, exile cards equal to its power from '
         "the top of its owner's library. You may cast nonland cards from "
         'among them for as long as they remain exiled, and you may spend mana '
         'as though it were mana of any type to cast those spells.',
 117070: 'Whenever Dinosaur Hunter deals damage to a Dinosaur, destroy that '
         'creature.',
 117071: 'When Dire Fleet Poisoner enters the battlefield, target attacking '
         'Pirate you control gets +1/+1 and gains deathtouch until end of '
         'turn.',
 117072: "Dusk Charger gets +2/+2 as long as you have the city's blessing.",
 117073: 'Attacking Pirates you control get +2/+0.',
 117074: 'When Fathom Fleet Boarder enters the battlefield, you lose 2 life '
         'unless you control another Pirate.',
 117075: '+2: Angrath, Minotaur Pirate deals 1 damage to target opponent or '
         "planeswalker and each creature that player or that planeswalker's "
         'controller controls.',
 117076: 'When Forerunner of the Coalition enters the battlefield, you may '
         'search your library for a Pirate card, reveal it, then shuffle your '
         'library and put that card on top of it.',
 117077: "Each opponent can't cast instant or sorcery spells during that "
         "player's next turn.",
 117078: 'Whenever another Pirate enters the battlefield under your control, '
         'each opponent loses 1 life.',
 117079: '-11: Destroy all creatures target opponent controls. Angrath, '
         'Minotaur Pirate deals damage to that player equal to their total '
         'power.',
 117080: "All creatures get -2/-2 until end of turn. If you have the city's "
         'blessing, instead only creatures your opponents control get -2/-2 '
         'until end of turn.',
 117081: "Grasping Scoundrel gets +1/+0 as long as it's attacking.",
 117082: 'Whenever a creature enters the battlefield under your control, it '
         'explores.',
 117087: 'Choose one   Search your library for a card, put it into your hand, '
         'then shuffle your library.  Choose a card you own from outside the '
         'game and put it into your hand.',
 117088: "Whenever another creature you control dies, if you have the city's "
         'blessing, put a +1/+1 counter on Mausoleum Harpy.',
 117089: 'Target creature gets -2/-2 until end of turn. You gain 2 life.',
 117090: 'You may cast Oathsworn Vampire from your graveyard if you gained '
         'life this turn.',
 117091: 'Whenever another creature you control dies, create a colorless '
         'Treasure artifact token with "{oT}, Sacrifice this artifact: Add one '
         'mana of any color."',
 117092: 'When Ravenous Chupacabra enters the battlefield, destroy target '
         'creature an opponent controls.',
 117093: 'Sun-Crested Pterodon has vigilance as long as you control another '
         'Dinosaur.',
 117094: 'As an additional cost to cast this spell, reveal a Vampire card from '
         'your hand or pay {o1}.',
 117095: 'Tap five untapped Merfolk you control: Put a +1/+1 counter on each '
         'Merfolk you control.',
 117096: '{oB}, Reveal Tetzimoc, Primal Death from your hand: Put a prey '
         'counter on target creature. Activate this ability only during your '
         'turn.',
 117097: 'When Tetzimoc enters the battlefield, destroy each creature your '
         'opponents control with a prey counter on it.',
 117098: '{o1}, Discard a card: Tomb Robber explores.',
 117099: "At the beginning of your upkeep, if you have the city's blessing, "
         'reveal the top card of your library and put it into your hand. Each '
         "opponent loses X life and you gain X life, where X is that card's "
         'converted mana cost.',
 117100: 'Other Vampires you control get +1/+1.',
 117101: 'When Voracious Vampire enters the battlefield, target Vampire you '
         'control gets +1/+1 and gains menace until end of turn.',
 117102: 'All lands lose all abilities except mana abilities.',
 117103: 'For each land you control, create a colorless Treasure artifact '
         'token with "{oT}, Sacrifice this artifact: Add one mana of any '
         'color."',
 117105: 'Choose one   Target creature gets +1/+1 and gains first strike until '
         'end of turn.  Target Pirate gets +1/+1 and gains double strike until '
         'end of turn.',
 117106: 'As an additional cost to cast this spell, reveal a Pirate card from '
         'your hand or pay {o2}.',
 117107: 'When Dire Fleet Daredevil enters the battlefield, exile target '
         "instant or sorcery card from an opponent's graveyard. You may cast "
         'that card this turn, and you may spend mana as though it were mana '
         'of any type to cast that spell. If that card would be put into a '
         'graveyard this turn, exile it instead.',
 117108: 'Whenever Etali, Primal Storm attacks, exile the top card of each '
         "player's library, then you may cast any number of nonland cards "
         'exiled this way without paying their mana costs.',
 117109: '{oT}, Sacrifice Fanatical Firebrand: It deals 1 damage to any '
         'target.',
 117110: 'When Aquatic Incursion enters the battlefield, create two 1/1 blue '
         'Merfolk creature tokens with hexproof.',
 117111: "Reckless Rage deals 4 damage to target creature you don't control "
         'and 2 damage to target creature you control.',
 117112: '{o2oW}, {oT}: Choose a creature at random that attacked this turn. '
         'Destroy that creature.',
 117113: 'Stampeding Horncrest has haste as long as you control another '
         'Dinosaur.',
 117114: 'Storm Fleet Swashbuckler has double strike as long as you have the '
         "city's blessing.",
 117115: '{o2oR}: Sun-Collared Raptor gets +3/+0 until end of turn.',
 117116: 'Enchanted creature gets +3/+0 and has trample.',
 117117: "Whenever Tilonalli's Summoner attacks, you may pay {oXoR}. If you "
         'do, create X 1/1 red Elemental creature tokens that are tapped and '
         'attacking. At the beginning of the next end step, exile those tokens '
         "unless you have the city's blessing.",
 117118: '<i>Enrage</i>  Whenever Cacophodon is dealt damage, untap target '
         'permanent.',
 117119: 'Whenever another Merfolk enters the battlefield under your control, '
         'put a +1/+1 counter on target Merfolk you control.',
 117120: 'Target creature you control explores.',
 117121: 'Ghalta, Primal Hunger costs {oX} less to cast, where X is the total '
         'power of creatures you control.',
 117122: 'When Jade Bearer enters the battlefield, put a +1/+1 counter on '
         'another target Merfolk you control.',
 117123: 'At the beginning of combat on your turn, put a +1/+1 counter on '
         'target creature you control. Then if that creature has three or more '
         "+1/+1 counters on it, transform Hadana's Climb.",
 117124: 'When Jadelight Ranger enters the battlefield, it explores, then it '
         'explores again.',
 117125: 'Enchanted creature gets +1/+1 and has "Whenever this creature deals '
         'combat damage to a player, you may draw a card."',
 117126: 'Dinosaur spells you cast cost {o2} less to cast.',
 117127: "Whenever Resplendent Griffin attacks, if you have the city's "
         'blessing, put a +1/+1 counter on it.',
 117128: '<i>Enrage</i>  Whenever Overgrown Armasaur is dealt damage, create a '
         '1/1 green Saproling creature token.',
 117129: '<i>Enrage</i>  Whenever Polyraptor is dealt damage, create a token '
         "that's a copy of Polyraptor.",
 117130: 'Put two +1/+1 counters on each creature you control.',
 117131: 'When Swift Warden enters the battlefield, target Merfolk you control '
         'gains hexproof until end of turn.',
 117132: "Saprolings you control get +2/+2 as long as you have the city's "
         'blessing.',
 117133: 'As an additional cost to cast this spell, reveal a Dinosaur card '
         'from your hand or pay {o1}.',
 117134: "Wayward Swordtooth can't attack or block unless you have the city's "
         'blessing.',
 117135: 'Whenever World Shaper attacks, you may put the top three cards of '
         'your library into your graveyard.',
 117136: 'When World Shaper dies, put all land cards from your graveyard onto '
         'the battlefield tapped.',
 117137: '+1: Each opponent discards a card and loses 2 life.',
 117138: '-3: Gain control of target creature until end of turn. Untap it. It '
         'gains haste until end of turn. Sacrifice it at the beginning of the '
         'next end step if it has converted mana cost 3 or less.',
 117139: '-8: Each opponent loses life equal to the number of cards in their '
         'graveyard.',
 117140: 'When Baffling End enters the battlefield, exile target creature an '
         'opponent controls with converted mana cost 3 or less.',
 117141: 'When Baffling End leaves the battlefield, target opponent creates a '
         '3/3 green Dinosaur creature token with trample.',
 117142: 'Sacrifice Atzocan Seer: Return target Dinosaur card from your '
         'graveyard to your hand.',
 117143: 'Exile target creature with power greater than or equal to your life '
         'total.',
 117145: 'When Azor, the Lawbringer enters the battlefield, each opponent '
         "can't cast instant or sorcery spells during that player's next turn.",
 117146: 'Whenever you gain life, untap Famished Paladin.',
 117147: 'When Forerunner of the Legion enters the battlefield, you may search '
         'your library for a Vampire card, reveal it, then shuffle your '
         'library and put that card on top of it.',
 117148: 'Whenever another Vampire enters the battlefield under your control, '
         'target creature gets +1/+1 until end of turn.',
 117149: 'Whenever Azor attacks, you may pay {oXoWoUoU}. If you do, you gain X '
         'life and draw X cards.',
 119063: '<i>Enrage</i>  Whenever Frilled Deathspitter is dealt damage, it '
         'deals 2 damage to target opponent or planeswalker.',
 120290: 'Destroy target artifact or enchantment.',
 120421: "Nezahal, Primal Tide can't be countered.",
 121046: '<i>Raid</i>  This spell costs {o1} less to cast if you attacked with '
         'a creature this turn.'}
