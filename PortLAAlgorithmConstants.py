#!/usr/bin/python3
#coding: utf-8

# post 08/02/2018
DEFAULT_MATCHES_14 = [["pa√ßos-de-ferreira", "tondela"], ["rio-ave", "maritimo"], ["braga", "vitoria-setubal"], ["portimonense", "benfica"], ["gd-chaves", "fc-porto"], ["belenenses", "desportivo-aves"], ["sporting-cp", "feirense"], ["boavista", "guimaraes"], ["moreirense", "estoril"], ]

# post 15/02/2018
DEFAULT_MATCHES_15 = [["feirense", "portimonense"], ["desportivo-aves", "maritimo"], ["benfica", "boavista"], ["estoril", "belenenses"], ["moreirense", "gd-chaves"], ["vitoria-setubal", "pa√ßos-de-ferreira"], ["fc-porto", "rio-ave"], ["guimaraes", "braga"], ["tondela", "sporting-cp"], ]

# post 22/02/2018
DEFAULT_MATCHES_16 = [["rio-ave", "desportivo-aves"], ["belenenses", "feirense"], ["maritimo", "guimaraes"], ["pa√ßos-de-ferreira", "benfica"], ["gd-chaves", "estoril"], ["boavista", "vitoria-setubal"], ["portimonense", "fc-porto"], ["braga", "tondela"], ["sporting-cp", "moreirense"], ]

# post 01/03/2018
DEFAULT_MATCHES_17 = [["fc-porto", "sporting-cp"], ["feirense", "boavista"], ["benfica", "maritimo"], ["estoril", "braga"], ["tondela", "gd-chaves"], ["moreirense", "pa√ßos-de-ferreira"], 
  ["vitoria-setubal", "rio-ave"], ["guimaraes", "belenenses"], ["desportivo-aves", "portimonense"], ]
  
# post 08/03/2018
DEFAULT_MATCHES_18 = [["braga", "moreirense"], ["rio-ave", "feirense"], ["benfica", "desportivo-aves"], ["boavista", "estoril"], 
  ["portimonense", "guimaraes"], ["maritimo", "vitoria-setubal"], ["belenenses", "tondela"], ["pa√ßos-de-ferreira", "fc-porto"], 
  ["gd-chaves", "sporting-cp"], ]

# post 15/03/2018
DEFAULT_MATCHES_X = [["vitoria-setubal", "portimonense"], ["tondela", "maritimo"], ["estoril", "pa√ßos-de-ferreira"], ["feirense", "benfica"], 
  ["fc-porto", "boavista"], ["moreirense", "belenenses"], ["guimaraes", "desportivo-aves"], ["gd-chaves", "braga"], 
  ["sporting-cp", "rio-ave"], ]  
  
# Vitoria-SC = guimaraes
PORTUGAL_LIGA_TEAMS = ["fc-porto", "benfica", "sporting-cp", "braga", "rio-ave", "maritimo", "gd-chaves", "guimaraes",
  "boavista", "tondela", "portimonense", "belenenses", "pa√ßos-de-ferreira", "feirense", "moreirense", "estoril",
  "vitoria-setubal", "desportivo-aves",]

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

## January
## New best match output : 69.55%, MUTABLE_VARS: {
MUTABLE_VARS["COEFF_VICT_GEN"] = -9.5
MUTABLE_VARS["COEFF_DEF_GEN"] = 4.6
MUTABLE_VARS["COEFF_DRAW_GEN"] = -14.1
MUTABLE_VARS["COEFF_SCORED_GEN"] = -0.2
MUTABLE_VARS["COEFF_TAKEN_GEN"] = -13.0
MUTABLE_VARS["COEFF_LEARNING"] = 14.3
MUTABLE_VARS["COEFF_GOALS"] = 5.97333
MUTABLE_VARS["COEFF_VALUE"] = -0.01676
MUTABLE_VARS["COEFF_EXP"] = -0.01284
MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 100.8
MUTABLE_VARS["COEFF_WIN_STREAK"] = 0.56
MUTABLE_VARS["GLOBAL_COEFF"] = 1.9





DEFAULT_MATCHES_X = ["['desportivo-aves', 'vitoria-setubal']", "['maritimo', 'feirense']", "['rio-ave', 'estoril']", "['boavista', 'tondela']", "['paÁos-de-ferreira', 'gd-chaves']", "['portimonense', 'moreirense']", "['benfica', 'guimaraes']", "['braga', 'sporting-cp']", "['belenenses', 'fc-porto']", "['estoril', 'maritimo']", "['fc-porto', 'desportivo-aves']", "['feirense', 'braga']", "['gd-chaves', 'belenenses']", "['guimaraes', 'rio-ave']", "['moreirense', 'boavista']", "['sporting-cp', 'paÁos-de-ferreira']", "['tondela', 'portimonense']", "['vitoria-setubal', 'benfica']"]

DEFAULT_MATCHES_X = [['desportivo-aves', 'vitoria-setubal'], ['maritimo', 'feirense'], ['rio-ave', 'estoril'], ['boavista', 'tondela'], ['paÁos-de-ferreira', 'gd-chaves'], ['portimonense', 'moreirense'], ['benfica', 'guimaraes'], ['braga', 'sporting-cp'], ['belenenses', 'fc-porto'], ['estoril', 'maritimo'], ['fc-porto', 'desportivo-aves'], ['feirense', 'braga'], ['gd-chaves', 'belenenses'], ['guimaraes', 'rio-ave'], ['moreirense', 'boavista'], ['sporting-cp', 'paÁos-de-ferreira'], ['tondela', 'portimonense'], ['vitoria-setubal', 'benfica']]

WEEK_MATCHES = [['paÁos-de-ferreira', 'braga'], ['desportivo-aves', 'feirense'], ['portimonense', 'estoril'], ['boavista', 'gd-chaves'], ['guimaraes', 'vitoria-setubal'], ['maritimo', 'moreirense'], ['benfica', 'fc-porto'], ['belenenses', 'sporting-cp'], ['rio-ave', 'tondela'], ['braga', 'maritimo']]