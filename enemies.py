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
        Level = 5,
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
        Level = 5,
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
        Level = 6,
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
        Level = 6,
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
        Level = 6,
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
            Moves = [[equipment.Polymath,75,100],[equipment.Global_Projection,0,75],[equipment.Prime_Sieve,50,100],[equipment.Geom_Strike,75,100]],
            Weakness = ["Fire","Gun"],
            Sprite = "eratosthenesoid",
            Level = 6,
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

if True: #Ruins of Time Encounters
    rot1_encounter1 = [[Gyrobifastigium_A,Gyrobifastigium_B,Gyrobifastigium_C],"Normal"]
    rot1_encounter2 = [[Dodecahedron_A,Gyrobifastigium_A,Gyrobifastigium_B],"Normal"]

    rot2_encounter1 = [[Eratosthenesoid_A,Dodecahedron_A,Dodecahedron_B],"Normal"]
    rot2_encounter2 = [[Eratosthenesoid_A,Dodecahedron_A,Gyrobifastigium_A],"Normal"]
    rot2_encounter3 = [[Eratosthenesoid_A,Gyrobifastigium_A,Gyrobifastigium_B],"Normal"]


