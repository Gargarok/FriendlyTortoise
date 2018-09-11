#!/usr/bin/python3
#coding: utf-8

# post 18/10/2017
DEFAULT_MATCHES_1 = [["st-etienne", "montpellier"], ["as-monaco", "caen"], ["nantes", "guingamp"], ["stade-rennes", "lille"]
                   , ["sc-amiens", "bordeaux"], ["metz", "dijon-fco"], ["nice", "strasbourg"], ["troyes", "lyon"]
                   , ["marseille", "paris-saint-germain"], ["angers", "toulouse"]]

# post 25/10/2017
DEFAULT_MATCHES_2 = [["paris-saint-germain", "nice"], ["bordeaux", "as-monaco"], ["dijon-fco", "nantes"], ["guingamp", "sc-amiens"]
                   , ["strasbourg", "angers"], ["montpellier", "stade-rennes"], ["caen", "troyes"], ["lyon", "metz"]
                   , ["toulouse", "st-etienne"], ["lille", "marseille"]]

# post 02/11/2017
DEFAULT_MATCHES_3 = [["stade-rennes", "bordeaux"], ["angers", "paris-saint-germain"], ["troyes", "strasbourg"], ["montpellier", "sc-amiens"]
                   , ["as-monaco", "guingamp"], ["nantes", "toulouse"], ["nice", "dijon-fco"], ["metz", "lille"]
                   , ["marseille", "caen"], ["st-etienne", "lyon"]]

# post 15/11/2017
DEFAULT_MATCHES_4 = [["lille", "st-etienne"], ["sc-amiens", "as-monaco"], ["paris-saint-germain", "nantes"], ["lyon", "montpellier"]
                   , ["bordeaux", "marseille"], ["dijon-fco", "troyes"], ["guingamp", "angers"], ["strasbourg", "stade-rennes"]
                   , ["toulouse", "metz"], ["caen", "nice"],]

# post 22/11/2017
DEFAULT_MATCHES_5 = [["st-etienne", "strasbourg"], ["caen", "bordeaux"], ["dijon-fco", "toulouse"], ["metz", "sc-amiens"]
                   , ["montpellier", "lille"], ["troyes", "angers"], ["nice", "lyon"], ["marseille", "guingamp"]
                   , ["as-monaco", "paris-saint-germain"], ["stade-rennes", "nantes"],]

# post 26/11/2017
DEFAULT_MATCHES_6 = [["strasbourg", "caen"], ["sc-amiens", "dijon-fco"], ["bordeaux", "st-etienne"], ["guingamp", "montpellier"]
                   , ["lyon", "lille"], ["metz", "marseille"], ["angers", "stade-rennes"], ["nantes", "as-monaco"]
                   , ["toulouse", "nice"], ["paris-saint-germain", "troyes"],]

# post 30/11/2017
DEFAULT_MATCHES_7 = [["dijon-fco", "bordeaux"], ["strasbourg", "paris-saint-germain"], ["as-monaco", "angers"], ["lille", "toulouse"]
                   , ["nice", "metz"], ["troyes", "guingamp"], ["stade-rennes", "sc-amiens"], ["st-etienne", "nantes"]
                   , ["caen", "lyon"], ["montpellier", "marseille"],]

# post 06/12/2017
DEFAULT_MATCHES_8 = [["bordeaux", "strasbourg"], ["paris-saint-germain", "lille"], ["angers", "montpellier"], ["guingamp", "dijon-fco"]
                   , ["metz", "stade-rennes"], ["as-monaco", "troyes"], ["toulouse", "caen"], ["sc-amiens", "lyon"]
                   , ["nantes", "nice"], ["marseille", "st-etienne"],]

# post 14/12/2017
DEFAULT_MATCHES_9 = [["st-etienne", "as-monaco"], ["stade-rennes", "paris-saint-germain"], ["strasbourg", "toulouse"], ["montpellier", "metz"]
                   , ["dijon-fco", "lille"], ["caen", "guingamp"], ["troyes", "sc-amiens"], ["nantes", "angers"]
                   , ["nice", "bordeaux"], ["lyon", "marseille"],]

# post 19/12/2017
DEFAULT_MATCHES_10 = [["sc-amiens", "nantes"], ["paris-saint-germain", "caen"], ["metz", "strasbourg"], ["as-monaco", "stade-rennes"]
                   , ["marseille", "troyes"], ["toulouse", "lyon"], ["bordeaux", "montpellier"], ["guingamp", "st-etienne"]
                   , ["angers", "dijon-fco"], ["lille", "nice"],]

# post 04/01/2018
DEFAULT_MATCHES_11 = [["strasbourg", "guingamp"], ["stade-rennes", "marseille"], ["caen", "lille"], ["dijon-fco", "metz"]
                   , ["montpellier", "as-monaco"], ["nice", "sc-amiens"], ["troyes", "bordeaux"], ["st-etienne", "toulouse"]
                   , ["lyon", "angers"], ["nantes", "paris-saint-germain"],]

# post 15/01/2018
DEFAULT_MATCHES_12 = [["bordeaux", "caen"], ["marseille", "strasbourg"], ["as-monaco", "nice"], ["guingamp", "lyon"]
                   , ["toulouse", "nantes"], ["sc-amiens", "montpellier"], ["lille", "stade-rennes"], ["angers", "troyes"]
                   , ["metz", "st-etienne"], ["paris-saint-germain", "dijon-fco"],]
                   
# post 18/01/2018
DEFAULT_MATCHES_13 = [["caen", "marseille"], ["nantes", "bordeaux"], ["troyes", "lille"], ["strasbourg", "dijon-fco"]
                   , ["montpellier", "toulouse"], ["stade-rennes", "angers"], ["sc-amiens", "guingamp"], ["nice", "st-etienne"]
                   , ["as-monaco", "metz"], ["lyon", "paris-saint-germain"],]          

# post 25/01/2018
DEFAULT_MATCHES_14 = [["dijon-fco", "stade-rennes"], ["paris-saint-germain", "montpellier"], ["angers", "sc-amiens"], ["st-etienne", "caen"]
                   , ["toulouse", "troyes"], ["guingamp", "nantes"], ["metz", "nice"], ["lille", "strasbourg"]
                   , ["bordeaux", "lyon"], ["marseille", "as-monaco"],]                      

# post 01/02/2018
DEFAULT_MATCHES_15 = [["marseille", "metz"], ["lille", "paris-saint-germain"], ["nice", "toulouse"], ["troyes", "dijon-fco"]
                   , ["montpellier", "angers"], ["strasbourg", "bordeaux"], ["sc-amiens", "st-etienne"], ["stade-rennes", "guingamp"]
                   , ["caen", "nantes"], ["as-monaco", "lyon"],]  

# post 08/02/2018
DEFAULT_MATCHES_16 = [["st-etienne", "marseille"], ["toulouse", "paris-saint-germain"], ["guingamp", "caen"], ["bordeaux", "sc-amiens"]
                   , ["angers", "as-monaco"], ["metz", "montpellier"], ["dijon-fco", "nice"], ["strasbourg", "troyes"]
                   , ["nantes", "lille"], ["lyon", "stade-rennes"],]        

# post 15/02/2018
DEFAULT_MATCHES_17 = [["as-monaco", "dijon-fco"], ["paris-saint-germain", "strasbourg"], ["sc-amiens", "toulouse"], ["caen", "stade-rennes"]
                   , ["montpellier", "guingamp"], ["angers", "st-etienne"], ["troyes", "metz"], ["nice", "nantes"]
                   , ["lille", "lyon"], ["marseille", "bordeaux"],]    

# post 22/02/2018
DEFAULT_MATCHES_18 = [["strasbourg", "montpellier"], ["toulouse", "as-monaco"], ["nantes", "sc-amiens"], ["guingamp", "metz"]
                   , ["lille", "angers"], ["dijon-fco", "caen"], ["stade-rennes", "troyes"], ["bordeaux", "nice"]
                   , ["lyon", "st-etienne"], ["paris-saint-germain", "marseille"],]              

# post 01/03/2018
DEFAULT_MATCHES_19 = [["nice", "lille"], ["as-monaco", "bordeaux"], ["troyes", "paris-saint-germain"], ["metz", "toulouse"]
                   , ["sc-amiens", "stade-rennes"], ["st-etienne", "dijon-fco"], ["angers", "guingamp"], ["caen", "strasbourg"]
                   , ["montpellier", "lyon"], ["marseille", "nantes"],]    

# post 08/03/2018
DEFAULT_MATCHES_20 = [["strasbourg", "as-monaco"], ["paris-saint-germain", "metz"], ["dijon-fco", "sc-amiens"], 
  ["stade-rennes", "st-etienne"], ["nantes", "troyes"], ["lille", "montpellier"], ["bordeaux", "angers"], 
  ["guingamp", "nice"], ["lyon", "caen"], ["toulouse", "marseille"],]       
  
# post 15/03/2018
DEFAULT_MATCHES_X = [["as-monaco", "lille"], ["bordeaux", "stade-rennes"], ["angers", "caen"], 
  ["montpellier", "dijon-fco"], ["sc-amiens", "troyes"], ["toulouse", "strasbourg"], ["nice", "paris-saint-germain"], 
  ["metz", "nantes"], ["st-etienne", "guingamp"], ["marseille", "lyon"],]       				   
                   
LIGUEONE_TEAMS = ["stade-rennes", "bordeaux", "angers", "paris-saint-germain", "troyes", "strasbourg", "montpellier", "sc-amiens"
                   , "as-monaco", "guingamp", "nantes", "toulouse", "nice", "dijon-fco", "metz", "lille"
                   , "marseille", "caen", "st-etienne", "lyon"]

PRONO_TEAMS = ["lyon", "as-monaco", "paris-saint-germain", "caen", "stade-rennes", "marseille", "nantes"]

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

## 64.3% in january
MUTABLE_VARS["COEFF_VICT_GEN"] = 6.5
MUTABLE_VARS["COEFF_DEF_GEN"] = -9.7
MUTABLE_VARS["COEFF_DRAW_GEN"] = 6.8
MUTABLE_VARS["COEFF_SCORED_GEN"] = 9.9
MUTABLE_VARS["COEFF_TAKEN_GEN"] = -3.6
MUTABLE_VARS["COEFF_LEARNING"] = -5.88
MUTABLE_VARS["COEFF_GOALS"] = -4.85333
MUTABLE_VARS["COEFF_VALUE"] = -0.00586
MUTABLE_VARS["COEFF_EXP"] = -0.02813
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 21.1
MUTABLE_VARS["COEFF_WIN_STREAK"] = 5.2
MUTABLE_VARS["GLOBAL_COEFF"] = -0.15





DEFAULT_MATCHES_X = ["['dijon-fco', 'marseille']", "['guingamp', 'bordeaux']", "['caen', 'montpellier']", "['lille', 'sc-amiens']", "['strasbourg', 'metz']", "['troyes', 'nice']", "['lyon', 'toulouse']", "['stade-rennes', 'as-monaco']", "['as-monaco', 'nantes']", "['angers', 'strasbourg']", "['bordeaux', 'lille']", "['guingamp', 'troyes']", "['sc-amiens', 'caen']", "['toulouse', 'dijon-fco']"]

DEFAULT_MATCHES_X = [['dijon-fco', 'marseille'], ['guingamp', 'bordeaux'], ['caen', 'montpellier'], ['lille', 'sc-amiens'], ['strasbourg', 'metz'], ['troyes', 'nice'], ['lyon', 'toulouse'], ['stade-rennes', 'as-monaco'], ['as-monaco', 'nantes'], ['angers', 'strasbourg'], ['bordeaux', 'lille'], ['guingamp', 'troyes'], ['sc-amiens', 'caen'], ['toulouse', 'dijon-fco']]

WEEK_MATCHES = [['nice', 'stade-rennes'], ['metz', 'lyon'], ['marseille', 'montpellier'], ['angers', 'nice'], ['lyon', 'sc-amiens'], ['caen', 'toulouse'], ['lille', 'guingamp'], ['nantes', 'dijon-fco'], ['stade-rennes', 'metz'], ['montpellier', 'bordeaux'], ['troyes', 'marseille'], ['paris-saint-germain', 'as-monaco']]