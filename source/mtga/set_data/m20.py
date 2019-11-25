
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


AerialAssault = Card(name="aerial_assault", pretty_name="Aerial Assault", cost=['2', 'W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[133630], set_id="M20", rarity="Common", collectible=True, set_number=1,
                     mtga_id=69786)
AjaniStrengthofthePride = Card(name="ajani_strength_of_the_pride", pretty_name="Ajani, Strength of the Pride", cost=['2', 'W', 'W'],
                               color_identity=['W'], card_type="Planeswalker", sub_types="Ajani",
                               abilities=[133631, 133616, 133633], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=2,
                               mtga_id=69787)
AncestralBlade = Card(name="ancestral_blade", pretty_name="Ancestral Blade", cost=['1', 'W'],
                      color_identity=['W'], card_type="Artifact", sub_types="Equipment",
                      abilities=[133634, 1314, 1268], set_id="M20", rarity="Uncommon", collectible=True, set_number=3,
                      mtga_id=69788)
AngelofVitality = Card(name="angel_of_vitality", pretty_name="Angel of Vitality", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Angel",
                       abilities=[8, 133622, 133624], set_id="M20", rarity="Uncommon", collectible=True, set_number=4,
                       mtga_id=69789)
AngelicGift = Card(name="angelic_gift", pretty_name="Angelic Gift", cost=['1', 'W'],
                   color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                   abilities=[1027, 86788, 1187], set_id="M20", rarity="Common", collectible=True, set_number=5,
                   mtga_id=69790)
ApostleofPurifyingLight = Card(name="apostle_of_purifying_light", pretty_name="Apostle of Purifying Light", cost=['1', 'W'],
                               color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                               abilities=[187, 133637], set_id="M20", rarity="Uncommon", collectible=True, set_number=6,
                               mtga_id=69791)
BattalionFootSoldier = Card(name="battalion_foot_soldier", pretty_name="Battalion Foot Soldier", cost=['2', 'W'],
                            color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                            abilities=[116758], set_id="M20", rarity="Common", collectible=True, set_number=7,
                            mtga_id=69792)
BishopofWings = Card(name="bishop_of_wings", pretty_name="Bishop of Wings", cost=['W', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                     abilities=[133639, 133640], set_id="M20", rarity="Rare", collectible=True, set_number=8,
                     mtga_id=69793)
BroughtBack = Card(name="brought_back", pretty_name="Brought Back", cost=['W', 'W'],
                   color_identity=['W'], card_type="Instant", sub_types="",
                   abilities=[133423], set_id="M20", rarity="Rare", collectible=True, set_number=9,
                   mtga_id=69794)
CavalierofDawn = Card(name="cavalier_of_dawn", pretty_name="Cavalier of Dawn", cost=['2', 'W', 'W', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Elemental Knight",
                      abilities=[15, 133537, 133424], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=10,
                      mtga_id=69795)
DawningAngel = Card(name="dawning_angel", pretty_name="Dawning Angel", cost=['4', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Angel",
                    abilities=[8, 88604], set_id="M20", rarity="Common", collectible=True, set_number=11,
                    mtga_id=69796)
DaybreakChaplain = Card(name="daybreak_chaplain", pretty_name="Daybreak Chaplain", cost=['1', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                        abilities=[12], set_id="M20", rarity="Common", collectible=True, set_number=12,
                        mtga_id=69797)
DevoutDecree = Card(name="devout_decree", pretty_name="Devout Decree", cost=['1', 'W'],
                    color_identity=['W'], card_type="Sorcery", sub_types="",
                    abilities=[133440], set_id="M20", rarity="Uncommon", collectible=True, set_number=13,
                    mtga_id=69798)
Disenchant = Card(name="disenchant", pretty_name="Disenchant", cost=['1', 'W'],
                  color_identity=['W'], card_type="Instant", sub_types="",
                  abilities=[120290], set_id="M20", rarity="Common", collectible=True, set_number=14,
                  mtga_id=69799)
EternalIsolation = Card(name="eternal_isolation", pretty_name="Eternal Isolation", cost=['1', 'W'],
                        color_identity=['W'], card_type="Sorcery", sub_types="",
                        abilities=[133463], set_id="M20", rarity="Uncommon", collectible=True, set_number=15,
                        mtga_id=69800)
FencingAce = Card(name="fencing_ace", pretty_name="Fencing Ace", cost=['1', 'W'],
                  color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                  abilities=[3], set_id="M20", rarity="Uncommon", collectible=True, set_number=16,
                  mtga_id=69801)
GauntletsofLight = Card(name="gauntlets_of_light", pretty_name="Gauntlets of Light", cost=['2', 'W'],
                        color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 133483, 133513], set_id="M20", rarity="Uncommon", collectible=True, set_number=17,
                        mtga_id=69802)
GlaringAegis = Card(name="glaring_aegis", pretty_name="Glaring Aegis", cost=['W'],
                    color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1027, 101945, 1103], set_id="M20", rarity="Common", collectible=True, set_number=18,
                    mtga_id=69803)
GodsWilling = Card(name="gods_willing", pretty_name="Gods Willing", cost=['W'],
                   color_identity=['W'], card_type="Instant", sub_types="",
                   abilities=[20551, 178], set_id="M20", rarity="Uncommon", collectible=True, set_number=19,
                   mtga_id=69804)
GriffinProtector = Card(name="griffin_protector", pretty_name="Griffin Protector", cost=['3', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Griffin",
                        abilities=[8, 99868], set_id="M20", rarity="Common", collectible=True, set_number=20,
                        mtga_id=69805)
GriffinSentinel = Card(name="griffin_sentinel", pretty_name="Griffin Sentinel", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Griffin",
                       abilities=[8, 15], set_id="M20", rarity="Common", collectible=True, set_number=21,
                       mtga_id=69806)
HangedExecutioner = Card(name="hanged_executioner", pretty_name="Hanged Executioner", cost=['2', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Spirit",
                         abilities=[8, 103130, 133565], set_id="M20", rarity="Rare", collectible=True, set_number=22,
                         mtga_id=69807)
HeraldoftheSun = Card(name="herald_of_the_sun", pretty_name="Herald of the Sun", cost=['4', 'W', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Angel",
                      abilities=[8, 133568], set_id="M20", rarity="Uncommon", collectible=True, set_number=23,
                      mtga_id=69808)
InspiredCharge = Card(name="inspired_charge", pretty_name="Inspired Charge", cost=['2', 'W', 'W'],
                      color_identity=['W'], card_type="Instant", sub_types="",
                      abilities=[11632], set_id="M20", rarity="Common", collectible=True, set_number=24,
                      mtga_id=69809)
InspiringCaptain = Card(name="inspiring_captain", pretty_name="Inspiring Captain", cost=['3', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                        abilities=[63634], set_id="M20", rarity="Common", collectible=True, set_number=25,
                        mtga_id=69810)
LeylineofSanctity = Card(name="leyline_of_sanctity", pretty_name="Leyline of Sanctity", cost=['2', 'W', 'W'],
                         color_identity=['W'], card_type="Enchantment", sub_types="",
                         abilities=[91944, 2655], set_id="M20", rarity="Rare", collectible=True, set_number=26,
                         mtga_id=69811)
LoxodonLifechanter = Card(name="loxodon_lifechanter", pretty_name="Loxodon Lifechanter", cost=['5', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Elephant Cleric",
                          abilities=[133588, 133435], set_id="M20", rarity="Rare", collectible=True, set_number=27,
                          mtga_id=69812)
LoyalPegasus = Card(name="loyal_pegasus", pretty_name="Loyal Pegasus", cost=['W'],
                    color_identity=['W'], card_type="Creature", sub_types="Pegasus",
                    abilities=[8, 87894], set_id="M20", rarity="Uncommon", collectible=True, set_number=28,
                    mtga_id=69813)
MasterSplicer = Card(name="master_splicer", pretty_name="Master Splicer", cost=['3', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Artificer",
                     abilities=[95377, 15953], set_id="M20", rarity="Uncommon", collectible=True, set_number=29,
                     mtga_id=69814)
MomentofHeroism = Card(name="moment_of_heroism", pretty_name="Moment of Heroism", cost=['1', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[2090], set_id="M20", rarity="Common", collectible=True, set_number=30,
                       mtga_id=69815)
MoorlandInquisitor = Card(name="moorland_inquisitor", pretty_name="Moorland Inquisitor", cost=['1', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                          abilities=[99802], set_id="M20", rarity="Common", collectible=True, set_number=31,
                          mtga_id=69816)
Pacifism = Card(name="pacifism", pretty_name="Pacifism", cost=['1', 'W'],
                color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                abilities=[1027, 1083], set_id="M20", rarity="Common", collectible=True, set_number=32,
                mtga_id=69817)
PlanarCleansing = Card(name="planar_cleansing", pretty_name="Planar Cleansing", cost=['3', 'W', 'W', 'W'],
                       color_identity=['W'], card_type="Sorcery", sub_types="",
                       abilities=[2763], set_id="M20", rarity="Rare", collectible=True, set_number=33,
                       mtga_id=69818)
RaisetheAlarm = Card(name="raise_the_alarm", pretty_name="Raise the Alarm", cost=['1', 'W'],
                     color_identity=['W'], card_type="Instant", sub_types="",
                     abilities=[2085], set_id="M20", rarity="Common", collectible=True, set_number=34,
                     mtga_id=69819)
RuleofLaw = Card(name="rule_of_law", pretty_name="Rule of Law", cost=['2', 'W'],
                 color_identity=['W'], card_type="Enchantment", sub_types="",
                 abilities=[88183], set_id="M20", rarity="Uncommon", collectible=True, set_number=35,
                 mtga_id=69820)
SepharaSkysBlade = Card(name="sephara_skys_blade", pretty_name="Sephara, Sky's Blade", cost=['4', 'W', 'W', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Angel",
                        abilities=[133449, 8, 12, 133453], set_id="M20", rarity="Rare", collectible=True, set_number=36,
                        mtga_id=69821)
Soulmender = Card(name="soulmender", pretty_name="Soulmender", cost=['W'],
                  color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                  abilities=[7247], set_id="M20", rarity="Common", collectible=True, set_number=37,
                  mtga_id=69822)
SquadCaptain = Card(name="squad_captain", pretty_name="Squad Captain", cost=['4', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                    abilities=[15, 133459], set_id="M20", rarity="Common", collectible=True, set_number=38,
                    mtga_id=69823)
StarfieldMystic = Card(name="starfield_mystic", pretty_name="Starfield Mystic", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                       abilities=[62067, 133466], set_id="M20", rarity="Rare", collectible=True, set_number=39,
                       mtga_id=69824)
SteadfastSentry = Card(name="steadfast_sentry", pretty_name="Steadfast Sentry", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                       abilities=[15, 87008], set_id="M20", rarity="Common", collectible=True, set_number=40,
                       mtga_id=69825)
YokedOx = Card(name="yoked_ox", pretty_name="Yoked Ox", cost=['W'],
               color_identity=['W'], card_type="Creature", sub_types="Ox",
               abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=41,
               mtga_id=69826)
AetherGust = Card(name="aether_gust", pretty_name="Aether Gust", cost=['1', 'U'],
                  color_identity=['U'], card_type="Instant", sub_types="",
                  abilities=[133472], set_id="M20", rarity="Uncommon", collectible=True, set_number=42,
                  mtga_id=69827)
AgentofTreachery = Card(name="agent_of_treachery", pretty_name="Agent of Treachery", cost=['5', 'U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Human Rogue",
                        abilities=[133477, 133482], set_id="M20", rarity="Rare", collectible=True, set_number=43,
                        mtga_id=69828)
AirElemental = Card(name="air_elemental", pretty_name="Air Elemental", cost=['3', 'U', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Elemental",
                    abilities=[8], set_id="M20", rarity="Uncommon", collectible=True, set_number=44,
                    mtga_id=69829)
Anticipate = Card(name="anticipate", pretty_name="Anticipate", cost=['1', 'U'],
                  color_identity=['U'], card_type="Instant", sub_types="",
                  abilities=[61084], set_id="M20", rarity="Common", collectible=True, set_number=45,
                  mtga_id=69830)
AtemsisAllSeeing = Card(name="atemsis_allseeing", pretty_name="Atemsis, All-Seeing", cost=['3', 'U', 'U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                        abilities=[8, 133492, 133498], set_id="M20", rarity="Rare", collectible=True, set_number=46,
                        mtga_id=69831)
Befuddle = Card(name="befuddle", pretty_name="Befuddle", cost=['2', 'U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[63602, 25848], set_id="M20", rarity="Common", collectible=True, set_number=47,
                mtga_id=69832)
BonetoAsh = Card(name="bone_to_ash", pretty_name="Bone to Ash", cost=['2', 'U', 'U'],
                 color_identity=['U'], card_type="Instant", sub_types="",
                 abilities=[24121, 25848], set_id="M20", rarity="Common", collectible=True, set_number=48,
                 mtga_id=69833)
BorealElemental = Card(name="boreal_elemental", pretty_name="Boreal Elemental", cost=['4', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Elemental",
                       abilities=[8, 96148], set_id="M20", rarity="Common", collectible=True, set_number=49,
                       mtga_id=69834)
BrinebornCutthroat = Card(name="brineborn_cutthroat", pretty_name="Brineborn Cutthroat", cost=['1', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Merfolk Pirate",
                          abilities=[7, 133509], set_id="M20", rarity="Uncommon", collectible=True, set_number=50,
                          mtga_id=69835)
CaptivatingGyre = Card(name="captivating_gyre", pretty_name="Captivating Gyre", cost=['4', 'U', 'U'],
                       color_identity=['U'], card_type="Sorcery", sub_types="",
                       abilities=[133511], set_id="M20", rarity="Uncommon", collectible=True, set_number=51,
                       mtga_id=69836)
CavalierofGales = Card(name="cavalier_of_gales", pretty_name="Cavalier of Gales", cost=['2', 'U', 'U', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Elemental Knight",
                       abilities=[8, 117053, 133516], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=52,
                       mtga_id=69837)
CeruleanDrake = Card(name="cerulean_drake", pretty_name="Cerulean Drake", cost=['1', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Drake",
                     abilities=[8, 188, 133522], set_id="M20", rarity="Uncommon", collectible=True, set_number=53,
                     mtga_id=69838)
CloudkinSeer = Card(name="cloudkin_seer", pretty_name="Cloudkin Seer", cost=['2', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Elemental Wizard",
                    abilities=[8, 86788], set_id="M20", rarity="Common", collectible=True, set_number=54,
                    mtga_id=69839)
Convolute = Card(name="convolute", pretty_name="Convolute", cost=['2', 'U'],
                 color_identity=['U'], card_type="Instant", sub_types="",
                 abilities=[17253], set_id="M20", rarity="Common", collectible=True, set_number=55,
                 mtga_id=69840)
DrawnfromDreams = Card(name="drawn_from_dreams", pretty_name="Drawn from Dreams", cost=['2', 'U', 'U'],
                       color_identity=['U'], card_type="Sorcery", sub_types="",
                       abilities=[133533], set_id="M20", rarity="Rare", collectible=True, set_number=56,
                       mtga_id=69841)
DungeonGeists = Card(name="dungeon_geists", pretty_name="Dungeon Geists", cost=['2', 'U', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Spirit",
                     abilities=[8, 99583], set_id="M20", rarity="Rare", collectible=True, set_number=57,
                     mtga_id=69842)
FaerieMiscreant = Card(name="faerie_miscreant", pretty_name="Faerie Miscreant", cost=['U'],
                       color_identity=['U'], card_type="Creature", sub_types="Faerie Rogue",
                       abilities=[8, 102223], set_id="M20", rarity="Common", collectible=True, set_number=58,
                       mtga_id=69843)
FloodofTears = Card(name="flood_of_tears", pretty_name="Flood of Tears", cost=['4', 'U', 'U'],
                    color_identity=['U'], card_type="Sorcery", sub_types="",
                    abilities=[133546], set_id="M20", rarity="Rare", collectible=True, set_number=59,
                    mtga_id=69844)
FortressCrab = Card(name="fortress_crab", pretty_name="Fortress Crab", cost=['3', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Crab",
                    abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=60,
                    mtga_id=69845)
FrilledSeaSerpent = Card(name="frilled_sea_serpent", pretty_name="Frilled Sea Serpent", cost=['4', 'U', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Serpent",
                         abilities=[119156], set_id="M20", rarity="Common", collectible=True, set_number=61,
                         mtga_id=69846)
FrostLynx = Card(name="frost_lynx", pretty_name="Frost Lynx", cost=['2', 'U'],
                 color_identity=['U'], card_type="Creature", sub_types="Elemental Cat",
                 abilities=[76874], set_id="M20", rarity="Common", collectible=True, set_number=62,
                 mtga_id=69847)
HardCover = Card(name="hard_cover", pretty_name="Hard Cover", cost=['U'],
                 color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                 abilities=[1027, 133548], set_id="M20", rarity="Uncommon", collectible=True, set_number=63,
                 mtga_id=69848)
LeylineofAnticipation = Card(name="leyline_of_anticipation", pretty_name="Leyline of Anticipation", cost=['2', 'U', 'U'],
                             color_identity=['U'], card_type="Enchantment", sub_types="",
                             abilities=[91944, 6951], set_id="M20", rarity="Rare", collectible=True, set_number=64,
                             mtga_id=69849)
MasterfulReplication = Card(name="masterful_replication", pretty_name="Masterful Replication", cost=['5', 'U'],
                            color_identity=['U'], card_type="Instant", sub_types="",
                            abilities=[133553], set_id="M20", rarity="Rare", collectible=True, set_number=65,
                            mtga_id=69850)
MetropolisSprite = Card(name="metropolis_sprite", pretty_name="Metropolis Sprite", cost=['1', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Faerie Rogue",
                        abilities=[8, 92933], set_id="M20", rarity="Common", collectible=True, set_number=66,
                        mtga_id=69851)
MoatPiranhas = Card(name="moat_piranhas", pretty_name="Moat Piranhas", cost=['1', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Fish",
                    abilities=[2], set_id="M20", rarity="Common", collectible=True, set_number=67,
                    mtga_id=69852)
MuYanlingSkyDancer = Card(name="mu_yanling_sky_dancer", pretty_name="Mu Yanling, Sky Dancer", cost=['1', 'U', 'U'],
                          color_identity=['U'], card_type="Planeswalker", sub_types="Yanling",
                          abilities=[133554, 133556, 133560], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=68,
                          mtga_id=69853)
Negate = Card(name="negate", pretty_name="Negate", cost=['1', 'U'],
              color_identity=['U'], card_type="Instant", sub_types="",
              abilities=[1142], set_id="M20", rarity="Common", collectible=True, set_number=69,
              mtga_id=69854)
Octoprophet = Card(name="octoprophet", pretty_name="Octoprophet", cost=['3', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Octopus",
                   abilities=[100685], set_id="M20", rarity="Common", collectible=True, set_number=70,
                   mtga_id=69855)
PortalofSanctuary = Card(name="portal_of_sanctuary", pretty_name="Portal of Sanctuary", cost=['2', 'U'],
                         color_identity=['U'], card_type="Artifact", sub_types="",
                         abilities=[133562], set_id="M20", rarity="Uncommon", collectible=True, set_number=71,
                         mtga_id=69856)
RenownedWeaponsmith = Card(name="renowned_weaponsmith", pretty_name="Renowned Weaponsmith", cost=['1', 'U'],
                           color_identity=['U'], card_type="Creature", sub_types="Human Artificer",
                           abilities=[22549, 22550], set_id="M20", rarity="Uncommon", collectible=True, set_number=72,
                           mtga_id=69857)
SagesRowDenizen = Card(name="sages_row_denizen", pretty_name="Sage's Row Denizen", cost=['2', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Vedalken Wizard",
                       abilities=[19680], set_id="M20", rarity="Common", collectible=True, set_number=73,
                       mtga_id=69858)
ScholaroftheAges = Card(name="scholar_of_the_ages", pretty_name="Scholar of the Ages", cost=['5', 'U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                        abilities=[133564], set_id="M20", rarity="Uncommon", collectible=True, set_number=74,
                        mtga_id=69859)
SleepParalysis = Card(name="sleep_paralysis", pretty_name="Sleep Paralysis", cost=['3', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                      abilities=[1027, 89789, 88178], set_id="M20", rarity="Common", collectible=True, set_number=75,
                      mtga_id=69860)
SpectralSailor = Card(name="spectral_sailor", pretty_name="Spectral Sailor", cost=['U'],
                      color_identity=['U'], card_type="Creature", sub_types="Spirit Pirate",
                      abilities=[7, 8, 1104], set_id="M20", rarity="Uncommon", collectible=True, set_number=76,
                      mtga_id=69861)
TalesEnd = Card(name="tales_end", pretty_name="Tale's End", cost=['1', 'U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[133567], set_id="M20", rarity="Rare", collectible=True, set_number=77,
                mtga_id=69862)
Unsummon = Card(name="unsummon", pretty_name="Unsummon", cost=['U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[22505], set_id="M20", rarity="Common", collectible=True, set_number=78,
                mtga_id=69863)
WardenofEvosIsle = Card(name="warden_of_evos_isle", pretty_name="Warden of Evos Isle", cost=['2', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Bird Wizard",
                        abilities=[8, 20230], set_id="M20", rarity="Uncommon", collectible=True, set_number=79,
                        mtga_id=69864)
WingedWords = Card(name="winged_words", pretty_name="Winged Words", cost=['2', 'U'],
                   color_identity=['U'], card_type="Sorcery", sub_types="",
                   abilities=[133569, 23607], set_id="M20", rarity="Common", collectible=True, set_number=80,
                   mtga_id=69865)
YaroksWavecrasher = Card(name="yaroks_wavecrasher", pretty_name="Yarok's Wavecrasher", cost=['3', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Elemental",
                         abilities=[101887], set_id="M20", rarity="Uncommon", collectible=True, set_number=81,
                         mtga_id=69866)
ZephyrCharge = Card(name="zephyr_charge", pretty_name="Zephyr Charge", cost=['1', 'U'],
                    color_identity=['U'], card_type="Enchantment", sub_types="",
                    abilities=[20341], set_id="M20", rarity="Common", collectible=True, set_number=82,
                    mtga_id=69867)
AgonizingSyphon = Card(name="agonizing_syphon", pretty_name="Agonizing Syphon", cost=['3', 'B'],
                       color_identity=['B'], card_type="Sorcery", sub_types="",
                       abilities=[88264], set_id="M20", rarity="Common", collectible=True, set_number=83,
                       mtga_id=69868)
AudaciousThief = Card(name="audacious_thief", pretty_name="Audacious Thief", cost=['2', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Human Rogue",
                      abilities=[133572], set_id="M20", rarity="Common", collectible=True, set_number=84,
                      mtga_id=69869)
BaronyVampire = Card(name="barony_vampire", pretty_name="Barony Vampire", cost=['2', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Vampire",
                     abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=85,
                     mtga_id=69870)
Bladebrand = Card(name="bladebrand", pretty_name="Bladebrand", cost=['1', 'B'],
                  color_identity=['B'], card_type="Instant", sub_types="",
                  abilities=[4294, 25848], set_id="M20", rarity="Common", collectible=True, set_number=86,
                  mtga_id=69871)
Blightbeetle = Card(name="blightbeetle", pretty_name="Blightbeetle", cost=['1', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Insect",
                    abilities=[189, 133575], set_id="M20", rarity="Uncommon", collectible=True, set_number=87,
                    mtga_id=69872)
BloodBurglar = Card(name="blood_burglar", pretty_name="Blood Burglar", cost=['1', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Vampire Rogue",
                    abilities=[133576], set_id="M20", rarity="Common", collectible=True, set_number=88,
                    mtga_id=69873)
BloodforBones = Card(name="blood_for_bones", pretty_name="Blood for Bones", cost=['3', 'B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[1275, 133579], set_id="M20", rarity="Uncommon", collectible=True, set_number=89,
                     mtga_id=69874)
BloodsoakedAltar = Card(name="bloodsoaked_altar", pretty_name="Bloodsoaked Altar", cost=['4', 'B', 'B'],
                        color_identity=['B'], card_type="Artifact", sub_types="",
                        abilities=[133580], set_id="M20", rarity="Uncommon", collectible=True, set_number=90,
                        mtga_id=69875)
BloodthirstyAerialist = Card(name="bloodthirsty_aerialist", pretty_name="Bloodthirsty Aerialist", cost=['1', 'B', 'B'],
                             color_identity=['B'], card_type="Creature", sub_types="Vampire Rogue",
                             abilities=[8, 92970], set_id="M20", rarity="Uncommon", collectible=True, set_number=91,
                             mtga_id=69876)
BoneSplinters = Card(name="bone_splinters", pretty_name="Bone Splinters", cost=['B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[1275, 26818], set_id="M20", rarity="Common", collectible=True, set_number=92,
                     mtga_id=69877)
BonecladNecromancer = Card(name="boneclad_necromancer", pretty_name="Boneclad Necromancer", cost=['3', 'B', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Human Wizard",
                           abilities=[133582], set_id="M20", rarity="Common", collectible=True, set_number=93,
                           mtga_id=69878)
CavalierofNight = Card(name="cavalier_of_night", pretty_name="Cavalier of Night", cost=['2', 'B', 'B', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Elemental Knight",
                       abilities=[12, 133583, 133584], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=94,
                       mtga_id=69879)
Disfigure = Card(name="disfigure", pretty_name="Disfigure", cost=['B'],
                 color_identity=['B'], card_type="Instant", sub_types="",
                 abilities=[27907], set_id="M20", rarity="Uncommon", collectible=True, set_number=95,
                 mtga_id=69880)
DreadPresence = Card(name="dread_presence", pretty_name="Dread Presence", cost=['3', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Nightmare",
                     abilities=[133427], set_id="M20", rarity="Rare", collectible=True, set_number=96,
                     mtga_id=69881)
Duress = Card(name="duress", pretty_name="Duress", cost=['B'],
              color_identity=['B'], card_type="Sorcery", sub_types="",
              abilities=[21775], set_id="M20", rarity="Common", collectible=True, set_number=97,
              mtga_id=69882)
EmbodimentofAgonies = Card(name="embodiment_of_agonies", pretty_name="Embodiment of Agonies", cost=['1', 'B', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Demon",
                           abilities=[8, 1, 133428], set_id="M20", rarity="Rare", collectible=True, set_number=98,
                           mtga_id=69883)
EpicureofBlood = Card(name="epicure_of_blood", pretty_name="Epicure of Blood", cost=['4', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Vampire",
                      abilities=[62618], set_id="M20", rarity="Common", collectible=True, set_number=99,
                      mtga_id=69884)
FathomFleetCutthroat = Card(name="fathom_fleet_cutthroat", pretty_name="Fathom Fleet Cutthroat", cost=['3', 'B'],
                            color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                            abilities=[1127], set_id="M20", rarity="Common", collectible=True, set_number=100,
                            mtga_id=69885)
FeralAbomination = Card(name="feral_abomination", pretty_name="Feral Abomination", cost=['5', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Thrull",
                        abilities=[1], set_id="M20", rarity="Common", collectible=True, set_number=101,
                        mtga_id=69886)
GorgingVulture = Card(name="gorging_vulture", pretty_name="Gorging Vulture", cost=['2', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Bird",
                      abilities=[8, 133429], set_id="M20", rarity="Common", collectible=True, set_number=102,
                      mtga_id=69887)
Gravedigger = Card(name="gravedigger", pretty_name="Gravedigger", cost=['3', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Zombie",
                   abilities=[1157], set_id="M20", rarity="Uncommon", collectible=True, set_number=103,
                   mtga_id=69888)
GruesomeScourger = Card(name="gruesome_scourger", pretty_name="Gruesome Scourger", cost=['3', 'B', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Orc Warrior",
                        abilities=[133590], set_id="M20", rarity="Uncommon", collectible=True, set_number=104,
                        mtga_id=69889)
KnightoftheEbonLegion = Card(name="knight_of_the_ebon_legion", pretty_name="Knight of the Ebon Legion", cost=['B'],
                             color_identity=['B'], card_type="Creature", sub_types="Vampire Knight",
                             abilities=[133430, 133431], set_id="M20", rarity="Rare", collectible=True, set_number=105,
                             mtga_id=69890)
LegionsEnd = Card(name="legions_end", pretty_name="Legion's End", cost=['1', 'B'],
                  color_identity=['B'], card_type="Sorcery", sub_types="",
                  abilities=[133432], set_id="M20", rarity="Rare", collectible=True, set_number=106,
                  mtga_id=69891)
LeylineoftheVoid = Card(name="leyline_of_the_void", pretty_name="Leyline of the Void", cost=['2', 'B', 'B'],
                        color_identity=['B'], card_type="Enchantment", sub_types="",
                        abilities=[91944, 91950], set_id="M20", rarity="Rare", collectible=True, set_number=107,
                        mtga_id=69892)
MindRot = Card(name="mind_rot", pretty_name="Mind Rot", cost=['2', 'B'],
               color_identity=['B'], card_type="Sorcery", sub_types="",
               abilities=[23608], set_id="M20", rarity="Common", collectible=True, set_number=108,
               mtga_id=69893)
Murder = Card(name="murder", pretty_name="Murder", cost=['1', 'B', 'B'],
              color_identity=['B'], card_type="Instant", sub_types="",
              abilities=[26818], set_id="M20", rarity="Common", collectible=True, set_number=109,
              mtga_id=69894)
NoxiousGrasp = Card(name="noxious_grasp", pretty_name="Noxious Grasp", cost=['1', 'B'],
                    color_identity=['B'], card_type="Instant", sub_types="",
                    abilities=[133433], set_id="M20", rarity="Uncommon", collectible=True, set_number=110,
                    mtga_id=69895)
RottingRegisaur = Card(name="rotting_regisaur", pretty_name="Rotting Regisaur", cost=['2', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Zombie Dinosaur",
                       abilities=[133592], set_id="M20", rarity="Rare", collectible=True, set_number=111,
                       mtga_id=69896)
SanitariumSkeleton = Card(name="sanitarium_skeleton", pretty_name="Sanitarium Skeleton", cost=['B'],
                          color_identity=['B'], card_type="Creature", sub_types="Skeleton",
                          abilities=[102887], set_id="M20", rarity="Common", collectible=True, set_number=112,
                          mtga_id=69897)
SchemingSymmetry = Card(name="scheming_symmetry", pretty_name="Scheming Symmetry", cost=['B'],
                        color_identity=['B'], card_type="Sorcery", sub_types="",
                        abilities=[133593], set_id="M20", rarity="Rare", collectible=True, set_number=113,
                        mtga_id=69898)
SorcereroftheFang = Card(name="sorcerer_of_the_fang", pretty_name="Sorcerer of the Fang", cost=['1', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Human Wizard",
                         abilities=[133595], set_id="M20", rarity="Common", collectible=True, set_number=114,
                         mtga_id=69899)
SorinImperiousBloodlord = Card(name="sorin_imperious_bloodlord", pretty_name="Sorin, Imperious Bloodlord", cost=['2', 'B'],
                               color_identity=['B'], card_type="Planeswalker", sub_types="Sorin",
                               abilities=[133596, 133597, 133598], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=115,
                               mtga_id=69900)
SoulSalvage = Card(name="soul_salvage", pretty_name="Soul Salvage", cost=['2', 'B'],
                   color_identity=['B'], card_type="Sorcery", sub_types="",
                   abilities=[1923], set_id="M20", rarity="Common", collectible=True, set_number=116,
                   mtga_id=69901)
ThoughtDistortion = Card(name="thought_distortion", pretty_name="Thought Distortion", cost=['4', 'B', 'B'],
                         color_identity=['B'], card_type="Sorcery", sub_types="",
                         abilities=[120287, 133434], set_id="M20", rarity="Uncommon", collectible=True, set_number=117,
                         mtga_id=69902)
UndeadServant = Card(name="undead_servant", pretty_name="Undead Servant", cost=['3', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Zombie",
                     abilities=[102284], set_id="M20", rarity="Common", collectible=True, set_number=118,
                     mtga_id=69903)
UnholyIndenture = Card(name="unholy_indenture", pretty_name="Unholy Indenture", cost=['2', 'B'],
                       color_identity=['B'], card_type="Enchantment", sub_types="Aura",
                       abilities=[1027, 133599], set_id="M20", rarity="Common", collectible=True, set_number=119,
                       mtga_id=69904)
VampireoftheDireMoon = Card(name="vampire_of_the_dire_moon", pretty_name="Vampire of the Dire Moon", cost=['B'],
                            color_identity=['B'], card_type="Creature", sub_types="Vampire",
                            abilities=[1, 12], set_id="M20", rarity="Uncommon", collectible=True, set_number=120,
                            mtga_id=69905)
VengefulWarchief = Card(name="vengeful_warchief", pretty_name="Vengeful Warchief", cost=['4', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Orc Warrior",
                        abilities=[133600], set_id="M20", rarity="Uncommon", collectible=True, set_number=121,
                        mtga_id=69906)
VilisBrokerofBlood = Card(name="vilis_broker_of_blood", pretty_name="Vilis, Broker of Blood", cost=['5', 'B', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Demon",
                          abilities=[8, 133601, 133602], set_id="M20", rarity="Rare", collectible=True, set_number=122,
                          mtga_id=69907)
YaroksFenlurker = Card(name="yaroks_fenlurker", pretty_name="Yarok's Fenlurker", cost=['B', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Horror",
                       abilities=[133603, 93172], set_id="M20", rarity="Uncommon", collectible=True, set_number=123,
                       mtga_id=69908)
ActofTreason = Card(name="act_of_treason", pretty_name="Act of Treason", cost=['2', 'R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[1278], set_id="M20", rarity="Common", collectible=True, set_number=124,
                    mtga_id=69909)
CavalierofFlame = Card(name="cavalier_of_flame", pretty_name="Cavalier of Flame", cost=['2', 'R', 'R', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Elemental Knight",
                       abilities=[133436, 133437, 133605], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=125,
                       mtga_id=69910)
ChandraAcolyteofFlame = Card(name="chandra_acolyte_of_flame", pretty_name="Chandra, Acolyte of Flame", cost=['1', 'R', 'R'],
                             color_identity=['R'], card_type="Planeswalker", sub_types="Chandra",
                             abilities=[133606, 133607, 133608], set_id="M20", rarity="Rare", collectible=True, set_number=126,
                             mtga_id=69911)
ChandraAwakenedInferno = Card(name="chandra_awakened_inferno", pretty_name="Chandra, Awakened Inferno", cost=['4', 'R', 'R'],
                              color_identity=['R'], card_type="Planeswalker", sub_types="Chandra",
                              abilities=[120287, 133609, 133610, 133612], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=127,
                              mtga_id=69912)
ChandraNovicePyromancer = Card(name="chandra_novice_pyromancer", pretty_name="Chandra, Novice Pyromancer", cost=['3', 'R'],
                               color_identity=['R'], card_type="Planeswalker", sub_types="Chandra",
                               abilities=[133561, 133613, 133292], set_id="M20", rarity="Uncommon", collectible=True, set_number=128,
                               mtga_id=69913)
ChandrasEmbercat = Card(name="chandras_embercat", pretty_name="Chandra's Embercat", cost=['1', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Elemental Cat",
                        abilities=[133614], set_id="M20", rarity="Common", collectible=True, set_number=129,
                        mtga_id=69914)
ChandrasOutrage = Card(name="chandras_outrage", pretty_name="Chandra's Outrage", cost=['2', 'R', 'R'],
                       color_identity=['R'], card_type="Instant", sub_types="",
                       abilities=[1204], set_id="M20", rarity="Common", collectible=True, set_number=130,
                       mtga_id=69915)
ChandrasRegulator = Card(name="chandras_regulator", pretty_name="Chandra's Regulator", cost=['1', 'R'],
                         color_identity=['R'], card_type="Artifact", sub_types="",
                         abilities=[133439, 133617], set_id="M20", rarity="Rare", collectible=True, set_number=131,
                         mtga_id=69916)
ChandrasSpitfire = Card(name="chandras_spitfire", pretty_name="Chandra's Spitfire", cost=['2', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Elemental",
                        abilities=[8, 92943], set_id="M20", rarity="Uncommon", collectible=True, set_number=132,
                        mtga_id=69917)
DaggersailAeronaut = Card(name="daggersail_aeronaut", pretty_name="Daggersail Aeronaut", cost=['3', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Goblin",
                          abilities=[133619], set_id="M20", rarity="Common", collectible=True, set_number=133,
                          mtga_id=69918)
DestructiveDigger = Card(name="destructive_digger", pretty_name="Destructive Digger", cost=['2', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin",
                         abilities=[133620], set_id="M20", rarity="Common", collectible=True, set_number=134,
                         mtga_id=69919)
DragonMage = Card(name="dragon_mage", pretty_name="Dragon Mage", cost=['5', 'R', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Dragon Wizard",
                  abilities=[8, 97002], set_id="M20", rarity="Uncommon", collectible=True, set_number=135,
                  mtga_id=69920)
DrakusethMawofFlames = Card(name="drakuseth_maw_of_flames", pretty_name="Drakuseth, Maw of Flames", cost=['4', 'R', 'R', 'R'],
                            color_identity=['R'], card_type="Creature", sub_types="Dragon",
                            abilities=[8, 133623], set_id="M20", rarity="Rare", collectible=True, set_number=136,
                            mtga_id=69921)
EmberHauler = Card(name="ember_hauler", pretty_name="Ember Hauler", cost=['R', 'R'],
                   color_identity=['R'], card_type="Creature", sub_types="Goblin",
                   abilities=[2164], set_id="M20", rarity="Uncommon", collectible=True, set_number=137,
                   mtga_id=69922)
FireElemental = Card(name="fire_elemental", pretty_name="Fire Elemental", cost=['3', 'R', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Elemental",
                     abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=138,
                     mtga_id=69923)
FlameSweep = Card(name="flame_sweep", pretty_name="Flame Sweep", cost=['2', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[133625], set_id="M20", rarity="Uncommon", collectible=True, set_number=139,
                  mtga_id=69924)
Fry = Card(name="fry", pretty_name="Fry", cost=['1', 'R'],
           color_identity=['R'], card_type="Instant", sub_types="",
           abilities=[120287, 133626], set_id="M20", rarity="Uncommon", collectible=True, set_number=140,
           mtga_id=69925)
GlintHornBuccaneer = Card(name="glinthorn_buccaneer", pretty_name="Glint-Horn Buccaneer", cost=['1', 'R', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Minotaur Pirate",
                          abilities=[9, 133627, 133628], set_id="M20", rarity="Rare", collectible=True, set_number=141,
                          mtga_id=69926)
GoblinBirdGrabber = Card(name="goblin_birdgrabber", pretty_name="Goblin Bird-Grabber", cost=['1', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin",
                         abilities=[133629], set_id="M20", rarity="Common", collectible=True, set_number=142,
                         mtga_id=69927)
GoblinRingleader = Card(name="goblin_ringleader", pretty_name="Goblin Ringleader", cost=['3', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Goblin",
                        abilities=[9, 89147], set_id="M20", rarity="Uncommon", collectible=True, set_number=143,
                        mtga_id=69928)
GoblinSmuggler = Card(name="goblin_smuggler", pretty_name="Goblin Smuggler", cost=['2', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Goblin Rogue",
                      abilities=[9, 133636], set_id="M20", rarity="Common", collectible=True, set_number=144,
                      mtga_id=69929)
Infuriate = Card(name="infuriate", pretty_name="Infuriate", cost=['R'],
                 color_identity=['R'], card_type="Instant", sub_types="",
                 abilities=[133638], set_id="M20", rarity="Common", collectible=True, set_number=145,
                 mtga_id=69930)
KeldonRaider = Card(name="keldon_raider", pretty_name="Keldon Raider", cost=['2', 'R', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                    abilities=[100041], set_id="M20", rarity="Common", collectible=True, set_number=146,
                    mtga_id=69931)
LavakinBrawler = Card(name="lavakin_brawler", pretty_name="Lavakin Brawler", cost=['3', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Elemental Warrior",
                      abilities=[133555], set_id="M20", rarity="Common", collectible=True, set_number=147,
                      mtga_id=69932)
LeylineofCombustion = Card(name="leyline_of_combustion", pretty_name="Leyline of Combustion", cost=['2', 'R', 'R'],
                           color_identity=['R'], card_type="Enchantment", sub_types="",
                           abilities=[91944, 133574], set_id="M20", rarity="Rare", collectible=True, set_number=148,
                           mtga_id=69933)
ManiacalRage = Card(name="maniacal_rage", pretty_name="Maniacal Rage", cost=['1', 'R'],
                    color_identity=['R'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1027, 90333], set_id="M20", rarity="Common", collectible=True, set_number=149,
                    mtga_id=69934)
MaraudingRaptor = Card(name="marauding_raptor", pretty_name="Marauding Raptor", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[63468, 133441], set_id="M20", rarity="Rare", collectible=True, set_number=150,
                       mtga_id=69935)
MaskofImmolation = Card(name="mask_of_immolation", pretty_name="Mask of Immolation", cost=['1', 'R'],
                        color_identity=['R'], card_type="Artifact", sub_types="Equipment",
                        abilities=[133442, 133444, 1319], set_id="M20", rarity="Uncommon", collectible=True, set_number=151,
                        mtga_id=69936)
PackMastiff = Card(name="pack_mastiff", pretty_name="Pack Mastiff", cost=['1', 'R'],
                   color_identity=['R'], card_type="Creature", sub_types="Hound",
                   abilities=[133545], set_id="M20", rarity="Common", collectible=True, set_number=152,
                   mtga_id=69937)
RapaciousDragon = Card(name="rapacious_dragon", pretty_name="Rapacious Dragon", cost=['4', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Dragon",
                       abilities=[8, 116820], set_id="M20", rarity="Uncommon", collectible=True, set_number=153,
                       mtga_id=69938)
RecklessAirStrike = Card(name="reckless_air_strike", pretty_name="Reckless Air Strike", cost=['R'],
                         color_identity=['R'], card_type="Sorcery", sub_types="",
                         abilities=[133446], set_id="M20", rarity="Common", collectible=True, set_number=154,
                         mtga_id=69939)
ReducetoAshes = Card(name="reduce_to_ashes", pretty_name="Reduce to Ashes", cost=['4', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[63439], set_id="M20", rarity="Common", collectible=True, set_number=155,
                     mtga_id=69940)
RepeatedReverberation = Card(name="repeated_reverberation", pretty_name="Repeated Reverberation", cost=['2', 'R', 'R'],
                             color_identity=['R'], card_type="Instant", sub_types="",
                             abilities=[133571], set_id="M20", rarity="Rare", collectible=True, set_number=156,
                             mtga_id=69941)
RipscalePredator = Card(name="ripscale_predator", pretty_name="Ripscale Predator", cost=['4', 'R', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[142], set_id="M20", rarity="Common", collectible=True, set_number=157,
                        mtga_id=69942)
ScamperingScorcher = Card(name="scampering_scorcher", pretty_name="Scampering Scorcher", cost=['3', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Elemental",
                          abilities=[133573], set_id="M20", rarity="Uncommon", collectible=True, set_number=158,
                          mtga_id=69943)
ScorchSpitter = Card(name="scorch_spitter", pretty_name="Scorch Spitter", cost=['R'],
                     color_identity=['R'], card_type="Creature", sub_types="Elemental Lizard",
                     abilities=[133447], set_id="M20", rarity="Common", collectible=True, set_number=159,
                     mtga_id=69944)
Shock = Card(name="shock", pretty_name="Shock", cost=['R'],
             color_identity=['R'], card_type="Instant", sub_types="",
             abilities=[86613], set_id="M20", rarity="Common", collectible=True, set_number=160,
             mtga_id=69945)
TectonicRift = Card(name="tectonic_rift", pretty_name="Tectonic Rift", cost=['3', 'R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[1098], set_id="M20", rarity="Common", collectible=True, set_number=161,
                    mtga_id=69946)
ThunderkinAwakener = Card(name="thunderkin_awakener", pretty_name="Thunderkin Awakener", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Elemental Shaman",
                          abilities=[9, 133448], set_id="M20", rarity="Rare", collectible=True, set_number=162,
                          mtga_id=69947)
UncagedFury = Card(name="uncaged_fury", pretty_name="Uncaged Fury", cost=['2', 'R'],
                   color_identity=['R'], card_type="Instant", sub_types="",
                   abilities=[19961], set_id="M20", rarity="Uncommon", collectible=True, set_number=163,
                   mtga_id=69948)
UnchainedBerserker = Card(name="unchained_berserker", pretty_name="Unchained Berserker", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Human Berserker",
                          abilities=[185, 133450], set_id="M20", rarity="Uncommon", collectible=True, set_number=164,
                          mtga_id=69949)
BarkhideTroll = Card(name="barkhide_troll", pretty_name="Barkhide Troll", cost=['G', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Troll",
                     abilities=[90859, 133451], set_id="M20", rarity="Uncommon", collectible=True, set_number=165,
                     mtga_id=69950)
BrightwoodTracker = Card(name="brightwood_tracker", pretty_name="Brightwood Tracker", cost=['3', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                         abilities=[133452], set_id="M20", rarity="Common", collectible=True, set_number=166,
                         mtga_id=69951)
CavalierofThorns = Card(name="cavalier_of_thorns", pretty_name="Cavalier of Thorns", cost=['2', 'G', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Elemental Knight",
                        abilities=[13, 133611, 133454], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=167,
                        mtga_id=69952)
CentaurCourser = Card(name="centaur_courser", pretty_name="Centaur Courser", cost=['2', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Centaur Warrior",
                      abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=168,
                      mtga_id=69953)
ElvishReclaimer = Card(name="elvish_reclaimer", pretty_name="Elvish Reclaimer", cost=['G'],
                       color_identity=['G'], card_type="Creature", sub_types="Elf Warrior",
                       abilities=[133455, 133456], set_id="M20", rarity="Rare", collectible=True, set_number=169,
                       mtga_id=69954)
FeralInvocation = Card(name="feral_invocation", pretty_name="Feral Invocation", cost=['2', 'G'],
                       color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                       abilities=[7, 1027, 2018], set_id="M20", rarity="Common", collectible=True, set_number=170,
                       mtga_id=69955)
FerociousPup = Card(name="ferocious_pup", pretty_name="Ferocious Pup", cost=['2', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Wolf",
                    abilities=[103216], set_id="M20", rarity="Common", collectible=True, set_number=171,
                    mtga_id=69956)
GargosViciousWatcher = Card(name="gargos_vicious_watcher", pretty_name="Gargos, Vicious Watcher", cost=['3', 'G', 'G', 'G'],
                            color_identity=['G'], card_type="Creature", sub_types="Hydra",
                            abilities=[15, 133458, 133457], set_id="M20", rarity="Rare", collectible=True, set_number=172,
                            mtga_id=69957)
GiftofParadise = Card(name="gift_of_paradise", pretty_name="Gift of Paradise", cost=['2', 'G'],
                      color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                      abilities=[1570, 1102, 61119], set_id="M20", rarity="Common", collectible=True, set_number=173,
                      mtga_id=69958)
GreenwoodSentinel = Card(name="greenwood_sentinel", pretty_name="Greenwood Sentinel", cost=['1', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                         abilities=[15], set_id="M20", rarity="Common", collectible=True, set_number=174,
                         mtga_id=69959)
GrowthCycle = Card(name="growth_cycle", pretty_name="Growth Cycle", cost=['1', 'G'],
                   color_identity=['G'], card_type="Instant", sub_types="",
                   abilities=[133478], set_id="M20", rarity="Common", collectible=True, set_number=175,
                   mtga_id=69960)
HealeroftheGlade = Card(name="healer_of_the_glade", pretty_name="Healer of the Glade", cost=['G'],
                        color_identity=['G'], card_type="Creature", sub_types="Elemental",
                        abilities=[1102], set_id="M20", rarity="Common", collectible=True, set_number=176,
                        mtga_id=69961)
HowlingGiant = Card(name="howling_giant", pretty_name="Howling Giant", cost=['5', 'G', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Giant Druid",
                    abilities=[13, 101013], set_id="M20", rarity="Uncommon", collectible=True, set_number=177,
                    mtga_id=69962)
LeafkinDruid = Card(name="leafkin_druid", pretty_name="Leafkin Druid", cost=['1', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Elemental Druid",
                    abilities=[133460], set_id="M20", rarity="Common", collectible=True, set_number=178,
                    mtga_id=69963)
LeylineofAbundance = Card(name="leyline_of_abundance", pretty_name="Leyline of Abundance", cost=['2', 'G', 'G'],
                          color_identity=['G'], card_type="Enchantment", sub_types="",
                          abilities=[91944, 133461, 133462], set_id="M20", rarity="Rare", collectible=True, set_number=179,
                          mtga_id=69964)
LoamingShaman = Card(name="loaming_shaman", pretty_name="Loaming Shaman", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Centaur Shaman",
                     abilities=[91002], set_id="M20", rarity="Uncommon", collectible=True, set_number=180,
                     mtga_id=69965)
MammothSpider = Card(name="mammoth_spider", pretty_name="Mammoth Spider", cost=['4', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Spider",
                     abilities=[13], set_id="M20", rarity="Common", collectible=True, set_number=181,
                     mtga_id=69966)
MightoftheMasses = Card(name="might_of_the_masses", pretty_name="Might of the Masses", cost=['G'],
                        color_identity=['G'], card_type="Instant", sub_types="",
                        abilities=[9094], set_id="M20", rarity="Uncommon", collectible=True, set_number=182,
                        mtga_id=69967)
NaturalEnd = Card(name="natural_end", pretty_name="Natural End", cost=['2', 'G'],
                  color_identity=['G'], card_type="Instant", sub_types="",
                  abilities=[19056], set_id="M20", rarity="Common", collectible=True, set_number=183,
                  mtga_id=69968)
NetcasterSpider = Card(name="netcaster_spider", pretty_name="Netcaster Spider", cost=['2', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Spider",
                       abilities=[13, 101422], set_id="M20", rarity="Common", collectible=True, set_number=184,
                       mtga_id=69969)
NightpackAmbusher = Card(name="nightpack_ambusher", pretty_name="Nightpack Ambusher", cost=['2', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Wolf",
                         abilities=[7, 133464, 133465], set_id="M20", rarity="Rare", collectible=True, set_number=185,
                         mtga_id=69970)
Overcome = Card(name="overcome", pretty_name="Overcome", cost=['3', 'G', 'G'],
                color_identity=['G'], card_type="Sorcery", sub_types="",
                abilities=[103828], set_id="M20", rarity="Uncommon", collectible=True, set_number=186,
                mtga_id=69971)
OvergrowthElemental = Card(name="overgrowth_elemental", pretty_name="Overgrowth Elemental", cost=['2', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Elemental",
                           abilities=[133517, 133467], set_id="M20", rarity="Uncommon", collectible=True, set_number=187,
                           mtga_id=69972)
Plummet = Card(name="plummet", pretty_name="Plummet", cost=['1', 'G'],
               color_identity=['G'], card_type="Instant", sub_types="",
               abilities=[29759], set_id="M20", rarity="Common", collectible=True, set_number=188,
               mtga_id=69973)
PulseofMurasa = Card(name="pulse_of_murasa", pretty_name="Pulse of Murasa", cost=['2', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[102721], set_id="M20", rarity="Uncommon", collectible=True, set_number=189,
                     mtga_id=69974)
RabidBite = Card(name="rabid_bite", pretty_name="Rabid Bite", cost=['1', 'G'],
                 color_identity=['G'], card_type="Sorcery", sub_types="",
                 abilities=[61234], set_id="M20", rarity="Common", collectible=True, set_number=190,
                 mtga_id=69975)
SeasonofGrowth = Card(name="season_of_growth", pretty_name="Season of Growth", cost=['1', 'G'],
                      color_identity=['G'], card_type="Enchantment", sub_types="",
                      abilities=[133468, 133544], set_id="M20", rarity="Uncommon", collectible=True, set_number=191,
                      mtga_id=69976)
SedgeScorpion = Card(name="sedge_scorpion", pretty_name="Sedge Scorpion", cost=['G'],
                     color_identity=['G'], card_type="Creature", sub_types="Scorpion",
                     abilities=[1], set_id="M20", rarity="Common", collectible=True, set_number=192,
                     mtga_id=69977)
SharedSummons = Card(name="shared_summons", pretty_name="Shared Summons", cost=['3', 'G', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[133469], set_id="M20", rarity="Rare", collectible=True, set_number=193,
                     mtga_id=69978)
ShiftingCeratops = Card(name="shifting_ceratops", pretty_name="Shifting Ceratops", cost=['2', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[120287, 186, 133470], set_id="M20", rarity="Rare", collectible=True, set_number=194,
                        mtga_id=69979)
SilverbackShaman = Card(name="silverback_shaman", pretty_name="Silverback Shaman", cost=['3', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Ape Shaman",
                        abilities=[14, 17519], set_id="M20", rarity="Common", collectible=True, set_number=195,
                        mtga_id=69980)
ThicketCrasher = Card(name="thicket_crasher", pretty_name="Thicket Crasher", cost=['3', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Elemental Rhino",
                      abilities=[14, 133471], set_id="M20", rarity="Common", collectible=True, set_number=196,
                      mtga_id=69981)
ThrashingBrontodon = Card(name="thrashing_brontodon", pretty_name="Thrashing Brontodon", cost=['1', 'G', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                          abilities=[89285], set_id="M20", rarity="Uncommon", collectible=True, set_number=197,
                          mtga_id=69982)
VeilofSummer = Card(name="veil_of_summer", pretty_name="Veil of Summer", cost=['G'],
                    color_identity=['G'], card_type="Instant", sub_types="",
                    abilities=[133473], set_id="M20", rarity="Uncommon", collectible=True, set_number=198,
                    mtga_id=69983)
VivienArkbowRanger = Card(name="vivien_arkbow_ranger", pretty_name="Vivien, Arkbow Ranger", cost=['1', 'G', 'G', 'G'],
                          color_identity=['G'], card_type="Planeswalker", sub_types="Vivien",
                          abilities=[133474, 133475, 133476], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=199,
                          mtga_id=69984)
VoraciousHydra = Card(name="voracious_hydra", pretty_name="Voracious Hydra", cost=['X', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Hydra",
                      abilities=[14, 76885, 133559], set_id="M20", rarity="Rare", collectible=True, set_number=200,
                      mtga_id=69985)
Vorstclaw = Card(name="vorstclaw", pretty_name="Vorstclaw", cost=['4', 'G', 'G'],
                 color_identity=['G'], card_type="Creature", sub_types="Elemental Horror",
                 abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=201,
                 mtga_id=69986)
WakerootElemental = Card(name="wakeroot_elemental", pretty_name="Wakeroot Elemental", cost=['4', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elemental",
                         abilities=[133479], set_id="M20", rarity="Rare", collectible=True, set_number=202,
                         mtga_id=69987)
WolfkinBond = Card(name="wolfkin_bond", pretty_name="Wolfkin Bond", cost=['4', 'G'],
                   color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                   abilities=[1027, 103216, 2018], set_id="M20", rarity="Common", collectible=True, set_number=203,
                   mtga_id=69988)
WolfridersSaddle = Card(name="wolfriders_saddle", pretty_name="Wolfrider's Saddle", cost=['3', 'G'],
                        color_identity=['G'], card_type="Artifact", sub_types="Equipment",
                        abilities=[133480, 133481, 1156], set_id="M20", rarity="Uncommon", collectible=True, set_number=204,
                        mtga_id=69989)
WoodlandChampion = Card(name="woodland_champion", pretty_name="Woodland Champion", cost=['1', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                        abilities=[133563], set_id="M20", rarity="Uncommon", collectible=True, set_number=205,
                        mtga_id=69990)
CorpseKnight = Card(name="corpse_knight", pretty_name="Corpse Knight", cost=['W', 'B'],
                    color_identity=['W', 'B'], card_type="Creature", sub_types="Zombie Knight",
                    abilities=[133484], set_id="M20", rarity="Uncommon", collectible=True, set_number=206,
                    mtga_id=69991)
CreepingTrailblazer = Card(name="creeping_trailblazer", pretty_name="Creeping Trailblazer", cost=['R', 'G'],
                           color_identity=['R', 'G'], card_type="Creature", sub_types="Elemental",
                           abilities=[133485, 133486], set_id="M20", rarity="Uncommon", collectible=True, set_number=207,
                           mtga_id=69992)
EmpyreanEagle = Card(name="empyrean_eagle", pretty_name="Empyrean Eagle", cost=['1', 'W', 'U'],
                     color_identity=['W', 'U'], card_type="Creature", sub_types="Bird Spirit",
                     abilities=[8, 62106], set_id="M20", rarity="Uncommon", collectible=True, set_number=208,
                     mtga_id=69993)
IronrootWarlord = Card(name="ironroot_warlord", pretty_name="Ironroot Warlord", cost=['1', 'G', 'W'],
                       color_identity=['G', 'W'], card_type="Creature", sub_types="Treefolk Soldier",
                       abilities=[17477, 133487], set_id="M20", rarity="Uncommon", collectible=True, set_number=209,
                       mtga_id=69994)
KaaliaZenithSeeker = Card(name="kaalia_zenith_seeker", pretty_name="Kaalia, Zenith Seeker", cost=['R', 'W', 'B'],
                          color_identity=['W', 'B', 'R'], card_type="Creature", sub_types="Human Cleric",
                          abilities=[8, 15, 133488], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=210,
                          mtga_id=69995)
KethistheHiddenHand = Card(name="kethis_the_hidden_hand", pretty_name="Kethis, the Hidden Hand", cost=['W', 'B', 'G'],
                           color_identity=['W', 'B', 'G'], card_type="Creature", sub_types="Elf Advisor",
                           abilities=[133489, 133491], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=211,
                           mtga_id=69996)
KykarWindsFury = Card(name="kykar_winds_fury", pretty_name="Kykar, Wind's Fury", cost=['1', 'U', 'R', 'W'],
                      color_identity=['W', 'U', 'R'], card_type="Creature", sub_types="Bird Wizard",
                      abilities=[8, 133570, 133493], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=212,
                      mtga_id=69997)
LightningStormkin = Card(name="lightning_stormkin", pretty_name="Lightning Stormkin", cost=['U', 'R'],
                         color_identity=['U', 'R'], card_type="Creature", sub_types="Elemental Wizard",
                         abilities=[8, 9], set_id="M20", rarity="Uncommon", collectible=True, set_number=213,
                         mtga_id=69998)
MoldervineReclamation = Card(name="moldervine_reclamation", pretty_name="Moldervine Reclamation", cost=['3', 'B', 'G'],
                             color_identity=['B', 'G'], card_type="Enchantment", sub_types="",
                             abilities=[133494], set_id="M20", rarity="Uncommon", collectible=True, set_number=214,
                             mtga_id=69999)
OgreSiegebreaker = Card(name="ogre_siegebreaker", pretty_name="Ogre Siegebreaker", cost=['2', 'B', 'R'],
                        color_identity=['B', 'R'], card_type="Creature", sub_types="Ogre Berserker",
                        abilities=[133495], set_id="M20", rarity="Uncommon", collectible=True, set_number=215,
                        mtga_id=70000)
OmnathLocusoftheRoil = Card(name="omnath_locus_of_the_roil", pretty_name="Omnath, Locus of the Roil", cost=['1', 'G', 'U', 'R'],
                            color_identity=['U', 'R', 'G'], card_type="Creature", sub_types="Elemental",
                            abilities=[133496, 133497], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=216,
                            mtga_id=70001)
RisenReef = Card(name="risen_reef", pretty_name="Risen Reef", cost=['1', 'G', 'U'],
                 color_identity=['G', 'U'], card_type="Creature", sub_types="Elemental",
                 abilities=[133604], set_id="M20", rarity="Uncommon", collectible=True, set_number=217,
                 mtga_id=70002)
SkyknightVanguard = Card(name="skyknight_vanguard", pretty_name="Skyknight Vanguard", cost=['R', 'W'],
                         color_identity=['R', 'W'], card_type="Creature", sub_types="Human Knight",
                         abilities=[8, 133499], set_id="M20", rarity="Uncommon", collectible=True, set_number=218,
                         mtga_id=70003)
TomeboundLich = Card(name="tomebound_lich", pretty_name="Tomebound Lich", cost=['1', 'U', 'B'],
                     color_identity=['U', 'B'], card_type="Creature", sub_types="Zombie Wizard",
                     abilities=[1, 12, 133577], set_id="M20", rarity="Uncommon", collectible=True, set_number=219,
                     mtga_id=70004)
YaroktheDesecrated = Card(name="yarok_the_desecrated", pretty_name="Yarok, the Desecrated", cost=['2', 'B', 'G', 'U'],
                          color_identity=['U', 'B', 'G'], card_type="Creature", sub_types="Elemental Horror",
                          abilities=[1, 12, 133500], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=220,
                          mtga_id=70005)
AnvilwroughtRaptor = Card(name="anvilwrought_raptor", pretty_name="Anvilwrought Raptor", cost=['4'],
                          color_identity=[], card_type="Artifact Creature", sub_types="Bird",
                          abilities=[8, 6], set_id="M20", rarity="Common", collectible=True, set_number=221,
                          mtga_id=70006)
BagofHolding = Card(name="bag_of_holding", pretty_name="Bag of Holding", cost=['1'],
                    color_identity=[], card_type="Artifact", sub_types="",
                    abilities=[6347, 1633, 133581], set_id="M20", rarity="Rare", collectible=True, set_number=222,
                    mtga_id=70007)
ColossusHammer = Card(name="colossus_hammer", pretty_name="Colossus Hammer", cost=['1'],
                      color_identity=[], card_type="Artifact", sub_types="Equipment",
                      abilities=[133501, 133502], set_id="M20", rarity="Uncommon", collectible=True, set_number=223,
                      mtga_id=70008)
DiamondKnight = Card(name="diamond_knight", pretty_name="Diamond Knight", cost=['3'],
                     color_identity=[], card_type="Artifact Creature", sub_types="Knight",
                     abilities=[15, 88237, 133503], set_id="M20", rarity="Uncommon", collectible=True, set_number=224,
                     mtga_id=70009)
DivinersLockbox = Card(name="diviners_lockbox", pretty_name="Diviner's Lockbox", cost=['4'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[133504], set_id="M20", rarity="Uncommon", collectible=True, set_number=225,
                       mtga_id=70010)
GolosTirelessPilgrim = Card(name="golos_tireless_pilgrim", pretty_name="Golos, Tireless Pilgrim", cost=['5'],
                            color_identity=['W', 'U', 'B', 'R', 'G'], card_type="Artifact Creature", sub_types="Scout",
                            abilities=[133586, 133587], set_id="M20", rarity="Rare", collectible=True, set_number=226,
                            mtga_id=70011)
GrafdiggersCage = Card(name="grafdiggers_cage", pretty_name="Grafdigger's Cage", cost=['1'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[99659, 113332], set_id="M20", rarity="Rare", collectible=True, set_number=227,
                       mtga_id=70012)
HeartPiercerBow = Card(name="heartpiercer_bow", pretty_name="Heart-Piercer Bow", cost=['2'],
                       color_identity=[], card_type="Artifact", sub_types="Equipment",
                       abilities=[101658, 1268], set_id="M20", rarity="Common", collectible=True, set_number=228,
                       mtga_id=70013)
IconofAncestry = Card(name="icon_of_ancestry", pretty_name="Icon of Ancestry", cost=['3'],
                      color_identity=[], card_type="Artifact", sub_types="",
                      abilities=[76882, 116805, 133506], set_id="M20", rarity="Rare", collectible=True, set_number=229,
                      mtga_id=70014)
ManifoldKey = Card(name="manifold_key", pretty_name="Manifold Key", cost=['1'],
                   color_identity=[], card_type="Artifact", sub_types="",
                   abilities=[133589, 119144], set_id="M20", rarity="Uncommon", collectible=True, set_number=230,
                   mtga_id=70015)
MaraudersAxe = Card(name="marauders_axe", pretty_name="Marauder's Axe", cost=['2'],
                    color_identity=[], card_type="Artifact", sub_types="Equipment",
                    abilities=[4712, 1319], set_id="M20", rarity="Common", collectible=True, set_number=231,
                    mtga_id=70016)
MeteorGolem = Card(name="meteor_golem", pretty_name="Meteor Golem", cost=['7'],
                   color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                   abilities=[119141], set_id="M20", rarity="Uncommon", collectible=True, set_number=232,
                   mtga_id=70017)
MysticForge = Card(name="mystic_forge", pretty_name="Mystic Forge", cost=['4'],
                   color_identity=[], card_type="Artifact", sub_types="",
                   abilities=[14523, 133507, 133591], set_id="M20", rarity="Rare", collectible=True, set_number=233,
                   mtga_id=70018)
PatternMatcher = Card(name="pattern_matcher", pretty_name="Pattern Matcher", cost=['4'],
                      color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                      abilities=[133508], set_id="M20", rarity="Uncommon", collectible=True, set_number=234,
                      mtga_id=70019)
Prismite = Card(name="prismite", pretty_name="Prismite", cost=['2'],
                color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                abilities=[133176], set_id="M20", rarity="Common", collectible=True, set_number=235,
                mtga_id=70020)
RetributiveWand = Card(name="retributive_wand", pretty_name="Retributive Wand", cost=['3'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[88153, 133594], set_id="M20", rarity="Uncommon", collectible=True, set_number=236,
                       mtga_id=70021)
SalvagerofRuin = Card(name="salvager_of_ruin", pretty_name="Salvager of Ruin", cost=['3'],
                      color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                      abilities=[133510], set_id="M20", rarity="Uncommon", collectible=True, set_number=237,
                      mtga_id=70022)
Scuttlemutt = Card(name="scuttlemutt", pretty_name="Scuttlemutt", cost=['3'],
                   color_identity=[], card_type="Artifact Creature", sub_types="Scarecrow",
                   abilities=[1055, 17871], set_id="M20", rarity="Uncommon", collectible=True, set_number=238,
                   mtga_id=70023)
SteelOverseer = Card(name="steel_overseer", pretty_name="Steel Overseer", cost=['2'],
                     color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                     abilities=[9082], set_id="M20", rarity="Rare", collectible=True, set_number=239,
                     mtga_id=70024)
StoneGolem = Card(name="stone_golem", pretty_name="Stone Golem", cost=['5'],
                  color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                  abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=240,
                  mtga_id=70025)
VialofDragonfire = Card(name="vial_of_dragonfire", pretty_name="Vial of Dragonfire", cost=['2'],
                        color_identity=[], card_type="Artifact", sub_types="",
                        abilities=[102173], set_id="M20", rarity="Common", collectible=True, set_number=241,
                        mtga_id=70026)
BloodfellCaves = Card(name="bloodfell_caves", pretty_name="Bloodfell Caves", cost=[],
                      color_identity=['B', 'R'], card_type="Land", sub_types="",
                      abilities=[76735, 90050, 1211], set_id="M20", rarity="Common", collectible=True, set_number=242,
                      mtga_id=70027)
BlossomingSands = Card(name="blossoming_sands", pretty_name="Blossoming Sands", cost=[],
                       color_identity=['G', 'W'], card_type="Land", sub_types="",
                       abilities=[76735, 90050, 1203], set_id="M20", rarity="Common", collectible=True, set_number=243,
                       mtga_id=70028)
CrypticCaves = Card(name="cryptic_caves", pretty_name="Cryptic Caves", cost=[],
                    color_identity=[], card_type="Land", sub_types="",
                    abilities=[1152, 133512], set_id="M20", rarity="Uncommon", collectible=True, set_number=244,
                    mtga_id=70029)
DismalBackwater = Card(name="dismal_backwater", pretty_name="Dismal Backwater", cost=[],
                       color_identity=['U', 'B'], card_type="Land", sub_types="",
                       abilities=[76735, 90050, 1167], set_id="M20", rarity="Common", collectible=True, set_number=245,
                       mtga_id=70030)
EvolvingWilds = Card(name="evolving_wilds", pretty_name="Evolving Wilds", cost=[],
                     color_identity=[], card_type="Land", sub_types="",
                     abilities=[88024], set_id="M20", rarity="Common", collectible=True, set_number=246,
                     mtga_id=70031)
FieldoftheDead = Card(name="field_of_the_dead", pretty_name="Field of the Dead", cost=[],
                      color_identity=[], card_type="Land", sub_types="",
                      abilities=[76735, 1152, 133514], set_id="M20", rarity="Rare", collectible=True, set_number=247,
                      mtga_id=70032)
JungleHollow = Card(name="jungle_hollow", pretty_name="Jungle Hollow", cost=[],
                    color_identity=['B', 'G'], card_type="Land", sub_types="",
                    abilities=[76735, 90050, 4407], set_id="M20", rarity="Common", collectible=True, set_number=248,
                    mtga_id=70033)
LotusField = Card(name="lotus_field", pretty_name="Lotus Field", cost=[],
                  color_identity=[], card_type="Land", sub_types="",
                  abilities=[10, 76735, 133515, 4957], set_id="M20", rarity="Rare", collectible=True, set_number=249,
                  mtga_id=70034)
RuggedHighlands = Card(name="rugged_highlands", pretty_name="Rugged Highlands", cost=[],
                       color_identity=['R', 'G'], card_type="Land", sub_types="",
                       abilities=[76735, 90050, 1131], set_id="M20", rarity="Common", collectible=True, set_number=250,
                       mtga_id=70035)
ScouredBarrens = Card(name="scoured_barrens", pretty_name="Scoured Barrens", cost=[],
                      color_identity=['W', 'B'], card_type="Land", sub_types="",
                      abilities=[76735, 90050, 18472], set_id="M20", rarity="Common", collectible=True, set_number=251,
                      mtga_id=70036)
SwiftwaterCliffs = Card(name="swiftwater_cliffs", pretty_name="Swiftwater Cliffs", cost=[],
                        color_identity=['U', 'R'], card_type="Land", sub_types="",
                        abilities=[76735, 90050, 1039], set_id="M20", rarity="Common", collectible=True, set_number=252,
                        mtga_id=70037)
TempleofEpiphany = Card(name="temple_of_epiphany", pretty_name="Temple of Epiphany", cost=[],
                        color_identity=['U', 'R'], card_type="Land", sub_types="",
                        abilities=[76735, 91717, 1039], set_id="M20", rarity="Rare", collectible=True, set_number=253,
                        mtga_id=70038)
TempleofMalady = Card(name="temple_of_malady", pretty_name="Temple of Malady", cost=[],
                      color_identity=['B', 'G'], card_type="Land", sub_types="",
                      abilities=[76735, 91717, 4407], set_id="M20", rarity="Rare", collectible=True, set_number=254,
                      mtga_id=70039)
TempleofMystery = Card(name="temple_of_mystery", pretty_name="Temple of Mystery", cost=[],
                       color_identity=['G', 'U'], card_type="Land", sub_types="",
                       abilities=[76735, 91717, 18504], set_id="M20", rarity="Rare", collectible=True, set_number=255,
                       mtga_id=70040)
TempleofSilence = Card(name="temple_of_silence", pretty_name="Temple of Silence", cost=[],
                       color_identity=['W', 'B'], card_type="Land", sub_types="",
                       abilities=[76735, 91717, 18472], set_id="M20", rarity="Rare", collectible=True, set_number=256,
                       mtga_id=70041)
TempleofTriumph = Card(name="temple_of_triumph", pretty_name="Temple of Triumph", cost=[],
                       color_identity=['R', 'W'], card_type="Land", sub_types="",
                       abilities=[76735, 91717, 4247], set_id="M20", rarity="Rare", collectible=True, set_number=257,
                       mtga_id=70042)
ThornwoodFalls = Card(name="thornwood_falls", pretty_name="Thornwood Falls", cost=[],
                      color_identity=['G', 'U'], card_type="Land", sub_types="",
                      abilities=[76735, 90050, 18504], set_id="M20", rarity="Common", collectible=True, set_number=258,
                      mtga_id=70043)
TranquilCove = Card(name="tranquil_cove", pretty_name="Tranquil Cove", cost=[],
                    color_identity=['W', 'U'], card_type="Land", sub_types="",
                    abilities=[76735, 90050, 1209], set_id="M20", rarity="Common", collectible=True, set_number=259,
                    mtga_id=70044)
WindScarredCrag = Card(name="windscarred_crag", pretty_name="Wind-Scarred Crag", cost=[],
                       color_identity=['R', 'W'], card_type="Land", sub_types="",
                       abilities=[76735, 90050, 4247], set_id="M20", rarity="Common", collectible=True, set_number=260,
                       mtga_id=70045)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=261,
              mtga_id=70046)
Plains2 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=262,
               mtga_id=70047)
Plains3 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=263,
               mtga_id=70048)
Plains4 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=264,
               mtga_id=70049)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=265,
              mtga_id=70050)
Island2 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=266,
               mtga_id=70051)
Island3 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=267,
               mtga_id=70052)
Island4 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=268,
               mtga_id=70053)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=269,
             mtga_id=70054)
Swamp2 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=270,
              mtga_id=70055)
Swamp3 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=271,
              mtga_id=70056)
Swamp4 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=272,
              mtga_id=70057)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=273,
                mtga_id=70058)
Mountain2 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=274,
                 mtga_id=70059)
Mountain3 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=275,
                 mtga_id=70060)
Mountain4 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=276,
                 mtga_id=70061)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=277,
              mtga_id=70062)
Forest2 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=278,
               mtga_id=70063)
Forest3 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=279,
               mtga_id=70064)
Forest4 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="M20", rarity="Basic", collectible=True, set_number=280,
               mtga_id=70065)
AjaniInspiringLeader = Card(name="ajani_inspiring_leader", pretty_name="Ajani, Inspiring Leader", cost=['4', 'W', 'W'],
                            color_identity=['W'], card_type="Planeswalker", sub_types="Ajani",
                            abilities=[133518, 133519, 133520], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=282,
                            mtga_id=70066)
GoldmaneGriffin = Card(name="goldmane_griffin", pretty_name="Goldmane Griffin", cost=['3', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Griffin",
                       abilities=[8, 15, 135533], set_id="M20", rarity="Rare", collectible=True, set_number=283,
                       mtga_id=70067)
SavannahSage = Card(name="savannah_sage", pretty_name="Savannah Sage", cost=['1', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Cat Cleric",
                    abilities=[88132], set_id="M20", rarity="Common", collectible=True, set_number=284,
                    mtga_id=70068)
TwinbladePaladin = Card(name="twinblade_paladin", pretty_name="Twinblade Paladin", cost=['3', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                        abilities=[92970, 133615], set_id="M20", rarity="Uncommon", collectible=True, set_number=285,
                        mtga_id=70069)
MuYanlingCelestialWind = Card(name="mu_yanling_celestial_wind", pretty_name="Mu Yanling, Celestial Wind", cost=['4', 'U', 'U'],
                              color_identity=['U'], card_type="Planeswalker", sub_types="Yanling",
                              abilities=[133523, 133524, 133525], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=286,
                              mtga_id=70070)
CelestialMessenger = Card(name="celestial_messenger", pretty_name="Celestial Messenger", cost=['2', 'U', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Bird Spirit",
                          abilities=[7, 8, 133526], set_id="M20", rarity="Common", collectible=True, set_number=287,
                          mtga_id=70071)
WaterkinShaman = Card(name="waterkin_shaman", pretty_name="Waterkin Shaman", cost=['1', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Elemental Shaman",
                      abilities=[133527], set_id="M20", rarity="Uncommon", collectible=True, set_number=288,
                      mtga_id=70072)
YanlingsHarbinger = Card(name="yanlings_harbinger", pretty_name="Yanling's Harbinger", cost=['3', 'U', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Bird",
                         abilities=[8, 135540], set_id="M20", rarity="Rare", collectible=True, set_number=289,
                         mtga_id=70073)
SorinVampireLord = Card(name="sorin_vampire_lord", pretty_name="Sorin, Vampire Lord", cost=['4', 'B', 'B'],
                        color_identity=['B'], card_type="Planeswalker", sub_types="Sorin",
                        abilities=[133528, 133529, 133531], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=290,
                        mtga_id=70074)
SavageGorger = Card(name="savage_gorger", pretty_name="Savage Gorger", cost=['1', 'B', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Vampire",
                    abilities=[8, 133532], set_id="M20", rarity="Common", collectible=True, set_number=291,
                    mtga_id=70075)
SorinsGuide = Card(name="sorins_guide", pretty_name="Sorin's Guide", cost=['3', 'B', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Vampire",
                   abilities=[135546], set_id="M20", rarity="Rare", collectible=True, set_number=292,
                   mtga_id=70076)
ThirstingBloodlord = Card(name="thirsting_bloodlord", pretty_name="Thirsting Bloodlord", cost=['2', 'B', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Vampire",
                          abilities=[117100], set_id="M20", rarity="Uncommon", collectible=True, set_number=293,
                          mtga_id=70077)
ChandraFlamesFury = Card(name="chandra_flames_fury", pretty_name="Chandra, Flame's Fury", cost=['4', 'R', 'R'],
                         color_identity=['R'], card_type="Planeswalker", sub_types="Chandra",
                         abilities=[133534, 133535, 133536], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=294,
                         mtga_id=70078)
ChandrasFlameWave = Card(name="chandras_flame_wave", pretty_name="Chandra's Flame Wave", cost=['3', 'R', 'R'],
                         color_identity=['R'], card_type="Sorcery", sub_types="",
                         abilities=[135550], set_id="M20", rarity="Rare", collectible=True, set_number=295,
                         mtga_id=70079)
PyroclasticElemental = Card(name="pyroclastic_elemental", pretty_name="Pyroclastic Elemental", cost=['3', 'R', 'R'],
                            color_identity=['R'], card_type="Creature", sub_types="Elemental",
                            abilities=[133566], set_id="M20", rarity="Uncommon", collectible=True, set_number=296,
                            mtga_id=70080)
WildfireElemental = Card(name="wildfire_elemental", pretty_name="Wildfire Elemental", cost=['2', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Elemental",
                         abilities=[133538], set_id="M20", rarity="Common", collectible=True, set_number=297,
                         mtga_id=70081)
VivienNaturesAvenger = Card(name="vivien_natures_avenger", pretty_name="Vivien, Nature's Avenger", cost=['4', 'G', 'G'],
                            color_identity=['G'], card_type="Planeswalker", sub_types="Vivien",
                            abilities=[133915, 133541, 133542], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=298,
                            mtga_id=70082)
EtherealElk = Card(name="ethereal_elk", pretty_name="Ethereal Elk", cost=['3', 'G', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Elk Spirit",
                   abilities=[14, 135556], set_id="M20", rarity="Rare", collectible=True, set_number=299,
                   mtga_id=70083)
GnarlbackRhino = Card(name="gnarlback_rhino", pretty_name="Gnarlback Rhino", cost=['2', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Rhino",
                      abilities=[14, 133543], set_id="M20", rarity="Uncommon", collectible=True, set_number=300,
                      mtga_id=70084)
ViviensCrocodile = Card(name="viviens_crocodile", pretty_name="Vivien's Crocodile", cost=['2', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Crocodile Spirit",
                        abilities=[133578], set_id="M20", rarity="Common", collectible=True, set_number=301,
                        mtga_id=70085)
AngelicGuardian = Card(name="angelic_guardian", pretty_name="Angelic Guardian", cost=['4', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Angel",
                       abilities=[8, 121333], set_id="M20", rarity="Rare", collectible=True, set_number=302,
                       mtga_id=70086)
BastionEnforcer = Card(name="bastion_enforcer", pretty_name="Bastion Enforcer", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Dwarf Soldier",
                       abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=303,
                       mtga_id=70087)
ConcordiaPegasus = Card(name="concordia_pegasus", pretty_name="Concordia Pegasus", cost=['1', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Pegasus",
                        abilities=[8], set_id="M20", rarity="Common", collectible=True, set_number=304,
                        mtga_id=70088)
HaazdaOfficer = Card(name="haazda_officer", pretty_name="Haazda Officer", cost=['2', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                     abilities=[103263], set_id="M20", rarity="Common", collectible=True, set_number=305,
                     mtga_id=70089)
ImpassionedOrator = Card(name="impassioned_orator", pretty_name="Impassioned Orator", cost=['1', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                         abilities=[122104], set_id="M20", rarity="Common", collectible=True, set_number=306,
                         mtga_id=70090)
ImperialOutrider = Card(name="imperial_outrider", pretty_name="Imperial Outrider", cost=['3', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                        abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=307,
                        mtga_id=70091)
IroncladKrovod = Card(name="ironclad_krovod", pretty_name="Ironclad Krovod", cost=['3', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Beast",
                      abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=308,
                      mtga_id=70092)
ProwlingCaracal = Card(name="prowling_caracal", pretty_name="Prowling Caracal", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Cat",
                       abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=309,
                       mtga_id=70093)
SerrasGuardian = Card(name="serras_guardian", pretty_name="Serra's Guardian", cost=['4', 'W', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Angel",
                      abilities=[8, 15, 20486], set_id="M20", rarity="Rare", collectible=True, set_number=310,
                      mtga_id=70094)
ShowofValor = Card(name="show_of_valor", pretty_name="Show of Valor", cost=['1', 'W'],
                   color_identity=['W'], card_type="Instant", sub_types="",
                   abilities=[19173], set_id="M20", rarity="Common", collectible=True, set_number=311,
                   mtga_id=70095)
SiegeMastodon = Card(name="siege_mastodon", pretty_name="Siege Mastodon", cost=['4', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Elephant",
                     abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=312,
                     mtga_id=70096)
TakeVengeance = Card(name="take_vengeance", pretty_name="Take Vengeance", cost=['1', 'W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[1385], set_id="M20", rarity="Common", collectible=True, set_number=313,
                     mtga_id=70097)
TrustedPegasus = Card(name="trusted_pegasus", pretty_name="Trusted Pegasus", cost=['2', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Pegasus",
                      abilities=[8, 121386], set_id="M20", rarity="Common", collectible=True, set_number=314,
                      mtga_id=70098)
CoralMerfolk = Card(name="coral_merfolk", pretty_name="Coral Merfolk", cost=['1', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Merfolk",
                    abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=315,
                    mtga_id=70099)
PhantomWarrior = Card(name="phantom_warrior", pretty_name="Phantom Warrior", cost=['1', 'U', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Illusion Warrior",
                      abilities=[62969], set_id="M20", rarity="Common", collectible=True, set_number=316,
                      mtga_id=70100)
RiddlemasterSphinx = Card(name="riddlemaster_sphinx", pretty_name="Riddlemaster Sphinx", cost=['4', 'U', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                          abilities=[8, 119222], set_id="M20", rarity="Rare", collectible=True, set_number=317,
                          mtga_id=70101)
SnappingDrake = Card(name="snapping_drake", pretty_name="Snapping Drake", cost=['3', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Drake",
                     abilities=[8], set_id="M20", rarity="Common", collectible=True, set_number=318,
                     mtga_id=70102)
BartizanBats = Card(name="bartizan_bats", pretty_name="Bartizan Bats", cost=['3', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Bat",
                    abilities=[8], set_id="M20", rarity="Common", collectible=True, set_number=319,
                    mtga_id=70103)
Bogstomper = Card(name="bogstomper", pretty_name="Bogstomper", cost=['4', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Beast",
                  abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=320,
                  mtga_id=70104)
DarkRemedy = Card(name="dark_remedy", pretty_name="Dark Remedy", cost=['1', 'B'],
                  color_identity=['B'], card_type="Instant", sub_types="",
                  abilities=[133585], set_id="M20", rarity="Common", collectible=True, set_number=321,
                  mtga_id=70105)
Disentomb = Card(name="disentomb", pretty_name="Disentomb", cost=['B'],
                 color_identity=['B'], card_type="Sorcery", sub_types="",
                 abilities=[24122], set_id="M20", rarity="Common", collectible=True, set_number=322,
                 mtga_id=70106)
Gravewaker = Card(name="gravewaker", pretty_name="Gravewaker", cost=['4', 'B', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Bird Spirit",
                  abilities=[8, 119163], set_id="M20", rarity="Rare", collectible=True, set_number=323,
                  mtga_id=70107)
SkeletonArcher = Card(name="skeleton_archer", pretty_name="Skeleton Archer", cost=['3', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Skeleton Archer",
                      abilities=[92894], set_id="M20", rarity="Common", collectible=True, set_number=324,
                      mtga_id=70108)
SorinsThirst = Card(name="sorins_thirst", pretty_name="Sorin's Thirst", cost=['B', 'B'],
                    color_identity=['B'], card_type="Instant", sub_types="",
                    abilities=[86929], set_id="M20", rarity="Common", collectible=True, set_number=325,
                    mtga_id=70109)
VampireOpportunist = Card(name="vampire_opportunist", pretty_name="Vampire Opportunist", cost=['1', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Vampire",
                          abilities=[133264], set_id="M20", rarity="Common", collectible=True, set_number=326,
                          mtga_id=70110)
WalkingCorpse = Card(name="walking_corpse", pretty_name="Walking Corpse", cost=['1', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Zombie",
                     abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=327,
                     mtga_id=70111)
EngulfingEruption = Card(name="engulfing_eruption", pretty_name="Engulfing Eruption", cost=['2', 'R', 'R'],
                         color_identity=['R'], card_type="Sorcery", sub_types="",
                         abilities=[13250], set_id="M20", rarity="Common", collectible=True, set_number=328,
                         mtga_id=70112)
FearlessHalberdier = Card(name="fearless_halberdier", pretty_name="Fearless Halberdier", cost=['2', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                          abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=329,
                          mtga_id=70113)
GoblinAssailant = Card(name="goblin_assailant", pretty_name="Goblin Assailant", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                       abilities=[], set_id="M20", rarity="Common", collectible=True, set_number=330,
                       mtga_id=70114)
HostileMinotaur = Card(name="hostile_minotaur", pretty_name="Hostile Minotaur", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Minotaur",
                       abilities=[9], set_id="M20", rarity="Common", collectible=True, set_number=331,
                       mtga_id=70115)
ImmortalPhoenix = Card(name="immortal_phoenix", pretty_name="Immortal Phoenix", cost=['4', 'R', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Phoenix",
                       abilities=[8, 98465], set_id="M20", rarity="Rare", collectible=True, set_number=332,
                       mtga_id=70116)
NimbleBirdsticker = Card(name="nimble_birdsticker", pretty_name="Nimble Birdsticker", cost=['2', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin",
                         abilities=[13], set_id="M20", rarity="Common", collectible=True, set_number=333,
                         mtga_id=70117)
RubblebeltRecluse = Card(name="rubblebelt_recluse", pretty_name="Rubblebelt Recluse", cost=['4', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Ogre Berserker",
                         abilities=[76824], set_id="M20", rarity="Common", collectible=True, set_number=334,
                         mtga_id=70118)
ShivanDragon = Card(name="shivan_dragon", pretty_name="Shivan Dragon", cost=['4', 'R', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Dragon",
                    abilities=[8, 1097], set_id="M20", rarity="Rare", collectible=True, set_number=335,
                    mtga_id=70119)
VolcanicDragon = Card(name="volcanic_dragon", pretty_name="Volcanic Dragon", cost=['4', 'R', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Dragon",
                      abilities=[8, 9], set_id="M20", rarity="Uncommon", collectible=True, set_number=336,
                      mtga_id=70120)
AggressiveMammoth = Card(name="aggressive_mammoth", pretty_name="Aggressive Mammoth", cost=['3', 'G', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elephant",
                         abilities=[14, 20623], set_id="M20", rarity="Rare", collectible=True, set_number=337,
                         mtga_id=70121)
BristlingBoar = Card(name="bristling_boar", pretty_name="Bristling Boar", cost=['3', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Boar",
                     abilities=[1026], set_id="M20", rarity="Common", collectible=True, set_number=338,
                     mtga_id=70122)
CanopySpider = Card(name="canopy_spider", pretty_name="Canopy Spider", cost=['1', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Spider",
                    abilities=[13], set_id="M20", rarity="Common", collectible=True, set_number=339,
                    mtga_id=70123)
FrilledSandwalla = Card(name="frilled_sandwalla", pretty_name="Frilled Sandwalla", cost=['G'],
                        color_identity=['G'], card_type="Creature", sub_types="Lizard",
                        abilities=[2347], set_id="M20", rarity="Common", collectible=True, set_number=340,
                        mtga_id=70124)
Oakenform = Card(name="oakenform", pretty_name="Oakenform", cost=['2', 'G'],
                 color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                 abilities=[1027, 1318], set_id="M20", rarity="Common", collectible=True, set_number=341,
                 mtga_id=70125)
PrizedUnicorn = Card(name="prized_unicorn", pretty_name="Prized Unicorn", cost=['3', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Unicorn",
                     abilities=[88808], set_id="M20", rarity="Common", collectible=True, set_number=342,
                     mtga_id=70126)
TitanicGrowth = Card(name="titanic_growth", pretty_name="Titanic Growth", cost=['1', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[1031], set_id="M20", rarity="Common", collectible=True, set_number=343,
                     mtga_id=70127)
WoodlandMystic = Card(name="woodland_mystic", pretty_name="Woodland Mystic", cost=['1', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                      abilities=[1005], set_id="M20", rarity="Common", collectible=True, set_number=344,
                      mtga_id=70128)
AjanisPridemate = Card(name="ajanis_pridemate", pretty_name="Ajani's Pridemate", cost=[],
                       color_identity=[], card_type="Creature", sub_types="Cat Soldier",
                       abilities=[92970], set_id="M20", rarity="Token", collectible=False, set_number=10001,
                       mtga_id=70129)
Soldier = Card(name="soldier", pretty_name="Soldier", cost=[],
               color_identity=[], card_type="Creature", sub_types="Soldier",
               abilities=[], set_id="M20", rarity="Token", collectible=False, set_number=10002,
               mtga_id=70130)
Spirit = Card(name="spirit", pretty_name="Spirit", cost=[],
              color_identity=[], card_type="Creature", sub_types="Spirit",
              abilities=[8], set_id="M20", rarity="Token", collectible=False, set_number=10003,
              mtga_id=70131)
ElementalBird = Card(name="elemental_bird", pretty_name="Elemental Bird", cost=[],
                     color_identity=[], card_type="Creature", sub_types="Elemental Bird",
                     abilities=[8], set_id="M20", rarity="Token", collectible=False, set_number=10004,
                     mtga_id=70132)
Demon = Card(name="demon", pretty_name="Demon", cost=[],
             color_identity=[], card_type="Creature", sub_types="Demon",
             abilities=[8], set_id="M20", rarity="Token", collectible=False, set_number=10005,
             mtga_id=70133)
Zombie = Card(name="zombie", pretty_name="Zombie", cost=[],
              color_identity=[], card_type="Creature", sub_types="Zombie",
              abilities=[], set_id="M20", rarity="Token", collectible=False, set_number=10006,
              mtga_id=70134)
Elemental = Card(name="elemental", pretty_name="Elemental", cost=[],
                 color_identity=[], card_type="Creature", sub_types="Elemental",
                 abilities=[], set_id="M20", rarity="Token", collectible=False, set_number=10007,
                 mtga_id=70135)
Wolf = Card(name="wolf", pretty_name="Wolf", cost=[],
            color_identity=[], card_type="Creature", sub_types="Wolf",
            abilities=[], set_id="M20", rarity="Token", collectible=False, set_number=10008,
            mtga_id=70136)
Golem = Card(name="golem", pretty_name="Golem", cost=[],
             color_identity=[], card_type="Artifact Creature", sub_types="Golem",
             abilities=[], set_id="M20", rarity="Token", collectible=False, set_number=10009,
             mtga_id=70137)
Treasure = Card(name="treasure", pretty_name="Treasure", cost=[],
                color_identity=[], card_type="Artifact", sub_types="Treasure",
                abilities=[183], set_id="M20", rarity="Token", collectible=False, set_number=10010,
                mtga_id=70138)
RienneAngelofRebirth = Card(name="rienne_angel_of_rebirth", pretty_name="Rienne, Angel of Rebirth", cost=['2', 'R', 'G', 'W'],
                            color_identity=['W', 'R', 'G'], card_type="Creature", sub_types="Angel",
                            abilities=[8, 1402, 1403], set_id="M20", rarity="Mythic Rare", collectible=True, set_number=281,
                            mtga_id=70139)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
CoreSet2020 = Set("m20", cards=clsmembers)

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
 178: 'Scry 1.',
 183: '{oT}, Sacrifice this artifact: Add one mana of any color.',
 185: 'Protection from white',
 186: 'Protection from blue',
 187: 'Protection from black',
 188: 'Protection from red',
 189: 'Protection from green',
 1005: '{oT}: Add {oG}.',
 1026: "Bristling Boar can't be blocked by more than one creature.",
 1027: 'Enchant creature',
 1031: 'Target creature gets +4/+4 until end of turn.',
 1039: '{oT}: Add {oU} or {oR}.',
 1055: '{oT}: Add one mana of any color.',
 1083: "Enchanted creature can't attack or block.",
 1097: '{oR}: Shivan Dragon gets +1/+0 until end of turn.',
 1098: "Destroy target land. Creatures without flying can't block this turn.",
 1102: 'When Healer of the Glade enters the battlefield, you gain 3 life.',
 1103: 'Enchanted creature gets +1/+3.',
 1104: '{o3oU}: Draw a card.',
 1127: 'When Fathom Fleet Cutthroat enters the battlefield, destroy target '
       'creature an opponent controls that was dealt damage this turn.',
 1131: '{oT}: Add {oR} or {oG}.',
 1142: 'Counter target noncreature spell.',
 1152: '{oT}: Add {oC}.',
 1156: 'Equip {o3}',
 1157: 'When Gravedigger enters the battlefield, you may return target '
       'creature card from your graveyard to your hand.',
 1167: '{oT}: Add {oU} or {oB}.',
 1187: 'Enchanted creature has flying.',
 1203: '{oT}: Add {oG} or {oW}.',
 1204: "Chandra's Outrage deals 4 damage to target creature and 2 damage to "
       "that creature's controller.",
 1209: '{oT}: Add {oW} or {oU}.',
 1211: '{oT}: Add {oB} or {oR}.',
 1268: 'Equip {o1}',
 1275: 'As an additional cost to cast this spell, sacrifice a creature.',
 1278: 'Gain control of target creature until end of turn. Untap that '
       'creature. It gains haste until end of turn.',
 1314: 'Equipped creature gets +1/+1.',
 1318: 'Enchanted creature gets +3/+3.',
 1319: 'Equip {o2}',
 1385: 'Destroy target tapped creature.',
 1402: 'Other multicolored creatures you control get +1/+0.',
 1403: 'Whenever another multicolored creature you control dies, return it to '
       "its owner's hand at the beginning of the next end step.",
 1570: 'Enchant land',
 1633: '{o2}, {oT}: Draw a card, then discard a card.',
 1923: 'Return up to two target creature cards from your graveyard to your '
       'hand.',
 2018: 'Enchanted creature gets +2/+2.',
 2085: 'Create two 1/1 white Soldier creature tokens.',
 2090: 'Target creature gets +2/+2 and gains lifelink until end of turn.',
 2164: '{o1}, Sacrifice Ember Hauler: It deals 2 damage to any target.',
 2347: '{o1oG}: Frilled Sandwalla gets +2/+2 until end of turn. Activate this '
       'ability only once each turn.',
 2655: 'You have hexproof.',
 2763: 'Destroy all nonland permanents.',
 4247: '{oT}: Add {oR} or {oW}.',
 4294: 'Target creature gains deathtouch until end of turn.',
 4407: '{oT}: Add {oB} or {oG}.',
 4712: 'Equipped creature gets +2/+0.',
 4957: '{oT}: Add three mana of any one color.',
 6347: 'Whenever you discard a card, exile that card from your graveyard.',
 6951: 'You may cast spells as though they had flash.',
 7247: '{oT}: You gain 1 life.',
 9082: '{oT}: Put a +1/+1 counter on each artifact creature you control.',
 9094: 'Target creature gets +1/+1 until end of turn for each creature you '
       'control.',
 11632: 'Creatures you control get +2/+1 until end of turn.',
 13250: 'Engulfing Eruption deals 5 damage to target creature.',
 14523: 'You may look at the top card of your library any time.',
 15953: 'Golems you control get +1/+1.',
 17253: 'Counter target spell unless its controller pays {o4}.',
 17477: "Ironroot Warlord's power is equal to the number of creatures you "
        'control.',
 17519: 'When Silverback Shaman dies, draw a card.',
 17871: '{oT}: Target creature becomes the color or colors of your choice '
        'until end of turn.',
 18472: '{oT}: Add {oW} or {oB}.',
 18504: '{oT}: Add {oG} or {oU}.',
 19056: 'Destroy target artifact or enchantment. You gain 3 life.',
 19173: 'Target creature gets +2/+4 until end of turn.',
 19680: 'Whenever another blue creature enters the battlefield under your '
        'control, target player puts the top two cards of their library into '
        'their graveyard.',
 19961: 'Target creature gets +1/+1 and gains double strike until end of turn.',
 20230: 'Creature spells with flying you cast cost {o1} less to cast.',
 20341: '{o1oU}: Target creature gains flying until end of turn.',
 20486: 'Other creatures you control have vigilance.',
 20551: 'Target creature you control gains protection from the color of your '
        'choice until end of turn.',
 20623: 'Other creatures you control have trample.',
 21775: 'Target opponent reveals their hand. You choose a noncreature, nonland '
        'card from it. That player discards that card.',
 22505: "Return target creature to its owner's hand.",
 22549: '{oT}: Add {oCoC}. Spend this mana only to cast artifact spells or '
        'activate abilities of artifacts.',
 22550: '{oU}, {oT}: Search your library for a card named Heart-Piercer Bow or '
        'Vial of Dragonfire, reveal it, put it into your hand, then shuffle '
        'your library.',
 23607: 'Draw two cards.',
 23608: 'Target player discards two cards.',
 24121: 'Counter target creature spell.',
 24122: 'Return target creature card from your graveyard to your hand.',
 25848: 'Draw a card.',
 26818: 'Destroy target creature.',
 27907: 'Target creature gets -2/-2 until end of turn.',
 29759: 'Destroy target creature with flying.',
 61084: 'Look at the top three cards of your library. Put one of them into '
        'your hand and the rest on the bottom of your library in any order.',
 61119: 'Enchanted land has "{oT}: Add two mana of any one color."',
 61234: 'Target creature you control deals damage equal to its power to target '
        "creature you don't control.",
 62067: 'Enchantment spells you cast cost {o1} less to cast.',
 62106: 'Other creatures you control with flying get +1/+1.',
 62618: 'Whenever you gain life, each opponent loses 1 life.',
 62969: "Phantom Warrior can't be blocked.",
 63439: 'Reduce to Ashes deals 5 damage to target creature. If that creature '
        'would die this turn, exile it instead.',
 63468: 'Creature spells you cast cost {o1} less to cast.',
 63602: 'Target creature gets -4/-0 until end of turn.',
 63634: 'When Inspiring Captain enters the battlefield, creatures you control '
        'get +1/+1 until end of turn.',
 76735: 'Wind-Scarred Crag enters the battlefield tapped.',
 76824: 'Rubblebelt Recluse attacks each combat if able.',
 76874: 'When Frost Lynx enters the battlefield, tap target creature an '
        "opponent controls. That creature doesn't untap during its "
        "controller's next untap step.",
 76882: 'As Icon of Ancestry enters the battlefield, choose a creature type.',
 76885: 'Voracious Hydra enters the battlefield with X +1/+1 counters on it.',
 86613: 'Shock deals 2 damage to any target.',
 86788: 'When Cloudkin Seer enters the battlefield, draw a card.',
 86929: "Sorin's Thirst deals 2 damage to target creature and you gain 2 life.",
 87008: 'When Steadfast Sentry dies, put a +1/+1 counter on target creature '
        'you control.',
 87894: "Loyal Pegasus can't attack or block alone.",
 88024: '{oT}, Sacrifice Evolving Wilds: Search your library for a basic land '
        'card, put it onto the battlefield tapped, then shuffle your library.',
 88132: 'When Savannah Sage enters the battlefield, you gain 2 life.',
 88153: '{o3}, {oT}: Retributive Wand deals 1 damage to any target.',
 88178: "Enchanted creature doesn't untap during its controller's untap step.",
 88183: "Each player can't cast more than one spell each turn.",
 88237: 'As Diamond Knight enters the battlefield, choose a color.',
 88264: 'Agonizing Syphon deals 3 damage to any target and you gain 3 life.',
 88604: 'When Dawning Angel enters the battlefield, you gain 4 life.',
 88808: 'All creatures able to block Prized Unicorn do so.',
 89147: 'When Goblin Ringleader enters the battlefield, reveal the top four '
        'cards of your library. Put all Goblin cards revealed this way into '
        'your hand and the rest on the bottom of your library in any order.',
 89285: '{o1}, Sacrifice Thrashing Brontodon: Destroy target artifact or '
        'enchantment.',
 89789: 'When Sleep Paralysis enters the battlefield, tap enchanted creature.',
 90050: 'When Wind-Scarred Crag enters the battlefield, you gain 1 life.',
 90333: "Enchanted creature gets +2/+2 and can't block.",
 90859: 'Barkhide Troll enters the battlefield with a +1/+1 counter on it.',
 91002: 'When Loaming Shaman enters the battlefield, target player shuffles '
        'any number of target cards from their graveyard into their library.',
 91717: 'When Temple of Triumph enters the battlefield, scry 1.',
 91944: 'If Leyline of Abundance is in your opening hand, you may begin the '
        'game with it on the battlefield.',
 91950: "If a card would be put into an opponent's graveyard from anywhere, "
        'exile it instead.',
 92894: 'When Skeleton Archer enters the battlefield, it deals 1 damage to any '
        'target.',
 92933: '{oU}: Metropolis Sprite gets +1/-1 until end of turn.',
 92943: "Whenever an opponent is dealt noncombat damage, Chandra's Spitfire "
        'gets +3/+0 until end of turn.',
 92970: "Whenever you gain life, put a +1/+1 counter on Ajani's Pridemate.",
 93172: "{o2oB}: Yarok's Fenlurker gets +1/+1 until end of turn.",
 95377: 'When Master Splicer enters the battlefield, create a 3/3 colorless '
        'Golem artifact creature token.',
 96148: 'Spells your opponents cast that target Boreal Elemental cost {o2} '
        'more to cast.',
 97002: 'Whenever Dragon Mage deals combat damage to a player, each player '
        'discards their hand, then draws seven cards.',
 98465: "When Immortal Phoenix dies, return it to its owner's hand.",
 99583: 'When Dungeon Geists enters the battlefield, tap target creature an '
        "opponent controls. That creature doesn't untap during its "
        "controller's untap step for as long as you control Dungeon Geists.",
 99659: "Creature cards in graveyards and libraries can't enter the "
        'battlefield.',
 99802: '{o2oW}: Moorland Inquisitor gains first strike until end of turn.',
 99868: 'Whenever another creature enters the battlefield under your control, '
        'Griffin Protector gets +1/+1 until end of turn.',
 100041: 'When Keldon Raider enters the battlefield, you may discard a card. '
         'If you do, draw a card.',
 100685: 'When Octoprophet enters the battlefield, scry 2.',
 101013: 'When Howling Giant enters the battlefield, create two 2/2 green Wolf '
         'creature tokens.',
 101422: 'Whenever Netcaster Spider blocks a creature with flying, Netcaster '
         'Spider gets +2/+0 until end of turn.',
 101658: 'Whenever equipped creature attacks, Heart-Piercer Bow deals 1 damage '
         'to target creature defending player controls.',
 101887: "When Yarok's Wavecrasher enters the battlefield, return another "
         "creature you control to its owner's hand.",
 101945: 'When Glaring Aegis enters the battlefield, tap target creature an '
         'opponent controls.',
 102173: '{o2}, {oT}, Sacrifice Vial of Dragonfire: It deals 2 damage to '
         'target creature.',
 102223: 'When Faerie Miscreant enters the battlefield, if you control another '
         'creature named Faerie Miscreant, draw a card.',
 102284: 'When Undead Servant enters the battlefield, create a 2/2 black '
         'Zombie creature token for each card named Undead Servant in your '
         'graveyard.',
 102721: "Return target creature or land card from a graveyard to its owner's "
         'hand. You gain 6 life.',
 102887: '{o2oB}: Return Sanitarium Skeleton from your graveyard to your hand.',
 103130: 'When Hanged Executioner enters the battlefield, create a 1/1 white '
         'Spirit creature token with flying.',
 103216: 'When Wolfkin Bond enters the battlefield, create a 2/2 green Wolf '
         'creature token.',
 103263: 'When Haazda Officer enters the battlefield, target creature you '
         'control gets +1/+1 until end of turn.',
 103828: 'Creatures you control get +2/+2 and gain trample until end of turn.',
 113332: "Players can't cast spells from graveyards or libraries.",
 116758: 'When Battalion Foot Soldier enters the battlefield, you may search '
         'your library for any number of cards named Battalion Foot Soldier, '
         'reveal them, put them into your hand, then shuffle your library.',
 116805: 'Creatures you control of the chosen type get +1/+1.',
 116820: 'When Rapacious Dragon enters the battlefield, create two Treasure '
         'tokens.',
 117053: 'When Cavalier of Gales enters the battlefield, draw three cards, '
         'then put two cards from your hand on top of your library in any '
         'order.',
 117100: 'Other Vampires you control get +1/+1.',
 119141: 'When Meteor Golem enters the battlefield, destroy target nonland '
         'permanent an opponent controls.',
 119144: "{o3}, {oT}: Target creature can't be blocked this turn.",
 119156: "{o5oUoU}: Frilled Sea Serpent can't be blocked this turn.",
 119163: '{o5oBoB}: Return target creature card from your graveyard to the '
         'battlefield tapped.',
 119222: 'When Riddlemaster Sphinx enters the battlefield, you may return '
         "target creature an opponent controls to its owner's hand.",
 120287: "This spell can't be countered.",
 120290: 'Destroy target artifact or enchantment.',
 121333: 'Whenever one or more creatures you control attack, they gain '
         'indestructible until end of turn.',
 121386: 'Whenever Trusted Pegasus attacks, target attacking creature without '
         'flying gains flying until end of turn.',
 122104: 'Whenever another creature enters the battlefield under your control, '
         'you gain 1 life.',
 133176: '{o2}: Add one mana of any color.',
 133264: '{o6oB}: Each opponent loses 2 life and you gain 2 life.',
 133292: '-2: Chandra, Novice Pyromancer deals 2 damage to any target.',
 133423: 'Choose up to two target permanent cards in your graveyard that were '
         'put there from the battlefield this turn. Return them to the '
         'battlefield tapped.',
 133424: 'When Cavalier of Dawn dies, return target artifact or enchantment '
         'card from your graveyard to your hand.',
 133427: 'Whenever a Swamp enters the battlefield under your control, choose '
         'one   You draw a card and you lose 1 life.  Dread Presence deals 2 '
         'damage to any target and you gain 2 life.',
 133428: 'Embodiment of Agonies enters the battlefield with a +1/+1 counter on '
         'it for each different mana cost among nonland cards in your '
         'graveyard. \n'
         '<i>(For example, {o2oB} and {o1oBoB} are different mana costs.)</i>',
 133429: 'When Gorging Vulture enters the battlefield, put the top four cards '
         'of your library into your graveyard. You gain 1 life for each '
         'creature card put into your graveyard this way.',
 133430: '{o2oB}: Knight of the Ebon Legion gets +3/+3 and gains deathtouch '
         'until end of turn.',
 133431: 'At the beginning of your end step, if a player lost 4 or more life '
         'this turn, put a +1/+1 counter on Knight of the Ebon Legion.',
 133432: 'Exile target creature an opponent controls with converted mana cost '
         '2 or less and all other creatures that player controls with the same '
         'name as that creature. Then that player reveals their hand and '
         'exiles all cards with that name from their hand and graveyard.',
 133433: "Destroy target creature or planeswalker that's green or white. You "
         'gain 1 life.',
 133434: 'Target opponent reveals their hand. Exile all noncreature, nonland '
         "cards from that player's hand and graveyard.",
 133435: '{o5oW}: Loxodon Lifechanter gets +X/+X until end of turn, where X is '
         'your life total.',
 133436: '{o1oR}: Creatures you control get +1/+0 and gain haste until end of '
         'turn.',
 133437: 'When Cavalier of Flame enters the battlefield, discard any number of '
         'cards, then draw that many cards.',
 133439: 'Whenever you activate a loyalty ability of a Chandra planeswalker, '
         'you may pay {o1}. If you do, copy that ability. You may choose new '
         'targets for the copy.',
 133440: "Exile target creature or planeswalker that's black or red. Scry 1.",
 133441: 'Whenever another creature enters the battlefield under your control, '
         'Marauding Raptor deals 2 damage to it. If a Dinosaur is dealt damage '
         'this way, Marauding Raptor gets +2/+0 until end of turn.',
 133442: 'When Mask of Immolation enters the battlefield, create a 1/1 red '
         'Elemental creature token, then attach Mask of Immolation to it.',
 133444: 'Equipped creature has "Sacrifice this creature: It deals 1 damage to '
         'any target."',
 133446: 'Choose one   Reckless Air Strike deals 3 damage to target creature '
         'with flying.  Destroy target artifact.',
 133447: 'Whenever Scorch Spitter attacks, it deals 1 damage to the player or '
         "planeswalker it's attacking.",
 133448: 'Whenever Thunderkin Awakener attacks, choose target Elemental '
         'creature card in your graveyard with toughness less than Thunderkin '
         "Awakener's toughness. Return that card to the battlefield tapped and "
         'attacking. Sacrifice it at the beginning of the next end step.',
 133449: 'You may pay {oW} and tap four untapped creatures you control with '
         "flying rather than pay this spell's mana cost.",
 133450: "Unchained Berserker gets +2/+0 as long as it's attacking.",
 133451: '{o1}, Remove a +1/+1 counter from Barkhide Troll: Barkhide Troll '
         'gains hexproof until end of turn.',
 133452: '{o5oG}, {oT}: Look at the top four cards of your library. You may '
         'reveal a creature card from among them and put it into your hand. '
         'Put the rest on the bottom of your library in a random order.',
 133453: 'Other creatures you control with flying have indestructible.',
 133454: 'When Cavalier of Thorns dies, you may exile it. If you do, put '
         'another target card from your graveyard on top of your library.',
 133455: 'Elvish Reclaimer gets +2/+2 as long as there are three or more land '
         'cards in your graveyard.',
 133456: '{o2}, {oT}, Sacrifice a land: Search your library for a land card, '
         'put it onto the battlefield tapped, then shuffle your library.',
 133457: 'Whenever a creature you control becomes the target of a spell, '
         "Gargos, Vicious Watcher fights up to one target creature you don't "
         'control.',
 133458: 'Hydra spells you cast cost {o4} less to cast.',
 133459: 'Squad Captain enters the battlefield with a +1/+1 counter on it for '
         'each other creature you control.',
 133460: '{oT}: Add {oG}. If you control four or more creatures, add {oGoG} '
         'instead.',
 133461: 'Whenever you tap a creature for mana, add an additional {oG}.',
 133462: '{o6oGoG}: Put a +1/+1 counter on each creature you control.',
 133463: 'Put target creature with power 4 or greater on the bottom of its '
         "owner's library.",
 133464: 'Other Wolves and Werewolves you control get +1/+1.',
 133465: "At the beginning of your end step, if you didn't cast a spell this "
         'turn, create a 2/2 green Wolf creature token.',
 133466: 'Whenever an enchantment you control is put into a graveyard from the '
         'battlefield, put a +1/+1 counter on Starfield Mystic.',
 133467: 'Whenever another creature you control dies, you gain 1 life. If that '
         'creature was an Elemental, put a +1/+1 counter on Overgrowth '
         'Elemental.',
 133468: 'Whenever a creature enters the battlefield under your control, scry '
         '1.',
 133469: 'Search your library for up to two creature cards with different '
         'names, reveal them, put them into your hand, then shuffle your '
         'library.',
 133470: '{oG}: Shifting Ceratops gains your choice of reach, trample, or '
         'haste until end of turn.',
 133471: 'Other Elementals you control have trample.',
 133472: "Choose target spell or permanent that's red or green. Its owner puts "
         'it on the top or bottom of their library.',
 133473: 'Draw a card if an opponent has cast a blue or black spell this turn. '
         "Spells you control can't be countered this turn. You and permanents "
         'you control gain hexproof from blue and from black until end of '
         'turn.',
 133474: '+1: Distribute two +1/+1 counters among up to two target creatures. '
         'They gain trample until end of turn.',
 133475: '-3: Target creature you control deals damage equal to its power to '
         'target creature or planeswalker.',
 133476: '-5: You may choose a creature card you own from outside the game, '
         'reveal it, and put it into your hand.',
 133477: 'When Agent of Treachery enters the battlefield, gain control of '
         'target permanent.',
 133478: 'Target creature gets +3/+3 until end of turn. It gets an additional '
         '+2/+2 until end of turn for each card named Growth Cycle in your '
         'graveyard.',
 133479: '{oGoGoGoGoG}: Untap target land you control. It becomes a 5/5 '
         "Elemental creature with haste. It's still a land.",
 133480: "When Wolfrider's Saddle enters the battlefield, create a 2/2 green "
         "Wolf creature token, then attach Wolfrider's Saddle to it.",
 133481: "Equipped creature gets +1/+1 and can't be blocked by more than one "
         'creature.',
 133482: 'At the beginning of your end step, if you control three or more '
         "permanents you don't own, draw three cards.",
 133483: 'Enchanted creature gets +0/+2 and assigns combat damage equal to its '
         'toughness rather than its power.',
 133484: 'Whenever another creature enters the battlefield under your control, '
         'each opponent loses 1 life.',
 133485: 'Other Elementals you control get +1/+0.',
 133486: '{o2oRoG}: Creeping Trailblazer gets +1/+1 until end of turn for each '
         'Elemental you control.',
 133487: '{o3oGoW}: Create a 1/1 white Soldier creature token.',
 133488: 'When Kaalia, Zenith Seeker enters the battlefield, look at the top '
         'six cards of your library. You may reveal an Angel card, a Demon '
         'card, and/or a Dragon card from among them and put them into your '
         'hand. Put the rest on the bottom of your library in a random order.',
 133489: 'Legendary spells you cast cost {o1} less to cast.',
 133491: 'Exile two legendary cards from your graveyard: Until end of turn, '
         'each legendary card in your graveyard gains "You may play this card '
         'from your graveyard."',
 133492: '{o2oU}, {oT}: Draw two cards, then discard a card.',
 133493: 'Sacrifice a Spirit: Add {oR}.',
 133494: 'Whenever a creature you control dies, you gain 1 life and draw a '
         'card.',
 133495: '{o2oBoR}: Destroy target creature that was dealt damage this turn.',
 133496: 'When Omnath, Locus of the Roil enters the battlefield, it deals '
         'damage to any target equal to the number of Elementals you control.',
 133497: 'Whenever a land enters the battlefield under your control, put a '
         '+1/+1 counter on target Elemental you control. If you control eight '
         'or more lands, draw a card.',
 133498: 'Whenever Atemsis, All-Seeing deals damage to an opponent, you may '
         'reveal your hand. If cards with at least six different converted '
         'mana costs are revealed this way, that player loses the game.',
 133499: 'Whenever Skyknight Vanguard attacks, create a 1/1 white Soldier '
         "creature token that's tapped and attacking.",
 133500: 'If a permanent entering the battlefield causes a triggered ability '
         'of a permanent you control to trigger, that ability triggers an '
         'additional time.',
 133501: 'Equipped creature gets +10/+10 and loses flying.',
 133502: 'Equip {o8}',
 133503: 'Whenever you cast a spell of the chosen color, put a +1/+1 counter '
         'on Diamond Knight.',
 133504: '{o1}, {oT}: Choose a card name, then reveal the top card of your '
         "library. If that card has the chosen name, sacrifice Diviner's "
         'Lockbox and draw three cards. Activate this ability only any time '
         'you could cast a sorcery.',
 133506: '{o3}, {oT}: Look at the top three cards of your library. You may '
         'reveal a creature card of the chosen type from among them and put it '
         'into your hand. Put the rest on the bottom of your library in a '
         'random order.',
 133507: "You may cast the top card of your library if it's an artifact card "
         'or a colorless nonland card.',
 133508: 'When Pattern Matcher enters the battlefield, you may search your '
         'library for a card with the same name as another creature you '
         'control, reveal it, put it into your hand, then shuffle your '
         'library.',
 133509: "Whenever you cast a spell during an opponent's turn, put a +1/+1 "
         'counter on Brineborn Cutthroat.',
 133510: 'Sacrifice Salvager of Ruin: Choose target permanent card in your '
         'graveyard that was put there from the battlefield this turn. Return '
         'it to your hand.',
 133511: "Return up to three target creatures to their owners' hands.",
 133512: '{o1}, {oT}, Sacrifice Cryptic Caves: Draw a card. Activate this '
         'ability only if you control five or more lands.',
 133513: 'Enchanted creature has "{o2oW}: Untap this creature."',
 133514: 'Whenever Field of the Dead or another land enters the battlefield '
         'under your control, if you control seven or more lands with '
         'different names, create a 2/2 black Zombie creature token.',
 133515: 'When Lotus Field enters the battlefield, sacrifice two lands.',
 133516: "When Cavalier of Gales dies, shuffle it into its owner's library, "
         'then scry 2.',
 133517: 'When Overgrowth Elemental enters the battlefield, put a +1/+1 '
         'counter on another target Elemental you control.',
 133518: '+2: You gain 2 life. Put two +1/+1 counters on up to one target '
         'creature.',
 133519: '-3: Exile target creature. Its controller gains 2 life.',
 133520: '-10: Creatures you control gain flying and double strike until end '
         'of turn.',
 133522: 'Sacrifice Cerulean Drake: Counter target spell that targets you.',
 133523: '+1: Until your next turn, up to one target creature gets -5/-0.',
 133524: "-3: Return up to two target creatures to their owners' hands.",
 133525: '-7: Creatures you control with flying get +5/+5 until end of turn.',
 133526: 'Celestial Messenger gets +1/+1 as long as you control a Yanling '
         'planeswalker.',
 133527: 'Whenever a creature with flying enters the battlefield under your '
         'control, Waterkin Shaman gets +1/+1 until end of turn.',
 133528: '+1: Up to one target creature gets +2/+0 until end of turn.',
 133529: '-2: Sorin, Vampire Lord deals 4 damage to any target. You gain 4 '
         'life.',
 133531: '-8: Until end of turn, each Vampire you control gains "{oT}: Gain '
         'control of target creature."',
 133532: 'At the beginning of your end step, if an opponent lost life this '
         'turn, put a +1/+1 counter on Savage Gorger.',
 133533: 'Look at the top seven cards of your library. Put two of them into '
         'your hand and the rest on the bottom of your library in a random '
         'order.',
 133534: "+1: Chandra, Flame's Fury deals 2 damage to any target.",
 133535: "-2: Chandra, Flame's Fury deals 4 damage to target creature and 2 "
         "damage to that creature's controller.",
 133536: "-8: Chandra, Flame's Fury deals 10 damage to target player and each "
         'creature that player controls.',
 133537: 'When Cavalier of Dawn enters the battlefield, destroy up to one '
         'target nonland permanent. Its controller creates a 3/3 colorless '
         'Golem artifact creature token.',
 133538: 'Whenever an opponent is dealt noncombat damage, creatures you '
         'control get +1/+0 until end of turn.',
 133541: '-1: Reveal cards from the top of your library until you reveal a '
         'creature card. Put that card into your hand and the rest on the '
         'bottom of your library in a random order.',
 133542: '-6: Target creature gets +10/+10 and gains trample until end of '
         'turn.',
 133543: 'Whenever you cast a spell that targets Gnarlback Rhino, draw a card.',
 133544: 'Whenever you cast a spell that targets a creature you control, draw '
         'a card.',
 133545: '{o1oR}: Each creature you control named Pack Mastiff gets +1/+0 '
         'until end of turn.',
 133546: "Return all nonland permanents to their owners' hands. If you return "
         'four or more nontoken permanents you control this way, you may put a '
         'permanent card from your hand onto the battlefield.',
 133548: 'Enchanted creature gets +0/+2 and has "{oT}: Draw a card, then '
         'discard a card."',
 133553: 'Choose one   Create two 3/3 colorless Golem artifact creature '
         'tokens.  Choose target artifact you control. Each other artifact you '
         'control becomes a copy of that artifact until end of turn.',
 133554: '+2: Until your next turn, up to one target creature gets -2/-0 and '
         'loses flying.',
 133555: 'Whenever Lavakin Brawler attacks, it gets +1/+0 until end of turn '
         'for each Elemental you control.',
 133556: '-3: Create a 4/4 blue Elemental Bird creature token with flying.',
 133559: 'When Voracious Hydra enters the battlefield, choose one   Double the '
         'number of +1/+1 counters on Voracious Hydra.  Voracious Hydra fights '
         "target creature you don't control.",
 133560: '-8: You get an emblem with "Islands you control have {oT}: Draw a '
         'card.\'"',
 133561: '+1: Elementals you control get +2/+0 until end of turn.',
 133562: '{o1}, {oT}: Return target creature you control and each Aura '
         "attached to it to their owners' hands. Activate this ability only "
         'during your turn.',
 133563: 'Whenever one or more tokens enter the battlefield under your '
         'control, put that many +1/+1 counters on Woodland Champion.',
 133564: 'When Scholar of the Ages enters the battlefield, return up to two '
         'target instant and/or sorcery cards from your graveyard to your '
         'hand.',
 133565: '{o3oW}, Exile Hanged Executioner: Exile target creature.',
 133566: '{o1oRoR}: Pyroclastic Elemental deals 1 damage to target player.',
 133567: 'Counter target activated ability, triggered ability, or legendary '
         'spell.',
 133568: '{o3oW}: Put a +1/+1 counter on another target creature with flying.',
 133569: 'This spell costs {o1} less to cast if you control a creature with '
         'flying.',
 133570: 'Whenever you cast a noncreature spell, create a 1/1 white Spirit '
         'creature token with flying.',
 133571: 'When you next cast an instant spell, cast a sorcery spell, or '
         'activate a loyalty ability this turn, copy that spell or ability '
         'twice. You may choose new targets for the copies.',
 133572: 'Whenever Audacious Thief attacks, you draw a card and you lose 1 '
         'life.',
 133573: 'When Scampering Scorcher enters the battlefield, create two 1/1 red '
         'Elemental creature tokens. Elementals you control gain haste until '
         'end of turn.',
 133574: 'Whenever you and/or at least one permanent you control becomes the '
         'target of a spell or ability an opponent controls, Leyline of '
         'Combustion deals 2 damage to that player.',
 133575: "Creatures your opponents control can't have +1/+1 counters put on "
         'them.',
 133576: "As long as it's your turn, Blood Burglar has lifelink.",
 133577: 'Whenever Tomebound Lich enters the battlefield or deals combat '
         'damage to a player, draw a card, then discard a card.',
 133578: "Vivien's Crocodile gets +1/+1 as long as you control a Vivien "
         'planeswalker.',
 133579: 'Return a creature card from your graveyard to the battlefield, then '
         'return another creature card from your graveyard to your hand.',
 133580: '{oT}, Pay 2 life, Discard a card, Sacrifice a creature: Create a 5/5 '
         'black Demon creature token with flying. Activate this ability only '
         'any time you could cast a sorcery.',
 133581: '{o4}, {oT}, Sacrifice Bag of Holding: Return all cards exiled with '
         "Bag of Holding to their owner's hand.",
 133582: 'When Boneclad Necromancer enters the battlefield, you may exile '
         'target creature card from a graveyard. If you do, create a 2/2 black '
         'Zombie creature token.',
 133583: 'When Cavalier of Night enters the battlefield, you may sacrifice '
         'another creature. When you do, destroy target creature an opponent '
         'controls.',
 133584: 'When Cavalier of Night dies, return target creature card with '
         'converted mana cost 3 or less from your graveyard to the '
         'battlefield.',
 133585: 'Target creature gets +1/+3 until end of turn.',
 133586: 'When Golos, Tireless Pilgrim enters the battlefield, you may search '
         'your library for a land card, put that card onto the battlefield '
         'tapped, then shuffle your library.',
 133587: '{o2oWoUoBoRoG}: Exile the top three cards of your library. You may '
         'play them this turn without paying their mana costs.',
 133588: 'When Loxodon Lifechanter enters the battlefield, you may have your '
         'life total become the total toughness of creatures you control.',
 133589: '{o1}, {oT}: Untap another target artifact.',
 133590: 'When Gruesome Scourger enters the battlefield, it deals damage to '
         'target opponent or planeswalker equal to the number of creatures you '
         'control.',
 133591: '{oT}, Pay 1 life: Exile the top card of your library.',
 133592: 'At the beginning of your upkeep, discard a card.',
 133593: 'Choose two target players. Each of them searches their library for a '
         'card, then shuffles their library and puts that card on top of it.',
 133594: 'When Retributive Wand is put into a graveyard from the battlefield, '
         'it deals 5 damage to any target.',
 133595: '{o5oB}, {oT}: Sorcerer of the Fang deals 2 damage to target opponent '
         'or planeswalker.',
 133596: '+1: Target creature you control gains deathtouch and lifelink until '
         "end of turn. If it's a Vampire, put a +1/+1 counter on it.",
 133597: '+1: You may sacrifice a Vampire. When you do, Sorin, Imperious '
         'Bloodlord deals 3 damage to any target and you gain 3 life.',
 133598: '-3: You may put a Vampire creature card from your hand onto the '
         'battlefield.',
 133599: 'When enchanted creature dies, return that card to the battlefield '
         'under your control with a +1/+1 counter on it.',
 133600: 'Whenever you lose life for the first time each turn, put a +1/+1 '
         'counter on Vengeful Warchief.',
 133601: '{oB}, Pay 2 life: Target creature gets -1/-1 until end of turn.',
 133602: 'Whenever you lose life, draw that many cards.',
 133603: "When Yarok's Fenlurker enters the battlefield, each opponent exiles "
         'a card from their hand.',
 133604: 'Whenever Risen Reef or another Elemental enters the battlefield '
         "under your control, look at the top card of your library. If it's a "
         "land card, you may put it onto the battlefield tapped. If you don't "
         'put the card onto the battlefield, put it into your hand.',
 133605: 'When Cavalier of Flame dies, it deals X damage to each opponent and '
         'each planeswalker they control, where X is the number of land cards '
         'in your graveyard.',
 133606: '0: Put a loyalty counter on each red planeswalker you control.',
 133607: '0: Create two 1/1 red Elemental creature tokens. They gain haste. '
         'Sacrifice them at the beginning of the next end step.',
 133608: '-2: You may cast target instant or sorcery card with converted mana '
         'cost 3 or less from your graveyard. If that card would be put into '
         'your graveyard this turn, exile it instead.',
 133609: '+2: Each opponent gets an emblem with "At the beginning of your '
         'upkeep, this emblem deals 1 damage to you."',
 133610: '-3: Chandra, Awakened Inferno deals 3 damage to each non-Elemental '
         'creature.',
 133611: 'When Cavalier of Thorns enters the battlefield, reveal the top five '
         'cards of your library. Put a land card from among them onto the '
         'battlefield and the rest into your graveyard.',
 133612: '-X: Chandra, Awakened Inferno deals X damage to target creature or '
         'planeswalker. If a permanent dealt damage this way would die this '
         'turn, exile it instead.',
 133613: '-1: Add {oRoR}.',
 133614: '{oT}: Add {oR}. Spend this mana only to cast an Elemental spell or a '
         'Chandra planeswalker spell.',
 133615: 'As long as you have 25 or more life, Twinblade Paladin has double '
         'strike.',
 133616: "-2: Create a 2/2 white Cat Soldier creature token named Ajani's "
         'Pridemate with "Whenever you gain life, put a +1/+1 counter on '
         'Ajani\'s Pridemate."',
 133617: '{o1}, {oT}, Discard a Mountain card or a red card: Draw a card.',
 133619: "As long as it's your turn, Daggersail Aeronaut has flying.",
 133620: '{o3}, {oT}, Sacrifice an artifact or land: Draw a card.',
 133622: 'If you would gain life, you gain that much life plus 1 instead.',
 133623: 'Whenever Drakuseth, Maw of Flames attacks, it deals 4 damage to any '
         'target and 3 damage to each of up to two other targets.',
 133624: 'Angel of Vitality gets +2/+2 as long as you have 25 or more life.',
 133625: 'Flame Sweep deals 2 damage to each creature except for creatures you '
         'control with flying.',
 133626: "Fry deals 5 damage to target creature or planeswalker that's white "
         'or blue.',
 133627: 'Whenever you discard a card, Glint-Horn Buccaneer deals 1 damage to '
         'each opponent.',
 133628: '{o1oR}, Discard a card: Draw a card. Activate this ability only if '
         'Glint-Horn Buccaneer is attacking.',
 133629: '{oR}: Goblin Bird-Grabber gains flying until end of turn. Activate '
         'this ability only if you control a creature with flying.',
 133630: 'Destroy target tapped creature. You gain 1 life for each creature '
         'you control with flying.',
 133631: '+1: You gain life equal to the number of creatures you control plus '
         'the number of planeswalkers you control.',
 133633: '0: If you have at least 15 life more than your starting life total, '
         'exile Ajani, Strength of the Pride and each artifact and creature '
         'your opponents control.',
 133634: 'When Ancestral Blade enters the battlefield, create a 1/1 white '
         'Soldier creature token, then attach Ancestral Blade to it.',
 133636: "{oT}: Another target creature with power 2 or less can't be blocked "
         'this turn.',
 133637: '{o2}: Exile target card from a graveyard.',
 133638: 'Target creature gets +3/+2 until end of turn.',
 133639: 'Whenever an Angel enters the battlefield under your control, you '
         'gain 4 life.',
 133640: 'Whenever an Angel you control dies, create a 1/1 white Spirit '
         'creature token with flying.',
 133915: '+1: Put three +1/+1 counters on up to one target creature.',
 135533: 'When Goldmane Griffin enters the battlefield, you may search your '
         'library and graveyard for a card named Ajani, Inspiring Leader, '
         'reveal it, put it into your hand, then shuffle your library.',
 135540: "When Yanling's Harbinger enters the battlefield, you may search your "
         'library and graveyard for a card named Mu Yanling, Celestial Wind, '
         'reveal it, put it into your hand, then shuffle your library.',
 135546: "When Sorin's Guide enters the battlefield, you may search your "
         'library and graveyard for a card named Sorin, Vampire Lord, reveal '
         'it, put it into your hand, then shuffle your library.',
 135550: "Chandra's Flame Wave deals 2 damage to target player and each "
         'creature that player controls. Search your library and graveyard for '
         "a card named Chandra, Flame's Fury, reveal it, put it into your "
         'hand, then shuffle your library.',
 135556: 'When Ethereal Elk enters the battlefield, you may search your '
         "library and graveyard for a card named Vivien, Nature's Avenger, "
         'reveal it, put it into your hand, then shuffle your library.'}
