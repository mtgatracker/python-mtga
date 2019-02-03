
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


AegisoftheHeavens = Card(name="aegis_of_the_heavens", pretty_name="Aegis of the Heavens", cost=['1', 'W'],
                         color_identity=['W'], card_type="Instant", sub_types="",
                         abilities=[119255], set_id="M19", rarity="Uncommon", collectible=True, set_number=1,
                         mtga_id=67682)
AethershieldArtificer = Card(name="aethershield_artificer", pretty_name="Aethershield Artificer", cost=['3', 'W'],
                             color_identity=['W'], card_type="Creature", sub_types="Dwarf Artificer",
                             abilities=[119256], set_id="M19", rarity="Uncommon", collectible=True, set_number=2,
                             mtga_id=67684)
AjaniAdversaryofTyrants = Card(name="ajani_adversary_of_tyrants", pretty_name="Ajani, Adversary of Tyrants", cost=['2', 'W', 'W'],
                               color_identity=['W'], card_type="Planeswalker", sub_types="Ajani",
                               abilities=[119257, 119244, 119259], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=3,
                               mtga_id=67686)
AjanisLastStand = Card(name="ajanis_last_stand", pretty_name="Ajani's Last Stand", cost=['2', 'W', 'W'],
                       color_identity=['W'], card_type="Enchantment", sub_types="",
                       abilities=[119260, 119261], set_id="M19", rarity="Rare", collectible=True, set_number=4,
                       mtga_id=67688)
AjanisPridemate = Card(name="ajanis_pridemate", pretty_name="Ajani's Pridemate", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Cat Soldier",
                       abilities=[92970], set_id="M19", rarity="Uncommon", collectible=True, set_number=5,
                       mtga_id=67690)
AjanisWelcome = Card(name="ajanis_welcome", pretty_name="Ajani's Welcome", cost=['W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="",
                     abilities=[119250], set_id="M19", rarity="Uncommon", collectible=True, set_number=6,
                     mtga_id=67692)
AngeloftheDawn = Card(name="angel_of_the_dawn", pretty_name="Angel of the Dawn", cost=['4', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Angel",
                      abilities=[8, 76894], set_id="M19", rarity="Common", collectible=True, set_number=7,
                      mtga_id=67694)
CavalryDrillmaster = Card(name="cavalry_drillmaster", pretty_name="Cavalry Drillmaster", cost=['1', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                          abilities=[119262], set_id="M19", rarity="Common", collectible=True, set_number=8,
                          mtga_id=67696)
CleansingNova = Card(name="cleansing_nova", pretty_name="Cleansing Nova", cost=['3', 'W', 'W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[119263], set_id="M19", rarity="Rare", collectible=True, set_number=9,
                     mtga_id=67698)
DaybreakChaplain = Card(name="daybreak_chaplain", pretty_name="Daybreak Chaplain", cost=['1', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                        abilities=[12], set_id="M19", rarity="Common", collectible=True, set_number=10,
                        mtga_id=67700)
DwarvenPriest = Card(name="dwarven_priest", pretty_name="Dwarven Priest", cost=['3', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Dwarf Cleric",
                     abilities=[90788], set_id="M19", rarity="Common", collectible=True, set_number=11,
                     mtga_id=67702)
GallantCavalry = Card(name="gallant_cavalry", pretty_name="Gallant Cavalry", cost=['3', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                      abilities=[15, 99956], set_id="M19", rarity="Common", collectible=True, set_number=12,
                      mtga_id=67704)
HeraldofFaith = Card(name="herald_of_faith", pretty_name="Herald of Faith", cost=['3', 'W', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Angel",
                     abilities=[8, 119264], set_id="M19", rarity="Uncommon", collectible=True, set_number=13,
                     mtga_id=67706)
HieromancersCage = Card(name="hieromancers_cage", pretty_name="Hieromancer's Cage", cost=['3', 'W'],
                        color_identity=['W'], card_type="Enchantment", sub_types="",
                        abilities=[20997], set_id="M19", rarity="Uncommon", collectible=True, set_number=14,
                        mtga_id=67708)
InspiredCharge = Card(name="inspired_charge", pretty_name="Inspired Charge", cost=['2', 'W', 'W'],
                      color_identity=['W'], card_type="Instant", sub_types="",
                      abilities=[11632], set_id="M19", rarity="Common", collectible=True, set_number=15,
                      mtga_id=67710)
InvoketheDivine = Card(name="invoke_the_divine", pretty_name="Invoke the Divine", cost=['2', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[2813], set_id="M19", rarity="Common", collectible=True, set_number=16,
                       mtga_id=67712)
Isolate = Card(name="isolate", pretty_name="Isolate", cost=['W'],
               color_identity=['W'], card_type="Instant", sub_types="",
               abilities=[119082], set_id="M19", rarity="Rare", collectible=True, set_number=17,
               mtga_id=67714)
KnightoftheTusk = Card(name="knight_of_the_tusk", pretty_name="Knight of the Tusk", cost=['4', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                       abilities=[15], set_id="M19", rarity="Common", collectible=True, set_number=18,
                       mtga_id=67716)
KnightsPledge = Card(name="knights_pledge", pretty_name="Knight's Pledge", cost=['1', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 2018], set_id="M19", rarity="Common", collectible=True, set_number=19,
                     mtga_id=67718)
KnightlyValor = Card(name="knightly_valor", pretty_name="Knightly Valor", cost=['4', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 99956, 19558], set_id="M19", rarity="Uncommon", collectible=True, set_number=20,
                     mtga_id=67720)
LenaSelflessChampion = Card(name="lena_selfless_champion", pretty_name="Lena, Selfless Champion", cost=['4', 'W', 'W'],
                            color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                            abilities=[119137, 119146], set_id="M19", rarity="Rare", collectible=True, set_number=21,
                            mtga_id=67722)
LeoninVanguard = Card(name="leonin_vanguard", pretty_name="Leonin Vanguard", cost=['W'],
                      color_identity=['W'], card_type="Creature", sub_types="Cat Soldier",
                      abilities=[119166], set_id="M19", rarity="Uncommon", collectible=True, set_number=22,
                      mtga_id=67724)
LeoninWarleader = Card(name="leonin_warleader", pretty_name="Leonin Warleader", cost=['2', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Cat Soldier",
                       abilities=[119181], set_id="M19", rarity="Rare", collectible=True, set_number=23,
                       mtga_id=67726)
LoxodonLineBreaker = Card(name="loxodon_line_breaker", pretty_name="Loxodon Line Breaker", cost=['2', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Elephant Soldier",
                          abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=24,
                          mtga_id=67728)
LuminousBonds = Card(name="luminous_bonds", pretty_name="Luminous Bonds", cost=['2', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 1083], set_id="M19", rarity="Common", collectible=True, set_number=25,
                     mtga_id=67730)
MakeaStand = Card(name="make_a_stand", pretty_name="Make a Stand", cost=['2', 'W'],
                  color_identity=['W'], card_type="Instant", sub_types="",
                  abilities=[62471], set_id="M19", rarity="Uncommon", collectible=True, set_number=26,
                  mtga_id=67732)
MentoroftheMeek = Card(name="mentor_of_the_meek", pretty_name="Mentor of the Meek", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                       abilities=[18682], set_id="M19", rarity="Rare", collectible=True, set_number=27,
                       mtga_id=67734)
MightyLeap = Card(name="mighty_leap", pretty_name="Mighty Leap", cost=['1', 'W'],
                  color_identity=['W'], card_type="Instant", sub_types="",
                  abilities=[1235], set_id="M19", rarity="Common", collectible=True, set_number=28,
                  mtga_id=67736)
MilitiaBugler = Card(name="militia_bugler", pretty_name="Militia Bugler", cost=['2', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                     abilities=[15, 119203], set_id="M19", rarity="Uncommon", collectible=True, set_number=29,
                     mtga_id=67738)
NoviceKnight = Card(name="novice_knight", pretty_name="Novice Knight", cost=['W'],
                    color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                    abilities=[2, 119206], set_id="M19", rarity="Uncommon", collectible=True, set_number=30,
                    mtga_id=67740)
OreskosSwiftclaw = Card(name="oreskos_swiftclaw", pretty_name="Oreskos Swiftclaw", cost=['1', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Cat Warrior",
                        abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=31,
                        mtga_id=67742)
PegasusCourser = Card(name="pegasus_courser", pretty_name="Pegasus Courser", cost=['2', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Pegasus",
                      abilities=[8, 103816], set_id="M19", rarity="Common", collectible=True, set_number=32,
                      mtga_id=67744)
RemorsefulCleric = Card(name="remorseful_cleric", pretty_name="Remorseful Cleric", cost=['1', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Spirit Cleric",
                        abilities=[8, 119081], set_id="M19", rarity="Rare", collectible=True, set_number=33,
                        mtga_id=67746)
ResplendentAngel = Card(name="resplendent_angel", pretty_name="Resplendent Angel", cost=['1', 'W', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Angel",
                        abilities=[8, 119087, 119083], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=34,
                        mtga_id=67748)
Revitalize = Card(name="revitalize", pretty_name="Revitalize", cost=['1', 'W'],
                  color_identity=['W'], card_type="Instant", sub_types="",
                  abilities=[30479, 25848], set_id="M19", rarity="Common", collectible=True, set_number=35,
                  mtga_id=67750)
RustwingFalcon = Card(name="rustwing_falcon", pretty_name="Rustwing Falcon", cost=['W'],
                      color_identity=['W'], card_type="Creature", sub_types="Bird",
                      abilities=[8], set_id="M19", rarity="Common", collectible=True, set_number=36,
                      mtga_id=67752)
ShieldMare = Card(name="shield_mare", pretty_name="Shield Mare", cost=['1', 'W', 'W'],
                  color_identity=['W'], card_type="Creature", sub_types="Horse",
                  abilities=[97130, 119224], set_id="M19", rarity="Uncommon", collectible=True, set_number=37,
                  mtga_id=67754)
StarCrownedStag = Card(name="starcrowned_stag", pretty_name="Star-Crowned Stag", cost=['3', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Elk",
                       abilities=[94230], set_id="M19", rarity="Common", collectible=True, set_number=38,
                       mtga_id=67756)
Suncleanser = Card(name="suncleanser", pretty_name="Suncleanser", cost=['1', 'W'],
                   color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                   abilities=[119093], set_id="M19", rarity="Rare", collectible=True, set_number=39,
                   mtga_id=67758)
TakeVengeance = Card(name="take_vengeance", pretty_name="Take Vengeance", cost=['1', 'W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[1385], set_id="M19", rarity="Common", collectible=True, set_number=40,
                     mtga_id=67760)
TrustyPackbeast = Card(name="trusty_packbeast", pretty_name="Trusty Packbeast", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Beast",
                       abilities=[119101], set_id="M19", rarity="Common", collectible=True, set_number=41,
                       mtga_id=67762)
ValiantKnight = Card(name="valiant_knight", pretty_name="Valiant Knight", cost=['3', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                     abilities=[119104, 119107], set_id="M19", rarity="Rare", collectible=True, set_number=42,
                     mtga_id=67764)
AetherTunnel = Card(name="aether_tunnel", pretty_name="Aether Tunnel", cost=['1', 'U'],
                    color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1027, 119109], set_id="M19", rarity="Uncommon", collectible=True, set_number=43,
                    mtga_id=67766)
Anticipate = Card(name="anticipate", pretty_name="Anticipate", cost=['1', 'U'],
                  color_identity=['U'], card_type="Instant", sub_types="",
                  abilities=[61084], set_id="M19", rarity="Common", collectible=True, set_number=44,
                  mtga_id=67768)
AvenWindMage = Card(name="aven_wind_mage", pretty_name="Aven Wind Mage", cost=['2', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Bird Wizard",
                    abilities=[8, 119114], set_id="M19", rarity="Common", collectible=True, set_number=45,
                    mtga_id=67770)
AviationPioneer = Card(name="aviation_pioneer", pretty_name="Aviation Pioneer", cost=['2', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                       abilities=[102214], set_id="M19", rarity="Common", collectible=True, set_number=46,
                       mtga_id=67772)
BonetoAsh = Card(name="bone_to_ash", pretty_name="Bone to Ash", cost=['2', 'U', 'U'],
                 color_identity=['U'], card_type="Instant", sub_types="",
                 abilities=[24121, 25848], set_id="M19", rarity="Uncommon", collectible=True, set_number=47,
                 mtga_id=67774)
Cancel = Card(name="cancel", pretty_name="Cancel", cost=['1', 'U', 'U'],
              color_identity=['U'], card_type="Instant", sub_types="",
              abilities=[25846], set_id="M19", rarity="Common", collectible=True, set_number=48,
              mtga_id=67776)
DepartedDeckhand = Card(name="departed_deckhand", pretty_name="Departed Deckhand", cost=['1', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Spirit Pirate",
                        abilities=[88041, 119133, 119136], set_id="M19", rarity="Uncommon", collectible=True, set_number=49,
                        mtga_id=67778)
Disperse = Card(name="disperse", pretty_name="Disperse", cost=['1', 'U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[94618], set_id="M19", rarity="Common", collectible=True, set_number=50,
                mtga_id=67780)
Divination = Card(name="divination", pretty_name="Divination", cost=['2', 'U'],
                  color_identity=['U'], card_type="Sorcery", sub_types="",
                  abilities=[23607], set_id="M19", rarity="Common", collectible=True, set_number=51,
                  mtga_id=67782)
DjinnofWishes = Card(name="djinn_of_wishes", pretty_name="Djinn of Wishes", cost=['3', 'U', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Djinn",
                     abilities=[8, 1111, 1112], set_id="M19", rarity="Rare", collectible=True, set_number=52,
                     mtga_id=67784)
Dwindle = Card(name="dwindle", pretty_name="Dwindle", cost=['2', 'U'],
               color_identity=['U'], card_type="Enchantment", sub_types="Aura",
               abilities=[1027, 20990, 119148], set_id="M19", rarity="Common", collectible=True, set_number=53,
               mtga_id=67786)
EssenceScatter = Card(name="essence_scatter", pretty_name="Essence Scatter", cost=['1', 'U'],
                      color_identity=['U'], card_type="Instant", sub_types="",
                      abilities=[24121], set_id="M19", rarity="Common", collectible=True, set_number=54,
                      mtga_id=67788)
ExclusionMage = Card(name="exclusion_mage", pretty_name="Exclusion Mage", cost=['2', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                     abilities=[96307], set_id="M19", rarity="Uncommon", collectible=True, set_number=55,
                     mtga_id=67790)
FrilledSeaSerpent = Card(name="frilled_sea_serpent", pretty_name="Frilled Sea Serpent", cost=['4', 'U', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Serpent",
                         abilities=[119156], set_id="M19", rarity="Common", collectible=True, set_number=56,
                         mtga_id=67792)
GearsmithProdigy = Card(name="gearsmith_prodigy", pretty_name="Gearsmith Prodigy", cost=['U'],
                        color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                        abilities=[103319], set_id="M19", rarity="Common", collectible=True, set_number=57,
                        mtga_id=67794)
Ghostform = Card(name="ghostform", pretty_name="Ghostform", cost=['1', 'U'],
                 color_identity=['U'], card_type="Sorcery", sub_types="",
                 abilities=[99695], set_id="M19", rarity="Common", collectible=True, set_number=58,
                 mtga_id=67796)
HorizonScholar = Card(name="horizon_scholar", pretty_name="Horizon Scholar", cost=['5', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                      abilities=[8, 100685], set_id="M19", rarity="Uncommon", collectible=True, set_number=59,
                      mtga_id=67798)
MetamorphicAlteration = Card(name="metamorphic_alteration", pretty_name="Metamorphic Alteration", cost=['1', 'U'],
                             color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                             abilities=[1027, 119174, 1078], set_id="M19", rarity="Rare", collectible=True, set_number=60,
                             mtga_id=67800)
MirrorImage = Card(name="mirror_image", pretty_name="Mirror Image", cost=['2', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Shapeshifter",
                   abilities=[119177], set_id="M19", rarity="Uncommon", collectible=True, set_number=61,
                   mtga_id=67802)
Mistcaller = Card(name="mistcaller", pretty_name="Mistcaller", cost=['U'],
                  color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                  abilities=[119180], set_id="M19", rarity="Rare", collectible=True, set_number=62,
                  mtga_id=67804)
MysticArchaeologist = Card(name="mystic_archaeologist", pretty_name="Mystic Archaeologist", cost=['1', 'U'],
                           color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                           abilities=[119182], set_id="M19", rarity="Rare", collectible=True, set_number=63,
                           mtga_id=67806)
Omenspeaker = Card(name="omenspeaker", pretty_name="Omenspeaker", cost=['1', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                   abilities=[100685], set_id="M19", rarity="Common", collectible=True, set_number=64,
                   mtga_id=67808)
Omniscience = Card(name="omniscience", pretty_name="Omniscience", cost=['7', 'U', 'U', 'U'],
                   color_identity=['U'], card_type="Enchantment", sub_types="",
                   abilities=[19205], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=65,
                   mtga_id=67810)
OnewiththeMachine = Card(name="one_with_the_machine", pretty_name="One with the Machine", cost=['3', 'U'],
                         color_identity=['U'], card_type="Sorcery", sub_types="",
                         abilities=[119185], set_id="M19", rarity="Rare", collectible=True, set_number=66,
                         mtga_id=67812)
PatientRebuilding = Card(name="patient_rebuilding", pretty_name="Patient Rebuilding", cost=['3', 'U', 'U'],
                         color_identity=['U'], card_type="Enchantment", sub_types="",
                         abilities=[119186], set_id="M19", rarity="Rare", collectible=True, set_number=67,
                         mtga_id=67814)
PsychicCorrosion = Card(name="psychic_corrosion", pretty_name="Psychic Corrosion", cost=['2', 'U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="",
                        abilities=[119187], set_id="M19", rarity="Uncommon", collectible=True, set_number=68,
                        mtga_id=67816)
SaiMasterThopterist = Card(name="sai_master_thopterist", pretty_name="Sai, Master Thopterist", cost=['2', 'U'],
                           color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                           abilities=[76777, 119188], set_id="M19", rarity="Rare", collectible=True, set_number=69,
                           mtga_id=67818)
SalvagerofSecrets = Card(name="salvager_of_secrets", pretty_name="Salvager of Secrets", cost=['3', 'U', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                         abilities=[90211], set_id="M19", rarity="Common", collectible=True, set_number=70,
                         mtga_id=67820)
ScholarofStars = Card(name="scholar_of_stars", pretty_name="Scholar of Stars", cost=['3', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                      abilities=[119190], set_id="M19", rarity="Common", collectible=True, set_number=71,
                      mtga_id=67822)
Sift = Card(name="sift", pretty_name="Sift", cost=['3', 'U'],
            color_identity=['U'], card_type="Sorcery", sub_types="",
            abilities=[6908], set_id="M19", rarity="Uncommon", collectible=True, set_number=72,
            mtga_id=67824)
SkilledAnimator = Card(name="skilled_animator", pretty_name="Skilled Animator", cost=['2', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                       abilities=[119191], set_id="M19", rarity="Uncommon", collectible=True, set_number=73,
                       mtga_id=67826)
Sleep = Card(name="sleep", pretty_name="Sleep", cost=['2', 'U', 'U'],
             color_identity=['U'], card_type="Sorcery", sub_types="",
             abilities=[92851], set_id="M19", rarity="Uncommon", collectible=True, set_number=74,
             mtga_id=67828)
SnappingDrake = Card(name="snapping_drake", pretty_name="Snapping Drake", cost=['3', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Drake",
                     abilities=[8], set_id="M19", rarity="Common", collectible=True, set_number=75,
                     mtga_id=67830)
SupremePhantom = Card(name="supreme_phantom", pretty_name="Supreme Phantom", cost=['1', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Spirit",
                      abilities=[8, 119192], set_id="M19", rarity="Rare", collectible=True, set_number=76,
                      mtga_id=67832)
SurgeMare = Card(name="surge_mare", pretty_name="Surge Mare", cost=['U', 'U'],
                 color_identity=['U'], card_type="Creature", sub_types="Horse Fish",
                 abilities=[97134, 119194, 119195], set_id="M19", rarity="Uncommon", collectible=True, set_number=77,
                 mtga_id=67834)
Switcheroo = Card(name="switcheroo", pretty_name="Switcheroo", cost=['4', 'U'],
                  color_identity=['U'], card_type="Sorcery", sub_types="",
                  abilities=[19199], set_id="M19", rarity="Uncommon", collectible=True, set_number=78,
                  mtga_id=67836)
TezzeretArtificeMaster = Card(name="tezzeret_artifice_master", pretty_name="Tezzeret, Artifice Master", cost=['3', 'U', 'U'],
                              color_identity=['U'], card_type="Planeswalker", sub_types="Tezzeret",
                              abilities=[119197, 119199, 119201], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=79,
                              mtga_id=67838)
TolarianScholar = Card(name="tolarian_scholar", pretty_name="Tolarian Scholar", cost=['2', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=80,
                       mtga_id=67840)
TotallyLost = Card(name="totally_lost", pretty_name="Totally Lost", cost=['4', 'U'],
                   color_identity=['U'], card_type="Instant", sub_types="",
                   abilities=[99758], set_id="M19", rarity="Common", collectible=True, set_number=81,
                   mtga_id=67842)
UncomfortableChill = Card(name="uncomfortable_chill", pretty_name="Uncomfortable Chill", cost=['2', 'U'],
                          color_identity=['U'], card_type="Instant", sub_types="",
                          abilities=[2920, 25848], set_id="M19", rarity="Common", collectible=True, set_number=82,
                          mtga_id=67844)
WallofMist = Card(name="wall_of_mist", pretty_name="Wall of Mist", cost=['1', 'U'],
                  color_identity=['U'], card_type="Creature", sub_types="Wall",
                  abilities=[2], set_id="M19", rarity="Common", collectible=True, set_number=83,
                  mtga_id=67846)
WindreaderSphinx = Card(name="windreader_sphinx", pretty_name="Windreader Sphinx", cost=['5', 'U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                        abilities=[8, 20301], set_id="M19", rarity="Rare", collectible=True, set_number=84,
                        mtga_id=67848)
AbnormalEndurance = Card(name="abnormal_endurance", pretty_name="Abnormal Endurance", cost=['1', 'B'],
                         color_identity=['B'], card_type="Instant", sub_types="",
                         abilities=[88098], set_id="M19", rarity="Common", collectible=True, set_number=85,
                         mtga_id=67850)
BloodDivination = Card(name="blood_divination", pretty_name="Blood Divination", cost=['3', 'B'],
                       color_identity=['B'], card_type="Sorcery", sub_types="",
                       abilities=[1275, 1746], set_id="M19", rarity="Uncommon", collectible=True, set_number=86,
                       mtga_id=67852)
Bogstomper = Card(name="bogstomper", pretty_name="Bogstomper", cost=['4', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Beast",
                  abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=87,
                  mtga_id=67854)
BoneDragon = Card(name="bone_dragon", pretty_name="Bone Dragon", cost=['3', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Dragon Skeleton",
                  abilities=[8, 119205], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=88,
                  mtga_id=67856)
ChildofNight = Card(name="child_of_night", pretty_name="Child of Night", cost=['1', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Vampire",
                    abilities=[12], set_id="M19", rarity="Common", collectible=True, set_number=89,
                    mtga_id=67858)
DeathBaron = Card(name="death_baron", pretty_name="Death Baron", cost=['1', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Zombie Wizard",
                  abilities=[5179], set_id="M19", rarity="Rare", collectible=True, set_number=90,
                  mtga_id=67860)
DemonofCatastrophes = Card(name="demon_of_catastrophes", pretty_name="Demon of Catastrophes", cost=['2', 'B', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Demon",
                           abilities=[1275, 8, 14], set_id="M19", rarity="Rare", collectible=True, set_number=91,
                           mtga_id=67862)
DiregrafGhoul = Card(name="diregraf_ghoul", pretty_name="Diregraf Ghoul", cost=['B'],
                     color_identity=['B'], card_type="Creature", sub_types="Zombie",
                     abilities=[76735], set_id="M19", rarity="Uncommon", collectible=True, set_number=92,
                     mtga_id=67864)
DoomedDissenter = Card(name="doomed_dissenter", pretty_name="Doomed Dissenter", cost=['1', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Human",
                       abilities=[88075], set_id="M19", rarity="Common", collectible=True, set_number=93,
                       mtga_id=67866)
Duress = Card(name="duress", pretty_name="Duress", cost=['B'],
              color_identity=['B'], card_type="Sorcery", sub_types="",
              abilities=[21775], set_id="M19", rarity="Common", collectible=True, set_number=94,
              mtga_id=67868)
EpicureofBlood = Card(name="epicure_of_blood", pretty_name="Epicure of Blood", cost=['4', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Vampire",
                      abilities=[62618], set_id="M19", rarity="Common", collectible=True, set_number=95,
                      mtga_id=67870)
FellSpecter = Card(name="fell_specter", pretty_name="Fell Specter", cost=['3', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Specter",
                   abilities=[8, 88244, 2904], set_id="M19", rarity="Uncommon", collectible=True, set_number=96,
                   mtga_id=67872)
FrayingOmnipotence = Card(name="fraying_omnipotence", pretty_name="Fraying Omnipotence", cost=['3', 'B', 'B'],
                          color_identity=['B'], card_type="Sorcery", sub_types="",
                          abilities=[119207], set_id="M19", rarity="Rare", collectible=True, set_number=97,
                          mtga_id=67874)
Gravedigger = Card(name="gravedigger", pretty_name="Gravedigger", cost=['3', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Zombie",
                   abilities=[1157], set_id="M19", rarity="Uncommon", collectible=True, set_number=98,
                   mtga_id=67876)
GraveyardMarshal = Card(name="graveyard_marshal", pretty_name="Graveyard Marshal", cost=['B', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Zombie Soldier",
                        abilities=[119208], set_id="M19", rarity="Rare", collectible=True, set_number=99,
                        mtga_id=67878)
HiredBlade = Card(name="hired_blade", pretty_name="Hired Blade", cost=['2', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Human Assassin",
                  abilities=[7], set_id="M19", rarity="Common", collectible=True, set_number=100,
                  mtga_id=67880)
InfectiousHorror = Card(name="infectious_horror", pretty_name="Infectious Horror", cost=['3', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Zombie Horror",
                        abilities=[90310], set_id="M19", rarity="Common", collectible=True, set_number=101,
                        mtga_id=67882)
InfernalReckoning = Card(name="infernal_reckoning", pretty_name="Infernal Reckoning", cost=['B'],
                         color_identity=['B'], card_type="Instant", sub_types="",
                         abilities=[119209], set_id="M19", rarity="Rare", collectible=True, set_number=102,
                         mtga_id=67884)
InfernalScarring = Card(name="infernal_scarring", pretty_name="Infernal Scarring", cost=['1', 'B'],
                        color_identity=['B'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 102264], set_id="M19", rarity="Common", collectible=True, set_number=103,
                        mtga_id=67886)
IsareththeAwakener = Card(name="isareth_the_awakener", pretty_name="Isareth the Awakener", cost=['1', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Human Wizard",
                          abilities=[1, 119210], set_id="M19", rarity="Rare", collectible=True, set_number=104,
                          mtga_id=67888)
LichsCaress = Card(name="lichs_caress", pretty_name="Lich's Caress", cost=['3', 'B', 'B'],
                   color_identity=['B'], card_type="Sorcery", sub_types="",
                   abilities=[119212], set_id="M19", rarity="Common", collectible=True, set_number=105,
                   mtga_id=67890)
LilianaUntouchedbyDeath = Card(name="liliana_untouched_by_death", pretty_name="Liliana, Untouched by Death", cost=['2', 'B', 'B'],
                               color_identity=['B'], card_type="Planeswalker", sub_types="Liliana",
                               abilities=[119213, 119214, 119215], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=106,
                               mtga_id=67892)
LilianasContract = Card(name="lilianas_contract", pretty_name="Liliana's Contract", cost=['3', 'B', 'B'],
                        color_identity=['B'], card_type="Enchantment", sub_types="",
                        abilities=[119216, 119084], set_id="M19", rarity="Rare", collectible=True, set_number=107,
                        mtga_id=67894)
MacabreWaltz = Card(name="macabre_waltz", pretty_name="Macabre Waltz", cost=['1', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[9569], set_id="M19", rarity="Common", collectible=True, set_number=108,
                    mtga_id=67896)
MindRot = Card(name="mind_rot", pretty_name="Mind Rot", cost=['2', 'B'],
               color_identity=['B'], card_type="Sorcery", sub_types="",
               abilities=[23608], set_id="M19", rarity="Common", collectible=True, set_number=109,
               mtga_id=67898)
Murder = Card(name="murder", pretty_name="Murder", cost=['1', 'B', 'B'],
              color_identity=['B'], card_type="Instant", sub_types="",
              abilities=[26818], set_id="M19", rarity="Uncommon", collectible=True, set_number=110,
              mtga_id=67900)
NightmaresThirst = Card(name="nightmares_thirst", pretty_name="Nightmare's Thirst", cost=['B'],
                        color_identity=['B'], card_type="Instant", sub_types="",
                        abilities=[119085], set_id="M19", rarity="Uncommon", collectible=True, set_number=111,
                        mtga_id=67902)
OpentheGraves = Card(name="open_the_graves", pretty_name="Open the Graves", cost=['3', 'B', 'B'],
                     color_identity=['B'], card_type="Enchantment", sub_types="",
                     abilities=[119086], set_id="M19", rarity="Rare", collectible=True, set_number=112,
                     mtga_id=67904)
PhylacteryLich = Card(name="phylactery_lich", pretty_name="Phylactery Lich", cost=['B', 'B', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Zombie",
                      abilities=[104, 92953, 92954], set_id="M19", rarity="Rare", collectible=True, set_number=113,
                      mtga_id=67906)
PlagueMare = Card(name="plague_mare", pretty_name="Plague Mare", cost=['1', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Nightmare Horse",
                  abilities=[97118, 119218], set_id="M19", rarity="Uncommon", collectible=True, set_number=114,
                  mtga_id=67908)
RavenousHarpy = Card(name="ravenous_harpy", pretty_name="Ravenous Harpy", cost=['2', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Harpy",
                     abilities=[8, 119088], set_id="M19", rarity="Uncommon", collectible=True, set_number=115,
                     mtga_id=67910)
ReassemblingSkeleton = Card(name="reassembling_skeleton", pretty_name="Reassembling Skeleton", cost=['1', 'B'],
                            color_identity=['B'], card_type="Creature", sub_types="Skeleton Warrior",
                            abilities=[1188], set_id="M19", rarity="Uncommon", collectible=True, set_number=116,
                            mtga_id=67912)
RisefromtheGrave = Card(name="rise_from_the_grave", pretty_name="Rise from the Grave", cost=['4', 'B'],
                        color_identity=['B'], card_type="Sorcery", sub_types="",
                        abilities=[2159], set_id="M19", rarity="Uncommon", collectible=True, set_number=117,
                        mtga_id=67914)
SkeletonArcher = Card(name="skeleton_archer", pretty_name="Skeleton Archer", cost=['3', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Skeleton Archer",
                      abilities=[92894], set_id="M19", rarity="Common", collectible=True, set_number=118,
                      mtga_id=67916)
SkymarchBloodletter = Card(name="skymarch_bloodletter", pretty_name="Skymarch Bloodletter", cost=['2', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                           abilities=[8, 91870], set_id="M19", rarity="Common", collectible=True, set_number=119,
                           mtga_id=67918)
SovereignsBite = Card(name="sovereigns_bite", pretty_name="Sovereign's Bite", cost=['1', 'B'],
                      color_identity=['B'], card_type="Sorcery", sub_types="",
                      abilities=[119090], set_id="M19", rarity="Common", collectible=True, set_number=120,
                      mtga_id=67920)
StitchersSupplier = Card(name="stitchers_supplier", pretty_name="Stitcher's Supplier", cost=['B'],
                         color_identity=['B'], card_type="Creature", sub_types="Zombie",
                         abilities=[119220], set_id="M19", rarity="Uncommon", collectible=True, set_number=121,
                         mtga_id=67922)
StranglingSpores = Card(name="strangling_spores", pretty_name="Strangling Spores", cost=['3', 'B'],
                        color_identity=['B'], card_type="Instant", sub_types="",
                        abilities=[2338], set_id="M19", rarity="Common", collectible=True, set_number=122,
                        mtga_id=67924)
TwoHeadedZombie = Card(name="twoheaded_zombie", pretty_name="Two-Headed Zombie", cost=['3', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Zombie",
                       abilities=[142], set_id="M19", rarity="Common", collectible=True, set_number=123,
                       mtga_id=67926)
VampireNeonate = Card(name="vampire_neonate", pretty_name="Vampire Neonate", cost=['B'],
                      color_identity=['B'], card_type="Creature", sub_types="Vampire",
                      abilities=[119221], set_id="M19", rarity="Common", collectible=True, set_number=124,
                      mtga_id=67928)
VampireSovereign = Card(name="vampire_sovereign", pretty_name="Vampire Sovereign", cost=['3', 'B', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Vampire",
                        abilities=[8, 119223], set_id="M19", rarity="Uncommon", collectible=True, set_number=125,
                        mtga_id=67930)
WalkingCorpse = Card(name="walking_corpse", pretty_name="Walking Corpse", cost=['1', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Zombie",
                     abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=126,
                     mtga_id=67932)
ActofTreason = Card(name="act_of_treason", pretty_name="Act of Treason", cost=['2', 'R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[1278], set_id="M19", rarity="Common", collectible=True, set_number=127,
                    mtga_id=67934)
AlpineMoon = Card(name="alpine_moon", pretty_name="Alpine Moon", cost=['R'],
                  color_identity=['R'], card_type="Enchantment", sub_types="",
                  abilities=[119225, 119226], set_id="M19", rarity="Rare", collectible=True, set_number=128,
                  mtga_id=67936)
ApexofPower = Card(name="apex_of_power", pretty_name="Apex of Power", cost=['7', 'R', 'R', 'R'],
                   color_identity=['R'], card_type="Sorcery", sub_types="",
                   abilities=[119227, 119091], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=129,
                   mtga_id=67938)
Banefire = Card(name="banefire", pretty_name="Banefire", cost=['X', 'R'],
                color_identity=['R'], card_type="Sorcery", sub_types="",
                abilities=[88144, 90322], set_id="M19", rarity="Rare", collectible=True, set_number=130,
                mtga_id=67940)
BoggartBrute = Card(name="boggart_brute", pretty_name="Boggart Brute", cost=['2', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                    abilities=[142], set_id="M19", rarity="Common", collectible=True, set_number=131,
                    mtga_id=67942)
CatalystElemental = Card(name="catalyst_elemental", pretty_name="Catalyst Elemental", cost=['2', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Elemental",
                         abilities=[92035], set_id="M19", rarity="Common", collectible=True, set_number=132,
                         mtga_id=67944)
CrashThrough = Card(name="crash_through", pretty_name="Crash Through", cost=['R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[103806, 25848], set_id="M19", rarity="Common", collectible=True, set_number=133,
                    mtga_id=67946)
DarkDwellerOracle = Card(name="darkdweller_oracle", pretty_name="Dark-Dweller Oracle", cost=['1', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin Shaman",
                         abilities=[119230], set_id="M19", rarity="Rare", collectible=True, set_number=134,
                         mtga_id=67948)
DemandingDragon = Card(name="demanding_dragon", pretty_name="Demanding Dragon", cost=['3', 'R', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Dragon",
                       abilities=[8, 119232], set_id="M19", rarity="Rare", collectible=True, set_number=135,
                       mtga_id=67950)
DismissivePyromancer = Card(name="dismissive_pyromancer", pretty_name="Dismissive Pyromancer", cost=['1', 'R'],
                            color_identity=['R'], card_type="Creature", sub_types="Human Wizard",
                            abilities=[20793, 119234], set_id="M19", rarity="Rare", collectible=True, set_number=136,
                            mtga_id=67952)
Doublecast = Card(name="doublecast", pretty_name="Doublecast", cost=['R', 'R'],
                  color_identity=['R'], card_type="Sorcery", sub_types="",
                  abilities=[119092], set_id="M19", rarity="Uncommon", collectible=True, set_number=137,
                  mtga_id=67954)
DragonEgg = Card(name="dragon_egg", pretty_name="Dragon Egg", cost=['2', 'R'],
                 color_identity=['R'], card_type="Creature", sub_types="Dragon Egg",
                 abilities=[2, 100587], set_id="M19", rarity="Uncommon", collectible=True, set_number=138,
                 mtga_id=67956)
Electrify = Card(name="electrify", pretty_name="Electrify", cost=['3', 'R'],
                 color_identity=['R'], card_type="Instant", sub_types="",
                 abilities=[21773], set_id="M19", rarity="Common", collectible=True, set_number=139,
                 mtga_id=67958)
FieryFinish = Card(name="fiery_finish", pretty_name="Fiery Finish", cost=['4', 'R', 'R'],
                   color_identity=['R'], card_type="Sorcery", sub_types="",
                   abilities=[88112], set_id="M19", rarity="Uncommon", collectible=True, set_number=140,
                   mtga_id=67960)
FireElemental = Card(name="fire_elemental", pretty_name="Fire Elemental", cost=['3', 'R', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Elemental",
                     abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=141,
                     mtga_id=67962)
GoblinInstigator = Card(name="goblin_instigator", pretty_name="Goblin Instigator", cost=['1', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Goblin Rogue",
                        abilities=[119237], set_id="M19", rarity="Common", collectible=True, set_number=142,
                        mtga_id=67964)
GoblinMotivator = Card(name="goblin_motivator", pretty_name="Goblin Motivator", cost=['R'],
                       color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                       abilities=[15166], set_id="M19", rarity="Common", collectible=True, set_number=143,
                       mtga_id=67966)
GoblinTrashmaster = Card(name="goblin_trashmaster", pretty_name="Goblin Trashmaster", cost=['2', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                         abilities=[119238, 119239], set_id="M19", rarity="Rare", collectible=True, set_number=144,
                         mtga_id=67968)
Guttersnipe = Card(name="guttersnipe", pretty_name="Guttersnipe", cost=['2', 'R'],
                   color_identity=['R'], card_type="Creature", sub_types="Goblin Shaman",
                   abilities=[100026], set_id="M19", rarity="Uncommon", collectible=True, set_number=145,
                   mtga_id=67970)
HavocDevils = Card(name="havoc_devils", pretty_name="Havoc Devils", cost=['2', 'R', 'R'],
                   color_identity=['R'], card_type="Creature", sub_types="Devil",
                   abilities=[14], set_id="M19", rarity="Common", collectible=True, set_number=146,
                   mtga_id=67972)
HostileMinotaur = Card(name="hostile_minotaur", pretty_name="Hostile Minotaur", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Minotaur",
                       abilities=[9], set_id="M19", rarity="Common", collectible=True, set_number=147,
                       mtga_id=67974)
InfernoHellion = Card(name="inferno_hellion", pretty_name="Inferno Hellion", cost=['3', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Hellion",
                      abilities=[14, 119198], set_id="M19", rarity="Uncommon", collectible=True, set_number=148,
                      mtga_id=67976)
LathlissDragonQueen = Card(name="lathliss_dragon_queen", pretty_name="Lathliss, Dragon Queen", cost=['4', 'R', 'R'],
                           color_identity=['R'], card_type="Creature", sub_types="Dragon",
                           abilities=[8, 119241, 119242], set_id="M19", rarity="Rare", collectible=True, set_number=149,
                           mtga_id=67978)
LavaAxe = Card(name="lava_axe", pretty_name="Lava Axe", cost=['4', 'R'],
               color_identity=['R'], card_type="Sorcery", sub_types="",
               abilities=[1118], set_id="M19", rarity="Common", collectible=True, set_number=150,
               mtga_id=67980)
LightningMare = Card(name="lightning_mare", pretty_name="Lightning Mare", cost=['R', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Elemental Horse",
                     abilities=[120287, 92274, 88126], set_id="M19", rarity="Uncommon", collectible=True, set_number=151,
                     mtga_id=67982)
LightningStrike = Card(name="lightning_strike", pretty_name="Lightning Strike", cost=['1', 'R'],
                       color_identity=['R'], card_type="Instant", sub_types="",
                       abilities=[70361], set_id="M19", rarity="Uncommon", collectible=True, set_number=152,
                       mtga_id=67984)
OnakkeOgre = Card(name="onakke_ogre", pretty_name="Onakke Ogre", cost=['2', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Ogre Warrior",
                  abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=153,
                  mtga_id=67986)
SarkhanFireblood = Card(name="sarkhan_fireblood", pretty_name="Sarkhan, Fireblood", cost=['1', 'R', 'R'],
                        color_identity=['R'], card_type="Planeswalker", sub_types="Sarkhan",
                        abilities=[119245, 119246, 119247], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=154,
                        mtga_id=67988)
SarkhansUnsealing = Card(name="sarkhans_unsealing", pretty_name="Sarkhan's Unsealing", cost=['3', 'R'],
                         color_identity=['R'], card_type="Enchantment", sub_types="",
                         abilities=[119249, 119251], set_id="M19", rarity="Rare", collectible=True, set_number=155,
                         mtga_id=67990)
Shock = Card(name="shock", pretty_name="Shock", cost=['R'],
             color_identity=['R'], card_type="Instant", sub_types="",
             abilities=[86613], set_id="M19", rarity="Common", collectible=True, set_number=156,
             mtga_id=67992)
SiegebreakerGiant = Card(name="siegebreaker_giant", pretty_name="Siegebreaker Giant", cost=['3', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Giant Warrior",
                         abilities=[14, 119252], set_id="M19", rarity="Uncommon", collectible=True, set_number=157,
                         mtga_id=67994)
Smelt = Card(name="smelt", pretty_name="Smelt", cost=['R'],
             color_identity=['R'], card_type="Instant", sub_types="",
             abilities=[22564], set_id="M19", rarity="Common", collectible=True, set_number=158,
             mtga_id=67996)
SparktongueDragon = Card(name="sparktongue_dragon", pretty_name="Sparktongue Dragon", cost=['3', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Dragon",
                         abilities=[8, 119253], set_id="M19", rarity="Common", collectible=True, set_number=159,
                         mtga_id=67998)
SpitFlame = Card(name="spit_flame", pretty_name="Spit Flame", cost=['2', 'R'],
                 color_identity=['R'], card_type="Instant", sub_types="",
                 abilities=[21773, 119254], set_id="M19", rarity="Rare", collectible=True, set_number=160,
                 mtga_id=68000)
SureStrike = Card(name="sure_strike", pretty_name="Sure Strike", cost=['1', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[1019], set_id="M19", rarity="Common", collectible=True, set_number=161,
                  mtga_id=68002)
TectonicRift = Card(name="tectonic_rift", pretty_name="Tectonic Rift", cost=['3', 'R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[1098], set_id="M19", rarity="Uncommon", collectible=True, set_number=162,
                    mtga_id=68004)
Thud = Card(name="thud", pretty_name="Thud", cost=['R'],
            color_identity=['R'], card_type="Sorcery", sub_types="",
            abilities=[1275, 1276], set_id="M19", rarity="Uncommon", collectible=True, set_number=163,
            mtga_id=68006)
TormentingVoice = Card(name="tormenting_voice", pretty_name="Tormenting Voice", cost=['1', 'R'],
                       color_identity=['R'], card_type="Sorcery", sub_types="",
                       abilities=[87929, 23607], set_id="M19", rarity="Common", collectible=True, set_number=164,
                       mtga_id=68008)
TrumpetBlast = Card(name="trumpet_blast", pretty_name="Trumpet Blast", cost=['2', 'R'],
                    color_identity=['R'], card_type="Instant", sub_types="",
                    abilities=[11569], set_id="M19", rarity="Common", collectible=True, set_number=165,
                    mtga_id=68010)
ViashinoPyromancer = Card(name="viashino_pyromancer", pretty_name="Viashino Pyromancer", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Viashino Wizard",
                          abilities=[119095], set_id="M19", rarity="Common", collectible=True, set_number=166,
                          mtga_id=68012)
VolcanicDragon = Card(name="volcanic_dragon", pretty_name="Volcanic Dragon", cost=['4', 'R', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Dragon",
                      abilities=[8, 9], set_id="M19", rarity="Uncommon", collectible=True, set_number=167,
                      mtga_id=68014)
VolleyVeteran = Card(name="volley_veteran", pretty_name="Volley Veteran", cost=['3', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                     abilities=[119096], set_id="M19", rarity="Uncommon", collectible=True, set_number=168,
                     mtga_id=68016)
BlanchwoodArmor = Card(name="blanchwood_armor", pretty_name="Blanchwood Armor", cost=['2', 'G'],
                       color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                       abilities=[1027, 1438], set_id="M19", rarity="Uncommon", collectible=True, set_number=169,
                       mtga_id=68018)
BristlingBoar = Card(name="bristling_boar", pretty_name="Bristling Boar", cost=['3', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Boar",
                     abilities=[1026], set_id="M19", rarity="Common", collectible=True, set_number=170,
                     mtga_id=68020)
CentaurCourser = Card(name="centaur_courser", pretty_name="Centaur Courser", cost=['2', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Centaur Warrior",
                      abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=171,
                      mtga_id=68022)
ColossalDreadmaw = Card(name="colossal_dreadmaw", pretty_name="Colossal Dreadmaw", cost=['4', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[14], set_id="M19", rarity="Common", collectible=True, set_number=172,
                        mtga_id=68024)
ColossalMajesty = Card(name="colossal_majesty", pretty_name="Colossal Majesty", cost=['2', 'G'],
                       color_identity=['G'], card_type="Enchantment", sub_types="",
                       abilities=[119097], set_id="M19", rarity="Uncommon", collectible=True, set_number=173,
                       mtga_id=68026)
DaggerbackBasilisk = Card(name="daggerback_basilisk", pretty_name="Daggerback Basilisk", cost=['2', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Basilisk",
                          abilities=[1], set_id="M19", rarity="Common", collectible=True, set_number=174,
                          mtga_id=68028)
DeclareDominance = Card(name="declare_dominance", pretty_name="Declare Dominance", cost=['3', 'G', 'G'],
                        color_identity=['G'], card_type="Sorcery", sub_types="",
                        abilities=[119098], set_id="M19", rarity="Uncommon", collectible=True, set_number=175,
                        mtga_id=68030)
DruidofHorns = Card(name="druid_of_horns", pretty_name="Druid of Horns", cost=['3', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Human Druid",
                    abilities=[119099], set_id="M19", rarity="Uncommon", collectible=True, set_number=176,
                    mtga_id=68032)
DruidoftheCowl = Card(name="druid_of_the_cowl", pretty_name="Druid of the Cowl", cost=['1', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                      abilities=[1005], set_id="M19", rarity="Common", collectible=True, set_number=177,
                      mtga_id=68034)
DryadGreenseeker = Card(name="dryad_greenseeker", pretty_name="Dryad Greenseeker", cost=['1', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dryad",
                        abilities=[119100], set_id="M19", rarity="Uncommon", collectible=True, set_number=178,
                        mtga_id=68036)
ElvishClancaller = Card(name="elvish_clancaller", pretty_name="Elvish Clancaller", cost=['G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                        abilities=[119184, 119102], set_id="M19", rarity="Rare", collectible=True, set_number=179,
                        mtga_id=68038)
ElvishRejuvenator = Card(name="elvish_rejuvenator", pretty_name="Elvish Rejuvenator", cost=['2', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                         abilities=[119103], set_id="M19", rarity="Common", collectible=True, set_number=180,
                         mtga_id=68040)
GhastbarkTwins = Card(name="ghastbark_twins", pretty_name="Ghastbark Twins", cost=['5', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Treefolk",
                      abilities=[14, 76869], set_id="M19", rarity="Uncommon", collectible=True, set_number=181,
                      mtga_id=68042)
GhirapurGuide = Card(name="ghirapur_guide", pretty_name="Ghirapur Guide", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                     abilities=[103385], set_id="M19", rarity="Uncommon", collectible=True, set_number=182,
                     mtga_id=68044)
GiantSpider = Card(name="giant_spider", pretty_name="Giant Spider", cost=['3', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Spider",
                   abilities=[13], set_id="M19", rarity="Common", collectible=True, set_number=183,
                   mtga_id=68046)
GiftofParadise = Card(name="gift_of_paradise", pretty_name="Gift of Paradise", cost=['2', 'G'],
                      color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                      abilities=[1570, 1102, 61119], set_id="M19", rarity="Uncommon", collectible=True, set_number=184,
                      mtga_id=68048)
Gigantosaurus = Card(name="gigantosaurus", pretty_name="Gigantosaurus", cost=['G', 'G', 'G', 'G', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                     abilities=[], set_id="M19", rarity="Rare", collectible=True, set_number=185,
                     mtga_id=68050)
GoreclawTerrorofQalSisma = Card(name="goreclaw_terror_of_qal_sisma", pretty_name="Goreclaw, Terror of Qal Sisma", cost=['3', 'G'],
                                color_identity=['G'], card_type="Creature", sub_types="Bear",
                                abilities=[119105, 119106], set_id="M19", rarity="Rare", collectible=True, set_number=186,
                                mtga_id=68052)
GreenwoodSentinel = Card(name="greenwood_sentinel", pretty_name="Greenwood Sentinel", cost=['1', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                         abilities=[15], set_id="M19", rarity="Common", collectible=True, set_number=187,
                         mtga_id=68054)
HighlandGame = Card(name="highland_game", pretty_name="Highland Game", cost=['1', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Elk",
                    abilities=[93266], set_id="M19", rarity="Common", collectible=True, set_number=188,
                    mtga_id=68056)
HungeringHydra = Card(name="hungering_hydra", pretty_name="Hungering Hydra", cost=['X', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Hydra",
                      abilities=[76885, 1026, 119108], set_id="M19", rarity="Rare", collectible=True, set_number=189,
                      mtga_id=68058)
Naturalize = Card(name="naturalize", pretty_name="Naturalize", cost=['1', 'G'],
                  color_identity=['G'], card_type="Instant", sub_types="",
                  abilities=[120290], set_id="M19", rarity="Common", collectible=True, set_number=190,
                  mtga_id=68060)
Oakenform = Card(name="oakenform", pretty_name="Oakenform", cost=['2', 'G'],
                 color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                 abilities=[1027, 1318], set_id="M19", rarity="Common", collectible=True, set_number=191,
                 mtga_id=68062)
PelakkaWurm = Card(name="pelakka_wurm", pretty_name="Pelakka Wurm", cost=['4', 'G', 'G', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Wurm",
                   abilities=[14, 17518, 17519], set_id="M19", rarity="Rare", collectible=True, set_number=192,
                   mtga_id=68064)
Plummet = Card(name="plummet", pretty_name="Plummet", cost=['1', 'G'],
               color_identity=['G'], card_type="Instant", sub_types="",
               abilities=[29759], set_id="M19", rarity="Common", collectible=True, set_number=193,
               mtga_id=68066)
ProdigiousGrowth = Card(name="prodigious_growth", pretty_name="Prodigious Growth", cost=['4', 'G', 'G'],
                        color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 119110], set_id="M19", rarity="Rare", collectible=True, set_number=194,
                        mtga_id=68068)
RabidBite = Card(name="rabid_bite", pretty_name="Rabid Bite", cost=['1', 'G'],
                 color_identity=['G'], card_type="Sorcery", sub_types="",
                 abilities=[61234], set_id="M19", rarity="Common", collectible=True, set_number=195,
                 mtga_id=68070)
ReclamationSage = Card(name="reclamation_sage", pretty_name="Reclamation Sage", cost=['2', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Elf Shaman",
                       abilities=[101429], set_id="M19", rarity="Uncommon", collectible=True, set_number=196,
                       mtga_id=68072)
Recollect = Card(name="recollect", pretty_name="Recollect", cost=['2', 'G'],
                 color_identity=['G'], card_type="Sorcery", sub_types="",
                 abilities=[6082], set_id="M19", rarity="Uncommon", collectible=True, set_number=197,
                 mtga_id=68074)
RhoxOracle = Card(name="rhox_oracle", pretty_name="Rhox Oracle", cost=['4', 'G'],
                  color_identity=['G'], card_type="Creature", sub_types="Rhino Monk",
                  abilities=[86788], set_id="M19", rarity="Common", collectible=True, set_number=198,
                  mtga_id=68076)
RootSnare = Card(name="root_snare", pretty_name="Root Snare", cost=['1', 'G'],
                 color_identity=['G'], card_type="Instant", sub_types="",
                 abilities=[27746], set_id="M19", rarity="Common", collectible=True, set_number=199,
                 mtga_id=68078)
RunicArmasaur = Card(name="runic_armasaur", pretty_name="Runic Armasaur", cost=['1', 'G', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                     abilities=[119111], set_id="M19", rarity="Rare", collectible=True, set_number=200,
                     mtga_id=68080)
Scapeshift = Card(name="scapeshift", pretty_name="Scapeshift", cost=['2', 'G', 'G'],
                  color_identity=['G'], card_type="Sorcery", sub_types="",
                  abilities=[15392], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=201,
                  mtga_id=68082)
TalonsofWildwood = Card(name="talons_of_wildwood", pretty_name="Talons of Wildwood", cost=['1', 'G'],
                        color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 15269, 119112], set_id="M19", rarity="Common", collectible=True, set_number=202,
                        mtga_id=68084)
ThornLieutenant = Card(name="thorn_lieutenant", pretty_name="Thorn Lieutenant", cost=['1', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Elf Warrior",
                       abilities=[119113, 102965], set_id="M19", rarity="Rare", collectible=True, set_number=203,
                       mtga_id=68086)
ThornhideWolves = Card(name="thornhide_wolves", pretty_name="Thornhide Wolves", cost=['4', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Wolf",
                       abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=204,
                       mtga_id=68088)
TitanicGrowth = Card(name="titanic_growth", pretty_name="Titanic Growth", cost=['1', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[1031], set_id="M19", rarity="Common", collectible=True, set_number=205,
                     mtga_id=68090)
VigilantBaloth = Card(name="vigilant_baloth", pretty_name="Vigilant Baloth", cost=['3', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Beast",
                      abilities=[15], set_id="M19", rarity="Uncommon", collectible=True, set_number=206,
                      mtga_id=68092)
VineMare = Card(name="vine_mare", pretty_name="Vine Mare", cost=['2', 'G', 'G'],
                color_identity=['G'], card_type="Creature", sub_types="Elemental Horse",
                abilities=[10, 97144], set_id="M19", rarity="Uncommon", collectible=True, set_number=207,
                mtga_id=68094)
VivienReid = Card(name="vivien_reid", pretty_name="Vivien Reid", cost=['3', 'G', 'G'],
                  color_identity=['G'], card_type="Planeswalker", sub_types="Vivien",
                  abilities=[119115, 119116, 119147], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=208,
                  mtga_id=68096)
ViviensInvocation = Card(name="viviens_invocation", pretty_name="Vivien's Invocation", cost=['5', 'G', 'G'],
                         color_identity=['G'], card_type="Sorcery", sub_types="",
                         abilities=[119149], set_id="M19", rarity="Rare", collectible=True, set_number=209,
                         mtga_id=68098)
WallofVines = Card(name="wall_of_vines", pretty_name="Wall of Vines", cost=['G'],
                   color_identity=['G'], card_type="Creature", sub_types="Plant Wall",
                   abilities=[2, 13], set_id="M19", rarity="Common", collectible=True, set_number=210,
                   mtga_id=68100)
AerialEngineer = Card(name="aerial_engineer", pretty_name="Aerial Engineer", cost=['2', 'W', 'U'],
                      color_identity=['W', 'U'], card_type="Creature", sub_types="Human Artificer",
                      abilities=[119152], set_id="M19", rarity="Uncommon", collectible=True, set_number=211,
                      mtga_id=68102)
ArcadestheStrategist = Card(name="arcades_the_strategist", pretty_name="Arcades, the Strategist", cost=['1', 'G', 'W', 'U'],
                            color_identity=['W', 'U', 'G'], card_type="Creature", sub_types="Elder Dragon",
                            abilities=[8, 15, 119118, 119119], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=212,
                            mtga_id=68104)
BrawlBashOgre = Card(name="brawlbash_ogre", pretty_name="Brawl-Bash Ogre", cost=['2', 'B', 'R'],
                     color_identity=['B', 'R'], card_type="Creature", sub_types="Ogre Warrior",
                     abilities=[142, 119120], set_id="M19", rarity="Uncommon", collectible=True, set_number=213,
                     mtga_id=68106)
ChromiumtheMutable = Card(name="chromium_the_mutable", pretty_name="Chromium, the Mutable", cost=['4', 'W', 'U', 'B'],
                          color_identity=['W', 'U', 'B'], card_type="Creature", sub_types="Elder Dragon",
                          abilities=[7, 120287, 8, 119171], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=214,
                          mtga_id=68108)
DraconicDisciple = Card(name="draconic_disciple", pretty_name="Draconic Disciple", cost=['1', 'R', 'G'],
                        color_identity=['R', 'G'], card_type="Creature", sub_types="Human Shaman",
                        abilities=[1055, 119121], set_id="M19", rarity="Uncommon", collectible=True, set_number=215,
                        mtga_id=68110)
EnigmaDrake = Card(name="enigma_drake", pretty_name="Enigma Drake", cost=['1', 'U', 'R'],
                   color_identity=['U', 'R'], card_type="Creature", sub_types="Drake",
                   abilities=[8, 87971], set_id="M19", rarity="Uncommon", collectible=True, set_number=216,
                   mtga_id=68112)
HeroicReinforcements = Card(name="heroic_reinforcements", pretty_name="Heroic Reinforcements", cost=['2', 'R', 'W'],
                            color_identity=['R', 'W'], card_type="Sorcery", sub_types="",
                            abilities=[119122], set_id="M19", rarity="Uncommon", collectible=True, set_number=217,
                            mtga_id=68114)
NicolBolastheRavager = Card(name="nicol_bolas_the_ravager", pretty_name="Nicol Bolas, the Ravager", cost=['1', 'U', 'B', 'R'],
                            color_identity=['U', 'B', 'R'], card_type="Creature", sub_types="Elder Dragon",
                            abilities=[8, 92927, 119123], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=218,
                            mtga_id=68116)
NicolBolastheArisen = Card(name="nicol_bolas_the_arisen", pretty_name="Nicol Bolas, the Arisen", cost=[],
                           color_identity=['U', 'B', 'R'], card_type="Planeswalker", sub_types="Bolas",
                           abilities=[119183, 119124, 119125, 119126], set_id="M19", rarity="Mythic Rare", collectible=False, set_number=218,
                           mtga_id=68118)
PalladiaMorstheRuiner = Card(name="palladiamors_the_ruiner", pretty_name="Palladia-Mors, the Ruiner", cost=['3', 'R', 'G', 'W'],
                             color_identity=['W', 'R', 'G'], card_type="Creature", sub_types="Elder Dragon",
                             abilities=[8, 15, 14, 119127], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=219,
                             mtga_id=68120)
PoisonTipArcher = Card(name="poisontip_archer", pretty_name="Poison-Tip Archer", cost=['2', 'B', 'G'],
                       color_identity=['B', 'G'], card_type="Creature", sub_types="Elf Archer",
                       abilities=[13, 1, 119128], set_id="M19", rarity="Uncommon", collectible=True, set_number=220,
                       mtga_id=68122)
PsychicSymbiont = Card(name="psychic_symbiont", pretty_name="Psychic Symbiont", cost=['4', 'U', 'B'],
                       color_identity=['U', 'B'], card_type="Creature", sub_types="Nightmare Horror",
                       abilities=[8, 119189], set_id="M19", rarity="Uncommon", collectible=True, set_number=221,
                       mtga_id=68124)
RegalBloodlord = Card(name="regal_bloodlord", pretty_name="Regal Bloodlord", cost=['3', 'W', 'B'],
                      color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire Soldier",
                      abilities=[8, 119129], set_id="M19", rarity="Uncommon", collectible=True, set_number=222,
                      mtga_id=68126)
SatyrEnchanter = Card(name="satyr_enchanter", pretty_name="Satyr Enchanter", cost=['1', 'G', 'W'],
                      color_identity=['G', 'W'], card_type="Creature", sub_types="Satyr Druid",
                      abilities=[13572], set_id="M19", rarity="Uncommon", collectible=True, set_number=223,
                      mtga_id=68128)
SkyriderPatrol = Card(name="skyrider_patrol", pretty_name="Skyrider Patrol", cost=['2', 'G', 'U'],
                      color_identity=['G', 'U'], card_type="Creature", sub_types="Elf Scout",
                      abilities=[8, 119130], set_id="M19", rarity="Uncommon", collectible=True, set_number=224,
                      mtga_id=68130)
VaevictisAsmaditheDire = Card(name="vaevictis_asmadi_the_dire", pretty_name="Vaevictis Asmadi, the Dire", cost=['3', 'B', 'R', 'G'],
                              color_identity=['B', 'R', 'G'], card_type="Creature", sub_types="Elder Dragon",
                              abilities=[8, 119131], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=225,
                              mtga_id=68132)
AmuletofSafekeeping = Card(name="amulet_of_safekeeping", pretty_name="Amulet of Safekeeping", cost=['2'],
                           color_identity=[], card_type="Artifact", sub_types="",
                           abilities=[119132, 119193], set_id="M19", rarity="Rare", collectible=True, set_number=226,
                           mtga_id=68134)
ArcaneEncyclopedia = Card(name="arcane_encyclopedia", pretty_name="Arcane Encyclopedia", cost=['3'],
                          color_identity=[], card_type="Artifact", sub_types="",
                          abilities=[119134], set_id="M19", rarity="Uncommon", collectible=True, set_number=227,
                          mtga_id=68136)
ChaosWand = Card(name="chaos_wand", pretty_name="Chaos Wand", cost=['3'],
                 color_identity=[], card_type="Artifact", sub_types="",
                 abilities=[119196], set_id="M19", rarity="Rare", collectible=True, set_number=228,
                 mtga_id=68138)
CrucibleofWorlds = Card(name="crucible_of_worlds", pretty_name="Crucible of Worlds", cost=['3'],
                        color_identity=[], card_type="Artifact", sub_types="",
                        abilities=[6832], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=229,
                        mtga_id=68140)
DesecratedTomb = Card(name="desecrated_tomb", pretty_name="Desecrated Tomb", cost=['3'],
                      color_identity=[], card_type="Artifact", sub_types="",
                      abilities=[119135], set_id="M19", rarity="Rare", collectible=True, set_number=230,
                      mtga_id=68142)
DiamondMare = Card(name="diamond_mare", pretty_name="Diamond Mare", cost=['2'],
                   color_identity=[], card_type="Artifact Creature", sub_types="Horse",
                   abilities=[88237, 62127], set_id="M19", rarity="Uncommon", collectible=True, set_number=231,
                   mtga_id=68144)
DragonsHoard = Card(name="dragons_hoard", pretty_name="Dragon's Hoard", cost=['3'],
                    color_identity=[], card_type="Artifact", sub_types="",
                    abilities=[119202, 119138, 1055], set_id="M19", rarity="Rare", collectible=True, set_number=232,
                    mtga_id=68146)
ExplosiveApparatus = Card(name="explosive_apparatus", pretty_name="Explosive Apparatus", cost=['1'],
                          color_identity=[], card_type="Artifact", sub_types="",
                          abilities=[103005], set_id="M19", rarity="Common", collectible=True, set_number=233,
                          mtga_id=68148)
FieldCreeper = Card(name="field_creeper", pretty_name="Field Creeper", cost=['2'],
                    color_identity=[], card_type="Artifact Creature", sub_types="Scarecrow",
                    abilities=[], set_id="M19", rarity="Common", collectible=True, set_number=234,
                    mtga_id=68150)
FountainofRenewal = Card(name="fountain_of_renewal", pretty_name="Fountain of Renewal", cost=['1'],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[21074, 119139], set_id="M19", rarity="Uncommon", collectible=True, set_number=235,
                         mtga_id=68152)
GargoyleSentinel = Card(name="gargoyle_sentinel", pretty_name="Gargoyle Sentinel", cost=['3'],
                        color_identity=[], card_type="Artifact Creature", sub_types="Gargoyle",
                        abilities=[2, 92921], set_id="M19", rarity="Uncommon", collectible=True, set_number=236,
                        mtga_id=68154)
GearsmithGuardian = Card(name="gearsmith_guardian", pretty_name="Gearsmith Guardian", cost=['5'],
                         color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                         abilities=[119140], set_id="M19", rarity="Common", collectible=True, set_number=237,
                         mtga_id=68156)
MagistratesScepter = Card(name="magistrates_scepter", pretty_name="Magistrate's Scepter", cost=['3'],
                          color_identity=[], card_type="Artifact", sub_types="",
                          abilities=[94489, 94490], set_id="M19", rarity="Rare", collectible=True, set_number=238,
                          mtga_id=68158)
Manalith = Card(name="manalith", pretty_name="Manalith", cost=['3'],
                color_identity=[], card_type="Artifact", sub_types="",
                abilities=[1055], set_id="M19", rarity="Common", collectible=True, set_number=239,
                mtga_id=68160)
MaraudersAxe = Card(name="marauders_axe", pretty_name="Marauder's Axe", cost=['2'],
                    color_identity=[], card_type="Artifact", sub_types="Equipment",
                    abilities=[4712, 1319], set_id="M19", rarity="Common", collectible=True, set_number=240,
                    mtga_id=68162)
MeteorGolem = Card(name="meteor_golem", pretty_name="Meteor Golem", cost=['7'],
                   color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                   abilities=[119141], set_id="M19", rarity="Uncommon", collectible=True, set_number=241,
                   mtga_id=68164)
Millstone = Card(name="millstone", pretty_name="Millstone", cost=['2'],
                 color_identity=[], card_type="Artifact", sub_types="",
                 abilities=[1588], set_id="M19", rarity="Uncommon", collectible=True, set_number=242,
                 mtga_id=68166)
RoguesGloves = Card(name="rogues_gloves", pretty_name="Rogue's Gloves", cost=['2'],
                    color_identity=[], card_type="Artifact", sub_types="Equipment",
                    abilities=[7642, 1319], set_id="M19", rarity="Uncommon", collectible=True, set_number=243,
                    mtga_id=68168)
SigiledSwordofValeron = Card(name="sigiled_sword_of_valeron", pretty_name="Sigiled Sword of Valeron", cost=['3'],
                             color_identity=[], card_type="Artifact", sub_types="Equipment",
                             abilities=[119142, 119143, 1156], set_id="M19", rarity="Rare", collectible=True, set_number=244,
                             mtga_id=68170)
Skyscanner = Card(name="skyscanner", pretty_name="Skyscanner", cost=['3'],
                  color_identity=[], card_type="Artifact Creature", sub_types="Thopter",
                  abilities=[8, 86788], set_id="M19", rarity="Common", collectible=True, set_number=245,
                  mtga_id=68172)
SuspiciousBookcase = Card(name="suspicious_bookcase", pretty_name="Suspicious Bookcase", cost=['2'],
                          color_identity=[], card_type="Artifact Creature", sub_types="Wall",
                          abilities=[2, 119144], set_id="M19", rarity="Uncommon", collectible=True, set_number=246,
                          mtga_id=68174)
TransmogrifyingWand = Card(name="transmogrifying_wand", pretty_name="Transmogrifying Wand", cost=['3'],
                           color_identity=[], card_type="Artifact", sub_types="",
                           abilities=[93150, 119145], set_id="M19", rarity="Rare", collectible=True, set_number=247,
                           mtga_id=68176)
CinderBarrens = Card(name="cinder_barrens", pretty_name="Cinder Barrens", cost=[],
                     color_identity=['B', 'R'], card_type="Land", sub_types="",
                     abilities=[76735, 1211], set_id="M19", rarity="Common", collectible=True, set_number=248,
                     mtga_id=68178)
DetectionTower = Card(name="detection_tower", pretty_name="Detection Tower", cost=[],
                      color_identity=[], card_type="Land", sub_types="",
                      abilities=[1152, 119211], set_id="M19", rarity="Rare", collectible=True, set_number=249,
                      mtga_id=68180)
ForsakenSanctuary = Card(name="forsaken_sanctuary", pretty_name="Forsaken Sanctuary", cost=[],
                         color_identity=['W', 'B'], card_type="Land", sub_types="",
                         abilities=[76735, 18472], set_id="M19", rarity="Common", collectible=True, set_number=250,
                         mtga_id=68182)
FoulOrchard = Card(name="foul_orchard", pretty_name="Foul Orchard", cost=[],
                   color_identity=['B', 'G'], card_type="Land", sub_types="",
                   abilities=[76735, 4407], set_id="M19", rarity="Common", collectible=True, set_number=251,
                   mtga_id=68184)
HighlandLake = Card(name="highland_lake", pretty_name="Highland Lake", cost=[],
                    color_identity=['U', 'R'], card_type="Land", sub_types="",
                    abilities=[76735, 1039], set_id="M19", rarity="Common", collectible=True, set_number=252,
                    mtga_id=68186)
MeanderingRiver = Card(name="meandering_river", pretty_name="Meandering River", cost=[],
                       color_identity=['W', 'U'], card_type="Land", sub_types="",
                       abilities=[76735, 1209], set_id="M19", rarity="Common", collectible=True, set_number=253,
                       mtga_id=68188)
ReliquaryTower = Card(name="reliquary_tower", pretty_name="Reliquary Tower", cost=[],
                      color_identity=[], card_type="Land", sub_types="",
                      abilities=[1640, 1152], set_id="M19", rarity="Uncommon", collectible=True, set_number=254,
                      mtga_id=68190)
RuptureSpire = Card(name="rupture_spire", pretty_name="Rupture Spire", cost=[],
                    color_identity=[], card_type="Land", sub_types="",
                    abilities=[76735, 3625, 1055], set_id="M19", rarity="Uncommon", collectible=True, set_number=255,
                    mtga_id=68192)
StoneQuarry = Card(name="stone_quarry", pretty_name="Stone Quarry", cost=[],
                   color_identity=['R', 'W'], card_type="Land", sub_types="",
                   abilities=[76735, 4247], set_id="M19", rarity="Common", collectible=True, set_number=256,
                   mtga_id=68194)
SubmergedBoneyard = Card(name="submerged_boneyard", pretty_name="Submerged Boneyard", cost=[],
                         color_identity=['U', 'B'], card_type="Land", sub_types="",
                         abilities=[76735, 1167], set_id="M19", rarity="Common", collectible=True, set_number=257,
                         mtga_id=68196)
TimberGorge = Card(name="timber_gorge", pretty_name="Timber Gorge", cost=[],
                   color_identity=['R', 'G'], card_type="Land", sub_types="",
                   abilities=[76735, 1131], set_id="M19", rarity="Common", collectible=True, set_number=258,
                   mtga_id=68198)
TranquilExpanse = Card(name="tranquil_expanse", pretty_name="Tranquil Expanse", cost=[],
                       color_identity=['G', 'W'], card_type="Land", sub_types="",
                       abilities=[76735, 1203], set_id="M19", rarity="Common", collectible=True, set_number=259,
                       mtga_id=68200)
WoodlandStream = Card(name="woodland_stream", pretty_name="Woodland Stream", cost=[],
                      color_identity=['G', 'U'], card_type="Land", sub_types="",
                      abilities=[76735, 18504], set_id="M19", rarity="Common", collectible=True, set_number=260,
                      mtga_id=68202)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=261,
              mtga_id=68204)
Plains2 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=262,
               mtga_id=68206)
Plains3 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=263,
               mtga_id=68208)
Plains4 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=264,
               mtga_id=68210)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=265,
              mtga_id=68212)
Island2 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=266,
               mtga_id=68214)
Island3 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=267,
               mtga_id=68216)
Island4 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=268,
               mtga_id=68218)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=269,
             mtga_id=68220)
Swamp2 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=270,
              mtga_id=68222)
Swamp3 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=271,
              mtga_id=68224)
Swamp4 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=272,
              mtga_id=68226)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=273,
                mtga_id=68228)
Mountain2 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=274,
                 mtga_id=68230)
Mountain3 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=275,
                 mtga_id=68232)
Mountain4 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=276,
                 mtga_id=68234)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=277,
              mtga_id=68236)
Forest2 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=278,
               mtga_id=68238)
Forest3 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=279,
               mtga_id=68240)
Forest4 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="M19", rarity="Basic", collectible=True, set_number=280,
               mtga_id=68242)
AjaniWiseCounselor = Card(name="ajani_wise_counselor", pretty_name="Ajani, Wise Counselor", cost=['3', 'W', 'W'],
                          color_identity=['W'], card_type="Planeswalker", sub_types="Ajani",
                          abilities=[18244, 119217, 119150], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=281,
                          mtga_id=68244)
AjanisInfluence = Card(name="ajanis_influence", pretty_name="Ajani's Influence", cost=['2', 'W', 'W'],
                       color_identity=['W'], card_type="Sorcery", sub_types="",
                       abilities=[23602, 119151], set_id="M19", rarity="Rare", collectible=True, set_number=282,
                       mtga_id=68246)
CourtCleric = Card(name="court_cleric", pretty_name="Court Cleric", cost=['W'],
                   color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                   abilities=[12, 119219], set_id="M19", rarity="Uncommon", collectible=True, set_number=283,
                   mtga_id=68248)
SerrasGuardian = Card(name="serras_guardian", pretty_name="Serra's Guardian", cost=['4', 'W', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Angel",
                      abilities=[8, 15, 20486], set_id="M19", rarity="Rare", collectible=True, set_number=284,
                      mtga_id=68250)
SilverbeakGriffin = Card(name="silverbeak_griffin", pretty_name="Silverbeak Griffin", cost=['W', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Griffin",
                         abilities=[8], set_id="M19", rarity="Common", collectible=True, set_number=285,
                         mtga_id=68252)
TezzeretCruelMachinist = Card(name="tezzeret_cruel_machinist", pretty_name="Tezzeret, Cruel Machinist", cost=['4', 'U', 'U'],
                              color_identity=['U'], card_type="Planeswalker", sub_types="Tezzeret",
                              abilities=[1323, 119153, 86616], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=286,
                              mtga_id=68254)
RiddlemasterSphinx = Card(name="riddlemaster_sphinx", pretty_name="Riddlemaster Sphinx", cost=['4', 'U', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                          abilities=[8, 119222], set_id="M19", rarity="Rare", collectible=True, set_number=287,
                          mtga_id=68256)
PendulumofPatterns = Card(name="pendulum_of_patterns", pretty_name="Pendulum of Patterns", cost=['2'],
                          color_identity=[], card_type="Artifact", sub_types="",
                          abilities=[1102, 116489], set_id="M19", rarity="Common", collectible=True, set_number=288,
                          mtga_id=68258)
TezzeretsGatebreaker = Card(name="tezzerets_gatebreaker", pretty_name="Tezzeret's Gatebreaker", cost=['4'],
                            color_identity=['U'], card_type="Artifact", sub_types="",
                            abilities=[119157, 119158], set_id="M19", rarity="Rare", collectible=True, set_number=289,
                            mtga_id=68260)
TezzeretsStrider = Card(name="tezzerets_strider", pretty_name="Tezzeret's Strider", cost=['3'],
                        color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                        abilities=[119159], set_id="M19", rarity="Uncommon", collectible=True, set_number=290,
                        mtga_id=68262)
LilianatheNecromancer = Card(name="liliana_the_necromancer", pretty_name="Liliana, the Necromancer", cost=['3', 'B', 'B'],
                             color_identity=['B'], card_type="Planeswalker", sub_types="Liliana",
                             abilities=[119160, 119228, 119161], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=291,
                             mtga_id=68264)
ArisenGorgon = Card(name="arisen_gorgon", pretty_name="Arisen Gorgon", cost=['1', 'B', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Zombie Gorgon",
                    abilities=[119162], set_id="M19", rarity="Uncommon", collectible=True, set_number=292,
                    mtga_id=68266)
Gravewaker = Card(name="gravewaker", pretty_name="Gravewaker", cost=['4', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Bird Spirit",
                  abilities=[8, 119163], set_id="M19", rarity="Rare", collectible=True, set_number=293,
                  mtga_id=68268)
LilianasSpoils = Card(name="lilianas_spoils", pretty_name="Liliana's Spoils", cost=['3', 'B'],
                      color_identity=['B'], card_type="Sorcery", sub_types="",
                      abilities=[119164, 119165], set_id="M19", rarity="Rare", collectible=True, set_number=294,
                      mtga_id=68270)
TatteredMummy = Card(name="tattered_mummy", pretty_name="Tattered Mummy", cost=['1', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Zombie Jackal",
                     abilities=[97556], set_id="M19", rarity="Common", collectible=True, set_number=295,
                     mtga_id=68272)
SarkhanDragonsoul = Card(name="sarkhan_dragonsoul", pretty_name="Sarkhan, Dragonsoul", cost=['4', 'R', 'R'],
                         color_identity=['R'], card_type="Planeswalker", sub_types="Sarkhan",
                         abilities=[119233, 119167, 119168], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=296,
                         mtga_id=68274)
KarganDragonrider = Card(name="kargan_dragonrider", pretty_name="Kargan Dragonrider", cost=['1', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                         abilities=[119169], set_id="M19", rarity="Common", collectible=True, set_number=297,
                         mtga_id=68276)
SarkhansDragonfire = Card(name="sarkhans_dragonfire", pretty_name="Sarkhan's Dragonfire", cost=['3', 'R', 'R'],
                          color_identity=['R'], card_type="Sorcery", sub_types="",
                          abilities=[70361, 119170], set_id="M19", rarity="Rare", collectible=True, set_number=298,
                          mtga_id=68278)
SarkhansWhelp = Card(name="sarkhans_whelp", pretty_name="Sarkhan's Whelp", cost=['2', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Dragon",
                     abilities=[8, 119236], set_id="M19", rarity="Uncommon", collectible=True, set_number=299,
                     mtga_id=68280)
ShivanDragon = Card(name="shivan_dragon", pretty_name="Shivan Dragon", cost=['4', 'R', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Dragon",
                    abilities=[8, 1097], set_id="M19", rarity="Rare", collectible=True, set_number=300,
                    mtga_id=68282)
VivienoftheArkbow = Card(name="vivien_of_the_arkbow", pretty_name="Vivien of the Arkbow", cost=['4', 'G', 'G'],
                         color_identity=['G'], card_type="Planeswalker", sub_types="Vivien",
                         abilities=[116479, 119172, 119173], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=301,
                         mtga_id=68284)
AggressiveMammoth = Card(name="aggressive_mammoth", pretty_name="Aggressive Mammoth", cost=['3', 'G', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elephant",
                         abilities=[14, 20623], set_id="M19", rarity="Rare", collectible=True, set_number=302,
                         mtga_id=68286)
SkallaWolf = Card(name="skalla_wolf", pretty_name="Skalla Wolf", cost=['3', 'G', 'G'],
                  color_identity=['G'], card_type="Creature", sub_types="Wolf Spirit",
                  abilities=[119240], set_id="M19", rarity="Rare", collectible=True, set_number=303,
                  mtga_id=68288)
UrsineChampion = Card(name="ursine_champion", pretty_name="Ursine Champion", cost=['1', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Human Berserker",
                      abilities=[119175], set_id="M19", rarity="Common", collectible=True, set_number=304,
                      mtga_id=68290)
ViviensJaguar = Card(name="viviens_jaguar", pretty_name="Vivien's Jaguar", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Cat Spirit",
                     abilities=[13, 1345], set_id="M19", rarity="Uncommon", collectible=True, set_number=305,
                     mtga_id=68292)
NexusofFate = Card(name="nexus_of_fate", pretty_name="Nexus of Fate", cost=['5', 'U', 'U'],
                   color_identity=['U'], card_type="Instant", sub_types="",
                   abilities=[4577, 6365], set_id="M19", rarity="Mythic Rare", collectible=True, set_number=306,
                   mtga_id=68294)
SunSentinel = Card(name="sun_sentinel", pretty_name="Sun Sentinel", cost=['1', 'W'],
                   color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                   abilities=[15], set_id="M19", rarity="Common", collectible=True, set_number=307,
                   mtga_id=68296)
AirElemental = Card(name="air_elemental", pretty_name="Air Elemental", cost=['3', 'U', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Elemental",
                    abilities=[8], set_id="M19", rarity="Uncommon", collectible=True, set_number=308,
                    mtga_id=68298)
Befuddle = Card(name="befuddle", pretty_name="Befuddle", cost=['2', 'U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[63602, 25848], set_id="M19", rarity="Common", collectible=True, set_number=309,
                mtga_id=68300)
MistCloakedHerald = Card(name="mistcloaked_herald", pretty_name="Mist-Cloaked Herald", cost=['U'],
                         color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                         abilities=[62969], set_id="M19", rarity="Common", collectible=True, set_number=310,
                         mtga_id=68302)
Waterknot = Card(name="waterknot", pretty_name="Waterknot", cost=['1', 'U', 'U'],
                 color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                 abilities=[1027, 89789, 88178], set_id="M19", rarity="Common", collectible=True, set_number=311,
                 mtga_id=68304)
GraspingScoundrel = Card(name="grasping_scoundrel", pretty_name="Grasping Scoundrel", cost=['B'],
                         color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[117081], set_id="M19", rarity="Common", collectible=True, set_number=312,
                         mtga_id=68306)
RadiatingLightning = Card(name="radiating_lightning", pretty_name="Radiating Lightning", cost=['3', 'R'],
                          color_identity=['R'], card_type="Instant", sub_types="",
                          abilities=[118840], set_id="M19", rarity="Common", collectible=True, set_number=313,
                          mtga_id=68308)
LlanowarElves = Card(name="llanowar_elves", pretty_name="Llanowar Elves", cost=['G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                     abilities=[1005], set_id="M19", rarity="Common", collectible=True, set_number=314,
                     mtga_id=68310)
Angel = Card(name="angel", pretty_name="Angel", cost=[],
             color_identity=[], card_type="Creature", sub_types="Angel",
             abilities=[8, 15], set_id="M19", rarity="Token", collectible=False, set_number=10001,
             mtga_id=68312)
Avatar = Card(name="avatar", pretty_name="Avatar", cost=[],
              color_identity=[], card_type="Creature", sub_types="Avatar",
              abilities=[8], set_id="M19", rarity="Token", collectible=False, set_number=10002,
              mtga_id=68313)
Cat = Card(name="cat", pretty_name="Cat", cost=[],
           color_identity=[], card_type="Creature", sub_types="Cat",
           abilities=[12], set_id="M19", rarity="Token", collectible=False, set_number=10003,
           mtga_id=68314)
Knight = Card(name="knight", pretty_name="Knight", cost=[],
              color_identity=[], card_type="Creature", sub_types="Knight",
              abilities=[15], set_id="M19", rarity="Token", collectible=False, set_number=10004,
              mtga_id=68315)
Ox = Card(name="ox", pretty_name="Ox", cost=[],
          color_identity=[], card_type="Creature", sub_types="Ox",
          abilities=[], set_id="M19", rarity="Token", collectible=False, set_number=10005,
          mtga_id=68316)
Soldier = Card(name="soldier", pretty_name="Soldier", cost=[],
               color_identity=[], card_type="Creature", sub_types="Soldier",
               abilities=[], set_id="M19", rarity="Token", collectible=False, set_number=10006,
               mtga_id=68317)
Bat = Card(name="bat", pretty_name="Bat", cost=[],
           color_identity=[], card_type="Creature", sub_types="Bat",
           abilities=[8], set_id="M19", rarity="Token", collectible=False, set_number=10007,
           mtga_id=68318)
Zombie = Card(name="zombie", pretty_name="Zombie", cost=[],
              color_identity=[], card_type="Creature", sub_types="Zombie",
              abilities=[], set_id="M19", rarity="Token", collectible=False, set_number=10008,
              mtga_id=68319)
Dragon = Card(name="dragon", pretty_name="Dragon", cost=[],
              color_identity=['R'], card_type="Creature", sub_types="Dragon",
              abilities=[8, 8867], set_id="M19", rarity="Token", collectible=False, set_number=10009,
              mtga_id=68320)
Dragon2 = Card(name="dragon", pretty_name="Dragon", cost=[],
               color_identity=[], card_type="Creature", sub_types="Dragon",
               abilities=[8], set_id="M19", rarity="Token", collectible=False, set_number=10010,
               mtga_id=68321)
Goblin = Card(name="goblin", pretty_name="Goblin", cost=[],
              color_identity=[], card_type="Creature", sub_types="Goblin",
              abilities=[], set_id="M19", rarity="Token", collectible=False, set_number=10011,
              mtga_id=68322)
Beast = Card(name="beast", pretty_name="Beast", cost=[],
             color_identity=[], card_type="Creature", sub_types="Beast",
             abilities=[], set_id="M19", rarity="Token", collectible=False, set_number=10012,
             mtga_id=68323)
ElfWarrior = Card(name="elf_warrior", pretty_name="Elf Warrior", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Elf Warrior",
                  abilities=[], set_id="M19", rarity="Token", collectible=False, set_number=10013,
                  mtga_id=68324)
Thopter = Card(name="thopter", pretty_name="Thopter", cost=[],
               color_identity=[], card_type="Artifact Creature", sub_types="Thopter",
               abilities=[8], set_id="M19", rarity="Token", collectible=False, set_number=10014,
               mtga_id=68325)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
CoreSet2019 = Set("m19", cards=clsmembers)

set_ability_map = {1: 'Deathtouch',
 2: 'Defender',
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
 1005: '{oT}: Add {oG}.',
 1019: 'Target creature gets +3/+0 and gains first strike until end of turn.',
 1026: "Hungering Hydra can't be blocked by more than one creature.",
 1027: 'Enchant creature',
 1031: 'Target creature gets +4/+4 until end of turn.',
 1039: '{oT}: Add {oU} or {oR}.',
 1055: '{oT}: Add one mana of any color.',
 1078: 'Enchanted creature is a copy of the chosen creature.',
 1083: "Enchanted creature can't attack or block.",
 1097: '{oR}: Shivan Dragon gets +1/+0 until end of turn.',
 1098: "Destroy target land. Creatures without flying can't block this turn.",
 1102: 'When Pendulum of Patterns enters the battlefield, you gain 3 life.',
 1111: 'Djinn of Wishes enters the battlefield with three wish counters on it.',
 1112: '{o2oUoU}, Remove a wish counter from Djinn of Wishes: Reveal the top '
       'card of your library. You may play that card without paying its mana '
       "cost. If you don't, exile it.",
 1118: 'Lava Axe deals 5 damage to target player or planeswalker.',
 1131: '{oT}: Add {oR} or {oG}.',
 1152: '{oT}: Add {oC}.',
 1156: 'Equip {o3}',
 1157: 'When Gravedigger enters the battlefield, you may return target '
       'creature card from your graveyard to your hand.',
 1167: '{oT}: Add {oU} or {oB}.',
 1188: '{o1oB}: Return Reassembling Skeleton from your graveyard to the '
       'battlefield tapped.',
 1203: '{oT}: Add {oG} or {oW}.',
 1209: '{oT}: Add {oW} or {oU}.',
 1211: '{oT}: Add {oB} or {oR}.',
 1235: 'Target creature gets +2/+2 and gains flying until end of turn.',
 1275: 'As an additional cost to cast this spell, sacrifice a creature.',
 1276: "Thud deals damage equal to the sacrificed creature's power to any "
       'target.',
 1278: 'Gain control of target creature until end of turn. Untap that '
       'creature. It gains haste until end of turn.',
 1318: 'Enchanted creature gets +3/+3.',
 1319: 'Equip {o2}',
 1323: '+1: Draw a card.',
 1345: "{o2oG}: Return Vivien's Jaguar from your graveyard to your hand. "
       'Activate this ability only if you control a Vivien planeswalker.',
 1385: 'Destroy target tapped creature.',
 1438: 'Enchanted creature gets +1/+1 for each Forest you control.',
 1570: 'Enchant land',
 1588: '{o2}, {oT}: Target player puts the top two cards of their library into '
       'their graveyard.',
 1640: 'You have no maximum hand size.',
 1746: 'Draw three cards.',
 2018: 'Enchanted creature gets +2/+2.',
 2159: 'Put target creature card from a graveyard onto the battlefield under '
       'your control. That creature is a black Zombie in addition to its other '
       'colors and types.',
 2338: 'Target creature gets -3/-3 until end of turn.',
 2813: 'Destroy target artifact or enchantment. You gain 4 life.',
 2904: 'Whenever an opponent discards a card, that player loses 2 life.',
 2920: 'Creatures your opponents control get -2/-0 until end of turn.',
 3625: 'When Rupture Spire enters the battlefield, sacrifice it unless you pay '
       '{o1}.',
 4247: '{oT}: Add {oR} or {oW}.',
 4407: '{oT}: Add {oB} or {oG}.',
 4577: 'Take an extra turn after this one.',
 4712: 'Equipped creature gets +2/+0.',
 5179: 'Skeletons you control and other Zombies you control get +1/+1 and have '
       'deathtouch.',
 6082: 'Return target card from your graveyard to your hand.',
 6365: 'If Nexus of Fate would be put into a graveyard from anywhere, reveal '
       "Nexus of Fate and shuffle it into its owner's library instead.",
 6832: 'You may play land cards from your graveyard.',
 6908: 'Draw three cards, then discard a card.',
 7642: 'Whenever equipped creature deals combat damage to a player, you may '
       'draw a card.',
 8867: '{oR}: This creature gets +1/+0 until end of turn.',
 9569: 'Return up to two target creature cards from your graveyard to your '
       'hand, then discard a card.',
 11569: 'Attacking creatures get +2/+0 until end of turn.',
 11632: 'Creatures you control get +2/+1 until end of turn.',
 13572: 'Whenever you cast an enchantment spell, draw a card.',
 15166: '{oT}: Target creature gains haste until end of turn.',
 15269: 'Enchanted creature gets +1/+1 and has trample.',
 15392: 'Sacrifice any number of lands. Search your library for up to that '
        'many land cards, put them onto the battlefield tapped, then shuffle '
        'your library.',
 17518: 'When Pelakka Wurm enters the battlefield, you gain 7 life.',
 17519: 'When Pelakka Wurm dies, draw a card.',
 18244: '+2: You gain 1 life for each creature you control.',
 18472: '{oT}: Add {oW} or {oB}.',
 18504: '{oT}: Add {oG} or {oU}.',
 18682: 'Whenever another creature with power 2 or less enters the battlefield '
        'under your control, you may pay {o1}. If you do, draw a card.',
 19199: 'Exchange control of two target creatures.',
 19205: 'You may cast spells from your hand without paying their mana costs.',
 19558: 'Enchanted creature gets +2/+2 and has vigilance.',
 20301: 'Whenever a creature with flying attacks, you may draw a card.',
 20486: 'Other creatures you control have vigilance.',
 20623: 'Other creatures you control have trample.',
 20793: '{oR}, {oT}, Discard a card: Draw a card.',
 20990: 'Enchanted creature gets -6/-0.',
 20997: "When Hieromancer's Cage enters the battlefield, exile target nonland "
        "permanent an opponent controls until Hieromancer's Cage leaves the "
        'battlefield.',
 21074: 'At the beginning of your upkeep, you gain 1 life.',
 21773: 'Spit Flame deals 4 damage to target creature.',
 21775: 'Target opponent reveals their hand. You choose a noncreature, nonland '
        'card from it. That player discards that card.',
 22564: 'Destroy target artifact.',
 23602: 'Put two +1/+1 counters on target creature.',
 23607: 'Draw two cards.',
 23608: 'Target player discards two cards.',
 24121: 'Counter target creature spell.',
 25846: 'Counter target spell.',
 25848: 'Draw a card.',
 26818: 'Destroy target creature.',
 27746: 'Prevent all combat damage that would be dealt this turn.',
 29759: 'Destroy target creature with flying.',
 30479: 'You gain 3 life.',
 61084: 'Look at the top three cards of your library. Put one of them into '
        'your hand and the rest on the bottom of your library in any order.',
 61119: 'Enchanted land has "{oT}: Add two mana of any one color."',
 61234: 'Target creature you control deals damage equal to its power to target '
        "creature you don't control.",
 62127: 'Whenever you cast a spell of the chosen color, you gain 1 life.',
 62471: 'Creatures you control get +1/+0 and gain indestructible until end of '
        'turn.',
 62618: 'Whenever you gain life, each opponent loses 1 life.',
 62969: "Mist-Cloaked Herald can't be blocked.",
 63602: 'Target creature gets -4/-0 until end of turn.',
 70361: "Sarkhan's Dragonfire deals 3 damage to any target.",
 76735: 'Woodland Stream enters the battlefield tapped.',
 76777: 'Whenever you cast an artifact spell, create a 1/1 colorless Thopter '
        'artifact creature token with flying.',
 76869: 'Ghastbark Twins can block an additional creature each combat.',
 76885: 'Hungering Hydra enters the battlefield with X +1/+1 counters on it.',
 76894: 'When Angel of the Dawn enters the battlefield, creatures you control '
        'get +1/+1 and gain vigilance until end of turn.',
 86613: 'Shock deals 2 damage to any target.',
 86616: '-7: Put any number of cards from your hand onto the battlefield face '
        "down. They're 5/5 artifact creatures.",
 86788: 'When Skyscanner enters the battlefield, draw a card.',
 87929: 'As an additional cost to cast this spell, discard a card.',
 87971: "Enigma Drake's power is equal to the number of instant and sorcery "
        'cards in your graveyard.',
 88041: 'When Departed Deckhand becomes the target of a spell, sacrifice it.',
 88075: 'When Doomed Dissenter dies, create a 2/2 black Zombie creature token.',
 88098: 'Until end of turn, target creature gets +2/+0 and gains "When this '
        "creature dies, return it to the battlefield tapped under its owner's "
        'control."',
 88112: 'Fiery Finish deals 7 damage to target creature.',
 88126: '{o1oR}: Lightning Mare gets +1/+0 until end of turn.',
 88144: 'Banefire deals X damage to any target.',
 88178: "Enchanted creature doesn't untap during its controller's untap step.",
 88237: 'As Diamond Mare enters the battlefield, choose a color.',
 88244: 'When Fell Specter enters the battlefield, target opponent discards a '
        'card.',
 89789: 'When Waterknot enters the battlefield, tap enchanted creature.',
 90211: 'When Salvager of Secrets enters the battlefield, return target '
        'instant or sorcery card from your graveyard to your hand.',
 90310: 'Whenever Infectious Horror attacks, each opponent loses 2 life.',
 90322: "If X is 5 or more, this spell can't be countered and the damage can't "
        'be prevented.',
 90788: 'When Dwarven Priest enters the battlefield, you gain 1 life for each '
        'creature you control.',
 91870: 'When Skymarch Bloodletter enters the battlefield, target opponent '
        'loses 1 life and you gain 1 life.',
 92035: 'Sacrifice Catalyst Elemental: Add {oRoR}.',
 92274: "Lightning Mare can't be blocked by blue creatures.",
 92851: "Tap all creatures target player controls. Those creatures don't untap "
        "during that player's next untap step.",
 92894: 'When Skeleton Archer enters the battlefield, it deals 1 damage to any '
        'target.',
 92921: '{o3}: Until end of turn, Gargoyle Sentinel loses defender and gains '
        'flying.',
 92927: 'When Nicol Bolas, the Ravager enters the battlefield, each opponent '
        'discards a card.',
 92953: 'As Phylactery Lich enters the battlefield, put a phylactery counter '
        'on an artifact you control.',
 92954: 'When you control no permanents with phylactery counters on them, '
        'sacrifice Phylactery Lich.',
 92970: "Whenever you gain life, put a +1/+1 counter on Ajani's Pridemate.",
 93150: 'Transmogrifying Wand enters the battlefield with three charge '
        'counters on it.',
 93266: 'When Highland Game dies, you gain 2 life.',
 94230: 'Whenever Star-Crowned Stag attacks, tap target creature defending '
        'player controls.',
 94489: "{o4}, {oT}: Put a charge counter on Magistrate's Scepter.",
 94490: "{oT}, Remove three charge counters from Magistrate's Scepter: Take an "
        'extra turn after this one.',
 94618: "Return target nonland permanent to its owner's hand.",
 96307: 'When Exclusion Mage enters the battlefield, return target creature an '
        "opponent controls to its owner's hand.",
 97118: "Plague Mare can't be blocked by white creatures.",
 97130: "Shield Mare can't be blocked by red creatures.",
 97134: "Surge Mare can't be blocked by green creatures.",
 97144: "Vine Mare can't be blocked by black creatures.",
 97556: 'When Tattered Mummy dies, each opponent loses 2 life.',
 99695: "Up to two target creatures can't be blocked this turn.",
 99758: "Put target nonland permanent on top of its owner's library.",
 99956: 'When Knightly Valor enters the battlefield, create a 2/2 white Knight '
        'creature token with vigilance.',
 100026: 'Whenever you cast an instant or sorcery spell, Guttersnipe deals 2 '
         'damage to each opponent.',
 100587: 'When Dragon Egg dies, create a 2/2 red Dragon creature token with '
         'flying and "{oR}: This creature gets +1/+0 until end of turn."',
 100685: 'When Omenspeaker enters the battlefield, scry 2.',
 101429: 'When Reclamation Sage enters the battlefield, you may destroy target '
         'artifact or enchantment.',
 102214: 'When Aviation Pioneer enters the battlefield, create a 1/1 colorless '
         'Thopter artifact creature token with flying.',
 102264: 'Enchanted creature gets +2/+0 and has "When this creature dies, draw '
         'a card."',
 102965: '{o5oG}: Thorn Lieutenant gets +4/+4 until end of turn.',
 103005: '{o3}, {oT}, Sacrifice Explosive Apparatus: It deals 2 damage to any '
         'target.',
 103319: 'Gearsmith Prodigy gets +1/+0 as long as you control an artifact.',
 103385: "{o2oG}: Target creature you control can't be blocked by creatures "
         'with power 2 or less this turn.',
 103806: 'Creatures you control gain trample until end of turn.',
 103816: 'Whenever Pegasus Courser attacks, another target attacking creature '
         'gains flying until end of turn.',
 116479: '+2: Put two +1/+1 counters on up to one target creature.',
 116489: '{o5}, {oT}, Sacrifice Pendulum of Patterns: Draw a card.',
 117081: "Grasping Scoundrel gets +1/+0 as long as it's attacking.",
 118840: 'Radiating Lightning deals 3 damage to target player and 1 damage to '
         'each creature that player controls.',
 119081: "Sacrifice Remorseful Cleric: Exile all cards from target player's "
         'graveyard.',
 119082: 'Exile target permanent with converted mana cost 1.',
 119083: '{o3oWoWoW}: Until end of turn, Resplendent Angel gets +2/+2 and '
         'gains lifelink.',
 119084: 'At the beginning of your upkeep, if you control four or more Demons '
         'with different names, you win the game.',
 119085: 'You gain 1 life. Target creature gets -X/-X until end of turn, where '
         'X is the amount of life you gained this turn.',
 119086: 'Whenever a nontoken creature you control dies, create a 2/2 black '
         'Zombie creature token.',
 119087: 'At the beginning of each end step, if you gained 5 or more life this '
         'turn, create a 4/4 white Angel creature token with flying and '
         'vigilance.',
 119088: '{o1}, Sacrifice another creature: Put a +1/+1 counter on Ravenous '
         'Harpy.',
 119090: 'Target player loses 3 life and you gain 3 life.',
 119091: 'If this spell was cast from your hand, add ten mana of any one '
         'color.',
 119092: 'When you cast your next instant or sorcery spell this turn, copy '
         'that spell. You may choose new targets for the copy.',
 119093: 'When Suncleanser enters the battlefield, choose one   Remove all '
         "counters from target creature. It can't have counters put on it for "
         'as long as Suncleanser remains on the battlefield.  Target opponent '
         "loses all counters. That player can't get counters for as long as "
         'Suncleanser remains on the battlefield.',
 119095: 'When Viashino Pyromancer enters the battlefield, it deals 2 damage '
         'to target player or planeswalker.',
 119096: 'When Volley Veteran enters the battlefield, it deals damage to '
         'target creature an opponent controls equal to the number of Goblins '
         'you control.',
 119097: 'At the beginning of your upkeep, if you control a creature with '
         'power 4 or greater, draw a card.',
 119098: 'Target creature gets +3/+3 until end of turn. All creatures able to '
         'block it this turn do so.',
 119099: 'Whenever you cast an Aura spell that targets Druid of Horns, create '
         'a 3/3 green Beast creature token.',
 119100: "{oT}: Look at the top card of your library. If it's a land card, you "
         'may reveal it and put it into your hand.',
 119101: 'When Trusty Packbeast enters the battlefield, return target artifact '
         'card from your graveyard to your hand.',
 119102: '{o4oGoG}, {oT}: Search your library for a card named Elvish '
         'Clancaller, put it onto the battlefield, then shuffle your library.',
 119103: 'When Elvish Rejuvenator enters the battlefield, look at the top five '
         'cards of your library. You may put a land card from among them onto '
         'the battlefield tapped. Put the rest on the bottom of your library '
         'in a random order.',
 119104: 'Other Knights you control get +1/+1.',
 119105: 'Creature spells you cast with power 4 or greater cost {o2} less to '
         'cast.',
 119106: 'Whenever Goreclaw, Terror of Qal Sisma attacks, each creature you '
         'control with power 4 or greater gets +1/+1 and gains trample until '
         'end of turn.',
 119107: '{o3oWoW}: Knights you control gain double strike until end of turn.',
 119108: 'Whenever Hungering Hydra is dealt damage, put that many +1/+1 '
         'counters on it.',
 119109: "Enchanted creature gets +1/+0 and can't be blocked.",
 119110: 'Enchanted creature gets +7/+7 and has trample.',
 119111: 'Whenever an opponent activates an ability of a creature or land that '
         "isn't a mana ability, you may draw a card.",
 119112: '{o2oG}: Return Talons of Wildwood from your graveyard to your hand.',
 119113: 'Whenever Thorn Lieutenant becomes the target of a spell or ability '
         'an opponent controls, create a 1/1 green Elf Warrior creature token.',
 119114: 'Whenever you cast an instant or sorcery spell, Aven Wind Mage gets '
         '+1/+1 until end of turn.',
 119115: '+1: Look at the top four cards of your library. You may reveal a '
         'creature or land card from among them and put it into your hand. Put '
         'the rest on the bottom of your library in a random order.',
 119116: '-3: Destroy target artifact, enchantment, or creature with flying.',
 119118: 'Whenever a creature with defender enters the battlefield under your '
         'control, draw a card.',
 119119: 'Each creature you control with defender assigns combat damage equal '
         'to its toughness rather than its power and can attack as though it '
         "didn't have defender.",
 119120: 'Whenever Brawl-Bash Ogre attacks, you may sacrifice another '
         'creature. If you do, Brawl-Bash Ogre gets +2/+2 until end of turn.',
 119121: '{o7}, {oT}, Sacrifice Draconic Disciple: Create a 5/5 red Dragon '
         'creature token with flying.',
 119122: 'Create two 1/1 white Soldier creature tokens. Until end of turn, '
         'creatures you control get +1/+1 and gain haste.',
 119123: '{o4oUoBoR}: Exile Nicol Bolas, the Ravager, then return him to the '
         "battlefield transformed under his owner's control. Activate this "
         'ability only any time you could cast a sorcery.',
 119124: '-3: Nicol Bolas, the Arisen deals 10 damage to target creature or '
         'planeswalker.',
 119125: '-4: Put target creature or planeswalker card from a graveyard onto '
         'the battlefield under your control.',
 119126: "-12: Exile all but the bottom card of target player's library.",
 119127: "Palladia-Mors, the Ruiner has hexproof if it hasn't dealt damage "
         'yet.',
 119128: 'Whenever another creature dies, each opponent loses 1 life.',
 119129: 'At the beginning of each end step, if you gained life this turn, '
         'create a 1/1 black Bat creature token with flying.',
 119130: 'At the beginning of combat on your turn, you may pay {oGoU}. When '
         'you do, put a +1/+1 counter on another target creature you control, '
         'and that creature gains flying until end of turn.',
 119131: 'Whenever Vaevictis Asmadi, the Dire attacks, for each player, choose '
         'target permanent that player controls. Those players sacrifice those '
         'permanents. Each player who sacrificed a permanent this way reveals '
         'the top card of their library, then puts it onto the battlefield if '
         "it's a permanent card.",
 119132: 'Whenever you become the target of a spell or ability an opponent '
         'controls, counter that spell or ability unless its controller pays '
         '{o1}.',
 119133: "Departed Deckhand can't be blocked except by Spirits.",
 119134: '{o3}, {oT}: Draw a card.',
 119135: 'Whenever one or more creature cards leave your graveyard, create a '
         '1/1 black Bat creature token with flying.',
 119136: "{o3oU}: Another target creature you control can't be blocked this "
         'turn except by Spirits.',
 119137: 'When Lena, Selfless Champion enters the battlefield, create a 1/1 '
         'white Soldier creature token for each nontoken creature you control.',
 119138: "{oT}, Remove a gold counter from Dragon's Hoard: Draw a card.",
 119139: '{o3}, Sacrifice Fountain of Renewal: Draw a card.',
 119140: 'Gearsmith Guardian gets +2/+0 as long as you control a blue '
         'creature.',
 119141: 'When Meteor Golem enters the battlefield, destroy target nonland '
         'permanent an opponent controls.',
 119142: 'Equipped creature gets +2/+0, has vigilance, and is a Knight in '
         'addition to its other types.',
 119143: 'Whenever equipped creature attacks, create a 2/2 white Knight '
         "creature token with vigilance that's attacking.",
 119144: "{o3}, {oT}: Target creature can't be blocked this turn.",
 119145: '{o1}, {oT}, Remove a charge counter from Transmogrifying Wand: '
         'Destroy target creature. Its controller creates a 2/4 white Ox '
         'creature token. Activate this ability only any time you could cast a '
         'sorcery.',
 119146: "Sacrifice Lena: Creatures you control with power less than Lena's "
         'power gain indestructible until end of turn.',
 119147: '-8: You get an emblem with "Creatures you control get +2/+2 and have '
         'vigilance, trample, and indestructible."',
 119148: 'When enchanted creature blocks, destroy it.',
 119149: 'Look at the top seven cards of your library. You may put a creature '
         'card from among them onto the battlefield. Put the rest on the '
         'bottom of your library in a random order. When a creature is put '
         'onto the battlefield this way, it deals damage equal to its power to '
         'target creature an opponent controls.',
 119150: '-9: Put X +1/+1 counters on target creature, where X is your life '
         'total.',
 119151: 'Look at the top five cards of your library. You may reveal a white '
         'card from among them and put it into your hand. Put the rest on the '
         'bottom of your library in a random order.',
 119152: 'As long as you control an artifact, Aerial Engineer gets +2/+0 and '
         'has flying.',
 119153: '0: Until your next turn, target artifact you control becomes a 5/5 '
         'creature in addition to its other types.',
 119156: "{o5oUoU}: Frilled Sea Serpent can't be blocked this turn.",
 119157: "When Tezzeret's Gatebreaker enters the battlefield, look at the top "
         'five cards of your library. You may reveal a blue or artifact card '
         'from among them and put it into your hand. Put the rest on the '
         'bottom of your library in a random order.',
 119158: "{o5oU}, {oT}, Sacrifice Tezzeret's Gatebreaker: Creatures you "
         "control can't be blocked this turn.",
 119159: "As long as you control a Tezzeret planeswalker, Tezzeret's Strider "
         'has menace.',
 119160: '+1: Target player loses 2 life.',
 119161: '-7: Destroy up to two target creatures. Put up to two creature cards '
         'from graveyards onto the battlefield under your control.',
 119162: 'Arisen Gorgon has deathtouch as long as you control a Liliana '
         'planeswalker.',
 119163: '{o5oBoB}: Return target creature card from your graveyard to the '
         'battlefield tapped.',
 119164: 'Target opponent discards a card.',
 119165: 'Look at the top five cards of your library. You may reveal a black '
         'card from among them and put it into your hand. Put the rest on the '
         'bottom of your library in a random order.',
 119166: 'At the beginning of combat on your turn, if you control three or '
         'more creatures, Leonin Vanguard gets +1/+1 until end of turn and you '
         'gain 1 life.',
 119167: '-3: Sarkhan, Dragonsoul deals 4 damage to target player or '
         'planeswalker.',
 119168: '-9: Search your library for any number of Dragon creature cards, put '
         'them onto the battlefield, then shuffle your library.',
 119169: 'As long as you control a Dragon, Kargan Dragonrider has flying.',
 119170: 'Look at the top five cards of your library. You may reveal a red '
         'card from among them and put it into your hand. Put the rest on the '
         'bottom of your library in a random order.',
 119171: 'Discard a card: Until end of turn, Chromium, the Mutable becomes a '
         'Human with base power and toughness 1/1, loses all abilities, and '
         "gains hexproof. It can't be blocked this turn.",
 119172: '-3: Target creature you control deals damage equal to its power to '
         "target creature you don't control.",
 119173: '-9: Creatures you control get +4/+4 and gain trample until end of '
         'turn.',
 119174: 'As Metamorphic Alteration enters the battlefield, choose a creature.',
 119175: '{o5oG}: Ursine Champion gets +3/+3 and becomes a Bear Berserker '
         'until end of turn. Activate this ability only once each turn.',
 119177: 'You may have Mirror Image enter the battlefield as a copy of any '
         'creature you control.',
 119180: 'Sacrifice Mistcaller: Until end of turn, if a nontoken creature '
         "would enter the battlefield and it wasn't cast, exile it instead.",
 119181: 'Whenever Leonin Warleader attacks, create two 1/1 white Cat creature '
         'tokens with lifelink that are tapped and attacking.',
 119182: '{o3oUoU}: Draw two cards.',
 119183: '+2: Draw two cards.',
 119184: 'Other Elves you control get +1/+1.',
 119185: 'Draw cards equal to the highest converted mana cost among artifacts '
         'you control.',
 119186: 'At the beginning of your upkeep, target opponent puts the top three '
         'cards of their library into their graveyard, then you draw a card '
         'for each land card put into that graveyard this way.',
 119187: 'Whenever you draw a card, each opponent puts the top two cards of '
         'their library into their graveyard.',
 119188: '{o1oU}, Sacrifice two artifacts: Draw a card.',
 119189: 'When Psychic Symbiont enters the battlefield, target opponent '
         'discards a card and you draw a card.',
 119190: 'When Scholar of Stars enters the battlefield, if you control an '
         'artifact, draw a card.',
 119191: 'When Skilled Animator enters the battlefield, target artifact you '
         'control becomes an artifact creature with base power and toughness '
         '5/5 for as long as Skilled Animator remains on the battlefield.',
 119192: 'Other Spirits you control get +1/+1.',
 119193: 'Creature tokens get -1/-0.',
 119194: 'Whenever Surge Mare deals damage to an opponent, you may draw a '
         'card. If you do, discard a card.',
 119195: '{o1oU}: Surge Mare gets +2/-2 until end of turn.',
 119196: '{o4}, {oT}: Target opponent exiles cards from the top of their '
         'library until they exile an instant or sorcery card. You may cast '
         'that card without paying its mana cost. Then put the exiled cards '
         "that weren't cast this way on the bottom of that library in a random "
         'order.',
 119197: '+1: Create a 1/1 colorless Thopter artifact creature token with '
         'flying.',
 119198: 'At the beginning of each end step, if Inferno Hellion attacked or '
         'blocked this turn, its owner shuffles it into their library.',
 119199: '0: Draw a card. If you control three or more artifacts, draw two '
         'cards instead.',
 119201: '-9: You get an emblem with "At the beginning of your end step, '
         'search your library for a permanent card, put it onto the '
         'battlefield, then shuffle your library."',
 119202: 'Whenever a Dragon enters the battlefield under your control, put a '
         "gold counter on Dragon's Hoard.",
 119203: 'When Militia Bugler enters the battlefield, look at the top four '
         'cards of your library. You may reveal a creature card with power 2 '
         'or less from among them and put it into your hand. Put the rest on '
         'the bottom of your library in a random order.',
 119205: '{o3oBoB}, Exile seven other cards from your graveyard: Return Bone '
         'Dragon from your graveyard to the battlefield tapped.',
 119206: 'As long as Novice Knight is enchanted or equipped, it can attack as '
         "though it didn't have defender.",
 119207: 'Each player loses half their life, then discards half the cards in '
         'their hand, then sacrifices half the creatures they control. Round '
         'up each time.',
 119208: '{o2oB}, Exile a creature card from your graveyard: Create a tapped '
         '2/2 black Zombie creature token.',
 119209: 'Exile target colorless creature. You gain life equal to its power.',
 119210: 'Whenever Isareth the Awakener attacks, you may pay {oX}. When you '
         'do, return target creature card with converted mana cost X from your '
         'graveyard to the battlefield with a corpse counter on it. If that '
         'creature would leave the battlefield, exile it instead of putting it '
         'anywhere else.',
 119211: '{o1}, {oT}: Until end of turn, your opponents and creatures your '
         'opponents control with hexproof can be the targets of spells and '
         "abilities you control as though they didn't have hexproof.",
 119212: 'Destroy target creature. You gain 3 life.',
 119213: '+1: Put the top three cards of your library into your graveyard. If '
         'at least one of them is a Zombie card, each opponent loses 2 life '
         'and you gain 2 life.',
 119214: '-2: Target creature gets -X/-X until end of turn, where X is the '
         'number of Zombies you control.',
 119215: '-3: You may cast Zombie cards from your graveyard this turn.',
 119216: "When Liliana's Contract enters the battlefield, you draw four cards "
         'and you lose 4 life.',
 119217: '-3: Creatures you control get +2/+2 until end of turn.',
 119218: 'When Plague Mare enters the battlefield, creatures your opponents '
         'control get -1/-1 until end of turn.',
 119219: 'Court Cleric gets +1/+1 as long as you control an Ajani '
         'planeswalker.',
 119220: "When Stitcher's Supplier enters the battlefield or dies, put the top "
         'three cards of your library into your graveyard.',
 119221: '{o2}, {oT}: Each opponent loses 1 life and you gain 1 life.',
 119222: 'When Riddlemaster Sphinx enters the battlefield, you may return '
         "target creature an opponent controls to its owner's hand.",
 119223: 'When Vampire Sovereign enters the battlefield, target opponent loses '
         '3 life and you gain 3 life.',
 119224: 'When Shield Mare enters the battlefield or becomes the target of a '
         'spell or ability an opponent controls, you gain 3 life.',
 119225: 'As Alpine Moon enters the battlefield, choose a nonbasic land card '
         'name.',
 119226: 'Lands your opponents control with the chosen name lose all land '
         'types and abilities, and they gain "{oT}: Add one mana of any '
         'color."',
 119227: 'Exile the top seven cards of your library. Until end of turn, you '
         'may cast nonland cards exiled this way.',
 119228: '-1: Return target creature card from your graveyard to your hand.',
 119230: '{o1}, Sacrifice a creature: Exile the top card of your library. You '
         'may play that card this turn.',
 119232: 'When Demanding Dragon enters the battlefield, it deals 5 damage to '
         'target opponent unless that player sacrifices a creature.',
 119233: '+2: Sarkhan, Dragonsoul deals 1 damage to each opponent and each '
         'creature your opponents control.',
 119234: '{o2oR}, {oT}, Sacrifice Dismissive Pyromancer: It deals 4 damage to '
         'target creature.',
 119236: 'Whenever you activate an ability of a Sarkhan planeswalker, '
         "Sarkhan's Whelp deals 1 damage to any target.",
 119237: 'When Goblin Instigator enters the battlefield, create a 1/1 red '
         'Goblin creature token.',
 119238: 'Other Goblins you control get +1/+1.',
 119239: 'Sacrifice a Goblin: Destroy target artifact.',
 119240: 'When Skalla Wolf enters the battlefield, look at the top five cards '
         'of your library. You may reveal a green card from among them and put '
         'it into your hand. Put the rest on the bottom of your library in a '
         'random order.',
 119241: 'Whenever another nontoken Dragon enters the battlefield under your '
         'control, create a 5/5 red Dragon creature token with flying.',
 119242: '{o1oR}: Dragons you control get +1/+0 until end of turn.',
 119244: '-2: Return target creature card with converted mana cost 2 or less '
         'from your graveyard to the battlefield.',
 119245: '+1: You may discard a card. If you do, draw a card.',
 119246: '+1: Add two mana in any combination of colors. Spend this mana only '
         'to cast Dragon spells.',
 119247: '-7: Create four 5/5 red Dragon creature tokens with flying.',
 119249: "Whenever you cast a creature spell with power 4, 5, or 6, Sarkhan's "
         'Unsealing deals 4 damage to any target.',
 119250: 'Whenever a creature enters the battlefield under your control, you '
         'gain 1 life.',
 119251: 'Whenever you cast a creature spell with power 7 or greater, '
         "Sarkhan's Unsealing deals 4 damage to each opponent and each "
         'creature and planeswalker they control.',
 119252: "{o3oR}: Target creature can't block this turn.",
 119253: 'When Sparktongue Dragon enters the battlefield, you may pay {o2oR}. '
         'When you do, it deals 3 damage to any target.',
 119254: 'Whenever a Dragon enters the battlefield under your control, you may '
         'pay {oR}. If you do, return Spit Flame from your graveyard to your '
         'hand.',
 119255: 'Target creature gets +1/+7 until end of turn.',
 119256: 'At the beginning of combat on your turn, target artifact creature '
         'you control gets +2/+2 and gains indestructible until end of turn.',
 119257: '+1: Put a +1/+1 counter on each of up to two target creatures.',
 119259: '-7: You get an emblem with "At the beginning of your end step, '
         'create three 1/1 white Cat creature tokens with lifelink."',
 119260: 'Whenever a creature or planeswalker you control dies, you may '
         "sacrifice Ajani's Last Stand. If you do, create a 4/4 white Avatar "
         'creature token with flying.',
 119261: 'When a spell or ability an opponent controls causes you to discard '
         'this card, if you control a Plains, create a 4/4 white Avatar '
         'creature token with flying.',
 119262: 'When Cavalry Drillmaster enters the battlefield, target creature '
         'gets +2/+0 and gains first strike until end of turn.',
 119263: 'Choose one   Destroy all creatures.  Destroy all artifacts and '
         'enchantments.',
 119264: 'Whenever Herald of Faith attacks, you gain 2 life.',
 120287: "This spell can't be countered.",
 120290: 'Destroy target artifact or enchantment.'}
