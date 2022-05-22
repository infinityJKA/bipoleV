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