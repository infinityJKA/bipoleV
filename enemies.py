from numpy import Inf
import equipment
class Enemy:
    def __init__(self,
    DisplayName = "DISPLAY NAME",
    Moves = [],
    Weakness = ["Fists"],
    Sprite = "",
    Level = 1,
    EXP = 200,
    Gold = 75,
    ATK = 150,
    MAG = 200,
    HLG = 100,
    DEF = 100,
    RES = 100,
    Current_HP = 300,
    Max_HP = 300,
    Current_SP = 100,
    Max_SP = 100,
    Bio = "this is the default bio",
    Effects = [],
    Max_Action_Count = 1,
    Current_Action_Count = 0,
    ):
        self.DisplayName = DisplayName
        self.Moves = Moves
        self.Weakness = Weakness
        self.Sprite = Sprite
        self.Level = Level
        self.EXP = EXP
        self.Gold = Gold
        self.ATK = ATK
        self.MAG = MAG
        self.HLG = HLG
        self.DEF = DEF
        self.RES = RES
        self.Current_HP = Current_HP
        self.Max_HP = Max_HP
        self.Current_SP = Current_SP
        self.Max_SP = Max_SP
        self.Bio = Bio
        self.Effects = Effects
        self.Max_Action_Count = Max_Action_Count
        self.Current_Action_Count = Current_Action_Count

if True: #Slime Forest Enemies
    Red_Slime_A = Enemy(
        DisplayName = "Red Slime A",
        Moves = [[equipment.Slam,0,100]],
        Weakness = ["Lance","Water"],
        Sprite = "red_slime",
        Level = 1,
        EXP = 250,
        Gold = 75,
        ATK = 100,
        MAG = 75,
        HLG = 10,
        DEF = 100,
        RES = 100,
        Max_HP = 300,
        Current_SP = 100,
        Max_SP = 100,
        Bio = "A basic red slime",
        Effects = []
    )
    Red_Slime_B = Enemy(
        DisplayName = "Red Slime B",
        Moves = [[equipment.Slam,0,100]],
        Weakness = ["Lance","Water"],
        Sprite = "red_slime",
        Level = 1,
        EXP = 250,
        Gold = 75,
        ATK = 100,
        MAG = 75,
        HLG = 10,
        DEF = 100,
        RES = 100,
        Max_HP = 300,
        Current_SP = 100,
        Max_SP = 100,
        Bio = "A basic red slime",
        Effects = []
    )
    Red_Slime_C = Enemy(
        DisplayName = "Red Slime C",
        Moves = [[equipment.Slam,0,100]],
        Weakness = ["Lance","Water"],
        Sprite = "red_slime",
        Level = 1,
        EXP = 250,
        Gold = 75,
        ATK = 100,
        MAG = 75,
        HLG = 10,
        DEF = 100,
        RES = 100,
        Max_HP = 300,
        Current_SP = 100,
        Max_SP = 100,
        Bio = "A basic red slime",
        Effects = []
    )
    Skull_Slime_A = Enemy(
        DisplayName = "Skull Slime A",
        Moves = [[equipment.Bite,0,100]],
        Weakness = ["Fists","Ice"],
        Sprite = "skull_slime",
        Level = 1,
        EXP = 275,
        Gold = 75,
        ATK = 100,
        MAG = 50,
        HLG = 5,
        DEF = 150,
        RES = 100,
        Max_HP = 350,
        Current_SP = 100,
        Max_SP = 100,
        Bio = "A slime with a strange skull",
        Effects = []
    )
    Mana_Fungus_A = Enemy(
        DisplayName = "Mana Fungus A",
        Moves = [[equipment.Energize,0,100],[equipment.Healing_Spores,0,100]],
        Weakness = ["Sword","Staff"],
        Sprite = "mana_fungus",
        Level = 1,
        EXP = 275,
        Gold = 75,
        ATK = 25,
        MAG = 25,
        HLG = 12,
        DEF = 150,
        RES = 100,
        Max_HP = 200,
        Current_SP = 100,
        Max_SP = 100,
        Bio = "It's a fungus",
        Effects = []
    )

    Funky_Fungus = Enemy(
        DisplayName = "Funky Fungus",
        Moves = [[equipment.Fungal_Thorns,0,100],[equipment.Funky_Dance,0,100]],
        Weakness = ["Bow","Staff","Fire"],
        Sprite = "funky_fungus",
        Level = 3,
        EXP = 300,
        Gold = 250,
        ATK = 150,
        MAG = 150,
        HLG = 12,
        DEF = 125,
        RES = 125,
        Max_HP = 15000,
        Current_SP = 200,
        Max_SP = 200,
        Bio = "A very funky fungus",
        Effects = []
    )

    Slimeinoid_A = Enemy(
        DisplayName = "Slimeinoid A",
        Moves = [[equipment.Fire_Breath,0,100],[equipment.Uppercut,0,100],[equipment.War_Cry,0,100]],
        Weakness = ["Sword","Water"],
        Sprite = "slimeinoid",
        Level = 2,
        EXP = 250,
        Gold = 80,
        ATK = 300,
        MAG = 300,
        HLG = 3,
        DEF = 185,
        RES = 150,
        Max_HP = 375,
        Current_SP = 525,
        Max_SP = 525,
        Bio = "A humanoid slime",
        Effects = [])

    Slimeinoid_B = Enemy(
        DisplayName = "Slimeinoid B",
        Moves = [[equipment.Fire_Breath,0,100],[equipment.Uppercut,0,100],[equipment.War_Cry,0,100]],
        Weakness = ["Sword","Water"],
        Sprite = "slimeinoid",
        Level = 2,
        EXP = 250,
        Gold = 80,
        ATK = 350,
        MAG = 300,
        HLG = 3,
        DEF = 185,
        RES = 150,
        Max_HP = 375,
        Current_SP = 525,
        Max_SP = 525,
        Bio = "A humanoid slime",
        Effects = [])

    Shufflin_Shrub_A = Enemy(
        DisplayName = "Shufflin Shrub A",
        Moves = [[equipment.Bingus_Energy_Wave,0,100],[equipment.Grassroots,0,100]],
        Weakness = ["Fists","Fire"],
        Sprite = "shufflinshrub",
        Level = 2,
        EXP = 225,
        Gold = 75,
        ATK = 300,
        MAG = 150,
        HLG = 13,
        DEF = 150,
        RES = 200,
        Max_HP = 325,
        Current_SP = 325,
        Max_SP = 325,
        Bio = "the j!?",
        Effects = [])

    Shufflin_Shrub_B = Enemy(
        DisplayName = "Shufflin Shrub B",
        Moves = [[equipment.Bingus_Energy_Wave,0,100],[equipment.Grassroots,0,100]],
        Weakness = ["Fists","Fire"],
        Sprite = "shufflinshrub",
        Level = 2,
        EXP = 225,
        Gold = 75,
        ATK = 300,
        MAG = 150,
        HLG = 13,
        DEF = 150,
        RES = 200,
        Max_HP = 325,
        Current_SP = 325,
        Max_SP = 325,
        Bio = "the j!?",
        Effects = [])

    Raging_Soul = Enemy(
        DisplayName = "Raging Soul",
        Moves = [[equipment.Abyssal_Inferno,0,100],[equipment.Fire_Breath,0,100],[equipment.Cursed_Prayer,0,100]],
        #Moves = [equipment.Fireball],#,equipment.Cut],
        Weakness = ["Bow","Water"],
        Sprite = "ragingsoul",
        Level = 5,
        EXP = 500,
        Gold = 500,
        ATK = 650,
        MAG = 650,
        HLG = 15,
        DEF = 150,
        RES = 150,
        Max_HP = 5500,
        Current_SP = 5500,
        Max_SP = 1500,
        Bio = "A raging soul haunting the forest",
        Effects = []
    )

if True: #Slime Forest Encounters
    #two_red_slimes = [Red_Slime_A,Red_Slime_B]
    #three_red_slimes = [Red_Slime_A,Red_Slime_B,Red_Slime_C]
    #single_red_slime = [[Red_Slime_A],"Normal"]
    sf1_encounter1 = [[Skull_Slime_A,Red_Slime_A,Red_Slime_B],"Normal"]
    sf1_encounter2 = [[Red_Slime_A,Mana_Fungus_A,Skull_Slime_A],"Normal"]
    sf1_encounter3 = [[Red_Slime_A,Red_Slime_B,Mana_Fungus_A],"Normal"]
    funky_fungus_encounter = [[Funky_Fungus],"Big"]
    sf2_encounter1 = [[Slimeinoid_A,Slimeinoid_B,Shufflin_Shrub_A],"Normal"]
    sf2_encounter2 = [[Shufflin_Shrub_A,Shufflin_Shrub_B,Slimeinoid_A],"Normal"]
    sf2_encounter3 = [[Shufflin_Shrub_A,Slimeinoid_A,Skull_Slime_A],"Normal"]
    raging_soul_boss = [[Raging_Soul,Shufflin_Shrub_A,Shufflin_Shrub_B],"Normal"]


if True: #Ruins of Time Enemies
    Gyrobifastigium_A = Enemy(
        DisplayName = "Gyrobifastigium A",
        Moves = [[equipment.Three_Space,0,100],[equipment.Prismatic_Honeycomb,0,100],[equipment.Geom_Strike,0,100]],
        Weakness = ["Staff","Water","Gun"],
        Sprite = "gyrobifastigium",
        Level = 4,
        EXP = 300,
        Gold = 150,
        ATK = 375,
        MAG = 375,
        HLG = 500,
        DEF = 350,
        RES = 400,
        Max_HP = 500,
        Max_SP = 750,
        Bio = "The truth, partically and not fully.\nYet still above us... the past...",
        Effects = []
    )

    Gyrobifastigium_B = Enemy(
        DisplayName = "Gyrobifastigium B",
        Moves = [[equipment.Three_Space,0,100],[equipment.Prismatic_Honeycomb,0,100],[equipment.Geom_Strike,0,100]],
        Weakness = ["Staff","Water","Gun"],
        Sprite = "gyrobifastigium",
        Level = 4,
        EXP = 300,
        Gold = 150,
        ATK = 375,
        MAG = 375,
        HLG = 500,
        DEF = 350,
        RES = 400,
        Max_HP = 500,
        Max_SP = 750,
        Bio = "The truth, partically and not fully.\nYet still above us... the past...",
        Effects = []
    )

    Gyrobifastigium_C = Enemy(
        DisplayName = "Gyrobifastigium C",
        Moves = [[equipment.Three_Space,0,100],[equipment.Prismatic_Honeycomb,0,100],[equipment.Geom_Strike,0,100]],
        Weakness = ["Staff","Water","Gun"],
        Sprite = "gyrobifastigium",
        Level = 4,
        EXP = 300,
        Gold = 150,
        ATK = 375,
        MAG = 375,
        HLG = 500,
        DEF = 350,
        RES = 400,
        Max_HP = 500,
        Max_SP = 750,
        Bio = "The truth, partically and not fully.\nYet still above us... the past...",
        Effects = []
    )

    Dodecahedron_A = Enemy(
        DisplayName = "Dodecahedron A",
        Moves = [[equipment.Convex_Polytope,0,100],[equipment.Stellation,0,100],[equipment.Geom_Strike,0,100]],
        Weakness = ["Lance","Ice","Gun"],
        Sprite = "dodecahedron",
        Level = 4,
        EXP = 325,
        Gold = 165,
        ATK = 375,
        MAG = 375,
        HLG = 500,
        DEF = 400,
        RES = 425,
        Max_HP = 650,
        Max_SP = 875,
        Bio = "Dodecahedron!!!",
        Effects = []
    )

    Dodecahedron_B = Enemy(
        DisplayName = "Dodecahedron B",
        Moves = [[equipment.Convex_Polytope,0,100],[equipment.Stellation,0,100],[equipment.Geom_Strike,0,100]],
        Weakness = ["Lance","Ice","Gun"],
        Sprite = "dodecahedron",
        Level = 4,
        EXP = 325,
        Gold = 165,
        ATK = 375,
        MAG = 375,
        HLG = 500,
        DEF = 400,
        RES = 425,
        Max_HP = 650,
        Max_SP = 875,
        Bio = "Dodecahedron!!!",
        Effects = []
    )

    Eratosthenesoid_A = Enemy(
        DisplayName = "Eratosthenesoid A",
        Moves = [[equipment.Polymath,75,100],[equipment.Global_Projection,0,75],[equipment.Prime_Sieve,50,100],[equipment.Geom_Strike,75,100]],
        Weakness = ["Fire","Gun"],
        Sprite = "eratosthenesoid",
        Level = 4,
        EXP = 350,
        Gold = 150,
        ATK = 850,
        MAG = 825,
        HLG = 900,
        DEF = 400,
        RES = 425,
        Max_HP = 1000,
        Max_SP = 1250,
        Bio = "Circumference.",
        Effects = []
    )

    Eratosthenesoid_B = Enemy(
        DisplayName = "Eratosthenesoid B",
        Moves = [[equipment.Polymath,75,100],[equipment.Global_Projection,0,75],[equipment.Prime_Sieve,50,100],[equipment.Geom_Strike,75,100]],
        Weakness = ["Fire","Gun"],
        Sprite = "eratosthenesoid",
        Level = 4,
        EXP = 350,
        Gold = 150,
        ATK = 850,
        MAG = 825,
        HLG = 900,
        DEF = 400,
        RES = 425,
        Max_HP = 1000,
        Max_SP = 1250,
        Bio = "Circumference.",
        Effects = []
    )

    Eratosthenesoid_C = Enemy(
        DisplayName = "Eratosthenesoid C",
        Moves = [[equipment.Polymath,75,100],[equipment.Global_Projection,0,75],[equipment.Prime_Sieve,50,100],[equipment.Geom_Strike,75,100]],
        Weakness = ["Fire","Gun"],
        Sprite = "eratosthenesoid",
        Level = 4,
        EXP = 350,
        Gold = 150,
        ATK = 850,
        MAG = 825,
        HLG = 900,
        DEF = 400,
        RES = 425,
        Max_HP = 1000,
        Max_SP = 1250,
        Bio = "Circumference.",
        Effects = []
    )

    Nynety = Enemy(
        DisplayName = "Nynety",
        Moves = [[equipment.Branching,98,100],[equipment.Dimensional_Reaction,98,100],[equipment.Nuclear_Fission,98,100],[equipment.Sine,75,97],[equipment.Cosine,75,97],[equipment.Tangent,25,75],[equipment.Reciprocal,25,75],[equipment.Fold,0,75],[equipment.Nontotient,0,75],[equipment.Solution,0,25],[equipment.Hyperbolic,0,25]],
        Weakness = ["Sword","Gun"],
        Sprite = "nynety",
        Level = 10,
        EXP = 600,
        Gold = 1000,
        ATK = 850,
        MAG = 825,
        HLG = 20,
        DEF = 400,
        RES = 425,
        Max_HP = 17500,
        Max_SP = 9001,
        Bio = "The most powerful Lesser Truth of the\nRuins of Time.",
        Effects = []
    )

if True: #Ruins of Time Encounters
    rot1_encounter1 = [[Gyrobifastigium_A,Gyrobifastigium_B,Gyrobifastigium_C],"Normal"]
    rot1_encounter2 = [[Dodecahedron_A,Gyrobifastigium_A,Gyrobifastigium_B],"Normal"]

    rot2_encounter1 = [[Eratosthenesoid_A,Dodecahedron_A,Dodecahedron_B],"Normal"]
    rot2_encounter2 = [[Eratosthenesoid_A,Dodecahedron_A,Gyrobifastigium_A],"Normal"]
    rot2_encounter3 = [[Eratosthenesoid_A,Gyrobifastigium_A,Gyrobifastigium_B],"Normal"]
    rot2_boss = [[Nynety,Gyrobifastigium_A,Gyrobifastigium_B],"Normal"]


if True: #Bandit Road Enemies
    Crazy_Guy_A = Enemy(
        DisplayName = "Crazy Guy A",
        Moves = [[equipment.Dagger,75,100],[equipment.Cut,0,75],[equipment.Stab,0,75],[equipment.Slash,0,25]],
        Weakness = ["Lance","Ice","Gun"],
        Sprite = "crazy_guy",
        Level = 7,
        EXP = 200,
        Gold = 175,
        ATK = 700,
        MAG = 600,
        HLG = 900,
        DEF = 300,
        RES = 200,
        Max_HP = 1350,
        Max_SP = 1250,
        Max_Action_Count = 3,
        Bio = "Don't ever mess with a\ncrazy guy.",
        Effects = []
    )

    Crazy_Guy_B = Enemy(
        DisplayName = "Crazy Guy B",
        Moves = [[equipment.Dagger,75,100],[equipment.Cut,0,75],[equipment.Stab,0,75],[equipment.Slash,0,25]],
        Weakness = ["Lance","Ice","Gun"],
        Sprite = "crazy_guy",
        Level = 7,
        EXP = 200,
        Gold = 175,
        ATK = 700,
        MAG = 600,
        HLG = 900,
        DEF = 300,
        RES = 200,
        Max_HP = 1350,
        Max_SP = 1250,
        Max_Action_Count = 3,
        Bio = "Don't ever mess with a\ncrazy guy.",
        Effects = []
    )

    Crazy_Guy_C = Enemy(
        DisplayName = "Crazy Guy C",
        Moves = [[equipment.Dagger,75,100],[equipment.Cut,0,75],[equipment.Stab,0,75],[equipment.Slash,0,25]],
        Weakness = ["Lance","Ice","Gun"],
        Sprite = "crazy_guy",
        Level = 7,
        EXP = 200,
        Gold = 175,
        ATK = 700,
        MAG = 600,
        HLG = 900,
        DEF = 300,
        RES = 200,
        Max_HP = 1350,
        Max_SP = 1250,
        Max_Action_Count = 3,
        Bio = "Don't ever mess with a\ncrazy guy.",
        Effects = []
    )

    Gangster_A = Enemy(
        DisplayName = "Gangster A",
        Moves = [[equipment.Fireball,66,100],[equipment.Freeze,33,66],[equipment.Bronze_Gauntlets,66,100],[equipment.Cut,33,66],[equipment.Sweep,0,33],[equipment.Flood,0,33]],
        Weakness = ["Staff","Fire","Bow"],
        Sprite = "gangster",
        Level = 7,
        EXP = 325,
        Gold = 350,
        ATK = 950,
        MAG = 875,
        HLG = 900,
        DEF = 600,
        RES = 525,
        Max_HP = 1500,
        Max_SP = 12500,
        Max_Action_Count = 1,
        Bio = "A gangster under Gangole, the leader\nof the Bandit Road Gang.",
        Effects = []
    )

    Gangster_B = Enemy(
        DisplayName = "Gangster B",
        Moves = [[equipment.Fireball,66,100],[equipment.Freeze,33,66],[equipment.Bronze_Gauntlets,66,100],[equipment.Cut,33,66],[equipment.Sweep,0,33],[equipment.Flood,0,33]],
        Weakness = ["Staff","Fire","Bow"],
        Sprite = "gangster",
        Level = 7,
        EXP = 325,
        Gold = 350,
        ATK = 950,
        MAG = 875,
        HLG = 900,
        DEF = 600,
        RES = 525,
        Max_HP = 1500,
        Max_SP = 12500,
        Max_Action_Count = 1,
        Bio = "A gangster under Gangole, the leader\nof the Bandit Road Gang.",
        Effects = []
    )

    Gangole = Enemy(
        DisplayName = "Gangole",
        Moves = [[equipment.Pew,98,100],[equipment.Spray,98,100],[equipment.Expensive_Cigar,95,98],[equipment.Pew,35,95],[equipment.Spray,35,95],[equipment.Expensive_Cigar,35,50],[equipment.Spinning_Chair,0,35],[equipment.Desperation_Shot,0,35],[equipment.Huffin,0,35]],
        Weakness = ["Fists","Lance","Staff","Ice","Gun"],
        Sprite = "gangole",
        Level = 9,
        EXP = 575,
        Gold = 2000,
        ATK = 900,
        MAG = 900,
        HLG = 25,
        DEF = 300,
        RES = 250,
        Max_HP = 25000,
        Max_SP = 69420,
        Bio = "Leader of the Bandit Road Gang, and\nwielder of The 22XX, an ancient\nweapon from the pre-Finis era.",
        Effects = []
    )

    Jeffy_Jimovans = Enemy(
        DisplayName = "Jeffy Jimovans",
        Moves = [[equipment.Bronze_Gauntlets,75,100],[equipment.Slash,0,75],[equipment.Stone_Staff,0,75],[equipment.Flood,0,25],[equipment.Long_Bow,0,25]],
        Weakness = ["Sword","Fire","Gun"],
        Sprite = "jeffy_jimovans",
        Level = 8,
        EXP = 500,
        Gold = 450,
        ATK = 750,
        MAG = 750,
        HLG = 900,
        DEF = 325,
        RES = 275,
        Max_HP = 1500,
        Max_SP = 1250,
        Max_Action_Count = 3,
        Bio = "Jeffy Jimovans is a high ranking member of the\nBandit Road Gang and has served the gang for\nmost of his life. He initally joined after he was\norphaned, rising through the ranks as a dedicated\nmember from a young age. He has developed a strong\nbrotherhood with Ersatz Humphrey, a fellow gang\nmember who he often hangs out with.",
        Effects = []
    )

    Ersatz_Humphrey = Enemy(
        DisplayName = "Ersatz Humphrey",
        Moves = [[equipment.Impair,98,100],[equipment.Mana_Thurst,98,100],[equipment.Screwdriver_of_Fate,50,98],[equipment.Life_Transfer,50,98],[equipment.Mana_Thurst,0,50],[equipment.Impair,0,15]],
        Weakness = ["Staff","Water"],
        Sprite = "ersatz_humphrey",
        Level = 8,
        EXP = 500,
        Gold = 500,
        ATK = 875,
        MAG = 875,
        HLG = 875,
        DEF = 400,
        RES = 425,
        Max_HP = 10000,
        Max_SP = 99999,
        Bio = "I really hope this guy gets a stupid\namount of lore after this battle.",
        Effects = []
    )

if True: #Bandit Road Encounters
    br_encounter1 = [[Crazy_Guy_A,Crazy_Guy_B,Crazy_Guy_C],"Normal"]
    br_encounter2 = [[Gangster_A,Crazy_Guy_A,Crazy_Guy_B],"Normal"]
    br_encounter3 = [[Crazy_Guy_A,Gangster_A,Gangster_B],"Normal"]
    br_boss = [[Gangole,Ersatz_Humphrey,Jeffy_Jimovans],"Normal"]


if True: #Ricefield Realm Enemies
    Point_Farmer_A = Enemy(
        DisplayName = "Point Farmer A",
        Moves = [[equipment.Pitchfork,0,100],[equipment.Irrigation,0,100],[equipment.Point_Harvest,0,99],[equipment.Bountiful,0,100]],
        Weakness = ["Staff","Bow","Ice","Gun"],
        Sprite = "point_farmer",
        Level = 9,
        EXP = 375,
        Gold = 425,
        ATK = 1100,
        MAG = 1025,
        HLG = 8,
        DEF = 725,
        RES = 650,
        Max_HP = 1500,
        Max_SP = 3500,
        Max_Action_Count = 1,
        Bio = "A simple point farmer, he harvests\npoints in the Ricefield Realm.",
        Effects = []
    )

    Point_Farmer_B = Enemy(
        DisplayName = "Point Farmer B",
        Moves = [[equipment.Pitchfork,0,100],[equipment.Irrigation,0,100],[equipment.Point_Harvest,0,100],[equipment.Bountiful,0,100]],
        Weakness = ["Staff","Bow","Ice","Gun"],
        Sprite = "point_farmer",
        Level = 9,
        EXP = 375,
        Gold = 425,
        ATK = 1100,
        MAG = 1025,
        HLG = 8,
        DEF = 725,
        RES = 650,
        Max_HP = 1500,
        Max_SP = 3500,
        Max_Action_Count = 1,
        Bio = "A simple point farmer, he harvests\npoints in the Ricefield Realm.",
        Effects = []
    )

    Bonus_Farmer_A = Enemy(
        DisplayName = "Bonus Farmer A",
        Moves = [[equipment.Heavy_Punch,51,100],[equipment.Pocket_Knife,51,100],[equipment.Speedy_Punch,0,50],[equipment.Arrgh,0,50]],
        Weakness = ["Lance","Fire","Water","Gun"],
        Sprite = "bonus_farmer",
        Level = 9,
        EXP = 400,
        Gold = 475,
        ATK = 1125,
        MAG = 950,
        HLG = 3,
        DEF = 925,
        RES = 450,
        Max_HP = 1750,
        Max_SP = 3000,
        Max_Action_Count = 2,
        Bio = "Bonus Farmers, they're not as popular as\nthe basic Point Farmers, but they're\njust as cool, if not cooler.",
        Effects = []
    )

    Bonus_Farmer_B = Enemy(
        DisplayName = "Bonus Farmer B",
        Moves = [[equipment.Heavy_Punch,51,100],[equipment.Pocket_Knife,51,100],[equipment.Speedy_Punch,0,50],[equipment.Arrgh,0,50]],
        Weakness = ["Lance","Fire","Water","Gun"],
        Sprite = "bonus_farmer",
        Level = 9,
        EXP = 400,
        Gold = 475,
        ATK = 1125,
        MAG = 950,
        HLG = 3,
        DEF = 925,
        RES = 450,
        Max_HP = 1750,
        Max_SP = 3000,
        Max_Action_Count = 2,
        Bio = "Bonus Farmers, they're not as popular as\nthe basic Point Farmers, but they're\njust as cool, if not cooler.",
        Effects = []
    )

    Omega_Point_Farmer_A = Enemy(
        DisplayName = "Omega Point Farmer A",
        Moves = [[equipment.Fire_Trick,0,100],[equipment.Douse,0,100],[equipment.Ice_Cube,0,100],[equipment.Recover,0,100],[equipment.Bet,51,100],[equipment.Raise,0,50]],
        Weakness = ["Fists","Sword","Lance","Bow"],
        Sprite = "omega_point_farmer",
        Level = 9,
        EXP = 550,
        Gold = 500,
        ATK = 875,
        MAG = 1150,
        HLG = 3,
        DEF = 725,
        RES = 1000,
        Max_HP = 1925,
        Max_SP = 4250,
        Max_Action_Count = 2,
        Bio = "A rare kind of Point Farmer, trained\nat The Shadow Market and The Point Casino.",
        Effects = []
    )

    Hyper_Final_Assassin_Ultra = Enemy(
        DisplayName = "Hyper Final Assassin Ultra",
        Moves = [[equipment.Await,99,100],[equipment.Burst_Slash_X,85,99],[equipment.Burst_Slash_Y,85,99],[equipment.Await,65,85],[equipment.Umbral_Vociferation,65,85],[equipment.Burst_Slash_Z,0,65],[equipment.Burst_Slash_A,0,65]],
        Weakness = ["Staff", "Bow","Water"],
        Sprite = "hyper_final_assassin_ultra",
        Level = 12,
        EXP = 1000,
        Gold = 6500,
        ATK = 1250,
        MAG = 1250,
        HLG = 10,
        DEF = 500,
        RES = 500,
        Max_HP = 150000,
        Max_SP = 10000,
        Max_Action_Count = 1,
        Bio = "Hyper Final Assassin Ultra (HFAU) is\nan elite warrior raised in the toils of war.",
        Effects = []
    )

if True: #Ricefield Realm Encounters
    rr_encounter1 = [[Bonus_Farmer_A,Point_Farmer_A,Point_Farmer_B],"Normal"]
    rr_encounter2 = [[Bonus_Farmer_A,Bonus_Farmer_B,Point_Farmer_A],"Normal"]
    rr_encounter3 = [[Omega_Point_Farmer_A,Point_Farmer_A],"Normal"]
    rr_boss = [[Hyper_Final_Assassin_Ultra],"Big"]

if True: #Metalimnion Enemies
    Radical_Warper = Enemy(
        DisplayName = "Radical Warper",
        Moves = [[equipment.Skateboard,0,100],[equipment.Boombox,0,100]],
        Weakness = ["Sword","Bow","Water","Gun"],
        Sprite = "radical_warper2",
        Level = 13,
        EXP = 350,
        Gold = 900,
        ATK = 1100,
        MAG = 1025,
        HLG = 8,
        DEF = 750,
        RES = 700,
        Max_HP = 2500,
        Max_SP = 500,
        Max_Action_Count = 1,
        Bio = "He's more radical at warping than\nyou are.",
        Effects = []
    )

    Picky_Jimmy = Enemy(
        DisplayName = "Picky Jimmy",
        Moves = [[equipment.Comically_Large_Pick,50,100],[equipment.Epic_Guitar_Riff,0,50]],
        Weakness = ["Fists","Lance","Ice","Gun"],
        Sprite = "picky_jimmy",
        Level = 13,
        EXP = 425,
        Gold = 7,
        ATK = 1100,
        MAG = 1025,
        HLG = 10,
        DEF = 725,
        RES = 725,
        Max_HP = 2250,
        Max_SP = 500,
        Max_Action_Count = 1,
        Bio = "Picky Jimmy is currently high on weed.",
        Effects = []
    )

    Gunman_Greg = Enemy(
        DisplayName = "Gunman Greg",
        Moves = [[equipment.Pew_Pew,0,100],[equipment.Silver_Gauntlets,0,100]],
        Weakness = ["Sword","Staff","Bow","Fire"],
        Sprite = "gunman_greg",
        Level = 13,
        EXP = 400,
        Gold = 700,
        ATK = 1400,
        MAG = 1025,
        HLG = 9,
        DEF = 775,
        RES = 700,
        Max_HP = 2500,
        Max_SP = 500,
        Max_Action_Count = 1,
        Bio = "Warper, Picky, and Greg make up an\nindie rock band called The Metalimnioners.\nPicky plays the guitar, Warper plays a cassette,\nand Greg plays with a gun.",
        Effects = []
    )

if True: #Metalimnion Encounters
    mboss1 = [[Radical_Warper,Picky_Jimmy,Gunman_Greg],"Normal"]

if True: #Labyrinth of Binding Enemies:
    Skeleton_Soldier_A = Enemy(
        DisplayName = "Skeleton Soldier A",
        Moves = [[equipment.Pierce,0,100]],
        Weakness = ["Bow","Staff","Fire"],
        Sprite = "skeleton_soldier",
        Level = 13,
        EXP = 350,
        Gold = 525,
        ATK = 4750,
        MAG = 3275,
        HLG = 9,
        DEF = 850,
        RES = 900,
        Max_HP = 3000,
        Max_SP = 1000,
        Max_Action_Count = 1,
        Bio = "A skeleton that was reanimated to\nbe a soldier guarding something.",
        Effects = []
    )

    Skel_Floater_A = Enemy(
        DisplayName = "Skel-Floater A",
        Moves = [[equipment.Inferno,0,100],[equipment.Skull_Flame,0,100],[equipment.Skel_Boost,0,100],[equipment.Healing_Aura,0,75]],
        Weakness = ["Fists","Lance","Gun"],
        Sprite = "skel-floater",
        Level = 13,
        EXP = 325,
        Gold = 500,
        ATK = 3250,
        MAG = 3550,
        HLG = 12,
        DEF = 725,
        RES = 775,
        Max_HP = 2000,
        Max_SP = 1500,
        Max_Action_Count = 2,
        Bio = "A reanimated skull that's flying in the air.",
        Effects = []
    )

    Skel_Floater_B = Enemy(
        DisplayName = "Skel-Floater A",
        Moves = [[equipment.Inferno,0,100],[equipment.Skull_Flame,0,100],[equipment.Skel_Boost,0,100],[equipment.Healing_Aura,0,75]],
        Weakness = ["Fists","Lance","Gun"],
        Sprite = "skel-floater",
        Level = 13,
        EXP = 325,
        Gold = 500,
        ATK = 3250,
        MAG = 3550,
        HLG = 12,
        DEF = 725,
        RES = 775,
        Max_HP = 2000,
        Max_SP = 1500,
        Max_Action_Count = 2,
        Bio = "A reanimated skull that's flying in the air.",
        Effects = []
    )

    Skulsorer_A = Enemy(
        DisplayName = "Skulsorer A",
        Moves = [[equipment.Cryoablate,0,100],[equipment.Skull_Frost,0,100],[equipment.Necrobsorber,0,100],[equipment.Healing_Aura,0,75]],
        Weakness = ["Lance","Staff","Bow","Fire"],
        Sprite = "skulsorer",
        Level = 13,
        EXP = 425,
        Gold = 625,
        ATK = 3425,
        MAG = 3575,
        HLG = 13,
        DEF = 725,
        RES = 800,
        Max_HP = 7500,
        Max_SP = 7500,
        Max_Action_Count = 2,
        Bio = "A sorcerer skeleton. Kind of cool.",
        Effects = []
    )

    Shield_Skelly_A = Enemy(
        DisplayName = "Shield Skelly A",
        Moves = [[equipment.Slash,0,100]],
        Weakness = ["Lance","Staff","Fire","Ice","Gun"],
        Sprite = "shield_skelly",
        Level = 13,
        EXP = 350,
        Gold = 525,
        ATK = 4750,
        MAG = 3275,
        HLG = 9,
        DEF = 3750,
        RES = 600,
        Max_HP = 3000,
        Max_SP = 1000,
        Max_Action_Count = 1,
        Bio = "It has a very strong shield, trust me.",
        Effects = []
    )

    Shield_Skelly_B = Enemy(
        DisplayName = "Shield Skelly B",
        Moves = [[equipment.Slash,0,100]],
        Weakness = ["Lance","Fire","Water","Gun"],
        Sprite = "shield_skelly",
        Level = 13,
        EXP = 350,
        Gold = 525,
        ATK = 5250,
        MAG = 2500,
        HLG = 9,
        DEF = 15250,
        RES = 600,
        Max_HP = 3000,
        Max_SP = 1000,
        Max_Action_Count = 1,
        Bio = "It has a very strong shield, trust me.",
        Effects = []
    )

    Eidola = Enemy(
        DisplayName = "Eidola",
        Moves = [[equipment.Skull_Flame,50,100],[equipment.Skull_Frost,50,100],[equipment.Necrobsorber,50,100],[equipment.Soul_Banishment,0,50]],
        Weakness = ["Fist","Sword","Gun"],
        Sprite = "eidola",
        Level = 16,
        EXP = 1200,
        Gold = 4500,
        ATK = 17500,
        MAG = 17500,
        HLG = 16,
        DEF = 2500,
        RES = 12500,
        Max_HP = 25000,
        Max_SP = 5000,
        Max_Action_Count = 2,
        Bio = "Eidola is an extremely powerful\nnecromancer that took control of\nthe Labyrinth of Binding.",
        Effects = []
    )

    Raidiole = Enemy(
        DisplayName = "Raidiole",
        Moves = [[equipment.Piercing_Shot,75,100],[equipment.Spikey_Spray,75,100],[equipment.Incite_Fear,0,90],[equipment.Metaphysical_Bullet,0,75],[equipment.Flaming_Shot,0,75],[equipment.Magic_Shot,0,75],[equipment.Staves_Spray,0,75]],
        Weakness = ["Sword","Ice","Gun"],
        Sprite = "raidiole",
        Level = 16,
        EXP = 1200,
        Gold = 4500,
        ATK = 17500,
        MAG = 17500,
        HLG = 18,
        DEF = 3250,
        RES = 3250,
        Max_HP = 25000,
        Max_SP = 15000,
        Max_Action_Count = 3.5,
        Bio = "Raidiole is a commander in the Empire\nof Eviole, and wishes to obtain\nthe Holy Cards before Protipole, probably\nfor evil reasons.",
        Effects = []
    )

if True: #Labyrinth of Binding Encounters
    lob_encounter1 = [[Skeleton_Soldier_A,Skel_Floater_A,Skel_Floater_B],"Normal"]
    lob_encounter2 = [[Skulsorer_A,Shield_Skelly_A,Shield_Skelly_B],"Normal"]
    lob_boss1 = [[Eidola,Shield_Skelly_A,Shield_Skelly_B],"Normal"]
    lob_boss2 = [[Raidiole],"Big"]


if True: #Alter Realm Enemies:
    Aqua = Enemy(
        DisplayName = "Mirrored A",
        Moves = [[equipment.Torrent,0,100],[equipment.Slash,0,100],[equipment.Flood,0,100]],
        Weakness = ["Lance","Bow","Ice","Gun"],
        Sprite = "aqua",
        Level = 17,
        EXP = 400,
        Gold = 750,
        ATK = 9500,
        MAG = 9500,
        HLG = 75,
        DEF = 2500,
        RES = 1750,
        Max_HP = 2500,
        Current_SP = 5000,
        Max_SP = 5000,
        Bio = "The Tale of the Infinity Realm: Expedition.",
        Effects = [],
        Max_Action_Count = 3
    )

    Lead = Enemy(
        DisplayName = "Mirrored B",
        Moves = [[equipment.Fire_Card,0,100],[equipment.Water_Card,0,100],[equipment.Ice_Card,0,100]],
        Weakness = ["Fists","Staff","Water","Gun"],
        Sprite = "lead",
        Level = 17,
        EXP = 300,
        Gold = 750,
        ATK = 19000,
        MAG = 19000,
        HLG = 175,
        DEF = 2000,
        RES = 2000,
        Max_HP = 3000,
        Current_SP = 7500,
        Max_SP = 7500,
        Bio = "Bipole III: Conspiracy of the Mechanical Entity.",
        Effects = [],
        Max_Action_Count = 5
    )

    Fael = Enemy(
        DisplayName = "Mirrored C",
        Moves = [[equipment.Snipe,0,100],[equipment.Recover,0,100]],
        Weakness = ["Fists","Sword","Lance","Staff","Fire"],
        Sprite = "fael",
        Level = 17,
        EXP = 300,
        Gold = 750,
        ATK = 9500,
        MAG = 9500,
        HLG = 100,
        DEF = 1500,
        RES = 2000,
        Max_HP = 2500,
        Current_SP = 5000,
        Max_SP = 5000,
        Bio = "Bipole IV: Liberation of Xuir.",
        Effects = [],
        Max_Action_Count = 3
    )

    Neville_ZX = Enemy(
        DisplayName = "Mirrored A",
        Moves = [[equipment.Hot_Glue_Gun,0,100],[equipment.Nolmech_Blast,0,100],[equipment.ZXer,0,100]],
        Weakness = ["Fists","Sword","Staff","Water"],
        Sprite = "neville_zx",
        Level = 17,
        EXP = 400,
        Gold = 750,
        ATK = 9500,
        MAG = 9500,
        HLG = 125,
        DEF = 2750,
        RES = 1500,
        Max_HP = 3000,
        Current_SP = 5000,
        Max_SP = 5000,
        Bio = "The Hand of the Neville Prophecy.",
        Effects = [],
        Max_Action_Count = 3
    )

    Protag = Enemy(
        DisplayName = "Mirrored B",
        Moves = [[equipment.Red_Card,0,100],[equipment.Question,0,100]],
        Weakness = ["Sword","Bow","Fire","Ice","Gun"],
        Sprite = "protag",
        Level = 17,
        EXP = 300,
        Gold = 750,
        ATK = 11000,
        MAG = 11000,
        HLG = 75,
        DEF = 1750,
        RES = 1750,
        Max_HP = 2500,
        Current_SP = 5000,
        Max_SP = 5000,
        Bio = "Bipole R-XXI: Trials The First Chapter.",
        Effects = [],
        Max_Action_Count = 4
    )

    Erif = Enemy(
        DisplayName = "Mirrored C",
        Moves = [[equipment.Flame_Blade,0,100],[equipment.Fire_Blast,0,100],[equipment.Recover,0,100]],
        Weakness = ["Fists","Bow","Staff","Water","Gun"],
        Sprite = "erif",
        Level = 17,
        EXP = 300,
        Gold = 750,
        ATK = 10250,
        MAG = 10250,
        HLG = 25,
        DEF = 1500,
        RES = 1500,
        Max_HP = 2500,
        Current_SP = 5000,
        Max_SP = 5000,
        Bio = "Bipole IV: Liberation of Xuir.",
        Effects = [],
        Max_Action_Count = 4
    )

    Egam = Enemy(
        DisplayName = "Mirrored A",
        Moves = [[equipment.Attack_Shield,0,100],[equipment.Magic_Shield,0,100],[equipment.Fire_Blast,0,100],[equipment.Congeal,0,100],[equipment.Hydro,0,100]],
        Weakness = ["Fists","Sword","Lance","Gun"],
        Sprite = "egam",
        Level = 17,
        EXP = 400,
        Gold = 750,
        ATK = 9750,
        MAG = 10250,
        HLG = 25,
        DEF = 1500,
        RES = 2250,
        Max_HP = 2750,
        Current_SP = 7500,
        Max_SP = 7500,
        Bio = "Bipole R-XV: Battle Simple.",
        Effects = [],
        Max_Action_Count = 5
    )

    Infinity = Enemy(
        DisplayName = "Mirrored B",
        Moves = [[equipment.Infinite_Blade,50,100],[equipment.Infinite_Blade_X,0,100],[equipment.Infinite_Blade_Y,0,50]],
        Weakness = ["Fists","Lance","Bow","Staff","Gun"],
        Sprite = "infinity",
        Level = 17,
        EXP = 300,
        Gold = 750,
        ATK = 9750,
        MAG = 9750,
        HLG = 20,
        DEF = 1500,
        RES = 1500,
        Max_HP = 2500,
        Current_SP = 5000,
        Max_SP = 5000,
        Bio = "The Tale of the Infinity Realm: Expedition.",
        Effects = [],
        Max_Action_Count = 4
    )

    Quest = Enemy(
        DisplayName = "Mirrored C",
        Moves = [[equipment.Inferno,0,100],[equipment.Cryoablate,0,100],[equipment.Torrent,0,100],[equipment.Healing_Aura,0,100]],
        Weakness = ["Fists","Lance","Bow","Staff","Gun"],
        Sprite = "quest",
        Level = 17,
        EXP = 300,
        Gold = 750,
        ATK = 12500,
        MAG = 12500,
        HLG = 20,
        DEF = 1250,
        RES = 1750,
        Max_HP = 2250,
        Current_SP = 5000,
        Max_SP = 5000,
        Bio = "Neville OS/Bipole R-XIX: Quest.",
        Effects = [],
        Max_Action_Count = 3
    )

if True: #Alter Realm Encounters
    ar_encounter1 = [[Aqua,Lead,Fael],"Normal"]
    ar_encounter2 = [[Neville_ZX,Protag,Erif],"Normal"]
    ar_encounter3 = [[Egam,Infinity,Quest],"Normal"]

