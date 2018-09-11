#!/usr/bin/python3
#coding: utf-8

# post 12/01/2018
DEFAULT_MATCHES_14 = [["chelsea", "leicestercity"], ["crystalpalace", "burnley"], ["huddersfieldtown", "westhamunited"], ["newcastleunited", "swanseacity"], ["watford", "southampton"], ["westbromwichalbion", "brighton&hovealbion"], ["tottenhamhotspur", "everton"], ["afcbournemouth", "arsenal"], ["liverpool", "manchestercity"], ["manchesterunited", "stokecity"],]

# post 15/02/2018
DEFAULT_MATCHES_15 = [["girona", "leganes"], ["las-palmas", "sevilla-fc"], ["eibar", "barcelona"], ["alavés", "deportivo-la-coruña"], ["málaga", "valencia"], ["real-sociedad", "levante"], ["atletico-madrid", "athletic-bilbao"], ["espanyol", "villarreal"], ["real-betis", "real-madrid"], ["getafe", "celta-vigo"],]

# post 21/02/2018
DEFAULT_MATCHES_16 = [["deportivo-la-coruña", "espanyol"], ["celta-vigo", "eibar"], ["real-madrid", "alavés"], ["leganes", "las-palmas"], ["barcelona", "girona"], ["villarreal", "getafe"], ["athletic-bilbao", "málaga"], ["valencia", "real-sociedad"], ["sevilla-fc", "atletico-madrid"], ["levante", "real-betis"],]

# post 26/02/2018
DEFAULT_MATCHES_17 = [["espanyol", "real-madrid"], ["girona", "celta-vigo"], ["málaga", "sevilla-fc"], ["getafe", "deportivo-la-coruña"], ["athletic-bilbao", "valencia"], ["eibar", "villarreal"], ["atletico-madrid", "leganes"], ["real-betis", "real-sociedad"], ["las-palmas", "barcelona"], ["alavés", "levante"],]

# post 01/03/2018
DEFAULT_MATCHES_18 = [["villarreal", "girona"], ["sevilla-fc", "athletic-bilbao"], ["deportivo-la-coruña", "eibar"], ["leganes", "málaga"], ["real-madrid", "getafe"], 
  ["levante", "espanyol"], ["barcelona", "atletico-madrid"], ["real-sociedad", "alavés"], ["valencia", "real-betis"], ["celta-vigo", "las-palmas"],]

# post 08/03/2018
DEFAULT_MATCHES_19 = [["girona", "deportivo-la-coruña"], ["eibar", "real-madrid"], ["sevilla-fc", "valencia"], 
  ["getafe", "levante"], ["málaga", "barcelona"], ["espanyol", "real-sociedad"], ["atletico-madrid", "celta-vigo"], 
  ["las-palmas", "villarreal"], ["athletic-bilbao", "leganes"], ["alavés", "real-betis"],]

# post 15/03/2018
DEFAULT_MATCHES_X = [["levante", "eibar"], ["deportivo-la-coruña", "las-palmas"], ["valencia", "alavés"], 
  ["real-sociedad", "getafe"], ["real-betis", "espanyol"], ["leganes", "sevilla-fc"], ["barcelona", "athletic-bilbao"], 
  ["villarreal", "atletico-madrid"], ["celta-vigo", "málaga"], ["real-madrid", "girona"],]  
  
SPANISH_LIGA_TEAMS = ["barcelona", "atletico-madrid", "valencia", "real-madrid", "villarreal", "sevilla-fc", "celta-vigo", "eibar"
  , "getafe", "girona", "leganes", "athletic-bilbao", "real-betis", "espanyol", "real-sociedad", "levante"
  , "alavés", "deportivo-la-coruña", "las-palmas", "málaga",]

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

## January + February
## ## 90 DAYS, New best match output : 70.24 %
MUTABLE_VARS["COEFF_VICT_GEN"] = -0.4
MUTABLE_VARS["COEFF_DEF_GEN"] = -7.5
MUTABLE_VARS["COEFF_DRAW_GEN"] = -15.9
MUTABLE_VARS["COEFF_SCORED_GEN"] = 0.4
MUTABLE_VARS["COEFF_TAKEN_GEN"] = 7.5
MUTABLE_VARS["COEFF_LEARNING"] = -16.8
MUTABLE_VARS["COEFF_GOALS"] = -4.7
MUTABLE_VARS["COEFF_VALUE"] = -0.01265
MUTABLE_VARS["COEFF_EXP"] = 0.0377
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 39.6
MUTABLE_VARS["COEFF_WIN_STREAK"] = 4.6
MUTABLE_VARS["GLOBAL_COEFF"] = -0.3





DEFAULT_MATCHES_X = ["['girona', 'levante']", "['athletic-bilbao', 'celta-vigo']", "['las-palmas', 'real-madrid']", "['sevilla-fc', 'barcelona']", "['espanyol', 'alav�s']", "['leganes', 'valencia']", "['eibar', 'real-sociedad']", "['m�laga', 'villarreal']", "['atletico-madrid', 'deportivo-la-coru�a']", "['getafe', 'real-betis']"]

DEFAULT_MATCHES_X = [['girona', 'levante'], ['athletic-bilbao', 'celta-vigo'], ['las-palmas', 'real-madrid'], ['sevilla-fc', 'barcelona'], ['espanyol', 'alav�s'], ['leganes', 'valencia'], ['eibar', 'real-sociedad'], ['m�laga', 'villarreal'], ['atletico-madrid', 'deportivo-la-coru�a'], ['getafe', 'real-betis']]

WEEK_MATCHES = [['deportivo-la-coru�a', 'm�laga'], ['alav�s', 'getafe'], ['celta-vigo', 'sevilla-fc'], ['real-betis', 'eibar'], ['barcelona', 'leganes'], ['levante', 'las-palmas'], ['real-madrid', 'atletico-madrid'], ['real-sociedad', 'girona'], ['valencia', 'espanyol'], ['villarreal', 'athletic-bilbao']]