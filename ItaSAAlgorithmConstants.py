#!/usr/bin/python3
#coding: utf-8

# post 01/02/2018
DEFAULT_MATCHES_14 = [["sampdoria", "torino"], ["internazionale", "crotone"], ["hellas-verona", "as-roma"], ["cagliari", "spal"], ["juventus", "sassuolo"], ["atalanta", "chievo-verona"], ["bologna", "fiorentina"], ["udinese", "ac-milan"], ["benevento", "napoli"], ["lazio", "genoa"],]

# post 08/02/2018
DEFAULT_MATCHES_15 = [["fiorentina", "juventus"], ["spal", "ac-milan"], ["crotone", "atalanta"], ["napoli", "lazio"], ["sassuolo", "cagliari"], ["sampdoria", "hellas-verona"], ["internazionale", "bologna"], ["chievo-verona", "genoa"], ["torino", "udinese"], ["as-roma", "benevento"],]

# post 15/02/2018
DEFAULT_MATCHES_16 = [["udinese", "as-roma"], ["chievo-verona", "cagliari"], ["genoa", "internazionale"], ["torino", "juventus"], ["napoli", "spal"], ["benevento", "crotone"], ["bologna", "sassuolo"], ["atalanta", "fiorentina"], ["ac-milan", "sampdoria"], ["lazio", "hellas-verona"],]

# post 22/02/2018
DEFAULT_MATCHES_17 = [["bologna", "genoa"], ["internazionale", "benevento"], ["crotone", "spal"], ["hellas-verona", "torino"], ["sampdoria", "udinese"], ["fiorentina", "chievo-verona"], ["sassuolo", "lazio"], ["juventus", "atalanta"], ["as-roma", "ac-milan"], ["cagliari", "napoli"],]

# post 01/03/2018
DEFAULT_MATCHES_18 = [["spal", "bologna"], ["lazio", "juventus"], ["napoli", "as-roma"], ["genoa", "cagliari"], ["chievo-verona", "sassuolo"], ["udinese", "fiorentina"], 
  ["torino", "crotone"], ["benevento", "hellas-verona"], ["atalanta", "sampdoria"], ["ac-milan", "internazionale"],]
  
# post 08/03/2018
DEFAULT_MATCHES_19 = [["as-roma", "torino"], ["hellas-verona", "chievo-verona"], ["fiorentina", "benevento"], 
  ["juventus", "udinese"], ["bologna", "atalanta"], ["crotone", "sampdoria"], ["cagliari", "lazio"], 
  ["sassuolo", "spal"], ["genoa", "ac-milan"], ["internazionale", "napoli"],]

# post 15/03/2018
DEFAULT_MATCHES_X = [["udinese", "sassuolo"], ["spal", "juventus"], ["sampdoria", "internazionale"], 
  ["crotone", "as-roma"], ["torino", "fiorentina"], ["hellas-verona", "atalanta"], ["ac-milan", "chievo-verona"], 
  ["benevento", "cagliari"], ["napoli", "genoa"], ["lazio", "bologna"],]  
  
ITA_SERIE_A_TEAMS = ["napoli", "juventus", "lazio", "internazionale", "as-roma", "sampdoria", "ac-milan", "atalanta",
  "udinese", "torino", "fiorentina", "bologna", "chievo-verona", "sassuolo", "genoa", "cagliari",
  "crotone", "spal", "hellas-verona", "benevento",]
  
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

## December to January
## New best match output : 64.08% associated exact pronos : 9.63% MUTABLE_VARS: {
##MUTABLE_VARS["COEFF_GOALS"] = -0.4
##MUTABLE_VARS["COEFF_VICT_GEN"] = 0.8
##MUTABLE_VARS["COEFF_VALUE"] = -0.00061
##MUTABLE_VARS["COEFF_DRAW_GEN"] = -4.8
##MUTABLE_VARS["COEFF_WIN_STREAK"] = 9.0
##MUTABLE_VARS["GLOBAL_COEFF"] = 0.6
##MUTABLE_VARS["COEFF_LEARNING"] = 3.1
##MUTABLE_VARS["COEFF_SCORED_GEN"] = 3.4
##MUTABLE_VARS["COEFF_DEF_GEN"] = -0.7
##MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 15.4
##MUTABLE_VARS["COEFF_EXP"] = -0.03823
##MUTABLE_VARS["COEFF_TAKEN_GEN"] = 1.3

## ## New best match output : 78 % in January
MUTABLE_VARS["COEFF_VICT_GEN"] = -14.7
MUTABLE_VARS["COEFF_DEF_GEN"] = 15.6
MUTABLE_VARS["COEFF_DRAW_GEN"] = -4.1
MUTABLE_VARS["COEFF_SCORED_GEN"] = 11.4
MUTABLE_VARS["COEFF_TAKEN_GEN"] = 6.4
MUTABLE_VARS["COEFF_LEARNING"] = 13.60667
MUTABLE_VARS["COEFF_GOALS"] = -6.6
MUTABLE_VARS["COEFF_VALUE"] = 0.03676
MUTABLE_VARS["COEFF_EXP"] = -0.17789
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 11.2
MUTABLE_VARS["COEFF_WIN_STREAK"] = 2.83333
MUTABLE_VARS["GLOBAL_COEFF"] = -0.44444




DEFAULT_MATCHES_X = ["['bologna', 'as-roma']", "['atalanta', 'udinese']", "['cagliari', 'torino']", "['fiorentina', 'crotone']", "['genoa', 'spal']", "['internazionale', 'hellas-verona']", "['lazio', 'benevento']", "['sassuolo', 'napoli']", "['chievo-verona', 'sampdoria']", "['juventus', 'ac-milan']"]

DEFAULT_MATCHES_X = [['bologna', 'as-roma'], ['atalanta', 'udinese'], ['cagliari', 'torino'], ['fiorentina', 'crotone'], ['genoa', 'spal'], ['internazionale', 'hellas-verona'], ['lazio', 'benevento'], ['sassuolo', 'napoli'], ['chievo-verona', 'sampdoria'], ['juventus', 'ac-milan']]

WEEK_MATCHES = [['benevento', 'juventus'], ['as-roma', 'fiorentina'], ['spal', 'atalanta'], ['sampdoria', 'genoa'], ['torino', 'internazionale'], ['crotone', 'bologna'], ['napoli', 'chievo-verona'], ['hellas-verona', 'cagliari'], ['udinese', 'lazio'], ['ac-milan', 'sassuolo']]