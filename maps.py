import enemies
global player_cords
global player_tracking
player_cords = [9,15]
#player_cords = [9,18]
player_tracking = [
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],["Player"],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],    
]

# R = Recruit
# T = Talk
# N = Talk (Not person)
# C = Chest
# D = Door
# S = Shop
# H = Healing
# B = Boss
# W = Warp
# L = Landing

List_of_All_Maps = []

global castle_map
castle_map = [
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["D01"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["C04"],["---"],["T03"],["000"],["T04"],["---"],["C03"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["000"],["000"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["C02"],["---"],["---"],["000"],["000"],["000"],["---"],["---"],["C01"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["T05"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["000"],["000"],["---"],["000"],["000"],["000"],["---"],["000"],["000"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["T02"],["000"],["---"],["---"],["T01"],["---"],["---"],["000"],["R01"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],###
]
List_of_All_Maps.append(castle_map)

castle_town_map = [
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["P01"],["000"],["000"],["T08"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["T07"],["000"],["S02"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["T02"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["000"],["000"],["R01"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["N03"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["T05"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["000"],["T03"],["000"],["D02"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["000"],["---"],["000"],["---"],["D03"],["---"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["000"],["H01"],["N01"],["000"],["---"],["---"],["---"],["T01"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["000"],["---"],["T04"],["---"],["000"],["---"],["000"],["---"],["N02"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["000"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["000"],["000"],["000"],["000"],["T06"],["000"],["000"],["---"],["000"],["S01"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["000"],["---"],["000"],["000"],["000"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["C01"],["---"],["---"],["D01"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["C02"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],###
]
List_of_All_Maps.append(castle_town_map)

slime_forest_map = [
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["C01"],["---"],["D01"],["---"],["000"],["000"],["000"],["---"],["000"],["000"],["C04"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["000"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["000"],["---"],["000"],["---"],["---"],["D02"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["000"],["000"],["---"],["---"],["000"],["---"],["---"],["000"],["---"],["000"],["---"],["---"],["C03"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["---"],["000"],["000"],["---"],["F01"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["000"],["000"],["---"],["000"],["---"],["000"],["---"],["---"],["000"],["---"],["000"],["---"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["000"],["000"],["000"],["000"],["---"],["000"],["---"],["N02"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["000"],["---"],["---"],["000"],["000"],["000"],["---"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["000"],["---"],["000"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["000"],["---"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["000"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["000"],["000"],["---"],["---"],["000"],["000"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["000"],["000"],["---"],["000"],["000"],["---"],["000"],["---"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["R01"],["n00"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["n00"],["n00"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["000"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["---"],["---"],["N01"],["---"],["000"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["---"],["C02"],["000"],["000"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],###
]
List_of_All_Maps.append(slime_forest_map)

slime_forest_map2 = [
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["D02"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["C05"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["F01"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["n00"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["N01"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["H01"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["_01"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["E01"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["000"],["000"],["000"],["000"],["---"],["---"],["000"],["---"],["---"],["000"],["---"],["000"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["000"],["000"],["000"],["---"],["---"],["---"],["000"],["000"],["000"],["---"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["000"],["---"],["---"],["000"],["000"],["---"],["---"],["_01"],["---"],["---"],["---"],["000"],["---"],["000"],["000"],["---"],["---"],["---"]],##
    [["---"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["C03"],["---"],["---"],["000"],["000"],["C01"],["---"],["000"],["---"],["---"],["---"]],##
    [["---"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["---"],["_01"],["---"],["000"],["000"],["---"],["---"],["---"],["000"],["---"],["---"],["---"]],##
    [["---"],["---"],["000"],["---"],["000"],["000"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["000"],["000"],["000"],["---"],["---"],["---"]],##
    [["---"],["---"],["000"],["C04"],["---"],["---"],["000"],["000"],["---"],["D01"],["---"],["000"],["000"],["000"],["000"],["---"],["C02"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],###
]
List_of_All_Maps.append(slime_forest_map2)

passway_village_map = [
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["D03"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["---"],["S02"],["S03"],["S04"],["Q01"],["T01"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["N03"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["---"],["P01"],["000"],["000"],["T02"],["000"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["D02"],["000"],["000"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["N01"],["---"],["000"],["000"],["---"],["000"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["---"],["000"],["N02"],["H01"],["000"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["000"],["000"],["R01"],["---"],["N99"],["---"],["000"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["000"],["S01"],["000"],["---"],["D01"],["---"],["---"],["R02"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],###
]
List_of_All_Maps.append(passway_village_map)


ruins_of_tine_map1 = [
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["E02"],["000"],["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["000"],["000"],["000"],["000"],["---"],["---"],["C02"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["_03"],["---"],["---"],["000"],["_01"],["000"],["---"],["---"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["000"],["000"],["---"],["---"],["000"],["---"],["000"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["000"],["---"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["000"],["---"],["---"],["T03"],["n00"],["n00"],["---"],["---"],["---"]],#
    [["---"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["---"],["---"],["---"],["000"],["---"],["---"],["T02"],["n00"],["n00"],["---"],["---"],["---"]],#
    [["---"],["---"],["E04"],["---"],["000"],["---"],["---"],["000"],["_04"],["D02"],["_03"],["000"],["000"],["000"],["n00"],["n00"],["n00"],["D01"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["000"],["---"],["---"],["000"],["---"],["---"],["---"],["000"],["---"],["---"],["n00"],["T01"],["n00"],["---"],["---"],["---"]],#
    [["---"],["---"],["E03"],["---"],["_04"],["000"],["000"],["_04"],["C05"],["---"],["---"],["000"],["---"],["---"],["n00"],["n00"],["n00"],["---"],["---"],["---"]],#
    [["---"],["---"],["000"],["---"],["000"],["---"],["---"],["000"],["---"],["---"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["000"],["000"],["000"],["---"],["---"],["000"],["---"],["---"],["000"],["---"],["C01"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["000"],["---"],["---"],["000"],["000"],["000"],["000"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["000"],["000"],["_02"],["000"],["---"],["---"],["000"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["000"],["---"],["---"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["C03"],["---"],["000"],["---"],["---"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["000"],["---"],["000"],["---"],["E01"],["---"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["000"],["---"],["000"],["---"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["000"],["000"],["000"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],#
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],##
    [["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"],["---"]],###
]
List_of_All_Maps.append(ruins_of_tine_map1)




List_of_All_Locations = []

Bieace_Castle = ["Bieace Castle", castle_map, "stone", "brown","bieace_castle",False,[],0,[0,["no eco",0],[0,0,0,0,0]]]
List_of_All_Locations.append(Bieace_Castle)

Bieace_Castle_Town = ["Bieace Castle Town", castle_town_map, "stone", "green","bieace_castle_town",False,[],0,[100.00,["Neutral",1],[95.23,94.21,93.43,95.32,98.56]]]
List_of_All_Locations.append(Bieace_Castle_Town)

Slime_Forest = ["Slime Forest A1", slime_forest_map, "stone", "dark_green","slime_forest",True,[enemies.sf1_encounter1,enemies.sf1_encounter2,enemies.sf1_encounter3],5,[0,["no eco",0],[0,0,0,0,0]]]
#Slime_Forest = ["Slime Forest", slime_forest_map, "stone", "dark_green","slime_forest",True,[enemies.single_red_slime],5,[0,["no eco",0],[0,0,0,0,0]]]
List_of_All_Locations.append(Slime_Forest)

Slime_Forest2 = ["Slime Forest A2", slime_forest_map2, "stone", "dark_green","slime_forest2",True,[enemies.sf2_encounter1,enemies.sf2_encounter2,enemies.sf2_encounter3],5,[0,["no eco",0],[0,0,0,0,0]]]
List_of_All_Locations.append(Slime_Forest2)

Passway_Village = ["Passway Village", passway_village_map, "stone", "green","passway_village",False,[],0,[100.00,["Neutral",1],[95.23,94.21,93.43,95.32,98.56]]]
List_of_All_Locations.append(Bieace_Castle_Town)

Ruins_of_Time1 = ["Ruins of Time A1", ruins_of_tine_map1, "stone", "ruins","ruins_of_time1",True,[enemies.sf2_encounter1],10,[0,["no eco",0],[0,0,0,0,0]]]
List_of_All_Locations.append(Slime_Forest2)

current_location = Bieace_Castle

#current_location = Passway_Village

current_tile = "000"

def print_player_cords():
    global player_tracking
    global player_cords
    x_cord = 0
    y_cord = 0
    contains_player = False
    for row in player_tracking:
        for location in row:
            if "player" in location:
                contains_player = True
                player_cords = [x_cord,y_cord]
            else:
                x_cord += 1
        if contains_player == False:
            x_cord = 0
            y_cord += 1
    print(player_cords)

def return_player_cords():
    global player_tracking
    global player_cords
    x_cord = 0
    y_cord = 0
    contains_player = False
    for row in player_tracking:
        for location in row:
            if "player" in location:
                contains_player = True
                player_cords = [x_cord,y_cord]
            else:
                x_cord += 1
        if contains_player == False:
            x_cord = 0
            y_cord += 1
    print(player_cords)
    return(player_cords)

def check_tile_on():
    global current_tile
    current_tile =  current_location[1][player_cords[1]][player_cords[0]][0]
    print(current_tile)

def move_player(down,right):
    global player_cords
    global player_tracking
    print("before:",player_tracking[player_cords[1]][player_cords[0]])
    player_tracking[player_cords[1]][player_cords[0]] = [""]
    print("after:",player_tracking[player_cords[1]][player_cords[0]])
    player_tracking[player_cords[1]+down][player_cords[0]+right] = ["player"]
    print_player_cords()
    check_tile_on()

# print_player_cords()
# check_tile_on()
