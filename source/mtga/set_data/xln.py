
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


AdantoVanguard = Card(name="adanto_vanguard", pretty_name="Adanto Vanguard", cost=['1', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                      abilities=[1006, 116881], set_id="XLN", rarity="Uncommon", collectible=True, set_number=1,
                      mtga_id=65961)
AshesoftheAbhorrent = Card(name="ashes_of_the_abhorrent", pretty_name="Ashes of the Abhorrent", cost=['1', 'W'],
                           color_identity=['W'], card_type="Enchantment", sub_types="",
                           abilities=[116882, 15027], set_id="XLN", rarity="Rare", collectible=True, set_number=2,
                           mtga_id=65963)
AxisofMortality = Card(name="axis_of_mortality", pretty_name="Axis of Mortality", cost=['4', 'W', 'W'],
                       color_identity=['W'], card_type="Enchantment", sub_types="",
                       abilities=[1010], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=3,
                       mtga_id=65965)
BellowingAegisaur = Card(name="bellowing_aegisaur", pretty_name="Bellowing Aegisaur", cost=['5', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[1011], set_id="XLN", rarity="Uncommon", collectible=True, set_number=4,
                         mtga_id=65967)
BishopofRebirth = Card(name="bishop_of_rebirth", pretty_name="Bishop of Rebirth", cost=['3', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Vampire Cleric",
                       abilities=[15, 116883], set_id="XLN", rarity="Rare", collectible=True, set_number=5,
                       mtga_id=65969)
BishopsSoldier = Card(name="bishops_soldier", pretty_name="Bishop's Soldier", cost=['1', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                      abilities=[12], set_id="XLN", rarity="Common", collectible=True, set_number=6,
                      mtga_id=65971)
BrightReprisal = Card(name="bright_reprisal", pretty_name="Bright Reprisal", cost=['4', 'W'],
                      color_identity=['W'], card_type="Instant", sub_types="",
                      abilities=[4663, 25848], set_id="XLN", rarity="Uncommon", collectible=True, set_number=7,
                      mtga_id=65973)
Demystify = Card(name="demystify", pretty_name="Demystify", cost=['W'],
                 color_identity=['W'], card_type="Instant", sub_types="",
                 abilities=[23606], set_id="XLN", rarity="Common", collectible=True, set_number=8,
                 mtga_id=65975)
DuskborneSkymarcher = Card(name="duskborne_skymarcher", pretty_name="Duskborne Skymarcher", cost=['W'],
                           color_identity=['W'], card_type="Creature", sub_types="Vampire Cleric",
                           abilities=[8, 116885], set_id="XLN", rarity="Uncommon", collectible=True, set_number=9,
                           mtga_id=65977)
EmissaryofSunrise = Card(name="emissary_of_sunrise", pretty_name="Emissary of Sunrise", cost=['2', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                         abilities=[6, 116886], set_id="XLN", rarity="Uncommon", collectible=True, set_number=10,
                         mtga_id=65979)
EncampmentKeeper = Card(name="encampment_keeper", pretty_name="Encampment Keeper", cost=['W'],
                        color_identity=['W'], card_type="Creature", sub_types="Hound",
                        abilities=[6, 116887], set_id="XLN", rarity="Common", collectible=True, set_number=11,
                        mtga_id=65981)
GlorifierofDusk = Card(name="glorifier_of_dusk", pretty_name="Glorifier of Dusk", cost=['3', 'W', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                       abilities=[101377, 1020], set_id="XLN", rarity="Uncommon", collectible=True, set_number=12,
                       mtga_id=65983)
GoringCeratops = Card(name="goring_ceratops", pretty_name="Goring Ceratops", cost=['5', 'W', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                      abilities=[3, 1021], set_id="XLN", rarity="Rare", collectible=True, set_number=13,
                      mtga_id=65985)
ImperialAerosaur = Card(name="imperial_aerosaur", pretty_name="Imperial Aerosaur", cost=['3', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[8, 116888], set_id="XLN", rarity="Uncommon", collectible=True, set_number=14,
                        mtga_id=65987)
ImperialLancer = Card(name="imperial_lancer", pretty_name="Imperial Lancer", cost=['W'],
                      color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                      abilities=[116889], set_id="XLN", rarity="Uncommon", collectible=True, set_number=15,
                      mtga_id=65989)
InspiringCleric = Card(name="inspiring_cleric", pretty_name="Inspiring Cleric", cost=['2', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Vampire Cleric",
                       abilities=[88604], set_id="XLN", rarity="Uncommon", collectible=True, set_number=16,
                       mtga_id=65991)
IxalansBinding = Card(name="ixalans_binding", pretty_name="Ixalan's Binding", cost=['3', 'W'],
                      color_identity=['W'], card_type="Enchantment", sub_types="",
                      abilities=[20997, 116731], set_id="XLN", rarity="Uncommon", collectible=True, set_number=17,
                      mtga_id=65993)
KinjallisCaller = Card(name="kinjallis_caller", pretty_name="Kinjalli's Caller", cost=['W'],
                       color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                       abilities=[116730], set_id="XLN", rarity="Common", collectible=True, set_number=18,
                       mtga_id=65995)
KinjallisSunwing = Card(name="kinjallis_sunwing", pretty_name="Kinjalli's Sunwing", cost=['2', 'W'],
                        color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[8, 15979], set_id="XLN", rarity="Rare", collectible=True, set_number=19,
                        mtga_id=65997)
LegionConquistador = Card(name="legion_conquistador", pretty_name="Legion Conquistador", cost=['2', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                          abilities=[116758], set_id="XLN", rarity="Common", collectible=True, set_number=20,
                          mtga_id=65999)
LegionsJudgment = Card(name="legions_judgment", pretty_name="Legion's Judgment", cost=['2', 'W'],
                       color_identity=['W'], card_type="Sorcery", sub_types="",
                       abilities=[13402], set_id="XLN", rarity="Common", collectible=True, set_number=21,
                       mtga_id=66001)
LegionsLanding = Card(name="legions_landing", pretty_name="Legion's Landing", cost=['W'],
                      color_identity=['W'], card_type="Enchantment", sub_types="",
                      abilities=[116788, 116801], set_id="XLN", rarity="Rare", collectible=True, set_number=22,
                      mtga_id=66003)
AdantotheFirstFort = Card(name="adanto_the_first_fort", pretty_name="Adanto, the First Fort", cost=[],
                          color_identity=['W'], card_type="Land", sub_types="",
                          abilities=[1001, 116815], set_id="XLN", rarity="Rare", collectible=False, set_number=22,
                          mtga_id=66005)
LoomingAltisaur = Card(name="looming_altisaur", pretty_name="Looming Altisaur", cost=['3', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[], set_id="XLN", rarity="Common", collectible=True, set_number=23,
                       mtga_id=66007)
MavrenFeinDuskApostle = Card(name="mavren_fein_dusk_apostle", pretty_name="Mavren Fein, Dusk Apostle", cost=['2', 'W'],
                             color_identity=['W'], card_type="Creature", sub_types="Vampire Cleric",
                             abilities=[116821], set_id="XLN", rarity="Rare", collectible=True, set_number=24,
                             mtga_id=66009)
PaladinoftheBloodstained = Card(name="paladin_of_the_bloodstained", pretty_name="Paladin of the Bloodstained", cost=['3', 'W'],
                                color_identity=['W'], card_type="Creature", sub_types="Vampire Knight",
                                abilities=[116788], set_id="XLN", rarity="Common", collectible=True, set_number=25,
                                mtga_id=66011)
PiousInterdiction = Card(name="pious_interdiction", pretty_name="Pious Interdiction", cost=['3', 'W'],
                         color_identity=['W'], card_type="Enchantment", sub_types="Aura",
                         abilities=[1027, 88132, 1083], set_id="XLN", rarity="Common", collectible=True, set_number=26,
                         mtga_id=66013)
PriestoftheWakeningSun = Card(name="priest_of_the_wakening_sun", pretty_name="Priest of the Wakening Sun", cost=['W'],
                              color_identity=['W'], card_type="Creature", sub_types="Human Cleric",
                              abilities=[116840, 1040], set_id="XLN", rarity="Rare", collectible=True, set_number=27,
                              mtga_id=66015)
PterodonKnight = Card(name="pterodon_knight", pretty_name="Pterodon Knight", cost=['3', 'W'],
                      color_identity=['W'], card_type="Creature", sub_types="Human Knight",
                      abilities=[1041], set_id="XLN", rarity="Common", collectible=True, set_number=28,
                      mtga_id=66017)
QueensCommission = Card(name="queens_commission", pretty_name="Queen's Commission", cost=['2', 'W'],
                        color_identity=['W'], card_type="Sorcery", sub_types="",
                        abilities=[116729], set_id="XLN", rarity="Common", collectible=True, set_number=29,
                        mtga_id=66019)
RallyingRoar = Card(name="rallying_roar", pretty_name="Rallying Roar", cost=['2', 'W'],
                    color_identity=['W'], card_type="Instant", sub_types="",
                    abilities=[116736], set_id="XLN", rarity="Uncommon", collectible=True, set_number=30,
                    mtga_id=66021)
RaptorCompanion = Card(name="raptor_companion", pretty_name="Raptor Companion", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[], set_id="XLN", rarity="Common", collectible=True, set_number=31,
                       mtga_id=66023)
RitualofRejuvenation = Card(name="ritual_of_rejuvenation", pretty_name="Ritual of Rejuvenation", cost=['2', 'W'],
                            color_identity=['W'], card_type="Instant", sub_types="",
                            abilities=[1586, 25848], set_id="XLN", rarity="Common", collectible=True, set_number=32,
                            mtga_id=66025)
SanguineSacrament = Card(name="sanguine_sacrament", pretty_name="Sanguine Sacrament", cost=['X', 'W', 'W'],
                         color_identity=['W'], card_type="Instant", sub_types="",
                         abilities=[116857], set_id="XLN", rarity="Rare", collectible=True, set_number=33,
                         mtga_id=66027)
SettletheWreckage = Card(name="settle_the_wreckage", pretty_name="Settle the Wreckage", cost=['2', 'W', 'W'],
                         color_identity=['W'], card_type="Instant", sub_types="",
                         abilities=[1046], set_id="XLN", rarity="Rare", collectible=True, set_number=34,
                         mtga_id=66029)
ShelteringLight = Card(name="sheltering_light", pretty_name="Sheltering Light", cost=['W'],
                       color_identity=['W'], card_type="Instant", sub_types="",
                       abilities=[116742], set_id="XLN", rarity="Uncommon", collectible=True, set_number=35,
                       mtga_id=66031)
ShiningAerosaur = Card(name="shining_aerosaur", pretty_name="Shining Aerosaur", cost=['4', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[8], set_id="XLN", rarity="Common", collectible=True, set_number=36,
                       mtga_id=66033)
SkybladeoftheLegion = Card(name="skyblade_of_the_legion", pretty_name="Skyblade of the Legion", cost=['1', 'W'],
                           color_identity=['W'], card_type="Creature", sub_types="Vampire Soldier",
                           abilities=[8], set_id="XLN", rarity="Common", collectible=True, set_number=37,
                           mtga_id=66035)
SlashofTalons = Card(name="slash_of_talons", pretty_name="Slash of Talons", cost=['W'],
                     color_identity=['W'], card_type="Instant", sub_types="",
                     abilities=[99791], set_id="XLN", rarity="Common", collectible=True, set_number=38,
                     mtga_id=66037)
SteadfastArmasaur = Card(name="steadfast_armasaur", pretty_name="Steadfast Armasaur", cost=['3', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[15, 116866], set_id="XLN", rarity="Uncommon", collectible=True, set_number=39,
                         mtga_id=66039)
SunriseSeeker = Card(name="sunrise_seeker", pretty_name="Sunrise Seeker", cost=['4', 'W'],
                     color_identity=['W'], card_type="Creature", sub_types="Human Scout",
                     abilities=[15, 116886], set_id="XLN", rarity="Common", collectible=True, set_number=40,
                     mtga_id=66041)
TerritorialHammerskull = Card(name="territorial_hammerskull", pretty_name="Territorial Hammerskull", cost=['2', 'W'],
                              color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                              abilities=[116870], set_id="XLN", rarity="Common", collectible=True, set_number=41,
                              mtga_id=66043)
TocatliHonorGuard = Card(name="tocatli_honor_guard", pretty_name="Tocatli Honor Guard", cost=['1', 'W'],
                         color_identity=['W'], card_type="Creature", sub_types="Human Soldier",
                         abilities=[95397], set_id="XLN", rarity="Rare", collectible=True, set_number=42,
                         mtga_id=66045)
VampiresZeal = Card(name="vampires_zeal", pretty_name="Vampire's Zeal", cost=['W'],
                    color_identity=['W'], card_type="Instant", sub_types="",
                    abilities=[116750], set_id="XLN", rarity="Common", collectible=True, set_number=43,
                    mtga_id=66047)
WakeningSunsAvatar = Card(name="wakening_suns_avatar", pretty_name="Wakening Sun's Avatar", cost=['5', 'W', 'W', 'W'],
                          color_identity=['W'], card_type="Creature", sub_types="Dinosaur Avatar",
                          abilities=[116751], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=44,
                          mtga_id=66049)
AirElemental = Card(name="air_elemental", pretty_name="Air Elemental", cost=['3', 'U', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Elemental",
                    abilities=[8], set_id="XLN", rarity="Uncommon", collectible=True, set_number=45,
                    mtga_id=66051)
ArcaneAdaptation = Card(name="arcane_adaptation", pretty_name="Arcane Adaptation", cost=['2', 'U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="",
                        abilities=[76882, 116757], set_id="XLN", rarity="Rare", collectible=True, set_number=46,
                        mtga_id=66053)
Cancel = Card(name="cancel", pretty_name="Cancel", cost=['1', 'U', 'U'],
              color_identity=['U'], card_type="Instant", sub_types="",
              abilities=[25846], set_id="XLN", rarity="Common", collectible=True, set_number=47,
              mtga_id=66055)
ChartaCourse = Card(name="chart_a_course", pretty_name="Chart a Course", cost=['1', 'U'],
                    color_identity=['U'], card_type="Sorcery", sub_types="",
                    abilities=[1057], set_id="XLN", rarity="Uncommon", collectible=True, set_number=48,
                    mtga_id=66057)
DaringSaboteur = Card(name="daring_saboteur", pretty_name="Daring Saboteur", cost=['1', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                      abilities=[100782, 100164], set_id="XLN", rarity="Rare", collectible=True, set_number=49,
                      mtga_id=66059)
DeadeyeQuartermaster = Card(name="deadeye_quartermaster", pretty_name="Deadeye Quartermaster", cost=['3', 'U'],
                            color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                            abilities=[116768], set_id="XLN", rarity="Uncommon", collectible=True, set_number=50,
                            mtga_id=66061)
DeeprootWaters = Card(name="deeproot_waters", pretty_name="Deeproot Waters", cost=['2', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="",
                      abilities=[116773], set_id="XLN", rarity="Uncommon", collectible=True, set_number=51,
                      mtga_id=66063)
DepthsofDesire = Card(name="depths_of_desire", pretty_name="Depths of Desire", cost=['2', 'U'],
                      color_identity=['U'], card_type="Instant", sub_types="",
                      abilities=[1063], set_id="XLN", rarity="Common", collectible=True, set_number=52,
                      mtga_id=66065)
DiveDown = Card(name="dive_down", pretty_name="Dive Down", cost=['U'],
                color_identity=['U'], card_type="Instant", sub_types="",
                abilities=[61160], set_id="XLN", rarity="Common", collectible=True, set_number=53,
                mtga_id=66067)
DreamcallerSiren = Card(name="dreamcaller_siren", pretty_name="Dreamcaller Siren", cost=['2', 'U', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Siren Pirate",
                        abilities=[7, 8, 86918, 116790], set_id="XLN", rarity="Rare", collectible=True, set_number=54,
                        mtga_id=66069)
EntrancingMelody = Card(name="entrancing_melody", pretty_name="Entrancing Melody", cost=['X', 'U', 'U'],
                        color_identity=['U'], card_type="Sorcery", sub_types="",
                        abilities=[116793], set_id="XLN", rarity="Rare", collectible=True, set_number=55,
                        mtga_id=66071)
FavorableWinds = Card(name="favorable_winds", pretty_name="Favorable Winds", cost=['1', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="",
                      abilities=[2075], set_id="XLN", rarity="Uncommon", collectible=True, set_number=56,
                      mtga_id=66073)
FleetSwallower = Card(name="fleet_swallower", pretty_name="Fleet Swallower", cost=['5', 'U', 'U'],
                      color_identity=['U'], card_type="Creature", sub_types="Fish",
                      abilities=[116797], set_id="XLN", rarity="Rare", collectible=True, set_number=57,
                      mtga_id=66075)
HeadwaterSentries = Card(name="headwater_sentries", pretty_name="Headwater Sentries", cost=['3', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                         abilities=[], set_id="XLN", rarity="Common", collectible=True, set_number=58,
                         mtga_id=66077)
HeraldofSecretStreams = Card(name="herald_of_secret_streams", pretty_name="Herald of Secret Streams", cost=['3', 'U'],
                             color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                             abilities=[1070], set_id="XLN", rarity="Rare", collectible=True, set_number=59,
                             mtga_id=66079)
JaceCunningCastaway = Card(name="jace_cunning_castaway", pretty_name="Jace, Cunning Castaway", cost=['1', 'U', 'U'],
                           color_identity=['U'], card_type="Planeswalker", sub_types="Jace",
                           abilities=[1071, 1073, 116811], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=60,
                           mtga_id=66081)
KopalaWardenofWaves = Card(name="kopala_warden_of_waves", pretty_name="Kopala, Warden of Waves", cost=['1', 'U', 'U'],
                           color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                           abilities=[116812, 1076], set_id="XLN", rarity="Rare", collectible=True, set_number=61,
                           mtga_id=66083)
LookoutsDispersal = Card(name="lookouts_dispersal", pretty_name="Lookout's Dispersal", cost=['2', 'U'],
                         color_identity=['U'], card_type="Instant", sub_types="",
                         abilities=[116814, 17253], set_id="XLN", rarity="Uncommon", collectible=True, set_number=62,
                         mtga_id=66085)
NavigatorsRuin = Card(name="navigators_ruin", pretty_name="Navigator's Ruin", cost=['2', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="",
                      abilities=[120995], set_id="XLN", rarity="Uncommon", collectible=True, set_number=63,
                      mtga_id=66087)
OneWiththeWind = Card(name="one_with_the_wind", pretty_name="One With the Wind", cost=['1', 'U'],
                      color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                      abilities=[1027, 2452], set_id="XLN", rarity="Common", collectible=True, set_number=64,
                      mtga_id=66089)
Opt = Card(name="opt", pretty_name="Opt", cost=['U'],
           color_identity=['U'], card_type="Instant", sub_types="",
           abilities=[66937, 25848], set_id="XLN", rarity="Common", collectible=True, set_number=65,
           mtga_id=66091)
OverflowingInsight = Card(name="overflowing_insight", pretty_name="Overflowing Insight", cost=['4', 'U', 'U', 'U'],
                          color_identity=['U'], card_type="Sorcery", sub_types="",
                          abilities=[116816], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=66,
                          mtga_id=66093)
PerilousVoyage = Card(name="perilous_voyage", pretty_name="Perilous Voyage", cost=['1', 'U'],
                      color_identity=['U'], card_type="Instant", sub_types="",
                      abilities=[116818], set_id="XLN", rarity="Uncommon", collectible=True, set_number=67,
                      mtga_id=66095)
PiratesPrize = Card(name="pirates_prize", pretty_name="Pirate's Prize", cost=['3', 'U'],
                    color_identity=['U'], card_type="Sorcery", sub_types="",
                    abilities=[116819], set_id="XLN", rarity="Common", collectible=True, set_number=68,
                    mtga_id=66097)
ProsperousPirates = Card(name="prosperous_pirates", pretty_name="Prosperous Pirates", cost=['4', 'U'],
                         color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[116820], set_id="XLN", rarity="Common", collectible=True, set_number=69,
                         mtga_id=66099)
RiverSneak = Card(name="river_sneak", pretty_name="River Sneak", cost=['1', 'U'],
                  color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                  abilities=[62969, 116822], set_id="XLN", rarity="Uncommon", collectible=True, set_number=70,
                  mtga_id=66101)
RiversRebuke = Card(name="rivers_rebuke", pretty_name="River's Rebuke", cost=['4', 'U', 'U'],
                    color_identity=['U'], card_type="Sorcery", sub_types="",
                    abilities=[116823], set_id="XLN", rarity="Rare", collectible=True, set_number=71,
                    mtga_id=66103)
RunAground = Card(name="run_aground", pretty_name="Run Aground", cost=['3', 'U'],
                  color_identity=['U'], card_type="Instant", sub_types="",
                  abilities=[116825], set_id="XLN", rarity="Common", collectible=True, set_number=72,
                  mtga_id=66105)
SailorofMeans = Card(name="sailor_of_means", pretty_name="Sailor of Means", cost=['2', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                     abilities=[116826], set_id="XLN", rarity="Common", collectible=True, set_number=73,
                     mtga_id=66107)
SearchforAzcanta = Card(name="search_for_azcanta", pretty_name="Search for Azcanta", cost=['1', 'U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="",
                        abilities=[116827], set_id="XLN", rarity="Rare", collectible=True, set_number=74,
                        mtga_id=66109)
AzcantatheSunkenRuin = Card(name="azcanta_the_sunken_ruin", pretty_name="Azcanta, the Sunken Ruin", cost=[],
                            color_identity=['U'], card_type="Land", sub_types="",
                            abilities=[1002, 116828], set_id="XLN", rarity="Rare", collectible=False, set_number=74,
                            mtga_id=66111)
ShaperApprentice = Card(name="shaper_apprentice", pretty_name="Shaper Apprentice", cost=['1', 'U'],
                        color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                        abilities=[116829], set_id="XLN", rarity="Common", collectible=True, set_number=75,
                        mtga_id=66113)
ShipwreckLooter = Card(name="shipwreck_looter", pretty_name="Shipwreck Looter", cost=['1', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                       abilities=[116830], set_id="XLN", rarity="Common", collectible=True, set_number=76,
                       mtga_id=66115)
ShoreKeeper = Card(name="shore_keeper", pretty_name="Shore Keeper", cost=['U'],
                   color_identity=['U'], card_type="Creature", sub_types="Trilobite",
                   abilities=[116831], set_id="XLN", rarity="Common", collectible=True, set_number=77,
                   mtga_id=66117)
SirenLookout = Card(name="siren_lookout", pretty_name="Siren Lookout", cost=['2', 'U'],
                    color_identity=['U'], card_type="Creature", sub_types="Siren Pirate",
                    abilities=[8, 116886], set_id="XLN", rarity="Common", collectible=True, set_number=78,
                    mtga_id=66119)
SirenStormtamer = Card(name="siren_stormtamer", pretty_name="Siren Stormtamer", cost=['U'],
                       color_identity=['U'], card_type="Creature", sub_types="Siren Pirate Wizard",
                       abilities=[8, 116833], set_id="XLN", rarity="Uncommon", collectible=True, set_number=79,
                       mtga_id=66121)
SirensRuse = Card(name="sirens_ruse", pretty_name="Siren's Ruse", cost=['1', 'U'],
                  color_identity=['U'], card_type="Instant", sub_types="",
                  abilities=[116834], set_id="XLN", rarity="Common", collectible=True, set_number=80,
                  mtga_id=66123)
SpellPierce = Card(name="spell_pierce", pretty_name="Spell Pierce", cost=['U'],
                   color_identity=['U'], card_type="Instant", sub_types="",
                   abilities=[30062], set_id="XLN", rarity="Common", collectible=True, set_number=81,
                   mtga_id=66125)
SpellSwindle = Card(name="spell_swindle", pretty_name="Spell Swindle", cost=['3', 'U', 'U'],
                    color_identity=['U'], card_type="Instant", sub_types="",
                    abilities=[116836], set_id="XLN", rarity="Rare", collectible=True, set_number=82,
                    mtga_id=66127)
StormFleetAerialist = Card(name="storm_fleet_aerialist", pretty_name="Storm Fleet Aerialist", cost=['1', 'U'],
                           color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                           abilities=[8, 101552], set_id="XLN", rarity="Uncommon", collectible=True, set_number=83,
                           mtga_id=66129)
StormFleetSpy = Card(name="storm_fleet_spy", pretty_name="Storm Fleet Spy", cost=['2', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Human Pirate",
                     abilities=[116838], set_id="XLN", rarity="Uncommon", collectible=True, set_number=84,
                     mtga_id=66131)
StormSculptor = Card(name="storm_sculptor", pretty_name="Storm Sculptor", cost=['3', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                     abilities=[62969, 87893], set_id="XLN", rarity="Common", collectible=True, set_number=85,
                     mtga_id=66133)
TempestCaller = Card(name="tempest_caller", pretty_name="Tempest Caller", cost=['2', 'U', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                     abilities=[116839], set_id="XLN", rarity="Uncommon", collectible=True, set_number=86,
                     mtga_id=66135)
WatertrapWeaver = Card(name="watertrap_weaver", pretty_name="Watertrap Weaver", cost=['2', 'U'],
                       color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                       abilities=[76874], set_id="XLN", rarity="Common", collectible=True, set_number=87,
                       mtga_id=66137)
WindStrider = Card(name="wind_strider", pretty_name="Wind Strider", cost=['4', 'U'],
                   color_identity=['U'], card_type="Creature", sub_types="Merfolk Wizard",
                   abilities=[7, 8], set_id="XLN", rarity="Common", collectible=True, set_number=88,
                   mtga_id=66139)
AnointedDeacon = Card(name="anointed_deacon", pretty_name="Anointed Deacon", cost=['4', 'B'],
                      color_identity=['B'], card_type="Creature", sub_types="Vampire Cleric",
                      abilities=[1106], set_id="XLN", rarity="Common", collectible=True, set_number=89,
                      mtga_id=66141)
ArguelsBloodFast = Card(name="arguels_blood_fast", pretty_name="Arguel's Blood Fast", cost=['1', 'B'],
                        color_identity=['B'], card_type="Enchantment", sub_types="",
                        abilities=[20452, 116841], set_id="XLN", rarity="Rare", collectible=True, set_number=90,
                        mtga_id=66143)
TempleofAclazotz = Card(name="temple_of_aclazotz", pretty_name="Temple of Aclazotz", cost=[],
                        color_identity=['B'], card_type="Land", sub_types="",
                        abilities=[1003, 93248], set_id="XLN", rarity="Rare", collectible=False, set_number=90,
                        mtga_id=66145)
BishopoftheBloodstained = Card(name="bishop_of_the_bloodstained", pretty_name="Bishop of the Bloodstained", cost=['3', 'B', 'B'],
                               color_identity=['B'], card_type="Creature", sub_types="Vampire Cleric",
                               abilities=[116842], set_id="XLN", rarity="Uncommon", collectible=True, set_number=91,
                               mtga_id=66147)
BlightKeeper = Card(name="blight_keeper", pretty_name="Blight Keeper", cost=['B'],
                    color_identity=['B'], card_type="Creature", sub_types="Bat Imp",
                    abilities=[8, 116843], set_id="XLN", rarity="Common", collectible=True, set_number=92,
                    mtga_id=66149)
BloodcrazedPaladin = Card(name="bloodcrazed_paladin", pretty_name="Bloodcrazed Paladin", cost=['1', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Vampire Knight",
                          abilities=[7, 116844], set_id="XLN", rarity="Rare", collectible=True, set_number=93,
                          mtga_id=66151)
BoneyardParley = Card(name="boneyard_parley", pretty_name="Boneyard Parley", cost=['5', 'B', 'B'],
                      color_identity=['B'], card_type="Sorcery", sub_types="",
                      abilities=[116845], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=94,
                      mtga_id=66153)
ContractKilling = Card(name="contract_killing", pretty_name="Contract Killing", cost=['3', 'B', 'B'],
                       color_identity=['B'], card_type="Sorcery", sub_types="",
                       abilities=[116846], set_id="XLN", rarity="Common", collectible=True, set_number=95,
                       mtga_id=66155)
CostlyPlunder = Card(name="costly_plunder", pretty_name="Costly Plunder", cost=['1', 'B'],
                     color_identity=['B'], card_type="Instant", sub_types="",
                     abilities=[95354, 23607], set_id="XLN", rarity="Common", collectible=True, set_number=96,
                     mtga_id=66157)
DarkNourishment = Card(name="dark_nourishment", pretty_name="Dark Nourishment", cost=['4', 'B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[95596], set_id="XLN", rarity="Uncommon", collectible=True, set_number=97,
                       mtga_id=66159)
DeadeyeTormentor = Card(name="deadeye_tormentor", pretty_name="Deadeye Tormentor", cost=['2', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                        abilities=[101515], set_id="XLN", rarity="Common", collectible=True, set_number=98,
                        mtga_id=66161)
DeadeyeTracker = Card(name="deadeye_tracker", pretty_name="Deadeye Tracker", cost=['B'],
                      color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                      abilities=[116848], set_id="XLN", rarity="Rare", collectible=True, set_number=99,
                      mtga_id=66163)
DeathlessAncient = Card(name="deathless_ancient", pretty_name="Deathless Ancient", cost=['4', 'B', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Vampire Knight",
                        abilities=[8, 116849], set_id="XLN", rarity="Uncommon", collectible=True, set_number=100,
                        mtga_id=66165)
DesperateCastaways = Card(name="desperate_castaways", pretty_name="Desperate Castaways", cost=['1', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                          abilities=[116850], set_id="XLN", rarity="Common", collectible=True, set_number=101,
                          mtga_id=66167)
DireFleetHoarder = Card(name="dire_fleet_hoarder", pretty_name="Dire Fleet Hoarder", cost=['1', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                        abilities=[116851], set_id="XLN", rarity="Common", collectible=True, set_number=102,
                        mtga_id=66169)
DireFleetInterloper = Card(name="dire_fleet_interloper", pretty_name="Dire Fleet Interloper", cost=['3', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                           abilities=[142, 116886], set_id="XLN", rarity="Common", collectible=True, set_number=103,
                           mtga_id=66171)
DireFleetRavager = Card(name="dire_fleet_ravager", pretty_name="Dire Fleet Ravager", cost=['3', 'B', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Orc Pirate Wizard",
                        abilities=[142, 1, 116852], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=104,
                        mtga_id=66173)
Duress = Card(name="duress", pretty_name="Duress", cost=['B'],
              color_identity=['B'], card_type="Sorcery", sub_types="",
              abilities=[21775], set_id="XLN", rarity="Common", collectible=True, set_number=105,
              mtga_id=66175)
FathomFleetCaptain = Card(name="fathom_fleet_captain", pretty_name="Fathom Fleet Captain", cost=['1', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                          abilities=[142, 1126], set_id="XLN", rarity="Rare", collectible=True, set_number=106,
                          mtga_id=66177)
FathomFleetCutthroat = Card(name="fathom_fleet_cutthroat", pretty_name="Fathom Fleet Cutthroat", cost=['3', 'B'],
                            color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                            abilities=[1127], set_id="XLN", rarity="Common", collectible=True, set_number=107,
                            mtga_id=66179)
GrimCaptainsCall = Card(name="grim_captains_call", pretty_name="Grim Captain's Call", cost=['2', 'B'],
                        color_identity=['B'], card_type="Sorcery", sub_types="",
                        abilities=[116854], set_id="XLN", rarity="Uncommon", collectible=True, set_number=108,
                        mtga_id=66181)
HeartlessPillage = Card(name="heartless_pillage", pretty_name="Heartless Pillage", cost=['2', 'B'],
                        color_identity=['B'], card_type="Sorcery", sub_types="",
                        abilities=[1129], set_id="XLN", rarity="Uncommon", collectible=True, set_number=109,
                        mtga_id=66183)
KitesailFreebooter = Card(name="kitesail_freebooter", pretty_name="Kitesail Freebooter", cost=['1', 'B'],
                          color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                          abilities=[8, 1130], set_id="XLN", rarity="Uncommon", collectible=True, set_number=110,
                          mtga_id=66185)
LurkingChupacabra = Card(name="lurking_chupacabra", pretty_name="Lurking Chupacabra", cost=['3', 'B'],
                         color_identity=['B'], card_type="Creature", sub_types="Beast Horror",
                         abilities=[116732], set_id="XLN", rarity="Uncommon", collectible=True, set_number=111,
                         mtga_id=66187)
MarchoftheDrowned = Card(name="march_of_the_drowned", pretty_name="March of the Drowned", cost=['B'],
                         color_identity=['B'], card_type="Sorcery", sub_types="",
                         abilities=[116733], set_id="XLN", rarity="Common", collectible=True, set_number=112,
                         mtga_id=66189)
MarkoftheVampire = Card(name="mark_of_the_vampire", pretty_name="Mark of the Vampire", cost=['3', 'B'],
                        color_identity=['B'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 19189], set_id="XLN", rarity="Common", collectible=True, set_number=113,
                        mtga_id=66191)
QueensAgent = Card(name="queens_agent", pretty_name="Queen's Agent", cost=['5', 'B'],
                   color_identity=['B'], card_type="Creature", sub_types="Vampire Scout",
                   abilities=[12, 116886], set_id="XLN", rarity="Common", collectible=True, set_number=114,
                   mtga_id=66193)
QueensBaySoldier = Card(name="queens_bay_soldier", pretty_name="Queen's Bay Soldier", cost=['1', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                        abilities=[], set_id="XLN", rarity="Common", collectible=True, set_number=115,
                        mtga_id=66195)
RaidersWake = Card(name="raiders_wake", pretty_name="Raiders' Wake", cost=['3', 'B'],
                   color_identity=['B'], card_type="Enchantment", sub_types="",
                   abilities=[2904, 116734], set_id="XLN", rarity="Uncommon", collectible=True, set_number=116,
                   mtga_id=66197)
RevelinRiches = Card(name="revel_in_riches", pretty_name="Revel in Riches", cost=['4', 'B'],
                     color_identity=['B'], card_type="Enchantment", sub_types="",
                     abilities=[116735, 116860], set_id="XLN", rarity="Rare", collectible=True, set_number=117,
                     mtga_id=66199)
RuinRaider = Card(name="ruin_raider", pretty_name="Ruin Raider", cost=['2', 'B'],
                  color_identity=['B'], card_type="Creature", sub_types="Orc Pirate",
                  abilities=[1140], set_id="XLN", rarity="Rare", collectible=True, set_number=118,
                  mtga_id=66201)
RuthlessKnave = Card(name="ruthless_knave", pretty_name="Ruthless Knave", cost=['2', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Orc Pirate",
                     abilities=[116737, 116738], set_id="XLN", rarity="Uncommon", collectible=True, set_number=119,
                     mtga_id=66203)
SanctumSeeker = Card(name="sanctum_seeker", pretty_name="Sanctum Seeker", cost=['2', 'B', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Vampire Knight",
                     abilities=[116739], set_id="XLN", rarity="Rare", collectible=True, set_number=120,
                     mtga_id=66205)
SeekersSquire = Card(name="seekers_squire", pretty_name="Seekers' Squire", cost=['1', 'B'],
                     color_identity=['B'], card_type="Creature", sub_types="Human Scout",
                     abilities=[116886], set_id="XLN", rarity="Uncommon", collectible=True, set_number=121,
                     mtga_id=66207)
SkitteringHeartstopper = Card(name="skittering_heartstopper", pretty_name="Skittering Heartstopper", cost=['B'],
                              color_identity=['B'], card_type="Creature", sub_types="Insect",
                              abilities=[94573], set_id="XLN", rarity="Common", collectible=True, set_number=122,
                              mtga_id=66209)
Skulduggery = Card(name="skulduggery", pretty_name="Skulduggery", cost=['B'],
                   color_identity=['B'], card_type="Instant", sub_types="",
                   abilities=[116740], set_id="XLN", rarity="Common", collectible=True, set_number=123,
                   mtga_id=66211)
SkymarchBloodletter = Card(name="skymarch_bloodletter", pretty_name="Skymarch Bloodletter", cost=['2', 'B'],
                           color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                           abilities=[8, 91870], set_id="XLN", rarity="Common", collectible=True, set_number=124,
                           mtga_id=66213)
SpreadingRot = Card(name="spreading_rot", pretty_name="Spreading Rot", cost=['4', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[5887], set_id="XLN", rarity="Common", collectible=True, set_number=125,
                    mtga_id=66215)
SwordPointDiplomacy = Card(name="swordpoint_diplomacy", pretty_name="Sword-Point Diplomacy", cost=['2', 'B'],
                           color_identity=['B'], card_type="Sorcery", sub_types="",
                           abilities=[116861], set_id="XLN", rarity="Rare", collectible=True, set_number=126,
                           mtga_id=66217)
VanquishtheWeak = Card(name="vanquish_the_weak", pretty_name="Vanquish the Weak", cost=['2', 'B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[61990], set_id="XLN", rarity="Common", collectible=True, set_number=127,
                       mtga_id=66219)
ViciousConquistador = Card(name="vicious_conquistador", pretty_name="Vicious Conquistador", cost=['B'],
                           color_identity=['B'], card_type="Creature", sub_types="Vampire Soldier",
                           abilities=[99121], set_id="XLN", rarity="Uncommon", collectible=True, set_number=128,
                           mtga_id=66221)
VraskasContempt = Card(name="vraskas_contempt", pretty_name="Vraska's Contempt", cost=['2', 'B', 'B'],
                       color_identity=['B'], card_type="Instant", sub_types="",
                       abilities=[116862], set_id="XLN", rarity="Rare", collectible=True, set_number=129,
                       mtga_id=66223)
WalkthePlank = Card(name="walk_the_plank", pretty_name="Walk the Plank", cost=['B', 'B'],
                    color_identity=['B'], card_type="Sorcery", sub_types="",
                    abilities=[116863], set_id="XLN", rarity="Uncommon", collectible=True, set_number=130,
                    mtga_id=66225)
WantedScoundrels = Card(name="wanted_scoundrels", pretty_name="Wanted Scoundrels", cost=['1', 'B'],
                        color_identity=['B'], card_type="Creature", sub_types="Human Pirate",
                        abilities=[116864], set_id="XLN", rarity="Uncommon", collectible=True, set_number=131,
                        mtga_id=66227)
AngrathsMarauders = Card(name="angraths_marauders", pretty_name="Angrath's Marauders", cost=['5', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[116865], set_id="XLN", rarity="Rare", collectible=True, set_number=132,
                         mtga_id=66229)
BondedHorncrest = Card(name="bonded_horncrest", pretty_name="Bonded Horncrest", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[87894], set_id="XLN", rarity="Uncommon", collectible=True, set_number=133,
                       mtga_id=66231)
BrazenBuccaneers = Card(name="brazen_buccaneers", pretty_name="Brazen Buccaneers", cost=['3', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                        abilities=[9, 116886], set_id="XLN", rarity="Common", collectible=True, set_number=134,
                        mtga_id=66233)
BurningSunsAvatar = Card(name="burning_suns_avatar", pretty_name="Burning Sun's Avatar", cost=['3', 'R', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Dinosaur Avatar",
                         abilities=[116741], set_id="XLN", rarity="Rare", collectible=True, set_number=135,
                         mtga_id=66235)
CaptainLanneryStorm = Card(name="captain_lannery_storm", pretty_name="Captain Lannery Storm", cost=['2', 'R'],
                           color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                           abilities=[9, 116867, 116868], set_id="XLN", rarity="Rare", collectible=True, set_number=136,
                           mtga_id=66237)
CaptivatingCrew = Card(name="captivating_crew", pretty_name="Captivating Crew", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                       abilities=[116869], set_id="XLN", rarity="Rare", collectible=True, set_number=137,
                       mtga_id=66239)
ChargingMonstrosaur = Card(name="charging_monstrosaur", pretty_name="Charging Monstrosaur", cost=['4', 'R'],
                           color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[14, 9], set_id="XLN", rarity="Uncommon", collectible=True, set_number=138,
                           mtga_id=66241)
Demolish = Card(name="demolish", pretty_name="Demolish", cost=['3', 'R'],
                color_identity=['R'], card_type="Sorcery", sub_types="",
                abilities=[1691], set_id="XLN", rarity="Common", collectible=True, set_number=139,
                mtga_id=66243)
DinosaurStampede = Card(name="dinosaur_stampede", pretty_name="Dinosaur Stampede", cost=['2', 'R'],
                        color_identity=['R'], card_type="Instant", sub_types="",
                        abilities=[116871], set_id="XLN", rarity="Uncommon", collectible=True, set_number=140,
                        mtga_id=66245)
DualShot = Card(name="dual_shot", pretty_name="Dual Shot", cost=['R'],
                color_identity=['R'], card_type="Instant", sub_types="",
                abilities=[102907], set_id="XLN", rarity="Common", collectible=True, set_number=141,
                mtga_id=66247)
FathomFleetFirebrand = Card(name="fathom_fleet_firebrand", pretty_name="Fathom Fleet Firebrand", cost=['1', 'R'],
                            color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                            abilities=[88126], set_id="XLN", rarity="Common", collectible=True, set_number=142,
                            mtga_id=66249)
FieryCannonade = Card(name="fiery_cannonade", pretty_name="Fiery Cannonade", cost=['2', 'R'],
                      color_identity=['R'], card_type="Instant", sub_types="",
                      abilities=[116743], set_id="XLN", rarity="Uncommon", collectible=True, set_number=143,
                      mtga_id=66251)
FireShrineKeeper = Card(name="fire_shrine_keeper", pretty_name="Fire Shrine Keeper", cost=['R'],
                        color_identity=['R'], card_type="Creature", sub_types="Elemental",
                        abilities=[142, 116744], set_id="XLN", rarity="Common", collectible=True, set_number=144,
                        mtga_id=66253)
FirecannonBlast = Card(name="firecannon_blast", pretty_name="Firecannon Blast", cost=['1', 'R', 'R'],
                       color_identity=['R'], card_type="Sorcery", sub_types="",
                       abilities=[1166], set_id="XLN", rarity="Common", collectible=True, set_number=145,
                       mtga_id=66255)
FrenziedRaptor = Card(name="frenzied_raptor", pretty_name="Frenzied Raptor", cost=['2', 'R'],
                      color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                      abilities=[], set_id="XLN", rarity="Common", collectible=True, set_number=146,
                      mtga_id=66257)
HeadstrongBrute = Card(name="headstrong_brute", pretty_name="Headstrong Brute", cost=['2', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Orc Pirate",
                       abilities=[86476, 116872], set_id="XLN", rarity="Common", collectible=True, set_number=147,
                       mtga_id=66259)
Hijack = Card(name="hijack", pretty_name="Hijack", cost=['1', 'R', 'R'],
              color_identity=['R'], card_type="Sorcery", sub_types="",
              abilities=[76420], set_id="XLN", rarity="Common", collectible=True, set_number=148,
              mtga_id=66261)
LightningStrike = Card(name="lightning_strike", pretty_name="Lightning Strike", cost=['1', 'R'],
                       color_identity=['R'], card_type="Instant", sub_types="",
                       abilities=[70361], set_id="XLN", rarity="Uncommon", collectible=True, set_number=149,
                       mtga_id=66263)
LightningRigCrew = Card(name="lightningrig_crew", pretty_name="Lightning-Rig Crew", cost=['2', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Goblin Pirate",
                        abilities=[62292, 1172], set_id="XLN", rarity="Uncommon", collectible=True, set_number=150,
                        mtga_id=66265)
MakeshiftMunitions = Card(name="makeshift_munitions", pretty_name="Makeshift Munitions", cost=['1', 'R'],
                          color_identity=['R'], card_type="Enchantment", sub_types="",
                          abilities=[116874], set_id="XLN", rarity="Uncommon", collectible=True, set_number=151,
                          mtga_id=66267)
NestRobber = Card(name="nest_robber", pretty_name="Nest Robber", cost=['1', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                  abilities=[9], set_id="XLN", rarity="Common", collectible=True, set_number=152,
                  mtga_id=66269)
OtepecHuntmaster = Card(name="otepec_huntmaster", pretty_name="Otepec Huntmaster", cost=['1', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Human Shaman",
                        abilities=[116730, 116835], set_id="XLN", rarity="Uncommon", collectible=True, set_number=153,
                        mtga_id=66271)
RampagingFerocidon = Card(name="rampaging_ferocidon", pretty_name="Rampaging Ferocidon", cost=['2', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                          abilities=[142, 92939, 1176], set_id="XLN", rarity="Rare", collectible=True, set_number=154,
                          mtga_id=66273)
RaptorHatchling = Card(name="raptor_hatchling", pretty_name="Raptor Hatchling", cost=['1', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[1177], set_id="XLN", rarity="Uncommon", collectible=True, set_number=155,
                       mtga_id=66275)
RepeatingBarrage = Card(name="repeating_barrage", pretty_name="Repeating Barrage", cost=['1', 'R', 'R'],
                        color_identity=['R'], card_type="Sorcery", sub_types="",
                        abilities=[70361, 116895], set_id="XLN", rarity="Rare", collectible=True, set_number=156,
                        mtga_id=66277)
RiggingRunner = Card(name="rigging_runner", pretty_name="Rigging Runner", cost=['R'],
                     color_identity=['R'], card_type="Creature", sub_types="Goblin Pirate",
                     abilities=[6, 101552], set_id="XLN", rarity="Uncommon", collectible=True, set_number=157,
                     mtga_id=66279)
Rile = Card(name="rile", pretty_name="Rile", cost=['R'],
            color_identity=['R'], card_type="Sorcery", sub_types="",
            abilities=[116745, 25848], set_id="XLN", rarity="Common", collectible=True, set_number=158,
            mtga_id=66281)
RowdyCrew = Card(name="rowdy_crew", pretty_name="Rowdy Crew", cost=['2', 'R', 'R'],
                 color_identity=['R'], card_type="Creature", sub_types="Human Pirate",
                 abilities=[14, 116876], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=159,
                 mtga_id=66283)
RummagingGoblin = Card(name="rummaging_goblin", pretty_name="Rummaging Goblin", cost=['2', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Goblin Rogue",
                       abilities=[2091], set_id="XLN", rarity="Common", collectible=True, set_number=160,
                       mtga_id=66285)
StarofExtinction = Card(name="star_of_extinction", pretty_name="Star of Extinction", cost=['5', 'R', 'R'],
                        color_identity=['R'], card_type="Sorcery", sub_types="",
                        abilities=[116877], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=161,
                        mtga_id=66287)
StormFleetArsonist = Card(name="storm_fleet_arsonist", pretty_name="Storm Fleet Arsonist", cost=['4', 'R'],
                          color_identity=['R'], card_type="Creature", sub_types="Orc Pirate",
                          abilities=[116878], set_id="XLN", rarity="Uncommon", collectible=True, set_number=162,
                          mtga_id=66289)
StormFleetPyromancer = Card(name="storm_fleet_pyromancer", pretty_name="Storm Fleet Pyromancer", cost=['4', 'R'],
                            color_identity=['R'], card_type="Creature", sub_types="Human Pirate Wizard",
                            abilities=[118593], set_id="XLN", rarity="Common", collectible=True, set_number=163,
                            mtga_id=66291)
SunCrownedHunters = Card(name="suncrowned_hunters", pretty_name="Sun-Crowned Hunters", cost=['4', 'R', 'R'],
                         color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                         abilities=[118594], set_id="XLN", rarity="Common", collectible=True, set_number=164,
                         mtga_id=66293)
SunbirdsInvocation = Card(name="sunbirds_invocation", pretty_name="Sunbird's Invocation", cost=['5', 'R'],
                          color_identity=['R'], card_type="Enchantment", sub_types="",
                          abilities=[116880], set_id="XLN", rarity="Rare", collectible=True, set_number=165,
                          mtga_id=66295)
SureStrike = Card(name="sure_strike", pretty_name="Sure Strike", cost=['1', 'R'],
                  color_identity=['R'], card_type="Instant", sub_types="",
                  abilities=[1019], set_id="XLN", rarity="Common", collectible=True, set_number=166,
                  mtga_id=66297)
Swashbuckling = Card(name="swashbuckling", pretty_name="Swashbuckling", cost=['1', 'R'],
                     color_identity=['R'], card_type="Enchantment", sub_types="Aura",
                     abilities=[1027, 1193], set_id="XLN", rarity="Common", collectible=True, set_number=167,
                     mtga_id=66299)
ThrashofRaptors = Card(name="thrash_of_raptors", pretty_name="Thrash of Raptors", cost=['3', 'R'],
                       color_identity=['R'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[116746], set_id="XLN", rarity="Common", collectible=True, set_number=168,
                       mtga_id=66301)
TilonallisKnight = Card(name="tilonallis_knight", pretty_name="Tilonalli's Knight", cost=['1', 'R'],
                        color_identity=['R'], card_type="Creature", sub_types="Human Knight",
                        abilities=[116747], set_id="XLN", rarity="Common", collectible=True, set_number=169,
                        mtga_id=66303)
TilonallisSkinshifter = Card(name="tilonallis_skinshifter", pretty_name="Tilonalli's Skinshifter", cost=['2', 'R'],
                             color_identity=['R'], card_type="Creature", sub_types="Human Shaman",
                             abilities=[9, 116748], set_id="XLN", rarity="Rare", collectible=True, set_number=170,
                             mtga_id=66305)
TroveofTemptation = Card(name="trove_of_temptation", pretty_name="Trove of Temptation", cost=['3', 'R'],
                         color_identity=['R'], card_type="Enchantment", sub_types="",
                         abilities=[116749, 116884], set_id="XLN", rarity="Uncommon", collectible=True, set_number=171,
                         mtga_id=66307)
UnfriendlyFire = Card(name="unfriendly_fire", pretty_name="Unfriendly Fire", cost=['4', 'R'],
                      color_identity=['R'], card_type="Instant", sub_types="",
                      abilities=[2200], set_id="XLN", rarity="Common", collectible=True, set_number=172,
                      mtga_id=66309)
VancesBlastingCannons = Card(name="vances_blasting_cannons", pretty_name="Vance's Blasting Cannons", cost=['3', 'R'],
                             color_identity=['R'], card_type="Enchantment", sub_types="",
                             abilities=[1195, 1196], set_id="XLN", rarity="Rare", collectible=True, set_number=173,
                             mtga_id=66311)
SpitfireBastion = Card(name="spitfire_bastion", pretty_name="Spitfire Bastion", cost=[],
                       color_identity=['R'], card_type="Land", sub_types="",
                       abilities=[1004, 1198], set_id="XLN", rarity="Rare", collectible=False, set_number=173,
                       mtga_id=66313)
WilyGoblin = Card(name="wily_goblin", pretty_name="Wily Goblin", cost=['R', 'R'],
                  color_identity=['R'], card_type="Creature", sub_types="Goblin Pirate",
                  abilities=[116826], set_id="XLN", rarity="Uncommon", collectible=True, set_number=174,
                  mtga_id=66315)
AncientBrontodon = Card(name="ancient_brontodon", pretty_name="Ancient Brontodon", cost=['6', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[], set_id="XLN", rarity="Common", collectible=True, set_number=175,
                        mtga_id=66317)
AtzocanArcher = Card(name="atzocan_archer", pretty_name="Atzocan Archer", cost=['2', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Human Archer",
                     abilities=[13, 116873], set_id="XLN", rarity="Uncommon", collectible=True, set_number=176,
                     mtga_id=66319)
BlindingFog = Card(name="blinding_fog", pretty_name="Blinding Fog", cost=['2', 'G'],
                   color_identity=['G'], card_type="Instant", sub_types="",
                   abilities=[116752], set_id="XLN", rarity="Common", collectible=True, set_number=177,
                   mtga_id=66321)
BlossomDryad = Card(name="blossom_dryad", pretty_name="Blossom Dryad", cost=['2', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Dryad",
                    abilities=[6266], set_id="XLN", rarity="Common", collectible=True, set_number=178,
                    mtga_id=66323)
CarnageTyrant = Card(name="carnage_tyrant", pretty_name="Carnage Tyrant", cost=['4', 'G', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                     abilities=[120287, 14, 10], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=179,
                     mtga_id=66325)
ColossalDreadmaw = Card(name="colossal_dreadmaw", pretty_name="Colossal Dreadmaw", cost=['4', 'G', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[14], set_id="XLN", rarity="Common", collectible=True, set_number=180,
                        mtga_id=66327)
CommunewithDinosaurs = Card(name="commune_with_dinosaurs", pretty_name="Commune with Dinosaurs", cost=['G'],
                            color_identity=['G'], card_type="Sorcery", sub_types="",
                            abilities=[116753], set_id="XLN", rarity="Common", collectible=True, set_number=181,
                            mtga_id=66329)
CrashtheRamparts = Card(name="crash_the_ramparts", pretty_name="Crash the Ramparts", cost=['2', 'G'],
                        color_identity=['G'], card_type="Instant", sub_types="",
                        abilities=[4776], set_id="XLN", rarity="Common", collectible=True, set_number=182,
                        mtga_id=66331)
CrushingCanopy = Card(name="crushing_canopy", pretty_name="Crushing Canopy", cost=['2', 'G'],
                      color_identity=['G'], card_type="Instant", sub_types="",
                      abilities=[1206], set_id="XLN", rarity="Common", collectible=True, set_number=183,
                      mtga_id=66333)
DeathgorgeScavenger = Card(name="deathgorge_scavenger", pretty_name="Deathgorge Scavenger", cost=['2', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[116897], set_id="XLN", rarity="Rare", collectible=True, set_number=184,
                           mtga_id=66335)
DeeprootChampion = Card(name="deeproot_champion", pretty_name="Deeproot Champion", cost=['1', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                        abilities=[1208], set_id="XLN", rarity="Rare", collectible=True, set_number=185,
                        mtga_id=66337)
DeeprootWarrior = Card(name="deeproot_warrior", pretty_name="Deeproot Warrior", cost=['1', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Merfolk Warrior",
                       abilities=[116755], set_id="XLN", rarity="Common", collectible=True, set_number=186,
                       mtga_id=66339)
DroveroftheMighty = Card(name="drover_of_the_mighty", pretty_name="Drover of the Mighty", cost=['1', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Human Druid",
                         abilities=[116756, 1055], set_id="XLN", rarity="Uncommon", collectible=True, set_number=187,
                         mtga_id=66341)
EmergentGrowth = Card(name="emergent_growth", pretty_name="Emergent Growth", cost=['3', 'G'],
                      color_identity=['G'], card_type="Sorcery", sub_types="",
                      abilities=[116847], set_id="XLN", rarity="Uncommon", collectible=True, set_number=188,
                      mtga_id=66343)
EmperorsVanguard = Card(name="emperors_vanguard", pretty_name="Emperor's Vanguard", cost=['3', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Human Scout",
                        abilities=[1213], set_id="XLN", rarity="Rare", collectible=True, set_number=189,
                        mtga_id=66345)
GrazingWhiptail = Card(name="grazing_whiptail", pretty_name="Grazing Whiptail", cost=['2', 'G', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[13], set_id="XLN", rarity="Common", collectible=True, set_number=190,
                       mtga_id=66347)
GrowingRitesofItlimoc = Card(name="growing_rites_of_itlimoc", pretty_name="Growing Rites of Itlimoc", cost=['2', 'G'],
                             color_identity=['G'], card_type="Enchantment", sub_types="",
                             abilities=[103200, 116759], set_id="XLN", rarity="Rare", collectible=True, set_number=191,
                             mtga_id=66349)
ItlimocCradleoftheSun = Card(name="itlimoc_cradle_of_the_sun", pretty_name="Itlimoc, Cradle of the Sun", cost=[],
                             color_identity=['G'], card_type="Land", sub_types="",
                             abilities=[1005, 13428], set_id="XLN", rarity="Rare", collectible=False, set_number=191,
                             mtga_id=66351)
IxallisDiviner = Card(name="ixallis_diviner", pretty_name="Ixalli's Diviner", cost=['1', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Human Druid",
                      abilities=[116886], set_id="XLN", rarity="Common", collectible=True, set_number=192,
                      mtga_id=66353)
IxallisKeeper = Card(name="ixallis_keeper", pretty_name="Ixalli's Keeper", cost=['1', 'G'],
                     color_identity=['G'], card_type="Creature", sub_types="Human Shaman",
                     abilities=[116760], set_id="XLN", rarity="Common", collectible=True, set_number=193,
                     mtga_id=66355)
JadeGuardian = Card(name="jade_guardian", pretty_name="Jade Guardian", cost=['3', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                    abilities=[10, 116761], set_id="XLN", rarity="Common", collectible=True, set_number=194,
                    mtga_id=66357)
JungleDelver = Card(name="jungle_delver", pretty_name="Jungle Delver", cost=['G'],
                    color_identity=['G'], card_type="Creature", sub_types="Merfolk Warrior",
                    abilities=[76748], set_id="XLN", rarity="Common", collectible=True, set_number=195,
                    mtga_id=66359)
KumenasSpeaker = Card(name="kumenas_speaker", pretty_name="Kumena's Speaker", cost=['G'],
                      color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                      abilities=[116762], set_id="XLN", rarity="Uncommon", collectible=True, set_number=196,
                      mtga_id=66361)
MerfolkBranchwalker = Card(name="merfolk_branchwalker", pretty_name="Merfolk Branchwalker", cost=['1', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Merfolk Scout",
                           abilities=[116886], set_id="XLN", rarity="Uncommon", collectible=True, set_number=197,
                           mtga_id=66363)
NewHorizons = Card(name="new_horizons", pretty_name="New Horizons", cost=['2', 'G'],
                   color_identity=['G'], card_type="Enchantment", sub_types="Aura",
                   abilities=[1570, 101825, 61119], set_id="XLN", rarity="Common", collectible=True, set_number=198,
                   mtga_id=66365)
OldGrowthDryads = Card(name="oldgrowth_dryads", pretty_name="Old-Growth Dryads", cost=['G'],
                       color_identity=['G'], card_type="Creature", sub_types="Dryad",
                       abilities=[1226], set_id="XLN", rarity="Rare", collectible=True, set_number=199,
                       mtga_id=66367)
Pounce = Card(name="pounce", pretty_name="Pounce", cost=['1', 'G'],
              color_identity=['G'], card_type="Instant", sub_types="",
              abilities=[99356], set_id="XLN", rarity="Common", collectible=True, set_number=200,
              mtga_id=66369)
RangingRaptors = Card(name="ranging_raptors", pretty_name="Ranging Raptors", cost=['2', 'G'],
                      color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                      abilities=[1228], set_id="XLN", rarity="Uncommon", collectible=True, set_number=201,
                      mtga_id=66371)
RavenousDaggertooth = Card(name="ravenous_daggertooth", pretty_name="Ravenous Daggertooth", cost=['2', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[1229], set_id="XLN", rarity="Common", collectible=True, set_number=202,
                           mtga_id=66373)
RipjawRaptor = Card(name="ripjaw_raptor", pretty_name="Ripjaw Raptor", cost=['2', 'G', 'G'],
                    color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                    abilities=[1230], set_id="XLN", rarity="Rare", collectible=True, set_number=203,
                    mtga_id=66375)
RiverHeraldsBoon = Card(name="river_heralds_boon", pretty_name="River Heralds' Boon", cost=['1', 'G'],
                        color_identity=['G'], card_type="Instant", sub_types="",
                        abilities=[116769], set_id="XLN", rarity="Common", collectible=True, set_number=204,
                        mtga_id=66377)
SavageStomp = Card(name="savage_stomp", pretty_name="Savage Stomp", cost=['2', 'G'],
                   color_identity=['G'], card_type="Sorcery", sub_types="",
                   abilities=[116763, 20207], set_id="XLN", rarity="Uncommon", collectible=True, set_number=205,
                   mtga_id=66379)
ShapersSanctuary = Card(name="shapers_sanctuary", pretty_name="Shapers' Sanctuary", cost=['G'],
                        color_identity=['G'], card_type="Enchantment", sub_types="",
                        abilities=[116764], set_id="XLN", rarity="Rare", collectible=True, set_number=206,
                        mtga_id=66381)
SliceinTwain = Card(name="slice_in_twain", pretty_name="Slice in Twain", cost=['2', 'G', 'G'],
                    color_identity=['G'], card_type="Instant", sub_types="",
                    abilities=[120290, 25848], set_id="XLN", rarity="Uncommon", collectible=True, set_number=207,
                    mtga_id=66383)
SnappingSailback = Card(name="snapping_sailback", pretty_name="Snapping Sailback", cost=['4', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[7, 116765], set_id="XLN", rarity="Uncommon", collectible=True, set_number=208,
                        mtga_id=66385)
SpikeTailedCeratops = Card(name="spiketailed_ceratops", pretty_name="Spike-Tailed Ceratops", cost=['4', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[76869], set_id="XLN", rarity="Common", collectible=True, set_number=209,
                           mtga_id=66387)
ThunderingSpineback = Card(name="thundering_spineback", pretty_name="Thundering Spineback", cost=['5', 'G', 'G'],
                           color_identity=['G'], card_type="Creature", sub_types="Dinosaur",
                           abilities=[116766, 116767], set_id="XLN", rarity="Uncommon", collectible=True, set_number=210,
                           mtga_id=66389)
TishanasWayfinder = Card(name="tishanas_wayfinder", pretty_name="Tishana's Wayfinder", cost=['2', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Merfolk Scout",
                         abilities=[116886], set_id="XLN", rarity="Common", collectible=True, set_number=211,
                         mtga_id=66391)
VerdantRebirth = Card(name="verdant_rebirth", pretty_name="Verdant Rebirth", cost=['1', 'G'],
                      color_identity=['G'], card_type="Instant", sub_types="",
                      abilities=[116802, 25848], set_id="XLN", rarity="Uncommon", collectible=True, set_number=212,
                      mtga_id=66393)
VerdantSunsAvatar = Card(name="verdant_suns_avatar", pretty_name="Verdant Sun's Avatar", cost=['5', 'G', 'G'],
                         color_identity=['G'], card_type="Creature", sub_types="Dinosaur Avatar",
                         abilities=[116804], set_id="XLN", rarity="Rare", collectible=True, set_number=213,
                         mtga_id=66395)
VineshaperMystic = Card(name="vineshaper_mystic", pretty_name="Vineshaper Mystic", cost=['2', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                        abilities=[116808], set_id="XLN", rarity="Uncommon", collectible=True, set_number=214,
                        mtga_id=66397)
WakeroftheWilds = Card(name="waker_of_the_wilds", pretty_name="Waker of the Wilds", cost=['2', 'G', 'G'],
                       color_identity=['G'], card_type="Creature", sub_types="Merfolk Shaman",
                       abilities=[116770], set_id="XLN", rarity="Rare", collectible=True, set_number=215,
                       mtga_id=66399)
WildgrowthWalker = Card(name="wildgrowth_walker", pretty_name="Wildgrowth Walker", cost=['1', 'G'],
                        color_identity=['G'], card_type="Creature", sub_types="Elemental",
                        abilities=[116771], set_id="XLN", rarity="Uncommon", collectible=True, set_number=216,
                        mtga_id=66401)
AdmiralBeckettBrass = Card(name="admiral_beckett_brass", pretty_name="Admiral Beckett Brass", cost=['1', 'U', 'B', 'R'],
                           color_identity=['U', 'B', 'R'], card_type="Creature", sub_types="Human Pirate",
                           abilities=[116772, 116813], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=217,
                           mtga_id=66403)
BelligerentBrontodon = Card(name="belligerent_brontodon", pretty_name="Belligerent Brontodon", cost=['5', 'G', 'W'],
                            color_identity=['G', 'W'], card_type="Creature", sub_types="Dinosaur",
                            abilities=[61077], set_id="XLN", rarity="Uncommon", collectible=True, set_number=218,
                            mtga_id=66405)
CalltotheFeast = Card(name="call_to_the_feast", pretty_name="Call to the Feast", cost=['2', 'W', 'B'],
                      color_identity=['W', 'B'], card_type="Sorcery", sub_types="",
                      abilities=[116774], set_id="XLN", rarity="Uncommon", collectible=True, set_number=219,
                      mtga_id=66407)
DeadeyePlunderers = Card(name="deadeye_plunderers", pretty_name="Deadeye Plunderers", cost=['3', 'U', 'B'],
                         color_identity=['U', 'B'], card_type="Creature", sub_types="Human Pirate",
                         abilities=[1250, 116898], set_id="XLN", rarity="Uncommon", collectible=True, set_number=220,
                         mtga_id=66409)
DireFleetCaptain = Card(name="dire_fleet_captain", pretty_name="Dire Fleet Captain", cost=['B', 'R'],
                        color_identity=['B', 'R'], card_type="Creature", sub_types="Orc Pirate",
                        abilities=[116817], set_id="XLN", rarity="Uncommon", collectible=True, set_number=221,
                        mtga_id=66411)
GishathSunsAvatar = Card(name="gishath_suns_avatar", pretty_name="Gishath, Sun's Avatar", cost=['5', 'R', 'G', 'W'],
                         color_identity=['W', 'R', 'G'], card_type="Creature", sub_types="Dinosaur Avatar",
                         abilities=[15, 14, 9, 116777], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=222,
                         mtga_id=66413)
HostageTaker = Card(name="hostage_taker", pretty_name="Hostage Taker", cost=['2', 'U', 'B'],
                    color_identity=['U', 'B'], card_type="Creature", sub_types="Human Pirate",
                    abilities=[118521], set_id="XLN", rarity="Rare", collectible=True, set_number=223,
                    mtga_id=66415)
HuatliWarriorPoet = Card(name="huatli_warrior_poet", pretty_name="Huatli, Warrior Poet", cost=['3', 'R', 'W'],
                         color_identity=['R', 'W'], card_type="Planeswalker", sub_types="Huatli",
                         abilities=[118786, 116780, 1258], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=224,
                         mtga_id=66417)
MaraudingLooter = Card(name="marauding_looter", pretty_name="Marauding Looter", cost=['2', 'U', 'R'],
                       color_identity=['U', 'R'], card_type="Creature", sub_types="Human Pirate",
                       abilities=[116824], set_id="XLN", rarity="Uncommon", collectible=True, set_number=225,
                       mtga_id=66419)
RagingSwordtooth = Card(name="raging_swordtooth", pretty_name="Raging Swordtooth", cost=['3', 'R', 'G'],
                        color_identity=['R', 'G'], card_type="Creature", sub_types="Dinosaur",
                        abilities=[14, 116781], set_id="XLN", rarity="Uncommon", collectible=True, set_number=226,
                        mtga_id=66421)
RegisaurAlpha = Card(name="regisaur_alpha", pretty_name="Regisaur Alpha", cost=['3', 'R', 'G'],
                     color_identity=['R', 'G'], card_type="Creature", sub_types="Dinosaur",
                     abilities=[116782, 116783], set_id="XLN", rarity="Rare", collectible=True, set_number=227,
                     mtga_id=66423)
ShapersofNature = Card(name="shapers_of_nature", pretty_name="Shapers of Nature", cost=['1', 'G', 'U'],
                       color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Shaman",
                       abilities=[116784, 116785], set_id="XLN", rarity="Uncommon", collectible=True, set_number=228,
                       mtga_id=66425)
SkyTerror = Card(name="sky_terror", pretty_name="Sky Terror", cost=['R', 'W'],
                 color_identity=['R', 'W'], card_type="Creature", sub_types="Dinosaur",
                 abilities=[8, 142], set_id="XLN", rarity="Uncommon", collectible=True, set_number=229,
                 mtga_id=66427)
TishanaVoiceofThunder = Card(name="tishana_voice_of_thunder", pretty_name="Tishana, Voice of Thunder", cost=['5', 'G', 'U'],
                             color_identity=['G', 'U'], card_type="Creature", sub_types="Merfolk Shaman",
                             abilities=[86635, 1640, 116832], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=230,
                             mtga_id=66429)
VonaButcherofMagan = Card(name="vona_butcher_of_magan", pretty_name="Vona, Butcher of Magan", cost=['3', 'W', 'B'],
                          color_identity=['W', 'B'], card_type="Creature", sub_types="Vampire Knight",
                          abilities=[15, 12, 116786], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=231,
                          mtga_id=66431)
VraskaRelicSeeker = Card(name="vraska_relic_seeker", pretty_name="Vraska, Relic Seeker", cost=['4', 'B', 'G'],
                         color_identity=['B', 'G'], card_type="Planeswalker", sub_types="Vraska",
                         abilities=[116787, 1270, 116837], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=232,
                         mtga_id=66433)
CobbledWings = Card(name="cobbled_wings", pretty_name="Cobbled Wings", cost=['2'],
                    color_identity=[], card_type="Artifact", sub_types="Equipment",
                    abilities=[4762, 1268], set_id="XLN", rarity="Common", collectible=True, set_number=233,
                    mtga_id=66435)
ConquerorsGalleon = Card(name="conquerors_galleon", pretty_name="Conqueror's Galleon", cost=['4'],
                         color_identity=[], card_type="Artifact", sub_types="Vehicle",
                         abilities=[1273, 76611], set_id="XLN", rarity="Rare", collectible=True, set_number=234,
                         mtga_id=66437)
ConquerorsFoothold = Card(name="conquerors_foothold", pretty_name="Conqueror's Foothold", cost=[],
                          color_identity=[], card_type="Land", sub_types="",
                          abilities=[1152, 1633, 1545, 116791], set_id="XLN", rarity="Rare", collectible=False, set_number=234,
                          mtga_id=66439)
DowsingDagger = Card(name="dowsing_dagger", pretty_name="Dowsing Dagger", cost=['2'],
                     color_identity=[], card_type="Artifact", sub_types="Equipment",
                     abilities=[1280, 2848, 116792, 1319], set_id="XLN", rarity="Rare", collectible=True, set_number=235,
                     mtga_id=66441)
LostVale = Card(name="lost_vale", pretty_name="Lost Vale", cost=[],
                color_identity=[], card_type="Land", sub_types="",
                abilities=[4957], set_id="XLN", rarity="Rare", collectible=False, set_number=235,
                mtga_id=66443)
DuskLegionDreadnought = Card(name="dusk_legion_dreadnought", pretty_name="Dusk Legion Dreadnought", cost=['5'],
                             color_identity=[], card_type="Artifact", sub_types="Vehicle",
                             abilities=[15, 76645], set_id="XLN", rarity="Uncommon", collectible=True, set_number=236,
                             mtga_id=66445)
ElaborateFirecannon = Card(name="elaborate_firecannon", pretty_name="Elaborate Firecannon", cost=['2'],
                           color_identity=[], card_type="Artifact", sub_types="",
                           abilities=[86621, 116794, 116795], set_id="XLN", rarity="Uncommon", collectible=True, set_number=237,
                           mtga_id=66447)
FellFlagship = Card(name="fell_flagship", pretty_name="Fell Flagship", cost=['3'],
                    color_identity=[], card_type="Artifact", sub_types="Vehicle",
                    abilities=[1289, 88861, 76515], set_id="XLN", rarity="Rare", collectible=True, set_number=238,
                    mtga_id=66449)
GildedSentinel = Card(name="gilded_sentinel", pretty_name="Gilded Sentinel", cost=['4'],
                      color_identity=[], card_type="Artifact Creature", sub_types="Golem",
                      abilities=[], set_id="XLN", rarity="Common", collectible=True, set_number=239,
                      mtga_id=66451)
HierophantsChalice = Card(name="hierophants_chalice", pretty_name="Hierophant's Chalice", cost=['3'],
                          color_identity=[], card_type="Artifact", sub_types="",
                          abilities=[91870, 1152], set_id="XLN", rarity="Common", collectible=True, set_number=240,
                          mtga_id=66453)
PillarofOrigins = Card(name="pillar_of_origins", pretty_name="Pillar of Origins", cost=['2'],
                       color_identity=[], card_type="Artifact", sub_types="",
                       abilities=[76882, 1292], set_id="XLN", rarity="Uncommon", collectible=True, set_number=241,
                       mtga_id=66455)
PiratesCutlass = Card(name="pirates_cutlass", pretty_name="Pirate's Cutlass", cost=['3'],
                      color_identity=[], card_type="Artifact", sub_types="Equipment",
                      abilities=[116796, 2848, 1319], set_id="XLN", rarity="Common", collectible=True, set_number=242,
                      mtga_id=66457)
PrimalAmulet = Card(name="primal_amulet", pretty_name="Primal Amulet", cost=['4'],
                    color_identity=[], card_type="Artifact", sub_types="",
                    abilities=[19445, 116853], set_id="XLN", rarity="Rare", collectible=True, set_number=243,
                    mtga_id=66459)
PrimalWellspring = Card(name="primal_wellspring", pretty_name="Primal Wellspring", cost=[],
                        color_identity=[], card_type="Land", sub_types="",
                        abilities=[116798], set_id="XLN", rarity="Rare", collectible=False, set_number=243,
                        mtga_id=66461)
PryingBlade = Card(name="prying_blade", pretty_name="Prying Blade", cost=['1'],
                   color_identity=[], card_type="Artifact", sub_types="Equipment",
                   abilities=[2873, 116799, 1319], set_id="XLN", rarity="Common", collectible=True, set_number=244,
                   mtga_id=66463)
SentinelTotem = Card(name="sentinel_totem", pretty_name="Sentinel Totem", cost=['1'],
                     color_identity=[], card_type="Artifact", sub_types="",
                     abilities=[91717, 116800], set_id="XLN", rarity="Uncommon", collectible=True, set_number=245,
                     mtga_id=66465)
ShadowedCaravel = Card(name="shadowed_caravel", pretty_name="Shadowed Caravel", cost=['2'],
                       color_identity=[], card_type="Artifact", sub_types="Vehicle",
                       abilities=[116855, 76645], set_id="XLN", rarity="Rare", collectible=True, set_number=246,
                       mtga_id=66467)
SleekSchooner = Card(name="sleek_schooner", pretty_name="Sleek Schooner", cost=['3'],
                     color_identity=[], card_type="Artifact", sub_types="Vehicle",
                     abilities=[76556], set_id="XLN", rarity="Uncommon", collectible=True, set_number=247,
                     mtga_id=66469)
SorcerousSpyglass = Card(name="sorcerous_spyglass", pretty_name="Sorcerous Spyglass", cost=['2'],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[116856, 88194], set_id="XLN", rarity="Rare", collectible=True, set_number=248,
                         mtga_id=66471)
ThaumaticCompass = Card(name="thaumatic_compass", pretty_name="Thaumatic Compass", cost=['2'],
                        color_identity=[], card_type="Artifact", sub_types="",
                        abilities=[116803, 1306], set_id="XLN", rarity="Rare", collectible=True, set_number=249,
                        mtga_id=66473)
SpiresofOrazca = Card(name="spires_of_orazca", pretty_name="Spires of Orazca", cost=[],
                      color_identity=[], card_type="Land", sub_types="",
                      abilities=[1152, 116858], set_id="XLN", rarity="Rare", collectible=False, set_number=249,
                      mtga_id=66475)
TreasureMap = Card(name="treasure_map", pretty_name="Treasure Map", cost=['2'],
                   color_identity=[], card_type="Artifact", sub_types="",
                   abilities=[1308], set_id="XLN", rarity="Rare", collectible=True, set_number=250,
                   mtga_id=66477)
TreasureCove = Card(name="treasure_cove", pretty_name="Treasure Cove", cost=[],
                    color_identity=[], card_type="Land", sub_types="",
                    abilities=[1152, 116859], set_id="XLN", rarity="Rare", collectible=False, set_number=250,
                    mtga_id=66479)
VanquishersBanner = Card(name="vanquishers_banner", pretty_name="Vanquisher's Banner", cost=['5'],
                         color_identity=[], card_type="Artifact", sub_types="",
                         abilities=[76882, 116805, 116806], set_id="XLN", rarity="Rare", collectible=True, set_number=251,
                         mtga_id=66481)
DragonskullSummit = Card(name="dragonskull_summit", pretty_name="Dragonskull Summit", cost=[],
                         color_identity=['B', 'R'], card_type="Land", sub_types="",
                         abilities=[1210, 1211], set_id="XLN", rarity="Rare", collectible=True, set_number=252,
                         mtga_id=66483)
DrownedCatacomb = Card(name="drowned_catacomb", pretty_name="Drowned Catacomb", cost=[],
                       color_identity=['U', 'B'], card_type="Land", sub_types="",
                       abilities=[92868, 1167], set_id="XLN", rarity="Rare", collectible=True, set_number=253,
                       mtga_id=66485)
FieldofRuin = Card(name="field_of_ruin", pretty_name="Field of Ruin", cost=[],
                   color_identity=[], card_type="Land", sub_types="",
                   abilities=[1152, 116809], set_id="XLN", rarity="Uncommon", collectible=True, set_number=254,
                   mtga_id=66487)
GlacialFortress = Card(name="glacial_fortress", pretty_name="Glacial Fortress", cost=[],
                       color_identity=['W', 'U'], card_type="Land", sub_types="",
                       abilities=[92859, 1209], set_id="XLN", rarity="Rare", collectible=True, set_number=255,
                       mtga_id=66489)
RootboundCrag = Card(name="rootbound_crag", pretty_name="Rootbound Crag", cost=[],
                     color_identity=['R', 'G'], card_type="Land", sub_types="",
                     abilities=[91993, 1131], set_id="XLN", rarity="Rare", collectible=True, set_number=256,
                     mtga_id=66491)
SunpetalGrove = Card(name="sunpetal_grove", pretty_name="Sunpetal Grove", cost=[],
                     color_identity=['G', 'W'], card_type="Land", sub_types="",
                     abilities=[92880, 1203], set_id="XLN", rarity="Rare", collectible=True, set_number=257,
                     mtga_id=66493)
UnclaimedTerritory = Card(name="unclaimed_territory", pretty_name="Unclaimed Territory", cost=[],
                          color_identity=[], card_type="Land", sub_types="",
                          abilities=[76882, 1152, 1292], set_id="XLN", rarity="Uncommon", collectible=True, set_number=258,
                          mtga_id=66495)
UnknownShores = Card(name="unknown_shores", pretty_name="Unknown Shores", cost=[],
                     color_identity=[], card_type="Land", sub_types="",
                     abilities=[1152, 1962], set_id="XLN", rarity="Common", collectible=True, set_number=259,
                     mtga_id=66497)
Plains = Card(name="plains", pretty_name="Plains", cost=[],
              color_identity=['W'], card_type="Land", sub_types="Plains",
              abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=260,
              mtga_id=66499)
Plains2 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=261,
               mtga_id=66501)
Plains3 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=262,
               mtga_id=66503)
Plains4 = Card(name="plains", pretty_name="Plains", cost=[],
               color_identity=['W'], card_type="Land", sub_types="Plains",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=263,
               mtga_id=66505)
Island = Card(name="island", pretty_name="Island", cost=[],
              color_identity=['U'], card_type="Land", sub_types="Island",
              abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=264,
              mtga_id=66507)
Island2 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=265,
               mtga_id=66509)
Island3 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=266,
               mtga_id=66511)
Island4 = Card(name="island", pretty_name="Island", cost=[],
               color_identity=['U'], card_type="Land", sub_types="Island",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=267,
               mtga_id=66513)
Swamp = Card(name="swamp", pretty_name="Swamp", cost=[],
             color_identity=['B'], card_type="Land", sub_types="Swamp",
             abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=268,
             mtga_id=66515)
Swamp2 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=269,
              mtga_id=66517)
Swamp3 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=270,
              mtga_id=66519)
Swamp4 = Card(name="swamp", pretty_name="Swamp", cost=[],
              color_identity=['B'], card_type="Land", sub_types="Swamp",
              abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=271,
              mtga_id=66521)
Mountain = Card(name="mountain", pretty_name="Mountain", cost=[],
                color_identity=['R'], card_type="Land", sub_types="Mountain",
                abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=272,
                mtga_id=66523)
Mountain2 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=273,
                 mtga_id=66525)
Mountain3 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=274,
                 mtga_id=66527)
Mountain4 = Card(name="mountain", pretty_name="Mountain", cost=[],
                 color_identity=['R'], card_type="Land", sub_types="Mountain",
                 abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=275,
                 mtga_id=66529)
Forest = Card(name="forest", pretty_name="Forest", cost=[],
              color_identity=['G'], card_type="Land", sub_types="Forest",
              abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=276,
              mtga_id=66531)
Forest2 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=277,
               mtga_id=66533)
Forest3 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=278,
               mtga_id=66535)
Forest4 = Card(name="forest", pretty_name="Forest", cost=[],
               color_identity=['G'], card_type="Land", sub_types="Forest",
               abilities=[], set_id="XLN", rarity="Basic", collectible=True, set_number=279,
               mtga_id=66537)
JaceIngeniousMindMage = Card(name="jace_ingenious_mindmage", pretty_name="Jace, Ingenious Mind-Mage", cost=['4', 'U', 'U'],
                             color_identity=['U'], card_type="Planeswalker", sub_types="Jace",
                             abilities=[1323, 116899, 116907], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=280,
                             mtga_id=66541)
CastawaysDespair = Card(name="castaways_despair", pretty_name="Castaway's Despair", cost=['3', 'U'],
                        color_identity=['U'], card_type="Enchantment", sub_types="Aura",
                        abilities=[1027, 89789, 88178], set_id="XLN", rarity="Common", collectible=True, set_number=281,
                        mtga_id=66543)
GraspingCurrent = Card(name="grasping_current", pretty_name="Grasping Current", cost=['4', 'U'],
                       color_identity=['U'], card_type="Sorcery", sub_types="",
                       abilities=[116900, 116901], set_id="XLN", rarity="Rare", collectible=True, set_number=282,
                       mtga_id=66545)
JacesSentinel = Card(name="jaces_sentinel", pretty_name="Jace's Sentinel", cost=['1', 'U'],
                     color_identity=['U'], card_type="Creature", sub_types="Merfolk Warrior",
                     abilities=[116902], set_id="XLN", rarity="Uncommon", collectible=True, set_number=283,
                     mtga_id=66547)
WoodlandStream = Card(name="woodland_stream", pretty_name="Woodland Stream", cost=[],
                      color_identity=['G', 'U'], card_type="Land", sub_types="",
                      abilities=[76735, 18504], set_id="XLN", rarity="Common", collectible=True, set_number=284,
                      mtga_id=66549)
HuatliDinosaurKnight = Card(name="huatli_dinosaur_knight", pretty_name="Huatli, Dinosaur Knight", cost=['4', 'R', 'W'],
                            color_identity=['R', 'W'], card_type="Planeswalker", sub_types="Huatli",
                            abilities=[116903, 116904, 116905], set_id="XLN", rarity="Mythic Rare", collectible=True, set_number=285,
                            mtga_id=66551)
HuatlisSnubhorn = Card(name="huatlis_snubhorn", pretty_name="Huatli's Snubhorn", cost=['1', 'W'],
                       color_identity=['W'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[15], set_id="XLN", rarity="Common", collectible=True, set_number=286,
                       mtga_id=66553)
HuatlisSpurring = Card(name="huatlis_spurring", pretty_name="Huatli's Spurring", cost=['R'],
                       color_identity=['R'], card_type="Instant", sub_types="",
                       abilities=[116906], set_id="XLN", rarity="Uncommon", collectible=True, set_number=287,
                       mtga_id=66555)
SunBlessedMount = Card(name="sunblessed_mount", pretty_name="Sun-Blessed Mount", cost=['3', 'R', 'W'],
                       color_identity=['R', 'W'], card_type="Creature", sub_types="Dinosaur",
                       abilities=[116908], set_id="XLN", rarity="Rare", collectible=True, set_number=288,
                       mtga_id=66557)
StoneQuarry = Card(name="stone_quarry", pretty_name="Stone Quarry", cost=[],
                   color_identity=['R', 'W'], card_type="Land", sub_types="",
                   abilities=[76735, 4247], set_id="XLN", rarity="Common", collectible=True, set_number=289,
                   mtga_id=66559)
Vampire = Card(name="vampire", pretty_name="Vampire", cost=[],
               color_identity=[], card_type="Creature", sub_types="Vampire",
               abilities=[12], set_id="XLN", rarity="Token", collectible=False, set_number=10001,
               mtga_id=66609)
Illusion = Card(name="illusion", pretty_name="Illusion", cost=[],
                color_identity=[], card_type="Creature", sub_types="Illusion",
                abilities=[116807], set_id="XLN", rarity="Token", collectible=False, set_number=10002,
                mtga_id=66610)
Merfolk = Card(name="merfolk", pretty_name="Merfolk", cost=[],
               color_identity=[], card_type="Creature", sub_types="Merfolk",
               abilities=[10], set_id="XLN", rarity="Token", collectible=False, set_number=10003,
               mtga_id=66611)
Pirate = Card(name="pirate", pretty_name="Pirate", cost=[],
              color_identity=[], card_type="Creature", sub_types="Pirate",
              abilities=[142], set_id="XLN", rarity="Token", collectible=False, set_number=10004,
              mtga_id=66612)
Dinosaur = Card(name="dinosaur", pretty_name="Dinosaur", cost=[],
                color_identity=[], card_type="Creature", sub_types="Dinosaur",
                abilities=[14], set_id="XLN", rarity="Token", collectible=False, set_number=10005,
                mtga_id=66613)
Plant = Card(name="plant", pretty_name="Plant", cost=[],
             color_identity=[], card_type="Creature", sub_types="Plant",
             abilities=[2], set_id="XLN", rarity="Token", collectible=False, set_number=10006,
             mtga_id=66614)
Treasure = Card(name="treasure", pretty_name="Treasure", cost=[],
                color_identity=[], card_type="Artifact", sub_types="Treasure",
                abilities=[119572], set_id="XLN", rarity="Token", collectible=False, set_number=10007,
                mtga_id=66615)
Treasure2 = Card(name="treasure", pretty_name="Treasure", cost=[],
                 color_identity=[], card_type="Artifact", sub_types="Treasure",
                 abilities=[119572], set_id="XLN", rarity="Token", collectible=False, set_number=10008,
                 mtga_id=66616)
Treasure3 = Card(name="treasure", pretty_name="Treasure", cost=[],
                 color_identity=[], card_type="Artifact", sub_types="Treasure",
                 abilities=[119572], set_id="XLN", rarity="Token", collectible=False, set_number=10009,
                 mtga_id=66617)
Treasure4 = Card(name="treasure", pretty_name="Treasure", cost=[],
                 color_identity=[], card_type="Artifact", sub_types="Treasure",
                 abilities=[119572], set_id="XLN", rarity="Token", collectible=False, set_number=10010,
                 mtga_id=66618)


clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
Ixalan = Set("xln", cards=clsmembers)

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
 1006: 'As long as Adanto Vanguard is attacking, it gets +2/+0.',
 1010: 'At the beginning of your upkeep, you may have two target players '
       'exchange life totals.',
 1011: '<i>Enrage</i>  Whenever Bellowing Aegisaur is dealt damage, put a '
       '+1/+1 counter on each other creature you control.',
 1019: 'Target creature gets +3/+0 and gains first strike until end of turn.',
 1020: 'Pay 2 life: Glorifier of Dusk gains vigilance until end of turn.',
 1021: 'Whenever Goring Ceratops attacks, other creatures you control gain '
       'double strike until end of turn.',
 1027: 'Enchant creature',
 1040: '{o3oWoW}, Sacrifice Priest of the Wakening Sun: Search your library '
       'for a Dinosaur card, reveal it, put it into your hand, then shuffle '
       'your library.',
 1041: 'Pterodon Knight has flying as long as you control a Dinosaur.',
 1046: 'Exile all attacking creatures target player controls. That player may '
       'search their library for that many basic land cards, put those cards '
       'onto the battlefield tapped, then shuffle their library.',
 1055: '{oT}: Add one mana of any color.',
 1057: 'Draw two cards. Then discard a card unless you attacked with a '
       'creature this turn.',
 1063: "Return target creature to its owner's hand. Create a colorless "
       'Treasure artifact token with "{oT}, Sacrifice this artifact: Add one '
       'mana of any color."',
 1070: "Creatures you control with +1/+1 counters on them can't be blocked.",
 1071: '+1: Whenever one or more creatures you control deal combat damage to a '
       'player this turn, draw a card, then discard a card.',
 1073: '-2: Create a 2/2 blue Illusion creature token with "When this creature '
       'becomes the target of a spell, sacrifice it."',
 1076: 'Abilities your opponents activate that target a Merfolk you control '
       'cost {o2} more to activate.',
 1083: "Enchanted creature can't attack or block.",
 1106: 'At the beginning of combat on your turn, you may have target Vampire '
       'get +2/+0 until end of turn.',
 1126: 'Whenever Fathom Fleet Captain attacks, if you control another nontoken '
       'Pirate, you may pay {o2}. If you do, create a 2/2 black Pirate '
       'creature token with menace.',
 1127: 'When Fathom Fleet Cutthroat enters the battlefield, destroy target '
       'creature an opponent controls that was dealt damage this turn.',
 1129: 'Target opponent discards two cards. \n'
       '<i>Raid</i>  If you attacked with a creature this turn, create a '
       'colorless Treasure artifact token with "{oT}, Sacrifice this artifact: '
       'Add one mana of any color."',
 1130: 'When Kitesail Freebooter enters the battlefield, target opponent '
       'reveals their hand. You choose a noncreature, nonland card from it. '
       'Exile that card until Kitesail Freebooter leaves the battlefield.',
 1131: '{oT}: Add {oR} or {oG}.',
 1140: '<i>Raid</i>  At the beginning of your end step, if you attacked with a '
       'creature this turn, reveal the top card of your library and put that '
       "card into your hand. You lose life equal to the card's converted mana "
       'cost.',
 1152: '{oT}: Add {oC}.',
 1166: 'Firecannon Blast deals 3 damage to target creature. \n'
       '<i>Raid</i>  Firecannon Blast deals 6 damage to that creature instead '
       'if you attacked with a creature this turn.',
 1167: '{oT}: Add {oU} or {oB}.',
 1172: 'Whenever you cast a Pirate spell, untap Lightning-Rig Crew.',
 1176: 'Whenever another creature enters the battlefield, Rampaging Ferocidon '
       "deals 1 damage to that creature's controller.",
 1177: '<i>Enrage</i>  Whenever Raptor Hatchling is dealt damage, create a 3/3 '
       'green Dinosaur creature token with trample.',
 1193: 'Enchanted creature gets +2/+2 and has haste.',
 1195: 'At the beginning of your upkeep, exile the top card of your library. '
       "If it's a nonland card, you may cast that card this turn.",
 1196: 'Whenever you cast your third spell in a turn, you may transform '
       "Vance's Blasting Cannons.",
 1198: '{o2oR}, {oT}: Spitfire Bastion deals 3 damage to any target.',
 1203: '{oT}: Add {oG} or {oW}.',
 1206: 'Choose one   Destroy target creature with flying.  Destroy target '
       'enchantment.',
 1208: 'Whenever you cast a noncreature spell, put a +1/+1 counter on Deeproot '
       'Champion.',
 1209: '{oT}: Add {oW} or {oU}.',
 1210: 'Dragonskull Summit enters the battlefield tapped unless you control a '
       'Swamp or a Mountain.',
 1211: '{oT}: Add {oB} or {oR}.',
 1213: "Whenever Emperor's Vanguard deals combat damage to a player, it "
       'explores.',
 1226: 'When Old-Growth Dryads enters the battlefield, each opponent may '
       'search their library for a basic land card, put it onto the '
       'battlefield tapped, then shuffle their library.',
 1228: '<i>Enrage</i>  Whenever Ranging Raptors is dealt damage, you may '
       'search your library for a basic land card, put it onto the battlefield '
       'tapped, then shuffle your library.',
 1229: '<i>Enrage</i>  Whenever Ravenous Daggertooth is dealt damage, you gain '
       '2 life.',
 1230: '<i>Enrage</i>  Whenever Ripjaw Raptor is dealt damage, draw a card.',
 1250: 'Deadeye Plunderers gets +1/+1 for each artifact you control.',
 1258: '-X: Huatli, Warrior Poet deals X damage divided as you choose among '
       "any number of target creatures. Creatures dealt damage this way can't "
       'block this turn.',
 1268: 'Equip {o1}',
 1270: '-3: Destroy target artifact, creature, or enchantment. Create a '
       'colorless Treasure artifact token with "{oT}, Sacrifice this artifact: '
       'Add one mana of any color."',
 1273: "When Conqueror's Galleon attacks, exile it at end of combat, then "
       'return it to the battlefield transformed under your control.',
 1280: 'When Dowsing Dagger enters the battlefield, target opponent creates '
       'two 0/2 green Plant creature tokens with defender.',
 1289: 'Pirates you control get +1/+0.',
 1292: '{oT}: Add one mana of any color. Spend this mana only to cast a '
       'creature spell of the chosen type.',
 1306: 'At the beginning of your end step, if you control seven or more lands, '
       'transform Thaumatic Compass.',
 1308: '{o1}, {oT}: Scry 1. Put a landmark counter on Treasure Map. Then if '
       'there are three or more landmark counters on it, remove those '
       'counters, transform Treasure Map, and create three colorless Treasure '
       'artifact tokens with "{oT}, Sacrifice this artifact: Add one mana of '
       'any color."',
 1319: 'Equip {o2}',
 1323: '+1: Draw a card.',
 1545: '{o4}, {oT}: Draw a card.',
 1570: 'Enchant land',
 1586: 'You gain 4 life.',
 1633: '{o2}, {oT}: Draw a card, then discard a card.',
 1640: 'You have no maximum hand size.',
 1691: 'Destroy target artifact or land.',
 1962: '{o1}, {oT}: Add one mana of any color.',
 2075: 'Creatures you control with flying get +1/+1.',
 2091: '{oT}, Discard a card: Draw a card.',
 2200: 'Unfriendly Fire deals 4 damage to any target.',
 2452: 'Enchanted creature gets +2/+2 and has flying.',
 2848: 'Equipped creature gets +2/+1.',
 2873: 'Equipped creature gets +1/+0.',
 2904: 'Whenever an opponent discards a card, that player loses 2 life.',
 4247: '{oT}: Add {oR} or {oW}.',
 4663: 'Destroy target attacking creature.',
 4762: 'Equipped creature has flying.',
 4776: 'Target creature gets +3/+3 and gains trample until end of turn.',
 4957: '{oT}: Add three mana of any one color.',
 5887: 'Destroy target land. Its controller loses 2 life.',
 6266: '{oT}: Untap target land.',
 13402: 'Destroy target creature with power 4 or greater.',
 13428: '{oT}: Add {oG} for each creature you control.',
 15027: 'Whenever a creature dies, you gain 1 life.',
 15979: 'Creatures your opponents control enter the battlefield tapped.',
 17253: 'Counter target spell unless its controller pays {o4}.',
 18504: '{oT}: Add {oG} or {oU}.',
 19189: 'Enchanted creature gets +2/+2 and has lifelink.',
 19445: 'Instant and sorcery spells you cast cost {o1} less to cast.',
 20207: 'Put a +1/+1 counter on target creature you control. Then that '
        "creature fights target creature you don't control.",
 20452: '{o1oB}, Pay 2 life: Draw a card.',
 20997: "When Ixalan's Binding enters the battlefield, exile target nonland "
        "permanent an opponent controls until Ixalan's Binding leaves the "
        'battlefield.',
 21775: 'Target opponent reveals their hand. You choose a noncreature, nonland '
        'card from it. That player discards that card.',
 23606: 'Destroy target enchantment.',
 23607: 'Draw two cards.',
 25846: 'Counter target spell.',
 25848: 'Draw a card.',
 30062: 'Counter target noncreature spell unless its controller pays {o2}.',
 61077: 'Each creature you control assigns combat damage equal to its '
        'toughness rather than its power.',
 61119: 'Enchanted land has "{oT}: Add two mana of any one color."',
 61160: 'Target creature you control gets +0/+3 and gains hexproof until end '
        'of turn.',
 61990: 'Destroy target creature with power 3 or less.',
 62292: '{oT}: Lightning-Rig Crew deals 1 damage to each opponent.',
 62969: "Storm Sculptor can't be blocked.",
 66937: 'Scry 1.',
 70361: 'Repeating Barrage deals 3 damage to any target.',
 76420: 'Gain control of target artifact or creature until end of turn. Untap '
        'it. It gains haste until end of turn.',
 76515: 'Crew 3',
 76556: 'Crew 1',
 76611: 'Crew 4',
 76645: 'Crew 2',
 76735: 'Stone Quarry enters the battlefield tapped.',
 76748: '{o3oG}: Put a +1/+1 counter on Jungle Delver.',
 76869: 'Spike-Tailed Ceratops can block an additional creature each combat.',
 76874: 'When Watertrap Weaver enters the battlefield, tap target creature an '
        "opponent controls. That creature doesn't untap during its "
        "controller's next untap step.",
 76882: 'As Unclaimed Territory enters the battlefield, choose a creature '
        'type.',
 86476: "Headstrong Brute can't block.",
 86621: "Elaborate Firecannon doesn't untap during your untap step.",
 86635: "Tishana, Voice of Thunder's power and toughness are each equal to the "
        'number of cards in your hand.',
 86918: 'Dreamcaller Siren can block only creatures with flying.',
 87893: 'When Storm Sculptor enters the battlefield, return a creature you '
        "control to its owner's hand.",
 87894: "Bonded Horncrest can't attack or block alone.",
 88126: '{o1oR}: Fathom Fleet Firebrand gets +1/+0 until end of turn.',
 88132: 'When Pious Interdiction enters the battlefield, you gain 2 life.',
 88178: "Enchanted creature doesn't untap during its controller's untap step.",
 88194: "Activated abilities of sources with the chosen name can't be "
        "activated unless they're mana abilities.",
 88604: 'When Inspiring Cleric enters the battlefield, you gain 4 life.',
 88861: 'Whenever Fell Flagship deals combat damage to a player, that player '
        'discards a card.',
 89789: "When Castaway's Despair enters the battlefield, tap enchanted "
        'creature.',
 91717: 'When Sentinel Totem enters the battlefield, scry 1.',
 91870: "When Hierophant's Chalice enters the battlefield, target opponent "
        'loses 1 life and you gain 1 life.',
 91993: 'Rootbound Crag enters the battlefield tapped unless you control a '
        'Mountain or a Forest.',
 92859: 'Glacial Fortress enters the battlefield tapped unless you control a '
        'Plains or an Island.',
 92868: 'Drowned Catacomb enters the battlefield tapped unless you control an '
        'Island or a Swamp.',
 92880: 'Sunpetal Grove enters the battlefield tapped unless you control a '
        'Forest or a Plains.',
 92939: "Players can't gain life.",
 93248: '{oT}, Sacrifice a creature: You gain life equal to the sacrificed '
        "creature's toughness.",
 94573: '{oB}: Skittering Heartstopper gains deathtouch until end of turn.',
 95354: 'As an additional cost to cast this spell, sacrifice an artifact or '
        'creature.',
 95397: "Creatures entering the battlefield don't cause abilities to trigger.",
 95596: 'Dark Nourishment deals 3 damage to any target. You gain 3 life.',
 99121: 'Whenever Vicious Conquistador attacks, each opponent loses 1 life.',
 99356: "Target creature you control fights target creature you don't control.",
 99791: 'Slash of Talons deals 2 damage to target attacking or blocking '
        'creature.',
 100164: 'Whenever Daring Saboteur deals combat damage to a player, you may '
         'draw a card. If you do, discard a card.',
 100782: "{o2oU}: Daring Saboteur can't be blocked this turn.",
 101377: 'Pay 2 life: Glorifier of Dusk gains flying until end of turn.',
 101515: '<i>Raid</i>  When Deadeye Tormentor enters the battlefield, if you '
         'attacked with a creature this turn, target opponent discards a card.',
 101552: '<i>Raid</i>  Rigging Runner enters the battlefield with a +1/+1 '
         'counter on it if you attacked with a creature this turn.',
 101825: 'When New Horizons enters the battlefield, put a +1/+1 counter on '
         'target creature you control.',
 102907: 'Dual Shot deals 1 damage to each of up to two target creatures.',
 103200: 'When Growing Rites of Itlimoc enters the battlefield, look at the '
         'top four cards of your library. You may reveal a creature card from '
         'among them and put it into your hand. Put the rest on the bottom of '
         'your library in any order.',
 116729: 'Create two 1/1 white Vampire creature tokens with lifelink.',
 116730: 'Dinosaur spells you cast cost {o1} less to cast.',
 116731: "Your opponents can't cast spells with the same name as the exiled "
         'card.',
 116732: 'Whenever a creature you control explores, target creature an '
         'opponent controls gets -2/-2 until end of turn.',
 116733: 'Choose one   Return target creature card from your graveyard to your '
         'hand.  Return two target Pirate cards from your graveyard to your '
         'hand.',
 116734: '<i>Raid</i>  At the beginning of your end step, if you attacked with '
         'a creature this turn, target opponent discards a card.',
 116735: 'Whenever a creature an opponent controls dies, create a colorless '
         'Treasure artifact token with "{oT}, Sacrifice this artifact: Add one '
         'mana of any color."',
 116736: 'Creatures you control get +1/+1 until end of turn. Untap them.',
 116737: '{o2oB}, Sacrifice a creature: Create two colorless Treasure artifact '
         'tokens with "{oT}, Sacrifice this artifact: Add one mana of any '
         'color."',
 116738: 'Sacrifice three Treasures: Draw a card.',
 116739: 'Whenever a Vampire you control attacks, each opponent loses 1 life '
         'and you gain 1 life.',
 116740: 'Until end of turn, target creature you control gets +1/+1 and target '
         'creature an opponent controls gets -1/-1.',
 116741: "When Burning Sun's Avatar enters the battlefield, it deals 3 damage "
         'to target opponent or planeswalker and 3 damage to up to one target '
         'creature.',
 116742: 'Target creature gains indestructible until end of turn. Scry 1.',
 116743: 'Fiery Cannonade deals 2 damage to each non-Pirate creature.',
 116744: '{o7oR}, {oT}, Sacrifice Fire Shrine Keeper: It deals 3 damage to '
         'each of up to two target creatures.',
 116745: 'Rile deals 1 damage to target creature you control. That creature '
         'gains trample until end of turn.',
 116746: 'As long as you control another Dinosaur, Thrash of Raptors gets '
         '+2/+0 and has trample.',
 116747: "Whenever Tilonalli's Knight attacks, if you control a Dinosaur, "
         "Tilonalli's Knight gets +1/+1 until end of turn.",
 116748: "Whenever Tilonalli's Skinshifter attacks, it becomes a copy of "
         'another target nonlegendary attacking creature until end of turn.',
 116749: 'Each opponent must attack you or a planeswalker you control with at '
         'least one creature each combat if able.',
 116750: "Target creature gets +2/+2 until end of turn. If it's a Vampire, it "
         'gains first strike until end of turn.',
 116751: "When Wakening Sun's Avatar enters the battlefield, if you cast it "
         'from your hand, destroy all non-Dinosaur creatures.',
 116752: 'Prevent all damage that would be dealt to creatures this turn. '
         'Creatures you control gain hexproof until end of turn.',
 116753: 'Look at the top five cards of your library. You may reveal a '
         'Dinosaur or land card from among them and put it into your hand. Put '
         'the rest on the bottom of your library in any order.',
 116755: 'Whenever Deeproot Warrior becomes blocked, it gets +1/+1 until end '
         'of turn.',
 116756: 'Drover of the Mighty gets +2/+2 as long as you control a Dinosaur.',
 116757: 'Creatures you control are the chosen type in addition to their other '
         'types. The same is true for creature spells you control and creature '
         "cards you own that aren't on the battlefield.",
 116758: 'When Legion Conquistador enters the battlefield, you may search your '
         'library for any number of cards named Legion Conquistador, reveal '
         'them, put them into your hand, then shuffle your library.',
 116759: 'At the beginning of your end step, if you control four or more '
         'creatures, transform Growing Rites of Itlimoc.',
 116760: "{o7oG}, {oT}, Sacrifice Ixalli's Keeper: Target creature gets +5/+5 "
         'and gains trample until end of turn.',
 116761: 'When Jade Guardian enters the battlefield, put a +1/+1 counter on '
         'target Merfolk you control.',
 116762: "Kumena's Speaker gets +1/+1 as long as you control another Merfolk "
         'or an Island.',
 116763: 'This spell costs {o2} less to cast if it targets a Dinosaur you '
         'control.',
 116764: 'Whenever a creature you control becomes the target of a spell or '
         'ability an opponent controls, you may draw a card.',
 116765: '<i>Enrage</i>  Whenever Snapping Sailback is dealt damage, put a '
         '+1/+1 counter on it.',
 116766: 'Other Dinosaurs you control get +1/+1.',
 116767: '{o5oG}: Create a 3/3 green Dinosaur creature token with trample.',
 116768: 'When Deadeye Quartermaster enters the battlefield, you may search '
         'your library for an Equipment or Vehicle card, reveal it, put it '
         'into your hand, then shuffle your library.',
 116769: 'Put a +1/+1 counter on target creature and a +1/+1 counter on up to '
         'one target Merfolk.',
 116770: '{oXoGoG}: Put X +1/+1 counters on target land you control. That land '
         "becomes a 0/0 Elemental creature with haste. It's still a land.",
 116771: 'Whenever a creature you control explores, put a +1/+1 counter on '
         'Wildgrowth Walker and you gain 3 life.',
 116772: 'Other Pirates you control get +1/+1.',
 116773: 'Whenever you cast a Merfolk spell, create a 1/1 blue Merfolk '
         'creature token with hexproof.',
 116774: 'Create three 1/1 white Vampire creature tokens with lifelink.',
 116777: "Whenever Gishath, Sun's Avatar deals combat damage to a player, "
         'reveal that many cards from the top of your library. Put any number '
         'of Dinosaur creature cards from among them onto the battlefield and '
         'the rest on the bottom of your library in a random order.',
 116780: '0: Create a 3/3 green Dinosaur creature token with trample.',
 116781: 'When Raging Swordtooth enters the battlefield, it deals 1 damage to '
         'each other creature.',
 116782: 'Other Dinosaurs you control have haste.',
 116783: 'When Regisaur Alpha enters the battlefield, create a 3/3 green '
         'Dinosaur creature token with trample.',
 116784: '{o3oG}: Put a +1/+1 counter on target creature.',
 116785: '{o2oU}, Remove a +1/+1 counter from a creature you control: Draw a '
         'card.',
 116786: '{oT}, Pay 7 life: Destroy target nonland permanent. Activate this '
         'ability only during your turn.',
 116787: '+2: Create a 2/2 black Pirate creature token with menace.',
 116788: 'When Paladin of the Bloodstained enters the battlefield, create a '
         '1/1 white Vampire creature token with lifelink.',
 116790: 'When Dreamcaller Siren enters the battlefield, if you control '
         'another Pirate, tap up to two target nonland permanents.',
 116791: '{o6}, {oT}: Return target card from your graveyard to your hand.',
 116792: 'Whenever equipped creature deals combat damage to a player, you may '
         'transform Dowsing Dagger.',
 116793: 'Gain control of target creature with converted mana cost X.',
 116794: '{o4}, {oT}: Elaborate Firecannon deals 2 damage to any target.',
 116795: 'At the beginning of your upkeep, you may discard a card. If you do, '
         'untap Elaborate Firecannon.',
 116796: "When Pirate's Cutlass enters the battlefield, attach it to target "
         'Pirate you control.',
 116797: 'Whenever Fleet Swallower attacks, target player puts the top half of '
         'their library, rounded up, into their graveyard.',
 116798: '{oT}: Add one mana of any color. When that mana is spent to cast an '
         'instant or sorcery spell, copy that spell and you may choose new '
         'targets for the copy.',
 116799: 'Whenever equipped creature deals combat damage to a player, create a '
         'colorless Treasure artifact token with "{oT}, Sacrifice this '
         'artifact: Add one mana of any color."',
 116800: '{oT}, Exile Sentinel Totem: Exile all cards from all graveyards.',
 116801: "When you attack with three or more creatures, transform Legion's "
         'Landing.',
 116802: 'Until end of turn, target creature gains "When this creature dies, '
         'return it to its owner\'s hand."',
 116803: '{o3}, {oT}: Search your library for a basic land card, reveal it, '
         'put it into your hand, then shuffle your library.',
 116804: "Whenever Verdant Sun's Avatar or another creature enters the "
         'battlefield under your control, you gain life equal to that '
         "creature's toughness.",
 116805: 'Creatures you control of the chosen type get +1/+1.',
 116806: 'Whenever you cast a creature spell of the chosen type, draw a card.',
 116807: 'When this creature becomes the target of a spell, sacrifice it.',
 116808: 'When Vineshaper Mystic enters the battlefield, put a +1/+1 counter '
         'on each of up to two target Merfolk you control.',
 116809: '{o2}, {oT}, Sacrifice Field of Ruin: Destroy target nonbasic land an '
         'opponent controls. Each player searches their library for a basic '
         'land card, puts it onto the battlefield, then shuffles their '
         'library.',
 116811: '-5: Create two tokens that are copies of Jace, Cunning Castaway, '
         "except they're not legendary.",
 116812: 'Spells your opponents cast that target a Merfolk you control cost '
         '{o2} more to cast.',
 116813: 'At the beginning of your end step, gain control of target nonland '
         'permanent controlled by a player who was dealt combat damage by '
         'three or more Pirates this turn.',
 116814: 'This spell costs {o1} less to cast if you control a Pirate.',
 116815: '{o2oW}, {oT}: Create a 1/1 white Vampire creature token with '
         'lifelink.',
 116816: 'Target player draws seven cards.',
 116817: 'Whenever Dire Fleet Captain attacks, it gets +1/+1 until end of turn '
         'for each other attacking Pirate.',
 116818: "Return target nonland permanent you don't control to its owner's "
         'hand. If its converted mana cost was 2 or less, scry 2.',
 116819: 'Draw two cards. Create a colorless Treasure artifact token with '
         '"{oT}, Sacrifice this artifact: Add one mana of any color."',
 116820: 'When Prosperous Pirates enters the battlefield, create two colorless '
         'Treasure artifact tokens with "{oT}, Sacrifice this artifact: Add '
         'one mana of any color."',
 116821: 'Whenever one or more nontoken Vampires you control attack, create a '
         '1/1 white Vampire creature token with lifelink.',
 116822: 'Whenever another Merfolk enters the battlefield under your control, '
         'River Sneak gets +1/+1 until end of turn.',
 116823: 'Return all nonland permanents target player controls to their '
         "owner's hand.",
 116824: '<i>Raid</i>  At the beginning of your end step, if you attacked with '
         'a creature this turn, you may draw a card. If you do, discard a '
         'card.',
 116825: "Put target artifact or creature on top of its owner's library.",
 116826: 'When Wily Goblin enters the battlefield, create a colorless Treasure '
         'artifact token with "{oT}, Sacrifice this artifact: Add one mana of '
         'any color."',
 116827: 'At the beginning of your upkeep, look at the top card of your '
         'library. You may put it into your graveyard. Then if you have seven '
         'or more cards in your graveyard, you may transform Search for '
         'Azcanta.',
 116828: '{o2oU}, {oT}: Look at the top four cards of your library. You may '
         'reveal a noncreature, nonland card from among them and put it into '
         'your hand. Put the rest on the bottom of your library in any order.',
 116829: 'Shaper Apprentice has flying as long as you control another Merfolk.',
 116830: '<i>Raid</i>  When Shipwreck Looter enters the battlefield, if you '
         'attacked with a creature this turn, you may draw a card. If you do, '
         'discard a card.',
 116831: '{o7oU}, {oT}, Sacrifice Shore Keeper: Draw three cards.',
 116832: 'When Tishana enters the battlefield, draw a card for each creature '
         'you control.',
 116833: '{oU}, Sacrifice Siren Stormtamer: Counter target spell or ability '
         'that targets you or a creature you control.',
 116834: 'Exile target creature you control, then return that card to the '
         "battlefield under its owner's control. If a Pirate was exiled this "
         'way, draw a card.',
 116835: '{oT}: Target Dinosaur gains haste until end of turn.',
 116836: 'Counter target spell. Create X colorless Treasure artifact tokens, '
         'where X is that spell\'s converted mana cost. They have "{oT}, '
         'Sacrifice this artifact: Add one mana of any color."',
 116837: "-10: Target player's life total becomes 1.",
 116838: '<i>Raid</i>  When Storm Fleet Spy enters the battlefield, if you '
         'attacked with a creature this turn, draw a card.',
 116839: 'When Tempest Caller enters the battlefield, tap all creatures target '
         'opponent controls.',
 116840: 'At the beginning of your upkeep, you may reveal a Dinosaur card from '
         'your hand. If you do, you gain 2 life.',
 116841: 'At the beginning of your upkeep, if you have 5 or less life, you may '
         "transform Arguel's Blood Fast.",
 116842: 'When Bishop of the Bloodstained enters the battlefield, target '
         'opponent loses 1 life for each Vampire you control.',
 116843: '{o7oB}, {oT}, Sacrifice Blight Keeper: Target opponent loses 4 life '
         'and you gain 4 life.',
 116844: 'Bloodcrazed Paladin enters the battlefield with a +1/+1 counter on '
         'it for each creature that died this turn.',
 116845: 'Exile up to five target creature cards from graveyards. An opponent '
         'separates those cards into two piles. Put all cards from the pile of '
         'your choice onto the battlefield under your control and the rest '
         "into their owners' graveyards.",
 116846: 'Destroy target creature. Create two colorless Treasure artifact '
         'tokens with "{oT}, Sacrifice this artifact: Add one mana of any '
         'color."',
 116847: 'Target creature gets +5/+5 until end of turn and must be blocked '
         'this turn if able.',
 116848: "{o1oB}, {oT}: Exile two target cards from an opponent's graveyard. "
         'Deadeye Tracker explores.',
 116849: 'Tap three untapped Vampires you control: Return Deathless Ancient '
         'from your graveyard to your hand.',
 116850: "Desperate Castaways can't attack unless you control an artifact.",
 116851: 'When Dire Fleet Hoarder dies, create a colorless Treasure artifact '
         'token with "{oT}, Sacrifice this artifact: Add one mana of any '
         'color."',
 116852: 'When Dire Fleet Ravager enters the battlefield, each player loses a '
         'third of their life, rounded up.',
 116853: 'Whenever you cast an instant or sorcery spell, put a charge counter '
         'on Primal Amulet. Then if there are four or more charge counters on '
         'it, you may remove those counters and transform it.',
 116854: 'Return a Pirate card from your graveyard to your hand, then do the '
         'same for Vampire, Dinosaur, and Merfolk.',
 116855: 'Whenever a creature you control explores, put a +1/+1 counter on '
         'Shadowed Caravel.',
 116856: "As Sorcerous Spyglass enters the battlefield, look at an opponent's "
         'hand, then choose any card name.',
 116857: 'You gain twice X life. Put Sanguine Sacrament on the bottom of its '
         "owner's library.",
 116858: '{oT}: Untap target attacking creature an opponent controls and '
         'remove it from combat.',
 116859: '{oT}, Sacrifice a Treasure: Draw a card.',
 116860: 'At the beginning of your upkeep, if you control ten or more '
         'Treasures, you win the game.',
 116861: 'Reveal the top three cards of your library. For each of those cards, '
         'put that card into your hand unless any opponent pays 3 life. Then '
         'exile the rest.',
 116862: 'Exile target creature or planeswalker. You gain 2 life.',
 116863: 'Destroy target non-Merfolk creature.',
 116864: 'When Wanted Scoundrels dies, target opponent creates two colorless '
         'Treasure artifact tokens with "{oT}, Sacrifice this artifact: Add '
         'one mana of any color."',
 116865: 'If a source you control would deal damage to a permanent or player, '
         'it deals double that damage to that permanent or player instead.',
 116866: '{o1oW}, {oT}: Steadfast Armasaur deals damage equal to its toughness '
         'to target creature blocking or blocked by it.',
 116867: 'Whenever Captain Lannery Storm attacks, create a colorless Treasure '
         'artifact token with "{oT}, Sacrifice this artifact: Add one mana of '
         'any color."',
 116868: 'Whenever you sacrifice a Treasure, Captain Lannery Storm gets +1/+0 '
         'until end of turn.',
 116869: '{o3oR}: Gain control of target creature an opponent controls until '
         'end of turn. Untap that creature. It gains haste until end of turn. '
         'Activate this ability only any time you could cast a sorcery.',
 116870: 'Whenever Territorial Hammerskull attacks, tap target creature an '
         'opponent controls.',
 116871: 'Attacking creatures get +2/+0 until end of turn. Dinosaurs you '
         'control gain trample until end of turn.',
 116872: 'Headstrong Brute has menace as long as you control another Pirate.',
 116873: 'When Atzocan Archer enters the battlefield, you may have it fight '
         'another target creature.',
 116874: '{o1}, Sacrifice an artifact or creature: Makeshift Munitions deals 1 '
         'damage to any target.',
 116876: 'When Rowdy Crew enters the battlefield, draw three cards, then '
         'discard two cards at random. If two cards that share a card type are '
         'discarded this way, put two +1/+1 counters on Rowdy Crew.',
 116877: 'Destroy target land. Star of Extinction deals 20 damage to each '
         'creature and each planeswalker.',
 116878: '<i>Raid</i>  When Storm Fleet Arsonist enters the battlefield, if '
         'you attacked with a creature this turn, target opponent sacrifices a '
         'permanent.',
 116880: 'Whenever you cast a spell from your hand, reveal the top X cards of '
         "your library, where X is that spell's converted mana cost. You may "
         'cast a card revealed this way with converted mana cost X or less '
         'without paying its mana cost. Put the rest on the bottom of your '
         'library in a random order.',
 116881: 'Pay 4 life: Adanto Vanguard gains indestructible until end of turn.',
 116882: "Players can't cast spells from graveyards or activate abilities of "
         'cards in graveyards.',
 116883: 'Whenever Bishop of Rebirth attacks, you may return target creature '
         'card with converted mana cost 3 or less from your graveyard to the '
         'battlefield.',
 116884: 'At the beginning of your end step, create a colorless Treasure '
         'artifact token with "{oT}, Sacrifice this artifact: Add one mana of '
         'any color."',
 116885: '{oW}, {oT}: Target attacking Vampire gets +1/+1 until end of turn.',
 116886: "When Tishana's Wayfinder enters the battlefield, it explores.",
 116887: '{o7oW}, {oT}, Sacrifice Encampment Keeper: Creatures you control get '
         '+2/+2 until end of turn.',
 116888: 'When Imperial Aerosaur enters the battlefield, another target '
         'creature you control gets +1/+1 and gains flying until end of turn.',
 116889: 'Imperial Lancer has double strike as long as you control a Dinosaur.',
 116895: '<i>Raid</i>  {o3oRoR}: Return Repeating Barrage from your graveyard '
         'to your hand. Activate this ability only if you attacked with a '
         'creature this turn.',
 116897: 'Whenever Deathgorge Scavenger enters the battlefield or attacks, you '
         'may exile target card from a graveyard. If a creature card is exiled '
         'this way, you gain 2 life. If a noncreature card is exiled this way, '
         'Deathgorge Scavenger gets +1/+1 until end of turn.',
 116898: '{o2oUoB}: Create a colorless Treasure artifact token with "{oT}, '
         'Sacrifice this artifact: Add one mana of any color."',
 116899: '+1: Untap all creatures you control.',
 116900: "Return up to two target creatures to their owner's hand.",
 116901: 'Search your library and/or graveyard for a card named Jace, '
         'Ingenious Mind-Mage, reveal it, and put it into your hand. If you '
         'searched your library this way, shuffle it.',
 116902: "As long as you control a Jace planeswalker, Jace's Sentinel gets "
         "+1/+0 and can't be blocked.",
 116903: '+2: Put two +1/+1 counters on up to one target Dinosaur you control.',
 116904: '-3: Target Dinosaur you control deals damage equal to its power to '
         "target creature you don't control.",
 116905: '-7: Dinosaurs you control get +4/+4 until end of turn.',
 116906: 'Target creature gets +2/+0 until end of turn. If you control a '
         'Huatli planeswalker, that creature gets +4/+0 until end of turn '
         'instead.',
 116907: '-9: Gain control of up to three target creatures.',
 116908: 'When Sun-Blessed Mount enters the battlefield, you may search your '
         'library and/or graveyard for a card named Huatli, Dinosaur Knight, '
         'reveal it, then put it into your hand. If you searched your library '
         'this way, shuffle it.',
 118521: 'When Hostage Taker enters the battlefield, exile another target '
         'creature or artifact until Hostage Taker leaves the battlefield. You '
         'may cast that card for as long as it remains exiled, and you may '
         'spend mana as though it were mana of any type to cast that spell.',
 118593: '<i>Raid</i>  When Storm Fleet Pyromancer enters the battlefield, if '
         'you attacked with a creature this turn, Storm Fleet Pyromancer deals '
         '2 damage to any target.',
 118594: '<i>Enrage</i>  Whenever Sun-Crowned Hunters is dealt damage, it '
         'deals 3 damage to target opponent or planeswalker.',
 118786: '+2: You gain life equal to the greatest power among creatures you '
         'control.',
 119572: '{oT}, Sacrifice this artifact: Add one mana of any color.',
 120287: "This spell can't be countered.",
 120290: 'Destroy target artifact or enchantment.',
 120995: '<i>Raid</i>  At the beginning of your end step, if you attacked with '
         'a creature this turn, target opponent puts the top four cards of '
         'their library into their graveyard.'}
