
from argparse import Action


class Equipment:
    def __init__(self,
    Display_Name = "DISPLAY NAME",
    Equip_Type = "Fists", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fists",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies, Self
    SP_Cost = 10, #Deducted
    Priority = 100, #Added
    PWR = 150,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "HP", #The stat to heal,
    Multi_Effect = False,
    Inflict = ["ATK",1.2,3], #Stat to boost, amount to boost by, turns to last
    Description = "test",
    Action_Count = 1
    ):
        self.DisplayName = Display_Name
        self.Equip_Type = Equip_Type
        self.Damage_Type = Damage_Type
        self.Move_Type = Move_Type
        self.Target = Target
        self.SP_Cost = SP_Cost
        self.PWR = PWR
        self.Priority = Priority
        self.Purchasing_Price = Purchasing_Price
        self.Multi_Effect = Multi_Effect
        self.Heal_Stat = Heal_Stat
        self.Inflict = Inflict
        self.Description = Description
        self.Action_Count = Action_Count

if True: #Fists

    Bronze_Gauntlets = Equipment(
    Display_Name = "Bronze Gauntlets",
    Equip_Type = "Fists", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fists",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Perform a weak punch"
    )

    Iron_Gauntlets = Equipment(
    Display_Name = "Iron Gauntlets",
    Equip_Type = "Fists", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fists",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 175, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Perform an average punch"
    )

    Slam = Equipment(
    Display_Name = "Slam",
    Equip_Type = "Fists", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak body slam"
    )

    Uppercut = Equipment(
    Display_Name = "Uppercut",
    Equip_Type = "Enemy", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 125, #Added
    PWR = 150,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "632(x)"
    )

    Weakening_Taunt = Equipment(
    Display_Name = "Weakening Taunt",
    Equip_Type = "Fists", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fists",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 25, #Deducted
    Priority = 125, #Added
    PWR = 100,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["WKN",1.2,3],
    Description = "Weaken the enemy with 1.2 WKN for 3 turns"
    )

    Sine = Equipment(
    Display_Name = "Sine",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fists",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 250,
    Action_Count = 0.5,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "In another timeline in which the Nexters\nreformed the world, many territories were\nnamed after aspects of the holy Truthes."
    )

if True: #Swords

    Dagger = Equipment(
    Display_Name = "Dagger",
    Equip_Type = "Sword", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 50, #Added
    PWR = 75,
    Purchasing_Price = 350, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Deals very weak sword damage and\ngain minimal priority."
    )

    Cut = Equipment(
    Display_Name = "Cut",
    Equip_Type = "Sword", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Cut the opponent with a weak strike"
    )

    Slice = Equipment(
    Display_Name = "Slice",
    Equip_Type = "Sword", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 175, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Cut the opponent with an average strike"
    )

    Slash = Equipment(
    Display_Name = "Slash",
    Equip_Type = "Sword", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 250, #Added
    PWR = 200,
    Purchasing_Price = 1500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Cut the opponent with a strong strike"
    )

    Sweep = Equipment(
    Display_Name = "Sweep",
    Equip_Type = "Sword", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 40, #Deducted
    Priority = 250, #Added
    PWR = 80,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Deals sword damage to all enemies"
    )

    Flame_Blade = Equipment(
    Display_Name = "Flame Blade",
    Equip_Type = "Archle", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 45, #Deducted
    Priority = 130, #Added
    PWR = 125,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Deals magic-sword damage, Archle only"
    )

    Sword_Lance = Equipment(
    Display_Name = "Sword-Lance",
    Equip_Type = "Sword", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Lance",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 65,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A sword that deals lance damage"
    )

    Bite = Equipment(
    Display_Name = "Bite",
    Equip_Type = "Sword", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak bite from a wild creature."
    )

    Tangent = Equipment(
    Display_Name = "Tangent",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 300,
    Action_Count = 0.4,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The Algorithm was designed to generate\nRealmers based off of the Nexters. However, the\nAlgorithm becomes less stable as it expands\nfurther out in the realm."
    )

if True: #Lances

    Jab = Equipment(
    Display_Name = "Jab",
    Equip_Type = "Lance", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Lance",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak attack using a lance"
    )

    Stab = Equipment(
    Display_Name = "Stab",
    Equip_Type = "Lance", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Lance",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 175, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An average attack using a lance"
    )

    Lance_Sword = Equipment(
    Display_Name = "Lance-Sword",
    Equip_Type = "Lance", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Sword",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 65,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A lance that deals sword damage"
    )

    Fungal_Thorns = Equipment(
    Display_Name = "Fungal Thorns",
    Equip_Type = "Lance", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Lance",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 80,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The weak thorns of a fungus\n(Do fungi even have thorns? Well, they do now!)"
    )

    Prime_Sieve = Equipment(
    Display_Name = "Prime Sieve",
    Equip_Type = "Eratosthenesoid", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Lance",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 165,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Extermination of the unworthy must\nbe enacted upon synthesization.\nWe must approach ascention."
    )

if True: #Staves

    Wooden_Staff = Equipment(
    Display_Name = "Wooden Staff",
    Equip_Type = "Staff", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Staff",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak staff"
    )

    Stone_Staff = Equipment(
    Display_Name = "Stone Staff",
    Equip_Type = "Staff", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Staff",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 175, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An average staff"
    )

    Enrage = Equipment(
    Display_Name = "Enrage",
    Equip_Type = "Staff", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Staff",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",1.4,2],["DEF",0.5,2]],
    Description = "Decreases DEF but increases\nATK."
    )

    Grassroots = Equipment(
    Display_Name = "Grassroots",
    Equip_Type = "Enemy", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Staff",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 175,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Prior to the Finis Event, human settlements\non Luna have led to a division of humanity.\nThe Manarians of the Earth and the Lunarians\nof the moon."
    )

    Geom_Strike = Equipment(
    Display_Name = "Geom Strike",
    Equip_Type = "The Lesser Truths", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Staff",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Topological? HUH!?!?\nIt was in the Finis Event in which The Realmer\nFormation occured once again.\nPartially, we experienced rebirth.\nRemenents of The Algorith... is this Geom Energy?\nIs the true path to ascendancy revealed upon us?\nMay we go beyond The Creators..."
    )

if True: #Bows

    Bow = Equipment(
    Display_Name = "Bow",
    Equip_Type = "Bow", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Bow",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 75, #Added
    PWR = 85,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak bow"
    )

    Long_Bow = Equipment(
    Display_Name = "Long Bow",
    Equip_Type = "Bow", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Bow",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 110, #Added
    PWR = 130,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An average bow"
    )

    Magic_Bow = Equipment(
    Display_Name = "Magic Bow",
    Equip_Type = "Bow", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Bow",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 75, #Added
    PWR = 85,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak bow that deals magic damage"
    )

    LP_Throw = Equipment(
    Display_Name = "LP Throw",
    Equip_Type = "Bithecary", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Bow",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 1000, #Deducted
    Priority = 2500, #Added
    PWR = 125,
    Purchasing_Price = 7500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "What the hell is going on!?!?!?"
    )

    Convex_Polytope = Equipment(
    Display_Name = "Convex Polytope",
    Equip_Type = "Dodecahedron", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Bow",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 25, #Deducted
    Priority = 0, #Added
    PWR = 115,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The Algorithm becomes progressively more\ncomplex as it forms the world. The\ntruth of the universe and its beginning is\nsimplicity."
    )

    Solution = Equipment(
    Display_Name = "Solution",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Bow",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 300,
    Action_Count = 0.2,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The Creators strived to create or discover an\nexistence above them, thus creating the\nCreations: demi-gods to the Creators. Many\nother demi-gods to different hierachies\nwere formed through various means, such\nas the Nexters creating the Dimensionals:\ndemi-gods to the Realmers."
    )

if True: #Fire

    Fireball = Equipment(
    Display_Name = "Fireball",
    Equip_Type = "Fire", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 35, #Deducted
    Priority = 75, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak fire attack"
    )

    Fire_Blast = Equipment(
    Display_Name = "Fire Blast",
    Equip_Type = "Fire", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 130, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An average fire attack"
    )

    Signal_Flare = Equipment(
    Display_Name = "Signal Flare",
    Equip_Type = "Fire", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Self", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 20, #Deducted
    Priority = 300, #Added
    PWR = 0,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict= ["ATK",0.9,2],
    Description = "Increases your priority and slightly\ndecreases your ATK for 2 turns."
    )

    Abyssal_Inferno = Equipment(
    Display_Name = "Abyssal Inferno",
    Equip_Type = "Fire", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 300, #Added
    PWR = 175,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Burning fire from the hatred of the\nRaging Soul."
    )

    Fire_Breath = Equipment(
    Display_Name = "Fire Breath",
    Equip_Type = "Slime", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The slimes are formed of Magica created\nby the Nexters following the\nFinis Event."
    )

    CigaretteLighter = Equipment(
    Display_Name = "Cigarette Lighter",
    Equip_Type = "Fire", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 85, #Added
    PWR = 45,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "\"KIDS! DO NOT SMOKE!\nSmoking very dangerous for your lungs\nand your safety. If someone offers\nyou a cigarette, make sure to decline!\"\n-the back of the lighter"
    )

    Global_Projection = Equipment(
    Display_Name = "Global Projection",
    Equip_Type = "Eratosthenesoid", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 25, #Deducted
    Priority = 0, #Added
    PWR = 125,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Stop projecting."
    )

    Dimensional_Reaction = Equipment(
    Display_Name = "Dimensional Reaction",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 250,
    Action_Count = 0.1,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "In some places, the barrier between\ndifferent realms and timelines may thin..."
    )

    Nontotient = Equipment(
    Display_Name = "Nontotient",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 200,
    Action_Count = 0.4,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The highest entities to exist are\nthe Creators, who created a layer of lower\nentities. Those entities would then advance\nenough to create their own lower entities,\nand the process repeated. Eventually, the\nNexters were created. Afterwards, the Realmers\nwere created by the Nexters."
    )

if True: #Water
    Aqua = Equipment(
    Display_Name = "Aqua",
    Equip_Type = "Water", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Water",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 35, #Deducted
    Priority = 75, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak water attack"
    )

    Hydro = Equipment(
    Display_Name = "Hydro",
    Equip_Type = "Water", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Water",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 130, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An average water attack"
    )

    Flood = Equipment(
    Display_Name = "Flood",
    Equip_Type = "Water", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Water",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 200, #Deducted
    Priority = 300, #Added
    PWR = 25,
    Purchasing_Price = 1250, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",0.8,2],["MAG",0.8,2]],
    Description = "Deals slight water damage and decreases\nATK/MAG for 2 turns to all enemies"
    )

    Cosine = Equipment(
    Display_Name = "Cosine",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fire",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 250,
    Action_Count = 0.5,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "In territories named after the\nholy Truthes, the origins of their\nnames have largely been forgotten to\nthe passage of time."
    )

if True: #Ice
    Freeze = Equipment(
    Display_Name = "Freeze",
    Equip_Type = "Ice", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Ice",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 35, #Deducted
    Priority = 75, #Added
    PWR = 100,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A weak ice attack"
    )

    Congeal = Equipment(
    Display_Name = "Congeal",
    Equip_Type = "Ice", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Ice",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 130, #Added
    PWR = 150,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An average ice attack"
    )

    Blizzard = Equipment(
    Display_Name = "Blizzard",
    Equip_Type = "Ice", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Ice",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 100, #Deducted
    Priority = 180, #Added
    PWR = 95,
    Purchasing_Price = 1250, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Deals ice damage to all enemies"
    )

    Shatter = Equipment(
    Display_Name = "Shatter",
    Equip_Type = "Ice", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Ice",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 90, #Added
    PWR = 100,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["DEF",0.5,1]],
    Description = "Deals weak ice damage and decreases\ntarget DEF/RES for the rest of the turn"
    )

    Three_Space = Equipment(
    Display_Name = "Eclidean 3-Space",
    Equip_Type = "Gyrobifastigium", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Ice",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 25, #Deducted
    Priority = 0, #Added
    PWR = 115,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Though the Nexters and Realmers may reside\nas three-dimensional entities, many higher\nentities have much more different forms."
    )

if True: #Healing
    Heal = Equipment(
    Display_Name = "Heal",
    Equip_Type = "Healing", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Healing, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 30, #Deducted
    Priority = 150, #Added
    PWR = 15,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "HP", #The stat to heal,
    Description = "A weak healing spell with a small cost."
    )

    Recover = Equipment(
    Display_Name = "Recover",
    Equip_Type = "Healing", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Healing, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 75, #Deducted
    Priority = 315, #Added
    PWR = 30,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "HP", #The stat to heal,
    Description = "An average healing spell with an average cost."
    )

    Long_Heal = Equipment(
    Display_Name = "Long Heal",
    Equip_Type = "Healing", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Healing, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 60, #Deducted
    Priority = 75, #Added
    PWR = 15,
    Purchasing_Price = 500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "HP", #The stat to heal,
    Description = "A weak healing spell with lower priority\nbut a higher cost."
    )

    Far_Heal = Equipment(
    Display_Name = "Far Heal",
    Equip_Type = "Healing", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Healing, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 145, #Deducted
    Priority = 160, #Added
    PWR = 30,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "HP", #The stat to heal,
    Description = "An average healing spell with lower priority\nbut a higher cost."
    )

    Healing_Spores = Equipment(
    Display_Name = "Healing Spores",
    Equip_Type = "Healing", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Healing, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 20, #Deducted
    Priority = 150, #Added
    PWR = 15,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "HP", #The stat to heal,
    Description = "WHY DO THE ENEMIES GET AOE HEALING!?!?!?\nWHY DO THE ENEMIES GET AOE HEALING!?!?!?\nWHY DO THE ENEMIES GET AOE HEALING!?!?!?"
    )
    
    Hyperbolic = Equipment(
    Display_Name = "Hyperbolic",
    Equip_Type = "Healing", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Healing, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 75, #Deducted
    Priority = 0, #Added
    PWR = 30,
    Action_Count = 0.3,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "HP", #The stat to heal,
    Description = "As more time passes from a creation or a\nreformation, the residual Lesser Truthes\nwill reduced more and more."
    )

if True: #Guns
    The_22XX = Equipment(
    Display_Name = "The 22XX",
    Equip_Type = "Protipole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Gun",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 700, #Added
    PWR = 100,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An ancient weapon from a previous civilization.\nThe side of the gun reads \"22XX\"."
    )

    Enderscope_X = Equipment(
    Display_Name = "Enderscope X",
    Equip_Type = "Archle", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Gun",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 250, #Deducted
    Priority = 50, #Added
    PWR = 200,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The Enderscope X ultilizes human Mana\ngeneration using CELL technology. The rifle was\ninvented by scientist Criz Zzir, and was used\nto arm the Bastion rebels."
    )

    Branching = Equipment(
    Display_Name = "Branching",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Gun",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 250,
    Action_Count = 0.1,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "The universe ever expands, with The Algorithm\nendlessly stemming from the singularity\npoint of the Creators."
    )

if True: #Boosts

    Strength_Potion = Equipment(
    Display_Name = "Strength Potion",
    Equip_Type = "Bithecary", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 350, #Deducted
    Priority = 150, #Added
    PWR = 0,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["ATK",1.5,3],
    Description = "Inflict 1.5x ATK for 3 turns."
    )

    Mentality_Potion = Equipment(
    Display_Name = "Mentality Potion",
    Equip_Type = "Bithecary", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 350, #Deducted
    Priority = 150, #Added
    PWR = 0,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["MAG",1.5,3],
    Description = "Inflict 1.5x MAG for 3 turns."
    )

    Power_Flag = Equipment(
    Display_Name = "Power Flag",
    Equip_Type = "Startole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Multiboost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 100, #Deducted
    Priority = 225, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",1.25,3],["MAG",1.25,3]],
    Description = "1.25x ATK and 1.5x MAG for 3 turns."
    )

    Disarm = Equipment(
    Display_Name = "Disarm",
    Equip_Type = "Protipole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Multiboost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 125, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",0.8,4],["MAG",0.8,4],["DEF",0.7,3],["RES",0.7,3]],
    Description = "Inflict 0.8x ATK/MAG for 4 turns\nand 0.7x DEF/RES for 3 turns."
    )

    Daunt = Equipment(
    Display_Name = "Daunt",
    Equip_Type = "Protipole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Multiboost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 150, #Deducted
    Priority = 350, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",0.85,3],["MAG",0.85,3],["DEF",0.85,3],["RES",0.85,3]],
    Description = "Inflict 0.85x ATK/MAG/DEF/RES for 3 turns."
    )

    Mana_Aura = Equipment(
    Display_Name = "Mana Aura",
    Equip_Type = "Wicole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 400, #Deducted
    Priority = 150, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["MAG",1.45,3],
    Description = "Inflict 1.45x MAG for 3 turns."
    )

    Equivalent_Exchange_I = Equipment(
    Display_Name = "Equivalent Exchange I",
    Equip_Type = "Alls Ros", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Multiboost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 750, #Deducted
    Priority = 200, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",1.5,3],["MAG",0.5,3]],
    Description = "1.5x ATK for 0.5x MAG (3 turns)\nEvery timeline has its correspondents,\nyou too."
    )

    Equivalent_Exchange_II = Equipment(
    Display_Name = "Equivalent Exchange II",
    Equip_Type = "Alls Ros", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Multiboost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 750, #Deducted
    Priority = 200, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["MAG",1.5,3],["ATK",0.5,3]],
    Description = "1.5x MAG for 0.5x ATK (3 turns)\nEvery timeline has its correspondents,\nyou too."
    )

    Equivalent_Exchange_III = Equipment(
    Display_Name = "Equivalent Exchange III",
    Equip_Type = "Alls Ros", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Multiboost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 750, #Deducted
    Priority = 200, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["DEF",1.5,3],["RES",0.5,3]],
    Description = "1.5x DEF for 0.5x RES (3 turns)\nEvery timeline has its correspondents,\nyou too."
    )

    Equivalent_Exchange_IV = Equipment(
    Display_Name = "Equivalent Exchange IV",
    Equip_Type = "Alls Ros", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Multiboost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 750, #Deducted
    Priority = 200, #Added
    PWR = 0,
    Purchasing_Price = 1000, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["RES",1.5,3],["DEF",0.5,3]],
    Description = "1.5x RES for 0.5x DEF (3 turns)\nEvery timeline has its correspondents,\nyou too."
    )

    Equivalent_Exchange_V = Equipment(
    Display_Name = "Equivalent Exchange V",
    Equip_Type = "Alls Ros", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 3500, #Deducted
    Priority = 450, #Added
    PWR = 8,
    Purchasing_Price = 1500, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "SP", #The stat to heal,
    Inflict = [],
    Description = "Every timeline has its correspondents,\nyou too."
    )
    
    Energize = Equipment(
    Display_Name = "Energize",
    Equip_Type = "Mana Fungus", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["ATK",1.6,2],
    Description = "Many monsters can convert their physical\nMagica into Mana for use in spells."
    )

    Bingus_Energy_Wave = Equipment(
    Display_Name = "Energy Wave",
    Equip_Type = "Enemy", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["RES",0.6,2],
    Description = "Despite being made up of Magica,\nmonsters still have the capability to\ngenerate their own Mana and Magica."
    )

    Cursed_Prayer = Equipment(
    Display_Name = "Cursed Prayer",
    Equip_Type = "enemy", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["DEF",0.3,3],["RES",0.3,3]],
    Description = "An evil prayer chanted upon the\nenemies of the Raging Soul"
    )

    War_Cry = Equipment(
    Display_Name = "War Cry",
    Equip_Type = "Enemy", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Self", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 25, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["ATK",3,3],
    Description = "wqejoiwjeoiuwqjeoiwqjeoiwqjeoiwqjeiowqjeiowqjoiewqjeoiwqjqwefqasfeewrsddaqaweqafwfqefewrsfewffeqfqewgewqgweqgefqwedsaewqedwqefewioewqjoiewjqi\nwejiowqjeiowjiewqfeqwfqdewfqweoewqjioewqjioewjoiewqjioewqjieowqwqijewoiejwqiejwqiejwioej\niwqjeoiwqjeiowqjeiowqjioewqjeiowqjeiowqjeiowqjeiowqjeoiwqjeiowqjeiowqewjiq"
    )

    Funky_Dance = Equipment(
    Display_Name = "Funky Dance",
    Equip_Type = "Funky Fungus", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Self", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["DEF",1.2,5],
    Description = "Fear the funk."
    )

    Prismatic_Honeycomb = Equipment(
    Display_Name = "Pri. Honeycomb",
    Equip_Type = "Gyrobifastigium", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 150, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["DEF",1.25,2],["ATK",1.25,2]],
    Description = "When creating realms, something known as\nThe Algorithm was used by many Nexters,\nnotably Azure."
    )

    Stellation = Equipment(
    Display_Name = "Stellation",
    Equip_Type = "Dodecahedron", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 150, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["DEF",1.5,2],
    Description = "Shifts among the structures of Realms are\nespecially common following creations or\nreformations."
    )

    Polymath = Equipment(
    Display_Name = "Polymath",
    Equip_Type = "Eratosthenesoid", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "Self", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["DEF",1.25,3],["RES",1.25,3],["ATK",1.25,3],["HLG",1.25,3],["MAG",1.25,3]],
    Description = "The Lesser Truths... residues of the\nfull and holy truth: creation."
    )

    Nuclear_Fission = Equipment(
    Display_Name = "Nuclear Fission",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Nynety",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 0,
    Action_Count = 0.05,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["DEF",1.5,2],["RES",1.5,2],["ATK",1.5,2],["MAG",1.5,2],["HLG",1.5,2]],
    Description = "Nuclear warfare proved further\ndangerous with the advent of CELL\ntechnology, a notable factor in Evan's\nplans of triggering a Time of Judgement."
    )

    Reciprocal  = Equipment(
    Display_Name = "Reciprocal",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Nynety",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 0,
    Action_Count = 0.4,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",1.4,2],["MAG",1.4,2],["DEF",1.25,2],["RES",1.25,2],["HLG",1.1,2]],
    Description = "All entities in a given have an alternate\nuniverse correspondent in another timeline,\nwith the exception being some certain entities\ngranted existence beyond the confines of a\nsingle timeline. However, these entities still\nhave correspondent in different time clusters,\nthe collective of multiple timelines."
    )

    Fold = Equipment(
    Display_Name = "Fold",
    Equip_Type = "Nynety", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Nynety",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 0,
    Action_Count = 0.4,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",0.9,2],["MAG",0.9,2],["DEF",0.85,2],["RES",0.85,2],["HLG",0.8,2]],
    Description = "Every realm has a 'border', the end of\nwhere reality functions properly."
    )

if True: #Starting Uniques

    The_22XX = Equipment(
    Display_Name = "The 22XX",
    Equip_Type = "Protipole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Gun",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 150, #Deducted
    Priority = 225, #Added
    PWR = 150,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "An ancient weapon from a previous civilization.\nThe side of the gun reads \"22XX\"."
    )

    Champion = Equipment(
    Display_Name = "Champion",
    Equip_Type = "Protipole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Protipole",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["ATK",1.4,2],
    Description = "Protipole is a renowned warrior of the\nBieace Empire, having succeeded in multiple\nquests across his years of service."
    )

    Multiboost_Test = Equipment(
    Display_Name = "Multiboost Test",
    Equip_Type = "Protipole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Protipole",
    Move_Type = "Multiboost", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 10, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",1.2,2],["MAG",1.2,2],["DEF",1.2,2],["RES",1.2,2],["WKN",1.2,2],["HLG",1.2,2]],
    Description = "testing item, stop hacking"
    )

    Guard = Equipment(
    Display_Name = "Guard",
    Equip_Type = "Startole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Startole",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Self", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 500, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["DEF",1.1,2],
    Description = "Distract enemies by making them more\nlikely to attack you."
    )

    Power_Charge = Equipment(
    Display_Name = "Power Charge",
    Equip_Type = "Bipoanderer", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Bipoanderer",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Self", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 100, #Deducted
    Priority = 325, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["ATK",2.5,2],
    Description = "Give yourself 2.5x ATK for 2 turns."
    )

    Thunderstorm = Equipment(
    Display_Name = "Thunderstorm",
    Equip_Type = "Wicole", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Water",
    Move_Type = "Magic", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 150, #Added
    PWR = 100,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "Deals water damage to all enemies."
    )

    Concoction = Equipment(
    Display_Name = "Concoction",
    Equip_Type = "Bithecary", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Healing, Gun
    Damage_Type = "Heal",
    Move_Type = "Heal", #Physical, Magic, Heal, Boost
    Target = "Single Ally", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 250, #Added
    PWR = 5,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = "SP", #The stat to heal,
    Description = "Restore SP to a single ally."
    )

    Camoflauge = Equipment(
    Display_Name = "Camoflauge",
    Equip_Type = "Archle", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Archle",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Self", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = -350, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["ATK",1.1,2],
    Description = "Hide from the enemy and prepare\nfor the next attack."
    )


equipment_inventory = []

class Consumable_Item:
    def __init__(self,
    Display_Name = "DISPLAY NAME",
    Purchasing_Price = 0,
    Target = "Single", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 50,
    Description = "install bipole"
    ):
        self.DisplayName = Display_Name
        self.Purchasing_Price = Purchasing_Price
        self.Target = Target
        self.Stat = Stat
        self.Percent_or_Static = Percent_or_Static
        self.Amount = Amount
        self.Description = Description

if True:

    Water = Consumable_Item(
    Display_Name = "Water",
    Purchasing_Price = 10,
    Target = "Single", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Percent",
    Amount = 1.05,
    Description = "It's literally just water."
    )

    Sparkling_Water = Consumable_Item(
    Display_Name = "Sparkling Water",
    Purchasing_Price = 50,
    Target = "Single", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 100,
    Description = "It's like water but spicy."
    )

    Bread = Consumable_Item(
    Display_Name = "Bread",
    Purchasing_Price = 125,
    Target = "Single", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 375,
    Description = "It's a piece of bread."
    )
    
    Ramen = Consumable_Item(
    Display_Name = "Ramen",
    Purchasing_Price = 450,
    Target = "Single", #Single or Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 500,
    Description = "\"nO tHiS bReAKs ThE mEdeViL eURoPeAn\nSEtTiNg yOu cAN't aDd rAMeN tO\nbIpOLe aHhHh...\" you're literally\nplaying a game in a series where a guy\nbecame a national hero for stealing an\nambulance, a teenager led multiple timelines\nto their destruction, an overweight\ncyclopse created a giant robot that\nlooks like Notre Dame to fight a god-like\nmitocondria, and an ultimate weapon called\nthe Physics Test Ball was created by\nthe gods to save the world. When was this\nseries ever realistic?"
    )

    HealingLeaves = Consumable_Item(
    Display_Name = "Healing Leaves",
    Purchasing_Price = 250,
    Target = "Single", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 400,
    Description = "Leaves that contain a natural\nhealing property."
    )

    HealingHerbs = Consumable_Item(
    Display_Name = "Healing Herbs",
    Purchasing_Price = 500,
    Target = "Full Party", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 400,
    Description = "Herbs that contain a natural\nhealing property."
    )

    Water = Consumable_Item(
    Display_Name = "Water",
    Purchasing_Price = 10,
    Target = "Single", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Percent",
    Amount = 1.05,
    Description = "It's literally just water."
    )

    Alcohol = Consumable_Item(
    Display_Name = "Alcohol",
    Purchasing_Price = 250,
    Target = "Single", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = -100000,
    Description = "Specifically cleaning alcohol.\nDon't drink it."
    )

    Nuts = Consumable_Item(
    Display_Name = "Nuts",
    Purchasing_Price = 200,
    Target = "Full Party", #Single or Full Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 300,
    Description = "Deez nu... actually, they're legumes."
    )

    Graham_Crackers = Consumable_Item(
    Display_Name = "Graham Cracker",
    Purchasing_Price = 500,
    Target = "Single", #Single or Party
    Stat = "HP",
    Percent_or_Static = "Static",
    Amount = 650,
    Description = "Perfect for crashing the economy."
    )

    Not_Butter = Consumable_Item(
    Display_Name = "Not Butter",
    Purchasing_Price = 1000,
    Target = "Party", #Single or Party
    Stat = "HP",
    Percent_or_Static = "Percent",
    Amount = -999999,
    Description = "cyanide"
    )

    J_Fuel = Consumable_Item(
    Display_Name = "J-Fuel",
    Purchasing_Price = 900,
    Target = "Single", #Single or Party
    Stat = "HP",
    Percent_or_Static = "Percent",
    Amount = 1.5,
    Description = "the j!?"
    )

    Hzeroslashtwo = Consumable_Item(
    Display_Name = "H(0/2)",
    Purchasing_Price = 1250,
    Target = "Party", #Single or Party
    Stat = "HP",
    Percent_or_Static = "Percent",
    Amount = 1.3,
    Description = "BONUS SHOP ITEM\n17.1324207031\n(Bipole 17 reference)"
    )

    e = Consumable_Item(
    Display_Name = "E",
    Purchasing_Price = 250,
    Target = "Single", #Single or Party
    Stat = "HP",
    Percent_or_Static = "Percent",
    Amount = 1.25,
    Description = "BONUS SHOP ITEM\n17.1324207031\n(Bipole 17 reference)"
    )

    Zx = Consumable_Item(
    Display_Name = "ZX",
    Purchasing_Price = 1000,
    Target = "Party", #Single or Party
    Stat = "SP",
    Percent_or_Static = "Percent",
    Amount = 1.15,
    Description = "BONUS SHOP ITEM\n17.1324207031\n(Bipole 17 reference)"
    )

    TileXtwoAS = Consumable_Item(
    Display_Name = "TileX2AS",
    Purchasing_Price = 1000,
    Target = "Single", #Single or Party
    Stat = "SP",
    Percent_or_Static = "Percent",
    Amount = 1.5,
    Description = "BONUS SHOP ITEM\n17.1324207031\n(Bipole 17 reference)"
    )

    Oatmeal = Consumable_Item(
    Display_Name = "Oatmeal",
    Purchasing_Price = 500,
    Target = "Single", #Single or Full Party
    Stat = "SP",
    Percent_or_Static = "Percent",
    Amount = 1.3,
    Description = "The holy Razzion delicacy."
    )


item_inventory = []

class Key_Item:
    def __init__(self,
    Display_Name = "DISPLAY NAME",
    sprite = "",
    text_file = ""
    ):
        self.DisplayName = Display_Name
        self.sprite = sprite
        self.text_file = text_file

if True:

    test_key = Key_Item(
        Display_Name="test key",
        sprite="nwap",
        text_file="test_item"
    )

    sussy_device = Key_Item(
        Display_Name="Sussy Device",
        sprite="sussy_device",
        text_file="sussy_device"
    )

    humphrey_lore = Key_Item(
        Display_Name="HUMPHREY LORE",
        sprite="humphrey_lore",
        text_file="humphrey_lore"
    )

    bonus_shop_pass = Key_Item(
        Display_Name="Bonus Shop Pass",
        sprite="bonus_shop_pass",
        text_file="bonus_shop_pass"
    )

    mysterious_crystals = Key_Item(
        Display_Name="Mysterious Crystals",
        sprite="mysterious_crystals",
        text_file="mysterious_crystals"
    )

    ecochecker = Key_Item(
        Display_Name="Eco-Checker",
        sprite="ecochecker",
        text_file="ecochecker"
    )

key_item_inventory = [humphrey_lore]