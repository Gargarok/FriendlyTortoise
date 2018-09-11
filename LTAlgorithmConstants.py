#!/usr/bin/python3
#coding: utf-8

# post 13/12/2017
DEFAULT_MATCHES_8 = [["ac-ajaccio", "aj-auxerre"], ["bourg-peronnas", "lorient"], ["chateauroux", "orléans"], ["clermont-foot", "sochaux"]
                   , ["gfc-ajaccio", "nimes"], ["le-havre-ac", "niort"], ["as-nancy-lorraine", "paris-fc"], ["us-quevilly", "brest"]
                   , ["stade-de-reims", "valenciennes"], ["lens", "tours"],]

# post 13/12/2017
DEFAULT_MATCHES_9 = [["ac-ajaccio", "aj-auxerre"], ["bourg-peronnas", "lorient"], ["chateauroux", "orléans"], ["clermont-foot", "sochaux"]
                   , ["gfc-ajaccio", "nimes"], ["le-havre-ac", "niort"], ["as-nancy-lorraine", "paris-fc"], ["us-quevilly", "brest"]
                   , ["stade-de-reims", "valenciennes"], ["lens", "tours"],]
                   
# post 02/02/2018
DEFAULT_MATCHES_10 = [["bourg-peronnas", "clermont-foot"], ["tours", "aj-auxerre"], ["orléans", "le-havre-ac"], ["paris-fc", "niort"]
                   , ["us-quevilly", "chateauroux"], ["valenciennes", "as-nancy-lorraine"], ["nimes", "ac-ajaccio"], ["sochaux", "gfc-ajaccio"]
                   , ["lorient", "lens"], ["brest", "stade-de-reims"],]
                   
# post 07/02/2018
DEFAULT_MATCHES_11 = [["as-nancy-lorraine", "us-quevilly"], ["clermont-foot", "gfc-ajaccio"], ["chateauroux", "bourg-peronnas"], 
  ["ac-ajaccio", "lorient"], ["tours", "paris-fc"], ["stade-de-reims", "sochaux"], ["le-havre-ac", "brest"], 
  ["niort", "orléans"], ["lens", "valenciennes"], ["aj-auxerre", "nimes"],]
  
# post 15/02/2018
DEFAULT_MATCHES_12 = [["orléans", "paris-fc"], ["gfc-ajaccio", "stade-de-reims"], ["nimes", "tours"], 
  ["sochaux", "le-havre-ac"], ["clermont-foot", "chateauroux"], ["brest", "niort"], ["bourg-peronnas", "as-nancy-lorraine"], 
  ["valenciennes", "ac-ajaccio"], ["lorient", "aj-auxerre"], ["us-quevilly", "lens"],]
  
# post 22/02/2018
DEFAULT_MATCHES_13 = [["chateauroux", "gfc-ajaccio"], ["niort", "nimes"], ["le-havre-ac", "bourg-peronnas"], 
  ["lens", "clermont-foot"], ["tours", "orléans"], ["aj-auxerre", "valenciennes"], ["ac-ajaccio", "sochaux"], 
  ["stade-de-reims", "us-quevilly"], ["paris-fc", "brest"], ["as-nancy-lorraine", "lorient"],]
  
# post 01/03/2018
DEFAULT_MATCHES_14 = [["chateauroux", "as-nancy-lorraine"], ["clermont-foot", "stade-de-reims"], ["valenciennes", "orléans"], 
  ["us-quevilly", "niort"], ["brest", "tours"], ["sochaux", "aj-auxerre"], ["bourg-peronnas", "ac-ajaccio"], 
  ["gfc-ajaccio", "lens"], ["nimes", "paris-fc"], ["lorient", "le-havre-ac"],]
  
# post 08/03/2018
DEFAULT_MATCHES_15 = [["niort", "lorient"], ["orléans", "nimes"], ["tours", "valenciennes"], 
  ["le-havre-ac", "clermont-foot"], ["stade-de-reims", "chateauroux"], ["ac-ajaccio", "us-quevilly"], ["aj-auxerre", "brest"], 
  ["as-nancy-lorraine", "gfc-ajaccio"], ["paris-fc", "sochaux"], ["lens", "bourg-peronnas"],]

# post 15/03/2018
DEFAULT_MATCHES_X = [["lorient", "orléans"], ["clermont-foot", "as-nancy-lorraine"], ["valenciennes", "paris-fc"], 
  ["chateauroux", "le-havre-ac"], ["bourg-peronnas", "niort"], ["sochaux", "tours"], ["us-quevilly", "aj-auxerre"], 
  ["gfc-ajaccio", "ac-ajaccio"], ["stade-de-reims", "lens"], ["brest", "nimes"],]  
  
LIGUETWO_TEAMS = ["stade-de-reims", "nimes", "ac-ajaccio", "le-havre-ac", "brest", "paris-fc", "lorient", "sochaux"
                   , "clermont-foot", "chateauroux", "niort", "valenciennes", "gfc-ajaccio", "lens", "as-nancy-lorraine", "aj-auxerre"
                   , "us-quevilly", "tours", "bourg-peronnas", "orléans"]

GENERAL_COEFF = "gen"
OFF_COEFF = "off"
DEF_COEFF = "def"
GENERAL_HOME = "home_gen"
OFF_HOME = "home_off"
DEF_HOME = "home_def"
GENERAL_AWAY = "away_gen"
OFF_AWAY = "away_off"
DEF_AWAY = "away_def"

COEFF_VICT_GEN = 2
COEFF_DEF_GEN = -1
COEFF_DRAW_GEN = 1
ADD_MATCHES_GEN = 10
COEFF_SCORED_GEN = 1
COEFF_TAKEN_GEN = -1
ADD_GOALS_GEN = 10

COEFF_VICT_OFF = 3/2
COEFF_DEF_OFF = -1
COEFF_DRAW_OFF = 1/2
COEFF_MATCHES_OFF = 5
ADD_MATCHES_OFF = 5
FIRST_COEFF_OFF = 1
COEFF_SCORED_OFF = 1/3
COEFF_TAKEN_OFF = -1/2
COEFF_GOALS_OFF = 5/2
ADD_GOALS_OFF = 5
SCD_COEFF_OFF = 2/3

COEFF_VICT_DEF = 1
COEFF_DEF_DEF = -4/3
COEFF_DRAW_DEF = 1/3
COEFF_MATCHES_DEF = 5
ADD_MATCHES_DEF = 6
FIRST_COEFF_DEF = 1
COEFF_SCORED_DEF = 1/2
COEFF_TAKEN_DEF = -2
COEFF_GOALS_DEF = 5/2
ADD_GOALS_DEF = 5
SCD_COEFF_DEF = 1

MUTABLE_VARS = {}

## OLD SCHOOL OUTPUT
##MUTABLE_VARS["GLOBAL_COEFF"] = 1
##
##MUTABLE_VARS["COEFF_VICT_GEN"] = 3
##MUTABLE_VARS["COEFF_DEF_GEN"] = -9/2
##MUTABLE_VARS["COEFF_DRAW_GEN"] = 0
##
##MUTABLE_VARS["COEFF_SCORED_GEN"] = 3
##MUTABLE_VARS["COEFF_TAKEN_GEN"] = -17/2
##
##MUTABLE_VARS["COEFF_LEARNING"] = 13/2
##MUTABLE_VARS["COEFF_GOALS"] = 7/2
##MUTABLE_VARS["COEFF_VALUE"] = 7/1200
##MUTABLE_VARS["COEFF_EXP"] = 27/1000
##MUTABLE_VARS["COEFF_WIN_STREAK"] = 1
##MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 32

## 66.45% 
MUTABLE_VARS["COEFF_VICT_GEN"] = 7.7
MUTABLE_VARS["COEFF_DEF_GEN"] = 10.0
MUTABLE_VARS["COEFF_DRAW_GEN"] = -14.0
MUTABLE_VARS["COEFF_SCORED_GEN"] = -9.8
MUTABLE_VARS["COEFF_TAKEN_GEN"] = 12.7
MUTABLE_VARS["COEFF_LEARNING"] = -2.25333
MUTABLE_VARS["COEFF_GOALS"] = 2.98667
MUTABLE_VARS["COEFF_VALUE"] = -0.00219
MUTABLE_VARS["COEFF_EXP"] = -0.02102
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 68.46667
MUTABLE_VARS["COEFF_WIN_STREAK"] = 12.13333
MUTABLE_VARS["GLOBAL_COEFF"] = 2.0




DEFAULT_MATCHES_X = ["['ac-ajaccio', 'clermont-foot']", "['aj-auxerre', 'bourg-peronnas']", "['le-havre-ac', 'us-quevilly']", "['nimes', 'valenciennes']", "['niort', 'sochaux']", "['orl�ans', 'brest']", "['paris-fc', 'gfc-ajaccio']", "['tours', 'lorient']", "['as-nancy-lorraine', 'stade-de-reims']", "['lens', 'chateauroux']"]

DEFAULT_MATCHES_X = [['ac-ajaccio', 'clermont-foot'], ['aj-auxerre', 'bourg-peronnas'], ['le-havre-ac', 'us-quevilly'], ['nimes', 'valenciennes'], ['niort', 'sochaux'], ['orl�ans', 'brest'], ['paris-fc', 'gfc-ajaccio'], ['tours', 'lorient'], ['as-nancy-lorraine', 'stade-de-reims'], ['lens', 'chateauroux']]

WEEK_MATCHES = [['clermont-foot', 'niort'], ['lorient', 'paris-fc'], ['us-quevilly', 'nimes'], ['bourg-peronnas', 'tours'], ['brest', 'valenciennes'], ['chateauroux', 'ac-ajaccio'], ['gfc-ajaccio', 'aj-auxerre'], ['sochaux', 'orl�ans'], ['stade-de-reims', 'le-havre-ac'], ['lens', 'as-nancy-lorraine']]