import equipment
class Party_Character:
    def __init__(self,
    Display_Name = "DISPLAY NAME",
    Usable_Weapons = ["Fists","Sword","Lance","Bow","Staff","Fire","Water","Ice","Healing"],
    Weakness = ["Fists","Sword","Lance","Bow","Staff","Fire","Water","Ice","Healing"],
    Equipped = [],
    Level = 1,
    EXP = 0,
    ATK = 150,
    ATK_Growth = 20,
    MAG = 150,
    MAG_Growth = 20,
    HLG = 150,
    HLG_Growth = 20,
    Max_HP = 650,
    Current_HP = 500,
    HP_Growth = 20,
    Max_SP = 250,
    Current_SP = 100,
    SP_Growth = 20,
    DEF = 200,
    DEF_Growth = 20,
    RES = 200,
    RES_Growth =20,
    Effects = [],
    Priority = 0000,
    Max_Action_Count = 1,
    Current_Action_Count = 0
    ):
        self.DisplayName = Display_Name
        self.Usable_Weapons = Usable_Weapons
        self.Weakness = Weakness
        self.Equipped = Equipped
        self.Level = Level
        self.EXP = EXP
        self.ATK = ATK
        self.ATK_Growth = ATK_Growth
        self.MAG = MAG
        self.MAG_Growth = MAG_Growth
        self.HLG = HLG
        self.HLG_Growth = HLG_Growth
        self.Max_HP = Max_HP
        self.Current_HP = Current_HP
        self.HP_Growth = HP_Growth
        self.Max_SP = Max_SP
        self.Current_SP = Current_SP
        self.SP_Growth = SP_Growth
        self.DEF = DEF
        self.DEF_Growth = DEF_Growth
        self.RES = RES
        self.RES_Growth = RES_Growth
        self.Effects = Effects
        self.Priority = Priority
        self.Max_Action_Count = Max_Action_Count
        self.Current_Action_Count = Current_Action_Count

List_of_All_Recruitable_Party_Members = []

if True: #Party Members
    
    Protipole = Party_Character(
    Display_Name = "Protipole",
    Usable_Weapons = ["Sword","Lance","Fire","Healing","Protipole"],
    Weakness = ["Staff","Water"],
    Equipped= [equipment.Champion],#[equipment.Disarm,equipment.Slash,equipment.Recover],#[equipment.Champion],
    Level = 1,
    Effects = [],
    
    ATK = 90,
    ATK_Growth = 18,
    
    MAG = 80,
    MAG_Growth = 18,
    
    HLG = 10,
    HLG_Growth = 17,

    Max_HP = 500,
    Current_HP = 500,
    HP_Growth = 19,

    Max_SP = 200,
    Current_SP = 200,
    SP_Growth = 16,
    
    DEF = 150,
    DEF_Growth = 17,
    
    RES = 200,
    RES_Growth = 17
    )
    List_of_All_Recruitable_Party_Members.append(Protipole)

    Startole = Party_Character(
    Display_Name = "Startole",
    Usable_Weapons = ["Fists","Lance", "Startole"],
    Weakness = ["Bow","Fire"],
    Equipped= [equipment.Guard],
    Level = 1,
    Effects = [],
    
    ATK = 85,
    ATK_Growth = 18,
    
    MAG = 40,
    MAG_Growth = 12,
    
    HLG = 6,
    HLG_Growth = 17,

    Max_HP = 650,
    Current_HP = 650,
    HP_Growth = 18,

    Max_SP = 100,
    Current_SP = 100,
    SP_Growth = 15,

    DEF = 230,
    DEF_Growth = 18,
    
    RES = 125,
    RES_Growth = 17
    )
    List_of_All_Recruitable_Party_Members.append(Startole)

    Bipoanderer = Party_Character(
    Display_Name = "Bipoanderer",
    Usable_Weapons = ["Sword","Bow","Water","Bipoanderer"],
    Weakness = ["Lance","Ice"],
    Equipped= [equipment.Power_Charge],
    Level = 1,
    Effects = [],
    
    ATK = 110,
    ATK_Growth = 18,
    
    MAG = 90,
    MAG_Growth = 18,
    
    HLG = 4,
    HLG_Growth = 15,

    Max_HP = 350,
    Current_HP = 350,
    HP_Growth = 18,

    Max_SP = 200,
    Current_SP = 200,
    SP_Growth = 17,
    
    DEF = 150,
    DEF_Growth = 16,
    
    RES = 250,
    RES_Growth = 17
    )
    List_of_All_Recruitable_Party_Members.append(Bipoanderer)

    Wicole = Party_Character(
    Display_Name = "Wicole",
    Usable_Weapons = ["Staff","Water","Ice","Healing","Wicole"],
    Weakness = ["Fists","Sword"],
    Equipped= [equipment.Thunderstorm],
    Level = 1,
    Effects = [],
    
    ATK = 75,
    ATK_Growth = 17,
    
    MAG = 110,
    MAG_Growth = 18,
    
    HLG = 10,
    HLG_Growth = 18,

    Max_HP = 375,
    Current_HP = 375,
    HP_Growth = 18,

    Max_SP = 350,
    Current_SP = 350,
    SP_Growth = 18,
    
    DEF = 150,
    DEF_Growth = 16,
    
    RES = 210,
    RES_Growth = 18
    )
    List_of_All_Recruitable_Party_Members.append(Wicole)

    Bithecary = Party_Character(
    Display_Name = "Bithecary",
    Usable_Weapons = ["Fists","Healing","Bithecary"],
    Weakness = ["Sword","Fire"],
    Equipped= [equipment.Concoction],
    Level = 1,
    Effects = [],
    
    ATK = 87,
    ATK_Growth = 18,
    
    MAG = 75,
    MAG_Growth = 18,
    
    HLG = 12,
    HLG_Growth = 19,

    Max_HP = 550,
    Current_HP = 550,
    HP_Growth = 19,

    Max_SP = 220,
    Current_SP = 220,
    SP_Growth = 16,
    
    DEF = 175,
    DEF_Growth = 17,
    
    RES = 175,
    RES_Growth = 17
    )
    List_of_All_Recruitable_Party_Members.append(Bithecary)
    
    Archle = Party_Character(
    Display_Name = "Archle",
    Usable_Weapons = ["Bow","Fire","Archle"],
    Weakness = ["Staff","Water"],
    Equipped= [equipment.Camoflauge],
    Level = 1,
    Effects = [],
    
    ATK = 86,
    ATK_Growth = 18,
    
    MAG = 86,
    MAG_Growth = 18,
    
    HLG = 8,
    HLG_Growth = 17,

    Max_HP = 450,
    Current_HP = 450,
    HP_Growth = 19,

    Max_SP = 190,
    Current_SP = 190,
    SP_Growth = 17,
    
    DEF = 173,
    DEF_Growth = 17,
    
    RES = 170,
    RES_Growth = 17
    )
    List_of_All_Recruitable_Party_Members.append(Archle)

    Bipouge = Party_Character(
        Display_Name = "Bipogue",
        Usable_Weapons = ["Fists","Sword","Bipouge"],
        Weakness = ["Lance","Ice"],
        Equipped= [equipment.Call_to_Arms],
        Level = 1,
        Effects = [],
        
        ATK = 97,
        ATK_Growth = 18,
        
        MAG = 86,
        MAG_Growth = 18,
        
        HLG = 7,
        HLG_Growth = 16,

        Max_HP = 575,
        Current_HP = 575,
        HP_Growth = 19,

        Max_SP = 210,
        Current_SP = 210,
        SP_Growth = 17,
        
        DEF = 185,
        DEF_Growth = 17,
        
        RES = 165,
        RES_Growth = 17
        )
    List_of_All_Recruitable_Party_Members.append(Bipouge)


Current_Party = [Protipole]
Unequipped_Characters = []
All_Recruited_Characters = [Protipole]