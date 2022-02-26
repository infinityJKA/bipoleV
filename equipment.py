
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
    Inflict = ["ATK",1.2,3], #Stat to boost, amount to boost by, turns to last
    Description = "test"
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
        self.Heal_Stat = Heal_Stat
        self.Inflict = Inflict
        self.Description = Description

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

    Weakening_Punch = Equipment(
    Display_Name = "Weakening Punch",
    Equip_Type = "Fists", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Fists",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 25, #Deducted
    Priority = 125, #Added
    PWR = 100,
    Purchasing_Price = 750, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["WKN",1.2],
    Description = "Perform a weak punch and weaken the enemy"
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
    Description = "Deals weaker sword damage and gains\nless priority."
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
    Description = "A weak bite from a wild creature"
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
    Description = "To the moon (trust me bro)"
    )

    Enrage = Equipment(
    Display_Name = "Slow",
    Equip_Type = "Staff", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Staff",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 100, #Added
    PWR = 100,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["ATK",1.4,2],["DEF",0.5,2]],
    Description = "Decreases enemy DEF but\nincrases their ATK"
    )

    Geom_Strike = Equipment(
    Display_Name = "Geom Strike",
    Equip_Type = "The Lesser Truths", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Staff",
    Move_Type = "Physical", #Physical, Magic, Heal, Boost
    Target = "Single Enemy", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 0, #Deducted
    Priority = 0, #Added
    PWR = 200,
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
    Description = "Burning fire from the hatred of the\nRaging Soul"
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
    Description = "Now that's a lot of (aoe fire) damage!"
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
    Priority = 180, #Added
    PWR = 100,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Description = "A TUPLE OF THREE NUMBERS!?!?!?"
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
    
if True: #Boosts
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
    Description = "Wait the enemies get boosts too!?!??!?!?!?\nwtfffffffff unfair cringed unbased unpoggers"
    )

    Bingus_Energy_Wave = Equipment(
    Display_Name = "Bingus Energy Wave",
    Equip_Type = "y*oure mom", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "All Enemies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 50, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = ["RES",0.6,2],
    Description = "free zpoingsbuorvb borux\nkeygen real working 2001 :)"
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
    Description = "Fear the funk"
    )

    Prismatic_Honeycomb = Equipment(
    Display_Name = "Pri. Honeycomb",
    Equip_Type = "Gyrobifastigium", #Fists, Sword, Lance, Staff, Bow, Fire, Water, Ice, Heal, Gun
    Damage_Type = "Boost",
    Move_Type = "Boost", #Physical, Magic, Heal, Boost
    Target = "All Allies", #Single Enemy, Single Ally, All Enemies, All Allies 
    SP_Cost = 150, #Deducted
    Priority = 250, #Added
    PWR = 0,
    Purchasing_Price = 0, #Sells for half of the purchasing price, cannot be sold if 0
    Heal_Stat = None, #The stat to heal,
    Inflict = [["DEF",1.25,2],["ATK",1.25,2]],
    Description = "When the space-filling convex polyhedron\nwith regular faces is a Johnson solid that packs\nitself together with identical polyhedra!!!!\n\ > [] < /"
    )

if True: #Starting Uniques

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
    Inflict = ["ATK",1.2,2],
    Description = "Oh yeah let's do this\nLEEEEEEEEEEEEERRRRRROOOOOOOYYYYYYYYYY..."
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
    Inflict = ["DEF",1.05,2],
    Description = "Distract enemies by making them more\nlikely to attack you"
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
    Description = "No, there is no \"genkai\" for you\nto break here"
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
    Description = "Finally, an AOE attack!"
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
    Description = "Skill issue."
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

    sussy_explosive = Key_Item(
        Display_Name="Sussy Device",
        sprite="mreconomy",
        text_file="sussy_device"
    )

    humphrey_lore = Key_Item(
        Display_Name="HUMPHREY LORE",
        sprite="humphrey_lore",
        text_file="humphrey_lore"
    )



key_item_inventory = [test_key,sussy_explosive, humphrey_lore]