
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


AngelofGrace = Card(name="angel_of_grace", pretty_name="Angel of Grace", cost=['3', 'W', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Angel",
                    abilities=[7, 8, 122094, 122095], set_id="RNA", rarity="Mythic Rare", set_number=1,
                    mtga_id=69129)
AngelicExaltation = Card(name="angelic_exaltation", pretty_name="Angelic Exaltation", cost=['3', 'W'],
                         color_identity=['W'], card_type="Enchantment", sub_types="",
                         abilities=[122096], set_id="RNA", rarity="Uncommon", set_number=2,
                         mtga_id=69130)
ArchwayAngel = Card(name="archway_angel", pretty_name="Archway Angel", cost=['5', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Angel",
                    abilities=[8, 122085], set_id="RNA", rarity="Uncommon", set_number=3,
                    mtga_id=69131)
ArrestersZeal = Card(name="arresters_zeal", pretty_name="Arrester's Zeal", cost=['W'],
                     color_identity=['W'], card_type="Instant", sub_types="",
                     abilities=[122098], set_id="RNA", rarity="Common", set_number=4,
                     mtga_id=69132)
BringtoTrial = Card(name="bring_to_trial", pretty_name="Bring to Trial", cost=['2', 'W'],
                    color_identity=['W'], card_type="Sorcery", sub_types="",
                    abilities=[122099], set_id="RNA", rarity="Common", set_number=5,
                    mtga_id=69133)
CivicStalwart = Card(name="civic_stalwart", pretty_name="Civic Stalwart", cost=['3', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Elephant Soldier",
                     abilities=[63634], set_id="RNA", rarity="Common", set_number=6,
                     mtga_id=69134)
ConcordiaPegasus = Card(name="concordia_pegasus", pretty_name="Concordia Pegasus", cost=['1', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Pegasus",
                        abilities=[8], set_id="RNA", rarity="Common", set_number=7,
                        mtga_id=69135)
ExposetoDaylight = Card(name="expose_to_daylight", pretty_name="Expose to Daylight", cost=['2', 'W'],
                        color_identity=['W'], card_type="Instant", sub_types="",
                        abilities=[122100], set_id="RNA", rarity="Common", set_number=8,
                        mtga_id=69136)
ForbiddingSpirit = Card(name="forbidding_spirit", pretty_name="Forbidding Spirit", cost=['1', 'W', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Spirit Cleric",
                        abilities=[122101], set_id="RNA", rarity="Uncommon", set_number=9,
                        mtga_id=69137)
HaazdaOfficer = Card(name="haazda_officer", pretty_name="Haazda Officer", cost=['2', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                     abilities=[103263], set_id="RNA", rarity="Common", set_number=10,
                     mtga_id=69138)
HeroofPrecinctOne = Card(name="hero_of_precinct_one", pretty_name="Hero of Precinct One", cost=['1', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Human Warrior",
                         abilities=[122103], set_id="RNA", rarity="Rare", set_number=11,
                         mtga_id=69139)
ImpassionedOrator = Card(name="impassioned_orator", pretty_name="Impassioned Orator", cost=['1', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                         abilities=[122104], set_id="RNA", rarity="Common", set_number=12,
                         mtga_id=69140)
JusticiarsPortal = Card(name="justiciars_portal", pretty_name="Justiciar's Portal", cost=['1', 'W'],
                        color_identity=['W'], card_type="Instant", sub_types="",
                        abilities=[122105], set_id="RNA", rarity="Common", set_number=13,
                        mtga_id=69141)
KnightofSorrows = Card(name="knight_of_sorrows", pretty_name="Knight of Sorrows", cost=['4', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                       abilities=[76869, 122106], set_id="RNA", rarity="Common", set_number=14,
                       mtga_id=69142)
LumberingBattlement = Card(name="lumbering_battlement", pretty_name="Lumbering Battlement", cost=['4', 'W'],
                           color_identity=['W'], card_type="Creature", sub_types="Beast",
                           abilities=[15, 122063, 122108], set_id="RNA", rarity="Rare", set_number=15,
                           mtga_id=69143)
MinistrantofObligation = Card(name="ministrant_of_obligation", pretty_name="Ministrant of Obligation", cost=['2', 'W'],
                              color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                              abilities=[122109], set_id="RNA", rarity="Uncommon", set_number=16,
                              mtga_id=69144)
ProwlingCaracal = Card(name="prowling_caracal", pretty_name="Prowling Caracal", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Cat",
                       abilities=[], set_id="RNA", rarity="Common", set_number=17,
                       mtga_id=69145)
RallytoBattle = Card(name="rally_to_battle", pretty_name="Rally to Battle", cost=['3', 'W'],
                     color_identity=['W'], card_type="Instant", sub_types="",
                     abilities=[121856], set_id="RNA", rarity="Uncommon", set_number=18,
                     mtga_id=69146)
ResoluteWatchdog = Card(name="resolute_watchdog", pretty_name="Resolute Watchdog", cost=['W'],
                        color_identity=['W'], card_type="Creature", sub_types="Hound",
                        abilities=[2, 122002], set_id="RNA", rarity="Uncommon", set_number=19,
                        mtga_id=69147)
SentinelsMark = Card(name="sentinels_mark", pretty_name="Sentinel's Mark", cost=['1', 'W'],
                     color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                     abilities=[7, 1027, 17633, 121879], set_id="RNA", rarity="Uncommon", set_number=20,
                     mtga_id=69148)
SkyTether = Card(name="sky_tether", pretty_name="Sky Tether", cost=['W'],
                 color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                 abilities=[1027, 121895], set_id="RNA", rarity="Uncommon", set_number=21,
                 mtga_id=69149)
SmotheringTithe = Card(name="smothering_tithe", pretty_name="Smothering Tithe", cost=['3', 'W'],
                       color_identity=['W'], card_type="Enchantment", sub_types="",
                       abilities=[121936], set_id="RNA", rarity="Rare", set_number=22,
                       mtga_id=69150)
SpiritoftheSpires = Card(name="spirit_of_the_spires", pretty_name="Spirit of the Spires", cost=['3', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Spirit",
                         abilities=[8, 12891], set_id="RNA", rarity="Uncommon", set_number=23,
                         mtga_id=69151)
SummaryJudgment = Card(name="summary_judgment", pretty_name="Summary Judgment", cost=['1', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[121981], set_id="RNA", rarity="Common", set_number=24,
                       mtga_id=69152)
SyndicateMessenger = Card(name="syndicate_messenger", pretty_name="Syndicate Messenger", cost=['3', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Bird",
                          abilities=[8, 122106], set_id="RNA", rarity="Common", set_number=25,
                          mtga_id=69153)
TenthDistrictVeteran = Card(name="tenth_district_veteran", pretty_name="Tenth District Veteran", cost=['2', 'W'],
                            color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                            abilities=[15, 122001], set_id="RNA", rarity="Common", set_number=26,
                            mtga_id=69154)
TitheTaker = Card(name="tithe_taker", pretty_name="Tithe Taker", cost=['1', 'W'],
                  color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                  abilities=[122007, 122106], set_id="RNA", rarity="Rare", set_number=27,
                  mtga_id=69155)
TwilightPanther = Card(name="twilight_panther", pretty_name="Twilight Panther", cost=['W'],
                       color_identity=['B', 'W'], card_type="Creature", sub_types="Cat Spirit",
                       abilities=[94573], set_id="RNA", rarity="Common", set_number=28,
                       mtga_id=69156)
UnbreakableFormation = Card(name="unbreakable_formation", pretty_name="Unbreakable Formation", cost=['2', 'W'],
                            color_identity=['W'], card_type="Instant", sub_types="",
                            abilities=[122018], set_id="RNA", rarity="Rare", set_number=29,
                            mtga_id=69157)
WatchfulGiant = Card(name="watchful_giant", pretty_name="Watchful Giant", cost=['5', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Giant Soldier",
                     abilities=[99786], set_id="RNA", rarity="Common", set_number=30,
                     mtga_id=69158)
ArrestersAdmonition = Card(name="arresters_admonition", pretty_name="Arrester's Admonition", cost=['2', 'U'],
                           color_identity=['U'], card_type="Instant", sub_types="",
                           abilities=[122028], set_id="RNA", rarity="Common", set_number=31,
                           mtga_id=69159)
BenthicBiomancer = Card(name="benthic_biomancer", pretty_name="Benthic Biomancer", cost=['U'],
                        color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard Mutant",
                        abilities=[122034, 121857], set_id="RNA", rarity="Rare", set_number=32,
                        mtga_id=69160)
Chillbringer = Card(name="chillbringer", pretty_name="Chillbringer", cost=['4', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Elemental",
                    abilities=[8, 121858], set_id="RNA", rarity="Common", set_number=33,
                    mtga_id=69161)
CleartheMind = Card(name="clear_the_mind", pretty_name="Clear the Mind", cost=['2', 'U'],
                    color_identity=['U'], card_type="Sorcery", sub_types="",
                    abilities=[25851, 25848], set_id="RNA", rarity="Common", set_number=34,
                    mtga_id=69162)
CodeofConstraint = Card(name="code_of_constraint", pretty_name="Code of Constraint", cost=['2', 'U'],
                        color_identity=['U'], card_type="Instant", sub_types="",
                        abilities=[122115], set_id="RNA", rarity="Uncommon", set_number=35,
                        mtga_id=69163)
CoralCommando = Card(name="coral_commando", pretty_name="Coral Commando", cost=['2', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                     abilities=[], set_id="RNA", rarity="Common", set_number=36,
                     mtga_id=69164)
EssenceCapture = Card(name="essence_capture", pretty_name="Essence Capture", cost=['U', 'U'],
                      color_identity=['U'], card_type="Instant", sub_types="",
                      abilities=[121874], set_id="RNA", rarity="Uncommon", set_number=37,
                      mtga_id=69165)
EyesEverywhere = Card(name="eyes_everywhere", pretty_name="Eyes Everywhere", cost=['2', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="",
                      abilities=[20495, 122067], set_id="RNA", rarity="Uncommon", set_number=38,
                      mtga_id=69166)
FaerieDuelist = Card(name="faerie_duelist", pretty_name="Faerie Duelist", cost=['1', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Faerie Rogue",
                     abilities=[7, 8, 122072], set_id="RNA", rarity="Common", set_number=39,
                     mtga_id=69167)
GatewaySneak = Card(name="gateway_sneak", pretty_name="Gateway Sneak", cost=['2', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Vedalken Rogue",
                    abilities=[122075, 92932], set_id="RNA", rarity="Uncommon", set_number=40,
                    mtga_id=69168)
Humongulus = Card(name="humongulus", pretty_name="Humongulus", cost=['4', 'U'],
                  color_identity=['U'], card_type="Creature", sub_types="Homunculus",
                  abilities=[10], set_id="RNA", rarity="Common", set_number=41,
                  mtga_id=69169)
MassManipulation = Card(name="mass_manipulation", pretty_name="Mass Manipulation", cost=['X', 'X', 'U', 'U', 'U', 'U'],
                        color_identity=['U'], card_type="Sorcery", sub_types="",
                        abilities=[121882], set_id="RNA", rarity="Rare", set_number=42,
                        mtga_id=69170)
MesmerizingBenthid = Card(name="mesmerizing_benthid", pretty_name="Mesmerizing Benthid", cost=['3', 'U', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Octopus",
                          abilities=[121894, 121899], set_id="RNA", rarity="Mythic Rare", set_number=43,
                          mtga_id=69171)
PersistentPetitioners = Card(name="persistent_petitioners", pretty_name="Persistent Petitioners", cost=['1', 'U'],
                             color_identity=['U'], card_type="Creature", sub_types="Human Advisor",
                             abilities=[121904, 121909, 88192], set_id="RNA", rarity="Common", set_number=44,
                             mtga_id=69172)
PrecognitivePerception = Card(name="precognitive_perception", pretty_name="Precognitive Perception", cost=['3', 'U', 'U'],
                              color_identity=['U'], card_type="Instant", sub_types="",
                              abilities=[121918], set_id="RNA", rarity="Rare", set_number=45,
                              mtga_id=69173)
PryingEyes = Card(name="prying_eyes", pretty_name="Prying Eyes", cost=['4', 'U', 'U'],
                  color_identity=['U'], card_type="Instant", sub_types="",
                  abilities=[19615], set_id="RNA", rarity="Common", set_number=46,
                  mtga_id=69174)
Pteramander = Card(name="pteramander", pretty_name="Pteramander", cost=['U'],
                   color_identity=['U'], card_type="Creature", sub_types="Salamander Drake",
                   abilities=[8, 121923], set_id="RNA", rarity="Uncommon", set_number=47,
                   mtga_id=69175)
Quench = Card(name="quench", pretty_name="Quench", cost=['1', 'U'],
              color_identity=['U'], card_type="Instant", sub_types="",
              abilities=[6374], set_id="RNA", rarity="Common", set_number=48,
              mtga_id=69176)
SagesRowSavant = Card(name="sages_row_savant", pretty_name="Sage's Row Savant", cost=['1', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Vedalken Wizard",
                      abilities=[100685], set_id="RNA", rarity="Common", set_number=49,
                      mtga_id=69177)
SenateCourier = Card(name="senate_courier", pretty_name="Senate Courier", cost=['2', 'U'],
                     color_identity=['W', 'U'], card_type="Creature", sub_types="Bird",
                     abilities=[8, 88910], set_id="RNA", rarity="Common", set_number=50,
                     mtga_id=69178)
ShimmerofPossibility = Card(name="shimmer_of_possibility", pretty_name="Shimmer of Possibility", cost=['1', 'U'],
                            color_identity=['U'], card_type="Sorcery", sub_types="",
                            abilities=[121940], set_id="RNA", rarity="Common", set_number=51,
                            mtga_id=69179)
SkatewingSpy = Card(name="skatewing_spy", pretty_name="Skatewing Spy", cost=['3', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Vedalken Rogue Mutant",
                    abilities=[121946, 19694], set_id="RNA", rarity="Uncommon", set_number=52,
                    mtga_id=69180)
SkitterEel = Card(name="skitter_eel", pretty_name="Skitter Eel", cost=['3', 'U'],
                  color_identity=['U'], card_type="Creature", sub_types="Fish Crab",
                  abilities=[121954], set_id="RNA", rarity="Common", set_number=53,
                  mtga_id=69181)
Slimebind = Card(name="slimebind", pretty_name="Slimebind", cost=['1', 'U'],
                 color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                 abilities=[7, 1027, 121959], set_id="RNA", rarity="Common", set_number=54,
                 mtga_id=69182)
SphinxofForesight = Card(name="sphinx_of_foresight", pretty_name="Sphinx of Foresight", cost=['2', 'U', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                         abilities=[121964, 8, 20495], set_id="RNA", rarity="Rare", set_number=55,
                         mtga_id=69183)
SwirlingTorrent = Card(name="swirling_torrent", pretty_name="Swirling Torrent", cost=['5', 'U'],
                       color_identity=['U'], card_type="Sorcery", sub_types="",
                       abilities=[121975], set_id="RNA", rarity="Uncommon", set_number=56,
                       mtga_id=69184)
ThoughtCollapse = Card(name="thought_collapse", pretty_name="Thought Collapse", cost=['1', 'U', 'U'],
                       color_identity=['U'], card_type="Instant", sub_types="",
                       abilities=[121980], set_id="RNA", rarity="Common", set_number=57,
                       mtga_id=69185)
VerityCircle = Card(name="verity_circle", pretty_name="Verity Circle", cost=['2', 'U'],
                    color_identity=['U'], card_type="Enchantment", sub_types="",
                    abilities=[121984, 121990], set_id="RNA", rarity="Rare", set_number=58,
                    mtga_id=69186)
WallofLostThoughts = Card(name="wall_of_lost_thoughts", pretty_name="Wall of Lost Thoughts", cost=['1', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Wall",
                          abilities=[2, 100740], set_id="RNA", rarity="Uncommon", set_number=59,
                          mtga_id=69187)
WindstormDrake = Card(name="windstorm_drake", pretty_name="Windstorm Drake", cost=['4', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Drake",
                      abilities=[8, 121999], set_id="RNA", rarity="Uncommon", set_number=60,
                      mtga_id=69188)
AwakentheErstwhile = Card(name="awaken_the_erstwhile", pretty_name="Awaken the Erstwhile", cost=['3', 'B', 'B'],
                          color_identity=['B'], card_type="Sorcery", sub_types="",
                          abilities=[122000], set_id="RNA", rarity="Rare", set_number=61,
                          mtga_id=69189)
BankruptinBlood = Card(name="bankrupt_in_blood", pretty_name="Bankrupt in Blood", cost=['1', 'B'],
                       color_identity=['B'], card_type="Sorcery", sub_types="",
                       abilities=[94180, 1746], set_id="RNA", rarity="Uncommon", set_number=62,
                       mtga_id=69190)
BladeJuggler = Card(name="blade_juggler", pretty_name="Blade Juggler", cost=['4', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Human Rogue",
                    abilities=[122005, 122006], set_id="RNA", rarity="Common", set_number=63,
                    mtga_id=69191)
Bladebrand = Card(name="bladebrand", pretty_name="Bladebrand", cost=['1', 'B'],
                  color_identity=['B'], card_type="Instant", sub_types="",
                  abilities=[4294, 25848], set_id="RNA", rarity="Common", set_number=64,
                  mtga_id=69192)
BloodmistInfiltrator = Card(name="bloodmist_infiltrator", pretty_name="Bloodmist Infiltrator", cost=['2', 'B'],
                            color_identity=['B'], card_type="Creature", sub_types="Vampire",
                            abilities=[122008], set_id="RNA", rarity="Uncommon", set_number=65,
                            mtga_id=69193)
CarrionImp = Card(name="carrion_imp", pretty_name="Carrion Imp", cost=['3', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Imp",
                  abilities=[8, 122009], set_id="RNA", rarity="Common", set_number=66,
                  mtga_id=69194)
CatacombCrocodile = Card(name="catacomb_crocodile", pretty_name="Catacomb Crocodile", cost=['4', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Crocodile",
                         abilities=[], set_id="RNA", rarity="Common", set_number=67,
                         mtga_id=69195)
CleartheStage = Card(name="clear_the_stage", pretty_name="Clear the Stage", cost=['4', 'B'],
                     color_identity=['B'], card_type="Instant", sub_types="",
                     abilities=[122010], set_id="RNA", rarity="Uncommon", set_number=68,
                     mtga_id=69196)
ConsigntothePit = Card(name="consign_to_the_pit", pretty_name="Consign to the Pit", cost=['5', 'B'],
                       color_identity=['B'], card_type="Sorcery", sub_types="",
                       abilities=[122012], set_id="RNA", rarity="Common", set_number=69,
                       mtga_id=69197)
CryoftheCarnarium = Card(name="cry_of_the_carnarium", pretty_name="Cry of the Carnarium", cost=['1', 'B', 'B'],
                         color_identity=['B'], card_type="Sorcery", sub_types="",
                         abilities=[122013], set_id="RNA", rarity="Uncommon", set_number=70,
                         mtga_id=69198)
DeadRevels = Card(name="dead_revels", pretty_name="Dead Revels", cost=['3', 'B'],
                  color_identity=['B'], card_type="Sorcery", sub_types="",
                  abilities=[122014, 1923], set_id="RNA", rarity="Common", set_number=71,
                  mtga_id=69199)
DebtorsTransport = Card(name="debtors_transport", pretty_name="Debtors' Transport", cost=['5', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Thrull",
                        abilities=[122109], set_id="RNA", rarity="Common", set_number=72,
                        mtga_id=69200)
DrillBit = Card(name="drill_bit", pretty_name="Drill Bit", cost=['2', 'B'],
                color_identity=['B'], card_type="Sorcery", sub_types="",
                abilities=[122015, 1074], set_id="RNA", rarity="Uncommon", set_number=73,
                mtga_id=69201)
FontofAgonies = Card(name="font_of_agonies", pretty_name="Font of Agonies", cost=['B'],
                     color_identity=['B'], card_type="Enchantment", sub_types="",
                     abilities=[122017, 122019], set_id="RNA", rarity="Rare", set_number=74,
                     mtga_id=69202)
GrotesqueDemise = Card(name="grotesque_demise", pretty_name="Grotesque Demise", cost=['2', 'B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[62243], set_id="RNA", rarity="Common", set_number=75,
                       mtga_id=69203)
Gutterbones = Card(name="gutterbones", pretty_name="Gutterbones", cost=['B'],
                   color_identity=['B'], card_type="Creature", sub_types="Skeleton Warrior",
                   abilities=[76735, 122021], set_id="RNA", rarity="Rare", set_number=76,
                   mtga_id=69204)
IllGottenInheritance = Card(name="illgotten_inheritance", pretty_name="Ill-Gotten Inheritance", cost=['3', 'B'],
                            color_identity=['B'], card_type="Enchantment", sub_types="",
                            abilities=[122022, 122024], set_id="RNA", rarity="Common", set_number=77,
                            mtga_id=69205)
NoxiousGroodion = Card(name="noxious_groodion", pretty_name="Noxious Groodion", cost=['2', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Beast",
                       abilities=[1], set_id="RNA", rarity="Common", set_number=78,
                       mtga_id=69206)
OrzhovEnforcer = Card(name="orzhov_enforcer", pretty_name="Orzhov Enforcer", cost=['1', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Human Rogue",
                      abilities=[1, 122106], set_id="RNA", rarity="Uncommon", set_number=79,
                      mtga_id=69207)
OrzhovRacketeers = Card(name="orzhov_racketeers", pretty_name="Orzhov Racketeers", cost=['4', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Human Rogue",
                        abilities=[88861, 122109], set_id="RNA", rarity="Uncommon", set_number=80,
                        mtga_id=69208)
PestilentSpirit = Card(name="pestilent_spirit", pretty_name="Pestilent Spirit", cost=['2', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Spirit",
                       abilities=[142, 1, 122025], set_id="RNA", rarity="Rare", set_number=81,
                       mtga_id=69209)
PlagueWight = Card(name="plague_wight", pretty_name="Plague Wight", cost=['1', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Zombie",
                   abilities=[122026], set_id="RNA", rarity="Common", set_number=82,
                   mtga_id=69210)
PriestofForgottenGods = Card(name="priest_of_forgotten_gods", pretty_name="Priest of Forgotten Gods", cost=['1', 'B'],
                             color_identity=['B'], card_type="Creature", sub_types="Human Cleric",
                             abilities=[122027], set_id="RNA", rarity="Rare", set_number=83,
                             mtga_id=69211)
RakdosTrumpeter = Card(name="rakdos_trumpeter", pretty_name="Rakdos Trumpeter", cost=['1', 'B'],
                       color_identity=['R', 'B'], card_type="Creature", sub_types="Human Shaman",
                       abilities=[142, 122029], set_id="RNA", rarity="Common", set_number=84,
                       mtga_id=69212)
SpawnofMayhem = Card(name="spawn_of_mayhem", pretty_name="Spawn of Mayhem", cost=['2', 'B', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Demon",
                     abilities=[122031, 8, 14, 122032], set_id="RNA", rarity="Mythic Rare", set_number=85,
                     mtga_id=69213)
SpireMangler = Card(name="spire_mangler", pretty_name="Spire Mangler", cost=['2', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Insect",
                    abilities=[7, 8, 122033], set_id="RNA", rarity="Uncommon", set_number=86,
                    mtga_id=69214)
ThirstingShade = Card(name="thirsting_shade", pretty_name="Thirsting Shade", cost=['B'],
                      color_identity=['B'], card_type="Creature", sub_types="Shade",
                      abilities=[12, 93172], set_id="RNA", rarity="Common", set_number=87,
                      mtga_id=69215)
UndercityScavenger = Card(name="undercity_scavenger", pretty_name="Undercity Scavenger", cost=['3', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Ogre Warrior",
                          abilities=[122035], set_id="RNA", rarity="Common", set_number=88,
                          mtga_id=69216)
UndercitysEmbrace = Card(name="undercitys_embrace", pretty_name="Undercity's Embrace", cost=['2', 'B'],
                         color_identity=['B'], card_type="Instant", sub_types="",
                         abilities=[122036], set_id="RNA", rarity="Common", set_number=89,
                         mtga_id=69217)
VindictiveVampire = Card(name="vindictive_vampire", pretty_name="Vindictive Vampire", cost=['3', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Vampire",
                         abilities=[122039], set_id="RNA", rarity="Uncommon", set_number=90,
                         mtga_id=69218)
ActofTreason = Card(name="act_of_treason", pretty_name="Act of Treason", cost=['2', 'R'],
                    color_identity=['R'], card_type="Sorcery", sub_types="",
                    abilities=[1278], set_id="RNA", rarity="Common", set_number=91,
                    mtga_id=69219)
Amplifire = Card(name="amplifire", pretty_name="Amplifire", cost=['2', 'R', 'R'],
                 color_identity=['R'], card_type="Creature", sub_types="Elemental",
                 abilities=[122040], set_id="RNA", rarity="Rare", set_number=92,
                 mtga_id=69220)
BurnBright = Card(name="burn_bright", pretty_name="Burn Bright", cost=['2', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[23611], set_id="RNA", rarity="Common", set_number=93,
                  mtga_id=69221)
BurningTreeVandal = Card(name="burningtree_vandal", pretty_name="Burning-Tree Vandal", cost=['2', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Human Rogue",
                         abilities=[175, 101881], set_id="RNA", rarity="Common", set_number=94,
                         mtga_id=69222)
CavalcadeofCalamity = Card(name="cavalcade_of_calamity", pretty_name="Cavalcade of Calamity", cost=['1', 'R'],
                           color_identity=['R'], card_type="Enchantment", sub_types="",
                           abilities=[122044], set_id="RNA", rarity="Uncommon", set_number=95,
                           mtga_id=69223)
ClamorShaman = Card(name="clamor_shaman", pretty_name="Clamor Shaman", cost=['2', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Goblin Shaman",
                    abilities=[175, 122045], set_id="RNA", rarity="Uncommon", set_number=96,
                    mtga_id=69224)
DaggerCaster = Card(name="dagger_caster", pretty_name="Dagger Caster", cost=['3', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Viashino Rogue",
                    abilities=[122047], set_id="RNA", rarity="Uncommon", set_number=97,
                    mtga_id=69225)
Deface = Card(name="deface", pretty_name="Deface", cost=['R'],
              color_identity=['R'], card_type="Sorcery", sub_types="",
              abilities=[122048], set_id="RNA", rarity="Common", set_number=98,
              mtga_id=69226)
Electrodominance = Card(name="electrodominance", pretty_name="Electrodominance", cost=['X', 'R', 'R'],
                        color_identity=['R'], card_type="Instant", sub_types="",
                        abilities=[122049], set_id="RNA", rarity="Rare", set_number=99,
                        mtga_id=69227)
FeralMaaka = Card(name="feral_maaka", pretty_name="Feral Maaka", cost=['1', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Cat",
                  abilities=[], set_id="RNA", rarity="Common", set_number=100,
                  mtga_id=69228)
FlamesoftheRazeBoar = Card(name="flames_of_the_razeboar", pretty_name="Flames of the Raze-Boar", cost=['5', 'R'],
                           color_identity=['R'], card_type="Instant", sub_types="",
                           abilities=[122050], set_id="RNA", rarity="Uncommon", set_number=101,
                           mtga_id=69229)
GatesAblaze = Card(name="gates_ablaze", pretty_name="Gates Ablaze", cost=['2', 'R'],
                   color_identity=['R'], card_type="Sorcery", sub_types="",
                   abilities=[122051], set_id="RNA", rarity="Uncommon", set_number=102,
                   mtga_id=69230)
GhorClanWrecker = Card(name="ghorclan_wrecker", pretty_name="Ghor-Clan Wrecker", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Human Warrior",
                       abilities=[175, 142], set_id="RNA", rarity="Common", set_number=103,
                       mtga_id=69231)
GoblinGathering = Card(name="goblin_gathering", pretty_name="Goblin Gathering", cost=['2', 'R'],
                       color_identity=['R'], card_type="Sorcery", sub_types="",
                       abilities=[122052], set_id="RNA", rarity="Common", set_number=104,
                       mtga_id=69232)
GravelHideGoblin = Card(name="gravelhide_goblin", pretty_name="Gravel-Hide Goblin", cost=['1', 'R'],
                        color_identity=['G', 'R'], card_type="Creature", sub_types="Goblin Shaman",
                        abilities=[122053], set_id="RNA", rarity="Common", set_number=105,
                        mtga_id=69233)
ImmolationShaman = Card(name="immolation_shaman", pretty_name="Immolation Shaman", cost=['1', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Viashino Shaman",
                        abilities=[121859, 121860], set_id="RNA", rarity="Rare", set_number=106,
                        mtga_id=69234)
LightUptheStage = Card(name="light_up_the_stage", pretty_name="Light Up the Stage", cost=['2', 'R'],
                       color_identity=['R'], card_type="Sorcery", sub_types="",
                       abilities=[121861, 121862], set_id="RNA", rarity="Uncommon", set_number=107,
                       mtga_id=69235)
MirrorMarch = Card(name="mirror_march", pretty_name="Mirror March", cost=['5', 'R'],
                   color_identity=['R'], card_type="Enchantment", sub_types="",
                   abilities=[121863], set_id="RNA", rarity="Rare", set_number=108,
                   mtga_id=69236)
RixMaadiReveler = Card(name="rix_maadi_reveler", pretty_name="Rix Maadi Reveler", cost=['1', 'R'],
                       color_identity=['B', 'R'], card_type="Creature", sub_types="Human Shaman",
                       abilities=[121864, 121865], set_id="RNA", rarity="Rare", set_number=109,
                       mtga_id=69237)
RubbleReading = Card(name="rubble_reading", pretty_name="Rubble Reading", cost=['3', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[121866], set_id="RNA", rarity="Common", set_number=110,
                     mtga_id=69238)
RubblebeltRecluse = Card(name="rubblebelt_recluse", pretty_name="Rubblebelt Recluse", cost=['4', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Ogre Berserker",
                         abilities=[76824], set_id="RNA", rarity="Common", set_number=111,
                         mtga_id=69239)
RumblingRuin = Card(name="rumbling_ruin", pretty_name="Rumbling Ruin", cost=['5', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Elemental",
                    abilities=[122054], set_id="RNA", rarity="Uncommon", set_number=112,
                    mtga_id=69240)
Scorchmark = Card(name="scorchmark", pretty_name="Scorchmark", cost=['1', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[7344], set_id="RNA", rarity="Common", set_number=113,
                  mtga_id=69241)
SkarrganHellkite = Card(name="skarrgan_hellkite", pretty_name="Skarrgan Hellkite", cost=['3', 'R', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Dragon",
                        abilities=[175, 8, 121867], set_id="RNA", rarity="Mythic Rare", set_number=114,
                        mtga_id=69242)
SkewertheCritics = Card(name="skewer_the_critics", pretty_name="Skewer the Critics", cost=['2', 'R'],
                        color_identity=['R'], card_type="Sorcery", sub_types="",
                        abilities=[121861, 70361], set_id="RNA", rarity="Common", set_number=115,
                        mtga_id=69243)
SmeltWardIgnus = Card(name="smeltward_ignus", pretty_name="Smelt-Ward Ignus", cost=['1', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Elemental",
                      abilities=[121868], set_id="RNA", rarity="Uncommon", set_number=116,
                      mtga_id=69244)
SpearSpewer = Card(name="spear_spewer", pretty_name="Spear Spewer", cost=['R'],
                   color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                   abilities=[2, 121869], set_id="RNA", rarity="Common", set_number=117,
                   mtga_id=69245)
SpikewheelAcrobat = Card(name="spikewheel_acrobat", pretty_name="Spikewheel Acrobat", cost=['3', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Human Rogue",
                         abilities=[121870], set_id="RNA", rarity="Common", set_number=118,
                         mtga_id=69246)
StormStrike = Card(name="storm_strike", pretty_name="Storm Strike", cost=['R'],
                   color_identity=['R'], card_type="Instant", sub_types="",
                   abilities=[122058], set_id="RNA", rarity="Common", set_number=119,
                   mtga_id=69247)
TinStreetDodger = Card(name="tin_street_dodger", pretty_name="Tin Street Dodger", cost=['R'],
                       color_identity=['R'], card_type="Creature", sub_types="Goblin Rogue",
                       abilities=[9, 122059], set_id="RNA", rarity="Uncommon", set_number=120,
                       mtga_id=69248)
AxebaneBeast = Card(name="axebane_beast", pretty_name="Axebane Beast", cost=['3', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Beast",
                    abilities=[], set_id="RNA", rarity="Common", set_number=121,
                    mtga_id=69249)
BiogenicOoze = Card(name="biogenic_ooze", pretty_name="Biogenic Ooze", cost=['3', 'G', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Ooze",
                    abilities=[122060, 122061, 122062], set_id="RNA", rarity="Mythic Rare", set_number=122,
                    mtga_id=69250)
BiogenicUpgrade = Card(name="biogenic_upgrade", pretty_name="Biogenic Upgrade", cost=['4', 'G', 'G'],
                       color_identity=['G'], card_type="Sorcery", sub_types="",
                       abilities=[122064], set_id="RNA", rarity="Uncommon", set_number=123,
                       mtga_id=69251)
EndRazeForerunners = Card(name="endraze_forerunners", pretty_name="End-Raze Forerunners", cost=['5', 'G', 'G', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Boar",
                          abilities=[15, 14, 9, 122065], set_id="RNA", rarity="Rare", set_number=124,
                          mtga_id=69252)
EnragedCeratok = Card(name="enraged_ceratok", pretty_name="Enraged Ceratok", cost=['2', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Rhino",
                      abilities=[87941], set_id="RNA", rarity="Uncommon", set_number=125,
                      mtga_id=69253)
GatebreakerRam = Card(name="gatebreaker_ram", pretty_name="Gatebreaker Ram", cost=['2', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Sheep",
                      abilities=[122066, 121871], set_id="RNA", rarity="Uncommon", set_number=126,
                      mtga_id=69254)
GiftofStrength = Card(name="gift_of_strength", pretty_name="Gift of Strength", cost=['1', 'G'],
                      color_identity=['G'], card_type="Instant", sub_types="",
                      abilities=[103821], set_id="RNA", rarity="Common", set_number=127,
                      mtga_id=69255)
GrowthChamberGuardian = Card(name="growthchamber_guardian", pretty_name="Growth-Chamber Guardian", cost=['1', 'G'],
                             color_identity=['G'], card_type="Creature", sub_types="Elf Crab Warrior",
                             abilities=[122068, 122069], set_id="RNA", rarity="Rare", set_number=128,
                             mtga_id=69256)
GruulBeastmaster = Card(name="gruul_beastmaster", pretty_name="Gruul Beastmaster", cost=['3', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Human Shaman",
                        abilities=[175, 122070], set_id="RNA", rarity="Uncommon", set_number=129,
                        mtga_id=69257)
GuardianProject = Card(name="guardian_project", pretty_name="Guardian Project", cost=['3', 'G'],
                       color_identity=['G'], card_type="Enchantment", sub_types="",
                       abilities=[122071], set_id="RNA", rarity="Rare", set_number=130,
                       mtga_id=69258)
IncubationDruid = Card(name="incubation_druid", pretty_name="Incubation Druid", cost=['1', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                       abilities=[122073, 121873], set_id="RNA", rarity="Rare", set_number=131,
                       mtga_id=69259)
MammothSpider = Card(name="mammoth_spider", pretty_name="Mammoth Spider", cost=['4', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Spider",
                     abilities=[13], set_id="RNA", rarity="Common", set_number=132,
                     mtga_id=69260)
OpentheGates = Card(name="open_the_gates", pretty_name="Open the Gates", cost=['G'],
                    color_identity=['G'], card_type="Sorcery", sub_types="",
                    abilities=[122074], set_id="RNA", rarity="Common", set_number=133,
                    mtga_id=69261)
RampageoftheClans = Card(name="rampage_of_the_clans", pretty_name="Rampage of the Clans", cost=['3', 'G'],
                         color_identity=['G'], card_type="Instant", sub_types="",
                         abilities=[121875], set_id="RNA", rarity="Rare", set_number=134,
                         mtga_id=69262)
RampagingRendhorn = Card(name="rampaging_rendhorn", pretty_name="Rampaging Rendhorn", cost=['4', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Beast",
                         abilities=[175], set_id="RNA", rarity="Common", set_number=135,
                         mtga_id=69263)
Regenesis = Card(name="regenesis", pretty_name="Regenesis", cost=['3', 'G', 'G'],
                 color_identity=['G'], card_type="Instant", sub_types="",
                 abilities=[121876], set_id="RNA", rarity="Uncommon", set_number=136,
                 mtga_id=69264)
RootSnare = Card(name="root_snare", pretty_name="Root Snare", cost=['1', 'G'],
                 color_identity=['G'], card_type="Instant", sub_types="",
                 abilities=[27746], set_id="RNA", rarity="Common", set_number=137,
                 mtga_id=69265)
SagittarsVolley = Card(name="sagittars_volley", pretty_name="Sagittars' Volley", cost=['2', 'G'],
                       color_identity=['G'], card_type="Instant", sub_types="",
                       abilities=[122077], set_id="RNA", rarity="Common", set_number=138,
                       mtga_id=69266)
SaruliCaretaker = Card(name="saruli_caretaker", pretty_name="Saruli Caretaker", cost=['G'],
                       color_identity=['G'], card_type="Creature", sub_types="Dryad",
                       abilities=[2, 4441], set_id="RNA", rarity="Common", set_number=139,
                       mtga_id=69267)
SauroformHybrid = Card(name="sauroform_hybrid", pretty_name="Sauroform Hybrid", cost=['1', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Human Lizard Warrior",
                       abilities=[122079], set_id="RNA", rarity="Common", set_number=140,
                       mtga_id=69268)
SilhanaWayfinder = Card(name="silhana_wayfinder", pretty_name="Silhana Wayfinder", cost=['1', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Elf Scout",
                        abilities=[121877], set_id="RNA", rarity="Uncommon", set_number=141,
                        mtga_id=69269)
SteepleCreeper = Card(name="steeple_creeper", pretty_name="Steeple Creeper", cost=['2', 'G'],
                      color_identity=['U', 'G'], card_type="Creature", sub_types="Frog Snake",
                      abilities=[1840], set_id="RNA", rarity="Common", set_number=142,
                      mtga_id=69270)
StonyStrength = Card(name="stony_strength", pretty_name="Stony Strength", cost=['G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[122080], set_id="RNA", rarity="Common", set_number=143,
                     mtga_id=69271)
SylvanBrushstrider = Card(name="sylvan_brushstrider", pretty_name="Sylvan Brushstrider", cost=['2', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Beast",
                          abilities=[88132], set_id="RNA", rarity="Common", set_number=144,
                          mtga_id=69272)
TerritorialBoar = Card(name="territorial_boar", pretty_name="Territorial Boar", cost=['1', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Boar",
                       abilities=[122020], set_id="RNA", rarity="Common", set_number=145,
                       mtga_id=69273)
TitanicBrawl = Card(name="titanic_brawl", pretty_name="Titanic Brawl", cost=['1', 'G'],
                    color_identity=['G'], card_type="Instant", sub_types="",
                    abilities=[122083, 99356], set_id="RNA", rarity="Common", set_number=146,
                    mtga_id=69274)
TowerDefense = Card(name="tower_defense", pretty_name="Tower Defense", cost=['1', 'G'],
                    color_identity=['G'], card_type="Instant", sub_types="",
                    abilities=[19748], set_id="RNA", rarity="Uncommon", set_number=147,
                    mtga_id=69275)
TrollbredGuardian = Card(name="trollbred_guardian", pretty_name="Trollbred Guardian", cost=['4', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Troll Frog Warrior",
                         abilities=[122068, 2683], set_id="RNA", rarity="Uncommon", set_number=148,
                         mtga_id=69276)
WildernessReclamation = Card(name="wilderness_reclamation", pretty_name="Wilderness Reclamation", cost=['3', 'G'],
                             color_identity=['G'], card_type="Enchantment", sub_types="",
                             abilities=[121878], set_id="RNA", rarity="Uncommon", set_number=149,
                             mtga_id=69277)
WreckingBeast = Card(name="wrecking_beast", pretty_name="Wrecking Beast", cost=['5', 'G', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Beast",
                     abilities=[175, 14], set_id="RNA", rarity="Common", set_number=150,
                     mtga_id=69278)
Absorb = Card(name="absorb", pretty_name="Absorb", cost=['W', 'U', 'U'],
              color_identity=['W', 'U'], card_type="Instant", sub_types="",
              abilities=[2821], set_id="RNA", rarity="Rare", set_number=151,
              mtga_id=69279)
Aeromunculus = Card(name="aeromunculus", pretty_name="Aeromunculus", cost=['1', 'G', 'U'],
                    color_identity=['G', 'U'], card_type="Creature", sub_types="Homunculus Mutant",
                    abilities=[8, 122086], set_id="RNA", rarity="Common", set_number=152,
                    mtga_id=69280)
AppliedBiomancy = Card(name="applied_biomancy", pretty_name="Applied Biomancy", cost=['G', 'U'],
                       color_identity=['G', 'U'], card_type="Instant", sub_types="",
                       abilities=[122087], set_id="RNA", rarity="Common", set_number=153,
                       mtga_id=69281)
AzoriusKnightArbiter = Card(name="azorius_knightarbiter", pretty_name="Azorius Knight-Arbiter", cost=['3', 'W', 'U'],
                            color_identity=['W', 'U'], card_type="Creature", sub_types="Human Knight",
                            abilities=[15, 62969], set_id="RNA", rarity="Common", set_number=154,
                            mtga_id=69282)
AzoriusSkyguard = Card(name="azorius_skyguard", pretty_name="Azorius Skyguard", cost=['4', 'W', 'U'],
                       color_identity=['W', 'U'], card_type="Creature", sub_types="Human Knight",
                       abilities=[8, 6, 8808], set_id="RNA", rarity="Uncommon", set_number=155,
                       mtga_id=69283)
BasilicaBellHaunt = Card(name="basilica_bellhaunt", pretty_name="Basilica Bell-Haunt", cost=['W', 'W', 'B', 'B'],
                         color_identity=['W', 'B'], card_type="Creature", sub_types="Spirit",
                         abilities=[122088], set_id="RNA", rarity="Uncommon", set_number=156,
                         mtga_id=69284)
Bedevil = Card(name="bedevil", pretty_name="Bedevil", cost=['B', 'B', 'R'],
               color_identity=['B', 'R'], card_type="Instant", sub_types="",
               abilities=[122089], set_id="RNA", rarity="Rare", set_number=157,
               mtga_id=69285)
BiomancersFamiliar = Card(name="biomancers_familiar", pretty_name="Biomancer's Familiar", cost=['G', 'U'],
                          color_identity=['G', 'U'], card_type="Creature", sub_types="Mutant",
                          abilities=[122090, 122091], set_id="RNA", rarity="Rare", set_number=158,
                          mtga_id=69286)
BolracClanCrusher = Card(name="bolracclan_crusher", pretty_name="Bolrac-Clan Crusher", cost=['3', 'R', 'G'],
                         color_identity=['R', 'G'], card_type="Creature", sub_types="Ogre Warrior",
                         abilities=[122092], set_id="RNA", rarity="Uncommon", set_number=159,
                         mtga_id=69287)
CaptiveAudience = Card(name="captive_audience", pretty_name="Captive Audience", cost=['5', 'B', 'R'],
                       color_identity=['B', 'R'], card_type="Enchantment", sub_types="",
                       abilities=[122093, 121951], set_id="RNA", rarity="Mythic Rare", set_number=160,
                       mtga_id=69288)
Cindervines = Card(name="cindervines", pretty_name="Cindervines", cost=['R', 'G'],
                   color_identity=['R', 'G'], card_type="Enchantment", sub_types="",
                   abilities=[122016, 122043], set_id="RNA", rarity="Rare", set_number=161,
                   mtga_id=69289)
ClanGuildmage = Card(name="clan_guildmage", pretty_name="Clan Guildmage", cost=['R', 'G'],
                     color_identity=['R', 'G'], card_type="Creature", sub_types="Human Shaman",
                     abilities=[121881, 121880], set_id="RNA", rarity="Uncommon", set_number=162,
                     mtga_id=69290)
CombineGuildmage = Card(name="combine_guildmage", pretty_name="Combine Guildmage", cost=['G', 'U'],
                        color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Wizard",
                        abilities=[121883, 121884], set_id="RNA", rarity="Uncommon", set_number=163,
                        mtga_id=69291)
CultGuildmage = Card(name="cult_guildmage", pretty_name="Cult Guildmage", cost=['B', 'R'],
                     color_identity=['B', 'R'], card_type="Creature", sub_types="Human Shaman",
                     abilities=[121885, 121886], set_id="RNA", rarity="Uncommon", set_number=164,
                     mtga_id=69292)
DeputyofDetention = Card(name="deputy_of_detention", pretty_name="Deputy of Detention", cost=['1', 'W', 'U'],
                         color_identity=['W', 'U'], card_type="Creature", sub_types="Vedalken Wizard",
                         abilities=[121887], set_id="RNA", rarity="Rare", set_number=165,
                         mtga_id=69293)
DomriChaosBringer = Card(name="domri_chaos_bringer", pretty_name="Domri, Chaos Bringer", cost=['2', 'R', 'G'],
                         color_identity=['R', 'G'], card_type="Planeswalker", sub_types="Domri",
                         abilities=[122004, 121889, 121891], set_id="RNA", rarity="Mythic Rare", set_number=166,
                         mtga_id=69294)
DovinGrandArbiter = Card(name="dovin_grand_arbiter", pretty_name="Dovin, Grand Arbiter", cost=['1', 'W', 'U'],
                         color_identity=['W', 'U'], card_type="Planeswalker", sub_types="Dovin",
                         abilities=[121892, 121893, 122038], set_id="RNA", rarity="Mythic Rare", set_number=167,
                         mtga_id=69295)
DovinsAcuity = Card(name="dovins_acuity", pretty_name="Dovin's Acuity", cost=['1', 'W', 'U'],
                    color_identity=['W', 'U'], card_type="Enchantment", sub_types="",
                    abilities=[122042, 121896], set_id="RNA", rarity="Uncommon", set_number=168,
                    mtga_id=69296)
EmergencyPowers = Card(name="emergency_powers", pretty_name="Emergency Powers", cost=['5', 'W', 'U'],
                       color_identity=['W', 'U'], card_type="Instant", sub_types="",
                       abilities=[121897], set_id="RNA", rarity="Mythic Rare", set_number=169,
                       mtga_id=69297)
EtherealAbsolution = Card(name="ethereal_absolution", pretty_name="Ethereal Absolution", cost=['4', 'W', 'B'],
                          color_identity=['W', 'B'], card_type="Enchantment", sub_types="",
                          abilities=[1456, 121898, 122056], set_id="RNA", rarity="Rare", set_number=170,
                          mtga_id=69298)
FinalPayment = Card(name="final_payment", pretty_name="Final Payment", cost=['W', 'B'],
                    color_identity=['W', 'B'], card_type="Instant", sub_types="",
                    abilities=[121900, 26818], set_id="RNA", rarity="Common", set_number=171,
                    mtga_id=69299)
FirebladeArtist = Card(name="fireblade_artist", pretty_name="Fireblade Artist", cost=['B', 'R'],
                       color_identity=['B', 'R'], card_type="Creature", sub_types="Human Shaman",
                       abilities=[9, 121901], set_id="RNA", rarity="Uncommon", set_number=172,
                       mtga_id=69300)
FrenziedArynx = Card(name="frenzied_arynx", pretty_name="Frenzied Arynx", cost=['2', 'R', 'G'],
                     color_identity=['R', 'G'], card_type="Creature", sub_types="Cat Beast",
                     abilities=[175, 14, 121902], set_id="RNA", rarity="Common", set_number=173,
                     mtga_id=69301)
FrilledMystic = Card(name="frilled_mystic", pretty_name="Frilled Mystic", cost=['G', 'G', 'U', 'U'],
                     color_identity=['G', 'U'], card_type="Creature", sub_types="Elf Lizard Wizard",
                     abilities=[7, 121903], set_id="RNA", rarity="Uncommon", set_number=174,
                     mtga_id=69302)
GallopingLizrog = Card(name="galloping_lizrog", pretty_name="Galloping Lizrog", cost=['3', 'G', 'U'],
                       color_identity=['G', 'U'], card_type="Creature", sub_types="Frog Lizard",
                       abilities=[14, 122082], set_id="RNA", rarity="Uncommon", set_number=175,
                       mtga_id=69303)
GetthePoint = Card(name="get_the_point", pretty_name="Get the Point", cost=['3', 'B', 'R'],
                   color_identity=['B', 'R'], card_type="Instant", sub_types="",
                   abilities=[121905], set_id="RNA", rarity="Common", set_number=176,
                   mtga_id=69304)
GraspingThrull = Card(name="grasping_thrull", pretty_name="Grasping Thrull", cost=['3', 'W', 'B'],
                      color_identity=['W', 'B'], card_type="Creature", sub_types="Thrull",
                      abilities=[8, 121906], set_id="RNA", rarity="Common", set_number=177,
                      mtga_id=69305)
GrowthSpiral = Card(name="growth_spiral", pretty_name="Growth Spiral", cost=['G', 'U'],
                    color_identity=['G', 'U'], card_type="Instant", sub_types="",
                    abilities=[121907], set_id="RNA", rarity="Common", set_number=178,
                    mtga_id=69306)
GruulSpellbreaker = Card(name="gruul_spellbreaker", pretty_name="Gruul Spellbreaker", cost=['1', 'R', 'G'],
                         color_identity=['R', 'G'], card_type="Creature", sub_types="Ogre Warrior",
                         abilities=[175, 14, 121908], set_id="RNA", rarity="Rare", set_number=179,
                         mtga_id=69307)
GyreEngineer = Card(name="gyre_engineer", pretty_name="Gyre Engineer", cost=['1', 'G', 'U'],
                    color_identity=['G', 'U'], card_type="Creature", sub_types="Vedalken Wizard",
                    abilities=[6102], set_id="RNA", rarity="Uncommon", set_number=180,
                    mtga_id=69308)
Hackrobat = Card(name="hackrobat", pretty_name="Hackrobat", cost=['1', 'B', 'R'],
                 color_identity=['B', 'R'], card_type="Creature", sub_types="Human Rogue",
                 abilities=[121910, 94573, 97807], set_id="RNA", rarity="Uncommon", set_number=181,
                 mtga_id=69309)
HighAlert = Card(name="high_alert", pretty_name="High Alert", cost=['1', 'W', 'U'],
                 color_identity=['W', 'U'], card_type="Enchantment", sub_types="",
                 abilities=[61077, 121911, 121912], set_id="RNA", rarity="Uncommon", set_number=182,
                 mtga_id=69310)
HydroidKrasis = Card(name="hydroid_krasis", pretty_name="Hydroid Krasis", cost=['X', 'G', 'U'],
                     color_identity=['G', 'U'], card_type="Creature", sub_types="Jellyfish Hydra Beast",
                     abilities=[121913, 8, 14, 76885], set_id="RNA", rarity="Mythic Rare", set_number=183,
                     mtga_id=69311)
ImperiousOligarch = Card(name="imperious_oligarch", pretty_name="Imperious Oligarch", cost=['W', 'B'],
                         color_identity=['W', 'B'], card_type="Creature", sub_types="Human Cleric",
                         abilities=[15, 122106], set_id="RNA", rarity="Common", set_number=184,
                         mtga_id=69312)
JudiththeScourgeDiva = Card(name="judith_the_scourge_diva", pretty_name="Judith, the Scourge Diva", cost=['1', 'B', 'R'],
                            color_identity=['B', 'R'], card_type="Creature", sub_types="Human Shaman",
                            abilities=[118813, 121914], set_id="RNA", rarity="Rare", set_number=185,
                            mtga_id=69313)
KayaOrzhovUsurper = Card(name="kaya_orzhov_usurper", pretty_name="Kaya, Orzhov Usurper", cost=['1', 'W', 'B'],
                         color_identity=['W', 'B'], card_type="Planeswalker", sub_types="Kaya",
                         abilities=[121915, 121916, 121917], set_id="RNA", rarity="Mythic Rare", set_number=186,
                         mtga_id=69314)
KayasWrath = Card(name="kayas_wrath", pretty_name="Kaya's Wrath", cost=['W', 'W', 'B', 'B'],
                  color_identity=['W', 'B'], card_type="Sorcery", sub_types="",
                  abilities=[121960], set_id="RNA", rarity="Rare", set_number=187,
                  mtga_id=69315)
KnightoftheLastBreath = Card(name="knight_of_the_last_breath", pretty_name="Knight of the Last Breath", cost=['5', 'W', 'B'],
                             color_identity=['W', 'B'], card_type="Creature", sub_types="Giant Knight",
                             abilities=[121966, 121970], set_id="RNA", rarity="Uncommon", set_number=188,
                             mtga_id=69316)
LaviniaAzoriusRenegade = Card(name="lavinia_azorius_renegade", pretty_name="Lavinia, Azorius Renegade", cost=['W', 'U'],
                              color_identity=['W', 'U'], card_type="Creature", sub_types="Human Soldier",
                              abilities=[121919, 121920], set_id="RNA", rarity="Rare", set_number=189,
                              mtga_id=69317)
LawmagesBinding = Card(name="lawmages_binding", pretty_name="Lawmage's Binding", cost=['1', 'W', 'U'],
                       color_identity=['W', 'U'], card_type="Enchantment", sub_types="Aura",
                       abilities=[7, 1027, 1183], set_id="RNA", rarity="Common", set_number=190,
                       mtga_id=69318)
MacabreMockery = Card(name="macabre_mockery", pretty_name="Macabre Mockery", cost=['2', 'B', 'R'],
                      color_identity=['B', 'R'], card_type="Instant", sub_types="",
                      abilities=[121986], set_id="RNA", rarity="Uncommon", set_number=191,
                      mtga_id=69319)
Mortify = Card(name="mortify", pretty_name="Mortify", cost=['1', 'W', 'B'],
               color_identity=['W', 'B'], card_type="Instant", sub_types="",
               abilities=[3555], set_id="RNA", rarity="Uncommon", set_number=192,
               mtga_id=69320)
NikyaoftheOldWays = Card(name="nikya_of_the_old_ways", pretty_name="Nikya of the Old Ways", cost=['3', 'R', 'G'],
                         color_identity=['R', 'G'], card_type="Creature", sub_types="Centaur Druid",
                         abilities=[121529, 3776], set_id="RNA", rarity="Rare", set_number=193,
                         mtga_id=69321)
PitilessPontiff = Card(name="pitiless_pontiff", pretty_name="Pitiless Pontiff", cost=['W', 'B'],
                       color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire Cleric",
                       abilities=[121921], set_id="RNA", rarity="Uncommon", set_number=194,
                       mtga_id=69322)
PrimeSpeakerVannifar = Card(name="prime_speaker_vannifar", pretty_name="Prime Speaker Vannifar", cost=['2', 'G', 'U'],
                            color_identity=['G', 'U'], card_type="Creature", sub_types="Elf Ooze Wizard",
                            abilities=[121922], set_id="RNA", rarity="Mythic Rare", set_number=195,
                            mtga_id=69323)
RafterDemon = Card(name="rafter_demon", pretty_name="Rafter Demon", cost=['2', 'B', 'R'],
                   color_identity=['B', 'R'], card_type="Creature", sub_types="Demon",
                   abilities=[122003, 121924], set_id="RNA", rarity="Common", set_number=196,
                   mtga_id=69324)
RakdosFirewheeler = Card(name="rakdos_firewheeler", pretty_name="Rakdos Firewheeler", cost=['B', 'B', 'R', 'R'],
                         color_identity=['B', 'R'], card_type="Creature", sub_types="Human Rogue",
                         abilities=[121925], set_id="RNA", rarity="Uncommon", set_number=197,
                         mtga_id=69325)
RakdosRoustabout = Card(name="rakdos_roustabout", pretty_name="Rakdos Roustabout", cost=['1', 'B', 'R'],
                        color_identity=['B', 'R'], card_type="Creature", sub_types="Ogre Warrior",
                        abilities=[121926], set_id="RNA", rarity="Common", set_number=198,
                        mtga_id=69326)
RakdostheShowstopper = Card(name="rakdos_the_showstopper", pretty_name="Rakdos, the Showstopper", cost=['4', 'B', 'R'],
                            color_identity=['B', 'R'], card_type="Creature", sub_types="Demon",
                            abilities=[8, 14, 121927], set_id="RNA", rarity="Mythic Rare", set_number=199,
                            mtga_id=69327)
RavagerWurm = Card(name="ravager_wurm", pretty_name="Ravager Wurm", cost=['3', 'R', 'G', 'G'],
                   color_identity=['R', 'G'], card_type="Creature", sub_types="Wurm",
                   abilities=[175, 121929], set_id="RNA", rarity="Mythic Rare", set_number=200,
                   mtga_id=69328)
RhythmoftheWild = Card(name="rhythm_of_the_wild", pretty_name="Rhythm of the Wild", cost=['1', 'R', 'G'],
                       color_identity=['R', 'G'], card_type="Enchantment", sub_types="",
                       abilities=[87960, 121930], set_id="RNA", rarity="Uncommon", set_number=201,
                       mtga_id=69329)
RubblebeltRunner = Card(name="rubblebelt_runner", pretty_name="Rubblebelt Runner", cost=['1', 'R', 'G'],
                        color_identity=['R', 'G'], card_type="Creature", sub_types="Viashino Warrior",
                        abilities=[121931], set_id="RNA", rarity="Common", set_number=202,
                        mtga_id=69330)
SavageSmash = Card(name="savage_smash", pretty_name="Savage Smash", cost=['1', 'R', 'G'],
                   color_identity=['R', 'G'], card_type="Sorcery", sub_types="",
                   abilities=[121932], set_id="RNA", rarity="Common", set_number=203,
                   mtga_id=69331)
SenateGuildmage = Card(name="senate_guildmage", pretty_name="Senate Guildmage", cost=['W', 'U'],
                       color_identity=['W', 'U'], card_type="Creature", sub_types="Human Wizard",
                       abilities=[17949, 2767], set_id="RNA", rarity="Uncommon", set_number=204,
                       mtga_id=69332)
SeraphoftheScales = Card(name="seraph_of_the_scales", pretty_name="Seraph of the Scales", cost=['2', 'W', 'B'],
                         color_identity=['W', 'B'], card_type="Creature", sub_types="Angel",
                         abilities=[8, 90864, 94573, 122109], set_id="RNA", rarity="Mythic Rare", set_number=205,
                         mtga_id=69333)
Sharktocrab = Card(name="sharktocrab", pretty_name="Sharktocrab", cost=['2', 'G', 'U'],
                   color_identity=['G', 'U'], card_type="Creature", sub_types="Fish Octopus Crab",
                   abilities=[122086, 121933], set_id="RNA", rarity="Uncommon", set_number=206,
                   mtga_id=69334)
SimicAscendancy = Card(name="simic_ascendancy", pretty_name="Simic Ascendancy", cost=['G', 'U'],
                       color_identity=['G', 'U'], card_type="Enchantment", sub_types="",
                       abilities=[121934, 121935, 122023], set_id="RNA", rarity="Rare", set_number=207,
                       mtga_id=69335)
SphinxofNewPrahv = Card(name="sphinx_of_new_prahv", pretty_name="Sphinx of New Prahv", cost=['W', 'W', 'U', 'U'],
                        color_identity=['W', 'U'], card_type="Creature", sub_types="Sphinx",
                        abilities=[8, 15, 96148], set_id="RNA", rarity="Uncommon", set_number=208,
                        mtga_id=69336)
SphinxsInsight = Card(name="sphinxs_insight", pretty_name="Sphinx's Insight", cost=['2', 'W', 'U'],
                      color_identity=['W', 'U'], card_type="Instant", sub_types="",
                      abilities=[121937], set_id="RNA", rarity="Common", set_number=209,
                      mtga_id=69337)
SunderShaman = Card(name="sunder_shaman", pretty_name="Sunder Shaman", cost=['R', 'R', 'G', 'G'],
                    color_identity=['R', 'G'], card_type="Creature", sub_types="Giant Shaman",
                    abilities=[1026, 121938], set_id="RNA", rarity="Uncommon", set_number=210,
                    mtga_id=69338)
SyndicateGuildmage = Card(name="syndicate_guildmage", pretty_name="Syndicate Guildmage", cost=['W', 'B'],
                          color_identity=['W', 'B'], card_type="Creature", sub_types="Human Cleric",
                          abilities=[121939, 122030], set_id="RNA", rarity="Uncommon", set_number=211,
                          mtga_id=69339)
TeysaKarlov = Card(name="teysa_karlov", pretty_name="Teysa Karlov", cost=['2', 'W', 'B'],
                   color_identity=['W', 'B'], card_type="Creature", sub_types="Human Advisor",
                   abilities=[121941, 121942], set_id="RNA", rarity="Rare", set_number=212,
                   mtga_id=69340)
TheaterofHorrors = Card(name="theater_of_horrors", pretty_name="Theater of Horrors", cost=['1', 'B', 'R'],
                        color_identity=['B', 'R'], card_type="Enchantment", sub_types="",
                        abilities=[121943, 121944, 121945], set_id="RNA", rarity="Rare", set_number=213,
                        mtga_id=69341)
ZeganaUtopianSpeaker = Card(name="zegana_utopian_speaker", pretty_name="Zegana, Utopian Speaker", cost=['2', 'G', 'U'],
                            color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Wizard",
                            abilities=[122037, 121947, 2683], set_id="RNA", rarity="Rare", set_number=214,
                            mtga_id=69342)
ZhurTaaGoblin = Card(name="zhurtaa_goblin", pretty_name="Zhur-Taa Goblin", cost=['R', 'G'],
                     color_identity=['R', 'G'], card_type="Creature", sub_types="Goblin Berserker",
                     abilities=[175], set_id="RNA", rarity="Uncommon", set_number=215,
                     mtga_id=69343)
FootlightFiend = Card(name="footlight_fiend", pretty_name="Footlight Fiend", cost=['(B/R)'],
                      color_identity=['B', 'R'], card_type="Creature", sub_types="Devil",
                      abilities=[1285], set_id="RNA", rarity="Common", set_number=216,
                      mtga_id=69344)
RubbleSlinger = Card(name="rubble_slinger", pretty_name="Rubble Slinger", cost=['2', '(R/G)'],
                     color_identity=['R', 'G'], card_type="Creature", sub_types="Human Warrior",
                     abilities=[13], set_id="RNA", rarity="Common", set_number=217,
                     mtga_id=69345)
Scuttlegator = Card(name="scuttlegator", pretty_name="Scuttlegator", cost=['4', '(G/U)', '(G/U)'],
                    color_identity=['G', 'U'], card_type="Creature", sub_types="Crab Turtle Crocodile",
                    abilities=[2, 121948, 121949], set_id="RNA", rarity="Common", set_number=218,
                    mtga_id=69346)
SenateGriffin = Card(name="senate_griffin", pretty_name="Senate Griffin", cost=['2', '(W/U)', '(W/U)'],
                     color_identity=['W', 'U'], card_type="Creature", sub_types="Griffin",
                     abilities=[8, 91717], set_id="RNA", rarity="Common", set_number=219,
                     mtga_id=69347)
VizkopaVampire = Card(name="vizkopa_vampire", pretty_name="Vizkopa Vampire", cost=['2', '(W/B)'],
                      color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire",
                      abilities=[12], set_id="RNA", rarity="Common", set_number=220,
                      mtga_id=69348)
BedeckBedazzle = Card(name="bedeck__bedazzle", pretty_name="Bedeck // Bedazzle", cost=['(B/R)', '(B/R)', '4', 'B', 'R'],
                      color_identity=['B', 'R'], card_type="Instant Instant", sub_types="",
                      abilities=[62448, 121950], set_id="RNA", rarity="Rare", set_number=221,
                      mtga_id=69349)
Bedeck = Card(name="bedeck", pretty_name="Bedeck", cost=['(B/R)', '(B/R)'],
              color_identity=['B', 'R'], card_type="Instant", sub_types="",
              abilities=[62448], set_id="RNA", rarity="Rare", set_number=221,
              mtga_id=69350)
Bedazzle = Card(name="bedazzle", pretty_name="Bedazzle", cost=['4', 'B', 'R'],
                color_identity=['B', 'R'], card_type="Instant", sub_types="",
                abilities=[121950], set_id="RNA", rarity="Rare", set_number=221,
                mtga_id=69351)
CarnivalCarnage = Card(name="carnival__carnage", pretty_name="Carnival // Carnage", cost=['(B/R)', '2', 'B', 'R'],
                       color_identity=['B', 'R'], card_type="Instant Sorcery", sub_types="",
                       abilities=[122046, 121952], set_id="RNA", rarity="Uncommon", set_number=222,
                       mtga_id=69352)
Carnival = Card(name="carnival", pretty_name="Carnival", cost=['(B/R)'],
                color_identity=['B', 'R'], card_type="Instant", sub_types="",
                abilities=[122046], set_id="RNA", rarity="Uncommon", set_number=222,
                mtga_id=69353)
Carnage = Card(name="carnage", pretty_name="Carnage", cost=['2', 'B', 'R'],
               color_identity=['B', 'R'], card_type="Sorcery", sub_types="",
               abilities=[121952], set_id="RNA", rarity="Uncommon", set_number=222,
               mtga_id=69354)
CollisionColossus = Card(name="collision__colossus", pretty_name="Collision // Colossus", cost=['1', '(R/G)', 'R', 'G'],
                         color_identity=['R', 'G'], card_type="Instant Instant", sub_types="",
                         abilities=[121953, 2729], set_id="RNA", rarity="Uncommon", set_number=223,
                         mtga_id=69355)
Collision = Card(name="collision", pretty_name="Collision", cost=['1', '(R/G)'],
                 color_identity=['R', 'G'], card_type="Instant", sub_types="",
                 abilities=[121953], set_id="RNA", rarity="Uncommon", set_number=223,
                 mtga_id=69356)
Colossus = Card(name="colossus", pretty_name="Colossus", cost=['R', 'G'],
                color_identity=['R', 'G'], card_type="Instant", sub_types="",
                abilities=[2729], set_id="RNA", rarity="Uncommon", set_number=223,
                mtga_id=69357)
ConsecrateConsume = Card(name="consecrate__consume", pretty_name="Consecrate // Consume", cost=['1', '(W/B)', '2', 'W', 'B'],
                         color_identity=['W', 'B'], card_type="Instant Sorcery", sub_types="",
                         abilities=[3518, 25848, 121955], set_id="RNA", rarity="Uncommon", set_number=224,
                         mtga_id=69358)
Consecrate = Card(name="consecrate", pretty_name="Consecrate", cost=['1', '(W/B)'],
                  color_identity=['W', 'B'], card_type="Instant", sub_types="",
                  abilities=[3518, 25848], set_id="RNA", rarity="Uncommon", set_number=224,
                  mtga_id=69359)
Consume = Card(name="consume", pretty_name="Consume", cost=['2', 'W', 'B'],
               color_identity=['W', 'B'], card_type="Sorcery", sub_types="",
               abilities=[121955], set_id="RNA", rarity="Uncommon", set_number=224,
               mtga_id=69360)
DeposeDeploy = Card(name="depose__deploy", pretty_name="Depose // Deploy", cost=['1', '(W/U)', '2', 'W', 'U'],
                    color_identity=['W', 'U'], card_type="Instant Instant", sub_types="",
                    abilities=[21839, 25848, 121956], set_id="RNA", rarity="Uncommon", set_number=225,
                    mtga_id=69361)
Depose = Card(name="depose", pretty_name="Depose", cost=['1', '(W/U)'],
              color_identity=['W', 'U'], card_type="Instant", sub_types="",
              abilities=[21839, 25848], set_id="RNA", rarity="Uncommon", set_number=225,
              mtga_id=69362)
Deploy = Card(name="deploy", pretty_name="Deploy", cost=['2', 'W', 'U'],
              color_identity=['W', 'U'], card_type="Instant", sub_types="",
              abilities=[121956], set_id="RNA", rarity="Uncommon", set_number=225,
              mtga_id=69363)
IncubationIncongruity = Card(name="incubation__incongruity", pretty_name="Incubation // Incongruity", cost=['(G/U)', '1', 'G', 'U'],
                             color_identity=['U', 'G'], card_type="Sorcery Instant", sub_types="",
                             abilities=[121957, 121958], set_id="RNA", rarity="Uncommon", set_number=226,
                             mtga_id=69364)
Incubation = Card(name="incubation", pretty_name="Incubation", cost=['(G/U)'],
                  color_identity=['G', 'U'], card_type="Sorcery", sub_types="",
                  abilities=[121957], set_id="RNA", rarity="Uncommon", set_number=226,
                  mtga_id=69365)
Incongruity = Card(name="incongruity", pretty_name="Incongruity", cost=['1', 'G', 'U'],
                   color_identity=['G', 'U'], card_type="Instant", sub_types="",
                   abilities=[121958], set_id="RNA", rarity="Uncommon", set_number=226,
                   mtga_id=69366)
RepudiateReplicate = Card(name="repudiate__replicate", pretty_name="Repudiate // Replicate", cost=['(G/U)', '(G/U)', '1', 'G', 'U'],
                          color_identity=['U', 'G'], card_type="Instant Sorcery", sub_types="",
                          abilities=[15503, 18554], set_id="RNA", rarity="Rare", set_number=227,
                          mtga_id=69367)
Repudiate = Card(name="repudiate", pretty_name="Repudiate", cost=['(G/U)', '(G/U)'],
                 color_identity=['G', 'U'], card_type="Instant", sub_types="",
                 abilities=[15503], set_id="RNA", rarity="Rare", set_number=227,
                 mtga_id=69368)
Replicate = Card(name="replicate", pretty_name="Replicate", cost=['1', 'G', 'U'],
                 color_identity=['G', 'U'], card_type="Sorcery", sub_types="",
                 abilities=[18554], set_id="RNA", rarity="Rare", set_number=227,
                 mtga_id=69369)
RevivalRevenge = Card(name="revival__revenge", pretty_name="Revival // Revenge", cost=['(W/B)', '(W/B)', '4', 'W', 'B'],
                      color_identity=['W', 'B'], card_type="Sorcery Sorcery", sub_types="",
                      abilities=[13335, 121961], set_id="RNA", rarity="Rare", set_number=228,
                      mtga_id=69370)
Revival = Card(name="revival", pretty_name="Revival", cost=['(W/B)', '(W/B)'],
               color_identity=['W', 'B'], card_type="Sorcery", sub_types="",
               abilities=[13335], set_id="RNA", rarity="Rare", set_number=228,
               mtga_id=69371)
Revenge = Card(name="revenge", pretty_name="Revenge", cost=['4', 'W', 'B'],
               color_identity=['W', 'B'], card_type="Sorcery", sub_types="",
               abilities=[121961], set_id="RNA", rarity="Rare", set_number=228,
               mtga_id=69372)
ThrashThreat = Card(name="thrash__threat", pretty_name="Thrash // Threat", cost=['(R/G)', '(R/G)', '2', 'R', 'G'],
                    color_identity=['R', 'G'], card_type="Instant Sorcery", sub_types="",
                    abilities=[121962, 121963], set_id="RNA", rarity="Rare", set_number=229,
                    mtga_id=69373)
Thrash = Card(name="thrash", pretty_name="Thrash", cost=['(R/G)', '(R/G)'],
              color_identity=['R', 'G'], card_type="Instant", sub_types="",
              abilities=[121962], set_id="RNA", rarity="Rare", set_number=229,
              mtga_id=69374)
Threat = Card(name="threat", pretty_name="Threat", cost=['2', 'R', 'G'],
              color_identity=['R', 'G'], card_type="Sorcery", sub_types="",
              abilities=[121963], set_id="RNA", rarity="Rare", set_number=229,
              mtga_id=69375)
WarrantWarden = Card(name="warrant__warden", pretty_name="Warrant // Warden", cost=['(W/U)', '(W/U)', '3', 'W', 'U'],
                     color_identity=['W', 'U'], card_type="Instant Sorcery", sub_types="",
                     abilities=[97291, 121965], set_id="RNA", rarity="Rare", set_number=230,
                     mtga_id=69376)
Warrant = Card(name="warrant", pretty_name="Warrant", cost=['(W/U)', '(W/U)'],
               color_identity=['W', 'U'], card_type="Instant", sub_types="",
               abilities=[97291], set_id="RNA", rarity="Rare", set_number=230,
               mtga_id=69377)
Warden = Card(name="warden", pretty_name="Warden", cost=['3', 'W', 'U'],
              color_identity=['W', 'U'], card_type="Sorcery", sub_types="",
              abilities=[121965], set_id="RNA", rarity="Rare", set_number=230,
              mtga_id=69378)
AzoriusLocket = Card(name="azorius_locket", pretty_name="Azorius Locket", cost=['3'],
                     color_identity=['W', 'U'], card_type="Artifact", sub_types="",
                     abilities=[1209, 121967], set_id="RNA", rarity="Common", set_number=231,
                     mtga_id=69379)
GateColossus = Card(name="gate_colossus", pretty_name="Gate Colossus", cost=['8'],
                    color_identity=[], card_type="Artifact Creature", sub_types="Construct",
                    abilities=[121968, 87941, 121969], set_id="RNA", rarity="Uncommon", set_number=232,
                    mtga_id=69380)
GlassoftheGuildpact = Card(name="glass_of_the_guildpact", pretty_name="Glass of the Guildpact", cost=['2'],
                           color_identity=[], card_type="Artifact", sub_types="",
                           abilities=[122055], set_id="RNA", rarity="Rare", set_number=233,
                           mtga_id=69381)
GruulLocket = Card(name="gruul_locket", pretty_name="Gruul Locket", cost=['3'],
                   color_identity=['R', 'G'], card_type="Artifact", sub_types="",
                   abilities=[1131, 122057], set_id="RNA", rarity="Common", set_number=234,
                   mtga_id=69382)
Junktroller = Card(name="junktroller", pretty_name="Junktroller", cost=['4'],
                   color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                   abilities=[2, 96682], set_id="RNA", rarity="Uncommon", set_number=235,
                   mtga_id=69383)
OrzhovLocket = Card(name="orzhov_locket", pretty_name="Orzhov Locket", cost=['3'],
                    color_identity=['W', 'B'], card_type="Artifact", sub_types="",
                    abilities=[18472, 121971], set_id="RNA", rarity="Common", set_number=236,
                    mtga_id=69384)
RakdosLocket = Card(name="rakdos_locket", pretty_name="Rakdos Locket", cost=['3'],
                    color_identity=['B', 'R'], card_type="Artifact", sub_types="",
                    abilities=[1211, 121972], set_id="RNA", rarity="Common", set_number=237,
                    mtga_id=69385)
ScrabblingClaws = Card(name="scrabbling_claws", pretty_name="Scrabbling Claws", cost=['1'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[2978, 94928], set_id="RNA", rarity="Uncommon", set_number=238,
                       mtga_id=69386)
ScreamingShield = Card(name="screaming_shield", pretty_name="Screaming Shield", cost=['1'],
                       color_identity=[], card_type="Artifact", sub_types="Equipment",
                       abilities=[121974, 1156], set_id="RNA", rarity="Uncommon", set_number=239,
                       mtga_id=69387)
SimicLocket = Card(name="simic_locket", pretty_name="Simic Locket", cost=['3'],
                   color_identity=['U', 'G'], card_type="Artifact", sub_types="",
                   abilities=[18504, 121976], set_id="RNA", rarity="Common", set_number=240,
                   mtga_id=69388)
SphinxoftheGuildpact = Card(name="sphinx_of_the_guildpact", pretty_name="Sphinx of the Guildpact", cost=['7'],
                            color_identity=[], card_type="Artifact Creature", sub_types="Sphinx",
                            abilities=[121977, 8, 121978], set_id="RNA", rarity="Uncommon", set_number=241,
                            mtga_id=69389)
TomeoftheGuildpact = Card(name="tome_of_the_guildpact", pretty_name="Tome of the Guildpact", cost=['5'],
                          color_identity=[], card_type="Artifact", sub_types="",
                          abilities=[121979, 1055], set_id="RNA", rarity="Rare", set_number=242,
                          mtga_id=69390)
AzoriusGuildgate = Card(name="azorius_guildgate", pretty_name="Azorius Guildgate", cost=[],
                        color_identity=['W', 'U'], card_type="Land", sub_types="Gate",
                        abilities=[76735, 1209], set_id="RNA", rarity="Common", set_number=243,
                        mtga_id=69391)
AzoriusGuildgate2 = Card(name="azorius_guildgate", pretty_name="Azorius Guildgate", cost=[],
                         color_identity=['W', 'U'], card_type="Land", sub_types="Gate",
                         abilities=[76735, 1209], set_id="RNA", rarity="Common", set_number=244,
                         mtga_id=69392)
BloodCrypt = Card(name="blood_crypt", pretty_name="Blood Crypt", cost=[],
                  color_identity=['B', 'R'], card_type="Land", sub_types="Swamp Mountain",
                  abilities=[90846], set_id="RNA", rarity="Rare", set_number=245,
                  mtga_id=69393)
BreedingPool = Card(name="breeding_pool", pretty_name="Breeding Pool", cost=[],
                    color_identity=['G', 'U'], card_type="Land", sub_types="Forest Island",
                    abilities=[90846], set_id="RNA", rarity="Rare", set_number=246,
                    mtga_id=69394)
GatewayPlaza = Card(name="gateway_plaza", pretty_name="Gateway Plaza", cost=[],
                    color_identity=[], card_type="Land", sub_types="Gate",
                    abilities=[76735, 3625, 1055], set_id="RNA", rarity="Common", set_number=247,
                    mtga_id=69395)
GodlessShrine = Card(name="godless_shrine", pretty_name="Godless Shrine", cost=[],
                     color_identity=['W', 'B'], card_type="Land", sub_types="Plains Swamp",
                     abilities=[90846], set_id="RNA", rarity="Rare", set_number=248,
                     mtga_id=69396)
GruulGuildgate = Card(name="gruul_guildgate", pretty_name="Gruul Guildgate", cost=[],
                      color_identity=['R', 'G'], card_type="Land", sub_types="Gate",
                      abilities=[76735, 1131], set_id="RNA", rarity="Common", set_number=249,
                      mtga_id=69397)
GruulGuildgate2 = Card(name="gruul_guildgate", pretty_name="Gruul Guildgate", cost=[],
                       color_identity=['R', 'G'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 1131], set_id="RNA", rarity="Common", set_number=250,
                       mtga_id=69398)
HallowedFountain = Card(name="hallowed_fountain", pretty_name="Hallowed Fountain", cost=[],
                        color_identity=['W', 'U'], card_type="Land", sub_types="Plains Island",
                        abilities=[90846], set_id="RNA", rarity="Rare", set_number=251,
                        mtga_id=69399)
OrzhovGuildgate = Card(name="orzhov_guildgate", pretty_name="Orzhov Guildgate", cost=[],
                       color_identity=['W', 'B'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 18472], set_id="RNA", rarity="Common", set_number=252,
                       mtga_id=69400)
OrzhovGuildgate2 = Card(name="orzhov_guildgate", pretty_name="Orzhov Guildgate", cost=[],
                        color_identity=['W', 'B'], card_type="Land", sub_types="Gate",
                        abilities=[76735, 18472], set_id="RNA", rarity="Common", set_number=253,
                        mtga_id=69401)
PlazaofHarmony = Card(name="plaza_of_harmony", pretty_name="Plaza of Harmony", cost=[],
                      color_identity=[], card_type="Land", sub_types="",
                      abilities=[121982, 1152, 121983], set_id="RNA", rarity="Rare", set_number=254,
                      mtga_id=69402)
RakdosGuildgate = Card(name="rakdos_guildgate", pretty_name="Rakdos Guildgate", cost=[],
                       color_identity=['B', 'R'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 1211], set_id="RNA", rarity="Common", set_number=255,
                       mtga_id=69403)
RakdosGuildgate2 = Card(name="rakdos_guildgate", pretty_name="Rakdos Guildgate", cost=[],
                        color_identity=['B', 'R'], card_type="Land", sub_types="Gate",
                        abilities=[76735, 1211], set_id="RNA", rarity="Common", set_number=256,
                        mtga_id=69404)
SimicGuildgate = Card(name="simic_guildgate", pretty_name="Simic Guildgate", cost=[],
                      color_identity=['G', 'U'], card_type="Land", sub_types="Gate",
                      abilities=[76735, 18504], set_id="RNA", rarity="Common", set_number=257,
                      mtga_id=69405)
SimicGuildgate2 = Card(name="simic_guildgate", pretty_name="Simic Guildgate", cost=[],
                       color_identity=['G', 'U'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 18504], set_id="RNA", rarity="Common", set_number=258,
                       mtga_id=69406)
StompingGround = Card(name="stomping_ground", pretty_name="Stomping Ground", cost=[],
                      color_identity=['R', 'G'], card_type="Land", sub_types="Mountain Forest",
                      abilities=[90846], set_id="RNA", rarity="Rare", set_number=259,
                      mtga_id=69407)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="RNA", rarity="Basic", set_number=260,
              mtga_id=69408)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="RNA", rarity="Basic", set_number=261,
              mtga_id=69409)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="RNA", rarity="Basic", set_number=262,
             mtga_id=69410)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="RNA", rarity="Basic", set_number=263,
                mtga_id=69411)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="RNA", rarity="Basic", set_number=264,
              mtga_id=69412)
DovinArchitectofLaw = Card(name="dovin_architect_of_law", pretty_name="Dovin, Architect of Law", cost=['4', 'W', 'U'],
                           color_identity=['W', 'U'], card_type="Planeswalker", sub_types="Dovin",
                           abilities=[122076, 121985, 122078], set_id="RNA", rarity="Mythic Rare", set_number=265,
                           mtga_id=69413)
EliteArrester = Card(name="elite_arrester", pretty_name="Elite Arrester", cost=['W'],
                     color_identity=['U', 'W'], card_type="Creature", sub_types="Human Soldier",
                     abilities=[121987], set_id="RNA", rarity="Common", set_number=266,
                     mtga_id=69414)
DovinsDismissal = Card(name="dovins_dismissal", pretty_name="Dovin's Dismissal", cost=['2', 'W', 'U'],
                       color_identity=['W', 'U'], card_type="Instant", sub_types="",
                       abilities=[121988], set_id="RNA", rarity="Rare", set_number=267,
                       mtga_id=69415)
DovinsAutomaton = Card(name="dovins_automaton", pretty_name="Dovin's Automaton", cost=['4'],
                       color_identity=[], card_type="Artifact Creature", sub_types="Homunculus",
                       abilities=[121989], set_id="RNA", rarity="Uncommon", set_number=268,
                       mtga_id=69416)
DomriCitySmasher = Card(name="domri_city_smasher", pretty_name="Domri, City Smasher", cost=['4', 'R', 'G'],
                        color_identity=['R', 'G'], card_type="Planeswalker", sub_types="Domri",
                        abilities=[122081, 121991, 121992], set_id="RNA", rarity="Mythic Rare", set_number=269,
                        mtga_id=69417)
Ragefire = Card(name="ragefire", pretty_name="Ragefire", cost=['1', 'R'],
                color_identity=['R'], card_type="Sorcery", sub_types="",
                abilities=[88831], set_id="RNA", rarity="Common", set_number=270,
                mtga_id=69418)
ChargingWarBoar = Card(name="charging_war_boar", pretty_name="Charging War Boar", cost=['1', 'R', 'G'],
                       color_identity=['R', 'G'], card_type="Creature", sub_types="Boar",
                       abilities=[9, 121993], set_id="RNA", rarity="Uncommon", set_number=271,
                       mtga_id=69419)
DomrisNodorog = Card(name="domris_nodorog", pretty_name="Domri's Nodorog", cost=['3', 'R', 'G'],
                     color_identity=['R', 'G'], card_type="Creature", sub_types="Beast",
                     abilities=[14, 121994], set_id="RNA", rarity="Rare", set_number=272,
                     mtga_id=69420)
TheHauntofHightower = Card(name="the_haunt_of_hightower", pretty_name="The Haunt of Hightower", cost=['4', 'B', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Vampire",
                           abilities=[8, 12, 122084, 8592], set_id="RNA", rarity="Mythic Rare", set_number=273,
                           mtga_id=69421)
Human = Card(name="human", pretty_name="Human", cost=[],
             color_identity=[], card_type="Creature", sub_types="Human",
             abilities=[], set_id="RNA", rarity="Token", set_number=1,
             mtga_id=69422)
Illusion = Card(name="illusion", pretty_name="Illusion", cost=[],
                color_identity=[], card_type="Creature", sub_types="Illusion",
                abilities=[121888], set_id="RNA", rarity="Token", set_number=2,
                mtga_id=69423)
Zombie = Card(name="zombie", pretty_name="Zombie", cost=[],
              color_identity=[], card_type="Creature", sub_types="Zombie",
              abilities=[], set_id="RNA", rarity="Token", set_number=3,
              mtga_id=69424)
Goblin = Card(name="goblin", pretty_name="Goblin", cost=[],
              color_identity=[], card_type="Creature", sub_types="Goblin",
              abilities=[], set_id="RNA", rarity="Token", set_number=4,
              mtga_id=69425)
Centaur = Card(name="centaur", pretty_name="Centaur", cost=[],
               color_identity=[], card_type="Creature", sub_types="Centaur",
               abilities=[], set_id="RNA", rarity="Token", set_number=5,
               mtga_id=69426)
FrogLizard = Card(name="frog_lizard", pretty_name="Frog Lizard", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Frog Lizard",
                  abilities=[], set_id="RNA", rarity="Token", set_number=6,
                  mtga_id=69427)
Ooze = Card(name="ooze", pretty_name="Ooze", cost=[],
            color_identity=[], card_type="Creature", sub_types="Ooze",
            abilities=[], set_id="RNA", rarity="Token", set_number=7,
            mtga_id=69428)
Beast = Card(name="beast", pretty_name="Beast", cost=[],
             color_identity=[], card_type="Creature", sub_types="Beast",
             abilities=[14], set_id="RNA", rarity="Token", set_number=8,
             mtga_id=69429)
Sphinx = Card(name="sphinx", pretty_name="Sphinx", cost=[],
              color_identity=[], card_type="Creature", sub_types="Sphinx",
              abilities=[8, 15], set_id="RNA", rarity="Token", set_number=9,
              mtga_id=69430)
Spirit = Card(name="spirit", pretty_name="Spirit", cost=[],
              color_identity=[], card_type="Creature", sub_types="Spirit",
              abilities=[8], set_id="RNA", rarity="Token", set_number=10,
              mtga_id=69431)
Thopter = Card(name="thopter", pretty_name="Thopter", cost=[],
               color_identity=[], card_type="Artifact Creature", sub_types="Thopter",
               abilities=[8], set_id="RNA", rarity="Token", set_number=11,
               mtga_id=69432)
Treasure = Card(name="treasure", pretty_name="Treasure", cost=[],
                color_identity=[], card_type="Artifact", sub_types="Treasure",
                abilities=[119572], set_id="RNA", rarity="Token", set_number=12,
                mtga_id=69433)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
RavnicaAllegiance = Set("rna", cards=clsmembers)

set_ability_map = {1: 'Deathtouch',
 2: 'Defender',
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
 175: 'Riot',
 1026: "Sunder Shaman can't be blocked by more than one creature.",
 1027: 'Enchant creature',
 1055: '{oT}: Add one mana of any color.',
 1074: 'Target player reveals their hand. You choose a nonland card from it. '
       'That player discards that card.',
 1131: '{oT}: Add {oR} or {oG}.',
 1152: '{oT}: Add {oC}.',
 1156: 'Equip {o3}',
 1183: "Enchanted creature can't attack or block, and its activated abilities "
       "can't be activated.",
 1209: '{oT}: Add {oW} or {oU}.',
 1211: '{oT}: Add {oB} or {oR}.',
 1278: 'Gain control of target creature until end of turn. Untap that '
       'creature. It gains haste until end of turn.',
 1285: 'When Footlight Fiend dies, it deals 1 damage to any target.',
 1456: 'Creatures you control get +1/+1.',
 1746: 'Draw three cards.',
 1840: '{o3oU}: Steeple Creeper gains flying until end of turn.',
 1923: 'Return up to two target creature cards from your graveyard to your '
       'hand.',
 2683: 'Each creature you control with a +1/+1 counter on it has trample.',
 2729: 'Target creature gets +4/+2 and gains trample until end of turn.',
 2767: '{oU}, {oT}: Draw a card, then discard a card.',
 2821: 'Counter target spell. You gain 3 life.',
 2978: '{oT}: Target player exiles a card from their graveyard.',
 3518: 'Exile target card from a graveyard.',
 3555: 'Destroy target creature or enchantment.',
 3625: 'When Gateway Plaza enters the battlefield, sacrifice it unless you pay '
       '{o1}.',
 3776: 'Whenever you tap a land for mana, add one mana of any type that land '
       'produced.',
 4294: 'Target creature gains deathtouch until end of turn.',
 4441: '{oT}, Tap an untapped creature you control: Add one mana of any color.',
 6102: '{oT}: Add {oGoU}.',
 6374: 'Counter target spell unless its controller pays {o2}.',
 7344: 'Scorchmark deals 2 damage to target creature. If that creature would '
       'die this turn, exile it instead.',
 8592: "Whenever a card is put into an opponent's graveyard from anywhere, put "
       'a +1/+1 counter on The Haunt of Hightower.',
 8808: 'Creatures your opponents control get -1/-0.',
 12891: 'Other creatures you control with flying get +0/+1.',
 13335: 'Return target creature card with converted mana cost 3 or less from '
        'your graveyard to the battlefield.',
 15503: 'Counter target activated or triggered ability.',
 17633: 'Enchanted creature gets +1/+2 and has vigilance.',
 17949: '{oW}, {oT}: You gain 2 life.',
 18472: '{oT}: Add {oW} or {oB}.',
 18504: '{oT}: Add {oG} or {oU}.',
 18554: "Create a token that's a copy of target creature you control.",
 19615: 'Draw four cards, then discard two cards.',
 19694: 'Each creature you control with a +1/+1 counter on it has flying.',
 19748: 'Creatures you control get +0/+5 and gain reach until end of turn.',
 20495: 'At the beginning of your upkeep, scry 1.',
 21839: 'Tap target creature.',
 23611: 'Creatures you control get +2/+0 until end of turn.',
 25848: 'Draw a card.',
 25851: 'Target player shuffles their graveyard into their library.',
 26818: 'Destroy target creature.',
 27746: 'Prevent all combat damage that would be dealt this turn.',
 61077: 'Each creature you control assigns combat damage equal to its '
        'toughness rather than its power.',
 62243: 'Exile target creature with power 3 or less.',
 62448: 'Target creature gets +3/-3 until end of turn.',
 62969: "Azorius Knight-Arbiter can't be blocked.",
 63634: 'When Civic Stalwart enters the battlefield, creatures you control get '
        '+1/+1 until end of turn.',
 70361: 'Skewer the Critics deals 3 damage to any target.',
 76735: 'Simic Guildgate enters the battlefield tapped.',
 76824: 'Rubblebelt Recluse attacks each combat if able.',
 76869: 'Knight of Sorrows can block an additional creature each combat.',
 76885: 'Hydroid Krasis enters the battlefield with X +1/+1 counters on it.',
 87941: "Gate Colossus can't be blocked by creatures with power 2 or less.",
 87960: "Creature spells you control can't be countered.",
 88132: 'When Sylvan Brushstrider enters the battlefield, you gain 2 life.',
 88192: 'A deck can have any number of cards named Persistent Petitioners.',
 88831: 'Ragefire deals 3 damage to target creature.',
 88861: 'Whenever Orzhov Racketeers deals combat damage to a player, that '
        'player discards a card.',
 88910: '{o1oW}: Senate Courier gains vigilance until end of turn.',
 90846: 'As Stomping Ground enters the battlefield, you may pay 2 life. If you '
        "don't, it enters the battlefield tapped.",
 90864: '{oW}: Seraph of the Scales gains vigilance until end of turn.',
 91717: 'When Senate Griffin enters the battlefield, scry 1.',
 92932: 'Whenever Gateway Sneak deals combat damage to a player, draw a card.',
 93172: '{o2oB}: Thirsting Shade gets +1/+1 until end of turn.',
 94180: 'As an additional cost to cast this spell, sacrifice two creatures.',
 94573: '{oB}: Seraph of the Scales gains deathtouch until end of turn.',
 94928: '{o1}, Sacrifice Scrabbling Claws: Exile target card from a graveyard. '
        'Draw a card.',
 96148: 'Spells your opponents cast that target Sphinx of New Prahv cost {o2} '
        'more to cast.',
 96682: "{oT}: Put target card from a graveyard on the bottom of its owner's "
        'library.',
 97291: "Put target attacking or blocking creature on top of its owner's "
        'library.',
 97807: '{oR}: Hackrobat gets +2/-2 until end of turn.',
 99356: "Target creature you control fights target creature you don't control.",
 99786: 'When Watchful Giant enters the battlefield, create a 1/1 white Human '
        'creature token.',
 100685: "When Sage's Row Savant enters the battlefield, scry 2.",
 100740: 'When Wall of Lost Thoughts enters the battlefield, target player '
         'puts the top four cards of their library into their graveyard.',
 101881: 'Whenever Burning-Tree Vandal attacks, you may discard a card. If you '
         'do, draw a card.',
 103263: 'When Haazda Officer enters the battlefield, target creature you '
         'control gets +1/+1 until end of turn.',
 103821: 'Target creature gets +3/+3 and gains reach until end of turn.',
 118813: 'Other creatures you control get +1/+0.',
 119572: '{oT}, Sacrifice this artifact: Add one mana of any color.',
 121529: "You can't cast noncreature spells.",
 121856: 'Creatures you control get +1/+3 until end of turn. Untap them.',
 121857: 'Whenever one or more +1/+1 counters are put on Benthic Biomancer, '
         'draw a card, then discard a card.',
 121858: 'When Chillbringer enters the battlefield, tap target creature an '
         "opponent controls. It doesn't untap during its controller's next "
         'untap step.',
 121859: 'Whenever an opponent activates an ability of an artifact, creature, '
         "or land that isn't a mana ability, Immolation Shaman deals 1 damage "
         'to that player.',
 121860: '{o3oRoR}: Immolation Shaman gets +3/+3 and gains menace until end of '
         'turn.',
 121861: 'Spectacle {oR}',
 121862: 'Exile the top two cards of your library. Until the end of your next '
         'turn, you may play those cards.',
 121863: 'Whenever a nontoken creature enters the battlefield under your '
         'control, flip a coin until you lose a flip. For each flip you won, '
         "create a token that's a copy of that creature. Those tokens gain "
         'haste. Exile them at the beginning of the next end step.',
 121864: 'Spectacle {o2oBoR}',
 121865: 'When Rix Maadi Reveler enters the battlefield, discard a card, then '
         "draw a card. If Rix Maadi Reveler's spectacle cost was paid, instead "
         'discard your hand, then draw three cards.',
 121866: 'Destroy target land. Scry 2.',
 121867: '{o3oR}: Skarrgan Hellkite deals 2 damage divided as you choose among '
         'one or two targets. Activate this ability only if Skarrgan Hellkite '
         'has a +1/+1 counter on it.',
 121868: '{o2oR}, Sacrifice Smelt-Ward Ignus: Gain control of target creature '
         'with power 3 or less until end of turn. Untap that creature. It '
         'gains haste until end of turn. Activate this ability only any time '
         'you could cast a sorcery.',
 121869: '{oT}: Spear Spewer deals 1 damage to each player.',
 121870: 'Spectacle {o2oR}',
 121871: 'As long as you control two or more Gates, Gatebreaker Ram has '
         'vigilance and trample.',
 121873: '{o3oGoG}: Adapt 3.',
 121874: 'Counter target creature spell. Put a +1/+1 counter on up to one '
         'target creature you control.',
 121875: 'Destroy all artifacts and enchantments. For each permanent destroyed '
         'this way, its controller creates a 3/3 green Centaur creature token.',
 121876: 'Return up to two target permanent cards from your graveyard to your '
         'hand.',
 121877: 'When Silhana Wayfinder enters the battlefield, look at the top four '
         'cards of your library. You may reveal a creature or land card from '
         'among them and put it on top of your library. Put the rest on the '
         'bottom of your library in a random order.',
 121878: 'At the beginning of your end step, untap all lands you control.',
 121879: "<i>Addendum</i>  When Sentinel's Mark enters the battlefield, if you "
         'cast it during your main phase, enchanted creature gains lifelink '
         'until end of turn.',
 121880: '{o2oG}, {oT}: Target land you control becomes a 4/4 Elemental '
         "creature with haste until end of turn. It's still a land.",
 121881: "{o1oR}, {oT}: Target creature can't block this turn.",
 121882: 'Gain control of X target creatures and/or planeswalkers.',
 121883: '{o1oG}, {oT}: This turn, each creature you control enters the '
         'battlefield with an additional +1/+1 counter on it.',
 121884: '{o1oU}, {oT}: Move a +1/+1 counter from target creature you control '
         'onto another target creature you control.',
 121885: '{o3oB}, {oT}: Target player discards a card. Activate this ability '
         'only any time you could cast a sorcery.',
 121886: '{oR}, {oT}: Cult Guildmage deals 1 damage to target opponent or '
         'planeswalker.',
 121887: 'When Deputy of Detention enters the battlefield, exile target '
         'nonland permanent an opponent controls and all other nonland '
         'permanents that player controls with the same name as that permanent '
         'until Deputy of Detention leaves the battlefield.',
 121888: "Whenever this creature blocks a creature, that creature doesn't "
         "untap during its controller's next untap step.",
 121889: '-3: Look at the top four cards of your library. You may reveal up to '
         'two creature cards from among them and put them into your hand. Put '
         'the rest on the bottom of your library in a random order.',
 121891: '-8: You get an emblem with "At the beginning of each end step, '
         'create a 4/4 red and green Beast creature token with trample."',
 121892: '+1: Until end of turn, whenever a creature you control deals combat '
         'damage to a player, put a loyalty counter on Dovin, Grand Arbiter.',
 121893: '-1: Create a 1/1 colorless Thopter artifact creature token with '
         'flying. You gain 1 life.',
 121894: 'When Mesmerizing Benthid enters the battlefield, create two 0/2 blue '
         'Illusion creature tokens with "Whenever this creature blocks a '
         "creature, that creature doesn't untap during its controller's next "
         'untap step."',
 121895: 'Enchanted creature has defender and loses flying.',
 121896: 'Whenever you cast an instant spell during your main phase, you may '
         "return Dovin's Acuity to its owner's hand.",
 121897: 'Each player shuffles their hand and graveyard into their library, '
         'then draws seven cards. Exile Emergency Powers. \n'
         '<i>Addendum</i>  If you cast this spell during your main phase, you '
         'may put a permanent card with converted mana cost 7 or less from '
         'your hand onto the battlefield.',
 121898: 'Creatures your opponents control get -1/-1.',
 121899: 'Mesmerizing Benthid has hexproof as long as you control an Illusion.',
 121900: 'As an additional cost to cast this spell, pay 5 life or sacrifice a '
         'creature or enchantment.',
 121901: 'At the beginning of your upkeep, you may sacrifice a creature. When '
         'you do, Fireblade Artist deals 2 damage to target opponent or '
         'planeswalker.',
 121902: '{o4oRoG}: Frenzied Arynx gets +3/+0 until end of turn.',
 121903: 'When Frilled Mystic enters the battlefield, you may counter target '
         'spell.',
 121904: '{o1}, {oT}: Target player puts the top card of their library into '
         'their graveyard.',
 121905: 'Destroy target creature. Scry 1.',
 121906: 'When Grasping Thrull enters the battlefield, it deals 2 damage to '
         'each opponent and you gain 2 life.',
 121907: 'Draw a card. You may put a land card from your hand onto the '
         'battlefield.',
 121908: "As long as it's your turn, you and Gruul Spellbreaker have hexproof.",
 121909: 'Tap four untapped Advisors you control: Target player puts the top '
         'twelve cards of their library into their graveyard.',
 121910: 'Spectacle {oBoR}',
 121911: "Creatures you control can attack as though they didn't have "
         'defender.',
 121912: '{o2oWoU}: Untap target creature.',
 121913: 'When you cast this spell, you gain half X life and draw half X '
         'cards. Round down each time.',
 121914: 'Whenever a nontoken creature you control dies, Judith, the Scourge '
         'Diva deals 1 damage to any target.',
 121915: '+1: Exile up to two target cards from a single graveyard. You gain 2 '
         'life if at least one creature card was exiled this way.',
 121916: '-1: Exile target nonland permanent with converted mana cost 1 or '
         'less.',
 121917: '-5: Kaya, Orzhov Usurper deals damage to target player equal to the '
         'number of cards that player owns in exile and you gain that much '
         'life.',
 121918: 'Draw three cards. \n'
         '<i>Addendum</i>  If you cast this spell during your main phase, '
         'instead scry 3, then draw three cards.',
 121919: "Each opponent can't cast noncreature spells with converted mana cost "
         'greater than the number of lands that player controls.',
 121920: 'Whenever an opponent casts a spell, if no mana was spent to cast it, '
         'counter that spell.',
 121921: '{o1}, Sacrifice another creature: Pitiless Pontiff gains deathtouch '
         'and indestructible until end of turn.',
 121922: '{oT}, Sacrifice another creature: Search your library for a creature '
         'card with converted mana cost equal to 1 plus the sacrificed '
         "creature's converted mana cost, put that card onto the battlefield, "
         'then shuffle your library. Activate this ability only any time you '
         'could cast a sorcery.',
 121923: '{o7oU}: Adapt 4. This ability costs {o1} less to activate for each '
         'instant and sorcery card in your graveyard.',
 121924: 'When Rafter Demon enters the battlefield, if its spectacle cost was '
         'paid, each opponent discards a card.',
 121925: 'When Rakdos Firewheeler enters the battlefield, it deals 2 damage to '
         'target opponent and 2 damage to up to one target creature or '
         'planeswalker.',
 121926: 'Whenever Rakdos Roustabout becomes blocked, it deals 1 damage to the '
         "player or planeswalker it's attacking.",
 121927: 'When Rakdos, the Showstopper enters the battlefield, flip a coin for '
         "each creature that isn't a Demon, Devil, or Imp. Destroy each "
         'creature whose coin comes up tails.',
 121929: 'When Ravager Wurm enters the battlefield, choose up to one   Ravager '
         "Wurm fights target creature you don't control.  Destroy target land "
         "with an activated ability that isn't a mana ability.",
 121930: 'Nontoken creatures you control have riot.',
 121931: "Rubblebelt Runner can't be blocked by creature tokens.",
 121932: 'Target creature you control gets +2/+2 until end of turn. It fights '
         "target creature you don't control.",
 121933: 'Whenever one or more +1/+1 counters are put on Sharktocrab, tap '
         "target creature an opponent controls. That creature doesn't untap "
         "during its controller's next untap step.",
 121934: '{o1oGoU}: Put a +1/+1 counter on target creature you control.',
 121935: 'Whenever one or more +1/+1 counters are put on a creature you '
         'control, put that many growth counters on Simic Ascendancy.',
 121936: 'Whenever an opponent draws a card, that player may pay {o2}. If the '
         "player doesn't, you create a colorless Treasure artifact token with "
         '"{oT}, Sacrifice this artifact: Add one mana of any color."',
 121937: 'Draw two cards. \n'
         '<i>Addendum</i>  If you cast this spell during your main phase, you '
         'gain 2 life.',
 121938: 'Whenever Sunder Shaman deals combat damage to a player, destroy '
         'target artifact or enchantment that player controls.',
 121939: '{o1oW}, {oT}: Tap target creature with power 4 or greater.',
 121940: 'Look at the top four cards of your library. Put one of them into '
         'your hand and the rest on the bottom of your library in a random '
         'order.',
 121941: 'If a creature dying causes a triggered ability of a permanent you '
         'control to trigger, that ability triggers an additional time.',
 121942: 'Creature tokens you control have vigilance and lifelink.',
 121943: 'At the beginning of your upkeep, exile the top card of your library.',
 121944: 'During your turn, if an opponent lost life this turn, you may play '
         'cards exiled with Theater of Horrors.',
 121945: '{o3oR}: Theater of Horrors deals 1 damage to target opponent or '
         'planeswalker.',
 121946: '{o5oU}: Adapt 2.',
 121947: '{o4oGoU}: Adapt 4.',
 121948: '{o6}{o(G/U)o(G/U)}: Adapt 3.',
 121949: 'As long as Scuttlegator has a +1/+1 counter on it, it can attack as '
         "though it didn't have defender.",
 121950: 'Destroy target nonbasic land. Bedazzle deals 2 damage to target '
         'opponent or planeswalker.',
 121951: "At the beginning of your upkeep, choose one that hasn't been "
         'chosen   Your life total becomes 4.  Discard your hand.  Each '
         'opponent creates five 2/2 black Zombie creature tokens.',
 121952: 'Carnage deals 3 damage to target opponent. That player discards two '
         'cards.',
 121953: 'Collision deals 6 damage to target creature with flying.',
 121954: '{o2oU}: Adapt 2.',
 121955: 'Target player sacrifices a creature with the greatest power among '
         'creatures they control. You gain life equal to its power.',
 121956: 'Create two 1/1 colorless Thopter artifact creature tokens with '
         'flying, then you gain 1 life for each creature you control.',
 121957: 'Look at the top five cards of your library. You may reveal a '
         'creature card from among them and put it into your hand. Put the '
         'rest on the bottom of your library in a random order.',
 121958: "Exile target creature. That creature's controller creates a 3/3 "
         'green Frog Lizard creature token.',
 121959: 'Enchanted creature gets -4/-0.',
 121960: 'Destroy all creatures. You gain life equal to the number of '
         'creatures you controlled that were destroyed this way.',
 121961: 'Double your life total. Target opponent loses half their life, '
         'rounded up.',
 121962: 'Target creature you control deals damage equal to its power to '
         "target creature or planeswalker you don't control.",
 121963: 'Create a 4/4 red and green Beast creature token with trample.',
 121964: 'You may reveal this card from your opening hand. If you do, scry 3 '
         'at the beginning of your first upkeep.',
 121965: 'Create a 4/4 white and blue Sphinx creature token with flying and '
         'vigilance.',
 121966: '{o3}, Sacrifice another nontoken creature: Create a 1/1 white and '
         'black Spirit creature token with flying.',
 121967: '{o(W/U)o(W/U)o(W/U)o(W/U)}, {oT}, Sacrifice Azorius Locket: Draw two '
         'cards.',
 121968: 'This spell costs {o1} less to cast for each Gate you control.',
 121969: 'Whenever a Gate enters the battlefield under your control, you may '
         'put Gate Colossus from your graveyard on top of your library.',
 121970: 'Afterlife 3',
 121971: '{o(W/B)o(W/B)o(W/B)o(W/B)}, {oT}, Sacrifice Orzhov Locket: Draw two '
         'cards.',
 121972: '{o(B/R)o(B/R)o(B/R)o(B/R)}, {oT}, Sacrifice Rakdos Locket: Draw two '
         'cards.',
 121974: 'Equipped creature gets +0/+3 and has "{o2}, {oT}: Target player puts '
         'the top three cards of their library into their graveyard."',
 121975: "Choose one or both   Put target creature on top of its owner's "
         "library.  Return target creature to its owner's hand.",
 121976: '{o(G/U)o(G/U)o(G/U)o(G/U)}, {oT}, Sacrifice Simic Locket: Draw two '
         'cards.',
 121977: 'Sphinx of the Guildpact is all colors.',
 121978: 'Hexproof from monocolored',
 121979: 'Whenever you cast a multicolored spell, draw a card.',
 121980: 'Counter target spell. Its controller puts the top three cards of '
         'their library into their graveyard.',
 121981: 'Summary Judgment deals 3 damage to target tapped creature. \n'
         '<i>Addendum</i>  If you cast this spell during your main phase, it '
         'deals 5 damage to that creature instead.',
 121982: 'When Plaza of Harmony enters the battlefield, if you control two or '
         'more Gates, you gain 3 life.',
 121983: '{oT}: Add one mana of any type that a Gate you control could '
         'produce.',
 121984: "Whenever a creature an opponent controls becomes tapped, if it isn't "
         'being declared as an attacker, you may draw a card.',
 121985: "-1: Tap target creature. It doesn't untap during its controller's "
         'next untap step.',
 121986: "Put target creature card from an opponent's graveyard onto the "
         'battlefield under your control. It gets +2/+0 and gains haste until '
         'end of turn. Sacrifice it at the beginning of the next end step.',
 121987: '{o1oU}, {oT}: Tap target creature.',
 121988: "Put up to one target tapped creature on top of its owner's library. "
         'You may search your library and/or graveyard for a card named Dovin, '
         'Architect of Law, reveal it, and put it into your hand. If you '
         'search your library this way, shuffle it.',
 121989: "As long as you control a Dovin planeswalker, Dovin's Automaton gets "
         '+2/+2 and has vigilance.',
 121990: '{o4oU}: Tap target creature without flying.',
 121991: '-3: Domri, City Smasher deals 3 damage to any target.',
 121992: '-8: Put three +1/+1 counters on each creature you control. Those '
         'creatures gain trample until end of turn.',
 121993: 'As long as you control a Domri planeswalker, Charging War Boar gets '
         '+1/+1 and has trample.',
 121994: "When Domri's Nodorog enters the battlefield, you may search your "
         'library and/or graveyard for a card named Domri, City Smasher, '
         'reveal it, and put it into your hand. If you search your library '
         'this way, shuffle it.',
 121999: 'Other creatures you control with flying get +1/+0.',
 122000: 'Each player discards all the cards in their hand, then creates that '
         'many 2/2 black Zombie creature tokens.',
 122001: 'Whenever Tenth District Veteran attacks, untap another target '
         'creature you control.',
 122002: '{o1}, Sacrifice Resolute Watchdog: Target creature you control gains '
         'indestructible until end of turn.',
 122003: 'Spectacle {o3oBoR}',
 122004: '+1: Add {oR} or {oG}. If that mana is spent on a creature spell, it '
         'gains riot.',
 122005: 'Spectacle {o2oB}',
 122006: 'When Blade Juggler enters the battlefield, it deals 1 damage to you '
         'and you draw a card.',
 122007: 'During your turn, spells your opponents cast cost {o1} more to cast '
         'and abilities your opponents activate cost {o1} more to activate '
         "unless they're mana abilities.",
 122008: 'Whenever Bloodmist Infiltrator attacks, you may sacrifice another '
         "creature. If you do, Bloodmist Infiltrator can't be blocked this "
         'turn.',
 122009: 'When Carrion Imp enters the battlefield, you may exile target '
         'creature card from a graveyard. If you do, you gain 2 life.',
 122010: 'Target creature gets -3/-3 until end of turn. If you control a '
         'creature with power 4 or greater, you may return up to one target '
         'creature card from your graveyard to your hand.',
 122012: 'Destroy target creature. Consign to the Pit deals 2 damage to that '
         "creature's controller.",
 122013: 'All creatures get -2/-2 until end of turn. Exile all creature cards '
         'in all graveyards that were put there from the battlefield this '
         'turn. If a creature would die this turn, exile it instead.',
 122014: 'Spectacle {o1oB}',
 122015: 'Spectacle {oB}',
 122016: 'Whenever an opponent casts a noncreature spell, Cindervines deals 1 '
         'damage to that player.',
 122017: 'Whenever you pay life, put that many blood counters on Font of '
         'Agonies.',
 122018: 'Creatures you control gain indestructible until end of turn. \n'
         '<i>Addendum</i>  If you cast this spell during your main phase, put '
         'a +1/+1 counter on each of those creatures and they gain vigilance '
         'until end of turn.',
 122019: '{o1oB}, Remove four blood counters from Font of Agonies: Destroy '
         'target creature.',
 122020: 'Whenever a creature with power 4 or greater enters the battlefield '
         'under your control, Territorial Boar gets +1/+1 and gains vigilance '
         'until end of turn.',
 122021: '{o1oB}: Return Gutterbones from your graveyard to your hand. '
         'Activate this ability only during your turn and only if an opponent '
         'lost life this turn.',
 122022: 'At the beginning of your upkeep, Ill-Gotten Inheritance deals 1 '
         'damage to each opponent and you gain 1 life.',
 122023: 'At the beginning of your upkeep, if Simic Ascendancy has twenty or '
         'more growth counters on it, you win the game.',
 122024: '{o5oB}, Sacrifice Ill-Gotten Inheritance: It deals 4 damage to '
         'target opponent and you gain 4 life.',
 122025: 'Instant and sorcery spells you control have deathtouch.',
 122026: 'Whenever Plague Wight becomes blocked, each creature blocking it '
         'gets -1/-1 until end of turn.',
 122027: '{oT}, Sacrifice two other creatures: Any number of target players '
         'each lose 2 life and sacrifice a creature. You add {oBoB} and draw a '
         'card.',
 122028: "Return target creature to its owner's hand. \n"
         '<i>Addendum</i>  If you cast this spell during your main phase, draw '
         'a card.',
 122029: '{o3oR}: Rakdos Trumpeter gets +2/+0 until end of turn.',
 122030: '{o4oB}, {oT}: Syndicate Guildmage deals 2 damage to target opponent '
         'or planeswalker.',
 122031: 'Spectacle {o1oBoB}',
 122032: 'At the beginning of your upkeep, Spawn of Mayhem deals 1 damage to '
         'each player. Then if you have 10 or less life, put a +1/+1 counter '
         'on Spawn of Mayhem.',
 122033: 'When Spire Mangler enters the battlefield, target creature with '
         'flying you control gets +2/+0 until end of turn.',
 122034: '{o1oU}: Adapt 1.',
 122035: 'When Undercity Scavenger enters the battlefield, you may sacrifice '
         'another creature. If you do, put two +1/+1 counters on Undercity '
         'Scavenger, then scry 2.',
 122036: 'Target opponent sacrifices a creature. If you control a creature '
         'with power 4 or greater, you gain 4 life.',
 122037: 'When Zegana, Utopian Speaker enters the battlefield, if you control '
         'another creature with a +1/+1 counter on it, draw a card.',
 122038: '-7: Look at the top ten cards of your library. Put three of them '
         'into your hand and the rest on the bottom of your library in a '
         'random order.',
 122039: 'Whenever another creature you control dies, Vindictive Vampire deals '
         '1 damage to each opponent and you gain 1 life.',
 122040: 'At the beginning of your upkeep, reveal cards from the top of your '
         'library until you reveal a creature card. Until your next turn, '
         "Amplifire's base power becomes twice that card's power and its base "
         "toughness becomes twice that card's toughness. Put the revealed "
         'cards on the bottom of your library in a random order.',
 122042: "When Dovin's Acuity enters the battlefield, you gain 2 life and draw "
         'a card.',
 122043: '{o1}, Sacrifice Cindervines: Destroy target artifact or enchantment. '
         "Cindervines deals 2 damage to that permanent's controller.",
 122044: 'Whenever a creature you control with power 1 or less attacks, '
         'Cavalcade of Calamity deals 1 damage to the player or planeswalker '
         'that creature is attacking.',
 122045: 'Whenever Clamor Shaman attacks, target creature an opponent controls '
         "can't block this turn.",
 122046: 'Carnival deals 1 damage to target creature or planeswalker and 1 '
         "damage to that permanent's controller.",
 122047: 'When Dagger Caster enters the battlefield, it deals 1 damage to each '
         'opponent and 1 damage to each creature your opponents control.',
 122048: 'Choose one   Destroy target artifact.  Destroy target creature with '
         'defender.',
 122049: 'Electrodominance deals X damage to any target. You may cast a card '
         'with converted mana cost X or less from your hand without paying its '
         'mana cost.',
 122050: 'Flames of the Raze-Boar deals 4 damage to target creature an '
         'opponent controls. Then Flames of the Raze-Boar deals 2 damage to '
         'each other creature that player controls if you control a creature '
         'with power 4 or greater.',
 122051: 'Gates Ablaze deals X damage to each creature, where X is the number '
         'of Gates you control.',
 122052: 'Create a number of 1/1 red Goblin creature tokens equal to two plus '
         'the number of cards named Goblin Gathering in your graveyard.',
 122053: '{o3oG}: Gravel-Hide Goblin gets +2/+2 until end of turn.',
 122054: 'When Rumbling Ruin enters the battlefield, count the number of +1/+1 '
         'counters on creatures you control. Creatures your opponents control '
         "with power less than or equal to that number can't block this turn.",
 122055: 'Multicolored creatures you control get +1/+1.',
 122056: "{o2oWoB}: Exile target card from an opponent's graveyard. If it was "
         'a creature card, you create a 1/1 white and black Spirit creature '
         'token with flying.',
 122057: '{o(R/G)o(R/G)o(R/G)o(R/G)}, {oT}, Sacrifice Gruul Locket: Draw two '
         'cards.',
 122058: 'Target creature gets +1/+0 and gains first strike until end of turn. '
         'Scry 1.',
 122059: "{oR}: Tin Street Dodger can't be blocked this turn except by "
         'creatures with defender.',
 122060: 'When Biogenic Ooze enters the battlefield, create a 2/2 green Ooze '
         'creature token.',
 122061: 'At the beginning of your end step, put a +1/+1 counter on each Ooze '
         'you control.',
 122062: '{o1oGoGoG}: Create a 2/2 green Ooze creature token.',
 122063: 'When Lumbering Battlement enters the battlefield, exile any number '
         'of other nontoken creatures you control until it leaves the '
         'battlefield.',
 122064: 'Distribute three +1/+1 counters among one, two, or three target '
         'creatures, then double the number of +1/+1 counters on each of those '
         'creatures.',
 122065: 'When End-Raze Forerunners enters the battlefield, other creatures '
         'you control get +2/+2 and gain vigilance and trample until end of '
         'turn.',
 122066: 'Gatebreaker Ram gets +1/+1 for each Gate you control.',
 122067: '{o5oU}: Exchange control of Eyes Everywhere and target nonland '
         'permanent. Activate this ability only any time you could cast a '
         'sorcery.',
 122068: '{o2oG}: Adapt 2.',
 122069: 'Whenever one or more +1/+1 counters are put on Growth-Chamber '
         'Guardian, you may search your library for a card named '
         'Growth-Chamber Guardian, reveal it, put it into your hand, then '
         'shuffle your library.',
 122070: 'Whenever Gruul Beastmaster attacks, another target creature you '
         "control gets +X/+0 until end of turn, where X is Gruul Beastmaster's "
         'power.',
 122071: 'Whenever a nontoken creature enters the battlefield under your '
         "control, if it doesn't have the same name as another creature you "
         'control or a creature card in your graveyard, draw a card.',
 122072: 'When Faerie Duelist enters the battlefield, target creature an '
         'opponent controls gets -2/-0 until end of turn.',
 122073: '{oT}: Add one mana of any type that a land you control could '
         'produce. If Incubation Druid has a +1/+1 counter on it, add three '
         'mana of that type instead.',
 122074: 'Search your library for a basic land card or Gate card, reveal it, '
         'put it into your hand, then shuffle your library.',
 122075: 'Whenever a Gate enters the battlefield under your control, Gateway '
         "Sneak can't be blocked this turn.",
 122076: '+1: You gain 2 life and draw a card.',
 122077: "Destroy target creature with flying. Sagittars' Volley deals 1 "
         'damage to each creature with flying your opponents control.',
 122078: '-9: Tap all permanents target opponent controls. That player skips '
         'their next untap step.',
 122079: '{o4oGoG}: Adapt 4.',
 122080: 'Put a +1/+1 counter on target creature you control. Untap that '
         'creature.',
 122081: '+2: Creatures you control get +1/+1 and gain haste until end of '
         'turn.',
 122082: 'When Galloping Lizrog enters the battlefield, you may remove any '
         'number of +1/+1 counters from among creatures you control. If you '
         'do, put twice that many +1/+1 counters on Galloping Lizrog.',
 122083: 'This spell costs {o1} less to cast if it targets a creature you '
         'control with a +1/+1 counter on it.',
 122084: 'Whenever The Haunt of Hightower attacks, defending player discards a '
         'card.',
 122085: 'When Archway Angel enters the battlefield, you gain 2 life for each '
         'Gate you control.',
 122086: '{o2oGoU}: Adapt 1.',
 122087: 'Choose one or both   Target creature gets +1/+1 until end of turn.  '
         "Return target creature to its owner's hand.",
 122088: 'When Basilica Bell-Haunt enters the battlefield, each opponent '
         'discards a card and you gain 3 life.',
 122089: 'Destroy target artifact, creature, or planeswalker.',
 122090: 'Activated abilities of creatures you control cost {o2} less to '
         "activate. This effect can't reduce the amount of mana an ability "
         'costs to activate to less than one mana.',
 122091: '{oT}: The next time target creature adapts this turn, it adapts as '
         'though it had no +1/+1 counters on it.',
 122092: '{oT}, Remove a +1/+1 counter from a creature you control: '
         'Bolrac-Clan Crusher deals 2 damage to any target.',
 122093: 'Captive Audience enters the battlefield under the control of an '
         'opponent of your choice.',
 122094: 'When Angel of Grace enters the battlefield, until end of turn, '
         'damage that would reduce your life total to less than 1 reduces it '
         'to 1 instead.',
 122095: '{o4oWoW}, Exile Angel of Grace from your graveyard: Your life total '
         'becomes 10.',
 122096: 'Whenever a creature you control attacks alone, it gets +X/+X until '
         'end of turn, where X is the number of creatures you control.',
 122098: 'Target creature gets +2/+2 until end of turn. \n'
         '<i>Addendum</i>  If you cast this spell during your main phase, that '
         'creature gains flying until end of turn.',
 122099: 'Exile target creature with power 4 or greater.',
 122100: 'Destroy target artifact or enchantment. Scry 1.',
 122101: 'When Forbidding Spirit enters the battlefield, until your next turn, '
         "creatures can't attack you or a planeswalker you control unless "
         'their controller pays {o2} for each of those creatures.',
 122103: 'Whenever you cast a multicolored spell, create a 1/1 white Human '
         'creature token.',
 122104: 'Whenever another creature enters the battlefield under your control, '
         'you gain 1 life.',
 122105: 'Exile target creature you control, then return that card to the '
         "battlefield under its owner's control. It gains first strike until "
         'end of turn.',
 122106: 'Afterlife 1',
 122108: 'Lumbering Battlement gets +2/+2 for each card exiled with it.',
 122109: 'Afterlife 2',
 122115: 'Target creature gets -4/-0 until end of turn. Draw a card. \n'
         '<i>Addendum</i>  If you cast this spell during your main phase, tap '
         "that creature and it doesn't untap during its controller's next "
         'untap step.'}
