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

import_module("ArgSLAAlgorithmConstants")
import_module("CommonAnalysis")
import_module("TeamConstants")

from CommonAnalysis import *
from ArgSLAAlgorithmConstants import *

####--####--####--####--####--####
####  CONSTANTS
####--####--####--####--####--####

PRONO_MODE = "pr"
TRYOUT_MODE = "tr"
MONTE_CARLO_TRYOUT_MODE = "mctr"
EXH_DISCOVERY_MODE = "disc"    # exhaustive discovery

ALLOWED_MODES = [PRONO_MODE, TRYOUT_MODE, MONTE_CARLO_TRYOUT_MODE, EXH_DISCOVERY_MODE]

LAUNCH_MODE = "NONE"

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

if LAUNCH_MODE == TRYOUT_MODE :  
  tryoutMode(cursor, matchDate, ARG_SUPERLIGA_NAME, ARGENTINA_SUPERLIGA_TEAMS, MUTABLE_VARS)
elif LAUNCH_MODE == EXH_DISCOVERY_MODE :
  discMode(cursor, matchDate, ARG_SUPERLIGA_NAME, ARGENTINA_SUPERLIGA_TEAMS, MUTABLE_VARS)
elif LAUNCH_MODE == MONTE_CARLO_TRYOUT_MODE :
  monteCarloMode(cursor, matchDate, ARG_SUPERLIGA_NAME, ARGENTINA_SUPERLIGA_TEAMS, MUTABLE_VARS)
elif LAUNCH_MODE == PRONO_MODE :          
  pronoMode(cursor, matchDate, ARGENTINA_SUPERLIGA_TEAMS, ARG_SUPERLIGA_NAME, WEEK_MATCHES, MUTABLE_VARS)
else :
  print ("No known actions were asked. Exiting...")


  
