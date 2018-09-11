#!/usr/bin/python3
#coding: utf-8

# post 08/12/2017
DEFAULT_MATCHES_8 = [["west-ham-united", "chelsea"], ["burnley", "watford"], ["crystal-palace", "afc-bournemouth"], ["huddersfield-town", "brighton-&-hove-albion"], ["swansea-city", "west-bromwich-albion"], ["tottenham-hotspur", "stoke-city"], ["newcastle-united", "leicester-city"], ["southampton", "arsenal"], ["liverpool", "everton"], ["manchester-united", "manchester-city"],]

# post 15/12/2017
DEFAULT_MATCHES_9 = [["leicester-city", "crystal-palace"], ["arsenal", "newcastle-united"], ["brighton-&-hove-albion", "burnley"], ["chelsea", "southampton"], ["stoke-city", "west-ham-united"], ["manchester-city", "tottenham-hotspur"], ["west-bromwich-albion", "manchester-united"], ["afc-bournemouth", "liverpool"], ["everton", "swansea-city"], ["watford", "huddersfield-town"],]

# post 21/12/2017
DEFAULT_MATCHES_10 = [["arsenal", "liverpool"], ["everton", "chelsea"], ["brighton-&-hove-albion", "watford"], ["manchester-city", "afc-bournemouth"], ["southampton", "huddersfield-town"], ["stoke-city", "west-bromwich-albion"], ["west-ham-united", "newcastle-united"], ["swansea-city", "crystal-palace"], ["burnley", "tottenham-hotspur"], ["leicester-city", "manchester-united"],]

# post 25/12/2017
DEFAULT_MATCHES_11 = [["tottenham-hotspur", "southampton"], ["afc-bournemouth", "west-ham-united"], ["chelsea", "brighton-&-hove-albion"], ["huddersfield-town", "stoke-city"], ["manchester-united", "burnley"], ["watford", "leicester-city"], ["west-bromwich-albion", "everton"], ["liverpool", "swansea-city"], ["newcastle-united", "manchester-city"], ["crystal-palace", "arsenal"],]

# post 29/12/2017
DEFAULT_MATCHES_12 = [["afc-bournemouth", "everton"], ["chelsea", "stoke-city"], ["huddersfield-town", "burnley"], ["liverpool", "leicester-city"], ["newcastle-united", "brighton-&-hove-albion"], ["watford", "swansea-city"], ["manchester-united", "southampton"], ["crystal-palace", "manchester-city"], ["west-bromwich-albion", "arsenal"], ["tottenham-hotspur", "west-ham-united"],]

# post 31/12/2017
DEFAULT_MATCHES_13 = [["brighton-&-hove-albion", "afc-bournemouth"], ["burnley", "liverpool"], ["leicester-city", "huddersfield-town"], ["stoke-city", "newcastle-united"], ["everton", "manchester-united"], ["southampton", "crystal-palace"], ["swansea-city", "tottenham-hotspur"], ["west-ham-united", "west-bromwich-albion"], ["manchester-city", "watford"], ["arsenal", "chelsea"],]

# post 12/01/2018
DEFAULT_MATCHES_14 = [["chelsea", "leicester-city"], ["crystal-palace", "burnley"], ["huddersfield-town", "west-ham-united"], ["newcastle-united", "swansea-city"], ["watford", "southampton"], ["west-bromwich-albion", "brighton-&-hove-albion"], ["tottenham-hotspur", "everton"], ["afc-bournemouth", "arsenal"], ["liverpool", "manchester-city"], ["manchester-united", "stoke-city"],]

# post 29/01/2018
DEFAULT_MATCHES_15 = [["swansea-city", "arsenal"], ["west-ham-united", "crystal-palace"], ["huddersfield-town", "liverpool"], ["southampton", "brighton-&-hove-albion"], ["chelsea", "afc-bournemouth"], ["everton", "leicester-city"], ["newcastle-united", "burnley"], ["manchester-city", "west-bromwich-albion"], ["tottenham-hotspur", "manchester-united"], ["stoke-city", "watford"],]

# post 03/02/2018
DEFAULT_MATCHES_16 = [["burnley", "manchester-city"], ["west-bromwich-albion", "southampton"], ["manchester-united", "huddersfield-town"], ["afc-bournemouth", "stoke-city"], ["leicester-city", "swansea-city"], ["brighton-&-hove-albion", "west-ham-united"], ["arsenal", "everton"], ["crystal-palace", "newcastle-united"], ["liverpool", "tottenham-hotspur"], ["watford", "chelsea"],]

# post 09/02/2018
DEFAULT_MATCHES_17 = [["tottenham-hotspur", "arsenal"], ["everton", "crystal-palace"], ["swansea-city", "burnley"], ["stoke-city", "brighton-&-hove-albion"], ["west-ham-united", "watford"], ["manchester-city", "leicester-city"], ["huddersfield-town", "afc-bournemouth"], ["newcastle-united", "manchester-united"], ["southampton", "liverpool"], ["chelsea", "west-bromwich-albion"],]

# post 23/02/2018
DEFAULT_MATCHES_18 = [["leicester-city", "stoke-city"], ["west-bromwich-albion", "huddersfield-town"], ["afc-bournemouth", "newcastle-united"], ["liverpool", "west-ham-united"], ["brighton-&-hove-albion", "swansea-city"], ["burnley", "southampton"], ["watford", "everton"], ["manchester-united", "chelsea"], ["crystal-palace", "tottenham-hotspur"], ["arsenal", "manchester-city"],]

# post 01/03/2018
DEFAULT_MATCHES_19 = [["burnley", "everton"], ["leicester-city", "afc-bournemouth"], ["swansea-city", "west-ham-united"], ["tottenham-hotspur", "huddersfield-town"], ["southampton", "stoke-city"], 
  ["watford", "west-bromwich-albion"], ["liverpool", "newcastle-united"], ["brighton-&-hove-albion", "arsenal"], ["manchester-city", "chelsea"], ["crystal-palace", "manchester-united"],]
  
# post 08/03/2018
DEFAULT_MATCHES_20 = [["manchester-united", "liverpool"], ["newcastle-united", "southampton"], ["everton", "brighton-&-hove-albion"],
  ["huddersfield-town", "swansea-city"], ["west-bromwich-albion", "leicester-city"], ["west-ham-united", "burnley"], 
  ["chelsea", "crystal-palace"], ["arsenal", "watford"], ["afc-bournemouth", "tottenham-hotspur"], 
  ["stoke-city", "manchester-city"],]              

# post 15/03/2018
DEFAULT_MATCHES_X = [["tottenham-hotspur", "newcastle-united"], ["burnley", "chelsea"], ["stoke-city", "everton"],
  ["huddersfield-town", "crystal-palace"], ["leicester-city", "arsenal"], ["swansea-city", "southampton"], 
  ["afc-bournemouth", "west-bromwich-albion"], ["liverpool", "watford"], ["west-ham-united", "manchester-united"], 
  ["manchester-city", "brighton-&-hove-albion"],]             
  
PREMIERLEAGUE_TEAMS = ["manchester-city", "manchester-united", "chelsea", "liverpool", "arsenal", "burnley", "tottenham-hotspur",
                        "leicester-city", "everton", "watford", "huddersfield-town", "southampton", "brighton-&-hove-albion",
                        "crystal-palace", "west-ham-united", "afc-bournemouth", "stoke-city", "newcastle-united",
                       "west-bromwich-albion", "swansea-city"]

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

##--## New best match output : 65.49%
MUTABLE_VARS["COEFF_VICT_GEN"] = 7.3
MUTABLE_VARS["COEFF_DEF_GEN"] = 22.8
MUTABLE_VARS["COEFF_DRAW_GEN"] = 0.5
MUTABLE_VARS["COEFF_SCORED_GEN"] = -3.3
MUTABLE_VARS["COEFF_TAKEN_GEN"] = -22.1
MUTABLE_VARS["COEFF_LEARNING"] = -20.58667
MUTABLE_VARS["COEFF_GOALS"] = 10.3
MUTABLE_VARS["COEFF_VALUE"] = -0.06582
MUTABLE_VARS["COEFF_EXP"] = 0.0309
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 31.0
MUTABLE_VARS["COEFF_WIN_STREAK"] = 10.92
MUTABLE_VARS["GLOBAL_COEFF"] = -0.4


DEFAULT_MATCHES_X = ["['crystal-palace', 'liverpool']", "['brighton-&-hove-albion', 'leicester-city']", "['manchester-united', 'swansea-city']", "['newcastle-united', 'huddersfield-town']", "['watford', 'afc-bournemouth']", "['west-bromwich-albion', 'burnley']", "['west-ham-united', 'southampton']", "['everton', 'manchester-city']", "['arsenal', 'stoke-city']", "['chelsea', 'tottenham-hotspur']"]

DEFAULT_MATCHES_X = [['crystal-palace', 'liverpool'], ['brighton-&-hove-albion', 'leicester-city'], ['manchester-united', 'swansea-city'], ['newcastle-united', 'huddersfield-town'], ['watford', 'afc-bournemouth'], ['west-bromwich-albion', 'burnley'], ['west-ham-united', 'southampton'], ['everton', 'manchester-city'], ['arsenal', 'stoke-city'], ['chelsea', 'tottenham-hotspur']]

WEEK_MATCHES = [['everton', 'liverpool'], ['afc-bournemouth', 'crystal-palace'], ['brighton-&-hove-albion', 'huddersfield-town'], ['leicester-city', 'newcastle-united'], ['stoke-city', 'tottenham-hotspur'], ['watford', 'burnley'], ['west-bromwich-albion', 'swansea-city'], ['manchester-city', 'manchester-united'], ['arsenal', 'southampton'], ['chelsea', 'west-ham-united']]