
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


KarntheGreatCreator = Card(name="karn_the_great_creator", pretty_name="Karn, the Great Creator", cost=['4'],
                           color_identity=[], card_type="Planeswalker", sub_types="Karn",
                           abilities=[133310, 133311, 133312], set_id="WAR", rarity="Rare", collectible=True, set_number=1,
                           mtga_id=69452)
UgintheIneffable = Card(name="ugin_the_ineffable", pretty_name="Ugin, the Ineffable", cost=['6'],
                        color_identity=[], card_type="Planeswalker", sub_types="Ugin",
                        abilities=[133298, 133356, 133314], set_id="WAR", rarity="Rare", collectible=True, set_number=2,
                        mtga_id=69453)
UginsConjurant = Card(name="ugins_conjurant", pretty_name="Ugin's Conjurant", cost=['X'],
                      color_identity=[], card_type="Creature", sub_types="Spirit Monk",
                      abilities=[76885, 133315], set_id="WAR", rarity="Uncommon", collectible=True, set_number=3,
                      mtga_id=69454)
AjanisPridemate = Card(name="ajanis_pridemate", pretty_name="Ajani's Pridemate", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Cat Soldier",
                       abilities=[92970], set_id="WAR", rarity="Uncommon", collectible=True, set_number=4,
                       mtga_id=69455)
BattlefieldPromotion = Card(name="battlefield_promotion", pretty_name="Battlefield Promotion", cost=['1', 'W'],
                            color_identity=['W'], card_type="Instant", sub_types="",
                            abilities=[133306], set_id="WAR", rarity="Common", collectible=True, set_number=5,
                            mtga_id=69456)
BondofDiscipline = Card(name="bond_of_discipline", pretty_name="Bond of Discipline", cost=['4', 'W'],
                        color_identity=['W'], card_type="Sorcery", sub_types="",
                        abilities=[133317], set_id="WAR", rarity="Uncommon", collectible=True, set_number=6,
                        mtga_id=69457)
BulwarkGiant = Card(name="bulwark_giant", pretty_name="Bulwark Giant", cost=['5', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Giant Soldier",
                    abilities=[2103], set_id="WAR", rarity="Common", collectible=True, set_number=7,
                    mtga_id=69458)
CharmedStray = Card(name="charmed_stray", pretty_name="Charmed Stray", cost=['W'],
                    color_identity=['W'], card_type="Creature", sub_types="Cat",
                    abilities=[12, 133318], set_id="WAR", rarity="Common", collectible=True, set_number=8,
                    mtga_id=69459)
DefiantStrike = Card(name="defiant_strike", pretty_name="Defiant Strike", cost=['W'],
                     color_identity=['W'], card_type="Instant", sub_types="",
                     abilities=[21849, 25848], set_id="WAR", rarity="Common", collectible=True, set_number=9,
                     mtga_id=69460)
DivineArrow = Card(name="divine_arrow", pretty_name="Divine Arrow", cost=['1', 'W'],
                   color_identity=['W'], card_type="Instant", sub_types="",
                   abilities=[100370], set_id="WAR", rarity="Common", collectible=True, set_number=10,
                   mtga_id=69461)
EnforcerGriffin = Card(name="enforcer_griffin", pretty_name="Enforcer Griffin", cost=['4', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Griffin",
                       abilities=[8], set_id="WAR", rarity="Common", collectible=True, set_number=11,
                       mtga_id=69462)
FinaleofGlory = Card(name="finale_of_glory", pretty_name="Finale of Glory", cost=['X', 'W', 'W'],
                     color_identity=['W'], card_type="Sorcery", sub_types="",
                     abilities=[133320], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=12,
                     mtga_id=69463)
GideonBlackblade = Card(name="gideon_blackblade", pretty_name="Gideon Blackblade", cost=['1', 'W', 'W'],
                        color_identity=['W'], card_type="Planeswalker", sub_types="Gideon",
                        abilities=[133321, 133046, 133344, 133050], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=13,
                        mtga_id=69464)
GideonsSacrifice = Card(name="gideons_sacrifice", pretty_name="Gideon's Sacrifice", cost=['W'],
                        color_identity=['W'], card_type="Instant", sub_types="",
                        abilities=[133336], set_id="WAR", rarity="Common", collectible=True, set_number=14,
                        mtga_id=69465)
GideonsTriumph = Card(name="gideons_triumph", pretty_name="Gideon's Triumph", cost=['1', 'W'],
                      color_identity=['W'], card_type="Instant", sub_types="",
                      abilities=[133066], set_id="WAR", rarity="Uncommon", collectible=True, set_number=15,
                      mtga_id=69466)
GodEternalOketra = Card(name="godeternal_oketra", pretty_name="God-Eternal Oketra", cost=['3', 'W', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Zombie God",
                        abilities=[3, 133076, 133098], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=16,
                        mtga_id=69467)
GratefulApparition = Card(name="grateful_apparition", pretty_name="Grateful Apparition", cost=['1', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Spirit",
                          abilities=[8, 133118], set_id="WAR", rarity="Uncommon", collectible=True, set_number=17,
                          mtga_id=69468)
IgnitetheBeacon = Card(name="ignite_the_beacon", pretty_name="Ignite the Beacon", cost=['4', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[133143], set_id="WAR", rarity="Rare", collectible=True, set_number=18,
                       mtga_id=69469)
IroncladKrovod = Card(name="ironclad_krovod", pretty_name="Ironclad Krovod", cost=['3', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Beast",
                      abilities=[], set_id="WAR", rarity="Common", collectible=True, set_number=19,
                      mtga_id=69470)
LawRuneEnforcer = Card(name="lawrune_enforcer", pretty_name="Law-Rune Enforcer", cost=['W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                       abilities=[133167], set_id="WAR", rarity="Common", collectible=True, set_number=20,
                       mtga_id=69471)
LoxodonSergeant = Card(name="loxodon_sergeant", pretty_name="Loxodon Sergeant", cost=['3', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Elephant Soldier",
                       abilities=[15, 133190], set_id="WAR", rarity="Common", collectible=True, set_number=21,
                       mtga_id=69472)
MakeshiftBattalion = Card(name="makeshift_battalion", pretty_name="Makeshift Battalion", cost=['2', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                          abilities=[133203], set_id="WAR", rarity="Common", collectible=True, set_number=22,
                          mtga_id=69473)
MartyrfortheCause = Card(name="martyr_for_the_cause", pretty_name="Martyr for the Cause", cost=['1', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                         abilities=[93170], set_id="WAR", rarity="Common", collectible=True, set_number=23,
                         mtga_id=69474)
ParhelionII = Card(name="parhelion_ii", pretty_name="Parhelion II", cost=['6', 'W', 'W'],
                   color_identity=['W'], card_type="Artifact", sub_types="Vehicle",
                   abilities=[8, 6, 15, 133216, 76611], set_id="WAR", rarity="Rare", collectible=True, set_number=24,
                   mtga_id=69475)
PouncingLynx = Card(name="pouncing_lynx", pretty_name="Pouncing Lynx", cost=['1', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Cat",
                    abilities=[121419], set_id="WAR", rarity="Common", collectible=True, set_number=25,
                    mtga_id=69476)
PrisonRealm = Card(name="prison_realm", pretty_name="Prison Realm", cost=['2', 'W'],
                   color_identity=['W'], card_type="Enchantment", sub_types="",
                   abilities=[133233, 91717], set_id="WAR", rarity="Uncommon", collectible=True, set_number=26,
                   mtga_id=69477)
RallyofWings = Card(name="rally_of_wings", pretty_name="Rally of Wings", cost=['1', 'W'],
                    color_identity=['W'], card_type="Instant", sub_types="",
                    abilities=[133047], set_id="WAR", rarity="Uncommon", collectible=True, set_number=27,
                    mtga_id=69478)
RavnicaatWar = Card(name="ravnica_at_war", pretty_name="Ravnica at War", cost=['3', 'W'],
                    color_identity=['W'], card_type="Sorcery", sub_types="",
                    abilities=[133058], set_id="WAR", rarity="Rare", collectible=True, set_number=28,
                    mtga_id=69479)
RisingPopulace = Card(name="rising_populace", pretty_name="Rising Populace", cost=['2', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Human",
                      abilities=[133049], set_id="WAR", rarity="Common", collectible=True, set_number=29,
                      mtga_id=69480)
SingleCombat = Card(name="single_combat", pretty_name="Single Combat", cost=['3', 'W', 'W'],
                    color_identity=['W'], card_type="Sorcery", sub_types="",
                    abilities=[133259], set_id="WAR", rarity="Rare", collectible=True, set_number=30,
                    mtga_id=69481)
SunbladeAngel = Card(name="sunblade_angel", pretty_name="Sunblade Angel", cost=['5', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Angel",
                     abilities=[8, 6, 15, 12], set_id="WAR", rarity="Uncommon", collectible=True, set_number=31,
                     mtga_id=69482)
TeyotheShieldmage = Card(name="teyo_the_shieldmage", pretty_name="Teyo, the Shieldmage", cost=['2', 'W'],
                         color_identity=['W'], card_type="Planeswalker", sub_types="Teyo",
                         abilities=[2655, 133063], set_id="WAR", rarity="Uncommon", collectible=True, set_number=32,
                         mtga_id=69483)
TeyosLightshield = Card(name="teyos_lightshield", pretty_name="Teyo's Lightshield", cost=['2', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Illusion",
                        abilities=[101825], set_id="WAR", rarity="Common", collectible=True, set_number=33,
                        mtga_id=69484)
TomikDistinguishedAdvokist = Card(name="tomik_distinguished_advokist", pretty_name="Tomik, Distinguished Advokist", cost=['W', 'W'],
                                  color_identity=['W'], card_type="Creature", sub_types="Human Advisor",
                                  abilities=[8, 133351, 133279], set_id="WAR", rarity="Rare", collectible=True, set_number=34,
                                  mtga_id=69485)
ToppletheStatue = Card(name="topple_the_statue", pretty_name="Topple the Statue", cost=['2', 'W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[133284, 25848], set_id="WAR", rarity="Common", collectible=True, set_number=35,
                       mtga_id=69486)
TrustedPegasus = Card(name="trusted_pegasus", pretty_name="Trusted Pegasus", cost=['2', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Pegasus",
                      abilities=[8, 121386], set_id="WAR", rarity="Common", collectible=True, set_number=36,
                      mtga_id=69487)
TheWanderer = Card(name="the_wanderer", pretty_name="The Wanderer", cost=['3', 'W'],
                   color_identity=['W'], card_type="Planeswalker", sub_types="",
                   abilities=[133293, 133070], set_id="WAR", rarity="Uncommon", collectible=True, set_number=37,
                   mtga_id=69488)
WanderersStrike = Card(name="wanderers_strike", pretty_name="Wanderer's Strike", cost=['4', 'W'],
                       color_identity=['W'], card_type="Sorcery", sub_types="",
                       abilities=[133075], set_id="WAR", rarity="Common", collectible=True, set_number=38,
                       mtga_id=69489)
WarScreecher = Card(name="war_screecher", pretty_name="War Screecher", cost=['1', 'W'],
                    color_identity=['W'], card_type="Creature", sub_types="Bird",
                    abilities=[8, 133079], set_id="WAR", rarity="Common", collectible=True, set_number=39,
                    mtga_id=69490)
AshioksSkulker = Card(name="ashioks_skulker", pretty_name="Ashiok's Skulker", cost=['4', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Nightmare",
                      abilities=[133085], set_id="WAR", rarity="Common", collectible=True, set_number=40,
                      mtga_id=69491)
AugurofBolas = Card(name="augur_of_bolas", pretty_name="Augur of Bolas", cost=['1', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                    abilities=[99877], set_id="WAR", rarity="Uncommon", collectible=True, set_number=41,
                    mtga_id=69492)
AvenEternal = Card(name="aven_eternal", pretty_name="Aven Eternal", cost=['2', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Zombie Bird Warrior",
                   abilities=[8, 133092], set_id="WAR", rarity="Common", collectible=True, set_number=42,
                   mtga_id=69493)
BondofInsight = Card(name="bond_of_insight", pretty_name="Bond of Insight", cost=['3', 'U'],
                     color_identity=['U'], card_type="Sorcery", sub_types="",
                     abilities=[133097], set_id="WAR", rarity="Uncommon", collectible=True, set_number=43,
                     mtga_id=69494)
CallousDismissal = Card(name="callous_dismissal", pretty_name="Callous Dismissal", cost=['1', 'U'],
                        color_identity=['U'], card_type="Sorcery", sub_types="",
                        abilities=[94618, 133105], set_id="WAR", rarity="Common", collectible=True, set_number=44,
                        mtga_id=69495)
CommencetheEndgame = Card(name="commence_the_endgame", pretty_name="Commence the Endgame", cost=['4', 'U', 'U'],
                          color_identity=['U'], card_type="Instant", sub_types="",
                          abilities=[120287, 133112], set_id="WAR", rarity="Rare", collectible=True, set_number=45,
                          mtga_id=69496)
ContentiousPlan = Card(name="contentious_plan", pretty_name="Contentious Plan", cost=['1', 'U'],
                       color_identity=['U'], card_type="Sorcery", sub_types="",
                       abilities=[18314, 25848], set_id="WAR", rarity="Common", collectible=True, set_number=46,
                       mtga_id=69497)
CrushDissent = Card(name="crush_dissent", pretty_name="Crush Dissent", cost=['3', 'U'],
                    color_identity=['U'], card_type="Instant", sub_types="",
                    abilities=[6374, 133127], set_id="WAR", rarity="Common", collectible=True, set_number=47,
                    mtga_id=69498)
ErraticVisionary = Card(name="erratic_visionary", pretty_name="Erratic Visionary", cost=['1', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                        abilities=[8760], set_id="WAR", rarity="Common", collectible=True, set_number=48,
                        mtga_id=69499)
EternalSkylord = Card(name="eternal_skylord", pretty_name="Eternal Skylord", cost=['4', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Zombie Wizard",
                      abilities=[133136, 133142], set_id="WAR", rarity="Uncommon", collectible=True, set_number=49,
                      mtga_id=69500)
FblthptheLost = Card(name="fblthp_the_lost", pretty_name="Fblthp, the Lost", cost=['1', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Homunculus",
                     abilities=[133147, 133153], set_id="WAR", rarity="Rare", collectible=True, set_number=50,
                     mtga_id=69501)
FinaleofRevelation = Card(name="finale_of_revelation", pretty_name="Finale of Revelation", cost=['X', 'U', 'U'],
                          color_identity=['U'], card_type="Sorcery", sub_types="",
                          abilities=[133340, 89260], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=51,
                          mtga_id=69502)
FluxChanneler = Card(name="flux_channeler", pretty_name="Flux Channeler", cost=['2', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Human Wizard",
                     abilities=[133166], set_id="WAR", rarity="Uncommon", collectible=True, set_number=52,
                     mtga_id=69503)
GodEternalKefnet = Card(name="godeternal_kefnet", pretty_name="God-Eternal Kefnet", cost=['2', 'U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Zombie God",
                        abilities=[8, 133171, 133098], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=53,
                        mtga_id=69504)
JaceWielderofMysteries = Card(name="jace_wielder_of_mysteries", pretty_name="Jace, Wielder of Mysteries", cost=['1', 'U', 'U', 'U'],
                              color_identity=['U'], card_type="Planeswalker", sub_types="Jace",
                              abilities=[18569, 133179, 133183], set_id="WAR", rarity="Rare", collectible=True, set_number=54,
                              mtga_id=69505)
JacesTriumph = Card(name="jaces_triumph", pretty_name="Jace's Triumph", cost=['2', 'U'],
                    color_identity=['U'], card_type="Sorcery", sub_types="",
                    abilities=[133189], set_id="WAR", rarity="Uncommon", collectible=True, set_number=55,
                    mtga_id=69506)
KasminaEnigmaticMentor = Card(name="kasmina_enigmatic_mentor", pretty_name="Kasmina, Enigmatic Mentor", cost=['3', 'U'],
                              color_identity=['U'], card_type="Planeswalker", sub_types="Kasmina",
                              abilities=[133193, 133197], set_id="WAR", rarity="Uncommon", collectible=True, set_number=56,
                              mtga_id=69507)
KasminasTransmutation = Card(name="kasminas_transmutation", pretty_name="Kasmina's Transmutation", cost=['1', 'U'],
                             color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                             abilities=[1027, 133200], set_id="WAR", rarity="Common", collectible=True, set_number=57,
                             mtga_id=69508)
KiorasDambreaker = Card(name="kioras_dambreaker", pretty_name="Kiora's Dambreaker", cost=['5', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Leviathan",
                        abilities=[133202], set_id="WAR", rarity="Common", collectible=True, set_number=58,
                        mtga_id=69509)
LazotepPlating = Card(name="lazotep_plating", pretty_name="Lazotep Plating", cost=['1', 'U'],
                      color_identity=['U'], card_type="Instant", sub_types="",
                      abilities=[133105, 133204], set_id="WAR", rarity="Uncommon", collectible=True, set_number=59,
                      mtga_id=69510)
NagaEternal = Card(name="naga_eternal", pretty_name="Naga Eternal", cost=['2', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Zombie Naga",
                   abilities=[], set_id="WAR", rarity="Common", collectible=True, set_number=60,
                   mtga_id=69511)
NarsetParterofVeils = Card(name="narset_parter_of_veils", pretty_name="Narset, Parter of Veils", cost=['1', 'U', 'U'],
                           color_identity=['U'], card_type="Planeswalker", sub_types="Narset",
                           abilities=[133205, 133207], set_id="WAR", rarity="Uncommon", collectible=True, set_number=61,
                           mtga_id=69512)
NarsetsReversal = Card(name="narsets_reversal", pretty_name="Narset's Reversal", cost=['U', 'U'],
                       color_identity=['U'], card_type="Instant", sub_types="",
                       abilities=[133209], set_id="WAR", rarity="Rare", collectible=True, set_number=62,
                       mtga_id=69513)
NoEscape = Card(name="no_escape", pretty_name="No Escape", cost=['2', 'U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[133345, 178], set_id="WAR", rarity="Common", collectible=True, set_number=63,
                mtga_id=69514)
RelentlessAdvance = Card(name="relentless_advance", pretty_name="Relentless Advance", cost=['3', 'U'],
                         color_identity=['U'], card_type="Sorcery", sub_types="",
                         abilities=[133211], set_id="WAR", rarity="Common", collectible=True, set_number=64,
                         mtga_id=69515)
RescuerSphinx = Card(name="rescuer_sphinx", pretty_name="Rescuer Sphinx", cost=['2', 'U', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Sphinx",
                     abilities=[8, 133212], set_id="WAR", rarity="Uncommon", collectible=True, set_number=65,
                     mtga_id=69516)
SilentSubmersible = Card(name="silent_submersible", pretty_name="Silent Submersible", cost=['U', 'U'],
                         color_identity=['U'], card_type="Artifact", sub_types="Vehicle",
                         abilities=[133213, 76645], set_id="WAR", rarity="Rare", collectible=True, set_number=66,
                         mtga_id=69517)
SkyTheaterStrix = Card(name="sky_theater_strix", pretty_name="Sky Theater Strix", cost=['1', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Bird",
                       abilities=[8, 133215], set_id="WAR", rarity="Common", collectible=True, set_number=67,
                       mtga_id=69518)
SparkDouble = Card(name="spark_double", pretty_name="Spark Double", cost=['3', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Illusion",
                   abilities=[133217], set_id="WAR", rarity="Rare", collectible=True, set_number=68,
                   mtga_id=69519)
SpellkeeperWeird = Card(name="spellkeeper_weird", pretty_name="Spellkeeper Weird", cost=['2', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Weird",
                        abilities=[133219], set_id="WAR", rarity="Common", collectible=True, set_number=69,
                        mtga_id=69520)
StealthMission = Card(name="stealth_mission", pretty_name="Stealth Mission", cost=['2', 'U'],
                      color_identity=['U'], card_type="Sorcery", sub_types="",
                      abilities=[133220], set_id="WAR", rarity="Common", collectible=True, set_number=70,
                      mtga_id=69521)
TamiyosEpiphany = Card(name="tamiyos_epiphany", pretty_name="Tamiyo's Epiphany", cost=['3', 'U'],
                       color_identity=['U'], card_type="Sorcery", sub_types="",
                       abilities=[3251], set_id="WAR", rarity="Common", collectible=True, set_number=71,
                       mtga_id=69522)
TeferisTimeTwist = Card(name="teferis_time_twist", pretty_name="Teferi's Time Twist", cost=['1', 'U'],
                        color_identity=['U'], card_type="Instant", sub_types="",
                        abilities=[133221], set_id="WAR", rarity="Common", collectible=True, set_number=72,
                        mtga_id=69523)
ThunderDrake = Card(name="thunder_drake", pretty_name="Thunder Drake", cost=['3', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Elemental Drake",
                    abilities=[8, 133223], set_id="WAR", rarity="Common", collectible=True, set_number=73,
                    mtga_id=69524)
TotallyLost = Card(name="totally_lost", pretty_name="Totally Lost", cost=['4', 'U'],
                   color_identity=['U'], card_type="Instant", sub_types="",
                   abilities=[99758], set_id="WAR", rarity="Common", collectible=True, set_number=74,
                   mtga_id=69525)
WallofRunes = Card(name="wall_of_runes", pretty_name="Wall of Runes", cost=['U'],
                   color_identity=['U'], card_type="Creature", sub_types="Wall",
                   abilities=[2, 91717], set_id="WAR", rarity="Common", collectible=True, set_number=75,
                   mtga_id=69526)
AidtheFallen = Card(name="aid_the_fallen", pretty_name="Aid the Fallen", cost=['1', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[133226], set_id="WAR", rarity="Common", collectible=True, set_number=76,
                    mtga_id=69527)
Banehound = Card(name="banehound", pretty_name="Banehound", cost=['B'],
                 color_identity=['B'], card_type="Creature", sub_types="Nightmare Hound",
                 abilities=[12, 9], set_id="WAR", rarity="Common", collectible=True, set_number=77,
                 mtga_id=69528)
BleedingEdge = Card(name="bleeding_edge", pretty_name="Bleeding Edge", cost=['1', 'B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[133228], set_id="WAR", rarity="Uncommon", collectible=True, set_number=78,
                    mtga_id=69529)
BolassCitadel = Card(name="bolass_citadel", pretty_name="Bolas's Citadel", cost=['3', 'B', 'B', 'B'],
                     color_identity=['B'], card_type="Artifact", sub_types="",
                     abilities=[14523, 133230, 133231], set_id="WAR", rarity="Rare", collectible=True, set_number=79,
                     mtga_id=69530)
BondofRevival = Card(name="bond_of_revival", pretty_name="Bond of Revival", cost=['4', 'B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[133347], set_id="WAR", rarity="Uncommon", collectible=True, set_number=80,
                     mtga_id=69531)
CharityExtractor = Card(name="charity_extractor", pretty_name="Charity Extractor", cost=['3', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Human Knight",
                        abilities=[12], set_id="WAR", rarity="Common", collectible=True, set_number=81,
                        mtga_id=69532)
CommandtheDreadhorde = Card(name="command_the_dreadhorde", pretty_name="Command the Dreadhorde", cost=['4', 'B', 'B'],
                            color_identity=['B'], card_type="Sorcery", sub_types="",
                            abilities=[133234], set_id="WAR", rarity="Rare", collectible=True, set_number=82,
                            mtga_id=69533)
DavrielRogueShadowmage = Card(name="davriel_rogue_shadowmage", pretty_name="Davriel, Rogue Shadowmage", cost=['2', 'B'],
                              color_identity=['B'], card_type="Planeswalker", sub_types="Davriel",
                              abilities=[133235, 133238], set_id="WAR", rarity="Uncommon", collectible=True, set_number=83,
                              mtga_id=69534)
DavrielsShadowfugue = Card(name="davriels_shadowfugue", pretty_name="Davriel's Shadowfugue", cost=['3', 'B'],
                           color_identity=['B'], card_type="Sorcery", sub_types="",
                           abilities=[18929], set_id="WAR", rarity="Common", collectible=True, set_number=84,
                           mtga_id=69535)
DeliverUntoEvil = Card(name="deliver_unto_evil", pretty_name="Deliver Unto Evil", cost=['2', 'B'],
                       color_identity=['B'], card_type="Sorcery", sub_types="",
                       abilities=[133239, 89260], set_id="WAR", rarity="Rare", collectible=True, set_number=85,
                       mtga_id=69536)
DreadhordeInvasion = Card(name="dreadhorde_invasion", pretty_name="Dreadhorde Invasion", cost=['1', 'B'],
                          color_identity=['B'], card_type="Enchantment", sub_types="",
                          abilities=[133348, 133241], set_id="WAR", rarity="Rare", collectible=True, set_number=86,
                          mtga_id=69537)
Dreadmalkin = Card(name="dreadmalkin", pretty_name="Dreadmalkin", cost=['B'],
                   color_identity=['B'], card_type="Creature", sub_types="Zombie Cat",
                   abilities=[142, 133243], set_id="WAR", rarity="Uncommon", collectible=True, set_number=87,
                   mtga_id=69538)
DuskmantleOperative = Card(name="duskmantle_operative", pretty_name="Duskmantle Operative", cost=['1', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Human Rogue",
                           abilities=[92664], set_id="WAR", rarity="Common", collectible=True, set_number=88,
                           mtga_id=69539)
TheElderspell = Card(name="the_elderspell", pretty_name="The Elderspell", cost=['B', 'B'],
                     color_identity=['B'], card_type="Sorcery", sub_types="",
                     abilities=[133350], set_id="WAR", rarity="Rare", collectible=True, set_number=89,
                     mtga_id=69540)
EternalTaskmaster = Card(name="eternal_taskmaster", pretty_name="Eternal Taskmaster", cost=['1', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Zombie",
                         abilities=[76735, 133248], set_id="WAR", rarity="Uncommon", collectible=True, set_number=90,
                         mtga_id=69541)
FinaleofEternity = Card(name="finale_of_eternity", pretty_name="Finale of Eternity", cost=['X', 'B', 'B'],
                        color_identity=['B'], card_type="Sorcery", sub_types="",
                        abilities=[133249], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=91,
                        mtga_id=69542)
GodEternalBontu = Card(name="godeternal_bontu", pretty_name="God-Eternal Bontu", cost=['3', 'B', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Zombie God",
                       abilities=[142, 133250, 133098], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=92,
                       mtga_id=69543)
HeraldoftheDreadhorde = Card(name="herald_of_the_dreadhorde", pretty_name="Herald of the Dreadhorde", cost=['3', 'B'],
                             color_identity=['B'], card_type="Creature", sub_types="Zombie Warrior",
                             abilities=[133252], set_id="WAR", rarity="Common", collectible=True, set_number=93,
                             mtga_id=69544)
KayasGhostform = Card(name="kayas_ghostform", pretty_name="Kaya's Ghostform", cost=['B'],
                      color_identity=['B'], card_type="Enchantment", sub_types="Aura",
                      abilities=[133253, 133254], set_id="WAR", rarity="Common", collectible=True, set_number=94,
                      mtga_id=69545)
LazotepBehemoth = Card(name="lazotep_behemoth", pretty_name="Lazotep Behemoth", cost=['4', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Zombie Hippo",
                       abilities=[], set_id="WAR", rarity="Common", collectible=True, set_number=95,
                       mtga_id=69546)
LazotepReaver = Card(name="lazotep_reaver", pretty_name="Lazotep Reaver", cost=['1', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Zombie Beast",
                     abilities=[133092], set_id="WAR", rarity="Common", collectible=True, set_number=96,
                     mtga_id=69547)
LilianaDreadhordeGeneral = Card(name="liliana_dreadhorde_general", pretty_name="Liliana, Dreadhorde General", cost=['4', 'B', 'B'],
                                color_identity=['B'], card_type="Planeswalker", sub_types="Liliana",
                                abilities=[133255, 133256, 133051, 133052], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=97,
                                mtga_id=69548)
LilianasTriumph = Card(name="lilianas_triumph", pretty_name="Liliana's Triumph", cost=['1', 'B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[133053], set_id="WAR", rarity="Uncommon", collectible=True, set_number=98,
                       mtga_id=69549)
MassacreGirl = Card(name="massacre_girl", pretty_name="Massacre Girl", cost=['3', 'B', 'B'],
                    color_identity=['B'], card_type="Creature", sub_types="Human Assassin",
                    abilities=[142, 133054], set_id="WAR", rarity="Rare", collectible=True, set_number=99,
                    mtga_id=69550)
ObNixilistheHateTwisted = Card(name="ob_nixilis_the_hatetwisted", pretty_name="Ob Nixilis, the Hate-Twisted", cost=['3', 'B', 'B'],
                               color_identity=['B'], card_type="Planeswalker", sub_types="Nixilis",
                               abilities=[88224, 133055], set_id="WAR", rarity="Uncommon", collectible=True, set_number=100,
                               mtga_id=69551)
ObNixilissCruelty = Card(name="ob_nixiliss_cruelty", pretty_name="Ob Nixilis's Cruelty", cost=['2', 'B'],
                         color_identity=['B'], card_type="Instant", sub_types="",
                         abilities=[133056], set_id="WAR", rarity="Common", collectible=True, set_number=101,
                         mtga_id=69552)
PriceofBetrayal = Card(name="price_of_betrayal", pretty_name="Price of Betrayal", cost=['B'],
                       color_identity=['B'], card_type="Sorcery", sub_types="",
                       abilities=[133057], set_id="WAR", rarity="Uncommon", collectible=True, set_number=102,
                       mtga_id=69553)
Shriekdiver = Card(name="shriekdiver", pretty_name="Shriekdiver", cost=['2', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Zombie Bird Warrior",
                   abilities=[8, 88067], set_id="WAR", rarity="Common", collectible=True, set_number=103,
                   mtga_id=69554)
SorinsThirst = Card(name="sorins_thirst", pretty_name="Sorin's Thirst", cost=['B', 'B'],
                    color_identity=['B'], card_type="Instant", sub_types="",
                    abilities=[86929], set_id="WAR", rarity="Common", collectible=True, set_number=104,
                    mtga_id=69555)
SparkHarvest = Card(name="spark_harvest", pretty_name="Spark Harvest", cost=['B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[133059, 19475], set_id="WAR", rarity="Common", collectible=True, set_number=105,
                    mtga_id=69556)
SparkReaper = Card(name="spark_reaper", pretty_name="Spark Reaper", cost=['2', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Zombie",
                   abilities=[133060], set_id="WAR", rarity="Common", collectible=True, set_number=106,
                   mtga_id=69557)
TithebearerGiant = Card(name="tithebearer_giant", pretty_name="Tithebearer Giant", cost=['5', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Giant Warrior",
                        abilities=[88159], set_id="WAR", rarity="Common", collectible=True, set_number=107,
                        mtga_id=69558)
TolloftheInvasion = Card(name="toll_of_the_invasion", pretty_name="Toll of the Invasion", cost=['2', 'B'],
                         color_identity=['B'], card_type="Sorcery", sub_types="",
                         abilities=[117067, 133105], set_id="WAR", rarity="Common", collectible=True, set_number=108,
                         mtga_id=69559)
UnlikelyAid = Card(name="unlikely_aid", pretty_name="Unlikely Aid", cost=['1', 'B'],
                   color_identity=['B'], card_type="Instant", sub_types="",
                   abilities=[133061], set_id="WAR", rarity="Common", collectible=True, set_number=109,
                   mtga_id=69560)
VampireOpportunist = Card(name="vampire_opportunist", pretty_name="Vampire Opportunist", cost=['1', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Vampire",
                          abilities=[133264], set_id="WAR", rarity="Common", collectible=True, set_number=110,
                          mtga_id=69561)
VizieroftheScorpion = Card(name="vizier_of_the_scorpion", pretty_name="Vizier of the Scorpion", cost=['2', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Zombie Wizard",
                           abilities=[133092, 133265], set_id="WAR", rarity="Uncommon", collectible=True, set_number=111,
                           mtga_id=69562)
VraskasFinisher = Card(name="vraskas_finisher", pretty_name="Vraska's Finisher", cost=['2', 'B'],
                       color_identity=['B'], card_type="Creature", sub_types="Gorgon Assassin",
                       abilities=[133266], set_id="WAR", rarity="Common", collectible=True, set_number=112,
                       mtga_id=69563)
AhnCropInvader = Card(name="ahncrop_invader", pretty_name="Ahn-Crop Invader", cost=['2', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Zombie Minotaur Warrior",
                      abilities=[121419, 133268], set_id="WAR", rarity="Common", collectible=True, set_number=113,
                      mtga_id=69564)
Blindblast = Card(name="blindblast", pretty_name="Blindblast", cost=['2', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[133269, 25848], set_id="WAR", rarity="Common", collectible=True, set_number=114,
                  mtga_id=69565)
BoltBend = Card(name="bolt_bend", pretty_name="Bolt Bend", cost=['3', 'R'],
                color_identity=['R'], card_type="Instant", sub_types="",
                abilities=[133270, 133271], set_id="WAR", rarity="Uncommon", collectible=True, set_number=115,
                mtga_id=69566)
BondofPassion = Card(name="bond_of_passion", pretty_name="Bond of Passion", cost=['4', 'R', 'R'],
                     color_identity=['R'], card_type="Sorcery", sub_types="",
                     abilities=[133272], set_id="WAR", rarity="Uncommon", collectible=True, set_number=116,
                     mtga_id=69567)
BurningProphet = Card(name="burning_prophet", pretty_name="Burning Prophet", cost=['1', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Human Wizard",
                      abilities=[133273], set_id="WAR", rarity="Common", collectible=True, set_number=117,
                      mtga_id=69568)
ChainwhipCyclops = Card(name="chainwhip_cyclops", pretty_name="Chainwhip Cyclops", cost=['4', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Cyclops Warrior",
                        abilities=[119252], set_id="WAR", rarity="Common", collectible=True, set_number=118,
                        mtga_id=69569)
ChandraFireArtisan = Card(name="chandra_fire_artisan", pretty_name="Chandra, Fire Artisan", cost=['2', 'R', 'R'],
                          color_identity=['R'], card_type="Planeswalker", sub_types="Chandra",
                          abilities=[133352, 133276, 133353], set_id="WAR", rarity="Rare", collectible=True, set_number=119,
                          mtga_id=69570)
ChandrasPyrohelix = Card(name="chandras_pyrohelix", pretty_name="Chandra's Pyrohelix", cost=['1', 'R'],
                         color_identity=['R'], card_type="Instant", sub_types="",
                         abilities=[90088], set_id="WAR", rarity="Common", collectible=True, set_number=120,
                         mtga_id=69571)
ChandrasTriumph = Card(name="chandras_triumph", pretty_name="Chandra's Triumph", cost=['1', 'R'],
                       color_identity=['R'], card_type="Instant", sub_types="",
                       abilities=[133354], set_id="WAR", rarity="Uncommon", collectible=True, set_number=121,
                       mtga_id=69572)
CyclopsElectromancer = Card(name="cyclops_electromancer", pretty_name="Cyclops Electromancer", cost=['4', 'R'],
                            color_identity=['R'], card_type="Creature", sub_types="Cyclops Wizard",
                            abilities=[88037], set_id="WAR", rarity="Uncommon", collectible=True, set_number=122,
                            mtga_id=69573)
Demolish = Card(name="demolish", pretty_name="Demolish", cost=['3', 'R'],
                color_identity=['R'], card_type="Sorcery", sub_types="",
                abilities=[1691], set_id="WAR", rarity="Common", collectible=True, set_number=123,
                mtga_id=69574)
DevouringHellion = Card(name="devouring_hellion", pretty_name="Devouring Hellion", cost=['2', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Hellion",
                        abilities=[133337], set_id="WAR", rarity="Uncommon", collectible=True, set_number=124,
                        mtga_id=69575)
DreadhordeArcanist = Card(name="dreadhorde_arcanist", pretty_name="Dreadhorde Arcanist", cost=['1', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Zombie Wizard",
                          abilities=[14, 133064], set_id="WAR", rarity="Rare", collectible=True, set_number=125,
                          mtga_id=69576)
DreadhordeTwins = Card(name="dreadhorde_twins", pretty_name="Dreadhorde Twins", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Zombie Jackal Warrior",
                       abilities=[133136, 133065], set_id="WAR", rarity="Uncommon", collectible=True, set_number=126,
                       mtga_id=69577)
FinaleofPromise = Card(name="finale_of_promise", pretty_name="Finale of Promise", cost=['X', 'R', 'R'],
                       color_identity=['R'], card_type="Sorcery", sub_types="",
                       abilities=[133355], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=127,
                       mtga_id=69578)
GoblinAssailant = Card(name="goblin_assailant", pretty_name="Goblin Assailant", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                       abilities=[], set_id="WAR", rarity="Common", collectible=True, set_number=128,
                       mtga_id=69579)
GoblinAssaultTeam = Card(name="goblin_assault_team", pretty_name="Goblin Assault Team", cost=['3', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Goblin Warrior",
                         abilities=[9, 87008], set_id="WAR", rarity="Common", collectible=True, set_number=129,
                         mtga_id=69580)
GrimInitiate = Card(name="grim_initiate", pretty_name="Grim Initiate", cost=['R'],
                    color_identity=['R'], card_type="Creature", sub_types="Zombie Warrior",
                    abilities=[6, 133287], set_id="WAR", rarity="Common", collectible=True, set_number=130,
                    mtga_id=69581)
Heartfire = Card(name="heartfire", pretty_name="Heartfire", cost=['1', 'R'],
                 color_identity=['R'], card_type="Instant", sub_types="",
                 abilities=[133289, 2200], set_id="WAR", rarity="Common", collectible=True, set_number=131,
                 mtga_id=69582)
HonortheGodPharaoh = Card(name="honor_the_godpharaoh", pretty_name="Honor the God-Pharaoh", cost=['2', 'R'],
                          color_identity=['R'], card_type="Sorcery", sub_types="",
                          abilities=[87929, 133290], set_id="WAR", rarity="Common", collectible=True, set_number=132,
                          mtga_id=69583)
IlhargtheRazeBoar = Card(name="ilharg_the_razeboar", pretty_name="Ilharg, the Raze-Boar", cost=['3', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Boar God",
                         abilities=[14, 133291, 133098], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=133,
                         mtga_id=69584)
InvadingManticore = Card(name="invading_manticore", pretty_name="Invading Manticore", cost=['5', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Zombie Manticore",
                         abilities=[133136], set_id="WAR", rarity="Common", collectible=True, set_number=134,
                         mtga_id=69585)
JayaVeneratedFiremage = Card(name="jaya_venerated_firemage", pretty_name="Jaya, Venerated Firemage", cost=['4', 'R'],
                             color_identity=['R'], card_type="Planeswalker", sub_types="Jaya",
                             abilities=[62019, 133292], set_id="WAR", rarity="Uncommon", collectible=True, set_number=135,
                             mtga_id=69586)
JayasGreeting = Card(name="jayas_greeting", pretty_name="Jaya's Greeting", cost=['1', 'R'],
                     color_identity=['R'], card_type="Instant", sub_types="",
                     abilities=[133294], set_id="WAR", rarity="Common", collectible=True, set_number=136,
                     mtga_id=69587)
KrenkoTinStreetKingpin = Card(name="krenko_tin_street_kingpin", pretty_name="Krenko, Tin Street Kingpin", cost=['2', 'R'],
                              color_identity=['R'], card_type="Creature", sub_types="Goblin",
                              abilities=[133295], set_id="WAR", rarity="Rare", collectible=True, set_number=137,
                              mtga_id=69588)
MizziumTank = Card(name="mizzium_tank", pretty_name="Mizzium Tank", cost=['1', 'R', 'R'],
                   color_identity=['R'], card_type="Artifact", sub_types="Vehicle",
                   abilities=[14, 133296, 76556], set_id="WAR", rarity="Rare", collectible=True, set_number=138,
                   mtga_id=69589)
NahirisStoneblades = Card(name="nahiris_stoneblades", pretty_name="Nahiri's Stoneblades", cost=['1', 'R'],
                          color_identity=['R'], card_type="Instant", sub_types="",
                          abilities=[133299], set_id="WAR", rarity="Common", collectible=True, set_number=139,
                          mtga_id=69590)
NehebDreadhordeChampion = Card(name="neheb_dreadhorde_champion", pretty_name="Neheb, Dreadhorde Champion", cost=['2', 'R', 'R'],
                               color_identity=['R'], card_type="Creature", sub_types="Zombie Minotaur Warrior",
                               abilities=[14, 133301], set_id="WAR", rarity="Rare", collectible=True, set_number=140,
                               mtga_id=69591)
RagingKronch = Card(name="raging_kronch", pretty_name="Raging Kronch", cost=['2', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Beast",
                    abilities=[76418], set_id="WAR", rarity="Common", collectible=True, set_number=141,
                    mtga_id=69592)
SamutsSprint = Card(name="samuts_sprint", pretty_name="Samut's Sprint", cost=['R'],
                    color_identity=['R'], card_type="Instant", sub_types="",
                    abilities=[133302], set_id="WAR", rarity="Common", collectible=True, set_number=142,
                    mtga_id=69593)
SarkhantheMasterless = Card(name="sarkhan_the_masterless", pretty_name="Sarkhan the Masterless", cost=['3', 'R', 'R'],
                            color_identity=['R'], card_type="Planeswalker", sub_types="Sarkhan",
                            abilities=[133303, 133305, 133308], set_id="WAR", rarity="Rare", collectible=True, set_number=143,
                            mtga_id=69594)
SarkhansCatharsis = Card(name="sarkhans_catharsis", pretty_name="Sarkhan's Catharsis", cost=['4', 'R'],
                         color_identity=['R'], card_type="Instant", sub_types="",
                         abilities=[1118], set_id="WAR", rarity="Common", collectible=True, set_number=144,
                         mtga_id=69595)
SpellgorgerWeird = Card(name="spellgorger_weird", pretty_name="Spellgorger Weird", cost=['2', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Weird",
                        abilities=[1208], set_id="WAR", rarity="Common", collectible=True, set_number=145,
                        mtga_id=69596)
TibaltRakishInstigator = Card(name="tibalt_rakish_instigator", pretty_name="Tibalt, Rakish Instigator", cost=['2', 'R'],
                              color_identity=['R'], card_type="Planeswalker", sub_types="Tibalt",
                              abilities=[20451, 133309], set_id="WAR", rarity="Uncommon", collectible=True, set_number=146,
                              mtga_id=69597)
TibaltsRager = Card(name="tibalts_rager", pretty_name="Tibalt's Rager", cost=['1', 'R'],
                    color_identity=['R'], card_type="Creature", sub_types="Devil",
                    abilities=[1285, 76843], set_id="WAR", rarity="Uncommon", collectible=True, set_number=147,
                    mtga_id=69598)
TurretOgre = Card(name="turret_ogre", pretty_name="Turret Ogre", cost=['3', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Ogre Warrior",
                  abilities=[13, 133319], set_id="WAR", rarity="Common", collectible=True, set_number=148,
                  mtga_id=69599)
ArborealGrazer = Card(name="arboreal_grazer", pretty_name="Arboreal Grazer", cost=['G'],
                      color_identity=['G'], card_type="Creature", sub_types="Beast",
                      abilities=[13, 133133], set_id="WAR", rarity="Common", collectible=True, set_number=149,
                      mtga_id=69600)
ArlinnVoiceofthePack = Card(name="arlinn_voice_of_the_pack", pretty_name="Arlinn, Voice of the Pack", cost=['4', 'G', 'G'],
                            color_identity=['G'], card_type="Planeswalker", sub_types="Arlinn",
                            abilities=[133214, 133244], set_id="WAR", rarity="Uncommon", collectible=True, set_number=150,
                            mtga_id=69601)
ArlinnsWolf = Card(name="arlinns_wolf", pretty_name="Arlinn's Wolf", cost=['2', 'G'],
                   color_identity=['G'], card_type="Creature", sub_types="Wolf",
                   abilities=[87941], set_id="WAR", rarity="Common", collectible=True, set_number=151,
                   mtga_id=69602)
AwakeningofVituGhazi = Card(name="awakening_of_vitughazi", pretty_name="Awakening of Vitu-Ghazi", cost=['3', 'G', 'G'],
                            color_identity=['G'], card_type="Instant", sub_types="",
                            abilities=[133288], set_id="WAR", rarity="Rare", collectible=True, set_number=152,
                            mtga_id=69603)
BandTogether = Card(name="band_together", pretty_name="Band Together", cost=['2', 'G'],
                    color_identity=['G'], card_type="Instant", sub_types="",
                    abilities=[133067], set_id="WAR", rarity="Common", collectible=True, set_number=153,
                    mtga_id=69604)
BloomHulk = Card(name="bloom_hulk", pretty_name="Bloom Hulk", cost=['3', 'G'],
                 color_identity=['G'], card_type="Creature", sub_types="Plant Elemental",
                 abilities=[133202], set_id="WAR", rarity="Common", collectible=True, set_number=154,
                 mtga_id=69605)
BondofFlourishing = Card(name="bond_of_flourishing", pretty_name="Bond of Flourishing", cost=['1', 'G'],
                         color_identity=['G'], card_type="Sorcery", sub_types="",
                         abilities=[133068], set_id="WAR", rarity="Uncommon", collectible=True, set_number=155,
                         mtga_id=69606)
CentaurNurturer = Card(name="centaur_nurturer", pretty_name="Centaur Nurturer", cost=['3', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Centaur Druid",
                       abilities=[1102, 1055], set_id="WAR", rarity="Common", collectible=True, set_number=156,
                       mtga_id=69607)
ChallengerTroll = Card(name="challenger_troll", pretty_name="Challenger Troll", cost=['4', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Troll",
                       abilities=[133069], set_id="WAR", rarity="Uncommon", collectible=True, set_number=157,
                       mtga_id=69608)
CourageinCrisis = Card(name="courage_in_crisis", pretty_name="Courage in Crisis", cost=['2', 'G'],
                       color_identity=['G'], card_type="Sorcery", sub_types="",
                       abilities=[133199], set_id="WAR", rarity="Common", collectible=True, set_number=158,
                       mtga_id=69609)
EvolutionSage = Card(name="evolution_sage", pretty_name="Evolution Sage", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                     abilities=[133071], set_id="WAR", rarity="Uncommon", collectible=True, set_number=159,
                     mtga_id=69610)
FinaleofDevastation = Card(name="finale_of_devastation", pretty_name="Finale of Devastation", cost=['X', 'G', 'G'],
                           color_identity=['G'], card_type="Sorcery", sub_types="",
                           abilities=[135155], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=160,
                           mtga_id=69611)
ForcedLanding = Card(name="forced_landing", pretty_name="Forced Landing", cost=['1', 'G'],
                     color_identity=['G'], card_type="Instant", sub_types="",
                     abilities=[133073], set_id="WAR", rarity="Common", collectible=True, set_number=161,
                     mtga_id=69612)
GiantGrowth = Card(name="giant_growth", pretty_name="Giant Growth", cost=['G'],
                   color_identity=['G'], card_type="Instant", sub_types="",
                   abilities=[24733], set_id="WAR", rarity="Common", collectible=True, set_number=162,
                   mtga_id=69613)
GodEternalRhonas = Card(name="godeternal_rhonas", pretty_name="God-Eternal Rhonas", cost=['3', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Zombie God",
                        abilities=[1, 133074, 133098], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=163,
                        mtga_id=69614)
JiangYangguWildcrafter = Card(name="jiang_yanggu_wildcrafter", pretty_name="Jiang Yanggu, Wildcrafter", cost=['2', 'G'],
                              color_identity=['G'], card_type="Planeswalker", sub_types="Yanggu",
                              abilities=[133237, 133242], set_id="WAR", rarity="Uncommon", collectible=True, set_number=164,
                              mtga_id=69615)
KraulStinger = Card(name="kraul_stinger", pretty_name="Kraul Stinger", cost=['2', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Insect Assassin",
                    abilities=[1], set_id="WAR", rarity="Common", collectible=True, set_number=165,
                    mtga_id=69616)
KronchWrangler = Card(name="kronch_wrangler", pretty_name="Kronch Wrangler", cost=['1', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Human Warrior",
                      abilities=[14, 133077], set_id="WAR", rarity="Common", collectible=True, set_number=166,
                      mtga_id=69617)
MowuLoyalCompanion = Card(name="mowu_loyal_companion", pretty_name="Mowu, Loyal Companion", cost=['3', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Hound",
                          abilities=[14, 15, 133078], set_id="WAR", rarity="Uncommon", collectible=True, set_number=167,
                          mtga_id=69618)
NewHorizons = Card(name="new_horizons", pretty_name="New Horizons", cost=['2', 'G'],
                   color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                   abilities=[1570, 101825, 61119], set_id="WAR", rarity="Common", collectible=True, set_number=168,
                   mtga_id=69619)
NissaWhoShakestheWorld = Card(name="nissa_who_shakes_the_world", pretty_name="Nissa, Who Shakes the World", cost=['3', 'G', 'G'],
                              color_identity=['G'], card_type="Planeswalker", sub_types="Nissa",
                              abilities=[133080, 133081, 133083], set_id="WAR", rarity="Rare", collectible=True, set_number=169,
                              mtga_id=69620)
NissasTriumph = Card(name="nissas_triumph", pretty_name="Nissa's Triumph", cost=['G', 'G'],
                     color_identity=['G'], card_type="Sorcery", sub_types="",
                     abilities=[133084], set_id="WAR", rarity="Uncommon", collectible=True, set_number=170,
                     mtga_id=69621)
ParadiseDruid = Card(name="paradise_druid", pretty_name="Paradise Druid", cost=['1', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                     abilities=[102136, 1055], set_id="WAR", rarity="Uncommon", collectible=True, set_number=171,
                     mtga_id=69622)
PlanewideCelebration = Card(name="planewide_celebration", pretty_name="Planewide Celebration", cost=['5', 'G', 'G'],
                            color_identity=['G'], card_type="Sorcery", sub_types="",
                            abilities=[133643], set_id="WAR", rarity="Rare", collectible=True, set_number=172,
                            mtga_id=69623)
PollenbrightDruid = Card(name="pollenbright_druid", pretty_name="Pollenbright Druid", cost=['1', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Elf Druid",
                         abilities=[133099], set_id="WAR", rarity="Common", collectible=True, set_number=173,
                         mtga_id=69624)
PrimordialWurm = Card(name="primordial_wurm", pretty_name="Primordial Wurm", cost=['4', 'G', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Wurm",
                      abilities=[], set_id="WAR", rarity="Common", collectible=True, set_number=174,
                      mtga_id=69625)
ReturntoNature = Card(name="return_to_nature", pretty_name="Return to Nature", cost=['1', 'G'],
                      color_identity=['G'], card_type="Instant", sub_types="",
                      abilities=[133114], set_id="WAR", rarity="Common", collectible=True, set_number=175,
                      mtga_id=69626)
Snarespinner = Card(name="snarespinner", pretty_name="Snarespinner", cost=['1', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Spider",
                    abilities=[13, 101422], set_id="WAR", rarity="Common", collectible=True, set_number=176,
                    mtga_id=69627)
SteadyAim = Card(name="steady_aim", pretty_name="Steady Aim", cost=['1', 'G'],
                 color_identity=['G'], card_type="Instant", sub_types="",
                 abilities=[133093], set_id="WAR", rarity="Common", collectible=True, set_number=177,
                 mtga_id=69628)
StormtheCitadel = Card(name="storm_the_citadel", pretty_name="Storm the Citadel", cost=['4', 'G'],
                       color_identity=['G'], card_type="Sorcery", sub_types="",
                       abilities=[133095], set_id="WAR", rarity="Uncommon", collectible=True, set_number=178,
                       mtga_id=69629)
ThunderingCeratok = Card(name="thundering_ceratok", pretty_name="Thundering Ceratok", cost=['4', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Rhino",
                         abilities=[14, 133096], set_id="WAR", rarity="Common", collectible=True, set_number=179,
                         mtga_id=69630)
VivienChampionoftheWilds = Card(name="vivien_champion_of_the_wilds", pretty_name="Vivien, Champion of the Wilds", cost=['2', 'G'],
                                color_identity=['G'], card_type="Planeswalker", sub_types="Vivien",
                                abilities=[20474, 133149, 133154], set_id="WAR", rarity="Rare", collectible=True, set_number=180,
                                mtga_id=69631)
ViviensArkbow = Card(name="viviens_arkbow", pretty_name="Vivien's Arkbow", cost=['1', 'G'],
                     color_identity=['G'], card_type="Artifact", sub_types="",
                     abilities=[133100], set_id="WAR", rarity="Rare", collectible=True, set_number=181,
                     mtga_id=69632)
ViviensGrizzly = Card(name="viviens_grizzly", pretty_name="Vivien's Grizzly", cost=['2', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Bear Spirit",
                      abilities=[133101], set_id="WAR", rarity="Common", collectible=True, set_number=182,
                      mtga_id=69633)
WardscaleCrocodile = Card(name="wardscale_crocodile", pretty_name="Wardscale Crocodile", cost=['4', 'G'],
                          color_identity=['G'], card_type="Creature", sub_types="Crocodile",
                          abilities=[10], set_id="WAR", rarity="Common", collectible=True, set_number=183,
                          mtga_id=69634)
AjanitheGreathearted = Card(name="ajani_the_greathearted", pretty_name="Ajani, the Greathearted", cost=['2', 'G', 'W'],
                            color_identity=['G', 'W'], card_type="Planeswalker", sub_types="Ajani",
                            abilities=[7132, 133173, 101312], set_id="WAR", rarity="Rare", collectible=True, set_number=184,
                            mtga_id=69635)
AngrathsRampage = Card(name="angraths_rampage", pretty_name="Angrath's Rampage", cost=['B', 'R'],
                       color_identity=['B', 'R'], card_type="Sorcery", sub_types="",
                       abilities=[133104], set_id="WAR", rarity="Uncommon", collectible=True, set_number=185,
                       mtga_id=69636)
BioessenceHydra = Card(name="bioessence_hydra", pretty_name="Bioessence Hydra", cost=['3', 'G', 'U'],
                       color_identity=['G', 'U'], card_type="Creature", sub_types="Hydra Mutant",
                       abilities=[14, 133198, 133106], set_id="WAR", rarity="Rare", collectible=True, set_number=186,
                       mtga_id=69637)
CasualtiesofWar = Card(name="casualties_of_war", pretty_name="Casualties of War", cost=['2', 'B', 'B', 'G', 'G'],
                       color_identity=['B', 'G'], card_type="Sorcery", sub_types="",
                       abilities=[133107], set_id="WAR", rarity="Rare", collectible=True, set_number=187,
                       mtga_id=69638)
CruelCelebrant = Card(name="cruel_celebrant", pretty_name="Cruel Celebrant", cost=['W', 'B'],
                      color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire",
                      abilities=[133208], set_id="WAR", rarity="Uncommon", collectible=True, set_number=188,
                      mtga_id=69639)
Deathsprout = Card(name="deathsprout", pretty_name="Deathsprout", cost=['1', 'B', 'B', 'G'],
                   color_identity=['B', 'G'], card_type="Instant", sub_types="",
                   abilities=[133108], set_id="WAR", rarity="Uncommon", collectible=True, set_number=189,
                   mtga_id=69640)
DomriAnarchofBolas = Card(name="domri_anarch_of_bolas", pretty_name="Domri, Anarch of Bolas", cost=['1', 'R', 'G'],
                          color_identity=['R', 'G'], card_type="Planeswalker", sub_types="Domri",
                          abilities=[18850, 133109, 133110], set_id="WAR", rarity="Rare", collectible=True, set_number=191,
                          mtga_id=69641)
DomrisAmbush = Card(name="domris_ambush", pretty_name="Domri's Ambush", cost=['R', 'G'],
                    color_identity=['R', 'G'], card_type="Sorcery", sub_types="",
                    abilities=[133111], set_id="WAR", rarity="Uncommon", collectible=True, set_number=192,
                    mtga_id=69642)
DovinsVeto = Card(name="dovins_veto", pretty_name="Dovin's Veto", cost=['W', 'U'],
                  color_identity=['W', 'U'], card_type="Instant", sub_types="",
                  abilities=[120287, 1142], set_id="WAR", rarity="Uncommon", collectible=True, set_number=193,
                  mtga_id=69643)
DreadhordeButcher = Card(name="dreadhorde_butcher", pretty_name="Dreadhorde Butcher", cost=['B', 'R'],
                         color_identity=['B', 'R'], card_type="Creature", sub_types="Zombie Warrior",
                         abilities=[9, 133113, 133218], set_id="WAR", rarity="Rare", collectible=True, set_number=194,
                         mtga_id=69644)
EliteGuardmage = Card(name="elite_guardmage", pretty_name="Elite Guardmage", cost=['2', 'W', 'U'],
                      color_identity=['W', 'U'], card_type="Creature", sub_types="Human Wizard",
                      abilities=[8, 133115], set_id="WAR", rarity="Uncommon", collectible=True, set_number=195,
                      mtga_id=69645)
EntertheGodEternals = Card(name="enter_the_godeternals", pretty_name="Enter the God-Eternals", cost=['2', 'U', 'U', 'B'],
                           color_identity=['U', 'B'], card_type="Sorcery", sub_types="",
                           abilities=[133116], set_id="WAR", rarity="Rare", collectible=True, set_number=196,
                           mtga_id=69646)
FeathertheRedeemed = Card(name="feather_the_redeemed", pretty_name="Feather, the Redeemed", cost=['R', 'W', 'W'],
                          color_identity=['R', 'W'], card_type="Creature", sub_types="Angel",
                          abilities=[8, 133117], set_id="WAR", rarity="Rare", collectible=True, set_number=197,
                          mtga_id=69647)
GleamingOverseer = Card(name="gleaming_overseer", pretty_name="Gleaming Overseer", cost=['1', 'U', 'B'],
                        color_identity=['U', 'B'], card_type="Creature", sub_types="Zombie Wizard",
                        abilities=[133092, 133222], set_id="WAR", rarity="Uncommon", collectible=True, set_number=198,
                        mtga_id=69648)
HeartwarmingRedemption = Card(name="heartwarming_redemption", pretty_name="Heartwarming Redemption", cost=['2', 'R', 'W'],
                              color_identity=['R', 'W'], card_type="Instant", sub_types="",
                              abilities=[133224], set_id="WAR", rarity="Uncommon", collectible=True, set_number=199,
                              mtga_id=69649)
HuatlisRaptor = Card(name="huatlis_raptor", pretty_name="Huatli's Raptor", cost=['G', 'W'],
                     color_identity=['G', 'W'], card_type="Creature", sub_types="Dinosaur",
                     abilities=[15, 133202], set_id="WAR", rarity="Uncommon", collectible=True, set_number=200,
                     mtga_id=69650)
LeylineProwler = Card(name="leyline_prowler", pretty_name="Leyline Prowler", cost=['1', 'B', 'G'],
                      color_identity=['B', 'G'], card_type="Creature", sub_types="Nightmare Beast",
                      abilities=[1, 12, 1055], set_id="WAR", rarity="Uncommon", collectible=True, set_number=202,
                      mtga_id=69652)
MayhemDevil = Card(name="mayhem_devil", pretty_name="Mayhem Devil", cost=['1', 'B', 'R'],
                   color_identity=['B', 'R'], card_type="Creature", sub_types="Devil",
                   abilities=[133120], set_id="WAR", rarity="Uncommon", collectible=True, set_number=204,
                   mtga_id=69653)
MerfolkSkydiver = Card(name="merfolk_skydiver", pretty_name="Merfolk Skydiver", cost=['G', 'U'],
                       color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Mutant",
                       abilities=[8, 101825, 133121], set_id="WAR", rarity="Uncommon", collectible=True, set_number=205,
                       mtga_id=69654)
Neoform = Card(name="neoform", pretty_name="Neoform", cost=['G', 'U'],
               color_identity=['G', 'U'], card_type="Sorcery", sub_types="",
               abilities=[1275, 133229], set_id="WAR", rarity="Uncommon", collectible=True, set_number=206,
               mtga_id=69655)
NicolBolasDragonGod = Card(name="nicol_bolas_dragongod", pretty_name="Nicol Bolas, Dragon-God", cost=['U', 'B', 'B', 'B', 'R'],
                           color_identity=['U', 'B', 'R'], card_type="Planeswalker", sub_types="Bolas",
                           abilities=[133122, 133123, 133124, 133125], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=207,
                           mtga_id=69656)
NivMizzetReborn = Card(name="nivmizzet_reborn", pretty_name="Niv-Mizzet Reborn", cost=['W', 'U', 'B', 'R', 'G'],
                       color_identity=['W', 'U', 'B', 'R', 'G'], card_type="Creature", sub_types="Dragon Avatar",
                       abilities=[8, 133126], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=208,
                       mtga_id=69657)
OathofKaya = Card(name="oath_of_kaya", pretty_name="Oath of Kaya", cost=['1', 'W', 'B'],
                  color_identity=['W', 'B'], card_type="Enchantment", sub_types="",
                  abilities=[133236, 133339], set_id="WAR", rarity="Rare", collectible=True, set_number=209,
                  mtga_id=69658)
PledgeofUnity = Card(name="pledge_of_unity", pretty_name="Pledge of Unity", cost=['1', 'G', 'W'],
                     color_identity=['G', 'W'], card_type="Instant", sub_types="",
                     abilities=[133129], set_id="WAR", rarity="Uncommon", collectible=True, set_number=210,
                     mtga_id=69659)
RalStormConduit = Card(name="ral_storm_conduit", pretty_name="Ral, Storm Conduit", cost=['2', 'U', 'R'],
                       color_identity=['U', 'R'], card_type="Planeswalker", sub_types="Ral",
                       abilities=[133130, 133131, 93029], set_id="WAR", rarity="Rare", collectible=True, set_number=211,
                       mtga_id=69660)
RalsOutburst = Card(name="rals_outburst", pretty_name="Ral's Outburst", cost=['2', 'U', 'R'],
                    color_identity=['U', 'R'], card_type="Instant", sub_types="",
                    abilities=[133282], set_id="WAR", rarity="Uncommon", collectible=True, set_number=212,
                    mtga_id=69661)
RoaleskApexHybrid = Card(name="roalesk_apex_hybrid", pretty_name="Roalesk, Apex Hybrid", cost=['2', 'G', 'G', 'U'],
                         color_identity=['G', 'U'], card_type="Creature", sub_types="Human Mutant",
                         abilities=[8, 14, 133132, 133349], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=213,
                         mtga_id=69662)
RoleReversal = Card(name="role_reversal", pretty_name="Role Reversal", cost=['U', 'U', 'R'],
                    color_identity=['U', 'R'], card_type="Sorcery", sub_types="",
                    abilities=[133134], set_id="WAR", rarity="Rare", collectible=True, set_number=214,
                    mtga_id=69663)
RubblebeltRioters = Card(name="rubblebelt_rioters", pretty_name="Rubblebelt Rioters", cost=['1', 'R', 'G'],
                         color_identity=['R', 'G'], card_type="Creature", sub_types="Human Berserker",
                         abilities=[9, 133135], set_id="WAR", rarity="Uncommon", collectible=True, set_number=215,
                         mtga_id=69664)
SolarBlaze = Card(name="solar_blaze", pretty_name="Solar Blaze", cost=['2', 'R', 'W'],
                  color_identity=['R', 'W'], card_type="Sorcery", sub_types="",
                  abilities=[15287], set_id="WAR", rarity="Rare", collectible=True, set_number=216,
                  mtga_id=69665)
SorinVengefulBloodlord = Card(name="sorin_vengeful_bloodlord", pretty_name="Sorin, Vengeful Bloodlord", cost=['2', 'W', 'B'],
                              color_identity=['W', 'B'], card_type="Planeswalker", sub_types="Sorin",
                              abilities=[133251, 133137, 133138], set_id="WAR", rarity="Rare", collectible=True, set_number=217,
                              mtga_id=69666)
SoulDiviner = Card(name="soul_diviner", pretty_name="Soul Diviner", cost=['U', 'B'],
                   color_identity=['U', 'B'], card_type="Creature", sub_types="Zombie Wizard",
                   abilities=[133139], set_id="WAR", rarity="Rare", collectible=True, set_number=218,
                   mtga_id=69667)
StorrevDevkarinLich = Card(name="storrev_devkarin_lich", pretty_name="Storrev, Devkarin Lich", cost=['1', 'B', 'B', 'G'],
                           color_identity=['B', 'G'], card_type="Creature", sub_types="Zombie Elf Wizard",
                           abilities=[14, 133140], set_id="WAR", rarity="Rare", collectible=True, set_number=219,
                           mtga_id=69668)
TamiyoCollectorofTales = Card(name="tamiyo_collector_of_tales", pretty_name="Tamiyo, Collector of Tales", cost=['2', 'G', 'U'],
                              color_identity=['G', 'U'], card_type="Planeswalker", sub_types="Tamiyo",
                              abilities=[133141, 133257, 133258], set_id="WAR", rarity="Rare", collectible=True, set_number=220,
                              mtga_id=69669)
TeferiTimeRaveler = Card(name="teferi_time_raveler", pretty_name="Teferi, Time Raveler", cost=['1', 'W', 'U'],
                         color_identity=['W', 'U'], card_type="Planeswalker", sub_types="Teferi",
                         abilities=[6363, 133144, 133145], set_id="WAR", rarity="Rare", collectible=True, set_number=221,
                         mtga_id=69670)
TenthDistrictLegionnaire = Card(name="tenth_district_legionnaire", pretty_name="Tenth District Legionnaire", cost=['R', 'W'],
                                color_identity=['R', 'W'], card_type="Creature", sub_types="Human Soldier",
                                abilities=[9, 133146], set_id="WAR", rarity="Uncommon", collectible=True, set_number=222,
                                mtga_id=69671)
TimeWipe = Card(name="time_wipe", pretty_name="Time Wipe", cost=['2', 'W', 'W', 'U'],
                color_identity=['W', 'U'], card_type="Sorcery", sub_types="",
                abilities=[133260], set_id="WAR", rarity="Rare", collectible=True, set_number=223,
                mtga_id=69672)
TolsimirFriendtoWolves = Card(name="tolsimir_friend_to_wolves", pretty_name="Tolsimir, Friend to Wolves", cost=['2', 'G', 'G', 'W'],
                              color_identity=['G', 'W'], card_type="Creature", sub_types="Elf Scout",
                              abilities=[133148, 133261], set_id="WAR", rarity="Rare", collectible=True, set_number=224,
                              mtga_id=69673)
TyrantsScorn = Card(name="tyrants_scorn", pretty_name="Tyrant's Scorn", cost=['U', 'B'],
                    color_identity=['U', 'B'], card_type="Instant", sub_types="",
                    abilities=[133263], set_id="WAR", rarity="Uncommon", collectible=True, set_number=225,
                    mtga_id=69676)
WidespreadBrutality = Card(name="widespread_brutality", pretty_name="Widespread Brutality", cost=['1', 'B', 'R', 'R'],
                           color_identity=['B', 'R'], card_type="Sorcery", sub_types="",
                           abilities=[133155], set_id="WAR", rarity="Rare", collectible=True, set_number=226,
                           mtga_id=69677)
AngrathCaptainofChaos = Card(name="angrath_captain_of_chaos", pretty_name="Angrath, Captain of Chaos", cost=['2', '(B/R)', '(B/R)'],
                             color_identity=['B', 'R'], card_type="Planeswalker", sub_types="Angrath",
                             abilities=[60706, 133156], set_id="WAR", rarity="Uncommon", collectible=True, set_number=227,
                             mtga_id=69678)
AshiokDreamRender = Card(name="ashiok_dream_render", pretty_name="Ashiok, Dream Render", cost=['1', '(U/B)', '(U/B)'],
                         color_identity=['U', 'B'], card_type="Planeswalker", sub_types="Ashiok",
                         abilities=[133267, 133158], set_id="WAR", rarity="Uncommon", collectible=True, set_number=228,
                         mtga_id=69679)
DovinHandofControl = Card(name="dovin_hand_of_control", pretty_name="Dovin, Hand of Control", cost=['2', '(W/U)'],
                          color_identity=['W', 'U'], card_type="Planeswalker", sub_types="Dovin",
                          abilities=[133159, 133160], set_id="WAR", rarity="Uncommon", collectible=True, set_number=229,
                          mtga_id=69680)
HuatlitheSunsHeart = Card(name="huatli_the_suns_heart", pretty_name="Huatli, the Sun's Heart", cost=['2', '(G/W)'],
                          color_identity=['G', 'W'], card_type="Planeswalker", sub_types="Huatli",
                          abilities=[61077, 133161], set_id="WAR", rarity="Uncommon", collectible=True, set_number=230,
                          mtga_id=69681)
KayaBaneoftheDead = Card(name="kaya_bane_of_the_dead", pretty_name="Kaya, Bane of the Dead", cost=['3', '(W/B)', '(W/B)', '(W/B)'],
                         color_identity=['W', 'B'], card_type="Planeswalker", sub_types="Kaya",
                         abilities=[133274, 1326], set_id="WAR", rarity="Uncommon", collectible=True, set_number=231,
                         mtga_id=69682)
KioraBehemothBeckoner = Card(name="kiora_behemoth_beckoner", pretty_name="Kiora, Behemoth Beckoner", cost=['2', '(G/U)'],
                             color_identity=['G', 'U'], card_type="Planeswalker", sub_types="Kiora",
                             abilities=[133162, 133163], set_id="WAR", rarity="Uncommon", collectible=True, set_number=232,
                             mtga_id=69683)
NahiriStormofStone = Card(name="nahiri_storm_of_stone", pretty_name="Nahiri, Storm of Stone", cost=['2', '(R/W)', '(R/W)'],
                          color_identity=['R', 'W'], card_type="Planeswalker", sub_types="Nahiri",
                          abilities=[133164, 133165], set_id="WAR", rarity="Uncommon", collectible=True, set_number=233,
                          mtga_id=69684)
SaheeliSublimeArtificer = Card(name="saheeli_sublime_artificer", pretty_name="Saheeli, Sublime Artificer", cost=['1', '(U/R)', '(U/R)'],
                               color_identity=['U', 'R'], card_type="Planeswalker", sub_types="Saheeli",
                               abilities=[1331, 133281], set_id="WAR", rarity="Uncommon", collectible=True, set_number=234,
                               mtga_id=69685)
SamutTyrantSmasher = Card(name="samut_tyrant_smasher", pretty_name="Samut, Tyrant Smasher", cost=['2', '(R/G)', '(R/G)'],
                          color_identity=['R', 'G'], card_type="Planeswalker", sub_types="Samut",
                          abilities=[1567, 133168], set_id="WAR", rarity="Uncommon", collectible=True, set_number=235,
                          mtga_id=69686)
FiremindVessel = Card(name="firemind_vessel", pretty_name="Firemind Vessel", cost=['4'],
                      color_identity=[], card_type="Artifact", sub_types="",
                      abilities=[76735, 133172], set_id="WAR", rarity="Uncommon", collectible=True, set_number=237,
                      mtga_id=69688)
GodPharaohsStatue = Card(name="godpharaohs_statue", pretty_name="God-Pharaoh's Statue", cost=['6'],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[133206, 133174], set_id="WAR", rarity="Uncommon", collectible=True, set_number=238,
                         mtga_id=69689)
GuildGlobe = Card(name="guild_globe", pretty_name="Guild Globe", cost=['2'],
                  color_identity=[], card_type="Artifact", sub_types="",
                  abilities=[86788, 133175], set_id="WAR", rarity="Common", collectible=True, set_number=239,
                  mtga_id=69690)
IronBully = Card(name="iron_bully", pretty_name="Iron Bully", cost=['3'],
                 color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                 abilities=[142, 92425], set_id="WAR", rarity="Common", collectible=True, set_number=240,
                 mtga_id=69691)
ManaGeode = Card(name="mana_geode", pretty_name="Mana Geode", cost=['3'],
                 color_identity=[], card_type="Artifact", sub_types="",
                 abilities=[91717, 1055], set_id="WAR", rarity="Common", collectible=True, set_number=241,
                 mtga_id=69692)
Prismite = Card(name="prismite", pretty_name="Prismite", cost=['2'],
                color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                abilities=[133176], set_id="WAR", rarity="Common", collectible=True, set_number=242,
                mtga_id=69693)
SaheelisSilverwing = Card(name="saheelis_silverwing", pretty_name="Saheeli's Silverwing", cost=['4'],
                          color_identity=[], card_type="Artifact Creature", sub_types="Drake",
                          abilities=[8, 133177], set_id="WAR", rarity="Common", collectible=True, set_number=243,
                          mtga_id=69694)
EmergenceZone = Card(name="emergence_zone", pretty_name="Emergence Zone", cost=[],
                     color_identity=[], card_type="Land", sub_types="",
                     abilities=[1152, 133178], set_id="WAR", rarity="Uncommon", collectible=True, set_number=245,
                     mtga_id=69695)
GatewayPlaza = Card(name="gateway_plaza", pretty_name="Gateway Plaza", cost=[],
                    color_identity=[], card_type="Land", sub_types="Gate",
                    abilities=[76735, 3625, 1055], set_id="WAR", rarity="Common", collectible=True, set_number=246,
                    mtga_id=69696)
InterplanarBeacon = Card(name="interplanar_beacon", pretty_name="Interplanar Beacon", cost=[],
                         color_identity=[], card_type="Land", sub_types="",
                         abilities=[133297, 1152, 133180], set_id="WAR", rarity="Uncommon", collectible=True, set_number=247,
                         mtga_id=69697)
KarnsBastion = Card(name="karns_bastion", pretty_name="Karn's Bastion", cost=[],
                    color_identity=[], card_type="Land", sub_types="",
                    abilities=[1152, 9345], set_id="WAR", rarity="Rare", collectible=True, set_number=248,
                    mtga_id=69698)
MobilizedDistrict = Card(name="mobilized_district", pretty_name="Mobilized District", cost=[],
                         color_identity=[], card_type="Land", sub_types="",
                         abilities=[1152, 133181], set_id="WAR", rarity="Rare", collectible=True, set_number=249,
                         mtga_id=69699)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=250,
              mtga_id=69701)
Plains2 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=251,
               mtga_id=69702)
Plains3 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=252,
               mtga_id=69703)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=253,
              mtga_id=69704)
Island2 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=254,
               mtga_id=69705)
Island3 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=255,
               mtga_id=69706)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=256,
             mtga_id=69707)
Swamp2 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=257,
              mtga_id=69708)
Swamp3 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=258,
              mtga_id=69709)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=259,
                mtga_id=69710)
Mountain2 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=260,
                 mtga_id=69711)
Mountain3 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=261,
                 mtga_id=69712)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=262,
              mtga_id=69713)
Forest2 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=263,
               mtga_id=69714)
Forest3 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="WAR", rarity="Basic", collectible=True, set_number=264,
               mtga_id=69715)
GideontheOathsworn = Card(name="gideon_the_oathsworn", pretty_name="Gideon, the Oathsworn", cost=['4', 'W', 'W'],
                          color_identity=['W'], card_type="Planeswalker", sub_types="Gideon",
                          abilities=[133184, 133185, 133186], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=265,
                          mtga_id=69716)
DesperateLunge = Card(name="desperate_lunge", pretty_name="Desperate Lunge", cost=['1', 'W'],
                      color_identity=['W'], card_type="Instant", sub_types="",
                      abilities=[133187], set_id="WAR", rarity="Common", collectible=True, set_number=266,
                      mtga_id=69717)
GideonsBattleCry = Card(name="gideons_battle_cry", pretty_name="Gideon's Battle Cry", cost=['2', 'W', 'W'],
                        color_identity=['W'], card_type="Sorcery", sub_types="",
                        abilities=[135279], set_id="WAR", rarity="Rare", collectible=True, set_number=267,
                        mtga_id=69718)
GideonsCompany = Card(name="gideons_company", pretty_name="Gideon's Company", cost=['3', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                      abilities=[133300, 133307], set_id="WAR", rarity="Uncommon", collectible=True, set_number=268,
                      mtga_id=69719)
OrzhovGuildgate = Card(name="orzhov_guildgate", pretty_name="Orzhov Guildgate", cost=[],
                       color_identity=['W', 'B'], card_type="Land", sub_types="Gate",
                       abilities=[76735, 18472], set_id="WAR", rarity="Common", collectible=True, set_number=269,
                       mtga_id=69720)
JaceArcaneStrategist = Card(name="jace_arcane_strategist", pretty_name="Jace, Arcane Strategist", cost=['4', 'U', 'U'],
                            color_identity=['U'], card_type="Planeswalker", sub_types="Jace",
                            abilities=[133646, 1323, 133201], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=270,
                            mtga_id=69721)
GuildpactInformant = Card(name="guildpact_informant", pretty_name="Guildpact Informant", cost=['2', 'U'],
                          color_identity=['U'], card_type="Creature", sub_types="Faerie Rogue",
                          abilities=[8, 133118], set_id="WAR", rarity="Common", collectible=True, set_number=271,
                          mtga_id=69722)
JacesProjection = Card(name="jaces_projection", pretty_name="Jace's Projection", cost=['2', 'U', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Wizard Illusion",
                       abilities=[133227, 133194], set_id="WAR", rarity="Uncommon", collectible=True, set_number=272,
                       mtga_id=69723)
JacesRuse = Card(name="jaces_ruse", pretty_name="Jace's Ruse", cost=['3', 'U', 'U'],
                 color_identity=['U'], card_type="Sorcery", sub_types="",
                 abilities=[135286], set_id="WAR", rarity="Rare", collectible=True, set_number=273,
                 mtga_id=69724)
SimicGuildgate = Card(name="simic_guildgate", pretty_name="Simic Guildgate", cost=[],
                      color_identity=['G', 'U'], card_type="Land", sub_types="Gate",
                      abilities=[76735, 18504], set_id="WAR", rarity="Common", collectible=True, set_number=274,
                      mtga_id=69725)
TezzeretMasteroftheBridge = Card(name="tezzeret_master_of_the_bridge", pretty_name="Tezzeret, Master of the Bridge", cost=['4', 'U', 'B'],
                                 color_identity=['U', 'B'], card_type="Planeswalker", sub_types="Tezzeret",
                                 abilities=[133195, 133196, 133316, 1374], set_id="WAR", rarity="Mythic Rare", collectible=True, set_number=275,
                                 mtga_id=69726)
Spirit = Card(name="spirit", pretty_name="Spirit", cost=[],
              color_identity=[], card_type="Creature", sub_types="Spirit",
              abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10001,
              mtga_id=69727)
Angel = Card(name="angel", pretty_name="Angel", cost=[],
             color_identity=[], card_type="Creature", sub_types="Angel",
             abilities=[8, 15], set_id="WAR", rarity="Token", collectible=False, set_number=10002,
             mtga_id=69728)
Soldier = Card(name="soldier", pretty_name="Soldier", cost=[],
               color_identity=[], card_type="Creature", sub_types="Soldier",
               abilities=[15], set_id="WAR", rarity="Token", collectible=False, set_number=10003,
               mtga_id=69729)
Wall = Card(name="wall", pretty_name="Wall", cost=[],
            color_identity=[], card_type="Creature", sub_types="Wall",
            abilities=[2], set_id="WAR", rarity="Token", collectible=False, set_number=10004,
            mtga_id=69730)
Wizard = Card(name="wizard", pretty_name="Wizard", cost=[],
              color_identity=[], card_type="Creature", sub_types="Wizard",
              abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10005,
              mtga_id=69731)
Assassin = Card(name="assassin", pretty_name="Assassin", cost=[],
                color_identity=[], card_type="Creature", sub_types="Assassin",
                abilities=[1, 133170], set_id="WAR", rarity="Token", collectible=False, set_number=10006,
                mtga_id=69732)
Zombie = Card(name="zombie", pretty_name="Zombie", cost=[],
              color_identity=[], card_type="Creature", sub_types="Zombie",
              abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10007,
              mtga_id=69733)
ZombieWarrior = Card(name="zombie_warrior", pretty_name="Zombie Warrior", cost=[],
                     color_identity=[], card_type="Creature", sub_types="Zombie Warrior",
                     abilities=[15], set_id="WAR", rarity="Token", collectible=False, set_number=10008,
                     mtga_id=69734)
ZombieArmy = Card(name="zombie_army", pretty_name="Zombie Army", cost=[],
                  color_identity=[], card_type="Creature", sub_types="Zombie Army",
                  abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10009,
                  mtga_id=69735)
ZombieArmy2 = Card(name="zombie_army", pretty_name="Zombie Army", cost=[],
                   color_identity=[], card_type="Creature", sub_types="Zombie Army",
                   abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10010,
                   mtga_id=69736)
ZombieArmy3 = Card(name="zombie_army", pretty_name="Zombie Army", cost=[],
                   color_identity=[], card_type="Creature", sub_types="Zombie Army",
                   abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10011,
                   mtga_id=69737)
Devil = Card(name="devil", pretty_name="Devil", cost=[],
             color_identity=[], card_type="Creature", sub_types="Devil",
             abilities=[119398], set_id="WAR", rarity="Token", collectible=False, set_number=10012,
             mtga_id=69738)
Dragon = Card(name="dragon", pretty_name="Dragon", cost=[],
              color_identity=[], card_type="Creature", sub_types="Dragon",
              abilities=[8], set_id="WAR", rarity="Token", collectible=False, set_number=10013,
              mtga_id=69739)
Goblin = Card(name="goblin", pretty_name="Goblin", cost=[],
              color_identity=[], card_type="Creature", sub_types="Goblin",
              abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10014,
              mtga_id=69740)
Wolf = Card(name="wolf", pretty_name="Wolf", cost=[],
            color_identity=[], card_type="Creature", sub_types="Wolf",
            abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10015,
            mtga_id=69741)
Citizen = Card(name="citizen", pretty_name="Citizen", cost=[],
               color_identity=[], card_type="Creature", sub_types="Citizen",
               abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10016,
               mtga_id=69742)
VojaFriendtoElves = Card(name="voja_friend_to_elves", pretty_name="Voja, Friend to Elves", cost=[],
                         color_identity=[], card_type="Creature", sub_types="Wolf",
                         abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10017,
                         mtga_id=69743)
Servo = Card(name="servo", pretty_name="Servo", cost=[],
             color_identity=[], card_type="Artifact Creature", sub_types="Servo",
             abilities=[], set_id="WAR", rarity="Token", collectible=False, set_number=10018,
             mtga_id=69744)
Despark = Card(name="despark", pretty_name="Despark", cost=['W', 'B'],
               color_identity=['W', 'B'], card_type="Instant", sub_types="",
               abilities=[133152], set_id="WAR", rarity="Uncommon", collectible=True, set_number=190,
               mtga_id=69762)
InvadetheCity = Card(name="invade_the_city", pretty_name="Invade the City", cost=['1', 'U', 'R'],
                     color_identity=['U', 'R'], card_type="Sorcery", sub_types="",
                     abilities=[133119], set_id="WAR", rarity="Uncommon", collectible=True, set_number=201,
                     mtga_id=69763)
LivingTwister = Card(name="living_twister", pretty_name="Living Twister", cost=['R', 'R', 'G'],
                     color_identity=['R', 'G'], card_type="Creature", sub_types="Elemental",
                     abilities=[133150, 133151], set_id="WAR", rarity="Rare", collectible=True, set_number=203,
                     mtga_id=69764)
VraskaSwarmsEminence = Card(name="vraska_swarms_eminence", pretty_name="Vraska, Swarm's Eminence", cost=['2', '(B/G)', '(B/G)'],
                            color_identity=['B', 'G'], card_type="Planeswalker", sub_types="Vraska",
                            abilities=[133169, 133286], set_id="WAR", rarity="Uncommon", collectible=True, set_number=236,
                            mtga_id=69765)
BlastZone = Card(name="blast_zone", pretty_name="Blast Zone", cost=[],
                 color_identity=[], card_type="Land", sub_types="",
                 abilities=[89497, 1152, 133182, 133304], set_id="WAR", rarity="Rare", collectible=True, set_number=244,
                 mtga_id=69766)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
WarOfTheSpark = Set("war", cards=clsmembers)

set_ability_map = {1: 'Deathtouch',
 2: 'Defender',
 3: 'Double strike',
 6: 'First strike',
 8: 'Flying',
 9: 'Haste',
 10: 'Hexproof',
 12: 'Lifelink',
 13: 'Reach',
 14: 'Trample',
 15: 'Vigilance',
 142: 'Menace',
 178: 'Scry 1.',
 1027: 'Enchant creature',
 1055: '{oT}: Add one mana of any color.',
 1102: 'When Centaur Nurturer enters the battlefield, you gain 3 life.',
 1118: "Sarkhan's Catharsis deals 5 damage to target player or planeswalker.",
 1142: 'Counter target noncreature spell.',
 1152: '{oT}: Add {oC}.',
 1208: 'Whenever you cast a noncreature spell, put a +1/+1 counter on '
       'Spellgorger Weird.',
 1275: 'As an additional cost to cast this spell, sacrifice a creature.',
 1285: "When Tibalt's Rager dies, it deals 1 damage to any target.",
 1323: '+1: Draw a card.',
 1326: '-3: Exile target creature.',
 1331: 'Whenever you cast a noncreature spell, create a 1/1 colorless Servo '
       'artifact creature token.',
 1374: '-8: Exile the top ten cards of your library. Put all artifact cards '
       'from among them onto the battlefield.',
 1567: 'Creatures you control have haste.',
 1570: 'Enchant land',
 1691: 'Destroy target artifact or land.',
 2103: 'When Bulwark Giant enters the battlefield, you gain 5 life.',
 2200: 'Heartfire deals 4 damage to any target.',
 2655: 'You have hexproof.',
 3251: 'Scry 4, then draw two cards.',
 3625: 'When Gateway Plaza enters the battlefield, sacrifice it unless you pay '
       '{o1}.',
 6363: 'Each opponent can cast spells only any time they could cast a sorcery.',
 6374: 'Counter target spell unless its controller pays {o2}.',
 7132: 'Creatures you control have vigilance.',
 8760: '{o1oU}, {oT}: Draw a card, then discard a card.',
 9345: '{o4}, {oT}: Proliferate.',
 14523: 'You may look at the top card of your library any time.',
 15287: 'Each creature deals damage to itself equal to its power.',
 18314: 'Proliferate.',
 18472: '{oT}: Add {oW} or {oB}.',
 18504: '{oT}: Add {oG} or {oU}.',
 18569: 'If you would draw a card while your library has no cards in it, you '
        'win the game instead.',
 18850: 'Creatures you control get +1/+0.',
 18929: 'Target player discards two cards and loses 2 life.',
 19475: 'Destroy target creature or planeswalker.',
 20451: "Your opponents can't gain life.",
 20474: 'You may cast creature spells as though they had flash.',
 21849: 'Target creature gets +1/+0 until end of turn.',
 24733: 'Target creature gets +3/+3 until end of turn.',
 25848: 'Draw a card.',
 60706: 'Creatures you control have menace.',
 61077: 'Each creature you control assigns combat damage equal to its '
        'toughness rather than its power.',
 61119: 'Enchanted land has "{oT}: Add two mana of any one color."',
 62019: 'If another red source you control would deal damage to a permanent or '
        'player, it deals that much damage plus 1 to that permanent or player '
        'instead.',
 76418: "Raging Kronch can't attack alone.",
 76556: 'Crew 1',
 76611: 'Crew 4',
 76645: 'Crew 2',
 76735: 'Simic Guildgate enters the battlefield tapped.',
 76843: "{o1oR}: Tibalt's Rager gets +2/+0 until end of turn.",
 76885: "Ugin's Conjurant enters the battlefield with X +1/+1 counters on it.",
 86788: 'When Guild Globe enters the battlefield, draw a card.',
 86929: "Sorin's Thirst deals 2 damage to target creature and you gain 2 life.",
 87008: 'When Goblin Assault Team dies, put a +1/+1 counter on target creature '
        'you control.',
 87929: 'As an additional cost to cast this spell, discard a card.',
 87941: "Arlinn's Wolf can't be blocked by creatures with power 2 or less.",
 88037: 'When Cyclops Electromancer enters the battlefield, it deals X damage '
        'to target creature an opponent controls, where X is the number of '
        'instant and sorcery cards in your graveyard.',
 88067: '{o1}: Shriekdiver gains haste until end of turn.',
 88159: 'When Tithebearer Giant enters the battlefield, you draw a card and '
        'you lose 1 life.',
 88224: 'Whenever an opponent draws a card, Ob Nixilis, the Hate-Twisted deals '
        '1 damage to that player.',
 89260: 'Exile Deliver Unto Evil.',
 89497: 'Blast Zone enters the battlefield with a charge counter on it.',
 90088: "Chandra's Pyrohelix deals 2 damage divided as you choose among one or "
        'two targets.',
 91717: 'When Mana Geode enters the battlefield, scry 1.',
 92425: 'When Iron Bully enters the battlefield, put a +1/+1 counter on target '
        'creature.',
 92664: "Duskmantle Operative can't be blocked by creatures with power 4 or "
        'greater.',
 92970: "Whenever you gain life, put a +1/+1 counter on Ajani's Pridemate.",
 93029: '-2: When you cast your next instant or sorcery spell this turn, copy '
        'that spell. You may choose new targets for the copy.',
 93170: 'When Martyr for the Cause dies, proliferate.',
 94618: "Return target nonland permanent to its owner's hand.",
 99758: "Put target nonland permanent on top of its owner's library.",
 99877: 'When Augur of Bolas enters the battlefield, look at the top three '
        'cards of your library. You may reveal an instant or sorcery card from '
        'among them and put it into your hand. Put the rest on the bottom of '
        'your library in any order.',
 100370: 'Divine Arrow deals 4 damage to target attacking or blocking '
         'creature.',
 101312: '-2: Put a +1/+1 counter on each creature you control and a loyalty '
         'counter on each other planeswalker you control.',
 101422: 'Whenever Snarespinner blocks a creature with flying, Snarespinner '
         'gets +2/+0 until end of turn.',
 101825: 'When Merfolk Skydiver enters the battlefield, put a +1/+1 counter on '
         'target creature you control.',
 102136: "Paradise Druid has hexproof as long as it's untapped.",
 117067: 'Target opponent reveals their hand. You choose a nonland card from '
         'it. That player discards that card.',
 119252: "{o3oR}: Target creature can't block this turn.",
 119398: 'When this creature dies, it deals 1 damage to any target.',
 120287: "This spell can't be countered.",
 121386: 'Whenever Trusted Pegasus attacks, target attacking creature without '
         'flying gains flying until end of turn.',
 121419: "As long as it's your turn, Ahn-Crop Invader has first strike.",
 133046: 'Prevent all damage that would be dealt to Gideon Blackblade during '
         'your turn.',
 133047: 'Untap all creatures you control. Creatures you control with flying '
         'get +2/+2 until end of turn.',
 133049: 'Whenever another creature or planeswalker you control dies, put a '
         '+1/+1 counter on Rising Populace.',
 133050: '-6: Exile target nonland permanent.',
 133051: '-4: Each player sacrifices two creatures.',
 133052: '-9: Each opponent chooses a permanent they control of each permanent '
         'type and sacrifices the rest.',
 133053: 'Each opponent sacrifices a creature. If you control a Liliana '
         'planeswalker, each opponent also discards a card.',
 133054: 'When Massacre Girl enters the battlefield, each other creature gets '
         '-1/-1 until end of turn. Whenever a creature dies this turn, each '
         'creature other than Massacre Girl gets -1/-1 until end of turn.',
 133055: '-2: Destroy target creature. Its controller draws two cards.',
 133056: 'Target creature gets -5/-5 until end of turn. If that creature would '
         'die this turn, exile it instead.',
 133057: 'Remove up to five counters from target artifact, creature, '
         'planeswalker, or opponent.',
 133058: 'Exile all multicolored permanents.',
 133059: 'As an additional cost to cast this spell, sacrifice a creature or '
         'pay {o3oB}.',
 133060: '{o3}, Sacrifice a creature or planeswalker: You gain 1 life and draw '
         'a card.',
 133061: 'Target creature gets +2/+0 and gains indestructible until end of '
         'turn.',
 133063: '-2: Create a 0/3 white Wall creature token with defender.',
 133064: 'Whenever Dreadhorde Arcanist attacks, you may cast target instant or '
         'sorcery card with converted mana cost less than or equal to '
         "Dreadhorde Arcanist's power from your graveyard without paying its "
         'mana cost. If that card would be put into your graveyard this turn, '
         'exile it instead.',
 133065: 'Zombie tokens you control have trample.',
 133066: 'Target opponent sacrifices a creature that attacked or blocked this '
         'turn. If you control a Gideon planeswalker, that player sacrifices '
         'two of those creatures instead.',
 133067: 'Up to two target creatures you control each deal damage equal to '
         'their power to another target creature.',
 133068: 'Look at the top three cards of your library. You may reveal a '
         'permanent card from among them and put it into your hand. Put the '
         'rest on the bottom of your library in any order. You gain 3 life.',
 133069: "Each creature you control with power 4 or greater can't be blocked "
         'by more than one creature.',
 133070: '-2: Exile target creature with power 4 or greater.',
 133071: 'Whenever a land enters the battlefield under your control, '
         'proliferate.',
 133073: "Put target creature with flying on the bottom of its owner's "
         'library.',
 133074: 'When God-Eternal Rhonas enters the battlefield, double the power of '
         'each other creature you control until end of turn. Those creatures '
         'gain vigilance until end of turn.',
 133075: 'Exile target creature, then proliferate.',
 133076: 'Whenever you cast a creature spell, create a 4/4 black Zombie '
         'Warrior creature token with vigilance.',
 133077: 'Whenever a creature with power 4 or greater enters the battlefield '
         'under your control, put a +1/+1 counter on Kronch Wrangler.',
 133078: 'If one or more +1/+1 counters would be put on Mowu, Loyal Companion, '
         'that many plus one +1/+1 counters are put on it instead.',
 133079: '{o5oW}, {oT}: Other creatures you control get +1/+1 until end of '
         'turn.',
 133080: 'Whenever you tap a Forest for mana, add an additional {oG}.',
 133081: '+1: Put three +1/+1 counters on up to one target noncreature land '
         'you control. Untap it. It becomes a 0/0 Elemental creature with '
         "vigilance and haste that's still a land.",
 133083: '-8: You get an emblem with "Lands you control have indestructible." '
         'Search your library for any number of Forest cards, put them onto '
         'the battlefield tapped, then shuffle your library.',
 133084: 'Search your library for up to two basic Forest cards. If you control '
         'a Nissa planeswalker, instead search your library for up to three '
         'land cards. Reveal those cards, put them into your hand, then '
         'shuffle your library.',
 133085: "{o3oU}: Ashiok's Skulker can't be blocked this turn.",
 133092: 'When Gleaming Overseer enters the battlefield, amass 1.',
 133093: 'Untap target creature. It gets +1/+4 and gains reach until end of '
         'turn.',
 133095: 'Until end of turn, creatures you control get +2/+2 and gain '
         '"Whenever this creature deals combat damage to a player or '
         'planeswalker, destroy target artifact or enchantment defending '
         'player controls."',
 133096: 'When Thundering Ceratok enters the battlefield, other creatures you '
         'control gain trample until end of turn.',
 133097: 'Each player puts the top four cards of their library into their '
         'graveyard. Return up to two instant and/or sorcery cards from your '
         'graveyard to your hand. Exile Bond of Insight.',
 133098: 'When God-Eternal Rhonas dies or is put into exile from the '
         "battlefield, you may put it into its owner's library third from the "
         'top.',
 133099: 'When Pollenbright Druid enters the battlefield, choose one   Put a '
         '+1/+1 counter on target creature.  Proliferate.',
 133100: '{oX}, {oT}, Discard a card: Look at the top X cards of your library. '
         'You may put a creature card with converted mana cost X or less from '
         'among them onto the battlefield. Put the rest on the bottom of your '
         'library in a random order.',
 133101: "{o3oG}: Look at the top card of your library. If it's a creature or "
         'planeswalker card, you may reveal it and put it into your hand. If '
         "you don't put the card into your hand, put it on the bottom of your "
         'library.',
 133104: 'Choose one   Target player sacrifices an artifact.  Target player '
         'sacrifices a creature.  Target player sacrifices a planeswalker.',
 133105: 'Amass 1.',
 133106: 'Whenever one or more loyalty counters are put on planeswalkers you '
         'control, put that many +1/+1 counters on Bioessence Hydra.',
 133107: 'Choose one or more   Destroy target artifact.  Destroy target '
         'creature.  Destroy target enchantment.  Destroy target land.  '
         'Destroy target planeswalker.',
 133108: 'Destroy target creature. Search your library for a basic land card, '
         'put it onto the battlefield tapped, then shuffle your library.',
 133109: "+1: Add {oR} or {oG}. Creature spells you cast this turn can't be "
         'countered.',
 133110: "-2: Target creature you control fights target creature you don't "
         'control.',
 133111: 'Put a +1/+1 counter on target creature you control. Then that '
         'creature deals damage equal to its power to target creature or '
         "planeswalker you don't control.",
 133112: 'Draw two cards, then amass X, where X is the number of cards in your '
         'hand.',
 133113: 'Whenever Dreadhorde Butcher deals combat damage to a player or '
         'planeswalker, put a +1/+1 counter on Dreadhorde Butcher.',
 133114: 'Choose one   Destroy target artifact.  Destroy target enchantment.  '
         'Exile target card from a graveyard.',
 133115: 'When Elite Guardmage enters the battlefield, you gain 3 life and '
         'draw a card.',
 133116: 'Enter the God-Eternals deals 4 damage to target creature and you '
         'gain life equal to the damage dealt this way. Target player puts the '
         'top four cards of their library into their graveyard. Amass 4.',
 133117: 'Whenever you cast an instant or sorcery spell that targets a '
         'creature you control, exile that card instead of putting it into '
         'your graveyard as it resolves. If you do, return it to your hand at '
         'the beginning of the next end step.',
 133118: 'Whenever Guildpact Informant deals combat damage to a player or '
         'planeswalker, proliferate.',
 133119: 'Amass X, where X is the number of instant and sorcery cards in your '
         'graveyard.',
 133120: 'Whenever a player sacrifices a permanent, Mayhem Devil deals 1 '
         'damage to any target.',
 133121: '{o3oGoU}: Proliferate.',
 133122: 'Nicol Bolas, Dragon-God has all loyalty abilities of all other '
         'planeswalkers on the battlefield.',
 133123: '+1: You draw a card. Each opponent exiles a card from their hand or '
         'a permanent they control.',
 133124: '-3: Destroy target creature or planeswalker.',
 133125: "-8: Each opponent who doesn't control a legendary creature or "
         'planeswalker loses the game.',
 133126: 'When Niv-Mizzet Reborn enters the battlefield, reveal the top ten '
         "cards of your library. For each color pair, choose a card that's "
         'exactly those colors from among them. Put the chosen cards into your '
         'hand and the rest on the bottom of your library in a random order.',
 133127: 'Amass 2.',
 133129: 'Put a +1/+1 counter on each creature you control. You gain 1 life '
         'for each creature you control.',
 133130: 'Whenever you cast or copy an instant or sorcery spell, Ral, Storm '
         'Conduit deals 1 damage to target opponent or planeswalker.',
 133131: '+2: Scry 1.',
 133132: 'When Roalesk, Apex Hybrid enters the battlefield, put two +1/+1 '
         'counters on another target creature you control.',
 133133: 'When Arboreal Grazer enters the battlefield, you may put a land card '
         'from your hand onto the battlefield tapped.',
 133134: 'Exchange control of two target permanents that share a permanent '
         'type.',
 133135: 'Whenever Rubblebelt Rioters attacks, it gets +X/+0 until end of '
         'turn, where X is the greatest power among creatures you control.',
 133136: 'When Invading Manticore enters the battlefield, amass 2.',
 133137: '+2: Sorin, Vengeful Bloodlord deals 1 damage to target player or '
         'planeswalker.',
 133138: '-X: Return target creature card with converted mana cost X from your '
         'graveyard to the battlefield. That creature is a Vampire in addition '
         'to its other types.',
 133139: '{oT}, Remove a counter from an artifact, creature, land, or '
         'planeswalker you control: Draw a card.',
 133140: 'Whenever Storrev, Devkarin Lich deals combat damage to a player or '
         'planeswalker, return to your hand target creature or planeswalker '
         "card in your graveyard that wasn't put there this combat.",
 133141: "Spells and abilities your opponents control can't cause you to "
         'discard cards or sacrifice permanents.',
 133142: 'Zombie tokens you control have flying.',
 133143: 'Search your library for up to two planeswalker cards, reveal them, '
         'put them into your hand, then shuffle your library.',
 133144: '+1: Until your next turn, you may cast sorcery spells as though they '
         'had flash.',
 133145: '-3: Return up to one target artifact, creature, or enchantment to '
         "its owner's hand. Draw a card.",
 133146: 'Whenever you cast a spell that targets Tenth District Legionnaire, '
         'put a +1/+1 counter on Tenth District Legionnaire, then scry 1.',
 133147: 'When Fblthp, the Lost enters the battlefield, draw a card. If it '
         'entered from your library or was cast from your library, draw two '
         'cards instead.',
 133148: 'When Tolsimir, Friend to Wolves enters the battlefield, create Voja, '
         'Friend to Elves, a legendary 3/3 green and white Wolf creature '
         'token.',
 133149: '+1: Until your next turn, up to one target creature gains vigilance '
         'and reach.',
 133150: '{o1oR}, Discard a land card: Living Twister deals 2 damage to any '
         'target.',
 133151: "{oG}: Return a tapped land you control to its owner's hand.",
 133152: 'Exile target permanent with converted mana cost 4 or greater.',
 133153: 'When Fblthp becomes the target of a spell, shuffle Fblthp into its '
         "owner's library.",
 133154: '-2: Look at the top three cards of your library. Exile one face down '
         'and put the rest on the bottom of your library in any order. For as '
         'long as it remains exiled, you may look at that card and you may '
         "cast it if it's a creature card.",
 133155: 'Amass 2, then the Army you amassed deals damage equal to its power '
         'to each non-Army creature.',
 133156: '-2: Amass 2.',
 133158: '-1: Target player puts the top four cards of their library into '
         "their graveyard. Then exile each opponent's graveyard.",
 133159: 'Artifact, instant, and sorcery spells your opponents cast cost {o1} '
         'more to cast.',
 133160: '-1: Until your next turn, prevent all damage that would be dealt to '
         'and dealt by target permanent an opponent controls.',
 133161: '-3: You gain life equal to the greatest toughness among creatures '
         'you control.',
 133162: 'Whenever a creature with power 4 or greater enters the battlefield '
         'under your control, draw a card.',
 133163: '-1: Untap target permanent.',
 133164: "As long as it's your turn, creatures you control have first strike "
         'and equip abilities you activate cost {o1} less to activate.',
 133165: '-X: Nahiri, Storm of Stone deals X damage to target tapped creature.',
 133166: 'Whenever you cast a noncreature spell, proliferate.',
 133167: '{o1}, {oT}: Tap target creature with converted mana cost 2 or '
         'greater.',
 133168: '-1: Target creature gets +2/+1 and gains haste until end of turn. '
         'Scry 1.',
 133169: 'Whenever a creature you control with deathtouch deals damage to a '
         'player or planeswalker, put a +1/+1 counter on that creature.',
 133170: 'Whenever this creature deals damage to a planeswalker, destroy that '
         'planeswalker.',
 133171: 'You may reveal the first card you draw each turn as you draw it. '
         'Whenever you reveal an instant or sorcery card this way, copy that '
         'card and you may cast the copy. That copy costs {o2} less to cast.',
 133172: '{oT}: Add two mana of different colors.',
 133173: '+1: You gain 3 life.',
 133174: 'At the beginning of your end step, each opponent loses 1 life.',
 133175: '{o2}, {oT}, Sacrifice Guild Globe: Add two mana of different colors.',
 133176: '{o2}: Add one mana of any color.',
 133177: "When Saheeli's Silverwing enters the battlefield, look at the top "
         "card of target opponent's library.",
 133178: '{o1}, {oT}, Sacrifice Emergence Zone: You may cast spells this turn '
         'as though they had flash.',
 133179: '+1: Target player puts the top two cards of their library into their '
         'graveyard. Draw a card.',
 133180: '{o1}, {oT}: Add two mana of different colors. Spend this mana only '
         'to cast planeswalker spells.',
 133181: '{o4}: Mobilized District becomes a 3/3 Citizen creature with '
         "vigilance until end of turn. It's still a land. This ability costs "
         '{o1} less to activate for each legendary creature and planeswalker '
         'you control.',
 133182: '{oXoX}, {oT}: Put X charge counters on Blast Zone.',
 133183: '-8: Draw seven cards. Then if your library has no cards in it, you '
         'win the game.',
 133184: 'Whenever you attack with two or more non-Gideon creatures, put a '
         '+1/+1 counter on each of those creatures.',
 133185: '+2: Until end of turn, Gideon, the Oathsworn becomes a 5/5 white '
         "Soldier creature that's still a planeswalker. Prevent all damage "
         'that would be dealt to him this turn.',
 133186: '-9: Exile Gideon, the Oathsworn and each creature your opponents '
         'control.',
 133187: 'Target creature gets +2/+2 and gains flying until end of turn. You '
         'gain 2 life.',
 133189: 'Draw two cards. If you control a Jace planeswalker, draw three cards '
         'instead.',
 133190: 'When Loxodon Sergeant enters the battlefield, other creatures you '
         'control gain vigilance until end of turn.',
 133193: 'Spells your opponents cast that target a creature or planeswalker '
         'you control cost {o2} more to cast.',
 133194: '{o3oU}: Put a loyalty counter on target Jace planeswalker.',
 133195: 'Creature and planeswalker spells you cast have affinity for '
         'artifacts.',
 133196: '+2: Tezzeret, Master of the Bridge deals X damage to each opponent, '
         'where X is the number of artifacts you control. You gain X life.',
 133197: '-2: Create a 2/2 blue Wizard creature token. Draw a card, then '
         'discard a card.',
 133198: 'Bioessence Hydra enters the battlefield with a +1/+1 counter on it '
         'for each loyalty counter on planeswalkers you control.',
 133199: 'Put a +1/+1 counter on target creature, then proliferate.',
 133200: 'Enchanted creature loses all abilities and has base power and '
         'toughness 1/1.',
 133201: "-7: Creatures you control can't be blocked this turn.",
 133202: "When Huatli's Raptor enters the battlefield, proliferate.",
 133203: 'Whenever Makeshift Battalion and at least two other creatures '
         'attack, put a +1/+1 counter on Makeshift Battalion.',
 133204: 'You and permanents you control gain hexproof until end of turn.',
 133205: "Each opponent can't draw more than one card each turn.",
 133206: 'Spells your opponents cast cost {o2} more to cast.',
 133207: '-2: Look at the top four cards of your library. You may reveal a '
         'noncreature, nonland card from among them and put it into your hand. '
         'Put the rest on the bottom of your library in a random order.',
 133208: 'Whenever Cruel Celebrant or another creature or planeswalker you '
         'control dies, each opponent loses 1 life and you gain 1 life.',
 133209: "Copy target instant or sorcery spell, then return it to its owner's "
         'hand. You may choose new targets for the copy.',
 133211: 'Amass 3.',
 133212: 'As Rescuer Sphinx enters the battlefield, you may return a nonland '
         "permanent you control to its owner's hand. If you do, Rescuer Sphinx "
         'enters the battlefield with a +1/+1 counter on it.',
 133213: 'Whenever Silent Submersible deals combat damage to a player or '
         'planeswalker, draw a card.',
 133214: "Each creature you control that's a Wolf or a Werewolf enters the "
         'battlefield with an additional +1/+1 counter on it.',
 133215: 'Whenever you cast a noncreature spell, Sky Theater Strix gets +1/+0 '
         'until end of turn.',
 133216: 'Whenever Parhelion II attacks, create two 4/4 white Angel creature '
         'tokens with flying and vigilance that are attacking.',
 133217: 'You may have Spark Double enter the battlefield as a copy of a '
         'creature or planeswalker you control, except it enters with an '
         "additional +1/+1 counter on it if it's a creature, it enters with an "
         "additional loyalty counter on it if it's a planeswalker, and it "
         "isn't legendary if that permanent is legendary.",
 133218: 'When Dreadhorde Butcher dies, it deals damage equal to its power to '
         'any target.',
 133219: '{o2}, {oT}, Sacrifice Spellkeeper Weird: Return target instant or '
         'sorcery card from your graveyard to your hand.',
 133220: 'Put two +1/+1 counters on target creature you control. That creature '
         "can't be blocked this turn.",
 133221: 'Exile target permanent you control. Return that card to the '
         "battlefield under its owner's control at the beginning of the next "
         'end step. If it enters the battlefield as a creature, it enters with '
         'an additional +1/+1 counter on it.',
 133222: 'Zombie tokens you control have hexproof and menace.',
 133223: 'Whenever you cast your second spell each turn, put a +1/+1 counter '
         'on Thunder Drake.',
 133224: 'Discard all the cards in your hand, then draw that many cards plus '
         'one. You gain life equal to the number of cards in your hand.',
 133226: 'Choose one or both   Return target creature card from your graveyard '
         'to your hand.  Return target planeswalker card from your graveyard '
         'to your hand.',
 133227: "Whenever you draw a card, put a +1/+1 counter on Jace's Projection.",
 133228: 'Up to one target creature gets -2/-2 until end of turn. Amass 2.',
 133229: 'Search your library for a creature card with converted mana cost '
         "equal to 1 plus the sacrificed creature's converted mana cost, put "
         'that card onto the battlefield with an additional +1/+1 counter on '
         'it, then shuffle your library.',
 133230: 'You may play the top card of your library. If you cast a spell this '
         'way, pay life equal to its converted mana cost rather than pay its '
         'mana cost.',
 133231: '{oT}, Sacrifice ten nonland permanents: Each opponent loses 10 life.',
 133233: 'When Prison Realm enters the battlefield, exile target creature or '
         'planeswalker an opponent controls until Prison Realm leaves the '
         'battlefield.',
 133234: 'Choose any number of target creature and/or planeswalker cards in '
         'graveyards. Command the Dreadhorde deals damage to you equal to the '
         'total converted mana cost of those cards. Put them onto the '
         'battlefield under your control.',
 133235: "At the beginning of each opponent's upkeep, if that player has one "
         'or fewer cards in hand, Davriel, Rogue Shadowmage deals 2 damage to '
         'them.',
 133236: 'When Oath of Kaya enters the battlefield, it deals 3 damage to any '
         'target and you gain 3 life.',
 133237: 'Each creature you control with a +1/+1 counter on it has "{oT}: Add '
         'one mana of any color."',
 133238: '-1: Target player discards a card.',
 133239: 'Choose up to four target cards in your graveyard. If you control a '
         'Bolas planeswalker, return those cards to your hand. Otherwise, an '
         'opponent chooses two of them. Leave the chosen cards in your '
         'graveyard and put the rest into your hand.',
 133241: 'Whenever a Zombie token you control with power 6 or greater attacks, '
         'it gains lifelink until end of turn.',
 133242: '-1: Put a +1/+1 counter on target creature.',
 133243: '{o2oB}, Sacrifice another creature or planeswalker: Put two +1/+1 '
         'counters on Dreadmalkin.',
 133244: '-2: Create a 2/2 green Wolf creature token.',
 133248: 'Whenever Eternal Taskmaster attacks, you may pay {o2oB}. If you do, '
         'return target creature card from your graveyard to your hand.',
 133249: 'Destroy up to three target creatures with toughness X or less. If X '
         'is 10 or more, return all creature cards from your graveyard to the '
         'battlefield.',
 133250: 'When God-Eternal Bontu enters the battlefield, sacrifice any number '
         'of other permanents, then draw that many cards.',
 133251: "As long as it's your turn, creatures and planeswalkers you control "
         'have lifelink.',
 133252: 'When Herald of the Dreadhorde dies, amass 2.',
 133253: 'Enchant creature or planeswalker you control',
 133254: 'When enchanted permanent dies or is put into exile, return that card '
         'to the battlefield under your control.',
 133255: 'Whenever a creature you control dies, draw a card.',
 133256: '+1: Create a 2/2 black Zombie creature token.',
 133257: '+1: Choose a nonland card name, then reveal the top four cards of '
         'your library. Put all cards with the chosen name from among them '
         'into your hand and the rest into your graveyard.',
 133258: '-3: Return target card from your graveyard to your hand.',
 133259: 'Each player chooses a creature or planeswalker they control, then '
         "sacrifices the rest. Players can't cast creature or planeswalker "
         'spells until the end of your next turn.',
 133260: "Return a creature you control to its owner's hand, then destroy all "
         'creatures.',
 133261: 'Whenever a Wolf enters the battlefield under your control, you gain '
         "3 life and that creature fights up to one target creature you don't "
         'control.',
 133263: 'Choose one   Destroy target creature with converted mana cost 3 or '
         "less.  Return target creature to its owner's hand.",
 133264: '{o6oB}: Each opponent loses 2 life and you gain 2 life.',
 133265: 'Zombie tokens you control have deathtouch.',
 133266: "When Vraska's Finisher enters the battlefield, destroy target "
         'creature or planeswalker an opponent controls that was dealt damage '
         'this turn.',
 133267: "Spells and abilities your opponents control can't cause their "
         'controller to search their library.',
 133268: '{o1}, Sacrifice another creature: Ahn-Crop Invader gets +2/+0 until '
         'end of turn.',
 133269: "Blindblast deals 1 damage to target creature. That creature can't "
         'block this turn.',
 133270: 'This spell costs {o3} less to cast if you control a creature with '
         'power 4 or greater.',
 133271: 'Change the target of target spell or ability with a single target.',
 133272: 'Gain control of target creature until end of turn. Untap that '
         'creature. It gains haste until end of turn. Bond of Passion deals 2 '
         'damage to any other target.',
 133273: 'Whenever you cast a noncreature spell, Burning Prophet gets +1/+0 '
         'until end of turn, then scry 1.',
 133274: 'Your opponents and permanents your opponents control with hexproof '
         'can be the targets of spells and abilities you control as though '
         "they didn't have hexproof.",
 133276: '+1: Exile the top card of your library. You may play it this turn.',
 133279: "Your opponents can't play land cards from graveyards.",
 133281: '-2: Target artifact you control becomes a copy of another target '
         "artifact or creature you control until end of turn, except it's an "
         'artifact in addition to its other types.',
 133282: "Ral's Outburst deals 3 damage to any target. Look at the top two "
         'cards of your library. Put one of them into your hand and the other '
         'into your graveyard.',
 133284: "Tap target permanent. If it's an artifact, destroy it.",
 133286: '-2: Create a 1/1 black Assassin creature token with deathtouch and '
         '"Whenever this creature deals damage to a planeswalker, destroy that '
         'planeswalker."',
 133287: 'When Grim Initiate dies, amass 1.',
 133288: 'Put nine +1/+1 counters on target land you control. It becomes a '
         "legendary 0/0 Elemental creature with haste named Vitu-Ghazi. It's "
         'still a land.',
 133289: 'As an additional cost to cast this spell, sacrifice a creature or '
         'planeswalker.',
 133290: 'Draw two cards. Amass 1.',
 133291: 'Whenever Ilharg, the Raze-Boar attacks, you may put a creature card '
         'from your hand onto the battlefield tapped and attacking. Return '
         'that creature to your hand at the beginning of the next end step.',
 133292: '-2: Jaya, Venerated Firemage deals 2 damage to any target.',
 133293: 'Prevent all noncombat damage that would be dealt to you and other '
         'permanents you control.',
 133294: "Jaya's Greeting deals 3 damage to target creature. Scry 1.",
 133295: 'Whenever Krenko, Tin Street Kingpin attacks, put a +1/+1 counter on '
         'it, then create a number of 1/1 red Goblin creature tokens equal to '
         "Krenko's power.",
 133296: 'Whenever you cast a noncreature spell, Mizzium Tank becomes an '
         'artifact creature and gets +1/+1 until end of turn.',
 133297: 'Whenever you cast a planeswalker spell, you gain 1 life.',
 133298: 'Colorless spells you cast cost {o2} less to cast.',
 133299: 'Up to two target creatures each get +2/+0 until end of turn.',
 133300: "Whenever you gain life, put two +1/+1 counters on Gideon's Company.",
 133301: 'Whenever Neheb, Dreadhorde Champion deals combat damage to a player '
         'or planeswalker, you may discard any number of cards. If you do, '
         'draw that many cards and add that much {oR}. Until end of turn, you '
         "don't lose this mana as steps and phases end.",
 133302: 'Target creature gets +2/+1 and gains haste until end of turn. Scry '
         '1.',
 133303: 'Whenever a creature attacks you or a planeswalker you control, each '
         'Dragon you control deals 1 damage to that creature.',
 133304: '{o3}, {oT}, Sacrifice Blast Zone: Destroy each nonland permanent '
         'with converted mana cost equal to the number of charge counters on '
         'Blast Zone.',
 133305: '+1: Until end of turn, each planeswalker you control becomes a 4/4 '
         'red Dragon creature and gains flying.',
 133306: 'Put a +1/+1 counter on target creature. That creature gains first '
         'strike until end of turn. You gain 2 life.',
 133307: '{o3oW}: Put a loyalty counter on target Gideon planeswalker.',
 133308: '-3: Create a 4/4 red Dragon creature token with flying.',
 133309: '-2: Create a 1/1 red Devil creature token with "When this creature '
         'dies, it deals 1 damage to any target."',
 133310: "Activated abilities of artifacts your opponents control can't be "
         'activated.',
 133311: '+1: Until your next turn, up to one target noncreature artifact '
         'becomes an artifact creature with power and toughness each equal to '
         'its converted mana cost.',
 133312: '-2: You may choose an artifact card you own from outside the game or '
         'in exile, reveal that card, and put it into your hand.',
 133314: "-3: Destroy target permanent that's one or more colors.",
 133315: "If damage would be dealt to Ugin's Conjurant while it has a +1/+1 "
         'counter on it, prevent that damage and remove that many +1/+1 '
         "counters from Ugin's Conjurant.",
 133316: '-3: Return target artifact card from your graveyard to your hand.',
 133317: 'Tap all creatures your opponents control. Creatures you control gain '
         'lifelink until end of turn.',
 133318: 'When Charmed Stray enters the battlefield, put a +1/+1 counter on '
         'each other creature you control named Charmed Stray.',
 133319: 'When Turret Ogre enters the battlefield, if you control another '
         'creature with power 4 or greater, Turret Ogre deals 2 damage to each '
         'opponent.',
 133320: 'Create X 2/2 white Soldier creature tokens with vigilance. If X is '
         '10 or more, also create X 4/4 white Angel creature tokens with '
         'flying and vigilance.',
 133321: "As long as it's your turn, Gideon Blackblade is a 4/4 Human Soldier "
         "creature with indestructible that's still a planeswalker.",
 133336: 'Choose a creature or planeswalker you control. All damage that would '
         'be dealt this turn to you and permanents you control is dealt to the '
         "chosen permanent instead <i>(if it's still on the battlefield)</i>.",
 133337: 'As Devouring Hellion enters the battlefield, you may sacrifice any '
         'number of creatures and/or planeswalkers. If you do, it enters with '
         'twice that many +1/+1 counters on it.',
 133339: 'Whenever an opponent attacks a planeswalker you control with one or '
         'more creatures, Oath of Kaya deals 2 damage to that player and you '
         'gain 2 life.',
 133340: 'Draw X cards. If X is 10 or more, instead shuffle your graveyard '
         'into your library, draw X cards, untap up to five lands, and you '
         'have no maximum hand size for the rest of the game.',
 133344: '+1: Up to one other target creature you control gains your choice of '
         'vigilance, lifelink, or indestructible until end of turn.',
 133345: 'Counter target creature or planeswalker spell. If that spell is '
         "countered this way, exile it instead of putting it into its owner's "
         'graveyard.',
 133347: 'Return target creature card from your graveyard to the battlefield. '
         'It gains haste until your next turn.',
 133348: 'At the beginning of your upkeep, you lose 1 life and amass 1.',
 133349: 'When Roalesk dies, proliferate, then proliferate again.',
 133350: 'Destroy any number of target planeswalkers. Choose a planeswalker '
         'you control. Put two loyalty counters on it for each planeswalker '
         'destroyed this way.',
 133351: "Lands on the battlefield and land cards in graveyards can't be the "
         'targets of spells or abilities your opponents control.',
 133352: 'Whenever one or more loyalty counters are removed from Chandra, Fire '
         'Artisan, she deals that much damage to target opponent or '
         'planeswalker.',
 133353: '-7: Exile the top seven cards of your library. You may play them '
         'this turn.',
 133354: "Chandra's Triumph deals 3 damage to target creature or planeswalker "
         "an opponent controls. Chandra's Triumph deals 5 damage to that "
         'permanent instead if you control a Chandra planeswalker.',
 133355: 'You may cast up to one target instant card and/or up to one target '
         'sorcery card from your graveyard each with converted mana cost X or '
         'less without paying their mana costs. If a card cast this way would '
         'be put into your graveyard this turn, exile it instead. If X is 10 '
         'or more, copy each of those spells twice. You may choose new targets '
         'for the copies.',
 133356: '+1: Exile the top card of your library face down and look at it. '
         'Create a 2/2 colorless Spirit creature token. When that token leaves '
         'the battlefield, put the exiled card into your hand.',
 133643: 'Choose four. You may choose the same mode more than once.  Create a '
         "2/2 Citizen creature token that's all colors.  Return target "
         'permanent card from your graveyard to your hand.  Proliferate.  You '
         'gain 4 life.',
 133646: 'Whenever you draw your second card each turn, put a +1/+1 counter on '
         'target creature you control.',
 135155: 'Search your library and graveyard for a creature card with converted '
         'mana cost X or less and put it onto the battlefield, then shuffle '
         'your library. If X is 10 or more, creatures you control get +X/+X '
         'and gain haste until end of turn.',
 135279: 'Put a +1/+1 counter on each creature you control. You may search '
         'your library and graveyard for a card named Gideon, the Oathsworn, '
         'reveal it, put it into your hand, then shuffle your library.',
 135286: "Return up to two target creatures to their owner's hand. You may "
         'search your library and graveyard for a card named Jace, Arcane '
         'Strategist, reveal it, put it into your hand, then shuffle your '
         'library.'}
