#!/usr/bin/python3
#coding: utf-8

LIGUE_ONE_NAME = "LIGUEONE"
LIGUE_TWO_NAME = "LIGUETWO"
PREMIER_LEAGUE_NAME = "PREMIERLEAGUE"
SPANISH_LIGA_NAME = "SPANISHLIGA"
ITA_SERIE_A_NAME = "ITASERIEA"
BUNDESLIGA_NAME = "BUNDESLIGA"
PORTUGAL_LIGA_NAME = "PORTUGALSERIEA"
ARG_SUPERLIGA_NAME  = "ARGSUPERLIGA"

LEAGUE_ONE_MATCHES_URL = "http://www.espn.com/soccer/scoreboard/_/league/FRA.1/date/"
LEAGUE_TWO_MATCHES_URL = "http://www.espn.com/soccer/scoreboard/_/league/FRA.2/date/"
PREMIER_LEAGUE_MATCHES_URL = "http://www.espn.com/soccer/scoreboard/_/league/ENG.1/date/"
BUNDESLIGA_URL = "http://www.espn.com/soccer/scoreboard/_/league/GER.1/date/"
ITA_SERIE_A_URL = "http://www.espn.com/soccer/scoreboard/_/league/ITA.1/date/"
SPANISH_LIGA_URL = "http://www.espn.com/soccer/scoreboard/_/league/ESP.1/date/"
PORTUGAL_LIGA_URL = "http://www.espn.com/soccer/scoreboard/_/league/POR.1/date/"

LIGUEONE_TEAMS = ["stade-rennes", "bordeaux", "angers", "paris-saint-germain", "troyes", "strasbourg", "montpellier", "sc-amiens",
  "as-monaco", "guingamp", "nantes", "toulouse", "nice", "dijon-fco", "metz", "lille",
  "marseille", "caen", "st-etienne", "lyon",]

LIGUETWO_TEAMS = ["stade-de-reims", "nimes", "ac-ajaccio", "le-havre-ac", "brest", "paris-fc", "lorient", "sochaux",
  "clermont-foot", "chateauroux", "niort", "valenciennes", "gfc-ajaccio", "lens", "as-nancy-lorraine", "aj-auxerre",
  "us-quevilly", "tours", "bourg-peronnas", "orléans",]

PREMIERLEAGUE_TEAMS = ["manchester-city", "manchester-united", "chelsea", "liverpool", "arsenal", "burnley", "tottenham-hotspur",
  "leicester-city", "everton", "watford", "huddersfield-town", "southampton", "brighton-&-hove-albion",
  "crystal-palace", "west-ham-united", "afc-bournemouth", "stoke-city", "newcastle-united",
  "west-bromwich-albion", "swansea-city",]
                       
SPANISH_LIGA_TEAMS = ["barcelona", "atletico-madrid", "valencia", "real-madrid", "villarreal", "sevilla-fc", "celta-vigo", "eibar"
  , "getafe", "girona", "leganes", "athletic-bilbao", "real-betis", "espanyol", "real-sociedad", "levante"
  , "alavés", "deportivo-la-coruña", "las-palmas", "málaga",]
                   
BUNDESLIGA_TEAMS = ["bayern-munich", "bayer-leverkusen", "schalke-04", "eintracht-frankfurt", "rb-leipzig", "borussia-dortmund", 
   "borussia-monchengladbach", "fc-augsburg" , "tsg-hoffenheim", "hannover-96", "hertha-berlin", "sc-freiburg", "vfl-wolfsburg", 
   "vfb-stuttgart", "mainz", "werder-bremen", "hamburg-sv", "fc-cologne",]
                   
ITA_SERIE_A_TEAMS = ["napoli", "juventus", "lazio", "internazionale", "as-roma", "sampdoria", "ac-milan", "atalanta",
  "udinese", "torino", "fiorentina", "bologna", "chievo-verona", "sassuolo", "genoa", "cagliari",
  "crotone", "spal", "hellas-verona", "benevento",]
                   
ARGENTINA_SUPERLIGA_TEAMS = ["boca-juniors", "san-lorenzo", "unión-de-sante-fe", "talleres-de-córdoba", "huracán", 
  "belgrano-de-córdoba", "independiente", "argentinos-juniors", "cólon-de-santa-fe", "godoy-cruz-de-mendoza", 
  "estudiantes-la-plata", "san-martín-de-san-juan", "atlético-tucumán", "banfield", "defense-y-justicia", 
  "vélez-sarsfield", "racing-club", "patronato", "gimnasia-la-plata", "river-plate", "rosario-central", "lanús", 
  "newell's-old-boys", "temperley", "chacarita-juniors", "olimpo-de-bahía-blanca", "tigre", "arsenal-de-sarandí",]
                   
PORTUGAL_LIGA_TEAMS = ["fc-porto", "benfica", "sporting-cp", "braga", "rio-ave", "maritimo", "gd-chaves", "guimaraes",
  "boavista", "tondela", "portimonense", "belenenses", "paços-de-ferreira", "feirense", "moreirense", "estoril",
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


