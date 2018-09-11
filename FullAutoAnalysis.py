#!/usr/bin/python3
#coding: utf-8

'''
#
# Does things
# 
'''

import re, io, os, sys, time
import datetime
import sqlite3
import random
from importlib import import_module
from random import seed
from random import randint

#import_module("FullAutoConstants")
import_module("CommonAnalysis")
import_module("TeamConstants")

from CommonAnalysis import *
from BundesLAAlgorithmConstants import *

####--####--####--####--####--####
####  CONSTANTS
####--####--####--####--####--####

AUTO_MODE = "auto"
ALLOWED_MODES = [AUTO_MODE]
LAUNCH_MODE = "NONE"

OUTPUT_FILE = "varOptimalOutput.txt"

ALL_LEAGUES = [{'name': BUNDESLIGA_NAME, 'teams': BUNDESLIGA_TEAMS},
  {'name': LIGUE_ONE_NAME, 'teams': LIGUEONE_TEAMS},
  {'name': LIGUE_TWO_NAME, 'teams': LIGUETWO_TEAMS},
  {'name': PREMIER_LEAGUE_NAME, 'teams': PREMIERLEAGUE_TEAMS},
  {'name': SPANISH_LIGA_NAME, 'teams': SPANISH_LIGA_TEAMS},
  {'name': ITA_SERIE_A_NAME, 'teams': ITA_SERIE_A_TEAMS},
  {'name': PORTUGAL_LIGA_NAME, 'teams': PORTUGAL_LIGA_TEAMS},
]

####--####--####--####--####--####
####  SCRIPT EXECUTION
####--####--####--####--####--####

matchDate = ""
if len(sys.argv) > 2 :
  matchDate = sys.argv[1]
  modeText = sys.argv[2]
  if modeText in ALLOWED_MODES :
    LAUNCH_MODE = modeText
  else:
    LAUNCH_MODE = "NONE"
else :
  print("Need. More. Arguments. Eat.")
  print("Usage : python3 <file.py> initial_date(dd/mm/yyyy) <mode>")
  print("Replace <mode> with " + TRYOUT_MODE + " for algorithm tryout, and with " + PRONO_MODE + " for this week's pronostics.")
  sys.exit()
  
cursor = initCursor()

if LAUNCH_MODE == AUTO_MODE :
  with open(OUTPUT_FILE, 'w') as outputFile :
    for teamDict in ALL_LEAGUES :
      print("Processing league " + teamDict['name'] + " ...")
      bestVars = monteCarloMode(cursor, matchDate, teamDict['name'], teamDict['teams'], MUTABLE_VARS, 0)
      finalVars = discMode(cursor, matchDate, teamDict['name'], teamDict['teams'], bestVars, 0)
      
      outputFile.write("## ## RESULTS FOR LEAGUE " + teamDict['name'] + " ## ##\n")
      outputFile.write("## ## WIN RATE: " + str(round(finalVars['WIN_RATE'], 2)) + "%\n")
      for key in finalVars.keys() :
        if key == 'WIN_RATE' :
          continue
        outputFile.write("MUTABLE_VARS[\"" + str(key) + "\"] = " + str(round(finalVars[key], 5)) + "\n")
      outputFile.write("\n\n")
      print(teamDict['name'] + " done ! We keep going !")
else :
  print ("No known actions were asked. Exiting...")


  
