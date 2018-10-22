
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


KarnScionofUrza = Card(name="karn_scion_of_urza", pretty_name="Karn, Scion of Urza", cost=['4'],
                       color_identity=[], card_type="Planeswalker", sub_types="Karn",
                       abilities=[119049, 119050, 119052], set_id="DAR", rarity="Mythic Rare", set_number=1,
                       mtga_id=67106)
AdamantWill = Card(name="adamant_will", pretty_name="Adamant Will", cost=['1', 'W'],
                   color_identity=['W'], card_type="Instant", sub_types="",
                   abilities=[119053], set_id="DAR", rarity="Common", set_number=2,
                   mtga_id=67108)
AvenSentry = Card(name="aven_sentry", pretty_name="Aven Sentry", cost=['3', 'W'],
                  color_identity=['W'], card_type="Creature", sub_types="Bird Soldier",
                  abilities=[8], set_id="DAR", rarity="Common", set_number=3,
                  mtga_id=67110)
BairdStewardofArgive = Card(name="baird_steward_of_argive", pretty_name="Baird, Steward of Argive", cost=['2', 'W', 'W'],
                            color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                            abilities=[15, 119054], set_id="DAR", rarity="Uncommon", set_number=4,
                            mtga_id=67112)
BenalishHonorGuard = Card(name="benalish_honor_guard", pretty_name="Benalish Honor Guard", cost=['1', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                          abilities=[119055], set_id="DAR", rarity="Common", set_number=5,
                          mtga_id=67114)
BenalishMarshal = Card(name="benalish_marshal", pretty_name="Benalish Marshal", cost=['W', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                       abilities=[2433], set_id="DAR", rarity="Rare", set_number=6,
                       mtga_id=67116)
BlessedLight = Card(name="blessed_light", pretty_name="Blessed Light", cost=['4', 'W'],
                    color_identity=['W'], card_type="Instant", sub_types="",
                    abilities=[6495], set_id="DAR", rarity="Common", set_number=7,
                    mtga_id=67118)
BoardtheWeatherlight = Card(name="board_the_weatherlight", pretty_name="Board the Weatherlight", cost=['1', 'W'],
                            color_identity=['W'], card_type="Sorcery", sub_types="",
                            abilities=[119045], set_id="DAR", rarity="Uncommon", set_number=8,
                            mtga_id=67120)
CalltheCavalry = Card(name="call_the_cavalry", pretty_name="Call the Cavalry", cost=['3', 'W'],
                      color_identity=['W'], card_type="Sorcery", sub_types="",
                      abilities=[19691], set_id="DAR", rarity="Common", set_number=9,
                      mtga_id=67122)
Charge = Card(name="charge", pretty_name="Charge", cost=['W'],
              color_identity=['W'], card_type="Instant", sub_types="",
              abilities=[25230], set_id="DAR", rarity="Common", set_number=10,
              mtga_id=67124)
DAvenantTrapper = Card(name="davenant_trapper", pretty_name="D'Avenant Trapper", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Archer",
                       abilities=[119057], set_id="DAR", rarity="Common", set_number=11,
                       mtga_id=67126)
DanithaCapashenParagon = Card(name="danitha_capashen_paragon", pretty_name="Danitha Capashen, Paragon", cost=['2', 'W'],
                              color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                              abilities=[6, 15, 12, 119058], set_id="DAR", rarity="Uncommon", set_number=12,
                              mtga_id=67128)
DaringArchaeologist = Card(name="daring_archaeologist", pretty_name="Daring Archaeologist", cost=['3', 'W'],
                           color_identity=['W'], card_type="Creature", sub_types="Human Artificer",
                           abilities=[88235, 119059], set_id="DAR", rarity="Rare", set_number=13,
                           mtga_id=67130)
DauntlessBodyguard = Card(name="dauntless_bodyguard", pretty_name="Dauntless Bodyguard", cost=['W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                          abilities=[119060, 119061], set_id="DAR", rarity="Uncommon", set_number=14,
                          mtga_id=67132)
Dub = Card(name="dub", pretty_name="Dub", cost=['2', 'W'],
           color_identity=['W'], card_type="Enchantment", sub_types="Aura",
           abilities=[1027, 118954], set_id="DAR", rarity="Common", set_number=15,
           mtga_id=67134)
EvraHalcyonWitness = Card(name="evra_halcyon_witness", pretty_name="Evra, Halcyon Witness", cost=['4', 'W', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Avatar",
                          abilities=[12, 118815], set_id="DAR", rarity="Rare", set_number=16,
                          mtga_id=67136)
ExcavationElephant = Card(name="excavation_elephant", pretty_name="Excavation Elephant", cost=['4', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Elephant",
                          abilities=[9313, 118837], set_id="DAR", rarity="Common", set_number=17,
                          mtga_id=67138)
FalloftheThran = Card(name="fall_of_the_thran", pretty_name="Fall of the Thran", cost=['5', 'W'],
                      color_identity=['W'], card_type="Enchantment", sub_types="Saga",
                      abilities=[118852, 103194, 119075], set_id="DAR", rarity="Rare", set_number=18,
                      mtga_id=67140)
GideonsReproach = Card(name="gideons_reproach", pretty_name="Gideon's Reproach", cost=['1', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[100370], set_id="DAR", rarity="Common", set_number=19,
                       mtga_id=67142)
HealingGrace = Card(name="healing_grace", pretty_name="Healing Grace", cost=['W'],
                    color_identity=['W'], card_type="Instant", sub_types="",
                    abilities=[118914], set_id="DAR", rarity="Common", set_number=20,
                    mtga_id=67144)
HistoryofBenalia = Card(name="history_of_benalia", pretty_name="History of Benalia", cost=['1', 'W', 'W'],
                        color_identity=['W'], card_type="Enchantment", sub_types="Saga",
                        abilities=[119071, 26820, 118952], set_id="DAR", rarity="Mythic Rare", set_number=21,
                        mtga_id=67146)
InvoketheDivine = Card(name="invoke_the_divine", pretty_name="Invoke the Divine", cost=['2', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[2813], set_id="DAR", rarity="Common", set_number=22,
                       mtga_id=67148)
KnightofGrace = Card(name="knight_of_grace", pretty_name="Knight of Grace", cost=['1', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                     abilities=[6, 118964, 118970], set_id="DAR", rarity="Uncommon", set_number=23,
                     mtga_id=67150)
KnightofNewBenalia = Card(name="knight_of_new_benalia", pretty_name="Knight of New Benalia", cost=['1', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                          abilities=[], set_id="DAR", rarity="Common", set_number=24,
                          mtga_id=67152)
KwendePrideofFemeref = Card(name="kwende_pride_of_femeref", pretty_name="Kwende, Pride of Femeref", cost=['3', 'W'],
                            color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                            abilities=[3, 1038], set_id="DAR", rarity="Uncommon", set_number=25,
                            mtga_id=67154)
LyraDawnbringer = Card(name="lyra_dawnbringer", pretty_name="Lyra Dawnbringer", cost=['3', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Angel",
                       abilities=[8, 6, 12, 118983], set_id="DAR", rarity="Mythic Rare", set_number=26,
                       mtga_id=67156)
MesaUnicorn = Card(name="mesa_unicorn", pretty_name="Mesa Unicorn", cost=['1', 'W'],
                   color_identity=['W'], card_type="Creature", sub_types="Unicorn",
                   abilities=[12], set_id="DAR", rarity="Common", set_number=27,
                   mtga_id=67158)
OnSerrasWings = Card(name="on_serras_wings", pretty_name="On Serra's Wings", cost=['3', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 118991], set_id="DAR", rarity="Uncommon", set_number=28,
                     mtga_id=67160)
PegasusCourser = Card(name="pegasus_courser", pretty_name="Pegasus Courser", cost=['2', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Pegasus",
                      abilities=[8, 103816], set_id="DAR", rarity="Common", set_number=29,
                      mtga_id=67162)
SanctumSpirit = Card(name="sanctum_spirit", pretty_name="Sanctum Spirit", cost=['3', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Spirit",
                     abilities=[12, 118814], set_id="DAR", rarity="Uncommon", set_number=30,
                     mtga_id=67164)
SealAway = Card(name="seal_away", pretty_name="Seal Away", cost=['1', 'W'],
                color_identity=['W'], card_type="Enchantment", sub_types="",
                abilities=[7, 118824], set_id="DAR", rarity="Uncommon", set_number=31,
                mtga_id=67166)
SergeantatArms = Card(name="sergeantatarms", pretty_name="Sergeant-at-Arms", cost=['2', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                      abilities=[2478, 119011], set_id="DAR", rarity="Common", set_number=32,
                      mtga_id=67168)
SerraAngel = Card(name="serra_angel", pretty_name="Serra Angel", cost=['3', 'W', 'W'],
                  color_identity=['W'], card_type="Creature", sub_types="Angel",
                  abilities=[8, 15], set_id="DAR", rarity="Uncommon", set_number=33,
                  mtga_id=67170)
SerraDisciple = Card(name="serra_disciple", pretty_name="Serra Disciple", cost=['1', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Bird Cleric",
                     abilities=[8, 6, 118831], set_id="DAR", rarity="Common", set_number=34,
                     mtga_id=67172)
ShalaiVoiceofPlenty = Card(name="shalai_voice_of_plenty", pretty_name="Shalai, Voice of Plenty", cost=['3', 'W'],
                           color_identity=['G', 'W'], card_type="Creature", sub_types="Angel",
                           abilities=[8, 118833, 119020], set_id="DAR", rarity="Rare", set_number=35,
                           mtga_id=67174)
TesharAncestorsApostle = Card(name="teshar_ancestors_apostle", pretty_name="Teshar, Ancestor's Apostle", cost=['3', 'W'],
                              color_identity=['W'], card_type="Creature", sub_types="Bird Cleric",
                              abilities=[8, 119024], set_id="DAR", rarity="Rare", set_number=36,
                              mtga_id=67176)
TragicPoet = Card(name="tragic_poet", pretty_name="Tragic Poet", cost=['W'],
                  color_identity=['W'], card_type="Creature", sub_types="Human",
                  abilities=[98492], set_id="DAR", rarity="Common", set_number=37,
                  mtga_id=67178)
TriumphofGerrard = Card(name="triumph_of_gerrard", pretty_name="Triumph of Gerrard", cost=['1', 'W'],
                        color_identity=['W'], card_type="Enchantment", sub_types="Saga",
                        abilities=[119267, 119268, 118841], set_id="DAR", rarity="Uncommon", set_number=38,
                        mtga_id=67180)
UrzasRuinousBlast = Card(name="urzas_ruinous_blast", pretty_name="Urza's Ruinous Blast", cost=['4', 'W'],
                         color_identity=['W'], card_type="Sorcery", sub_types="",
                         abilities=[118845], set_id="DAR", rarity="Rare", set_number=39,
                         mtga_id=67182)
AcademyDrake = Card(name="academy_drake", pretty_name="Academy Drake", cost=['2', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Drake",
                    abilities=[2852, 8, 96521], set_id="DAR", rarity="Common", set_number=40,
                    mtga_id=67184)
AcademyJourneymage = Card(name="academy_journeymage", pretty_name="Academy Journeymage", cost=['4', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                          abilities=[118857, 96307], set_id="DAR", rarity="Common", set_number=41,
                          mtga_id=67186)
TheAntiquitiesWar = Card(name="the_antiquities_war", pretty_name="The Antiquities War", cost=['3', 'U'],
                         color_identity=['U'], card_type="Enchantment", sub_types="Saga",
                         abilities=[119269, 119272, 118868], set_id="DAR", rarity="Rare", set_number=42,
                         mtga_id=67188)
ArcaneFlight = Card(name="arcane_flight", pretty_name="Arcane Flight", cost=['U'],
                    color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1027, 6270], set_id="DAR", rarity="Common", set_number=43,
                    mtga_id=67190)
ArtificersAssistant = Card(name="artificers_assistant", pretty_name="Artificer's Assistant", cost=['U'],
                           color_identity=['U'], card_type="Creature", sub_types="Bird",
                           abilities=[8, 118876], set_id="DAR", rarity="Common", set_number=44,
                           mtga_id=67192)
Befuddle = Card(name="befuddle", pretty_name="Befuddle", cost=['2', 'U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[63602, 25848], set_id="DAR", rarity="Common", set_number=45,
                mtga_id=67194)
BlinkofanEye = Card(name="blink_of_an_eye", pretty_name="Blink of an Eye", cost=['1', 'U'],
                    color_identity=['U'], card_type="Instant", sub_types="",
                    abilities=[2739, 99193], set_id="DAR", rarity="Common", set_number=46,
                    mtga_id=67196)
CloudreaderSphinx = Card(name="cloudreader_sphinx", pretty_name="Cloudreader Sphinx", cost=['4', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                         abilities=[8, 100685], set_id="DAR", rarity="Common", set_number=47,
                         mtga_id=67198)
ColdWaterSnapper = Card(name="coldwater_snapper", pretty_name="Cold-Water Snapper", cost=['5', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Turtle",
                        abilities=[10], set_id="DAR", rarity="Common", set_number=48,
                        mtga_id=67200)
CuratorsWard = Card(name="curators_ward", pretty_name="Curator's Ward", cost=['2', 'U'],
                    color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1420, 118905, 118910], set_id="DAR", rarity="Uncommon", set_number=49,
                    mtga_id=67202)
DeepFreeze = Card(name="deep_freeze", pretty_name="Deep Freeze", cost=['2', 'U'],
                  color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                  abilities=[1027, 118913], set_id="DAR", rarity="Common", set_number=50,
                  mtga_id=67204)
DiligentExcavator = Card(name="diligent_excavator", pretty_name="Diligent Excavator", cost=['1', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                         abilities=[118917], set_id="DAR", rarity="Uncommon", set_number=51,
                         mtga_id=67206)
Divination = Card(name="divination", pretty_name="Divination", cost=['2', 'U'],
                  color_identity=['U'], card_type="Sorcery", sub_types="",
                  abilities=[23607], set_id="DAR", rarity="Common", set_number=52,
                  mtga_id=67208)
HomaridExplorer = Card(name="homarid_explorer", pretty_name="Homarid Explorer", cost=['3', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Homarid Scout",
                       abilities=[100740], set_id="DAR", rarity="Common", set_number=53,
                       mtga_id=67210)
InBolassClutches = Card(name="in_bolass_clutches", pretty_name="In Bolas's Clutches", cost=['4', 'U', 'U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1420, 1421, 118930], set_id="DAR", rarity="Uncommon", set_number=54,
                        mtga_id=67212)
KarnsTemporalSundering = Card(name="karns_temporal_sundering", pretty_name="Karn's Temporal Sundering", cost=['4', 'U', 'U'],
                              color_identity=['U'], card_type="Sorcery", sub_types="",
                              abilities=[118934], set_id="DAR", rarity="Rare", set_number=55,
                              mtga_id=67214)
MerfolkTrickster = Card(name="merfolk_trickster", pretty_name="Merfolk Trickster", cost=['U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                        abilities=[7, 118938], set_id="DAR", rarity="Uncommon", set_number=56,
                        mtga_id=67216)
TheMirariConjecture = Card(name="the_mirari_conjecture", pretty_name="The Mirari Conjecture", cost=['4', 'U'],
                           color_identity=['U'], card_type="Enchantment", sub_types="Saga",
                           abilities=[118939, 118945, 118951], set_id="DAR", rarity="Rare", set_number=57,
                           mtga_id=67218)
NabanDeanofIteration = Card(name="naban_dean_of_iteration", pretty_name="Naban, Dean of Iteration", cost=['1', 'U'],
                            color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                            abilities=[118955], set_id="DAR", rarity="Rare", set_number=58,
                            mtga_id=67220)
NaruMehaMasterWizard = Card(name="naru_meha_master_wizard", pretty_name="Naru Meha, Master Wizard", cost=['2', 'U', 'U'],
                            color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                            abilities=[7, 118956, 118958], set_id="DAR", rarity="Mythic Rare", set_number=59,
                            mtga_id=67222)
Opt = Card(name="opt", pretty_name="Opt", cost=['U'],
           color_identity=['U'], card_type="Instant", sub_types="",
           abilities=[66937, 25848], set_id="DAR", rarity="Common", set_number=60,
           mtga_id=67224)
PrecognitionField = Card(name="precognition_field", pretty_name="Precognition Field", cost=['3', 'U'],
                         color_identity=['U'], card_type="Enchantment", sub_types="",
                         abilities=[14523, 20123, 118960], set_id="DAR", rarity="Rare", set_number=61,
                         mtga_id=67226)
RelicRunner = Card(name="relic_runner", pretty_name="Relic Runner", cost=['1', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Human Rogue",
                   abilities=[118962], set_id="DAR", rarity="Common", set_number=62,
                   mtga_id=67228)
Rescue = Card(name="rescue", pretty_name="Rescue", cost=['U'],
              color_identity=['U'], card_type="Instant", sub_types="",
              abilities=[98407], set_id="DAR", rarity="Common", set_number=63,
              mtga_id=67230)
SageofLatNam = Card(name="sage_of_latnam", pretty_name="Sage of Lat-Nam", cost=['1', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                    abilities=[1716], set_id="DAR", rarity="Uncommon", set_number=64,
                    mtga_id=67232)
SentinelofthePearlTrident = Card(name="sentinel_of_the_pearl_trident", pretty_name="Sentinel of the Pearl Trident", cost=['4', 'U'],
                                 color_identity=['U'], card_type="Creature", sub_types="Merfolk Soldier",
                                 abilities=[7, 118965], set_id="DAR", rarity="Uncommon", set_number=65,
                                 mtga_id=67234)
SlinnVodatheRisingDeep = Card(name="slinn_voda_the_rising_deep", pretty_name="Slinn Voda, the Rising Deep", cost=['6', 'U', 'U'],
                              color_identity=['U'], card_type="Creature", sub_types="Leviathan",
                              abilities=[2739, 118966], set_id="DAR", rarity="Uncommon", set_number=66,
                              mtga_id=67236)
Syncopate = Card(name="syncopate", pretty_name="Syncopate", cost=['X', 'U'],
                 color_identity=['U'], card_type="Instant", sub_types="",
                 abilities=[95637], set_id="DAR", rarity="Common", set_number=67,
                 mtga_id=67238)
TempestDjinn = Card(name="tempest_djinn", pretty_name="Tempest Djinn", cost=['U', 'U', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Djinn",
                    abilities=[8, 118967], set_id="DAR", rarity="Rare", set_number=68,
                    mtga_id=67240)
TetsukoUmezawaFugitive = Card(name="tetsuko_umezawa_fugitive", pretty_name="Tetsuko Umezawa, Fugitive", cost=['1', 'U'],
                              color_identity=['U'], card_type="Creature", sub_types="Human Rogue",
                              abilities=[118969], set_id="DAR", rarity="Uncommon", set_number=69,
                              mtga_id=67242)
TimeofIce = Card(name="time_of_ice", pretty_name="Time of Ice", cost=['3', 'U'],
                 color_identity=['U'], card_type="Enchantment", sub_types="Saga",
                 abilities=[119074, 21742, 118973], set_id="DAR", rarity="Uncommon", set_number=70,
                 mtga_id=67244)
TolarianScholar = Card(name="tolarian_scholar", pretty_name="Tolarian Scholar", cost=['2', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[], set_id="DAR", rarity="Common", set_number=71,
                       mtga_id=67246)
Unwind = Card(name="unwind", pretty_name="Unwind", cost=['2', 'U'],
              color_identity=['U'], card_type="Instant", sub_types="",
              abilities=[118974], set_id="DAR", rarity="Common", set_number=72,
              mtga_id=67248)
VodalianArcanist = Card(name="vodalian_arcanist", pretty_name="Vodalian Arcanist", cost=['1', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                        abilities=[75763], set_id="DAR", rarity="Common", set_number=73,
                        mtga_id=67250)
WeightofMemory = Card(name="weight_of_memory", pretty_name="Weight of Memory", cost=['3', 'U', 'U'],
                      color_identity=['U'], card_type="Sorcery", sub_types="",
                      abilities=[20379], set_id="DAR", rarity="Uncommon", set_number=74,
                      mtga_id=67252)
WizardsRetort = Card(name="wizards_retort", pretty_name="Wizard's Retort", cost=['1', 'U', 'U'],
                     color_identity=['U'], card_type="Instant", sub_types="",
                     abilities=[118857, 25846], set_id="DAR", rarity="Uncommon", set_number=75,
                     mtga_id=67254)
ZahidDjinnoftheLamp = Card(name="zahid_djinn_of_the_lamp", pretty_name="Zahid, Djinn of the Lamp", cost=['4', 'U', 'U'],
                           color_identity=['U'], card_type="Creature", sub_types="Djinn",
                           abilities=[118980, 8], set_id="DAR", rarity="Rare", set_number=76,
                           mtga_id=67256)
BlessingofBelzenlok = Card(name="blessing_of_belzenlok", pretty_name="Blessing of Belzenlok", cost=['B'],
                           color_identity=['B'], card_type="Instant", sub_types="",
                           abilities=[118981], set_id="DAR", rarity="Common", set_number=77,
                           mtga_id=67258)
CabalEvangel = Card(name="cabal_evangel", pretty_name="Cabal Evangel", cost=['1', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Human Cleric",
                    abilities=[], set_id="DAR", rarity="Common", set_number=78,
                    mtga_id=67260)
CabalPaladin = Card(name="cabal_paladin", pretty_name="Cabal Paladin", cost=['3', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Human Knight",
                    abilities=[118982], set_id="DAR", rarity="Common", set_number=79,
                    mtga_id=67262)
CaligoSkinWitch = Card(name="caligo_skinwitch", pretty_name="Caligo Skin-Witch", cost=['1', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[10662, 118985], set_id="DAR", rarity="Common", set_number=80,
                       mtga_id=67264)
CastDown = Card(name="cast_down", pretty_name="Cast Down", cost=['1', 'B'],
                color_identity=['B'], card_type="Instant", sub_types="",
                abilities=[118987], set_id="DAR", rarity="Uncommon", set_number=81,
                mtga_id=67266)
ChainersTorment = Card(name="chainers_torment", pretty_name="Chainer's Torment", cost=['3', 'B'],
                       color_identity=['B'], card_type="Enchantment", sub_types="Saga",
                       abilities=[119079, 119080, 118989], set_id="DAR", rarity="Uncommon", set_number=82,
                       mtga_id=67268)
DarkBargain = Card(name="dark_bargain", pretty_name="Dark Bargain", cost=['3', 'B'],
                   color_identity=['B'], card_type="Instant", sub_types="",
                   abilities=[118990], set_id="DAR", rarity="Common", set_number=83,
                   mtga_id=67270)
DeathbloomThallid = Card(name="deathbloom_thallid", pretty_name="Deathbloom Thallid", cost=['2', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Fungus",
                         abilities=[90362], set_id="DAR", rarity="Common", set_number=84,
                         mtga_id=67272)
DemonicVigor = Card(name="demonic_vigor", pretty_name="Demonic Vigor", cost=['B'],
                    color_identity=['B'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1027, 3974, 89217], set_id="DAR", rarity="Common", set_number=85,
                    mtga_id=67274)
DemonlordBelzenlok = Card(name="demonlord_belzenlok", pretty_name="Demonlord Belzenlok", cost=['4', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Elder Demon",
                          abilities=[8, 14, 118994], set_id="DAR", rarity="Mythic Rare", set_number=86,
                          mtga_id=67276)
Divest = Card(name="divest", pretty_name="Divest", cost=['B'],
              color_identity=['B'], card_type="Sorcery", sub_types="",
              abilities=[118995], set_id="DAR", rarity="Common", set_number=87,
              mtga_id=67278)
DreadShade = Card(name="dread_shade", pretty_name="Dread Shade", cost=['B', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Shade",
                  abilities=[1162], set_id="DAR", rarity="Rare", set_number=88,
                  mtga_id=67280)
DrudgeSentinel = Card(name="drudge_sentinel", pretty_name="Drudge Sentinel", cost=['2', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Skeleton Warrior",
                      abilities=[118996], set_id="DAR", rarity="Common", set_number=89,
                      mtga_id=67282)
TheEldestReborn = Card(name="the_eldest_reborn", pretty_name="The Eldest Reborn", cost=['4', 'B'],
                       color_identity=['B'], card_type="Enchantment", sub_types="Saga",
                       abilities=[118998, 119000, 119001], set_id="DAR", rarity="Uncommon", set_number=90,
                       mtga_id=67284)
Eviscerate = Card(name="eviscerate", pretty_name="Eviscerate", cost=['3', 'B'],
                  color_identity=['B'], card_type="Sorcery", sub_types="",
                  abilities=[26818], set_id="DAR", rarity="Common", set_number=91,
                  mtga_id=67286)
FeralAbomination = Card(name="feral_abomination", pretty_name="Feral Abomination", cost=['5', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Thrull",
                        abilities=[1], set_id="DAR", rarity="Common", set_number=92,
                        mtga_id=67288)
FinalParting = Card(name="final_parting", pretty_name="Final Parting", cost=['3', 'B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[119002], set_id="DAR", rarity="Uncommon", set_number=93,
                    mtga_id=67290)
FungalInfection = Card(name="fungal_infection", pretty_name="Fungal Infection", cost=['B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[119003], set_id="DAR", rarity="Common", set_number=94,
                       mtga_id=67292)
JosuVessLichKnight = Card(name="josu_vess_lich_knight", pretty_name="Josu Vess, Lich Knight", cost=['2', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Zombie Knight",
                          abilities=[119004, 142, 119005], set_id="DAR", rarity="Rare", set_number=95,
                          mtga_id=67294)
KazarovSengirPureblood = Card(name="kazarov_sengir_pureblood", pretty_name="Kazarov, Sengir Pureblood", cost=['5', 'B', 'B'],
                              color_identity=['R', 'B'], card_type="Creature", sub_types="Vampire",
                              abilities=[8, 119006, 119007], set_id="DAR", rarity="Rare", set_number=96,
                              mtga_id=67296)
KnightofMalice = Card(name="knight_of_malice", pretty_name="Knight of Malice", cost=['1', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Human Knight",
                      abilities=[6, 119008, 119009], set_id="DAR", rarity="Uncommon", set_number=97,
                      mtga_id=67298)
LichsMastery = Card(name="lichs_mastery", pretty_name="Lich's Mastery", cost=['3', 'B', 'B', 'B'],
                    color_identity=['B'], card_type="Enchantment", sub_types="",
                    abilities=[10, 118816, 118817, 118818, 16132], set_id="DAR", rarity="Rare", set_number=98,
                    mtga_id=67300)
LingeringPhantom = Card(name="lingering_phantom", pretty_name="Lingering Phantom", cost=['5', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Spirit",
                        abilities=[118819], set_id="DAR", rarity="Uncommon", set_number=99,
                        mtga_id=67302)
PhyrexianScriptures = Card(name="phyrexian_scriptures", pretty_name="Phyrexian Scriptures", cost=['2', 'B', 'B'],
                           color_identity=['B'], card_type="Enchantment", sub_types="Saga",
                           abilities=[118820, 118821, 118822], set_id="DAR", rarity="Mythic Rare", set_number=100,
                           mtga_id=67304)
RatColony = Card(name="rat_colony", pretty_name="Rat Colony", cost=['1', 'B'],
                 color_identity=['B'], card_type="Creature", sub_types="Rat",
                 abilities=[118823, 88192], set_id="DAR", rarity="Common", set_number=101,
                 mtga_id=67306)
RiteofBelzenlok = Card(name="rite_of_belzenlok", pretty_name="Rite of Belzenlok", cost=['2', 'B', 'B'],
                       color_identity=['B'], card_type="Enchantment", sub_types="Saga",
                       abilities=[119276, 119277, 118827], set_id="DAR", rarity="Rare", set_number=102,
                       mtga_id=67308)
SettletheScore = Card(name="settle_the_score", pretty_name="Settle the Score", cost=['2', 'B', 'B'],
                      color_identity=['B'], card_type="Sorcery", sub_types="",
                      abilities=[118828], set_id="DAR", rarity="Uncommon", set_number=103,
                      mtga_id=67310)
SoulSalvage = Card(name="soul_salvage", pretty_name="Soul Salvage", cost=['2', 'B'],
                   color_identity=['B'], card_type="Sorcery", sub_types="",
                   abilities=[1923], set_id="DAR", rarity="Common", set_number=104,
                   mtga_id=67312)
StrongholdConfessor = Card(name="stronghold_confessor", pretty_name="Stronghold Confessor", cost=['B'],
                           color_identity=['B'], card_type="Creature", sub_types="Human Cleric",
                           abilities=[2817, 142, 96521], set_id="DAR", rarity="Common", set_number=105,
                           mtga_id=67314)
ThallidOmnivore = Card(name="thallid_omnivore", pretty_name="Thallid Omnivore", cost=['3', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Fungus",
                       abilities=[119014], set_id="DAR", rarity="Common", set_number=106,
                       mtga_id=67316)
ThallidSoothsayer = Card(name="thallid_soothsayer", pretty_name="Thallid Soothsayer", cost=['3', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Fungus",
                         abilities=[119015], set_id="DAR", rarity="Uncommon", set_number=107,
                         mtga_id=67318)
TorgaarFamineIncarnate = Card(name="torgaar_famine_incarnate", pretty_name="Torgaar, Famine Incarnate", cost=['6', 'B', 'B'],
                              color_identity=['B'], card_type="Creature", sub_types="Avatar",
                              abilities=[119016, 119018], set_id="DAR", rarity="Rare", set_number=108,
                              mtga_id=67320)
UrgorostheEmptyOne = Card(name="urgoros_the_empty_one", pretty_name="Urgoros, the Empty One", cost=['4', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Specter",
                          abilities=[8, 119019], set_id="DAR", rarity="Uncommon", set_number=109,
                          mtga_id=67322)
ViciousOffering = Card(name="vicious_offering", pretty_name="Vicious Offering", cost=['1', 'B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[96532, 119021], set_id="DAR", rarity="Common", set_number=110,
                       mtga_id=67324)
WhisperBloodLiturgist = Card(name="whisper_blood_liturgist", pretty_name="Whisper, Blood Liturgist", cost=['3', 'B'],
                             color_identity=['B'], card_type="Creature", sub_types="Human Cleric",
                             abilities=[119022], set_id="DAR", rarity="Uncommon", set_number=111,
                             mtga_id=67326)
WindgraceAcolyte = Card(name="windgrace_acolyte", pretty_name="Windgrace Acolyte", cost=['4', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Cat Warrior",
                        abilities=[8, 119023], set_id="DAR", rarity="Common", set_number=112,
                        mtga_id=67328)
YargleGluttonofUrborg = Card(name="yargle_glutton_of_urborg", pretty_name="Yargle, Glutton of Urborg", cost=['4', 'B'],
                             color_identity=['B'], card_type="Creature", sub_types="Frog Spirit",
                             abilities=[], set_id="DAR", rarity="Uncommon", set_number=113,
                             mtga_id=67330)
YawgmothsVileOffering = Card(name="yawgmoths_vile_offering", pretty_name="Yawgmoth's Vile Offering", cost=['4', 'B'],
                             color_identity=['B'], card_type="Sorcery", sub_types="",
                             abilities=[118829], set_id="DAR", rarity="Rare", set_number=114,
                             mtga_id=67332)
BloodstoneGoblin = Card(name="bloodstone_goblin", pretty_name="Bloodstone Goblin", cost=['1', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                        abilities=[118830], set_id="DAR", rarity="Common", set_number=115,
                        mtga_id=67334)
ChampionoftheFlame = Card(name="champion_of_the_flame", pretty_name="Champion of the Flame", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                          abilities=[14, 119025], set_id="DAR", rarity="Uncommon", set_number=116,
                          mtga_id=67336)
FerventStrike = Card(name="fervent_strike", pretty_name="Fervent Strike", cost=['R'],
                     color_identity=['R'], card_type="Instant", sub_types="",
                     abilities=[119026], set_id="DAR", rarity="Common", set_number=117,
                     mtga_id=67338)
FieryIntervention = Card(name="fiery_intervention", pretty_name="Fiery Intervention", cost=['4', 'R'],
                         color_identity=['R'], card_type="Sorcery", sub_types="",
                         abilities=[119027], set_id="DAR", rarity="Common", set_number=118,
                         mtga_id=67340)
FightwithFire = Card(name="fight_with_fire", pretty_name="Fight with Fire", cost=['2', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[118832, 119028], set_id="DAR", rarity="Uncommon", set_number=119,
                     mtga_id=67342)
FireElemental = Card(name="fire_elemental", pretty_name="Fire Elemental", cost=['3', 'R', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Elemental",
                     abilities=[], set_id="DAR", rarity="Common", set_number=120,
                     mtga_id=67344)
FirefistAdept = Card(name="firefist_adept", pretty_name="Firefist Adept", cost=['4', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Human Wizard",
                     abilities=[118834], set_id="DAR", rarity="Uncommon", set_number=121,
                     mtga_id=67346)
TheFirstEruption = Card(name="the_first_eruption", pretty_name="The First Eruption", cost=['2', 'R'],
                        color_identity=['R'], card_type="Enchantment", sub_types="Saga",
                        abilities=[118835, 119029, 119031], set_id="DAR", rarity="Rare", set_number=122,
                        mtga_id=67348)
TheFlameofKeld = Card(name="the_flame_of_keld", pretty_name="The Flame of Keld", cost=['1', 'R'],
                      color_identity=['R'], card_type="Enchantment", sub_types="Saga",
                      abilities=[119032, 119033, 118836], set_id="DAR", rarity="Uncommon", set_number=123,
                      mtga_id=67350)
FrenziedRage = Card(name="frenzied_rage", pretty_name="Frenzied Rage", cost=['1', 'R'],
                    color_identity=['R'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1027, 62540], set_id="DAR", rarity="Common", set_number=124,
                    mtga_id=67352)
GhituChronicler = Card(name="ghitu_chronicler", pretty_name="Ghitu Chronicler", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[14490, 119035], set_id="DAR", rarity="Common", set_number=125,
                       mtga_id=67354)
GhituJourneymage = Card(name="ghitu_journeymage", pretty_name="Ghitu Journeymage", cost=['2', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Human Wizard",
                        abilities=[118975], set_id="DAR", rarity="Common", set_number=126,
                        mtga_id=67356)
GhituLavarunner = Card(name="ghitu_lavarunner", pretty_name="Ghitu Lavarunner", cost=['R'],
                       color_identity=['R'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[119036], set_id="DAR", rarity="Common", set_number=127,
                       mtga_id=67358)
GoblinBarrage = Card(name="goblin_barrage", pretty_name="Goblin Barrage", cost=['3', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[119037, 119038], set_id="DAR", rarity="Uncommon", set_number=128,
                     mtga_id=67360)
GoblinChainwhirler = Card(name="goblin_chainwhirler", pretty_name="Goblin Chainwhirler", cost=['R', 'R', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                          abilities=[6, 119039], set_id="DAR", rarity="Rare", set_number=129,
                          mtga_id=67362)
GoblinWarchief = Card(name="goblin_warchief", pretty_name="Goblin Warchief", cost=['1', 'R', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                      abilities=[2045, 2046], set_id="DAR", rarity="Uncommon", set_number=130,
                      mtga_id=67364)
HaphazardBombardment = Card(name="haphazard_bombardment", pretty_name="Haphazard Bombardment", cost=['5', 'R'],
                            color_identity=['R'], card_type="Enchantment", sub_types="",
                            abilities=[119040, 119041], set_id="DAR", rarity="Rare", set_number=131,
                            mtga_id=67366)
JayaBallard = Card(name="jaya_ballard", pretty_name="Jaya Ballard", cost=['2', 'R', 'R', 'R'],
                   color_identity=['R'], card_type="Planeswalker", sub_types="Jaya",
                   abilities=[119042, 119043, 119046], set_id="DAR", rarity="Mythic Rare", set_number=132,
                   mtga_id=67368)
JayasImmolatingInferno = Card(name="jayas_immolating_inferno", pretty_name="Jaya's Immolating Inferno", cost=['X', 'R', 'R'],
                              color_identity=['R'], card_type="Sorcery", sub_types="",
                              abilities=[119047], set_id="DAR", rarity="Rare", set_number=133,
                              mtga_id=67370)
KeldonOverseer = Card(name="keldon_overseer", pretty_name="Keldon Overseer", cost=['2', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                      abilities=[14490, 9, 119048], set_id="DAR", rarity="Common", set_number=134,
                      mtga_id=67372)
KeldonRaider = Card(name="keldon_raider", pretty_name="Keldon Raider", cost=['2', 'R', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                    abilities=[100041], set_id="DAR", rarity="Common", set_number=135,
                    mtga_id=67374)
KeldonWarcaller = Card(name="keldon_warcaller", pretty_name="Keldon Warcaller", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                       abilities=[118838], set_id="DAR", rarity="Common", set_number=136,
                       mtga_id=67376)
OrcishVandal = Card(name="orcish_vandal", pretty_name="Orcish Vandal", cost=['1', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Orc Warrior",
                    abilities=[93267], set_id="DAR", rarity="Uncommon", set_number=137,
                    mtga_id=67378)
RadiatingLightning = Card(name="radiating_lightning", pretty_name="Radiating Lightning", cost=['3', 'R'],
                          color_identity=['R'], card_type="Instant", sub_types="",
                          abilities=[118840], set_id="DAR", rarity="Common", set_number=138,
                          mtga_id=67380)
RampagingCyclops = Card(name="rampaging_cyclops", pretty_name="Rampaging Cyclops", cost=['3', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Cyclops",
                        abilities=[119056], set_id="DAR", rarity="Common", set_number=139,
                        mtga_id=67382)
RunAmok = Card(name="run_amok", pretty_name="Run Amok", cost=['1', 'R'],
               color_identity=['R'], card_type="Instant", sub_types="",
               abilities=[118842], set_id="DAR", rarity="Common", set_number=140,
               mtga_id=67384)
SeismicShift = Card(name="seismic_shift", pretty_name="Seismic Shift", cost=['3', 'R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[118843], set_id="DAR", rarity="Common", set_number=141,
                    mtga_id=67386)
ShivanFire = Card(name="shivan_fire", pretty_name="Shivan Fire", cost=['R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[2852, 118844], set_id="DAR", rarity="Common", set_number=142,
                  mtga_id=67388)
SiegeGangCommander = Card(name="siegegang_commander", pretty_name="Siege-Gang Commander", cost=['3', 'R', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Goblin",
                          abilities=[2076, 2077], set_id="DAR", rarity="Rare", set_number=143,
                          mtga_id=67390)
SkirkProspector = Card(name="skirk_prospector", pretty_name="Skirk Prospector", cost=['R'],
                       color_identity=['R'], card_type="Creature", sub_types="Goblin",
                       abilities=[2429], set_id="DAR", rarity="Common", set_number=144,
                       mtga_id=67392)
Skizzik = Card(name="skizzik", pretty_name="Skizzik", cost=['3', 'R'],
               color_identity=['R'], card_type="Creature", sub_types="Elemental",
               abilities=[1876, 14, 9, 92187], set_id="DAR", rarity="Uncommon", set_number=145,
               mtga_id=67394)
SqueetheImmortal = Card(name="squee_the_immortal", pretty_name="Squee, the Immortal", cost=['1', 'R', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Goblin",
                        abilities=[118846], set_id="DAR", rarity="Rare", set_number=146,
                        mtga_id=67396)
TwoHeadedGiant = Card(name="twoheaded_giant", pretty_name="Two-Headed Giant", cost=['2', 'R', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Giant Warrior",
                      abilities=[118847], set_id="DAR", rarity="Rare", set_number=147,
                      mtga_id=67398)
ValdukKeeperoftheFlame = Card(name="valduk_keeper_of_the_flame", pretty_name="Valduk, Keeper of the Flame", cost=['2', 'R'],
                              color_identity=['R'], card_type="Creature", sub_types="Human Shaman",
                              abilities=[118848], set_id="DAR", rarity="Uncommon", set_number=148,
                              mtga_id=67400)
VerixBladewing = Card(name="verix_bladewing", pretty_name="Verix Bladewing", cost=['2', 'R', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Dragon",
                      abilities=[2817, 8, 1205], set_id="DAR", rarity="Mythic Rare", set_number=149,
                      mtga_id=67402)
WarcryPhoenix = Card(name="warcry_phoenix", pretty_name="Warcry Phoenix", cost=['3', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Phoenix",
                     abilities=[8, 9, 118849], set_id="DAR", rarity="Uncommon", set_number=150,
                     mtga_id=67404)
WarlordsFury = Card(name="warlords_fury", pretty_name="Warlord's Fury", cost=['R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[26886, 25848], set_id="DAR", rarity="Common", set_number=151,
                    mtga_id=67406)
WizardsLightning = Card(name="wizards_lightning", pretty_name="Wizard's Lightning", cost=['2', 'R'],
                        color_identity=['R'], card_type="Instant", sub_types="",
                        abilities=[118850, 70361], set_id="DAR", rarity="Uncommon", set_number=152,
                        mtga_id=67408)
AdventurousImpulse = Card(name="adventurous_impulse", pretty_name="Adventurous Impulse", cost=['G'],
                          color_identity=['G'], card_type="Sorcery", sub_types="",
                          abilities=[118851], set_id="DAR", rarity="Common", set_number=153,
                          mtga_id=67410)
AncientAnimus = Card(name="ancient_animus", pretty_name="Ancient Animus", cost=['1', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[118993], set_id="DAR", rarity="Common", set_number=154,
                     mtga_id=67412)
ArborArmament = Card(name="arbor_armament", pretty_name="Arbor Armament", cost=['G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[118997], set_id="DAR", rarity="Common", set_number=155,
                     mtga_id=67414)
BalothGorger = Card(name="baloth_gorger", pretty_name="Baloth Gorger", cost=['2', 'G', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Beast",
                    abilities=[2852, 118853], set_id="DAR", rarity="Common", set_number=156,
                    mtga_id=67416)
BrokenBond = Card(name="broken_bond", pretty_name="Broken Bond", cost=['1', 'G'],
                  color_identity=['G'], card_type="Sorcery", sub_types="",
                  abilities=[118854], set_id="DAR", rarity="Common", set_number=157,
                  mtga_id=67418)
CorrosiveOoze = Card(name="corrosive_ooze", pretty_name="Corrosive Ooze", cost=['1', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Ooze",
                     abilities=[118855], set_id="DAR", rarity="Common", set_number=158,
                     mtga_id=67420)
ElfhameDruid = Card(name="elfhame_druid", pretty_name="Elfhame Druid", cost=['1', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                    abilities=[1005, 119013], set_id="DAR", rarity="Uncommon", set_number=159,
                    mtga_id=67422)
FungalPlots = Card(name="fungal_plots", pretty_name="Fungal Plots", cost=['1', 'G'],
                   color_identity=['G'], card_type="Enchantment", sub_types="",
                   abilities=[118858, 118859], set_id="DAR", rarity="Uncommon", set_number=160,
                   mtga_id=67424)
GaeasBlessing = Card(name="gaeas_blessing", pretty_name="Gaea's Blessing", cost=['1', 'G'],
                     color_identity=['G'], card_type="Sorcery", sub_types="",
                     abilities=[12792, 25848, 95093], set_id="DAR", rarity="Uncommon", set_number=161,
                     mtga_id=67426)
GaeasProtector = Card(name="gaeas_protector", pretty_name="Gaea's Protector", cost=['3', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Elemental Warrior",
                      abilities=[96651], set_id="DAR", rarity="Common", set_number=162,
                      mtga_id=67428)
GiftofGrowth = Card(name="gift_of_growth", pretty_name="Gift of Growth", cost=['1', 'G'],
                    color_identity=['G'], card_type="Instant", sub_types="",
                    abilities=[2465, 118860], set_id="DAR", rarity="Common", set_number=163,
                    mtga_id=67430)
GrowfromtheAshes = Card(name="grow_from_the_ashes", pretty_name="Grow from the Ashes", cost=['2', 'G'],
                        color_identity=['G'], card_type="Sorcery", sub_types="",
                        abilities=[2465, 118861], set_id="DAR", rarity="Common", set_number=164,
                        mtga_id=67432)
GrunntheLonelyKing = Card(name="grunn_the_lonely_king", pretty_name="Grunn, the Lonely King", cost=['4', 'G', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Ape Warrior",
                          abilities=[2817, 92093, 1227], set_id="DAR", rarity="Uncommon", set_number=165,
                          mtga_id=67434)
KamahlsDruidicVow = Card(name="kamahls_druidic_vow", pretty_name="Kamahl's Druidic Vow", cost=['X', 'G', 'G'],
                         color_identity=['G'], card_type="Sorcery", sub_types="",
                         abilities=[118862], set_id="DAR", rarity="Rare", set_number=166,
                         mtga_id=67436)
KrosanDruid = Card(name="krosan_druid", pretty_name="Krosan Druid", cost=['2', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Centaur Druid",
                   abilities=[118865, 118864], set_id="DAR", rarity="Common", set_number=167,
                   mtga_id=67438)
LlanowarElves = Card(name="llanowar_elves", pretty_name="Llanowar Elves", cost=['G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                     abilities=[1005], set_id="DAR", rarity="Common", set_number=168,
                     mtga_id=67440)
LlanowarEnvoy = Card(name="llanowar_envoy", pretty_name="Llanowar Envoy", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                     abilities=[2410], set_id="DAR", rarity="Common", set_number=169,
                     mtga_id=67442)
LlanowarScout = Card(name="llanowar_scout", pretty_name="Llanowar Scout", cost=['1', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                     abilities=[6425], set_id="DAR", rarity="Common", set_number=170,
                     mtga_id=67444)
MammothSpider = Card(name="mammoth_spider", pretty_name="Mammoth Spider", cost=['4', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Spider",
                     abilities=[13], set_id="DAR", rarity="Common", set_number=171,
                     mtga_id=67446)
MarwyntheNurturer = Card(name="marwyn_the_nurturer", pretty_name="Marwyn, the Nurturer", cost=['2', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                         abilities=[118866, 118867], set_id="DAR", rarity="Rare", set_number=172,
                         mtga_id=67448)
TheMendingofDominaria = Card(name="the_mending_of_dominaria", pretty_name="The Mending of Dominaria", cost=['3', 'G', 'G'],
                             color_identity=['G'], card_type="Enchantment", sub_types="Saga",
                             abilities=[119273, 119274, 118869], set_id="DAR", rarity="Rare", set_number=173,
                             mtga_id=67450)
MultaniYavimayasAvatar = Card(name="multani_yavimayas_avatar", pretty_name="Multani, Yavimaya's Avatar", cost=['4', 'G', 'G'],
                              color_identity=['G'], card_type="Creature", sub_types="Elemental Avatar",
                              abilities=[13, 14, 118870, 118871], set_id="DAR", rarity="Mythic Rare", set_number=174,
                              mtga_id=67452)
NaturesSpiral = Card(name="natures_spiral", pretty_name="Nature's Spiral", cost=['1', 'G'],
                     color_identity=['G'], card_type="Sorcery", sub_types="",
                     abilities=[2938], set_id="DAR", rarity="Uncommon", set_number=175,
                     mtga_id=67454)
PiercetheSky = Card(name="pierce_the_sky", pretty_name="Pierce the Sky", cost=['1', 'G'],
                    color_identity=['G'], card_type="Instant", sub_types="",
                    abilities=[100814], set_id="DAR", rarity="Common", set_number=176,
                    mtga_id=67456)
PrimordialWurm = Card(name="primordial_wurm", pretty_name="Primordial Wurm", cost=['4', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Wurm",
                      abilities=[], set_id="DAR", rarity="Common", set_number=177,
                      mtga_id=67458)
SaprolingMigration = Card(name="saproling_migration", pretty_name="Saproling Migration", cost=['1', 'G'],
                          color_identity=['G'], card_type="Sorcery", sub_types="",
                          abilities=[2852, 118915], set_id="DAR", rarity="Common", set_number=178,
                          mtga_id=67460)
SongofFreyalise = Card(name="song_of_freyalise", pretty_name="Song of Freyalise", cost=['1', 'G'],
                       color_identity=['G'], card_type="Enchantment", sub_types="Saga",
                       abilities=[119270, 119271, 118874], set_id="DAR", rarity="Uncommon", set_number=179,
                       mtga_id=67462)
SporeSwarm = Card(name="spore_swarm", pretty_name="Spore Swarm", cost=['3', 'G'],
                  color_identity=['G'], card_type="Instant", sub_types="",
                  abilities=[24741], set_id="DAR", rarity="Uncommon", set_number=180,
                  mtga_id=67464)
SporecrownThallid = Card(name="sporecrown_thallid", pretty_name="Sporecrown Thallid", cost=['1', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Fungus",
                         abilities=[118875], set_id="DAR", rarity="Uncommon", set_number=181,
                         mtga_id=67466)
SteelLeafChampion = Card(name="steel_leaf_champion", pretty_name="Steel Leaf Champion", cost=['G', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Knight",
                         abilities=[87941], set_id="DAR", rarity="Rare", set_number=182,
                         mtga_id=67468)
SylvanAwakening = Card(name="sylvan_awakening", pretty_name="Sylvan Awakening", cost=['2', 'G'],
                       color_identity=['G'], card_type="Sorcery", sub_types="",
                       abilities=[1248], set_id="DAR", rarity="Rare", set_number=183,
                       mtga_id=67470)
TerritorialAllosaurus = Card(name="territorial_allosaurus", pretty_name="Territorial Allosaurus", cost=['2', 'G', 'G'],
                             color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                             abilities=[2722, 118877], set_id="DAR", rarity="Rare", set_number=184,
                             mtga_id=67472)
ThornElemental = Card(name="thorn_elemental", pretty_name="Thorn Elemental", cost=['5', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Elemental",
                      abilities=[88255], set_id="DAR", rarity="Uncommon", set_number=185,
                      mtga_id=67474)
UntamedKavu = Card(name="untamed_kavu", pretty_name="Untamed Kavu", cost=['1', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Kavu",
                   abilities=[2817, 15, 14, 118853], set_id="DAR", rarity="Uncommon", set_number=186,
                   mtga_id=67476)
VerdantForce = Card(name="verdant_force", pretty_name="Verdant Force", cost=['5', 'G', 'G', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Elemental",
                    abilities=[2640], set_id="DAR", rarity="Rare", set_number=187,
                    mtga_id=67478)
WildOnslaught = Card(name="wild_onslaught", pretty_name="Wild Onslaught", cost=['3', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[2852, 118957], set_id="DAR", rarity="Uncommon", set_number=188,
                     mtga_id=67480)
YavimayaSapherd = Card(name="yavimaya_sapherd", pretty_name="Yavimaya Sapherd", cost=['2', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Fungus",
                       abilities=[118878], set_id="DAR", rarity="Common", set_number=189,
                       mtga_id=67482)
AdeliztheCinderWind = Card(name="adeliz_the_cinder_wind", pretty_name="Adeliz, the Cinder Wind", cost=['1', 'U', 'R'],
                           color_identity=['U', 'R'], card_type="Creature", sub_types="Human Wizard",
                           abilities=[8, 9, 118879], set_id="DAR", rarity="Uncommon", set_number=190,
                           mtga_id=67484)
ArvadtheCursed = Card(name="arvad_the_cursed", pretty_name="Arvad the Cursed", cost=['3', 'W', 'B'],
                      color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire Knight",
                      abilities=[1, 12, 118880], set_id="DAR", rarity="Uncommon", set_number=191,
                      mtga_id=67486)
AryelKnightofWindgrace = Card(name="aryel_knight_of_windgrace", pretty_name="Aryel, Knight of Windgrace", cost=['2', 'W', 'B'],
                              color_identity=['W', 'B'], card_type="Creature", sub_types="Human Knight",
                              abilities=[15, 118881, 118882], set_id="DAR", rarity="Rare", set_number=192,
                              mtga_id=67488)
DarigaazReincarnated = Card(name="darigaaz_reincarnated", pretty_name="Darigaaz Reincarnated", cost=['4', 'B', 'R', 'G'],
                            color_identity=['B', 'R', 'G'], card_type="Creature", sub_types="Dragon",
                            abilities=[8, 14, 9, 118963, 118883], set_id="DAR", rarity="Mythic Rare", set_number=193,
                            mtga_id=67490)
GarnatheBloodflame = Card(name="garna_the_bloodflame", pretty_name="Garna, the Bloodflame", cost=['3', 'B', 'R'],
                          color_identity=['B', 'R'], card_type="Creature", sub_types="Human Warrior",
                          abilities=[7, 118884, 61135], set_id="DAR", rarity="Uncommon", set_number=194,
                          mtga_id=67492)
GrandWarlordRadha = Card(name="grand_warlord_radha", pretty_name="Grand Warlord Radha", cost=['2', 'R', 'G'],
                         color_identity=['R', 'G'], card_type="Creature", sub_types="Elf Warrior",
                         abilities=[9, 118885], set_id="DAR", rarity="Rare", set_number=195,
                         mtga_id=67494)
HallartheFirefletcher = Card(name="hallar_the_firefletcher", pretty_name="Hallar, the Firefletcher", cost=['1', 'R', 'G'],
                             color_identity=['R', 'G'], card_type="Creature", sub_types="Elf Archer",
                             abilities=[14, 118886], set_id="DAR", rarity="Uncommon", set_number=196,
                             mtga_id=67496)
JhoiraWeatherlightCaptain = Card(name="jhoira_weatherlight_captain", pretty_name="Jhoira, Weatherlight Captain", cost=['2', 'U', 'R'],
                                 color_identity=['U', 'R'], card_type="Creature", sub_types="Human Artificer",
                                 abilities=[118968], set_id="DAR", rarity="Mythic Rare", set_number=197,
                                 mtga_id=67498)
JodahArchmageEternal = Card(name="jodah_archmage_eternal", pretty_name="Jodah, Archmage Eternal", cost=['1', 'U', 'R', 'W'],
                            color_identity=['W', 'U', 'B', 'R', 'G'], card_type="Creature", sub_types="Human Wizard",
                            abilities=[8, 7022], set_id="DAR", rarity="Rare", set_number=198,
                            mtga_id=67500)
MuldrothatheGravetide = Card(name="muldrotha_the_gravetide", pretty_name="Muldrotha, the Gravetide", cost=['3', 'B', 'G', 'U'],
                             color_identity=['U', 'B', 'G'], card_type="Creature", sub_types="Elemental Avatar",
                             abilities=[118972], set_id="DAR", rarity="Mythic Rare", set_number=199,
                             mtga_id=67502)
OathofTeferi = Card(name="oath_of_teferi", pretty_name="Oath of Teferi", cost=['3', 'W', 'U'],
                    color_identity=['W', 'U'], card_type="Enchantment", sub_types="",
                    abilities=[118888, 118889], set_id="DAR", rarity="Rare", set_number=200,
                    mtga_id=67504)
PrimevalsGloriousRebirth = Card(name="primevals_glorious_rebirth", pretty_name="Primevals' Glorious Rebirth", cost=['5', 'W', 'B'],
                                color_identity=['W', 'B'], card_type="Sorcery", sub_types="",
                                abilities=[118890], set_id="DAR", rarity="Rare", set_number=201,
                                mtga_id=67506)
RaffCapashenShipsMage = Card(name="raff_capashen_ships_mage", pretty_name="Raff Capashen, Ship's Mage", cost=['2', 'W', 'U'],
                             color_identity=['W', 'U'], card_type="Creature", sub_types="Human Wizard",
                             abilities=[7, 8, 118978], set_id="DAR", rarity="Uncommon", set_number=202,
                             mtga_id=67508)
RonaDiscipleofGix = Card(name="rona_disciple_of_gix", pretty_name="Rona, Disciple of Gix", cost=['1', 'U', 'B'],
                         color_identity=['U', 'B'], card_type="Creature", sub_types="Human Artificer",
                         abilities=[118979, 118892, 118893], set_id="DAR", rarity="Uncommon", set_number=203,
                         mtga_id=67510)
ShannaSisaysLegacy = Card(name="shanna_sisays_legacy", pretty_name="Shanna, Sisay's Legacy", cost=['G', 'W'],
                          color_identity=['G', 'W'], card_type="Creature", sub_types="Human Warrior",
                          abilities=[118894, 118895], set_id="DAR", rarity="Uncommon", set_number=204,
                          mtga_id=67512)
SlimefoottheStowaway = Card(name="slimefoot_the_stowaway", pretty_name="Slimefoot, the Stowaway", cost=['1', 'B', 'G'],
                            color_identity=['B', 'G'], card_type="Creature", sub_types="Fungus",
                            abilities=[118986, 118896], set_id="DAR", rarity="Uncommon", set_number=205,
                            mtga_id=67514)
TatyovaBenthicDruid = Card(name="tatyova_benthic_druid", pretty_name="Tatyova, Benthic Druid", cost=['3', 'G', 'U'],
                           color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Druid",
                           abilities=[118897], set_id="DAR", rarity="Uncommon", set_number=206,
                           mtga_id=67516)
TeferiHeroofDominaria = Card(name="teferi_hero_of_dominaria", pretty_name="Teferi, Hero of Dominaria", cost=['3', 'W', 'U'],
                             color_identity=['W', 'U'], card_type="Planeswalker", sub_types="Teferi",
                             abilities=[118898, 118899, 118992], set_id="DAR", rarity="Mythic Rare", set_number=207,
                             mtga_id=67518)
TianaShipsCaretaker = Card(name="tiana_ships_caretaker", pretty_name="Tiana, Ship's Caretaker", cost=['3', 'R', 'W'],
                           color_identity=['R', 'W'], card_type="Creature", sub_types="Angel Artificer",
                           abilities=[8, 6, 118901], set_id="DAR", rarity="Uncommon", set_number=208,
                           mtga_id=67520)
AesthirGlider = Card(name="aesthir_glider", pretty_name="Aesthir Glider", cost=['3'],
                     color_identity=[], card_type="Artifact Creature", sub_types="Bird Construct",
                     abilities=[8, 86476], set_id="DAR", rarity="Common", set_number=209,
                     mtga_id=67522)
AmaranthineWall = Card(name="amaranthine_wall", pretty_name="Amaranthine Wall", cost=['4'],
                       color_identity=[], card_type="Artifact Creature", sub_types="Wall",
                       abilities=[2, 118902], set_id="DAR", rarity="Uncommon", set_number=210,
                       mtga_id=67524)
BlackbladeReforged = Card(name="blackblade_reforged", pretty_name="Blackblade Reforged", cost=['2'],
                          color_identity=[], card_type="Artifact", sub_types="Equipment",
                          abilities=[118903, 118904, 118999], set_id="DAR", rarity="Rare", set_number=211,
                          mtga_id=67526)
BloodtallowCandle = Card(name="bloodtallow_candle", pretty_name="Bloodtallow Candle", cost=['1'],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[1290], set_id="DAR", rarity="Common", set_number=212,
                         mtga_id=67528)
DampingSphere = Card(name="damping_sphere", pretty_name="Damping Sphere", cost=['2'],
                     color_identity=[], card_type="Artifact", sub_types="",
                     abilities=[118906, 118907], set_id="DAR", rarity="Uncommon", set_number=213,
                     mtga_id=67530)
ForebearsBlade = Card(name="forebears_blade", pretty_name="Forebear's Blade", cost=['3'],
                      color_identity=[], card_type="Artifact", sub_types="Equipment",
                      abilities=[118908, 118909, 1156], set_id="DAR", rarity="Rare", set_number=214,
                      mtga_id=67532)
GildedLotus = Card(name="gilded_lotus", pretty_name="Gilded Lotus", cost=['5'],
                   color_identity=[], card_type="Artifact", sub_types="",
                   abilities=[4957], set_id="DAR", rarity="Rare", set_number=215,
                   mtga_id=67534)
GuardiansofKoilos = Card(name="guardians_of_koilos", pretty_name="Guardians of Koilos", cost=['5'],
                         color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                         abilities=[1297], set_id="DAR", rarity="Common", set_number=216,
                         mtga_id=67536)
HelmoftheHost = Card(name="helm_of_the_host", pretty_name="Helm of the Host", cost=['4'],
                     color_identity=[], card_type="Artifact", sub_types="Equipment",
                     abilities=[118911, 1077], set_id="DAR", rarity="Rare", set_number=217,
                     mtga_id=67538)
HowlingGolem = Card(name="howling_golem", pretty_name="Howling Golem", cost=['3'],
                    color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                    abilities=[118912], set_id="DAR", rarity="Uncommon", set_number=218,
                    mtga_id=67540)
IcyManipulator = Card(name="icy_manipulator", pretty_name="Icy Manipulator", cost=['4'],
                      color_identity=[], card_type="Artifact", sub_types="",
                      abilities=[4990], set_id="DAR", rarity="Uncommon", set_number=219,
                      mtga_id=67542)
JhoirasFamiliar = Card(name="jhoiras_familiar", pretty_name="Jhoira's Familiar", cost=['4'],
                       color_identity=[], card_type="Artifact Creature", sub_types="Bird",
                       abilities=[8, 119010], set_id="DAR", rarity="Uncommon", set_number=220,
                       mtga_id=67544)
JoustingLance = Card(name="jousting_lance", pretty_name="Jousting Lance", cost=['2'],
                     color_identity=[], card_type="Artifact", sub_types="Equipment",
                     abilities=[4712, 1304, 1156], set_id="DAR", rarity="Common", set_number=221,
                     mtga_id=67546)
Juggernaut = Card(name="juggernaut", pretty_name="Juggernaut", cost=['4'],
                  color_identity=[], card_type="Artifact Creature", sub_types="Juggernaut",
                  abilities=[118916, 88231], set_id="DAR", rarity="Uncommon", set_number=222,
                  mtga_id=67548)
MishrasSelfReplicator = Card(name="mishras_selfreplicator", pretty_name="Mishra's Self-Replicator", cost=['5'],
                             color_identity=[], card_type="Artifact Creature", sub_types="Assembly-Worker",
                             abilities=[119012], set_id="DAR", rarity="Rare", set_number=223,
                             mtga_id=67550)
MoxAmber = Card(name="mox_amber", pretty_name="Mox Amber", cost=[],
                color_identity=[], card_type="Artifact", sub_types="",
                abilities=[118918], set_id="DAR", rarity="Mythic Rare", set_number=224,
                mtga_id=67552)
NavigatorsCompass = Card(name="navigators_compass", pretty_name="Navigator's Compass", cost=['1'],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[1102, 118920], set_id="DAR", rarity="Common", set_number=225,
                         mtga_id=67554)
PardicWanderer = Card(name="pardic_wanderer", pretty_name="Pardic Wanderer", cost=['6'],
                      color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                      abilities=[14], set_id="DAR", rarity="Common", set_number=226,
                      mtga_id=67556)
PowerstoneShard = Card(name="powerstone_shard", pretty_name="Powerstone Shard", cost=['3'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[118921], set_id="DAR", rarity="Common", set_number=227,
                       mtga_id=67558)
ShieldoftheRealm = Card(name="shield_of_the_realm", pretty_name="Shield of the Realm", cost=['2'],
                        color_identity=[], card_type="Artifact", sub_types="Equipment",
                        abilities=[118922, 1268], set_id="DAR", rarity="Uncommon", set_number=228,
                        mtga_id=67560)
ShortSword = Card(name="short_sword", pretty_name="Short Sword", cost=['1'],
                  color_identity=[], card_type="Artifact", sub_types="Equipment",
                  abilities=[1314, 1268], set_id="DAR", rarity="Common", set_number=229,
                  mtga_id=67562)
SkitteringSurveyor = Card(name="skittering_surveyor", pretty_name="Skittering Surveyor", cost=['3'],
                          color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                          abilities=[92911], set_id="DAR", rarity="Common", set_number=230,
                          mtga_id=67564)
SorcerersWand = Card(name="sorcerers_wand", pretty_name="Sorcerer's Wand", cost=['1'],
                     color_identity=[], card_type="Artifact", sub_types="Equipment",
                     abilities=[118925, 1156], set_id="DAR", rarity="Uncommon", set_number=231,
                     mtga_id=67566)
SparringConstruct = Card(name="sparring_construct", pretty_name="Sparring Construct", cost=['1'],
                         color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                         abilities=[87008], set_id="DAR", rarity="Common", set_number=232,
                         mtga_id=67568)
ThranTemporalGateway = Card(name="thran_temporal_gateway", pretty_name="Thran Temporal Gateway", cost=['4'],
                            color_identity=[], card_type="Artifact", sub_types="",
                            abilities=[119017], set_id="DAR", rarity="Rare", set_number=233,
                            mtga_id=67570)
TraxosScourgeofKroog = Card(name="traxos_scourge_of_kroog", pretty_name="Traxos, Scourge of Kroog", cost=['4'],
                            color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                            abilities=[14, 18591, 118927], set_id="DAR", rarity="Rare", set_number=234,
                            mtga_id=67572)
UrzasTome = Card(name="urzas_tome", pretty_name="Urza's Tome", cost=['2'],
                 color_identity=[], card_type="Artifact", sub_types="",
                 abilities=[1322], set_id="DAR", rarity="Uncommon", set_number=235,
                 mtga_id=67574)
VoltaicServant = Card(name="voltaic_servant", pretty_name="Voltaic Servant", cost=['2'],
                      color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                      abilities=[118928], set_id="DAR", rarity="Common", set_number=236,
                      mtga_id=67576)
Weatherlight = Card(name="weatherlight", pretty_name="Weatherlight", cost=['4'],
                    color_identity=[], card_type="Artifact", sub_types="Vehicle",
                    abilities=[8, 118929, 76515], set_id="DAR", rarity="Mythic Rare", set_number=237,
                    mtga_id=67578)
CabalStronghold = Card(name="cabal_stronghold", pretty_name="Cabal Stronghold", cost=[],
                       color_identity=['B'], card_type="Land", sub_types="",
                       abilities=[1152, 1327], set_id="DAR", rarity="Rare", set_number=238,
                       mtga_id=67580)
ClifftopRetreat = Card(name="clifftop_retreat", pretty_name="Clifftop Retreat", cost=[],
                       color_identity=['R', 'W'], card_type="Land", sub_types="",
                       abilities=[99480, 4247], set_id="DAR", rarity="Rare", set_number=239,
                       mtga_id=67582)
HinterlandHarbor = Card(name="hinterland_harbor", pretty_name="Hinterland Harbor", cost=[],
                        color_identity=['G', 'U'], card_type="Land", sub_types="",
                        abilities=[99488, 18504], set_id="DAR", rarity="Rare", set_number=240,
                        mtga_id=67584)
IsolatedChapel = Card(name="isolated_chapel", pretty_name="Isolated Chapel", cost=[],
                      color_identity=['W', 'B'], card_type="Land", sub_types="",
                      abilities=[99478, 18472], set_id="DAR", rarity="Rare", set_number=241,
                      mtga_id=67586)
MemorialtoFolly = Card(name="memorial_to_folly", pretty_name="Memorial to Folly", cost=[],
                       color_identity=['B'], card_type="Land", sub_types="",
                       abilities=[76735, 1003, 118933], set_id="DAR", rarity="Uncommon", set_number=242,
                       mtga_id=67588)
MemorialtoGenius = Card(name="memorial_to_genius", pretty_name="Memorial to Genius", cost=[],
                        color_identity=['U'], card_type="Land", sub_types="",
                        abilities=[76735, 1002, 118935], set_id="DAR", rarity="Uncommon", set_number=243,
                        mtga_id=67590)
MemorialtoGlory = Card(name="memorial_to_glory", pretty_name="Memorial to Glory", cost=[],
                       color_identity=['W'], card_type="Land", sub_types="",
                       abilities=[76735, 1001, 118936], set_id="DAR", rarity="Uncommon", set_number=244,
                       mtga_id=67592)
MemorialtoUnity = Card(name="memorial_to_unity", pretty_name="Memorial to Unity", cost=[],
                       color_identity=['G'], card_type="Land", sub_types="",
                       abilities=[76735, 1005, 1341], set_id="DAR", rarity="Uncommon", set_number=245,
                       mtga_id=67594)
MemorialtoWar = Card(name="memorial_to_war", pretty_name="Memorial to War", cost=[],
                     color_identity=['R'], card_type="Land", sub_types="",
                     abilities=[76735, 1004, 119034], set_id="DAR", rarity="Uncommon", set_number=246,
                     mtga_id=67596)
SulfurFalls = Card(name="sulfur_falls", pretty_name="Sulfur Falls", cost=[],
                   color_identity=['U', 'R'], card_type="Land", sub_types="",
                   abilities=[99486, 1039], set_id="DAR", rarity="Rare", set_number=247,
                   mtga_id=67598)
WoodlandCemetery = Card(name="woodland_cemetery", pretty_name="Woodland Cemetery", cost=[],
                        color_identity=['B', 'G'], card_type="Land", sub_types="",
                        abilities=[99484, 4407], set_id="DAR", rarity="Rare", set_number=248,
                        mtga_id=67600)
ZhalfirinVoid = Card(name="zhalfirin_void", pretty_name="Zhalfirin Void", cost=[],
                     color_identity=[], card_type="Land", sub_types="",
                     abilities=[91717, 1152], set_id="DAR", rarity="Uncommon", set_number=249,
                     mtga_id=67602)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="DAR", rarity="Basic", set_number=250,
              mtga_id=67604)
Plains2 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="DAR", rarity="Basic", set_number=251,
               mtga_id=67606)
Plains3 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="DAR", rarity="Basic", set_number=252,
               mtga_id=67608)
Plains4 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="DAR", rarity="Basic", set_number=253,
               mtga_id=67610)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="DAR", rarity="Basic", set_number=254,
              mtga_id=67612)
Island2 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="DAR", rarity="Basic", set_number=255,
               mtga_id=67614)
Island3 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="DAR", rarity="Basic", set_number=256,
               mtga_id=67616)
Island4 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="DAR", rarity="Basic", set_number=257,
               mtga_id=67618)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="DAR", rarity="Basic", set_number=258,
             mtga_id=67620)
Swamp2 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="DAR", rarity="Basic", set_number=259,
              mtga_id=67622)
Swamp3 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="DAR", rarity="Basic", set_number=260,
              mtga_id=67624)
Swamp4 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="DAR", rarity="Basic", set_number=261,
              mtga_id=67626)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="DAR", rarity="Basic", set_number=262,
                mtga_id=67628)
Mountain2 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="DAR", rarity="Basic", set_number=263,
                 mtga_id=67630)
Mountain3 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="DAR", rarity="Basic", set_number=264,
                 mtga_id=67632)
Mountain4 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="DAR", rarity="Basic", set_number=265,
                 mtga_id=67634)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="DAR", rarity="Basic", set_number=266,
              mtga_id=67636)
Forest2 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="DAR", rarity="Basic", set_number=267,
               mtga_id=67638)
Forest3 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="DAR", rarity="Basic", set_number=268,
               mtga_id=67640)
Forest4 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="DAR", rarity="Basic", set_number=269,
               mtga_id=67642)
TeferiTimebender = Card(name="teferi_timebender", pretty_name="Teferi, Timebender", cost=['4', 'W', 'U'],
                        color_identity=['W', 'U'], card_type="Planeswalker", sub_types="Teferi",
                        abilities=[1349, 118940, 118941], set_id="DAR", rarity="Mythic Rare", set_number=270,
                        mtga_id=67644)
TemporalMachinations = Card(name="temporal_machinations", pretty_name="Temporal Machinations", cost=['2', 'U'],
                            color_identity=['U'], card_type="Sorcery", sub_types="",
                            abilities=[118942], set_id="DAR", rarity="Common", set_number=271,
                            mtga_id=67646)
NiambiFaithfulHealer = Card(name="niambi_faithful_healer", pretty_name="Niambi, Faithful Healer", cost=['1', 'W', 'U'],
                            color_identity=['W', 'U'], card_type="Creature", sub_types="Human Cleric",
                            abilities=[118943], set_id="DAR", rarity="Rare", set_number=272,
                            mtga_id=67648)
TeferisSentinel = Card(name="teferis_sentinel", pretty_name="Teferi's Sentinel", cost=['5'],
                       color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                       abilities=[118944], set_id="DAR", rarity="Uncommon", set_number=273,
                       mtga_id=67650)
MeanderingRiver = Card(name="meandering_river", pretty_name="Meandering River", cost=[],
                       color_identity=['W', 'U'], card_type="Land", sub_types="",
                       abilities=[76735, 1209], set_id="DAR", rarity="Common", set_number=274,
                       mtga_id=67652)
ChandraBoldPyromancer = Card(name="chandra_bold_pyromancer", pretty_name="Chandra, Bold Pyromancer", cost=['4', 'R', 'R'],
                             color_identity=['R'], card_type="Planeswalker", sub_types="Chandra",
                             abilities=[118946, 118947, 118948], set_id="DAR", rarity="Mythic Rare", set_number=275,
                             mtga_id=67654)
ChandrasOutburst = Card(name="chandras_outburst", pretty_name="Chandra's Outburst", cost=['3', 'R', 'R'],
                        color_identity=['R'], card_type="Sorcery", sub_types="",
                        abilities=[86663, 118950], set_id="DAR", rarity="Rare", set_number=276,
                        mtga_id=67656)
KarplusanHound = Card(name="karplusan_hound", pretty_name="Karplusan Hound", cost=['3', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Hound",
                      abilities=[1361], set_id="DAR", rarity="Uncommon", set_number=277,
                      mtga_id=67658)
PyromanticPilgrim = Card(name="pyromantic_pilgrim", pretty_name="Pyromantic Pilgrim", cost=['2', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Human Wizard",
                         abilities=[9], set_id="DAR", rarity="Common", set_number=278,
                         mtga_id=67660)
TimberGorge = Card(name="timber_gorge", pretty_name="Timber Gorge", cost=[],
                   color_identity=['R', 'G'], card_type="Land", sub_types="",
                   abilities=[76735, 1131], set_id="DAR", rarity="Common", set_number=279,
                   mtga_id=67662)
Knight = Card(name="knight", pretty_name="Knight", cost=[],
              color_identity=[], card_type="Creature", sub_types="Knight",
              abilities=[15], set_id="DAR", rarity="Token", set_number=1,
              mtga_id=67664)
Knight2 = Card(name="knight", pretty_name="Knight", cost=[],
               color_identity=[], card_type="Creature", sub_types="Knight",
               abilities=[15], set_id="DAR", rarity="Token", set_number=2,
               mtga_id=67665)
Soldier = Card(name="soldier", pretty_name="Soldier", cost=[],
               color_identity=[], card_type="Creature", sub_types="Soldier",
               abilities=[], set_id="DAR", rarity="Token", set_number=3,
               mtga_id=67666)
Cleric = Card(name="cleric", pretty_name="Cleric", cost=[],
              color_identity=[], card_type="Creature", sub_types="Cleric",
              abilities=[], set_id="DAR", rarity="Token", set_number=4,
              mtga_id=67667)
ZombieKnight = Card(name="zombie_knight", pretty_name="Zombie Knight", cost=[],
                    color_identity=[], card_type="Creature", sub_types="Zombie Knight",
                    abilities=[142], set_id="DAR", rarity="Token", set_number=5,
                    mtga_id=67668)
NightmareHorror = Card(name="nightmare_horror", pretty_name="Nightmare Horror", cost=[],
                       color_identity=[], card_type="Creature", sub_types="Nightmare Horror",
                       abilities=[], set_id="DAR", rarity="Token", set_number=6,
                       mtga_id=67669)
Demon = Card(name="demon", pretty_name="Demon", cost=[],
             color_identity=[], card_type="Creature", sub_types="Demon",
             abilities=[8, 14, 118826], set_id="DAR", rarity="Token", set_number=7,
             mtga_id=67670)
Elemental = Card(name="elemental", pretty_name="Elemental", cost=[],
                 color_identity=[], card_type="Creature", sub_types="Elemental",
                 abilities=[14, 9], set_id="DAR", rarity="Token", set_number=8,
                 mtga_id=67671)
Goblin = Card(name="goblin", pretty_name="Goblin", cost=[],
              color_identity=[], card_type="Creature", sub_types="Goblin",
              abilities=[], set_id="DAR", rarity="Token", set_number=9,
              mtga_id=67672)
KaroxBladewing = Card(name="karox_bladewing", pretty_name="Karox Bladewing", cost=[],
                      color_identity=[], card_type="Creature", sub_types="Dragon",
                      abilities=[8], set_id="DAR", rarity="Token", set_number=10,
                      mtga_id=67673)
Saproling = Card(name="saproling", pretty_name="Saproling", cost=[],
                 color_identity=[], card_type="Creature", sub_types="Saproling",
                 abilities=[], set_id="DAR", rarity="Token", set_number=11,
                 mtga_id=67674)
Saproling2 = Card(name="saproling", pretty_name="Saproling", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Saproling",
                  abilities=[], set_id="DAR", rarity="Token", set_number=12,
                  mtga_id=67675)
Saproling3 = Card(name="saproling", pretty_name="Saproling", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Saproling",
                  abilities=[], set_id="DAR", rarity="Token", set_number=13,
                  mtga_id=67676)
Construct = Card(name="construct", pretty_name="Construct", cost=[],
                 color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                 abilities=[119051], set_id="DAR", rarity="Token", set_number=14,
                 mtga_id=67677)
FiresongandSunspeaker = Card(name="firesong_and_sunspeaker", pretty_name="Firesong and Sunspeaker", cost=['4', 'R', 'W'],
                             color_identity=['R', 'W'], card_type="Creature", sub_types="Minotaur Cleric",
                             abilities=[119626, 119627], set_id="DAR", rarity="Rare", set_number=280,
                             mtga_id=68369)

# manually added:
TeferiHeroofDominaria_Masterpiece = Card(name="teferi_hero_of_dominaria", pretty_name="Teferi, Hero of Dominaria", cost=['3', 'W', 'U'],
                                         color_identity=['W', 'U'], card_type="Legendary Planeswalker", sub_types="Teferi",
                                         abilities=[118898, 118899, 118992], set_id="DOM", rarity="Mythic Rare", set_number=6000, mtga_id=69451)

clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
Dominaria = Set("dar", cards=clsmembers)

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
 142: 'Menace',
 1001: '{oT}: Add {oW}.',
 1002: '{oT}: Add {oU}.',
 1003: '{oT}: Add {oB}.',
 1004: '{oT}: Add {oR}.',
 1005: '{oT}: Add {oG}.',
 1027: 'Enchant creature',
 1038: 'Creatures you control with first strike have double strike.',
 1039: '{oT}: Add {oU} or {oR}.',
 1077: 'Equip {o5}',
 1102: "When Navigator's Compass enters the battlefield, you gain 3 life.",
 1131: '{oT}: Add {oR} or {oG}.',
 1152: '{oT}: Add {oC}.',
 1156: 'Equip {o3}',
 1162: '{oB}: Dread Shade gets +1/+1 until end of turn.',
 1205: 'When Verix Bladewing enters the battlefield, if it was kicked, create '
       'Karox Bladewing, a legendary 4/4 red Dragon creature token with '
       'flying.',
 1209: '{oT}: Add {oW} or {oU}.',
 1227: 'Whenever Grunn attacks alone, double its power and toughness until end '
       'of turn.',
 1248: 'Until your next turn, all lands you control become 2/2 Elemental '
       "creatures with reach, indestructible, and haste. They're still lands.",
 1268: 'Equip {o1}',
 1290: '{o6}, {oT}, Sacrifice Bloodtallow Candle: Target creature gets -5/-5 '
       'until end of turn.',
 1297: 'When Guardians of Koilos enters the battlefield, you may return '
       "another target historic permanent you control to its owner's hand.",
 1304: "As long as it's your turn, equipped creature has first strike.",
 1314: 'Equipped creature gets +1/+1.',
 1322: '{o3}, {oT}: Draw a card. Then discard a card unless you exile a '
       'historic card from your graveyard.',
 1327: '{o3}, {oT}: Add {oB} for each basic Swamp you control.',
 1341: '{o2oG}, {oT}, Sacrifice Memorial to Unity: Look at the top five cards '
       'of your library. You may reveal a creature card from among them and '
       'put it into your hand. Then put the rest on the bottom of your library '
       'in a random order.',
 1349: '+2: Untap up to one target artifact or creature.',
 1361: 'Whenever Karplusan Hound attacks, if you control a Chandra '
       'planeswalker, this creature deals 2 damage to any target.',
 1420: 'Enchant permanent',
 1421: 'You control enchanted permanent.',
 1716: '{oT}, Sacrifice an artifact: Draw a card.',
 1876: 'Kicker {oR}',
 1923: 'Return up to two target creature cards from your graveyard to your '
       'hand.',
 2045: 'Goblin spells you cast cost {o1} less to cast.',
 2046: 'Goblins you control have haste.',
 2076: 'When Siege-Gang Commander enters the battlefield, create three 1/1 red '
       'Goblin creature tokens.',
 2077: '{o1oR}, Sacrifice a Goblin: Siege-Gang Commander deals 2 damage to any '
       'target.',
 2410: '{o1oG}: Add one mana of any color.',
 2429: 'Sacrifice a Goblin: Add {oR}.',
 2433: 'Other creatures you control get +1/+1.',
 2465: 'Kicker {o2}',
 2478: 'Kicker {o2oW}',
 2640: 'At the beginning of each upkeep, create a 1/1 green Saproling creature '
       'token.',
 2722: 'Kicker {o2oG}',
 2739: 'Kicker {o1oU}',
 2813: 'Destroy target artifact or enchantment. You gain 4 life.',
 2817: 'Kicker {o3}',
 2852: 'Kicker {o4}',
 2938: 'Return target permanent card from your graveyard to your hand.',
 3974: 'Enchanted creature gets +1/+1.',
 4247: '{oT}: Add {oR} or {oW}.',
 4407: '{oT}: Add {oB} or {oG}.',
 4712: 'Equipped creature gets +2/+0.',
 4957: '{oT}: Add three mana of any one color.',
 4990: '{o1}, {oT}: Tap target artifact, creature, or land.',
 6270: 'Enchanted creature gets +1/+1 and has flying.',
 6425: '{oT}: You may put a land card from your hand onto the battlefield.',
 6495: 'Exile target creature or enchantment.',
 7022: 'You may pay {oWoUoBoRoG} rather than pay the mana cost for spells that '
       'you cast.',
 9313: 'Kicker {o1oW}',
 10662: 'Kicker {o3oB}',
 12792: 'Target player shuffles up to three target cards from their graveyard '
        'into their library.',
 14490: 'Kicker {o3oR}',
 14523: 'You may look at the top card of your library any time.',
 16132: "When Lich's Mastery leaves the battlefield, you lose the game.",
 18472: '{oT}: Add {oW} or {oB}.',
 18504: '{oT}: Add {oG} or {oU}.',
 18591: "Traxos, Scourge of Kroog enters the battlefield tapped and doesn't "
        'untap during your untap step.',
 19691: 'Create two 2/2 white Knight creature tokens with vigilance.',
 20123: "You may cast the top card of your library if it's an instant or "
        'sorcery card.',
 20379: 'Draw three cards. Target player puts the top three cards of their '
        'library into their graveyard.',
 21742: "II  Tap target creature an opponent controls. It doesn't untap during "
        "its controller's untap step for as long as you control Time of Ice.",
 23607: 'Draw two cards.',
 24741: 'Create three 1/1 green Saproling creature tokens.',
 25230: 'Creatures you control get +1/+1 until end of turn.',
 25846: 'Counter target spell.',
 25848: 'Draw a card.',
 26818: 'Destroy target creature.',
 26820: 'II  Create a 2/2 white Knight creature token with vigilance.',
 26886: 'Creatures you control gain first strike until end of turn.',
 61135: 'Other creatures you control have haste.',
 62540: 'Enchanted creature gets +2/+1 and has menace.',
 63602: 'Target creature gets -4/-0 until end of turn.',
 66937: 'Scry 1.',
 70361: "Wizard's Lightning deals 3 damage to any target.",
 75763: '{oT}: Add {oC}. Spend this mana only to cast an instant or sorcery '
        'spell.',
 76515: 'Crew 3',
 76735: 'Timber Gorge enters the battlefield tapped.',
 86476: "Aesthir Glider can't block.",
 86663: "Chandra's Outburst deals 4 damage to target player or planeswalker.",
 87008: 'When Sparring Construct dies, put a +1/+1 counter on target creature '
        'you control.',
 87941: "Steel Leaf Champion can't be blocked by creatures with power 2 or "
        'less.',
 88192: 'A deck can have any number of cards named Rat Colony.',
 88231: "Juggernaut can't be blocked by Walls.",
 88235: 'When Daring Archaeologist enters the battlefield, you may return '
        'target artifact card from your graveyard to your hand.',
 88255: 'You may have Thorn Elemental assign its combat damage as though it '
        "weren't blocked.",
 89217: "When enchanted creature dies, return that card to its owner's hand.",
 90362: 'When Deathbloom Thallid dies, create a 1/1 green Saproling creature '
        'token.',
 91717: 'When Zhalfirin Void enters the battlefield, scry 1.',
 92093: 'If Grunn, the Lonely King was kicked, it enters the battlefield with '
        'five +1/+1 counters on it.',
 92187: "At the beginning of the end step, if Skizzik wasn't kicked, sacrifice "
        'it.',
 92911: 'When Skittering Surveyor enters the battlefield, you may search your '
        'library for a basic land card, reveal it, put it into your hand, then '
        'shuffle your library.',
 93267: '{oT}, Sacrifice an artifact: Orcish Vandal deals 2 damage to any '
        'target.',
 95093: "When Gaea's Blessing is put into your graveyard from your library, "
        'shuffle your graveyard into your library.',
 95637: 'Counter target spell unless its controller pays {oX}. If that spell '
        'is countered this way, exile it instead of putting it into its '
        "owner's graveyard.",
 96307: 'When Academy Journeymage enters the battlefield, return target '
        "creature an opponent controls to its owner's hand.",
 96521: 'If Stronghold Confessor was kicked, it enters the battlefield with '
        'two +1/+1 counters on it.',
 96532: 'KickerSacrifice a creature.',
 96651: "Gaea's Protector must be blocked if able.",
 98407: "Return target permanent you control to its owner's hand.",
 98492: '{oT}, Sacrifice Tragic Poet: Return target enchantment card from your '
        'graveyard to your hand.',
 99193: "Return target nonland permanent to its owner's hand. If this spell "
        'was kicked, draw a card.',
 99478: 'Isolated Chapel enters the battlefield tapped unless you control a '
        'Plains or a Swamp.',
 99480: 'Clifftop Retreat enters the battlefield tapped unless you control a '
        'Mountain or a Plains.',
 99484: 'Woodland Cemetery enters the battlefield tapped unless you control a '
        'Swamp or a Forest.',
 99486: 'Sulfur Falls enters the battlefield tapped unless you control an '
        'Island or a Mountain.',
 99488: 'Hinterland Harbor enters the battlefield tapped unless you control a '
        'Forest or an Island.',
 100041: 'When Keldon Raider enters the battlefield, you may discard a card. '
         'If you do, draw a card.',
 100370: "Gideon's Reproach deals 4 damage to target attacking or blocking "
         'creature.',
 100685: 'When Cloudreader Sphinx enters the battlefield, scry 2.',
 100740: 'When Homarid Explorer enters the battlefield, target player puts the '
         'top four cards of their library into their graveyard.',
 100814: 'Pierce the Sky deals 7 damage to target creature with flying.',
 103194: 'II  Each player returns two land cards from their graveyard to the '
         'battlefield.',
 103816: 'Whenever Pegasus Courser attacks, another target attacking creature '
         'gains flying until end of turn.',
 118814: 'Discard a historic card: Sanctum Spirit gains indestructible until '
         'end of turn.',
 118815: "{o4}: Exchange your life total with Evra, Halcyon Witness's power.",
 118816: "You can't lose the game.",
 118817: 'Whenever you gain life, draw that many cards.',
 118818: 'Whenever you lose life, for each 1 life you lost, exile a permanent '
         'you control or a card from your hand or graveyard.',
 118819: 'Whenever you cast a historic spell, you may pay {oB}. If you do, '
         'return Lingering Phantom from your graveyard to your hand.',
 118820: 'I  Put a +1/+1 counter on up to one target creature. That creature '
         'becomes an artifact in addition to its other types.',
 118821: 'II  Destroy all nonartifact creatures.',
 118822: "III  Exile all cards from all opponents' graveyards.",
 118823: 'Rat Colony gets +1/+0 for each other Rat you control.',
 118824: 'When Seal Away enters the battlefield, exile target tapped creature '
         'an opponent controls until Seal Away leaves the battlefield.',
 118826: 'At the beginning of your upkeep, sacrifice another creature. If you '
         "can't, this creature deals 6 damage to you.",
 118827: 'III  Create a 6/6 black Demon creature token with flying, trample, '
         'and "At the beginning of your upkeep, sacrifice another creature. If '
         'you can\'t, this creature deals 6 damage to you."',
 118828: 'Exile target creature. Put two loyalty counters on a planeswalker '
         'you control.',
 118829: 'Put up to one target creature or planeswalker card from a graveyard '
         'onto the battlefield under your control. Destroy up to one target '
         "creature or planeswalker. Exile Yawgmoth's Vile Offering.",
 118830: 'Whenever you cast a spell, if that spell was kicked, Bloodstone '
         'Goblin gets +1/+1 and gains menace until end of turn.',
 118831: 'Whenever you cast a historic spell, Serra Disciple gets +1/+1 until '
         'end of turn.',
 118832: 'Kicker {o5oR}',
 118833: 'You, planeswalkers you control, and other creatures you control have '
         'hexproof.',
 118834: 'When Firefist Adept enters the battlefield, it deals X damage to '
         'target creature an opponent controls, where X is the number of '
         'Wizards you control.',
 118835: 'I  The First Eruption deals 1 damage to each creature without '
         'flying.',
 118836: 'III  If a red source you control would deal damage to a permanent or '
         'player this turn, it deals that much damage plus 2 to that permanent '
         'or player instead.',
 118837: 'When Excavation Elephant enters the battlefield, if it was kicked, '
         'return target artifact card from your graveyard to your hand.',
 118838: 'Whenever Keldon Warcaller attacks, put a lore counter on target Saga '
         'you control.',
 118840: 'Radiating Lightning deals 3 damage to target player and 1 damage to '
         'each creature that player controls.',
 118841: 'III  Target creature you control with the greatest power gains '
         'flying, first strike, and lifelink until end of turn.',
 118842: 'Target attacking creature gets +3/+3 and gains trample until end of '
         'turn.',
 118843: "Destroy target land. Up to two target creatures can't block this "
         'turn.',
 118844: 'Shivan Fire deals 2 damage to target creature. If this spell was '
         'kicked, it deals 4 damage to that creature instead.',
 118845: "Exile all nonland permanents that aren't legendary.",
 118846: 'You may cast Squee, the Immortal from your graveyard or from exile.',
 118847: 'Whenever Two-Headed Giant attacks, flip two coins. If both coins '
         'come up heads, Two-Headed Giant gains double strike until end of '
         'turn. If both coins come up tails, Two-Headed Giant gains menace '
         'until end of turn.',
 118848: 'At the beginning of combat on your turn, for each Aura and Equipment '
         'attached to Valduk, Keeper of the Flame, create a 3/1 red Elemental '
         'creature token with trample and haste. Exile those tokens at the '
         'beginning of the next end step.',
 118849: 'Whenever you attack with three or more creatures, you may pay '
         '{o2oR}. If you do, return Warcry Phoenix from your graveyard to the '
         'battlefield tapped and attacking.',
 118850: 'This spell costs {o2} less to cast if you control a Wizard.',
 118851: 'Look at the top three cards of your library. You may reveal a '
         'creature or land card from among them and put it into your hand. Put '
         'the rest on the bottom of your library in any order.',
 118852: 'I  Destroy all lands.',
 118853: 'If Untamed Kavu was kicked, it enters the battlefield with three '
         '+1/+1 counters on it.',
 118854: 'Destroy target artifact or enchantment. You may put a land card from '
         'your hand onto the battlefield.',
 118855: 'Whenever Corrosive Ooze blocks or becomes blocked by an equipped '
         'creature, destroy all Equipment attached to that creature at end of '
         'combat.',
 118857: 'This spell costs {o1} less to cast if you control a Wizard.',
 118858: '{o1oG}, Exile a creature card from your graveyard: Create a 1/1 '
         'green Saproling creature token.',
 118859: 'Sacrifice two Saprolings: You gain 2 life and draw a card.',
 118860: 'Untap target creature. It gets +2/+2 until end of turn. If this '
         'spell was kicked, that creature gets +4/+4 until end of turn '
         'instead.',
 118861: 'Search your library for a basic land card, put it onto the '
         'battlefield, then shuffle your library. If this spell was kicked, '
         'instead search your library for two basic land cards, put them onto '
         'the battlefield, then shuffle your library.',
 118862: 'Look at the top X cards of your library. You may put any number of '
         'land and/or legendary permanent cards with converted mana cost X or '
         'less from among them onto the battlefield. Put the rest into your '
         'graveyard.',
 118864: 'When Krosan Druid enters the battlefield, if it was kicked, you gain '
         '10 life.',
 118865: 'Kicker {o4oG}',
 118866: 'Whenever another Elf enters the battlefield under your control, put '
         'a +1/+1 counter on Marwyn, the Nurturer.',
 118867: "{oT}: Add an amount of {oG} equal to Marwyn's power.",
 118868: 'III  Artifacts you control become artifact creatures with base power '
         'and toughness 5/5 until end of turn.',
 118869: 'III  Return all land cards from your graveyard to the battlefield, '
         'then shuffle your graveyard into your library.',
 118870: "Multani, Yavimaya's Avatar gets +1/+1 for each land you control and "
         'each land card in your graveyard.',
 118871: "{o1oG}, Return two lands you control to their owner's hand: Return "
         'Multani from your graveyard to your hand.',
 118874: 'III  Put a +1/+1 counter on each creature you control. Those '
         'creatures gain vigilance, trample, and indestructible until end of '
         'turn.',
 118875: "Each other creature you control that's a Fungus or Saproling gets "
         '+1/+1.',
 118876: 'Whenever you cast a historic spell, scry 1.',
 118877: 'When Territorial Allosaurus enters the battlefield, if it was '
         'kicked, it fights another target creature.',
 118878: 'When Yavimaya Sapherd enters the battlefield, create a 1/1 green '
         'Saproling creature token.',
 118879: 'Whenever you cast an instant or sorcery spell, Wizards you control '
         'get +1/+1 until end of turn.',
 118880: 'Other legendary creatures you control get +2/+2.',
 118881: '{o2oW}, {oT}: Create a 2/2 white Knight creature token with '
         'vigilance.',
 118882: '{oB}, {oT}, Tap X untapped Knights you control: Destroy target '
         'creature with power X or less.',
 118883: 'At the beginning of your upkeep, if Darigaaz is exiled with an egg '
         'counter on it, remove an egg counter from it. Then if Darigaaz has '
         'no egg counters on it, return it to the battlefield.',
 118884: 'When Garna, the Bloodflame enters the battlefield, return to your '
         'hand all creature cards in your graveyard that were put there from '
         'anywhere this turn.',
 118885: 'Whenever one or more creatures you control attack, add that much '
         'mana in any combination of {oR} and/or {oG}. Until end of turn, you '
         "don't lose this mana as steps and phases end.",
 118886: 'Whenever you cast a spell, if that spell was kicked, put a +1/+1 '
         'counter on Hallar, the Firefletcher, then Hallar deals damage equal '
         'to the number of +1/+1 counters on it to each opponent.',
 118888: 'When Oath of Teferi enters the battlefield, exile another target '
         'permanent you control. Return it to the battlefield under its '
         "owner's control at the beginning of the next end step.",
 118889: 'You may activate the loyalty abilities of planeswalkers you control '
         'twice each turn rather than only once.',
 118890: 'Return all legendary permanent cards from your graveyard to the '
         'battlefield.',
 118892: 'You may cast nonland cards exiled with Rona.',
 118893: '{o4}, {oT}: Exile the top card of your library.',
 118894: "Shanna, Sisay's Legacy can't be the target of abilities your "
         'opponents control.',
 118895: 'Shanna gets +1/+1 for each creature you control.',
 118896: '{o4}: Create a 1/1 green Saproling creature token.',
 118897: 'Whenever a land enters the battlefield under your control, you gain '
         '1 life and draw a card.',
 118898: '+1: Draw a card. At the beginning of the next end step, untap up to '
         'two lands.',
 118899: "-3: Put target nonland permanent into its owner's library third from "
         'the top.',
 118901: 'Whenever an Aura or Equipment you control is put into a graveyard '
         "from the battlefield, you may return that card to its owner's hand "
         'at the beginning of the next end step.',
 118902: '{o2}: Amaranthine Wall gains indestructible until end of turn.',
 118903: 'Equipped creature gets +1/+1 for each land you control.',
 118904: 'Equip legendary creature {o3}',
 118905: 'Enchanted permanent has hexproof.',
 118906: 'If a land is tapped for two or more mana, it produces {oC} instead '
         'of any other type and amount.',
 118907: 'Each spell a player casts costs {o1} more to cast for each other '
         'spell that player has cast this turn.',
 118908: 'Equipped creature gets +3/+0 and has vigilance and trample.',
 118909: "Whenever equipped creature dies, attach Forebear's Blade to target "
         'creature you control.',
 118910: 'When enchanted permanent leaves the battlefield, if it was historic, '
         'draw two cards.',
 118911: "At the beginning of combat on your turn, create a token that's a "
         "copy of equipped creature, except the token isn't legendary if "
         'equipped creature is legendary. That token gains haste.',
 118912: 'Whenever Howling Golem attacks or blocks, each player draws a card.',
 118913: 'Enchanted creature has base power and toughness 0/4, has defender, '
         'loses all other abilities, and is a blue Wall in addition to its '
         'other colors and types.',
 118914: 'Prevent the next 3 damage that would be dealt to any target this '
         'turn by a source of your choice. You gain 3 life.',
 118915: 'Create two 1/1 green Saproling creature tokens. If this spell was '
         'kicked, create four of those tokens instead.',
 118916: 'Juggernaut attacks each combat if able.',
 118917: 'Whenever you cast a historic spell, target player puts the top two '
         'cards of their library into their graveyard.',
 118918: '{oT}: Add one mana of any color among legendary creatures and '
         'planeswalkers you control.',
 118920: '{oT}: Until end of turn, target land you control becomes the basic '
         'land type of your choice in addition to its other types.',
 118921: '{oT}: Add {oC} for each artifact you control named Powerstone Shard.',
 118922: 'If a source would deal damage to equipped creature, prevent 2 of '
         'that damage.',
 118925: 'Equipped creature has "{oT}: This creature deals 1 damage to target '
         'player or planeswalker. If this creature is a Wizard, it deals 2 '
         'damage to that player or planeswalker instead."',
 118927: 'Whenever you cast a historic spell, untap Traxos.',
 118928: 'At the beginning of your end step, untap target artifact.',
 118929: 'Whenever Weatherlight deals combat damage to a player, look at the '
         'top five cards of your library. You may reveal a historic card from '
         'among them and put it into your hand. Put the rest on the bottom of '
         'your library in a random order.',
 118930: 'Enchanted permanent is legendary.',
 118933: '{o2oB}, {oT}, Sacrifice Memorial to Folly: Return target creature '
         'card from your graveyard to your hand.',
 118934: 'Target player takes an extra turn after this one. Return up to one '
         "target nonland permanent to its owner's hand. Exile Karn's Temporal "
         'Sundering.',
 118935: '{o4oU}, {oT}, Sacrifice Memorial to Genius: Draw two cards.',
 118936: '{o3oW}, {oT}, Sacrifice Memorial to Glory: Create two 1/1 white '
         'Soldier creature tokens.',
 118938: 'When Merfolk Trickster enters the battlefield, tap target creature '
         'an opponent controls. It loses all abilities until end of turn.',
 118939: 'I  Return target instant card from your graveyard to your hand.',
 118940: '-3: You gain 2 life and draw two cards.',
 118941: '-9: Take an extra turn after this one.',
 118942: "Return target creature to its owner's hand. If you control an "
         'artifact, draw a card.',
 118943: 'When Niambi, Faithful Healer enters the battlefield, you may search '
         'your library and/or graveyard for a card named Teferi, Timebender, '
         'reveal it, and put it into your hand. If you search your library '
         'this way, shuffle it.',
 118944: "As long as you control a Teferi planeswalker, Teferi's Sentinel gets "
         '+4/+0.',
 118945: 'II  Return target sorcery card from your graveyard to your hand.',
 118946: '+1: Add {oRoR}. Chandra, Bold Pyromancer deals 2 damage to target '
         'player.',
 118947: '-3: Chandra, Bold Pyromancer deals 3 damage to target creature or '
         'planeswalker.',
 118948: '-7: Chandra, Bold Pyromancer deals 10 damage to target player and '
         'each creature and planeswalker they control.',
 118950: 'Search your library and/or graveyard for a card named Chandra, Bold '
         'Pyromancer, reveal it, and put it into your hand. If you search your '
         'library this way, shuffle it.',
 118951: 'III  Until end of turn, whenever you cast an instant or sorcery '
         'spell, copy it. You may choose new targets for the copy.',
 118952: 'III  Knights you control get +2/+1 until end of turn.',
 118954: 'Enchanted creature gets +2/+2, has first strike, and is a Knight in '
         'addition to its other types.',
 118955: 'If a Wizard entering the battlefield under your control causes a '
         'triggered ability of a permanent you control to trigger, that '
         'ability triggers an additional time.',
 118956: 'When Naru Meha, Master Wizard enters the battlefield, copy target '
         'instant or sorcery spell you control. You may choose new targets for '
         'the copy.',
 118957: 'Put a +1/+1 counter on each creature you control. If this spell was '
         'kicked, put two +1/+1 counters on each creature you control instead.',
 118958: 'Other Wizards you control get +1/+1.',
 118960: '{o3}: Exile the top card of your library.',
 118962: "Relic Runner can't be blocked if you've cast a historic spell this "
         'turn.',
 118963: 'If Darigaaz Reincarnated would die, instead exile it with three egg '
         'counters on it.',
 118964: 'Hexproof from black',
 118965: 'When Sentinel of the Pearl Trident enters the battlefield, you may '
         'exile target historic permanent you control. If you do, return that '
         "card to the battlefield under its owner's control at the beginning "
         'of the next end step.',
 118966: 'When Slinn Voda, the Rising Deep enters the battlefield, if it was '
         "kicked, return all creatures to their owners' hands except for "
         'Merfolk, Krakens, Leviathans, Octopuses, and Serpents.',
 118967: 'Tempest Djinn gets +1/+0 for each basic Island you control.',
 118968: 'Whenever you cast a historic spell, draw a card.',
 118969: "Creatures you control with power or toughness 1 or less can't be "
         'blocked.',
 118970: 'Knight of Grace gets +1/+0 as long as any player controls a black '
         'permanent.',
 118972: 'During each of your turns, you may play up to one permanent card of '
         'each permanent type from your graveyard.',
 118973: "III  Return all tapped creatures to their owners' hands.",
 118974: 'Counter target noncreature spell. Untap up to three lands.',
 118975: 'When Ghitu Journeymage enters the battlefield, if you control '
         'another Wizard, Ghitu Journeymage deals 2 damage to each opponent.',
 118978: 'You may cast historic spells as though they had flash.',
 118979: 'When Rona, Disciple of Gix enters the battlefield, you may exile '
         'target historic card from your graveyard.',
 118980: 'You may pay {o3oU} and tap an untapped artifact you control rather '
         "than pay this spell's mana cost.",
 118981: "Target creature gets +2/+1 until end of turn. If it's legendary, it "
         'also gains lifelink until end of turn.',
 118982: 'Whenever you cast a historic spell, Cabal Paladin deals 2 damage to '
         'each opponent.',
 118983: 'Other Angels you control get +1/+1 and have lifelink.',
 118985: 'When Caligo Skin-Witch enters the battlefield, if it was kicked, '
         'each opponent discards two cards.',
 118986: 'Whenever a Saproling you control dies, Slimefoot, the Stowaway deals '
         '1 damage to each opponent and you gain 1 life.',
 118987: 'Destroy target nonlegendary creature.',
 118989: 'III  Create an X/X black Nightmare Horror creature token, where X is '
         'half your life total, rounded up. It deals X damage to you.',
 118990: 'Look at the top three cards of your library. Put two of them into '
         'your hand and the other into your graveyard. Dark Bargain deals 2 '
         'damage to you.',
 118991: 'Enchanted creature is legendary, gets +1/+1, and has flying, '
         'vigilance, and lifelink.',
 118992: '-8: You get an emblem with "Whenever you draw a card, exile target '
         'permanent an opponent controls."',
 118993: "Put a +1/+1 counter on target creature you control if it's "
         'legendary. Then it fights target creature an opponent controls.',
 118994: 'When Demonlord Belzenlok enters the battlefield, exile cards from '
         'the top of your library until you exile a nonland card, then put '
         "that card into your hand. If the card's converted mana cost is 4 or "
         'greater, repeat this process. Demonlord Belzenlok deals 1 damage to '
         'you for each card put into your hand this way.',
 118995: 'Target player reveals their hand. You choose an artifact or creature '
         'card from it. That player discards that card.',
 118996: '{o3}: Tap Drudge Sentinel. It gains indestructible until end of '
         'turn.',
 118997: 'Put a +1/+1 counter on target creature. That creature gains reach '
         'until end of turn.',
 118998: 'I  Each opponent sacrifices a creature or planeswalker.',
 118999: 'Equip {o7}',
 119000: 'II  Each opponent discards a card.',
 119001: 'III  Put target creature or planeswalker card from a graveyard onto '
         'the battlefield under your control.',
 119002: 'Search your library for two cards. Put one into your hand and the '
         'other into your graveyard. Then shuffle your library.',
 119003: 'Target creature gets -1/-1 until end of turn. Create a 1/1 green '
         'Saproling creature token.',
 119004: 'Kicker {o5oB}',
 119005: 'When Josu Vess, Lich Knight enters the battlefield, if it was '
         'kicked, create eight 2/2 black Zombie Knight creature tokens with '
         'menace.',
 119006: 'Whenever a creature an opponent controls is dealt damage, put a '
         '+1/+1 counter on Kazarov, Sengir Pureblood.',
 119007: '{o3oR}: Kazarov deals 2 damage to target creature.',
 119008: 'Hexproof from white',
 119009: 'Knight of Malice gets +1/+0 as long as any player controls a white '
         'permanent.',
 119010: 'Historic spells you cast cost {o1} less to cast.',
 119011: 'When Sergeant-at-Arms enters the battlefield, if it was kicked, '
         'create two 1/1 white Soldier creature tokens.',
 119012: 'Whenever you cast a historic spell, you may pay {o1}. If you do, '
         "create a token that's a copy of Mishra's Self-Replicator.",
 119013: '{oT}: Add {oGoG}. Spend this mana only to cast kicked spells.',
 119014: '{o1}, Sacrifice another creature: Thallid Omnivore gets +2/+2 until '
         'end of turn. If a Saproling was sacrificed this way, you gain 2 '
         'life.',
 119015: '{o2}, Sacrifice a creature: Draw a card.',
 119016: 'As an additional cost to cast this spell, you may sacrifice any '
         'number of creatures. This spell costs {o2} less to cast for each '
         'creature sacrificed this way.',
 119017: '{o4}, {oT}: You may put a historic permanent card from your hand '
         'onto the battlefield.',
 119018: 'When Torgaar, Famine Incarnate enters the battlefield, up to one '
         "target player's life total becomes half their starting life total, "
         'rounded down.',
 119019: 'Whenever Urgoros, the Empty One deals combat damage to a player, '
         "that player discards a card at random. If the player can't, you draw "
         'a card.',
 119020: '{o4oGoG}: Put a +1/+1 counter on each creature you control.',
 119021: 'Target creature gets -2/-2 until end of turn. If this spell was '
         'kicked, that creature gets -5/-5 until end of turn instead.',
 119022: '{oT}, Sacrifice two creatures: Return target creature card from your '
         'graveyard to the battlefield.',
 119023: 'When Windgrace Acolyte enters the battlefield, put the top three '
         'cards of your library into your graveyard and you gain 3 life.',
 119024: 'Whenever you cast a historic spell, return target creature card with '
         'converted mana cost 3 or less from your graveyard to the '
         'battlefield.',
 119025: 'Champion of the Flame gets +2/+2 for each Aura and Equipment '
         'attached to it.',
 119026: 'Target creature gets +1/+0 and gains first strike and haste until '
         'end of turn.',
 119027: 'Choose one   Fiery Intervention deals 5 damage to target creature.  '
         'Destroy target artifact.',
 119028: 'Fight with Fire deals 5 damage to target creature. If this spell was '
         'kicked, it deals 10 damage divided as you choose among any number of '
         'targets instead.',
 119029: 'II  Add {oRoR}.',
 119031: 'III  Sacrifice a Mountain. If you do, The First Eruption deals 3 '
         'damage to each creature.',
 119032: 'I  Discard your hand.',
 119033: 'II  Draw two cards.',
 119034: '{o4oR}, {oT}, Sacrifice Memorial to War: Destroy target land.',
 119035: 'When Ghitu Chronicler enters the battlefield, if it was kicked, '
         'return target instant or sorcery card from your graveyard to your '
         'hand.',
 119036: 'As long as there are two or more instant and/or sorcery cards in '
         'your graveyard, Ghitu Lavarunner gets +1/+0 and has haste.',
 119037: 'KickerSacrifice an artifact or Goblin.',
 119038: 'Goblin Barrage deals 4 damage to target creature. If this spell was '
         'kicked, it also deals 4 damage to target player or planeswalker.',
 119039: 'When Goblin Chainwhirler enters the battlefield, it deals 1 damage '
         'to each opponent and each creature and planeswalker they control.',
 119040: 'When Haphazard Bombardment enters the battlefield, choose four '
         "nonenchantment permanents you don't control and put an aim counter "
         'on each of them.',
 119041: 'At the beginning of your end step, if two or more permanents you '
         "don't control have an aim counter on them, destroy one of those "
         'permanents at random.',
 119042: '+1: Add {oRoRoR}. Spend this mana only to cast instant or sorcery '
         'spells.',
 119043: '+1: Discard up to three cards, then draw that many cards.',
 119045: 'Look at the top five cards of your library. You may reveal a '
         'historic card from among them and put it into your hand. Put the '
         'rest on the bottom of your library in a random order.',
 119046: '-8: You get an emblem with "You may cast instant and sorcery cards '
         'from your graveyard. If a card cast this way would be put into your '
         'graveyard, exile it instead."',
 119047: "Jaya's Immolating Inferno deals X damage to each of up to three "
         'targets.',
 119048: 'When Keldon Overseer enters the battlefield, if it was kicked, gain '
         'control of target creature until end of turn. Untap that creature. '
         'It gains haste until end of turn.',
 119049: '+1: Reveal the top two cards of your library. An opponent chooses '
         'one of them. Put that card into your hand and exile the other with a '
         'silver counter on it.',
 119050: '-1: Put a card you own with a silver counter on it from exile into '
         'your hand.',
 119051: 'This creature gets +1/+1 for each artifact you control.',
 119052: '-2: Create a 0/0 colorless Construct artifact creature token with '
         '"This creature gets +1/+1 for each artifact you control."',
 119053: 'Target creature gets +2/+2 and gains indestructible until end of '
         'turn.',
 119054: "Creatures can't attack you or a planeswalker you control unless "
         'their controller pays {o1} for each of those creatures.',
 119055: 'Benalish Honor Guard gets +1/+0 for each legendary creature you '
         'control.',
 119056: 'Rampaging Cyclops gets -2/-0 as long as two or more creatures are '
         'blocking it.',
 119057: 'Whenever you cast a historic spell, tap target creature an opponent '
         'controls.',
 119058: 'Aura and Equipment spells you cast cost {o1} less to cast.',
 119059: 'Whenever you cast a historic spell, put a +1/+1 counter on Daring '
         'Archaeologist.',
 119060: 'As Dauntless Bodyguard enters the battlefield, choose another '
         'creature you control.',
 119061: 'Sacrifice Dauntless Bodyguard: The chosen creature gains '
         'indestructible until end of turn.',
 119071: 'I  Create a 2/2 white Knight creature token with vigilance.',
 119074: "I  Tap target creature an opponent controls. It doesn't untap during "
         "its controller's untap step for as long as you control Time of Ice.",
 119075: 'III  Each player returns two land cards from their graveyard to the '
         'battlefield.',
 119079: "I  Chainer's Torment deals 2 damage to each opponent and you gain 2 "
         'life.',
 119080: "II  Chainer's Torment deals 2 damage to each opponent and you gain 2 "
         'life.',
 119267: 'I  Put a +1/+1 counter on target creature you control with the '
         'greatest power.',
 119268: 'II  Put a +1/+1 counter on target creature you control with the '
         'greatest power.',
 119269: 'I  Look at the top five cards of your library. You may reveal an '
         'artifact card from among them and put it into your hand. Put the '
         'rest on the bottom of your library in a random order.',
 119270: 'I  Until your next turn, creatures you control gain "{oT}: Add one '
         'mana of any color."',
 119271: 'II  Until your next turn, creatures you control gain "{oT}: Add one '
         'mana of any color."',
 119272: 'II  Look at the top five cards of your library. You may reveal an '
         'artifact card from among them and put it into your hand. Put the '
         'rest on the bottom of your library in a random order.',
 119273: 'I  Put the top two cards of your library into your graveyard, then '
         'you may return a creature card from your graveyard to your hand.',
 119274: 'II  Put the top two cards of your library into your graveyard, then '
         'you may return a creature card from your graveyard to your hand.',
 119276: 'I  Create two 0/1 black Cleric creature tokens.',
 119277: 'II  Create two 0/1 black Cleric creature tokens.',
 119626: 'Red instant and sorcery spells you control have lifelink.',
 119627: 'Whenever a white instant or sorcery spell causes you to gain life, '
         'Firesong and Sunspeaker deals 3 damage to target creature or player.'}
