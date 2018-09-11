#!/usr/bin/python3
#coding: utf-8

# post 12/01/2018
DEFAULT_MATCHES_14 = [["chelsea", "leicester-city"], ["crystal-palace", "burnley"], ["huddersfield-town", "west-ham-united"], ["newcastle-united", "swansea-city"], ["watford", "southampton"], ["west-bromwich-albion", "brighton-&-hove-albion"], ["tottenham-hotspur", "everton"], ["afc-bournemouth", "arsenal"], ["liverpool", "manchester-city"], ["manchester-united", "stoke-city"],]

# post 29/01/2018
WEEK_MATCHES = [["estudiantes-la-plata", "unión-de-sante-fe"], ["racing-club", "lanús"], ["belgrano-de-córdoba", "vélez-sarsfield"], ["argentinos-juniors", "atlético-tucumán"], ["san-lorenzo", "newell's-old-boys"], ["temperley", "independiente"], ["rosario-central", "olimpo-de-bahía-blanca"], ["san-martín-de-san-juan", "talleres-de-córdoba"], ["arsenal-de-sarandí", "huracán"], ["river-plate", "godoy-cruz-de-mendoza"],
 ["banfield", "boca-juniors"], ["tigre", "defense-y-justicia"], ["patronato", "chacarita-juniors"], ["cólon-de-santa-fe", "gimnasia-la-plata"],]

ARGENTINA_SUPERLIGA_TEAMS = ["boca-juniors", "san-lorenzo", "unión-de-sante-fe", "talleres-de-córdoba", "huracán", 
  "belgrano-de-córdoba", "independiente", "argentinos-juniors", "cólon-de-santa-fe", "godoy-cruz-de-mendoza", 
  "estudiantes-la-plata", "san-martín-de-san-juan", "atlético-tucumán", "banfield", "defense-y-justicia", 
  "vélez-sarsfield", "racing-club", "patronato", "gimnasia-la-plata", "river-plate", "rosario-central", "lanús", 
  "newell's-old-boys", "temperley", "chacarita-juniors", "olimpo-de-bahía-blanca", "tigre", "arsenal-de-sarandí",]

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

##--## New best match output : 66.42%, associated exact pronos : 17.89%, MUTABLE_VARS: {
MUTABLE_VARS["COEFF_WIN_STREAK"] = 0.3466666666666667
MUTABLE_VARS["COEFF_SCORED_GEN"] = -2.0
MUTABLE_VARS["GLOBAL_COEFF"] = 0.4
MUTABLE_VARS["COEFF_LEARNING"] = 1.3866666666666667
MUTABLE_VARS["COEFF_GOALS"] = 0.34666666666666657
MUTABLE_VARS["COEFF_VALUE"] = -0.002841530054644808
MUTABLE_VARS["COEFF_VICT_GEN"] = -2.2
MUTABLE_VARS["COEFF_EXP"] = -0.01723991507430998
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 59.71333333333334
MUTABLE_VARS["COEFF_DEF_GEN"] = -1.0
MUTABLE_VARS["COEFF_TAKEN_GEN"] = -0.5
MUTABLE_VARS["COEFF_DRAW_GEN"] = -0.5


