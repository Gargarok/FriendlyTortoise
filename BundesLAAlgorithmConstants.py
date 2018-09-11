#!/usr/bin/python3
#coding: utf-8

# post 15/02/2018
DEFAULT_MATCHES_14 = [["chelsea", "leicester-city"], ["crystal-palace", "burnley"], ["huddersfield-town", "west-ham-united"], ["newcastle-united", "swansea-city"], ["watford", "southampton"], ["west-bromwich-albion", "brighton-&-hove-albion"], ["tottenham-hotspur", "everton"], ["afc-bournemouth", "arsenal"], ["liverpool", "manchester-city"], ["manchester-united", "stoke-city"],]

# post 15/02/2018 
DEFAULT_MATCHES_15 = [["hertha-berlin", "mainz"], ["hamburg-sv", "bayer-leverkusen"], ["vfl-wolfsburg", "bayern-munich"], ["sc-freiburg", "werder-bremen"], ["schalke-04", "tsg-hoffenheim"], ["fc-augsburg", "vfb-stuttgart"], ["borussia-monchengladbach", "borussia-dortmund"], ["eintracht-frankfurt", "rb-leipzig"], ["fc-cologne", "hannover-96"], ]

# post 22/02/2018 
DEFAULT_MATCHES_16 = [["mainz", "vfl-wolfsburg"], ["tsg-hoffenheim", "sc-freiburg"], ["vfb-stuttgart", "eintracht-frankfurt"], ["hannover-96", "borussia-monchengladbach"], ["bayern-munich", "hertha-berlin"], ["werder-bremen", "hamburg-sv"], ["bayer-leverkusen", "schalke-04"], ["rb-leipzig", "fc-cologne"], ["borussia-dortmund", "fc-augsburg"], ]

# post 01/03/2018 
DEFAULT_MATCHES_17 = [["borussia-monchengladbach", "werder-bremen"], ["vfl-wolfsburg", "bayer-leverkusen"], ["eintracht-frankfurt", "hannover-96"], ["hamburg-sv", "mainz"], 
  ["fc-augsburg", "tsg-hoffenheim"], ["schalke-04", "hertha-berlin"], ["rb-leipzig", "borussia-dortmund"], ["fc-cologne", "vfb-stuttgart"], ["sc-freiburg", "bayern-munich"], ]
  
# post 08/03/2018 
DEFAULT_MATCHES_18 = [["mainz", "schalke-04"], ["hertha-berlin", "sc-freiburg"], ["tsg-hoffenheim", "vfl-wolfsburg"], 
  ["hannover-96", "fc-augsburg"], ["bayern-munich", "hamburg-sv"], ["bayer-leverkusen", "borussia-monchengladbach"], 
  ["vfb-stuttgart", "rb-leipzig"], ["borussia-dortmund", "eintracht-frankfurt"], ["werder-bremen", "fc-cologne"], ]

# post 15/03/2018 
DEFAULT_MATCHES_X = [["sc-freiburg", "vfb-stuttgart"], ["eintracht-frankfurt", "mainz"], ["borussia-monchengladbach", "tsg-hoffenheim"], 
  ["hamburg-sv", "hertha-berlin"], ["fc-augsburg", "werder-bremen"], ["vfl-wolfsburg", "schalke-04"], 
  ["borussia-dortmund", "hannover-96"], ["fc-cologne", "bayer-leverkusen"], ["rb-leipzig", "bayern-munich"], ]  
  
BUNDESLIGA_TEAMS = ["bayern-munich", "bayer-leverkusen", "schalke-04", "eintracht-frankfurt", "rb-leipzig", "borussia-dortmund", 
   "borussia-monchengladbach", "fc-augsburg" , "tsg-hoffenheim", "hannover-96", "hertha-berlin", "sc-freiburg", "vfl-wolfsburg", 
   "vfb-stuttgart", "mainz", "werder-bremen", "hamburg-sv", "fc-cologne",]
   
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

## ## New best match output : 73.14 %, January
MUTABLE_VARS["COEFF_VICT_GEN"] = 13.3
MUTABLE_VARS["COEFF_DEF_GEN"] = -21.5
MUTABLE_VARS["COEFF_DRAW_GEN"] = 9.8
MUTABLE_VARS["COEFF_SCORED_GEN"] = 10.4
MUTABLE_VARS["COEFF_TAKEN_GEN"] = 1.8
MUTABLE_VARS["COEFF_LEARNING"] = -4.76667
MUTABLE_VARS["COEFF_GOALS"] = -20.16
MUTABLE_VARS["COEFF_VALUE"] = 0.08092
MUTABLE_VARS["COEFF_EXP"] = -0.0413
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 66.0
MUTABLE_VARS["COEFF_WIN_STREAK"] = 15.98
MUTABLE_VARS["GLOBAL_COEFF"] = 0.0375



DEFAULT_MATCHES_X = [['bayer-leverkusen', 'fc-augsburg'], ['hannover-96', 'rb-leipzig'], ['schalke-04', 'sc-freiburg'], ['tsg-hoffenheim', 'fc-cologne'], ['vfb-stuttgart', 'hamburg-sv'], ['bayern-munich', 'borussia-dortmund'], ['hertha-berlin', 'vfl-wolfsburg'], ['werder-bremen', 'eintracht-frankfurt'], ['mainz', 'borussia-monchengladbach'], ['hannover-96', 'werder-bremen']]

WEEK_MATCHES = [['borussia-monchengladbach', 'hertha-berlin'], ['fc-augsburg', 'bayern-munich'], ['fc-cologne', 'mainz'], ['sc-freiburg', 'vfl-wolfsburg'], ['hamburg-sv', 'schalke-04'], ['borussia-dortmund', 'vfb-stuttgart'], ['eintracht-frankfurt', 'tsg-hoffenheim'], ['rb-leipzig', 'bayer-leverkusen'], ['vfl-wolfsburg', 'fc-augsburg'], ['bayer-leverkusen', 'eintracht-frankfurt'], ['hertha-berlin', 'fc-cologne'], ['tsg-hoffenheim', 'hamburg-sv'], ['vfb-stuttgart', 'hannover-96'], ['bayern-munich', 'borussia-monchengladbach']]