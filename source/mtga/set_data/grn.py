
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


BladeInstructor = Card(name="blade_instructor", pretty_name="Blade Instructor", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                       abilities=[171], set_id="GRN", rarity="Common", set_number=1,
                       mtga_id=68462)
BountyAgent = Card(name="bounty_agent", pretty_name="Bounty Agent", cost=['1', 'W'],
                   color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                   abilities=[15, 121564], set_id="GRN", rarity="Rare", set_number=2,
                   mtga_id=68463)
CandlelightVigil = Card(name="candlelight_vigil", pretty_name="Candlelight Vigil", cost=['3', 'W'],
                        color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 121551], set_id="GRN", rarity="Common", set_number=3,
                        mtga_id=68464)
CitywideBust = Card(name="citywide_bust", pretty_name="Citywide Bust", cost=['1', 'W', 'W'],
                    color_identity=['W'], card_type="Sorcery", sub_types="",
                    abilities=[121565], set_id="GRN", rarity="Rare", set_number=4,
                    mtga_id=68465)
CollartheCulprit = Card(name="collar_the_culprit", pretty_name="Collar the Culprit", cost=['3', 'W'],
                        color_identity=['W'], card_type="Instant", sub_types="",
                        abilities=[22658], set_id="GRN", rarity="Common", set_number=5,
                        mtga_id=68466)
ConclaveTribunal = Card(name="conclave_tribunal", pretty_name="Conclave Tribunal", cost=['3', 'W'],
                        color_identity=['W'], card_type="Enchantment", sub_types="",
                        abilities=[52, 20997], set_id="GRN", rarity="Uncommon", set_number=6,
                        mtga_id=68467)
CrushContraband = Card(name="crush_contraband", pretty_name="Crush Contraband", cost=['3', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[121557], set_id="GRN", rarity="Uncommon", set_number=7,
                       mtga_id=68468)
DawnofHope = Card(name="dawn_of_hope", pretty_name="Dawn of Hope", cost=['1', 'W'],
                  color_identity=['W'], card_type="Enchantment", sub_types="",
                  abilities=[121567, 121568], set_id="GRN", rarity="Rare", set_number=8,
                  mtga_id=68469)
Demotion = Card(name="demotion", pretty_name="Demotion", cost=['W'],
                color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                abilities=[1027, 90489], set_id="GRN", rarity="Uncommon", set_number=9,
                mtga_id=68470)
DivineVisitation = Card(name="divine_visitation", pretty_name="Divine Visitation", cost=['3', 'W', 'W'],
                        color_identity=['W'], card_type="Enchantment", sub_types="",
                        abilities=[121569], set_id="GRN", rarity="Mythic Rare", set_number=10,
                        mtga_id=68471)
FlightofEquenauts = Card(name="flight_of_equenauts", pretty_name="Flight of Equenauts", cost=['7', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                         abilities=[52, 8], set_id="GRN", rarity="Uncommon", set_number=11,
                         mtga_id=68472)
GirdforBattle = Card(name="gird_for_battle", pretty_name="Gird for Battle", cost=['W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[18631], set_id="GRN", rarity="Uncommon", set_number=12,
                     mtga_id=68473)
HaazdaMarshal = Card(name="haazda_marshal", pretty_name="Haazda Marshal", cost=['W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                     abilities=[121570], set_id="GRN", rarity="Uncommon", set_number=13,
                     mtga_id=68474)
HealersHawk = Card(name="healers_hawk", pretty_name="Healer's Hawk", cost=['W'],
                   color_identity=['W'], card_type="Creature", sub_types="Bird",
                   abilities=[8, 12], set_id="GRN", rarity="Common", set_number=14,
                   mtga_id=68475)
HuntedWitness = Card(name="hunted_witness", pretty_name="Hunted Witness", cost=['W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human",
                     abilities=[121571], set_id="GRN", rarity="Common", set_number=15,
                     mtga_id=68476)
InspiringUnicorn = Card(name="inspiring_unicorn", pretty_name="Inspiring Unicorn", cost=['2', 'W', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Unicorn",
                        abilities=[121572], set_id="GRN", rarity="Uncommon", set_number=16,
                        mtga_id=68477)
IntrusivePackbeast = Card(name="intrusive_packbeast", pretty_name="Intrusive Packbeast", cost=['4', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Beast",
                          abilities=[15, 121352], set_id="GRN", rarity="Common", set_number=17,
                          mtga_id=68478)
LedevGuardian = Card(name="ledev_guardian", pretty_name="Ledev Guardian", cost=['3', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                     abilities=[52], set_id="GRN", rarity="Common", set_number=18,
                     mtga_id=68479)
LightoftheLegion = Card(name="light_of_the_legion", pretty_name="Light of the Legion", cost=['4', 'W', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Angel",
                        abilities=[8, 171, 121471], set_id="GRN", rarity="Rare", set_number=19,
                        mtga_id=68480)
LoxodonRestorer = Card(name="loxodon_restorer", pretty_name="Loxodon Restorer", cost=['4', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Elephant Cleric",
                       abilities=[52, 88604], set_id="GRN", rarity="Common", set_number=20,
                       mtga_id=68481)
LuminousBonds = Card(name="luminous_bonds", pretty_name="Luminous Bonds", cost=['2', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 1083], set_id="GRN", rarity="Common", set_number=21,
                     mtga_id=68482)
ParhelionPatrol = Card(name="parhelion_patrol", pretty_name="Parhelion Patrol", cost=['3', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                       abilities=[8, 15, 171], set_id="GRN", rarity="Common", set_number=22,
                       mtga_id=68483)
RighteousBlow = Card(name="righteous_blow", pretty_name="Righteous Blow", cost=['W'],
                     color_identity=['W'], card_type="Instant", sub_types="",
                     abilities=[99791], set_id="GRN", rarity="Common", set_number=23,
                     mtga_id=68484)
RocCharger = Card(name="roc_charger", pretty_name="Roc Charger", cost=['2', 'W'],
                  color_identity=['W'], card_type="Creature", sub_types="Bird",
                  abilities=[8, 121386], set_id="GRN", rarity="Uncommon", set_number=24,
                  mtga_id=68485)
SkylineScout = Card(name="skyline_scout", pretty_name="Skyline Scout", cost=['1', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Human Scout",
                    abilities=[121407], set_id="GRN", rarity="Common", set_number=25,
                    mtga_id=68486)
SunhomeStalwart = Card(name="sunhome_stalwart", pretty_name="Sunhome Stalwart", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                       abilities=[6, 171], set_id="GRN", rarity="Uncommon", set_number=26,
                       mtga_id=68487)
SwornCompanions = Card(name="sworn_companions", pretty_name="Sworn Companions", cost=['2', 'W'],
                       color_identity=['W'], card_type="Sorcery", sub_types="",
                       abilities=[121431], set_id="GRN", rarity="Common", set_number=27,
                       mtga_id=68488)
TakeHeart = Card(name="take_heart", pretty_name="Take Heart", cost=['W'],
                 color_identity=['W'], card_type="Instant", sub_types="",
                 abilities=[121451], set_id="GRN", rarity="Common", set_number=28,
                 mtga_id=68489)
TenthDistrictGuard = Card(name="tenth_district_guard", pretty_name="Tenth District Guard", cost=['1', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                          abilities=[121464], set_id="GRN", rarity="Common", set_number=29,
                          mtga_id=68490)
VeneratedLoxodon = Card(name="venerated_loxodon", pretty_name="Venerated Loxodon", cost=['4', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Elephant Cleric",
                        abilities=[52, 121470], set_id="GRN", rarity="Rare", set_number=30,
                        mtga_id=68491)
CaptureSphere = Card(name="capture_sphere", pretty_name="Capture Sphere", cost=['3', 'U'],
                     color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                     abilities=[7, 1027, 89789, 88178], set_id="GRN", rarity="Common", set_number=31,
                     mtga_id=68492)
ChemistersInsight = Card(name="chemisters_insight", pretty_name="Chemister's Insight", cost=['3', 'U'],
                         color_identity=['U'], card_type="Instant", sub_types="",
                         abilities=[23607, 170], set_id="GRN", rarity="Uncommon", set_number=32,
                         mtga_id=68493)
CitywatchSphinx = Card(name="citywatch_sphinx", pretty_name="Citywatch Sphinx", cost=['5', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                       abilities=[8, 121497], set_id="GRN", rarity="Uncommon", set_number=33,
                       mtga_id=68494)
DazzlingLights = Card(name="dazzling_lights", pretty_name="Dazzling Lights", cost=['U'],
                      color_identity=['U'], card_type="Instant", sub_types="",
                      abilities=[6672, 121353], set_id="GRN", rarity="Common", set_number=34,
                      mtga_id=68495)
DeviousCoverUp = Card(name="devious_coverup", pretty_name="Devious Cover-Up", cost=['2', 'U', 'U'],
                      color_identity=['U'], card_type="Instant", sub_types="",
                      abilities=[121354], set_id="GRN", rarity="Common", set_number=35,
                      mtga_id=68496)
DimirInformant = Card(name="dimir_informant", pretty_name="Dimir Informant", cost=['2', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Human Rogue",
                      abilities=[121357], set_id="GRN", rarity="Common", set_number=36,
                      mtga_id=68497)
DisdainfulStroke = Card(name="disdainful_stroke", pretty_name="Disdainful Stroke", cost=['1', 'U'],
                        color_identity=['U'], card_type="Instant", sub_types="",
                        abilities=[21963], set_id="GRN", rarity="Common", set_number=37,
                        mtga_id=68498)
DreamEater = Card(name="dream_eater", pretty_name="Dream Eater", cost=['4', 'U', 'U'],
                  color_identity=['U'], card_type="Creature", sub_types="Nightmare Sphinx",
                  abilities=[7, 8, 121521], set_id="GRN", rarity="Mythic Rare", set_number=38,
                  mtga_id=68499)
DrownedSecrets = Card(name="drowned_secrets", pretty_name="Drowned Secrets", cost=['1', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="",
                      abilities=[121364], set_id="GRN", rarity="Rare", set_number=39,
                      mtga_id=68500)
EnhancedSurveillance = Card(name="enhanced_surveillance", pretty_name="Enhanced Surveillance", cost=['1', 'U'],
                            color_identity=['U'], card_type="Enchantment", sub_types="",
                            abilities=[121365, 121531], set_id="GRN", rarity="Uncommon", set_number=40,
                            mtga_id=68501)
GuildSummit = Card(name="guild_summit", pretty_name="Guild Summit", cost=['2', 'U'],
                   color_identity=['U'], card_type="Enchantment", sub_types="",
                   abilities=[121534, 121537], set_id="GRN", rarity="Uncommon", set_number=41,
                   mtga_id=68502)
Leapfrog = Card(name="leapfrog", pretty_name="Leapfrog", cost=['2', 'U'],
                color_identity=['U'], card_type="Creature", sub_types="Frog",
                abilities=[121539], set_id="GRN", rarity="Common", set_number=42,
                mtga_id=68503)
MaximizeAltitude = Card(name="maximize_altitude", pretty_name="Maximize Altitude", cost=['U'],
                        color_identity=['U'], card_type="Sorcery", sub_types="",
                        abilities=[121369, 170], set_id="GRN", rarity="Common", set_number=43,
                        mtga_id=68504)
MissionBriefing = Card(name="mission_briefing", pretty_name="Mission Briefing", cost=['U', 'U'],
                       color_identity=['U'], card_type="Instant", sub_types="",
                       abilities=[121375], set_id="GRN", rarity="Rare", set_number=44,
                       mtga_id=68505)
MurmuringMystic = Card(name="murmuring_mystic", pretty_name="Murmuring Mystic", cost=['3', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[121381], set_id="GRN", rarity="Uncommon", set_number=45,
                       mtga_id=68506)
MuseDrake = Card(name="muse_drake", pretty_name="Muse Drake", cost=['3', 'U'],
                 color_identity=['U'], card_type="Creature", sub_types="Drake",
                 abilities=[8, 86788], set_id="GRN", rarity="Common", set_number=46,
                 mtga_id=68507)
Narcomoeba = Card(name="narcomoeba", pretty_name="Narcomoeba", cost=['1', 'U'],
                  color_identity=['U'], card_type="Creature", sub_types="Illusion",
                  abilities=[8, 91716], set_id="GRN", rarity="Rare", set_number=47,
                  mtga_id=68508)
NightveilSprite = Card(name="nightveil_sprite", pretty_name="Nightveil Sprite", cost=['1', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Faerie Rogue",
                       abilities=[8, 121394], set_id="GRN", rarity="Uncommon", set_number=48,
                       mtga_id=68509)
OmnispellAdept = Card(name="omnispell_adept", pretty_name="Omnispell Adept", cost=['4', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                      abilities=[121397], set_id="GRN", rarity="Rare", set_number=49,
                      mtga_id=68510)
PasswallAdept = Card(name="passwall_adept", pretty_name="Passwall Adept", cost=['1', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                     abilities=[101336], set_id="GRN", rarity="Common", set_number=50,
                     mtga_id=68511)
Quasiduplicate = Card(name="quasiduplicate", pretty_name="Quasiduplicate", cost=['1', 'U', 'U'],
                      color_identity=['U'], card_type="Sorcery", sub_types="",
                      abilities=[18554, 170], set_id="GRN", rarity="Rare", set_number=51,
                      mtga_id=68512)
RadicalIdea = Card(name="radical_idea", pretty_name="Radical Idea", cost=['1', 'U'],
                   color_identity=['U'], card_type="Instant", sub_types="",
                   abilities=[25848, 170], set_id="GRN", rarity="Common", set_number=52,
                   mtga_id=68513)
SelectiveSnare = Card(name="selective_snare", pretty_name="Selective Snare", cost=['X', 'U'],
                      color_identity=['U'], card_type="Sorcery", sub_types="",
                      abilities=[121416], set_id="GRN", rarity="Uncommon", set_number=53,
                      mtga_id=68514)
SinisterSabotage = Card(name="sinister_sabotage", pretty_name="Sinister Sabotage", cost=['1', 'U', 'U'],
                        color_identity=['U'], card_type="Instant", sub_types="",
                        abilities=[25846, 121425], set_id="GRN", rarity="Uncommon", set_number=54,
                        mtga_id=68515)
ThoughtboundPhantasm = Card(name="thoughtbound_phantasm", pretty_name="Thoughtbound Phantasm", cost=['U'],
                            color_identity=['U'], card_type="Creature", sub_types="Spirit",
                            abilities=[2, 121430, 121434], set_id="GRN", rarity="Uncommon", set_number=55,
                            mtga_id=68516)
UnexplainedDisappearance = Card(name="unexplained_disappearance", pretty_name="Unexplained Disappearance", cost=['1', 'U'],
                                color_identity=['U'], card_type="Instant", sub_types="",
                                abilities=[22505, 121425], set_id="GRN", rarity="Common", set_number=56,
                                mtga_id=68517)
VedalkenMesmerist = Card(name="vedalken_mesmerist", pretty_name="Vedalken Mesmerist", cost=['1', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Vedalken Wizard",
                         abilities=[121442], set_id="GRN", rarity="Common", set_number=57,
                         mtga_id=68518)
WallofMist = Card(name="wall_of_mist", pretty_name="Wall of Mist", cost=['1', 'U'],
                  color_identity=['U'], card_type="Creature", sub_types="Wall",
                  abilities=[2], set_id="GRN", rarity="Common", set_number=58,
                  mtga_id=68519)
WatcherintheMist = Card(name="watcher_in_the_mist", pretty_name="Watcher in the Mist", cost=['3', 'U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Spirit",
                        abilities=[8, 121357], set_id="GRN", rarity="Common", set_number=59,
                        mtga_id=68520)
WishcoinCrab = Card(name="wishcoin_crab", pretty_name="Wishcoin Crab", cost=['3', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Crab",
                    abilities=[], set_id="GRN", rarity="Common", set_number=60,
                    mtga_id=68521)
BarrierofBones = Card(name="barrier_of_bones", pretty_name="Barrier of Bones", cost=['B'],
                      color_identity=['B'], card_type="Creature", sub_types="Skeleton Wall",
                      abilities=[2, 121445], set_id="GRN", rarity="Common", set_number=61,
                      mtga_id=68522)
BartizanBats = Card(name="bartizan_bats", pretty_name="Bartizan Bats", cost=['3', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Bat",
                    abilities=[8], set_id="GRN", rarity="Common", set_number=62,
                    mtga_id=68523)
BloodOperative = Card(name="blood_operative", pretty_name="Blood Operative", cost=['1', 'B', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Vampire Assassin",
                      abilities=[12, 121450, 121454], set_id="GRN", rarity="Rare", set_number=63,
                      mtga_id=68524)
BurglarRat = Card(name="burglar_rat", pretty_name="Burglar Rat", cost=['1', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Rat",
                  abilities=[92927], set_id="GRN", rarity="Common", set_number=64,
                  mtga_id=68525)
ChildofNight = Card(name="child_of_night", pretty_name="Child of Night", cost=['1', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Vampire",
                    abilities=[12], set_id="GRN", rarity="Common", set_number=65,
                    mtga_id=68526)
CreepingChill = Card(name="creeping_chill", pretty_name="Creeping Chill", cost=['3', 'B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[121462, 121463], set_id="GRN", rarity="Uncommon", set_number=66,
                     mtga_id=68527)
DeadWeight = Card(name="dead_weight", pretty_name="Dead Weight", cost=['B'],
                  color_identity=['B'], card_type="Enchantment", sub_types="Aura",
                  abilities=[1027, 7138], set_id="GRN", rarity="Common", set_number=67,
                  mtga_id=68528)
DeadlyVisit = Card(name="deadly_visit", pretty_name="Deadly Visit", cost=['3', 'B', 'B'],
                   color_identity=['B'], card_type="Sorcery", sub_types="",
                   abilities=[26818, 121353], set_id="GRN", rarity="Common", set_number=68,
                   mtga_id=68529)
DoomWhisperer = Card(name="doom_whisperer", pretty_name="Doom Whisperer", cost=['3', 'B', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Nightmare Demon",
                     abilities=[8, 14, 121466], set_id="GRN", rarity="Mythic Rare", set_number=69,
                     mtga_id=68530)
DouserofLights = Card(name="douser_of_lights", pretty_name="Douser of Lights", cost=['4', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Horror",
                      abilities=[], set_id="GRN", rarity="Common", set_number=70,
                      mtga_id=68531)
GruesomeMenagerie = Card(name="gruesome_menagerie", pretty_name="Gruesome Menagerie", cost=['3', 'B', 'B'],
                         color_identity=['B'], card_type="Sorcery", sub_types="",
                         abilities=[121467], set_id="GRN", rarity="Rare", set_number=71,
                         mtga_id=68532)
HiredPoisoner = Card(name="hired_poisoner", pretty_name="Hired Poisoner", cost=['B'],
                     color_identity=['B'], card_type="Creature", sub_types="Human Assassin",
                     abilities=[1], set_id="GRN", rarity="Common", set_number=72,
                     mtga_id=68533)
KraulSwarm = Card(name="kraul_swarm", pretty_name="Kraul Swarm", cost=['4', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Insect Warrior",
                  abilities=[8, 121468], set_id="GRN", rarity="Uncommon", set_number=73,
                  mtga_id=68534)
LotlethGiant = Card(name="lotleth_giant", pretty_name="Lotleth Giant", cost=['6', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Zombie Giant",
                    abilities=[121469], set_id="GRN", rarity="Uncommon", set_number=74,
                    mtga_id=68535)
MausoleumSecrets = Card(name="mausoleum_secrets", pretty_name="Mausoleum Secrets", cost=['1', 'B'],
                        color_identity=['B'], card_type="Instant", sub_types="",
                        abilities=[121472], set_id="GRN", rarity="Rare", set_number=75,
                        mtga_id=68536)
MephiticVapors = Card(name="mephitic_vapors", pretty_name="Mephitic Vapors", cost=['2', 'B'],
                      color_identity=['B'], card_type="Sorcery", sub_types="",
                      abilities=[30056, 121353], set_id="GRN", rarity="Common", set_number=76,
                      mtga_id=68537)
MidnightReaper = Card(name="midnight_reaper", pretty_name="Midnight Reaper", cost=['2', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Zombie Knight",
                      abilities=[121475], set_id="GRN", rarity="Rare", set_number=77,
                      mtga_id=68538)
MoodmarkPainter = Card(name="moodmark_painter", pretty_name="Moodmark Painter", cost=['2', 'B', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Human Shaman",
                       abilities=[121476], set_id="GRN", rarity="Common", set_number=78,
                       mtga_id=68539)
NecroticWound = Card(name="necrotic_wound", pretty_name="Necrotic Wound", cost=['B'],
                     color_identity=['B'], card_type="Instant", sub_types="",
                     abilities=[121477], set_id="GRN", rarity="Uncommon", set_number=79,
                     mtga_id=68540)
NeverHappened = Card(name="never_happened", pretty_name="Never Happened", cost=['2', 'B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[121478], set_id="GRN", rarity="Common", set_number=80,
                     mtga_id=68541)
PilferingImp = Card(name="pilfering_imp", pretty_name="Pilfering Imp", cost=['B'],
                    color_identity=['B'], card_type="Creature", sub_types="Imp",
                    abilities=[8, 121479], set_id="GRN", rarity="Uncommon", set_number=81,
                    mtga_id=68542)
Plaguecrafter = Card(name="plaguecrafter", pretty_name="Plaguecrafter", cost=['2', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Human Shaman",
                     abilities=[121480], set_id="GRN", rarity="Uncommon", set_number=82,
                     mtga_id=68543)
PriceofFame = Card(name="price_of_fame", pretty_name="Price of Fame", cost=['3', 'B'],
                   color_identity=['B'], card_type="Instant", sub_types="",
                   abilities=[121482, 26818, 121353], set_id="GRN", rarity="Uncommon", set_number=83,
                   mtga_id=68544)
RitualofSoot = Card(name="ritual_of_soot", pretty_name="Ritual of Soot", cost=['2', 'B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[24394], set_id="GRN", rarity="Rare", set_number=84,
                    mtga_id=68545)
SeveredStrands = Card(name="severed_strands", pretty_name="Severed Strands", cost=['1', 'B'],
                      color_identity=['B'], card_type="Sorcery", sub_types="",
                      abilities=[1275, 121483], set_id="GRN", rarity="Common", set_number=85,
                      mtga_id=68546)
SpinalCentipede = Card(name="spinal_centipede", pretty_name="Spinal Centipede", cost=['2', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Insect",
                       abilities=[87008], set_id="GRN", rarity="Common", set_number=86,
                       mtga_id=68547)
UndercityNecrolisk = Card(name="undercity_necrolisk", pretty_name="Undercity Necrolisk", cost=['3', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Zombie Lizard",
                          abilities=[121484], set_id="GRN", rarity="Uncommon", set_number=87,
                          mtga_id=68548)
VeiledShade = Card(name="veiled_shade", pretty_name="Veiled Shade", cost=['2', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Shade",
                   abilities=[76746], set_id="GRN", rarity="Common", set_number=88,
                   mtga_id=68549)
ViciousRumors = Card(name="vicious_rumors", pretty_name="Vicious Rumors", cost=['B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[121486], set_id="GRN", rarity="Common", set_number=89,
                     mtga_id=68550)
WhisperingSnitch = Card(name="whispering_snitch", pretty_name="Whispering Snitch", cost=['1', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Vampire Rogue",
                        abilities=[121488], set_id="GRN", rarity="Uncommon", set_number=90,
                        mtga_id=68551)
ArclightPhoenix = Card(name="arclight_phoenix", pretty_name="Arclight Phoenix", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Phoenix",
                       abilities=[8, 9, 121489], set_id="GRN", rarity="Mythic Rare", set_number=91,
                       mtga_id=68552)
BargingSergeant = Card(name="barging_sergeant", pretty_name="Barging Sergeant", cost=['4', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Minotaur Soldier",
                       abilities=[9, 171], set_id="GRN", rarity="Common", set_number=92,
                       mtga_id=68553)
BookDevourer = Card(name="book_devourer", pretty_name="Book Devourer", cost=['5', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Beast",
                    abilities=[14, 121491], set_id="GRN", rarity="Uncommon", set_number=93,
                    mtga_id=68554)
CommandtheStorm = Card(name="command_the_storm", pretty_name="Command the Storm", cost=['4', 'R'],
                       color_identity=['R'], card_type="Instant", sub_types="",
                       abilities=[13250], set_id="GRN", rarity="Common", set_number=94,
                       mtga_id=68555)
CosmotronicWave = Card(name="cosmotronic_wave", pretty_name="Cosmotronic Wave", cost=['3', 'R'],
                       color_identity=['R'], card_type="Sorcery", sub_types="",
                       abilities=[121493], set_id="GRN", rarity="Common", set_number=95,
                       mtga_id=68556)
DirectCurrent = Card(name="direct_current", pretty_name="Direct Current", cost=['1', 'R', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[86613, 170], set_id="GRN", rarity="Common", set_number=96,
                     mtga_id=68557)
ElectrostaticField = Card(name="electrostatic_field", pretty_name="Electrostatic Field", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Wall",
                          abilities=[2, 121494], set_id="GRN", rarity="Uncommon", set_number=97,
                          mtga_id=68558)
ErraticCyclops = Card(name="erratic_cyclops", pretty_name="Erratic Cyclops", cost=['3', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Cyclops Shaman",
                      abilities=[14, 121495], set_id="GRN", rarity="Rare", set_number=98,
                      mtga_id=68559)
ExperimentalFrenzy = Card(name="experimental_frenzy", pretty_name="Experimental Frenzy", cost=['3', 'R'],
                          color_identity=['R'], card_type="Enchantment", sub_types="",
                          abilities=[14523, 3396, 1107, 121499], set_id="GRN", rarity="Rare", set_number=99,
                          mtga_id=68560)
FearlessHalberdier = Card(name="fearless_halberdier", pretty_name="Fearless Halberdier", cost=['2', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                          abilities=[], set_id="GRN", rarity="Common", set_number=100,
                          mtga_id=68561)
FireUrchin = Card(name="fire_urchin", pretty_name="Fire Urchin", cost=['1', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Elemental",
                  abilities=[14, 121500], set_id="GRN", rarity="Common", set_number=101,
                  mtga_id=68562)
GoblinBanneret = Card(name="goblin_banneret", pretty_name="Goblin Banneret", cost=['R'],
                      color_identity=['R'], card_type="Creature", sub_types="Goblin Soldier",
                      abilities=[171, 76843], set_id="GRN", rarity="Uncommon", set_number=102,
                      mtga_id=68563)
GoblinCratermaker = Card(name="goblin_cratermaker", pretty_name="Goblin Cratermaker", cost=['1', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                         abilities=[121505], set_id="GRN", rarity="Uncommon", set_number=103,
                         mtga_id=68564)
GoblinLocksmith = Card(name="goblin_locksmith", pretty_name="Goblin Locksmith", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Goblin Rogue",
                       abilities=[121506], set_id="GRN", rarity="Common", set_number=104,
                       mtga_id=68565)
GraviticPunch = Card(name="gravitic_punch", pretty_name="Gravitic Punch", cost=['3', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[121507, 170], set_id="GRN", rarity="Common", set_number=105,
                     mtga_id=68566)
HellkiteWhelp = Card(name="hellkite_whelp", pretty_name="Hellkite Whelp", cost=['4', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Dragon",
                     abilities=[8, 121508], set_id="GRN", rarity="Uncommon", set_number=106,
                     mtga_id=68567)
InescapableBlaze = Card(name="inescapable_blaze", pretty_name="Inescapable Blaze", cost=['4', 'R', 'R'],
                        color_identity=['R'], card_type="Instant", sub_types="",
                        abilities=[120287, 121510], set_id="GRN", rarity="Uncommon", set_number=107,
                        mtga_id=68568)
LavaCoil = Card(name="lava_coil", pretty_name="Lava Coil", cost=['1', 'R'],
                color_identity=['R'], card_type="Sorcery", sub_types="",
                abilities=[121512], set_id="GRN", rarity="Uncommon", set_number=108,
                mtga_id=68569)
LegionWarboss = Card(name="legion_warboss", pretty_name="Legion Warboss", cost=['2', 'R'],
                     color_identity=['R'], card_type="Creature", sub_types="Goblin Soldier",
                     abilities=[171, 121513], set_id="GRN", rarity="Rare", set_number=109,
                     mtga_id=68570)
ManiacalRage = Card(name="maniacal_rage", pretty_name="Maniacal Rage", cost=['1', 'R'],
                    color_identity=['R'], card_type="Enchantment", sub_types="Aura",
                    abilities=[1027, 90333], set_id="GRN", rarity="Common", set_number=110,
                    mtga_id=68571)
MaximizeVelocity = Card(name="maximize_velocity", pretty_name="Maximize Velocity", cost=['R'],
                        color_identity=['R'], card_type="Sorcery", sub_types="",
                        abilities=[121514, 170], set_id="GRN", rarity="Common", set_number=111,
                        mtga_id=68572)
OrneryGoblin = Card(name="ornery_goblin", pretty_name="Ornery Goblin", cost=['1', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                    abilities=[99455], set_id="GRN", rarity="Common", set_number=112,
                    mtga_id=68573)
RiskFactor = Card(name="risk_factor", pretty_name="Risk Factor", cost=['2', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[121515, 170], set_id="GRN", rarity="Rare", set_number=113,
                  mtga_id=68574)
RubblebeltBoar = Card(name="rubblebelt_boar", pretty_name="Rubblebelt Boar", cost=['3', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Boar",
                      abilities=[94974], set_id="GRN", rarity="Common", set_number=114,
                      mtga_id=68575)
RunawaySteamKin = Card(name="runaway_steamkin", pretty_name="Runaway Steam-Kin", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Elemental",
                       abilities=[121516, 121517], set_id="GRN", rarity="Rare", set_number=115,
                       mtga_id=68576)
SmeltWardMinotaur = Card(name="smeltward_minotaur", pretty_name="Smelt-Ward Minotaur", cost=['2', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Minotaur Warrior",
                         abilities=[121518], set_id="GRN", rarity="Uncommon", set_number=116,
                         mtga_id=68577)
StreetRiot = Card(name="street_riot", pretty_name="Street Riot", cost=['4', 'R'],
                  color_identity=['R'], card_type="Enchantment", sub_types="",
                  abilities=[121519], set_id="GRN", rarity="Uncommon", set_number=117,
                  mtga_id=68578)
SureStrike = Card(name="sure_strike", pretty_name="Sure Strike", cost=['1', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[1019], set_id="GRN", rarity="Common", set_number=118,
                  mtga_id=68579)
TorchCourier = Card(name="torch_courier", pretty_name="Torch Courier", cost=['R'],
                    color_identity=['R'], card_type="Creature", sub_types="Goblin",
                    abilities=[9, 121355], set_id="GRN", rarity="Common", set_number=119,
                    mtga_id=68580)
WojekBodyguard = Card(name="wojek_bodyguard", pretty_name="Wojek Bodyguard", cost=['2', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Human Soldier",
                      abilities=[171, 87894], set_id="GRN", rarity="Common", set_number=120,
                      mtga_id=68581)
AffectionateIndrik = Card(name="affectionate_indrik", pretty_name="Affectionate Indrik", cost=['5', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Beast",
                          abilities=[102099], set_id="GRN", rarity="Uncommon", set_number=121,
                          mtga_id=68582)
ArboretumElemental = Card(name="arboretum_elemental", pretty_name="Arboretum Elemental", cost=['7', 'G', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Elemental",
                          abilities=[52, 10], set_id="GRN", rarity="Uncommon", set_number=122,
                          mtga_id=68583)
BeastWhisperer = Card(name="beast_whisperer", pretty_name="Beast Whisperer", cost=['2', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                      abilities=[62610], set_id="GRN", rarity="Rare", set_number=123,
                      mtga_id=68584)
BountyofMight = Card(name="bounty_of_might", pretty_name="Bounty of Might", cost=['4', 'G', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[24733, 24733, 24733], set_id="GRN", rarity="Rare", set_number=124,
                     mtga_id=68585)
CircuitousRoute = Card(name="circuitous_route", pretty_name="Circuitous Route", cost=['3', 'G'],
                       color_identity=['G'], card_type="Sorcery", sub_types="",
                       abilities=[121356], set_id="GRN", rarity="Uncommon", set_number=125,
                       mtga_id=68586)
CrushingCanopy = Card(name="crushing_canopy", pretty_name="Crushing Canopy", cost=['2', 'G'],
                      color_identity=['G'], card_type="Instant", sub_types="",
                      abilities=[1206], set_id="GRN", rarity="Common", set_number=126,
                      mtga_id=68587)
DevkarinDissident = Card(name="devkarin_dissident", pretty_name="Devkarin Dissident", cost=['1', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Warrior",
                         abilities=[121358], set_id="GRN", rarity="Common", set_number=127,
                         mtga_id=68588)
DistrictGuide = Card(name="district_guide", pretty_name="District Guide", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                     abilities=[121359], set_id="GRN", rarity="Uncommon", set_number=128,
                     mtga_id=68589)
GenerousStray = Card(name="generous_stray", pretty_name="Generous Stray", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Cat",
                     abilities=[86788], set_id="GRN", rarity="Common", set_number=129,
                     mtga_id=68590)
GolgariRaiders = Card(name="golgari_raiders", pretty_name="Golgari Raiders", cost=['3', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Elf Warrior",
                      abilities=[9, 121360], set_id="GRN", rarity="Uncommon", set_number=130,
                      mtga_id=68591)
GrapplingSundew = Card(name="grappling_sundew", pretty_name="Grappling Sundew", cost=['1', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Plant",
                       abilities=[2, 13, 121361], set_id="GRN", rarity="Uncommon", set_number=131,
                       mtga_id=68592)
HatcherySpider = Card(name="hatchery_spider", pretty_name="Hatchery Spider", cost=['5', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Spider",
                      abilities=[13, 121362], set_id="GRN", rarity="Rare", set_number=132,
                      mtga_id=68593)
HitchclawRecluse = Card(name="hitchclaw_recluse", pretty_name="Hitchclaw Recluse", cost=['2', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Spider",
                        abilities=[13], set_id="GRN", rarity="Common", set_number=133,
                        mtga_id=68594)
IronshellBeetle = Card(name="ironshell_beetle", pretty_name="Ironshell Beetle", cost=['1', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Insect",
                       abilities=[92425], set_id="GRN", rarity="Common", set_number=134,
                       mtga_id=68595)
KraulForagers = Card(name="kraul_foragers", pretty_name="Kraul Foragers", cost=['4', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Insect Scout",
                     abilities=[121526], set_id="GRN", rarity="Common", set_number=135,
                     mtga_id=68596)
KraulHarpooner = Card(name="kraul_harpooner", pretty_name="Kraul Harpooner", cost=['1', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Insect Warrior",
                      abilities=[13, 121527], set_id="GRN", rarity="Uncommon", set_number=136,
                      mtga_id=68597)
MightoftheMasses = Card(name="might_of_the_masses", pretty_name="Might of the Masses", cost=['G'],
                        color_identity=['G'], card_type="Instant", sub_types="",
                        abilities=[9094], set_id="GRN", rarity="Uncommon", set_number=137,
                        mtga_id=68598)
NullhideFerox = Card(name="nullhide_ferox", pretty_name="Nullhide Ferox", cost=['2', 'G', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Beast",
                     abilities=[10, 121529, 121530, 92976], set_id="GRN", rarity="Mythic Rare", set_number=138,
                     mtga_id=68599)
PacksFavor = Card(name="packs_favor", pretty_name="Pack's Favor", cost=['2', 'G'],
                  color_identity=['G'], card_type="Instant", sub_types="",
                  abilities=[52, 24733], set_id="GRN", rarity="Common", set_number=139,
                  mtga_id=68600)
PauseforReflection = Card(name="pause_for_reflection", pretty_name="Pause for Reflection", cost=['2', 'G'],
                          color_identity=['G'], card_type="Instant", sub_types="",
                          abilities=[52, 27746], set_id="GRN", rarity="Common", set_number=140,
                          mtga_id=68601)
PeltCollector = Card(name="pelt_collector", pretty_name="Pelt Collector", cost=['G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Warrior",
                     abilities=[121532, 121533], set_id="GRN", rarity="Rare", set_number=141,
                     mtga_id=68602)
PortcullisVine = Card(name="portcullis_vine", pretty_name="Portcullis Vine", cost=['G'],
                      color_identity=['G'], card_type="Creature", sub_types="Plant Wall",
                      abilities=[2, 121363], set_id="GRN", rarity="Common", set_number=142,
                      mtga_id=68603)
PreyUpon = Card(name="prey_upon", pretty_name="Prey Upon", cost=['G'],
                color_identity=['G'], card_type="Sorcery", sub_types="",
                abilities=[99356], set_id="GRN", rarity="Common", set_number=143,
                mtga_id=68604)
SiegeWurm = Card(name="siege_wurm", pretty_name="Siege Wurm", cost=['5', 'G', 'G'],
                 color_identity=['G'], card_type="Creature", sub_types="Wurm",
                 abilities=[52, 14], set_id="GRN", rarity="Common", set_number=144,
                 mtga_id=68605)
SproutingRenewal = Card(name="sprouting_renewal", pretty_name="Sprouting Renewal", cost=['2', 'G'],
                        color_identity=['G'], card_type="Sorcery", sub_types="",
                        abilities=[52, 121536], set_id="GRN", rarity="Uncommon", set_number=145,
                        mtga_id=68606)
UrbanUtopia = Card(name="urban_utopia", pretty_name="Urban Utopia", cost=['1', 'G'],
                   color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                   abilities=[1570, 86788, 99704], set_id="GRN", rarity="Common", set_number=146,
                   mtga_id=68607)
VigorsporeWurm = Card(name="vigorspore_wurm", pretty_name="Vigorspore Wurm", cost=['5', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Wurm",
                      abilities=[121538, 1026], set_id="GRN", rarity="Common", set_number=147,
                      mtga_id=68608)
VividRevival = Card(name="vivid_revival", pretty_name="Vivid Revival", cost=['4', 'G'],
                    color_identity=['G'], card_type="Sorcery", sub_types="",
                    abilities=[121366], set_id="GRN", rarity="Rare", set_number=148,
                    mtga_id=68609)
WaryOkapi = Card(name="wary_okapi", pretty_name="Wary Okapi", cost=['2', 'G'],
                 color_identity=['G'], card_type="Creature", sub_types="Antelope",
                 abilities=[15], set_id="GRN", rarity="Common", set_number=149,
                 mtga_id=68610)
WildCeratok = Card(name="wild_ceratok", pretty_name="Wild Ceratok", cost=['3', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Rhino",
                   abilities=[], set_id="GRN", rarity="Common", set_number=150,
                   mtga_id=68611)
ArtfulTakedown = Card(name="artful_takedown", pretty_name="Artful Takedown", cost=['2', 'U', 'B'],
                      color_identity=['U', 'B'], card_type="Instant", sub_types="",
                      abilities=[121541], set_id="GRN", rarity="Common", set_number=151,
                      mtga_id=68612)
AssassinsTrophy = Card(name="assassins_trophy", pretty_name="Assassin's Trophy", cost=['B', 'G'],
                       color_identity=['B', 'G'], card_type="Instant", sub_types="",
                       abilities=[121542], set_id="GRN", rarity="Rare", set_number=152,
                       mtga_id=68613)
AureliaExemplarofJustice = Card(name="aurelia_exemplar_of_justice", pretty_name="Aurelia, Exemplar of Justice", cost=['2', 'R', 'W'],
                                color_identity=['R', 'W'], card_type="Creature", sub_types="Angel",
                                abilities=[8, 171, 121367], set_id="GRN", rarity="Mythic Rare", set_number=153,
                                mtga_id=68614)
BeaconBolt = Card(name="beacon_bolt", pretty_name="Beacon Bolt", cost=['1', 'U', 'R'],
                  color_identity=['U', 'R'], card_type="Sorcery", sub_types="",
                  abilities=[121543, 170], set_id="GRN", rarity="Uncommon", set_number=154,
                  mtga_id=68615)
BeamsplitterMage = Card(name="beamsplitter_mage", pretty_name="Beamsplitter Mage", cost=['U', 'R'],
                        color_identity=['U', 'R'], card_type="Creature", sub_types="Vedalken Wizard",
                        abilities=[121544], set_id="GRN", rarity="Uncommon", set_number=155,
                        mtga_id=68616)
BorosChallenger = Card(name="boros_challenger", pretty_name="Boros Challenger", cost=['R', 'W'],
                       color_identity=['R', 'W'], card_type="Creature", sub_types="Human Soldier",
                       abilities=[171, 121546], set_id="GRN", rarity="Uncommon", set_number=156,
                       mtga_id=68617)
Camaraderie = Card(name="camaraderie", pretty_name="Camaraderie", cost=['4', 'G', 'W'],
                   color_identity=['G', 'W'], card_type="Sorcery", sub_types="",
                   abilities=[121490], set_id="GRN", rarity="Rare", set_number=157,
                   mtga_id=68618)
CentaurPeacemaker = Card(name="centaur_peacemaker", pretty_name="Centaur Peacemaker", cost=['1', 'G', 'W'],
                         color_identity=['G', 'W'], card_type="Creature", sub_types="Centaur Cleric",
                         abilities=[121547], set_id="GRN", rarity="Common", set_number=158,
                         mtga_id=68619)
ChanceforGlory = Card(name="chance_for_glory", pretty_name="Chance for Glory", cost=['1', 'R', 'W'],
                      color_identity=['R', 'W'], card_type="Instant", sub_types="",
                      abilities=[121548], set_id="GRN", rarity="Mythic Rare", set_number=159,
                      mtga_id=68620)
CharnelTroll = Card(name="charnel_troll", pretty_name="Charnel Troll", cost=['1', 'B', 'G'],
                    color_identity=['B', 'G'], card_type="Creature", sub_types="Troll",
                    abilities=[14, 121549, 121550], set_id="GRN", rarity="Rare", set_number=160,
                    mtga_id=68621)
ConclaveCavalier = Card(name="conclave_cavalier", pretty_name="Conclave Cavalier", cost=['G', 'G', 'W', 'W'],
                        color_identity=['G', 'W'], card_type="Creature", sub_types="Centaur Knight",
                        abilities=[15, 121368], set_id="GRN", rarity="Uncommon", set_number=161,
                        mtga_id=68622)
ConclaveGuildmage = Card(name="conclave_guildmage", pretty_name="Conclave Guildmage", cost=['G', 'W'],
                         color_identity=['G', 'W'], card_type="Creature", sub_types="Elf Cleric",
                         abilities=[121552, 121553], set_id="GRN", rarity="Uncommon", set_number=162,
                         mtga_id=68623)
CracklingDrake = Card(name="crackling_drake", pretty_name="Crackling Drake", cost=['U', 'U', 'R', 'R'],
                      color_identity=['U', 'R'], card_type="Creature", sub_types="Drake",
                      abilities=[8, 121554, 86788], set_id="GRN", rarity="Uncommon", set_number=163,
                      mtga_id=68624)
DarkbladeAgent = Card(name="darkblade_agent", pretty_name="Darkblade Agent", cost=['1', 'U', 'B'],
                      color_identity=['U', 'B'], card_type="Creature", sub_types="Human Assassin",
                      abilities=[121556], set_id="GRN", rarity="Common", set_number=164,
                      mtga_id=68625)
DeafeningClarion = Card(name="deafening_clarion", pretty_name="Deafening Clarion", cost=['1', 'R', 'W'],
                        color_identity=['R', 'W'], card_type="Sorcery", sub_types="",
                        abilities=[121558], set_id="GRN", rarity="Rare", set_number=165,
                        mtga_id=68626)
DimirSpybug = Card(name="dimir_spybug", pretty_name="Dimir Spybug", cost=['U', 'B'],
                   color_identity=['U', 'B'], card_type="Creature", sub_types="Insect",
                   abilities=[8, 142, 121430], set_id="GRN", rarity="Uncommon", set_number=166,
                   mtga_id=68627)
DisinformationCampaign = Card(name="disinformation_campaign", pretty_name="Disinformation Campaign", cost=['1', 'U', 'B'],
                              color_identity=['U', 'B'], card_type="Enchantment", sub_types="",
                              abilities=[121559, 121560], set_id="GRN", rarity="Uncommon", set_number=167,
                              mtga_id=68628)
EmmaraSouloftheAccord = Card(name="emmara_soul_of_the_accord", pretty_name="Emmara, Soul of the Accord", cost=['G', 'W'],
                             color_identity=['G', 'W'], card_type="Creature", sub_types="Elf Cleric",
                             abilities=[121561], set_id="GRN", rarity="Rare", set_number=168,
                             mtga_id=68629)
ErstwhileTrooper = Card(name="erstwhile_trooper", pretty_name="Erstwhile Trooper", cost=['1', 'B', 'G'],
                        color_identity=['B', 'G'], card_type="Creature", sub_types="Zombie Soldier",
                        abilities=[121562], set_id="GRN", rarity="Common", set_number=169,
                        mtga_id=68630)
EtratatheSilencer = Card(name="etrata_the_silencer", pretty_name="Etrata, the Silencer", cost=['2', 'U', 'B'],
                         color_identity=['U', 'B'], card_type="Creature", sub_types="Vampire Assassin",
                         abilities=[62969, 121566], set_id="GRN", rarity="Rare", set_number=170,
                         mtga_id=68631)
FiremindsResearch = Card(name="fireminds_research", pretty_name="Firemind's Research", cost=['U', 'R'],
                         color_identity=['U', 'R'], card_type="Enchantment", sub_types="",
                         abilities=[121370, 121371, 121372], set_id="GRN", rarity="Rare", set_number=171,
                         mtga_id=68632)
GarrisonSergeant = Card(name="garrison_sergeant", pretty_name="Garrison Sergeant", cost=['3', 'R', 'W'],
                        color_identity=['R', 'W'], card_type="Creature", sub_types="Viashino Soldier",
                        abilities=[121373], set_id="GRN", rarity="Common", set_number=172,
                        mtga_id=68633)
GlowsporeShaman = Card(name="glowspore_shaman", pretty_name="Glowspore Shaman", cost=['B', 'G'],
                       color_identity=['B', 'G'], card_type="Creature", sub_types="Elf Shaman",
                       abilities=[121374], set_id="GRN", rarity="Uncommon", set_number=173,
                       mtga_id=68634)
GoblinElectromancer = Card(name="goblin_electromancer", pretty_name="Goblin Electromancer", cost=['U', 'R'],
                           color_identity=['U', 'R'], card_type="Creature", sub_types="Goblin Wizard",
                           abilities=[19445], set_id="GRN", rarity="Common", set_number=174,
                           mtga_id=68635)
GolgariFindbroker = Card(name="golgari_findbroker", pretty_name="Golgari Findbroker", cost=['B', 'B', 'G', 'G'],
                         color_identity=['B', 'G'], card_type="Creature", sub_types="Elf Shaman",
                         abilities=[121376], set_id="GRN", rarity="Uncommon", set_number=175,
                         mtga_id=68636)
HammerDropper = Card(name="hammer_dropper", pretty_name="Hammer Dropper", cost=['2', 'R', 'W'],
                     color_identity=['R', 'W'], card_type="Creature", sub_types="Giant Soldier",
                     abilities=[171], set_id="GRN", rarity="Common", set_number=176,
                     mtga_id=68637)
HouseGuildmage = Card(name="house_guildmage", pretty_name="House Guildmage", cost=['U', 'B'],
                      color_identity=['U', 'B'], card_type="Creature", sub_types="Human Wizard",
                      abilities=[121377, 121378], set_id="GRN", rarity="Uncommon", set_number=177,
                      mtga_id=68638)
Hypothesizzle = Card(name="hypothesizzle", pretty_name="Hypothesizzle", cost=['3', 'U', 'R'],
                     color_identity=['U', 'R'], card_type="Instant", sub_types="",
                     abilities=[121379], set_id="GRN", rarity="Common", set_number=178,
                     mtga_id=68639)
Ionize = Card(name="ionize", pretty_name="Ionize", cost=['1', 'U', 'R'],
              color_identity=['U', 'R'], card_type="Instant", sub_types="",
              abilities=[121380], set_id="GRN", rarity="Rare", set_number=179,
              mtga_id=68640)
IzoniThousandEyed = Card(name="izoni_thousandeyed", pretty_name="Izoni, Thousand-Eyed", cost=['2', 'B', 'B', 'G', 'G'],
                         color_identity=['B', 'G'], card_type="Creature", sub_types="Elf Shaman",
                         abilities=[121474, 121382], set_id="GRN", rarity="Rare", set_number=180,
                         mtga_id=68641)
JoinShields = Card(name="join_shields", pretty_name="Join Shields", cost=['3', 'G', 'W'],
                   color_identity=['G', 'W'], card_type="Instant", sub_types="",
                   abilities=[121383], set_id="GRN", rarity="Uncommon", set_number=181,
                   mtga_id=68642)
JusticeStrike = Card(name="justice_strike", pretty_name="Justice Strike", cost=['R', 'W'],
                     color_identity=['R', 'W'], card_type="Instant", sub_types="",
                     abilities=[12670], set_id="GRN", rarity="Uncommon", set_number=182,
                     mtga_id=68643)
KnightofAutumn = Card(name="knight_of_autumn", pretty_name="Knight of Autumn", cost=['1', 'G', 'W'],
                      color_identity=['G', 'W'], card_type="Creature", sub_types="Dryad Knight",
                      abilities=[121509], set_id="GRN", rarity="Rare", set_number=183,
                      mtga_id=68644)
LazavtheMultifarious = Card(name="lazav_the_multifarious", pretty_name="Lazav, the Multifarious", cost=['U', 'B'],
                            color_identity=['U', 'B'], card_type="Creature", sub_types="Shapeshifter",
                            abilities=[121445, 122112], set_id="GRN", rarity="Mythic Rare", set_number=184,
                            mtga_id=68645)
LeagueGuildmage = Card(name="league_guildmage", pretty_name="League Guildmage", cost=['U', 'R'],
                       color_identity=['U', 'R'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[8701, 121388], set_id="GRN", rarity="Uncommon", set_number=185,
                       mtga_id=68646)
LedevChampion = Card(name="ledev_champion", pretty_name="Ledev Champion", cost=['1', 'G', 'W'],
                     color_identity=['G', 'W'], card_type="Creature", sub_types="Elf Knight",
                     abilities=[121389, 121524], set_id="GRN", rarity="Uncommon", set_number=186,
                     mtga_id=68647)
LegionGuildmage = Card(name="legion_guildmage", pretty_name="Legion Guildmage", cost=['R', 'W'],
                       color_identity=['R', 'W'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[121390, 121391], set_id="GRN", rarity="Uncommon", set_number=187,
                       mtga_id=68648)
MarchoftheMultitudes = Card(name="march_of_the_multitudes", pretty_name="March of the Multitudes", cost=['X', 'G', 'W', 'W'],
                            color_identity=['G', 'W'], card_type="Instant", sub_types="",
                            abilities=[52, 121392], set_id="GRN", rarity="Mythic Rare", set_number=188,
                            mtga_id=68649)
MnemonicBetrayal = Card(name="mnemonic_betrayal", pretty_name="Mnemonic Betrayal", cost=['1', 'U', 'B'],
                        color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
                        abilities=[121393, 89260], set_id="GRN", rarity="Mythic Rare", set_number=189,
                        mtga_id=68650)
Molderhulk = Card(name="molderhulk", pretty_name="Molderhulk", cost=['7', 'B', 'G'],
                  color_identity=['B', 'G'], card_type="Creature", sub_types="Fungus Zombie",
                  abilities=[121545, 101750], set_id="GRN", rarity="Uncommon", set_number=190,
                  mtga_id=68651)
NightveilPredator = Card(name="nightveil_predator", pretty_name="Nightveil Predator", cost=['U', 'U', 'B', 'B'],
                         color_identity=['U', 'B'], card_type="Creature", sub_types="Vampire",
                         abilities=[8, 1, 10], set_id="GRN", rarity="Uncommon", set_number=191,
                         mtga_id=68652)
NivMizzetParun = Card(name="nivmizzet_parun", pretty_name="Niv-Mizzet, Parun", cost=['U', 'U', 'U', 'R', 'R', 'R'],
                      color_identity=['U', 'R'], card_type="Creature", sub_types="Dragon Wizard",
                      abilities=[120287, 8, 91091, 121395], set_id="GRN", rarity="Rare", set_number=192,
                      mtga_id=68653)
NotionRain = Card(name="notion_rain", pretty_name="Notion Rain", cost=['1', 'U', 'B'],
                  color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
                  abilities=[121396], set_id="GRN", rarity="Common", set_number=193,
                  mtga_id=68654)
OchranAssassin = Card(name="ochran_assassin", pretty_name="Ochran Assassin", cost=['1', 'B', 'G'],
                      color_identity=['B', 'G'], card_type="Creature", sub_types="Elf Assassin",
                      abilities=[1, 88808], set_id="GRN", rarity="Uncommon", set_number=194,
                      mtga_id=68655)
RalIzzetViceroy = Card(name="ral_izzet_viceroy", pretty_name="Ral, Izzet Viceroy", cost=['3', 'U', 'R'],
                       color_identity=['U', 'R'], card_type="Planeswalker", sub_types="Ral",
                       abilities=[121399, 121398, 121400], set_id="GRN", rarity="Mythic Rare", set_number=195,
                       mtga_id=68656)
RhizomeLurcher = Card(name="rhizome_lurcher", pretty_name="Rhizome Lurcher", cost=['2', 'B', 'G'],
                      color_identity=['B', 'G'], card_type="Creature", sub_types="Fungus Zombie",
                      abilities=[121401], set_id="GRN", rarity="Common", set_number=196,
                      mtga_id=68657)
RosemaneCentaur = Card(name="rosemane_centaur", pretty_name="Rosemane Centaur", cost=['3', 'G', 'W'],
                       color_identity=['G', 'W'], card_type="Creature", sub_types="Centaur Soldier",
                       abilities=[52, 15], set_id="GRN", rarity="Common", set_number=197,
                       mtga_id=68658)
SkyknightLegionnaire = Card(name="skyknight_legionnaire", pretty_name="Skyknight Legionnaire", cost=['1', 'R', 'W'],
                            color_identity=['R', 'W'], card_type="Creature", sub_types="Human Knight",
                            abilities=[8, 9], set_id="GRN", rarity="Common", set_number=198,
                            mtga_id=68659)
SonicAssault = Card(name="sonic_assault", pretty_name="Sonic Assault", cost=['1', 'U', 'R'],
                    color_identity=['U', 'R'], card_type="Instant", sub_types="",
                    abilities=[121402, 170], set_id="GRN", rarity="Common", set_number=199,
                    mtga_id=68660)
SumalaWoodshaper = Card(name="sumala_woodshaper", pretty_name="Sumala Woodshaper", cost=['2', 'G', 'W'],
                        color_identity=['G', 'W'], card_type="Creature", sub_types="Elf Druid",
                        abilities=[121427], set_id="GRN", rarity="Common", set_number=200,
                        mtga_id=68661)
SwarmGuildmage = Card(name="swarm_guildmage", pretty_name="Swarm Guildmage", cost=['B', 'G'],
                      color_identity=['B', 'G'], card_type="Creature", sub_types="Elf Shaman",
                      abilities=[121403, 121404], set_id="GRN", rarity="Uncommon", set_number=201,
                      mtga_id=68662)
SwathcutterGiant = Card(name="swathcutter_giant", pretty_name="Swathcutter Giant", cost=['4', 'R', 'W'],
                        color_identity=['R', 'W'], card_type="Creature", sub_types="Giant Soldier",
                        abilities=[15, 121405], set_id="GRN", rarity="Uncommon", set_number=202,
                        mtga_id=68663)
SwiftbladeVindicator = Card(name="swiftblade_vindicator", pretty_name="Swiftblade Vindicator", cost=['R', 'W'],
                            color_identity=['R', 'W'], card_type="Creature", sub_types="Human Soldier",
                            abilities=[3, 15, 14], set_id="GRN", rarity="Rare", set_number=203,
                            mtga_id=68664)
TajicLegionsEdge = Card(name="tajic_legions_edge", pretty_name="Tajic, Legion's Edge", cost=['1', 'R', 'W'],
                        color_identity=['R', 'W'], card_type="Creature", sub_types="Human Soldier",
                        abilities=[9, 171, 121406, 100360], set_id="GRN", rarity="Rare", set_number=204,
                        mtga_id=68665)
ThiefofSanity = Card(name="thief_of_sanity", pretty_name="Thief of Sanity", cost=['1', 'U', 'B'],
                     color_identity=['U', 'B'], card_type="Creature", sub_types="Specter",
                     abilities=[8, 121452], set_id="GRN", rarity="Rare", set_number=205,
                     mtga_id=68666)
ThoughtErasure = Card(name="thought_erasure", pretty_name="Thought Erasure", cost=['U', 'B'],
                      color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
                      abilities=[117067, 121425], set_id="GRN", rarity="Uncommon", set_number=206,
                      mtga_id=68667)
ThousandYearStorm = Card(name="thousandyear_storm", pretty_name="Thousand-Year Storm", cost=['4', 'U', 'R'],
                         color_identity=['U', 'R'], card_type="Enchantment", sub_types="",
                         abilities=[121458], set_id="GRN", rarity="Mythic Rare", set_number=207,
                         mtga_id=68668)
TrostaniDiscordant = Card(name="trostani_discordant", pretty_name="Trostani Discordant", cost=['3', 'G', 'W'],
                          color_identity=['G', 'W'], card_type="Creature", sub_types="Dryad",
                          abilities=[2433, 121409, 121410], set_id="GRN", rarity="Mythic Rare", set_number=208,
                          mtga_id=68669)
TruefireCaptain = Card(name="truefire_captain", pretty_name="Truefire Captain", cost=['R', 'R', 'W', 'W'],
                       color_identity=['R', 'W'], card_type="Creature", sub_types="Human Knight",
                       abilities=[171, 121465], set_id="GRN", rarity="Uncommon", set_number=209,
                       mtga_id=68670)
UndercityUprising = Card(name="undercity_uprising", pretty_name="Undercity Uprising", cost=['2', 'B', 'G'],
                         color_identity=['B', 'G'], card_type="Sorcery", sub_types="",
                         abilities=[121411], set_id="GRN", rarity="Common", set_number=210,
                         mtga_id=68671)
UnderrealmLich = Card(name="underrealm_lich", pretty_name="Underrealm Lich", cost=['3', 'B', 'G'],
                      color_identity=['B', 'G'], card_type="Creature", sub_types="Zombie Elf Shaman",
                      abilities=[121412, 121413], set_id="GRN", rarity="Mythic Rare", set_number=211,
                      mtga_id=68672)
UnmooredEgo = Card(name="unmoored_ego", pretty_name="Unmoored Ego", cost=['1', 'U', 'B'],
                   color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
                   abilities=[121414], set_id="GRN", rarity="Rare", set_number=212,
                   mtga_id=68673)
VraskaGolgariQueen = Card(name="vraska_golgari_queen", pretty_name="Vraska, Golgari Queen", cost=['2', 'B', 'G'],
                          color_identity=['B', 'G'], card_type="Planeswalker", sub_types="Vraska",
                          abilities=[121415, 121473, 121418], set_id="GRN", rarity="Mythic Rare", set_number=213,
                          mtga_id=68674)
WeeDragonauts = Card(name="wee_dragonauts", pretty_name="Wee Dragonauts", cost=['1', 'U', 'R'],
                     color_identity=['U', 'R'], card_type="Creature", sub_types="Faerie Wizard",
                     abilities=[8, 91866], set_id="GRN", rarity="Uncommon", set_number=214,
                     mtga_id=68675)
WorldsoulColossus = Card(name="worldsoul_colossus", pretty_name="Worldsoul Colossus", cost=['X', 'G', 'W'],
                         color_identity=['G', 'W'], card_type="Creature", sub_types="Elemental",
                         abilities=[52, 76885], set_id="GRN", rarity="Uncommon", set_number=215,
                         mtga_id=68676)
FreshFacedRecruit = Card(name="freshfaced_recruit", pretty_name="Fresh-Faced Recruit", cost=['1', '(R/W)'],
                         color_identity=['R', 'W'], card_type="Creature", sub_types="Human Soldier",
                         abilities=[121419], set_id="GRN", rarity="Common", set_number=216,
                         mtga_id=68677)
PistonFistCyclops = Card(name="pistonfist_cyclops", pretty_name="Piston-Fist Cyclops", cost=['1', '(U/R)', '(U/R)'],
                         color_identity=['U', 'R'], card_type="Creature", sub_types="Cyclops",
                         abilities=[2, 121481], set_id="GRN", rarity="Common", set_number=217,
                         mtga_id=68678)
PitilessGorgon = Card(name="pitiless_gorgon", pretty_name="Pitiless Gorgon", cost=['1', '(B/G)', '(B/G)'],
                      color_identity=['B', 'G'], card_type="Creature", sub_types="Gorgon",
                      abilities=[1], set_id="GRN", rarity="Common", set_number=218,
                      mtga_id=68679)
VernadiShieldmate = Card(name="vernadi_shieldmate", pretty_name="Vernadi Shieldmate", cost=['1', '(G/W)'],
                         color_identity=['G', 'W'], card_type="Creature", sub_types="Human Soldier",
                         abilities=[15], set_id="GRN", rarity="Common", set_number=219,
                         mtga_id=68680)
WhisperAgent = Card(name="whisper_agent", pretty_name="Whisper Agent", cost=['1', '(U/B)', '(U/B)'],
                    color_identity=['U', 'B'], card_type="Creature", sub_types="Human Rogue",
                    abilities=[7, 121445], set_id="GRN", rarity="Common", set_number=220,
                    mtga_id=68681)
AssureAssemble = Card(name="assure__assemble", pretty_name="Assure // Assemble", cost=['(G/W)', '(G/W)', '4', 'G', 'W'],
                      color_identity=['W', 'G'], card_type="Instant Instant", sub_types="",
                      abilities=[121420, 121421], set_id="GRN", rarity="Rare", set_number=221,
                      mtga_id=68682)
Assure = Card(name="assure", pretty_name="Assure", cost=['(G/W)', '(G/W)'],
              color_identity=['G', 'W'], card_type="Instant", sub_types="",
              abilities=[121420], set_id="GRN", rarity="Rare", set_number=221,
              mtga_id=68683)
Assemble = Card(name="assemble", pretty_name="Assemble", cost=['4', 'G', 'W'],
                color_identity=['G', 'W'], card_type="Instant", sub_types="",
                abilities=[121421], set_id="GRN", rarity="Rare", set_number=221,
                mtga_id=68684)
ConniveConcoct = Card(name="connive__concoct", pretty_name="Connive // Concoct", cost=['2', '(U/B)', '(U/B)', '3', 'U', 'B'],
                      color_identity=['U', 'B'], card_type="Sorcery Sorcery", sub_types="",
                      abilities=[121422, 121423], set_id="GRN", rarity="Rare", set_number=222,
                      mtga_id=68685)
Connive = Card(name="connive", pretty_name="Connive", cost=['2', '(U/B)', '(U/B)'],
               color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
               abilities=[121422], set_id="GRN", rarity="Rare", set_number=222,
               mtga_id=68686)
Concoct = Card(name="concoct", pretty_name="Concoct", cost=['3', 'U', 'B'],
               color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
               abilities=[121423], set_id="GRN", rarity="Rare", set_number=222,
               mtga_id=68687)
DiscoveryDispersal = Card(name="discovery__dispersal", pretty_name="Discovery // Dispersal", cost=['1', '(U/B)', '3', 'U', 'B'],
                          color_identity=['U', 'B'], card_type="Sorcery Instant", sub_types="",
                          abilities=[121424, 121485], set_id="GRN", rarity="Uncommon", set_number=223,
                          mtga_id=68688)
Discovery = Card(name="discovery", pretty_name="Discovery", cost=['1', '(U/B)'],
                 color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
                 abilities=[121424], set_id="GRN", rarity="Uncommon", set_number=223,
                 mtga_id=68689)
Dispersal = Card(name="dispersal", pretty_name="Dispersal", cost=['3', 'U', 'B'],
                 color_identity=['U', 'B'], card_type="Instant", sub_types="",
                 abilities=[121485], set_id="GRN", rarity="Uncommon", set_number=223,
                 mtga_id=68690)
ExpansionExplosion = Card(name="expansion__explosion", pretty_name="Expansion // Explosion", cost=['(U/R)', '(U/R)', 'X', 'U', 'U', 'R', 'R'],
                          color_identity=['U', 'R'], card_type="Instant Instant", sub_types="",
                          abilities=[121426, 121487], set_id="GRN", rarity="Rare", set_number=224,
                          mtga_id=68691)
Expansion = Card(name="expansion", pretty_name="Expansion", cost=['(U/R)', '(U/R)'],
                 color_identity=['U', 'R'], card_type="Instant", sub_types="",
                 abilities=[121426], set_id="GRN", rarity="Rare", set_number=224,
                 mtga_id=68692)
Explosion = Card(name="explosion", pretty_name="Explosion", cost=['X', 'U', 'U', 'R', 'R'],
                 color_identity=['U', 'R'], card_type="Instant", sub_types="",
                 abilities=[121487], set_id="GRN", rarity="Rare", set_number=224,
                 mtga_id=68693)
FindFinality = Card(name="find__finality", pretty_name="Find // Finality", cost=['(B/G)', '(B/G)', '4', 'B', 'G'],
                    color_identity=['B', 'G'], card_type="Sorcery Sorcery", sub_types="",
                    abilities=[1923, 121428], set_id="GRN", rarity="Rare", set_number=225,
                    mtga_id=68694)
Find = Card(name="find", pretty_name="Find", cost=['(B/G)', '(B/G)'],
            color_identity=['B', 'G'], card_type="Sorcery", sub_types="",
            abilities=[1923], set_id="GRN", rarity="Rare", set_number=225,
            mtga_id=68695)
Finality = Card(name="finality", pretty_name="Finality", cost=['4', 'B', 'G'],
                color_identity=['B', 'G'], card_type="Sorcery", sub_types="",
                abilities=[121428], set_id="GRN", rarity="Rare", set_number=225,
                mtga_id=68696)
FlowerFlourish = Card(name="flower__flourish", pretty_name="Flower // Flourish", cost=['(G/W)', '4', 'G', 'W'],
                      color_identity=['W', 'G'], card_type="Sorcery Sorcery", sub_types="",
                      abilities=[121429, 24883], set_id="GRN", rarity="Uncommon", set_number=226,
                      mtga_id=68697)
Flower = Card(name="flower", pretty_name="Flower", cost=['(G/W)'],
              color_identity=['G', 'W'], card_type="Sorcery", sub_types="",
              abilities=[121429], set_id="GRN", rarity="Uncommon", set_number=226,
              mtga_id=68698)
Flourish = Card(name="flourish", pretty_name="Flourish", cost=['4', 'G', 'W'],
                color_identity=['G', 'W'], card_type="Sorcery", sub_types="",
                abilities=[24883], set_id="GRN", rarity="Uncommon", set_number=226,
                mtga_id=68699)
IntegrityIntervention = Card(name="integrity__intervention", pretty_name="Integrity // Intervention", cost=['(R/W)', '2', 'R', 'W'],
                             color_identity=['W', 'R'], card_type="Instant Instant", sub_types="",
                             abilities=[6437, 88264], set_id="GRN", rarity="Uncommon", set_number=227,
                             mtga_id=68700)
Integrity = Card(name="integrity", pretty_name="Integrity", cost=['(R/W)'],
                 color_identity=['R', 'W'], card_type="Instant", sub_types="",
                 abilities=[6437], set_id="GRN", rarity="Uncommon", set_number=227,
                 mtga_id=68701)
Intervention = Card(name="intervention", pretty_name="Intervention", cost=['2', 'R', 'W'],
                    color_identity=['R', 'W'], card_type="Instant", sub_types="",
                    abilities=[88264], set_id="GRN", rarity="Uncommon", set_number=227,
                    mtga_id=68702)
InvertInvent = Card(name="invert__invent", pretty_name="Invert // Invent", cost=['(U/R)', '4', 'U', 'R'],
                    color_identity=['U', 'R'], card_type="Instant Instant", sub_types="",
                    abilities=[133045, 121433], set_id="GRN", rarity="Uncommon", set_number=228,
                    mtga_id=68703)
Invert = Card(name="invert", pretty_name="Invert", cost=['(U/R)'],
              color_identity=['U', 'R'], card_type="Instant", sub_types="",
              abilities=[133045], set_id="GRN", rarity="Uncommon", set_number=228,
              mtga_id=68704)
Invent = Card(name="invent", pretty_name="Invent", cost=['4', 'U', 'R'],
              color_identity=['U', 'R'], card_type="Instant", sub_types="",
              abilities=[121433], set_id="GRN", rarity="Uncommon", set_number=228,
              mtga_id=68705)
ResponseResurgence = Card(name="response__resurgence", pretty_name="Response // Resurgence", cost=['(R/W)', '(R/W)', '3', 'R', 'W'],
                          color_identity=['W', 'R'], card_type="Instant Sorcery", sub_types="",
                          abilities=[101788, 121498], set_id="GRN", rarity="Rare", set_number=229,
                          mtga_id=68706)
Response = Card(name="response", pretty_name="Response", cost=['(R/W)', '(R/W)'],
                color_identity=['R', 'W'], card_type="Instant", sub_types="",
                abilities=[101788], set_id="GRN", rarity="Rare", set_number=229,
                mtga_id=68707)
Resurgence = Card(name="resurgence", pretty_name="Resurgence", cost=['3', 'R', 'W'],
                  color_identity=['R', 'W'], card_type="Sorcery", sub_types="",
                  abilities=[121498], set_id="GRN", rarity="Rare", set_number=229,
                  mtga_id=68708)
StatusStatue = Card(name="status__statue", pretty_name="Status // Statue", cost=['(B/G)', '2', 'B', 'G'],
                    color_identity=['B', 'G'], card_type="Instant Instant", sub_types="",
                    abilities=[121435, 121436], set_id="GRN", rarity="Uncommon", set_number=230,
                    mtga_id=68709)
Status = Card(name="status", pretty_name="Status", cost=['(B/G)'],
              color_identity=['B', 'G'], card_type="Instant", sub_types="",
              abilities=[121435], set_id="GRN", rarity="Uncommon", set_number=230,
              mtga_id=68710)
Statue = Card(name="statue", pretty_name="Statue", cost=['2', 'B', 'G'],
              color_identity=['B', 'G'], card_type="Instant", sub_types="",
              abilities=[121436], set_id="GRN", rarity="Uncommon", set_number=230,
              mtga_id=68711)
BorosLocket = Card(name="boros_locket", pretty_name="Boros Locket", cost=['3'],
                   color_identity=['W', 'R'], card_type="Artifact", sub_types="",
                   abilities=[4247, 121437], set_id="GRN", rarity="Common", set_number=231,
                   mtga_id=68712)
ChamberSentry = Card(name="chamber_sentry", pretty_name="Chamber Sentry", cost=['X'],
                     color_identity=['U', 'B', 'W', 'G', 'R'], card_type="Artifact Creature", sub_types="Construct",
                     abilities=[121438, 121503, 121439], set_id="GRN", rarity="Rare", set_number=232,
                     mtga_id=68713)
ChromaticLantern = Card(name="chromatic_lantern", pretty_name="Chromatic Lantern", cost=['3'],
                        color_identity=[], card_type="Artifact", sub_types="",
                        abilities=[88225, 1055], set_id="GRN", rarity="Rare", set_number=233,
                        mtga_id=68714)
DimirLocket = Card(name="dimir_locket", pretty_name="Dimir Locket", cost=['3'],
                   color_identity=['U', 'B'], card_type="Artifact", sub_types="",
                   abilities=[1167, 121440], set_id="GRN", rarity="Common", set_number=234,
                   mtga_id=68715)
GatekeeperGargoyle = Card(name="gatekeeper_gargoyle", pretty_name="Gatekeeper Gargoyle", cost=['6'],
                          color_identity=[], card_type="Artifact Creature", sub_types="Gargoyle",
                          abilities=[8, 121441], set_id="GRN", rarity="Uncommon", set_number=235,
                          mtga_id=68716)
GlaiveoftheGuildpact = Card(name="glaive_of_the_guildpact", pretty_name="Glaive of the Guildpact", cost=['2'],
                            color_identity=[], card_type="Artifact", sub_types="Equipment",
                            abilities=[121511, 1156], set_id="GRN", rarity="Uncommon", set_number=236,
                            mtga_id=68717)
GolgariLocket = Card(name="golgari_locket", pretty_name="Golgari Locket", cost=['3'],
                     color_identity=['B', 'G'], card_type="Artifact", sub_types="",
                     abilities=[4407, 121443], set_id="GRN", rarity="Common", set_number=237,
                     mtga_id=68718)
IzzetLocket = Card(name="izzet_locket", pretty_name="Izzet Locket", cost=['3'],
                   color_identity=['U', 'R'], card_type="Artifact", sub_types="",
                   abilities=[1039, 121444], set_id="GRN", rarity="Common", set_number=238,
                   mtga_id=68719)
RampagingMonument = Card(name="rampaging_monument", pretty_name="Rampaging Monument", cost=['4'],
                         color_identity=[], card_type="Artifact Creature", sub_types="Cleric",
                         abilities=[14, 90236, 121446], set_id="GRN", rarity="Uncommon", set_number=239,
                         mtga_id=68720)
SelesnyaLocket = Card(name="selesnya_locket", pretty_name="Selesnya Locket", cost=['3'],
                      color_identity=['W', 'G'], card_type="Artifact", sub_types="",
                      abilities=[1203, 121447], set_id="GRN", rarity="Common", set_number=240,
                      mtga_id=68721)
SilentDart = Card(name="silent_dart", pretty_name="Silent Dart", cost=['1'],
                  color_identity=[], card_type="Artifact", sub_types="",
                  abilities=[121448], set_id="GRN", rarity="Uncommon", set_number=241,
                  mtga_id=68722)
WandofVertebrae = Card(name="wand_of_vertebrae", pretty_name="Wand of Vertebrae", cost=['1'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[121449, 121520], set_id="GRN", rarity="Uncommon", set_number=242,
                       mtga_id=68723)
BorosGuildgate = Card(name="boros_guildgate", pretty_name="Boros Guildgate", cost=[],
                      color_identity=['R', 'W'], card_type="Land", sub_types="Gate",
                      abilities=[76735, 4247], set_id="GRN", rarity="Common", set_number=243,
                      mtga_id=68724)
BorosGuildgate2 = Card(name="boros_guildgate", pretty_name="Boros Guildgate", cost=[],
                       color_identity=['R', 'W'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 4247], set_id="GRN", rarity="Common", set_number=244,
                       mtga_id=68725)
DimirGuildgate = Card(name="dimir_guildgate", pretty_name="Dimir Guildgate", cost=[],
                      color_identity=['U', 'B'], card_type="Land", sub_types="Gate",
                      abilities=[76735, 1167], set_id="GRN", rarity="Common", set_number=245,
                      mtga_id=68726)
DimirGuildgate2 = Card(name="dimir_guildgate", pretty_name="Dimir Guildgate", cost=[],
                       color_identity=['U', 'B'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 1167], set_id="GRN", rarity="Common", set_number=246,
                       mtga_id=68727)
GatewayPlaza = Card(name="gateway_plaza", pretty_name="Gateway Plaza", cost=[],
                    color_identity=[], card_type="Land", sub_types="Gate",
                    abilities=[76735, 3625, 1055], set_id="GRN", rarity="Common", set_number=247,
                    mtga_id=68728)
GolgariGuildgate = Card(name="golgari_guildgate", pretty_name="Golgari Guildgate", cost=[],
                        color_identity=['B', 'G'], card_type="Land", sub_types="Gate",
                        abilities=[76735, 4407], set_id="GRN", rarity="Common", set_number=248,
                        mtga_id=68729)
GolgariGuildgate2 = Card(name="golgari_guildgate", pretty_name="Golgari Guildgate", cost=[],
                         color_identity=['B', 'G'], card_type="Land", sub_types="Gate",
                         abilities=[76735, 4407], set_id="GRN", rarity="Common", set_number=249,
                         mtga_id=68730)
GuildmagesForum = Card(name="guildmages_forum", pretty_name="Guildmages' Forum", cost=[],
                       color_identity=[], card_type="Land", sub_types="",
                       abilities=[1152, 121453], set_id="GRN", rarity="Rare", set_number=250,
                       mtga_id=68731)
IzzetGuildgate = Card(name="izzet_guildgate", pretty_name="Izzet Guildgate", cost=[],
                      color_identity=['U', 'R'], card_type="Land", sub_types="Gate",
                      abilities=[76735, 1039], set_id="GRN", rarity="Common", set_number=251,
                      mtga_id=68732)
IzzetGuildgate2 = Card(name="izzet_guildgate", pretty_name="Izzet Guildgate", cost=[],
                       color_identity=['U', 'R'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 1039], set_id="GRN", rarity="Common", set_number=252,
                       mtga_id=68733)
OvergrownTomb = Card(name="overgrown_tomb", pretty_name="Overgrown Tomb", cost=[],
                     color_identity=['B', 'G'], card_type="Land", sub_types="Swamp Forest",
                     abilities=[90846], set_id="GRN", rarity="Rare", set_number=253,
                     mtga_id=68734)
SacredFoundry = Card(name="sacred_foundry", pretty_name="Sacred Foundry", cost=[],
                     color_identity=['R', 'W'], card_type="Land", sub_types="Mountain Plains",
                     abilities=[90846], set_id="GRN", rarity="Rare", set_number=254,
                     mtga_id=68735)
SelesnyaGuildgate = Card(name="selesnya_guildgate", pretty_name="Selesnya Guildgate", cost=[],
                         color_identity=['G', 'W'], card_type="Land", sub_types="Gate",
                         abilities=[76735, 1203], set_id="GRN", rarity="Common", set_number=255,
                         mtga_id=68736)
SelesnyaGuildgate2 = Card(name="selesnya_guildgate", pretty_name="Selesnya Guildgate", cost=[],
                          color_identity=['G', 'W'], card_type="Land", sub_types="Gate",
                          abilities=[76735, 1203], set_id="GRN", rarity="Common", set_number=256,
                          mtga_id=68737)
SteamVents = Card(name="steam_vents", pretty_name="Steam Vents", cost=[],
                  color_identity=['U', 'R'], card_type="Land", sub_types="Island Mountain",
                  abilities=[90846], set_id="GRN", rarity="Rare", set_number=257,
                  mtga_id=68738)
TempleGarden = Card(name="temple_garden", pretty_name="Temple Garden", cost=[],
                    color_identity=['G', 'W'], card_type="Land", sub_types="Forest Plains",
                    abilities=[90846], set_id="GRN", rarity="Rare", set_number=258,
                    mtga_id=68739)
WateryGrave = Card(name="watery_grave", pretty_name="Watery Grave", cost=[],
                   color_identity=['U', 'B'], card_type="Land", sub_types="Island Swamp",
                   abilities=[90846], set_id="GRN", rarity="Rare", set_number=259,
                   mtga_id=68740)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="GRN", rarity="Basic", set_number=260,
              mtga_id=68741)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="GRN", rarity="Basic", set_number=261,
              mtga_id=68742)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="GRN", rarity="Basic", set_number=262,
             mtga_id=68743)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="GRN", rarity="Basic", set_number=263,
                mtga_id=68744)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="GRN", rarity="Basic", set_number=264,
              mtga_id=68745)
RalCallerofStorms = Card(name="ral_caller_of_storms", pretty_name="Ral, Caller of Storms", cost=['4', 'U', 'R'],
                         color_identity=['U', 'R'], card_type="Planeswalker", sub_types="Ral",
                         abilities=[1323, 121455, 121522], set_id="GRN", rarity="Mythic Rare", set_number=265,
                         mtga_id=68746)
RalsDispersal = Card(name="rals_dispersal", pretty_name="Ral's Dispersal", cost=['3', 'U', 'U'],
                     color_identity=['U'], card_type="Instant", sub_types="",
                     abilities=[121456], set_id="GRN", rarity="Rare", set_number=266,
                     mtga_id=68747)
PrecisionBolt = Card(name="precision_bolt", pretty_name="Precision Bolt", cost=['2', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[70361], set_id="GRN", rarity="Common", set_number=267,
                     mtga_id=68748)
RalsStaticaster = Card(name="rals_staticaster", pretty_name="Ral's Staticaster", cost=['2', 'U', 'R'],
                       color_identity=['U', 'R'], card_type="Creature", sub_types="Viashino Wizard",
                       abilities=[14, 121457], set_id="GRN", rarity="Uncommon", set_number=268,
                       mtga_id=68749)
VraskaRegalGorgon = Card(name="vraska_regal_gorgon", pretty_name="Vraska, Regal Gorgon", cost=['5', 'B', 'G'],
                         color_identity=['B', 'G'], card_type="Planeswalker", sub_types="Vraska",
                         abilities=[121523, 102469, 121525], set_id="GRN", rarity="Mythic Rare", set_number=269,
                         mtga_id=68750)
KraulRaider = Card(name="kraul_raider", pretty_name="Kraul Raider", cost=['2', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Insect Warrior",
                   abilities=[142], set_id="GRN", rarity="Common", set_number=270,
                   mtga_id=68751)
AttendantofVraska = Card(name="attendant_of_vraska", pretty_name="Attendant of Vraska", cost=['1', 'B', 'G'],
                         color_identity=['B', 'G'], card_type="Creature", sub_types="Zombie Soldier",
                         abilities=[121459], set_id="GRN", rarity="Uncommon", set_number=271,
                         mtga_id=68752)
VraskasStoneglare = Card(name="vraskas_stoneglare", pretty_name="Vraska's Stoneglare", cost=['4', 'B', 'G'],
                         color_identity=['B', 'G'], card_type="Sorcery", sub_types="",
                         abilities=[121460], set_id="GRN", rarity="Rare", set_number=272,
                         mtga_id=68753)
ImperviousGreatwurm = Card(name="impervious_greatwurm", pretty_name="Impervious Greatwurm", cost=['7', 'G', 'G', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Wurm",
                           abilities=[52, 104], set_id="GRN", rarity="Mythic Rare", set_number=273,
                           mtga_id=68754)
Angel = Card(name="angel", pretty_name="Angel", cost=[],
             color_identity=[], card_type="Creature", sub_types="Angel",
             abilities=[8, 15], set_id="GRN", rarity="Token", set_number=1,
             mtga_id=68755)
Soldier = Card(name="soldier", pretty_name="Soldier", cost=[],
               color_identity=[], card_type="Creature", sub_types="Soldier",
               abilities=[12], set_id="GRN", rarity="Token", set_number=2,
               mtga_id=68756)
BirdIllusion = Card(name="bird_illusion", pretty_name="Bird Illusion", cost=[],
                    color_identity=[], card_type="Creature", sub_types="Bird Illusion",
                    abilities=[8], set_id="GRN", rarity="Token", set_number=3,
                    mtga_id=68757)
Goblin = Card(name="goblin", pretty_name="Goblin", cost=[],
              color_identity=[], card_type="Creature", sub_types="Goblin",
              abilities=[], set_id="GRN", rarity="Token", set_number=4,
              mtga_id=68758)
Insect = Card(name="insect", pretty_name="Insect", cost=[],
              color_identity=[], card_type="Creature", sub_types="Insect",
              abilities=[], set_id="GRN", rarity="Token", set_number=5,
              mtga_id=68759)
ElfKnight = Card(name="elf_knight", pretty_name="Elf Knight", cost=[],
                 color_identity=[], card_type="Creature", sub_types="Elf Knight",
                 abilities=[15], set_id="GRN", rarity="Token", set_number=6,
                 mtga_id=68760)

# manually added
RalIzzetViceroy_Masterpiece = Card(name="ral_izzet_viceroy", pretty_name="Ral, Izzet Viceroy", cost=['3', 'U', 'R'],
                                   color_identity=['U', 'R'], card_type="Planeswalker", sub_types="Ral",
                                   abilities=[121399, 121398, 121400], set_id="GRN",
                                   rarity="Mythic Rare", set_number=5000, mtga_id=69449)
VraskaGolgariQueen_Masterpiece = Card(name="vraska_golgari_queen", pretty_name="Vraska, Golgari Queen",
                                      cost=['2', 'B', 'G'], color_identity=['B', 'G'], card_type="Planeswalker",
                                      sub_types="Vraska", abilities=[121415, 121473, 121418], set_id="GRN",
                                      rarity="Mythic Rare", set_number=8000, mtga_id=69450)



clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
GuildsOfRavnica = Set("grn", cards=clsmembers)

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
 52: 'Convoke',
 104: 'Indestructible',
 142: 'Menace',
 170: 'Jump-start',
 171: 'Mentor',
 1019: 'Target creature gets +3/+0 and gains first strike until end of turn.',
 1026: "Vigorspore Wurm can't be blocked by more than one creature.",
 1027: 'Enchant creature',
 1039: '{oT}: Add {oU} or {oR}.',
 1055: '{oT}: Add one mana of any color.',
 1083: "Enchanted creature can't attack or block.",
 1107: "You can't play cards from your hand.",
 1152: '{oT}: Add {oC}.',
 1156: 'Equip {o3}',
 1167: '{oT}: Add {oU} or {oB}.',
 1203: '{oT}: Add {oG} or {oW}.',
 1206: 'Choose one   Destroy target creature with flying.  Destroy target '
       'enchantment.',
 1275: 'As an additional cost to cast this spell, sacrifice a creature.',
 1323: '+1: Draw a card.',
 1570: 'Enchant land',
 1923: 'Return up to two target creature cards from your graveyard to your '
       'hand.',
 2433: 'Other creatures you control get +1/+1.',
 3396: 'You may play the top card of your library.',
 3625: 'When Gateway Plaza enters the battlefield, sacrifice it unless you pay '
       '{o1}.',
 4247: '{oT}: Add {oR} or {oW}.',
 4407: '{oT}: Add {oB} or {oG}.',
 6437: 'Target creature gets +2/+2 until end of turn.',
 6672: 'Target creature gets -3/-0 until end of turn.',
 7138: 'Enchanted creature gets -2/-2.',
 8701: '{o3oU}, {oT}: Draw a card.',
 9094: 'Target creature gets +1/+1 until end of turn for each creature you '
       'control.',
 12670: 'Target creature deals damage to itself equal to its power.',
 13250: 'Command the Storm deals 5 damage to target creature.',
 14523: 'You may look at the top card of your library any time.',
 18554: "Create a token that's a copy of target creature you control.",
 18631: 'Put a +1/+1 counter on each of up to two target creatures.',
 19445: 'Instant and sorcery spells you cast cost {o1} less to cast.',
 20997: 'When Conclave Tribunal enters the battlefield, exile target nonland '
        'permanent an opponent controls until Conclave Tribunal leaves the '
        'battlefield.',
 21963: 'Counter target spell with converted mana cost 4 or greater.',
 22505: "Return target creature to its owner's hand.",
 22658: 'Destroy target creature with toughness 4 or greater.',
 23607: 'Draw two cards.',
 24394: 'Destroy all creatures with converted mana cost 3 or less.',
 24733: 'Target creature gets +3/+3 until end of turn.',
 24883: 'Creatures you control get +2/+2 until end of turn.',
 25846: 'Counter target spell.',
 25848: 'Draw a card.',
 26818: 'Destroy target creature.',
 27746: 'Prevent all combat damage that would be dealt this turn.',
 30056: 'All creatures get -1/-1 until end of turn.',
 62610: 'Whenever you cast a creature spell, draw a card.',
 62969: "Etrata, the Silencer can't be blocked.",
 70361: 'Precision Bolt deals 3 damage to any target.',
 76735: 'Selesnya Guildgate enters the battlefield tapped.',
 76746: '{o1oB}: Veiled Shade gets +1/+1 until end of turn.',
 76843: '{o1oR}: Goblin Banneret gets +2/+0 until end of turn.',
 76885: 'Worldsoul Colossus enters the battlefield with X +1/+1 counters on '
        'it.',
 86613: 'Direct Current deals 2 damage to any target.',
 86788: 'When Crackling Drake enters the battlefield, draw a card.',
 87008: 'When Spinal Centipede dies, put a +1/+1 counter on target creature '
        'you control.',
 87894: "Wojek Bodyguard can't attack or block alone.",
 88178: "Enchanted creature doesn't untap during its controller's untap step.",
 88225: 'Lands you control have "{oT}: Add one mana of any color."',
 88264: 'Intervention deals 3 damage to any target and you gain 3 life.',
 88604: 'When Loxodon Restorer enters the battlefield, you gain 4 life.',
 88808: 'All creatures able to block Ochran Assassin do so.',
 89260: 'Exile Mnemonic Betrayal.',
 89789: 'When Capture Sphere enters the battlefield, tap enchanted creature.',
 90236: 'Rampaging Monument enters the battlefield with three +1/+1 counters '
        'on it.',
 90333: "Enchanted creature gets +2/+2 and can't block.",
 90489: "Enchanted creature can't block, and its activated abilities can't be "
        'activated.',
 90846: 'As Watery Grave enters the battlefield, you may pay 2 life. If you '
        "don't, it enters the battlefield tapped.",
 91091: 'Whenever you draw a card, Niv-Mizzet, Parun deals 1 damage to any '
        'target.',
 91716: 'When Narcomoeba is put into your graveyard from your library, you may '
        'put it onto the battlefield.',
 91866: 'Whenever you cast an instant or sorcery spell, Wee Dragonauts gets '
        '+2/+0 until end of turn.',
 92425: 'When Ironshell Beetle enters the battlefield, put a +1/+1 counter on '
        'target creature.',
 92927: 'When Burglar Rat enters the battlefield, each opponent discards a '
        'card.',
 92976: 'If a spell or ability an opponent controls causes you to discard '
        'Nullhide Ferox, put it onto the battlefield instead of putting it '
        'into your graveyard.',
 94974: 'When Rubblebelt Boar enters the battlefield, target creature gets '
        '+2/+0 until end of turn.',
 99356: "Target creature you control fights target creature you don't control.",
 99455: 'Whenever Ornery Goblin blocks or becomes blocked by a creature, '
        'Ornery Goblin deals 1 damage to that creature.',
 99704: 'Enchanted land has "{oT}: Add one mana of any color."',
 99791: 'Righteous Blow deals 2 damage to target attacking or blocking '
        'creature.',
 100360: "{oRoW}: Tajic, Legion's Edge gains first strike until end of turn.",
 101336: "{o2oU}: Target creature can't be blocked this turn.",
 101750: 'When Molderhulk enters the battlefield, return target land card from '
         'your graveyard to the battlefield.',
 101788: 'Response deals 5 damage to target attacking or blocking creature.',
 102099: 'When Affectionate Indrik enters the battlefield, you may have it '
         "fight target creature you don't control.",
 102469: '-3: Destroy target creature.',
 117067: 'Target opponent reveals their hand. You choose a nonland card from '
         'it. That player discards that card.',
 120287: "This spell can't be countered.",
 121352: 'When Intrusive Packbeast enters the battlefield, tap up to two '
         'target creatures your opponents control.',
 121353: 'Surveil 2.',
 121354: 'Counter target spell. If that spell is countered this way, exile it '
         "instead of putting it into its owner's graveyard. You may shuffle up "
         'to four target cards from your graveyard into your library.',
 121355: 'Sacrifice Torch Courier: Another target creature gains haste until '
         'end of turn.',
 121356: 'Search your library for up to two basic land cards and/or Gate '
         'cards, put them onto the battlefield tapped, then shuffle your '
         'library.',
 121357: 'When Watcher in the Mist enters the battlefield, surveil 2.',
 121358: '{o4oG}: Devkarin Dissident gets +2/+2 until end of turn.',
 121359: 'When District Guide enters the battlefield, you may search your '
         'library for a basic land card or Gate card, reveal it, put it into '
         'your hand, then shuffle your library.',
 121360: '<i>Undergrowth</i>  Golgari Raiders enters the battlefield with a '
         '+1/+1 counter on it for each creature card in your graveyard.',
 121361: '{o4oG}: Grappling Sundew gains indestructible until end of turn.',
 121362: '<i>Undergrowth</i>  When you cast this spell, reveal the top X cards '
         'of your library, where X is the number of creature cards in your '
         'graveyard. You may put a green permanent card with converted mana '
         'cost X or less from among them onto the battlefield. Put the rest on '
         'the bottom of your library in a random order.',
 121363: '{o2}, {oT}, Sacrifice a creature with defender: Draw a card.',
 121364: 'Whenever you cast a blue spell, target player puts the top two cards '
         'of their library into their graveyard.',
 121365: 'You may look at an additional two cards each time you surveil.',
 121366: 'Return up to three target multicolored cards from your graveyard to '
         'your hand. Exile Vivid Revival.',
 121367: 'At the beginning of combat on your turn, choose up to one target '
         'creature you control. Until end of turn, that creature gets +2/+0, '
         "gains trample if it's red, and gains vigilance if it's white.",
 121368: 'When Conclave Cavalier dies, create two 2/2 green and white Elf '
         'Knight creature tokens with vigilance.',
 121369: 'Target creature gets +1/+1 and gains flying until end of turn.',
 121370: 'Whenever you cast an instant or sorcery spell, put a charge counter '
         "on Firemind's Research.",
 121371: "{o1oU}, Remove two charge counters from Firemind's Research: Draw a "
         'card.',
 121372: "{o1oR}, Remove five charge counters from Firemind's Research: It "
         'deals 5 damage to any target.',
 121373: 'Garrison Sergeant has double strike as long as you control a Gate.',
 121374: 'When Glowspore Shaman enters the battlefield, put the top three '
         'cards of your library into your graveyard. You may put a land card '
         'from your graveyard on top of your library.',
 121375: 'Surveil 2, then choose an instant or sorcery card in your graveyard. '
         'You may cast that card this turn. If that card would be put into '
         'your graveyard this turn, exile it instead.',
 121376: 'When Golgari Findbroker enters the battlefield, return target '
         'permanent card from your graveyard to your hand.',
 121377: "{o1oU}, {oT}: Target creature doesn't untap during its controller's "
         'next untap step.',
 121378: '{o2oB}, {oT}: Surveil 2.',
 121379: 'Draw two cards. Then you may discard a nonland card. When you do, '
         'Hypothesizzle deals 4 damage to target creature.',
 121380: "Counter target spell. Ionize deals 2 damage to that spell's "
         'controller.',
 121381: 'Whenever you cast an instant or sorcery spell, create a 1/1 blue '
         'Bird Illusion creature token with flying.',
 121382: '{oBoG}, Sacrifice another creature: You gain 1 life and draw a card.',
 121383: 'Untap all creatures you control. They gain hexproof and '
         'indestructible until end of turn.',
 121386: 'Whenever Roc Charger attacks, target attacking creature without '
         'flying gains flying until end of turn.',
 121388: '{oXoR}, {oT}: Copy target instant or sorcery spell you control with '
         'converted mana cost X. You may choose new targets for the copy.',
 121389: 'Whenever Ledev Champion attacks, you may tap any number of untapped '
         'creatures you control. Ledev Champion gets +1/+1 until end of turn '
         'for each creature tapped this way.',
 121390: '{o5oR}, {oT}: Legion Guildmage deals 3 damage to each opponent.',
 121391: '{o2oW}, {oT}: Tap another target creature.',
 121392: 'Create X 1/1 white Soldier creature tokens with lifelink.',
 121393: "Exile all cards from all opponents' graveyards. You may cast those "
         'cards this turn, and you may spend mana as though it were mana of '
         'any type to cast those spells. At the beginning of the next end '
         'step, if any of those cards remain exiled, return them to their '
         "owners' graveyards.",
 121394: 'Whenever Nightveil Sprite attacks, surveil 1.',
 121395: 'Whenever a player casts an instant or sorcery spell, you draw a '
         'card.',
 121396: 'Surveil 2, then draw two cards. Notion Rain deals 2 damage to you.',
 121397: '{o2oU}, {oT}: You may cast an instant or sorcery card from your hand '
         'without paying its mana cost.',
 121398: '-3: Ral, Izzet Viceroy deals damage to target creature equal to the '
         'total number of instant and sorcery cards you own in exile and in '
         'your graveyard.',
 121399: '+1: Look at the top two cards of your library. Put one of them into '
         'your hand and the other into your graveyard.',
 121400: '-8: You get an emblem with "Whenever you cast an instant or sorcery '
         'spell, this emblem deals 4 damage to any target and you draw two '
         'cards."',
 121401: '<i>Undergrowth</i>  Rhizome Lurcher enters the battlefield with a '
         'number of +1/+1 counters on it equal to the number of creature cards '
         'in your graveyard.',
 121402: "Tap target creature. Sonic Assault deals 2 damage to that creature's "
         'controller.',
 121403: '{o4oB}, {oT}: Creatures you control get +1/+0 and gain menace until '
         'end of turn.',
 121404: '{o1oG}, {oT}: You gain 2 life.',
 121405: 'Whenever Swathcutter Giant attacks, it deals 1 damage to each '
         'creature defending player controls.',
 121406: 'Prevent all noncombat damage that would be dealt to other creatures '
         'you control.',
 121407: 'Whenever Skyline Scout attacks, you may pay {o1oW}. If you do, it '
         'gains flying until end of turn.',
 121409: 'When Trostani Discordant enters the battlefield, create two 1/1 '
         'white Soldier creature tokens with lifelink.',
 121410: 'At the beginning of your end step, each player gains control of all '
         'creatures they own.',
 121411: 'Creatures you control gain deathtouch until end of turn. Then target '
         "creature you control fights target creature you don't control.",
 121412: 'If you would draw a card, instead look at the top three cards of '
         'your library, then put one into your hand and the rest into your '
         'graveyard.',
 121413: 'Pay 4 life: Underrealm Lich gains indestructible until end of turn. '
         'Tap it.',
 121414: "Choose a card name. Search target opponent's graveyard, hand, and "
         'library for up to four cards with that name and exile them. That '
         'player shuffles their library, then draws a card for each card '
         'exiled from their hand this way.',
 121415: '+2: You may sacrifice another permanent. If you do, you gain 1 life '
         'and draw a card.',
 121416: 'Return X target creatures of the creature type of your choice to '
         "their owner's hand.",
 121418: '-9: You get an emblem with "Whenever a creature you control deals '
         'combat damage to a player, that player loses the game."',
 121419: "As long as it's your turn, Fresh-Faced Recruit has first strike.",
 121420: 'Put a +1/+1 counter on target creature. That creature gains '
         'indestructible until end of turn.',
 121421: 'Create three 2/2 green and white Elf Knight creature tokens with '
         'vigilance.',
 121422: 'Gain control of target creature with power 2 or less.',
 121423: 'Surveil 3, then return a creature card from your graveyard to the '
         'battlefield.',
 121424: 'Surveil 2, then draw a card.',
 121425: 'Surveil 1.',
 121426: 'Copy target instant or sorcery spell with converted mana cost 4 or '
         'less. You may choose new targets for the copy.',
 121427: 'When Sumala Woodshaper enters the battlefield, look at the top four '
         'cards of your library. You may reveal a creature or enchantment card '
         'from among them and put it into your hand. Put the rest on the '
         'bottom of your library in a random order.',
 121428: 'You may put two +1/+1 counters on a creature you control. Then all '
         'creatures get -4/-4 until end of turn.',
 121429: 'Search your library for a basic Forest or Plains card, reveal it, '
         'put it into your hand, then shuffle your library.',
 121430: 'Whenever you surveil, put a +1/+1 counter on Dimir Spybug.',
 121431: 'Create two 1/1 white Soldier creature tokens with lifelink.',
 121433: 'Search your library for an instant card and/or a sorcery card, '
         'reveal them, put them into your hand, then shuffle your library.',
 121434: 'As long as Thoughtbound Phantasm has three or more +1/+1 counters on '
         "it, it can attack as though it didn't have defender.",
 121435: 'Target creature gets +1/+1 and gains deathtouch until end of turn.',
 121436: 'Destroy target artifact, creature, or enchantment.',
 121437: '{o(R/W)o(R/W)o(R/W)o(R/W)}, {oT}, Sacrifice Boros Locket: Draw two '
         'cards.',
 121438: 'Chamber Sentry enters the battlefield with a +1/+1 counter on it for '
         'each color of mana spent to cast it.',
 121439: '{oWoUoBoRoG}: Return Chamber Sentry from your graveyard to your '
         'hand.',
 121440: '{o(U/B)o(U/B)o(U/B)o(U/B)}, {oT}, Sacrifice Dimir Locket: Draw two '
         'cards.',
 121441: 'Gatekeeper Gargoyle enters the battlefield with a +1/+1 counter on '
         'it for each Gate you control.',
 121442: 'Whenever Vedalken Mesmerist attacks, target creature an opponent '
         'controls gets -2/-0 until end of turn.',
 121443: '{o(B/G)o(B/G)o(B/G)o(B/G)}, {oT}, Sacrifice Golgari Locket: Draw two '
         'cards.',
 121444: '{o(U/R)o(U/R)o(U/R)o(U/R)}, {oT}, Sacrifice Izzet Locket: Draw two '
         'cards.',
 121445: 'When Whisper Agent enters the battlefield, surveil 1.',
 121446: 'Whenever you cast a multicolored spell, put a +1/+1 counter on '
         'Rampaging Monument.',
 121447: '{o(G/W)o(G/W)o(G/W)o(G/W)}, {oT}, Sacrifice Selesnya Locket: Draw '
         'two cards.',
 121448: '{o4}, {oT}, Sacrifice Silent Dart: It deals 3 damage to target '
         'creature.',
 121449: '{oT}: Put the top card of your library into your graveyard.',
 121450: 'When Blood Operative enters the battlefield, you may exile target '
         'card from a graveyard.',
 121451: 'Target creature gets +2/+2 until end of turn. You gain 1 life for '
         'each attacking creature you control.',
 121452: 'Whenever Thief of Sanity deals combat damage to a player, look at '
         "the top three cards of that player's library, exile one of them face "
         'down, then put the rest into their graveyard. You may look at and '
         'cast that card for as long as it remains exiled, and you may spend '
         'mana as though it were mana of any type to cast that spell.',
 121453: '{o1}, {oT}: Add one mana of any color. If that mana is spent on a '
         'multicolored creature spell, that creature enters the battlefield '
         'with an additional +1/+1 counter on it.',
 121454: 'Whenever you surveil, if Blood Operative is in your graveyard, you '
         'may pay 3 life. If you do, return Blood Operative to your hand.',
 121455: '-2: Ral, Caller of Storms deals 3 damage divided as you choose among '
         'one, two, or three targets.',
 121456: "Return target creature to its owner's hand. You may search your "
         'library and/or graveyard for a card named Ral, Caller of Storms, '
         'reveal it, and put it into your hand. If you search your library '
         'this way, shuffle it.',
 121457: "Whenever Ral's Staticaster attacks, if you control a Ral "
         "planeswalker, Ral's Staticaster gets +1/+0 for each card in your "
         'hand until end of turn.',
 121458: 'Whenever you cast an instant or sorcery spell, copy it for each '
         "other instant and sorcery spell you've cast before it this turn. You "
         'may choose new targets for the copies.',
 121459: 'When Attendant of Vraska dies, if you control a Vraska planeswalker, '
         "you gain life equal to Attendant of Vraska's power.",
 121460: 'Destroy target creature. You gain life equal to its toughness. You '
         'may search your library and/or graveyard for a card named Vraska, '
         'Regal Gorgon, reveal it, and put it into your hand. If you search '
         'your library this way, shuffle it.',
 121462: 'Creeping Chill deals 3 damage to each opponent and you gain 3 life.',
 121463: 'When Creeping Chill is put into your graveyard from your library, '
         'you may exile it. If you do, Creeping Chill deals 3 damage to each '
         'opponent and you gain 3 life.',
 121464: 'When Tenth District Guard enters the battlefield, target creature '
         'gets +0/+1 until end of turn.',
 121465: 'Whenever Truefire Captain is dealt damage, it deals that much damage '
         'to target player.',
 121466: 'Pay 2 life: Surveil 2.',
 121467: 'Choose a creature card with converted mana cost 1 in your graveyard, '
         'then do the same for creature cards with converted mana costs 2 and '
         '3. Return those cards to the battlefield.',
 121468: '{o2oB}, Discard a creature card: Return Kraul Swarm from your '
         'graveyard to your hand.',
 121469: '<i>Undergrowth</i>  When Lotleth Giant enters the battlefield, it '
         'deals 1 damage to target opponent for each creature card in your '
         'graveyard.',
 121470: 'When Venerated Loxodon enters the battlefield, put a +1/+1 counter '
         'on each creature that convoked it.',
 121471: 'When Light of the Legion dies, put a +1/+1 counter on each white '
         'creature you control.',
 121472: '<i>Undergrowth</i>  Search your library for a black card with '
         'converted mana cost less than or equal to the number of creature '
         'cards in your graveyard, reveal it, put it into your hand, then '
         'shuffle your library.',
 121473: '-3: Destroy target nonland permanent with converted mana cost 3 or '
         'less.',
 121474: '<i>Undergrowth</i>  When Izoni, Thousand-Eyed enters the '
         'battlefield, create a 1/1 black and green Insect creature token for '
         'each creature card in your graveyard.',
 121475: 'Whenever a nontoken creature you control dies, Midnight Reaper deals '
         '1 damage to you and you draw a card.',
 121476: '<i>Undergrowth</i>  When Moodmark Painter enters the battlefield, '
         'target creature gains menace and gets +X/+0 until end of turn, where '
         'X is the number of creature cards in your graveyard.',
 121477: '<i>Undergrowth</i>  Target creature gets -X/-X until end of turn, '
         'where X is the number of creature cards in your graveyard. If that '
         'creature would die this turn, exile it instead.',
 121478: 'Target opponent reveals their hand. You choose a nonland card from '
         "that player's graveyard or hand and exile it.",
 121479: '{o1oB}, {oT}, Sacrifice Pilfering Imp: Target opponent reveals their '
         'hand. You choose a nonland card from it. That player discards that '
         'card. Activate this ability only any time you could cast a sorcery.',
 121480: 'When Plaguecrafter enters the battlefield, each player sacrifices a '
         "creature or planeswalker. Each player who can't discards a card.",
 121481: "As long as you've cast an instant or sorcery spell this turn, "
         "Piston-Fist Cyclops can attack as though it didn't have defender.",
 121482: 'This spell costs {o2} less to cast if it targets a legendary '
         'creature.',
 121483: "You gain life equal to the sacrificed creature's toughness. Destroy "
         'target creature an opponent controls.',
 121484: '{o1}, Sacrifice another creature: Put a +1/+1 counter on Undercity '
         'Necrolisk. It gains menace until end of turn. Activate this ability '
         'only any time you could cast a sorcery.',
 121485: 'Each opponent returns a nonland permanent they control with the '
         'highest converted mana cost among permanents they control to its '
         "owner's hand, then discards a card.",
 121486: 'Vicious Rumors deals 1 damage to each opponent. Each opponent '
         'discards a card, then puts the top card of their library into their '
         'graveyard. You gain 1 life.',
 121487: 'Explosion deals X damage to any target. Target player draws X cards.',
 121488: 'Whenever you surveil for the first time each turn, Whispering Snitch '
         'deals 1 damage to each opponent and you gain 1 life.',
 121489: "At the beginning of combat on your turn, if you've cast three or "
         'more instant and sorcery spells this turn, return Arclight Phoenix '
         'from your graveyard to the battlefield.',
 121490: 'You gain X life and draw X cards, where X is the number of creatures '
         'you control. Creatures you control get +1/+1 until end of turn.',
 121491: 'Whenever Book Devourer deals combat damage to a player, you may '
         'discard all the cards in your hand. If you do, draw that many cards.',
 121493: 'Cosmotronic Wave deals 1 damage to each creature your opponents '
         "control. Creatures your opponents control can't block this turn.",
 121494: 'Whenever you cast an instant or sorcery spell, Electrostatic Field '
         'deals 1 damage to each opponent.',
 121495: 'Whenever you cast an instant or sorcery spell, Erratic Cyclops gets '
         "+X/+0 until end of turn, where X is that spell's converted mana "
         'cost.',
 121497: 'When Citywatch Sphinx dies, surveil 2.',
 121498: 'Creatures you control gain first strike and vigilance until end of '
         'turn. After this main phase, there is an additional combat phase '
         'followed by an additional main phase.',
 121499: '{o3oR}: Destroy Experimental Frenzy.',
 121500: 'Whenever you cast an instant or sorcery spell, Fire Urchin gets '
         '+1/+0 until end of turn.',
 121503: '{oX}, {oT}, Remove X +1/+1 counters from Chamber Sentry: It deals X '
         'damage to any target.',
 121505: '{o1}, Sacrifice Goblin Cratermaker: Choose one   Goblin Cratermaker '
         'deals 2 damage to target creature.  Destroy target colorless nonland '
         'permanent.',
 121506: "Whenever Goblin Locksmith attacks, creatures with defender can't "
         'block this turn.',
 121507: 'Target creature you control deals damage equal to its power to '
         'target player.',
 121508: 'Whenever Hellkite Whelp attacks, it deals 1 damage to target '
         'creature defending player controls.',
 121509: 'When Knight of Autumn enters the battlefield, choose one   Put two '
         '+1/+1 counters on Knight of Autumn.  Destroy target artifact or '
         'enchantment.  You gain 4 life.',
 121510: 'Inescapable Blaze deals 6 damage to any target.',
 121511: 'Equipped creature gets +1/+0 for each Gate you control and has '
         'vigilance and menace.',
 121512: 'Lava Coil deals 4 damage to target creature. If that creature would '
         'die this turn, exile it instead.',
 121513: 'At the beginning of combat on your turn, create a 1/1 red Goblin '
         'creature token. That token gains haste until end of turn and attacks '
         'this combat if able.',
 121514: 'Target creature gets +1/+1 and gains haste until end of turn.',
 121515: 'Target opponent may have Risk Factor deal 4 damage to them. If that '
         "player doesn't, you draw three cards.",
 121516: 'Whenever you cast a red spell, if Runaway Steam-Kin has fewer than '
         'three +1/+1 counters on it, put a +1/+1 counter on Runaway '
         'Steam-Kin.',
 121517: 'Remove three +1/+1 counters from Runaway Steam-Kin: Add {oRoRoR}.',
 121518: 'Whenever you cast an instant or sorcery spell, target creature an '
         "opponent controls can't block this turn.",
 121519: "As long as it's your turn, creatures you control get +1/+0 and have "
         'trample.',
 121520: '{o2}, {oT}, Exile Wand of Vertebrae: Shuffle up to five target cards '
         'from your graveyard into your library.',
 121521: 'When Dream Eater enters the battlefield, surveil 4. When you do, you '
         'may return target nonland permanent an opponent controls to its '
         "owner's hand.",
 121522: '-7: Draw seven cards. Ral, Caller of Storms deals 7 damage to each '
         'creature your opponents control.',
 121523: '+2: Put a +1/+1 counter on up to one target creature. That creature '
         'gains menace until end of turn.',
 121524: '{o3oGoW}: Create a 1/1 white Soldier creature token with lifelink.',
 121525: '-10: For each creature card in your graveyard, put a +1/+1 counter '
         'on each creature you control.',
 121526: '<i>Undergrowth</i>  When Kraul Foragers enters the battlefield, you '
         'gain 1 life for each creature card in your graveyard.',
 121527: '<i>Undergrowth</i>  When Kraul Harpooner enters the battlefield, '
         "choose up to one target creature with flying you don't control. "
         'Kraul Harpooner gets +X/+0 until end of turn, where X is the number '
         'of creature cards in your graveyard, then you may have Kraul '
         'Harpooner fight that creature.',
 121529: "You can't cast noncreature spells.",
 121530: '{o2}: Nullhide Ferox loses all abilities until end of turn. Any '
         'player may activate this ability.',
 121531: 'Exile Enhanced Surveillance: Shuffle your graveyard into your '
         'library.',
 121532: 'Whenever another creature you control enters the battlefield or '
         "dies, if that creature's power is greater than Pelt Collector's, put "
         'a +1/+1 counter on Pelt Collector.',
 121533: 'As long as Pelt Collector has three or more +1/+1 counters on it, it '
         'has trample.',
 121534: 'When Guild Summit enters the battlefield, you may tap any number of '
         'untapped Gates you control. Draw a card for each Gate tapped this '
         'way.',
 121536: 'Choose one   Create a 2/2 green and white Elf Knight creature token '
         'with vigilance.  Destroy target artifact or enchantment.',
 121537: 'Whenever a Gate enters the battlefield under your control, draw a '
         'card.',
 121538: '<i>Undergrowth</i>  When Vigorspore Wurm enters the battlefield, '
         'target creature gains vigilance and gets +X/+X until end of turn, '
         'where X is the number of creature cards in your graveyard.',
 121539: "Leapfrog has flying as long as you've cast an instant or sorcery "
         'spell this turn.',
 121541: 'Choose one or both   Tap target creature.  Target creature gets '
         '-2/-4 until end of turn.',
 121542: 'Destroy target permanent an opponent controls. Its controller may '
         'search their library for a basic land card, put it onto the '
         'battlefield, then shuffle their library.',
 121543: 'Beacon Bolt deals damage to target creature equal to the total '
         'number of instant and sorcery cards you own in exile and in your '
         'graveyard.',
 121544: 'Whenever you cast an instant or sorcery spell that targets only '
         'Beamsplitter Mage, if you control one or more other creatures that '
         'spell could target, choose one of those creatures. Copy that spell. '
         'The copy targets the chosen creature.',
 121545: '<i>Undergrowth</i>  This spell costs {o1} less to cast for each '
         'creature card in your graveyard.',
 121546: '{o2oRoW}: Boros Challenger gets +1/+1 until end of turn.',
 121547: 'When Centaur Peacemaker enters the battlefield, each player gains 4 '
         'life.',
 121548: 'Creatures you control gain indestructible. Take an extra turn after '
         "this one. At the beginning of that turn's end step, you lose the "
         'game.',
 121549: 'At the beginning of your upkeep, exile a creature card from your '
         'graveyard. If you do, put a +1/+1 counter on Charnel Troll. '
         'Otherwise, sacrifice it.',
 121550: '{oBoG}, Discard a creature card: Put a +1/+1 counter on Charnel '
         'Troll.',
 121551: 'Enchanted creature gets +3/+2 and has vigilance.',
 121552: '{oG}, {oT}: Creatures you control gain trample until end of turn.',
 121553: '{o5oW}, {oT}: Create a 2/2 green and white Elf Knight creature token '
         'with vigilance.',
 121554: "Crackling Drake's power is equal to the total number of instant and "
         'sorcery cards you own in exile and in your graveyard.',
 121556: "As long as you've surveilled this turn, Darkblade Agent has "
         'deathtouch and "Whenever this creature deals combat damage to a '
         'player, you draw a card."',
 121557: 'Choose one or both   Exile target artifact.  Exile target '
         'enchantment.',
 121558: 'Choose one or both   Deafening Clarion deals 3 damage to each '
         'creature.  Creatures you control gain lifelink until end of turn.',
 121559: 'When Disinformation Campaign enters the battlefield, you draw a card '
         'and each opponent discards a card.',
 121560: "Whenever you surveil, return Disinformation Campaign to its owner's "
         'hand.',
 121561: 'Whenever Emmara, Soul of the Accord becomes tapped, create a 1/1 '
         'white Soldier creature token with lifelink.',
 121562: 'Discard a creature card: Erstwhile Trooper gets +2/+2 and gains '
         'trample until end of turn. Activate this ability only once each '
         'turn.',
 121564: '{oT}, Sacrifice Bounty Agent: Destroy target legendary permanent '
         "that's an artifact, creature, or enchantment.",
 121565: 'Destroy all creatures with toughness 4 or greater.',
 121566: 'Whenever Etrata deals combat damage to a player, exile target '
         'creature that player controls and put a hit counter on that card. '
         'That player loses the game if they own three or more exiled cards '
         "with hit counters on them. Etrata's owner shuffles Etrata into their "
         'library.',
 121567: 'Whenever you gain life, you may pay {o2}. If you do, draw a card.',
 121568: '{o3oW}: Create a 1/1 white Soldier creature token with lifelink.',
 121569: 'If one or more creature tokens would be created under your control, '
         'that many 4/4 white Angel creature tokens with flying and vigilance '
         'are created instead.',
 121570: 'Whenever Haazda Marshal and at least two other creatures attack, '
         'create a 1/1 white Soldier creature token with lifelink.',
 121571: 'When Hunted Witness dies, create a 1/1 white Soldier creature token '
         'with lifelink.',
 121572: 'Whenever Inspiring Unicorn attacks, creatures you control get +1/+1 '
         'until end of turn.',
 122112: '{oX}: Lazav, the Multifarious becomes a copy of target creature card '
         'in your graveyard with converted mana cost X, except its name is '
         "Lazav, the Multifarious, it's legendary in addition to its other "
         'types, and it has this ability.',
 133045: 'Switch the power and toughness of each of up to two target creatures '
         'until end of turn.'}
