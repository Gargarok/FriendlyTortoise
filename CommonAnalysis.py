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

import_module("TeamConstants")
import_module("CommonMethods")
import_module("SqlQueries")

from SqlQueries import *
from CommonMethods import *
from TeamConstants import *

####--####--####--####--####--####
####  CONSTANTS
####--####--####--####--####--####

APP_FOLDER = "E:/Script/LigueMatches/"
DATABASE_FOLDER = "Database"
FOLDER_SEP = "/"

DATABASE_FILE = DATABASE_FOLDER + FOLDER_SEP + "panda_matches.db"

VALUES_TO_DISCOVER = 5
DISCOVERY_ACCURACY = 3
MONTE_CARLO_ITERATIONS = 2**14

def initCursor() :
  if not os.path.isfile(APP_FOLDER + DATABASE_FILE):
    print("Database " + DATABASE_FILE + " was not found. Exiting...")
    sys.exit()
 
  dbConn = sqlite3.connect(APP_FOLDER + DATABASE_FILE)
  cursor = dbConn.cursor()
  return cursor

def tryoutMode(cursor, matchDate, championship, teamList, varsMap) :  
  for key in varsMap.keys() :
    MUTABLE_VARS[key] = varsMap[key]

  nextMatchesDate = datetime.datetime.strptime(matchDate, "%d/%m/%Y")
  allTeamResults = getAllResults(nextMatchesDate, cursor, teamList, championship)
  coeffDict = computeTeamCoeff(allTeamResults)
  statDict = tryoutAlgorithm(matchDate, cursor, teamList, championship)

  if len(statDict) > 0 :
    totalVictPercent = statDict["vict"]
    totalLossPercent = statDict["loss"]
    totalDrawPercent = statDict["draws"]
    totalMatchOutputPercent = statDict["matchOutput"]
    totalExactPercent = statDict["exactRes"]
    totalGoalDiffAvg = statDict["avgGoalDiff"]

    print("###  ###  ###  ###  ###  ###  ###  ###  ###")
    print("###  ### ALGO TOTAL ACCURACY : " )
    print("### VICTORIES FOR HOME (%) : " + str(totalVictPercent))
    print("### LOSSES FOR HOME (%) : " + str(totalLossPercent))
    print("### DRAWS (%) : " + str(totalDrawPercent))
    print("### GOOD OUTPUT (%) : " + str(totalMatchOutputPercent))
    print("### EXACT RESULTS (%) : " + str(totalExactPercent))
    print("### GOALS DIFFERENCE (avg) : " + str(totalGoalDiffAvg))
    print("###  ###  ###  ###  ###  ###  ###  ###  ###")

def discMode(cursor, matchDate, championship, teamList, varsMap, printOutput) :
  for key in varsMap.keys() :
    MUTABLE_VARS[key] = varsMap[key]
  
  initCoeffLearning = MUTABLE_VARS["COEFF_LEARNING"] 
  initCoeffGoals = MUTABLE_VARS["COEFF_GOALS"] 
  initCoeffValue = MUTABLE_VARS["COEFF_VALUE"] 
  initCoeffExp = MUTABLE_VARS["COEFF_EXP"] 
  initCoeffTeamRange = MUTABLE_VARS["SIMILAR_TEAM_RANGE"] 
  initCoeffWinStreak = MUTABLE_VARS["COEFF_WIN_STREAK"] 
  
  lowIndexRange = - (int)(VALUES_TO_DISCOVER / 2.0)
  highIndexRange = (int)(VALUES_TO_DISCOVER/ 2.0) + 1
  
  totalIterations = (highIndexRange - lowIndexRange) ** 6.0
  print("TOTAL ITERATIONS: " + str(totalIterations))
  print("RANGE: " + str(range(lowIndexRange, highIndexRange)))
  
  stepDivide = VALUES_TO_DISCOVER * DISCOVERY_ACCURACY
  
  learningRange = [(x * initCoeffLearning)/stepDivide for x in range(lowIndexRange, highIndexRange)]
  goalsRange = [(x * initCoeffGoals)/stepDivide for x in range(lowIndexRange, highIndexRange)]
  valueRange = [(x * initCoeffValue)/stepDivide for x in range(lowIndexRange, highIndexRange)]
  expRange = [(x * initCoeffExp)/stepDivide for x in range(lowIndexRange, highIndexRange)]
  simiTeamRange = [(x * initCoeffTeamRange)/stepDivide for x in range(lowIndexRange, highIndexRange)]
  winStreakRange = [(x * initCoeffWinStreak)/stepDivide for x in range(lowIndexRange, highIndexRange)]

  bestVariables = {}
  bestGlobalOutput = 0.0
  bestExactProno = 0.0
  currentIteration = 0
  progress = 0.0
  for a in learningRange :
    MUTABLE_VARS["COEFF_LEARNING"] = initCoeffLearning + a
    for b in goalsRange :
      MUTABLE_VARS["COEFF_GOALS"] = initCoeffGoals + b
      for c in valueRange :
        MUTABLE_VARS["COEFF_VALUE"] = initCoeffValue + c
        for d in expRange :
          MUTABLE_VARS["COEFF_EXP"] = initCoeffExp + d
          for e in simiTeamRange :
            MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = initCoeffTeamRange + e
            for f in winStreakRange :
              MUTABLE_VARS["COEFF_WIN_STREAK"] = initCoeffWinStreak + f
              results = tryoutAlgorithm(matchDate, cursor, teamList, championship)    
              if results["matchOutput"] > bestGlobalOutput :
                bestGlobalOutput = results["matchOutput"]
                bestVariables["COEFF_VICT_GEN"] = MUTABLE_VARS["COEFF_VICT_GEN"]
                bestVariables["COEFF_DEF_GEN"] = MUTABLE_VARS["COEFF_DEF_GEN"]
                bestVariables["COEFF_DRAW_GEN"] = MUTABLE_VARS["COEFF_DRAW_GEN"]
                bestVariables["COEFF_SCORED_GEN"] = MUTABLE_VARS["COEFF_SCORED_GEN"]
                bestVariables["COEFF_TAKEN_GEN"] = MUTABLE_VARS["COEFF_TAKEN_GEN"]
                bestVariables["COEFF_LEARNING"] = MUTABLE_VARS["COEFF_LEARNING"]
                bestVariables["COEFF_GOALS"] = MUTABLE_VARS["COEFF_GOALS"]
                bestVariables["COEFF_VALUE"] = MUTABLE_VARS["COEFF_VALUE"]
                bestVariables["COEFF_EXP"] = MUTABLE_VARS["COEFF_EXP"]
                bestVariables["SIMILAR_TEAM_RANGE"] = MUTABLE_VARS["SIMILAR_TEAM_RANGE"]
                bestVariables["COEFF_WIN_STREAK"] = MUTABLE_VARS["COEFF_WIN_STREAK"]
                bestVariables["GLOBAL_COEFF"] = MUTABLE_VARS["GLOBAL_COEFF"]
                
                if printOutput :
                  print ("## ## New best match output : " + str(round(bestGlobalOutput, 2)) 
                       + "%, associated exact pronos : " + str(round(results["exactRes"], 2)) + "%, MUTABLE_VARS: "
                       + str(MUTABLE_VARS))
                  print("##     ##     ##")

              currentIteration += 1
              currentProgress = int(100.0 * currentIteration/totalIterations)
              if currentProgress > progress :
                progress = currentProgress
                if printOutput :
                  print("## ## ## ## " + str(progress) + "% done.")
  bestVariables["WIN_RATE"] = bestGlobalOutput                
  return bestVariables
  
def monteCarloMode (cursor, matchDate, championship, teamList, varsMap, printOutput) :
  for key in varsMap.keys() :
    MUTABLE_VARS[key] = varsMap[key]
  
  print("TOTAL ITERATIONS: " + str(MONTE_CARLO_ITERATIONS))
  progress = 0.0
  bestAvgGoalsDiff = 50.0
  bestExactProno = -1.0
  bestGlobalOutput = -1.0
  bestDraws = -1.0
  bestHomeVictories = -1.0
  bestHomeLosses = -1.0
  bestVariables = {}
  
  for iteration in range(0, MONTE_CARLO_ITERATIONS) :
    random.seed(iteration)
    standCoeffInit = randint(0, 30) * 1.0
    lowCoeffInit = 1.0/randint(1, 10)
    veryLowCoeffInit = randint(1, 800) * 1.0
    
    MUTABLE_VARS["COEFF_VICT_GEN"] = standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))
    MUTABLE_VARS["COEFF_DEF_GEN"] = standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))
    MUTABLE_VARS["COEFF_DRAW_GEN"] = standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))
    MUTABLE_VARS["COEFF_SCORED_GEN"] = standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))
    MUTABLE_VARS["COEFF_TAKEN_GEN"] = standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))
    MUTABLE_VARS["COEFF_LEARNING"] = standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))
    MUTABLE_VARS["COEFF_GOALS"] = standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))
    MUTABLE_VARS["COEFF_VALUE"] = (standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))) * 1.0/(randint(1, 700))
    MUTABLE_VARS["COEFF_EXP"] = (standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))) * 1.0/(randint(1, 700))
    MUTABLE_VARS["SIMILAR_TEAM_RANGE"] = 1.0 * randint(0, 100) + (randint(0, 10)/10.0)
    MUTABLE_VARS["COEFF_WIN_STREAK"] = randint(0, 15) + (randint(0, 10)/10.0)
    MUTABLE_VARS["GLOBAL_COEFF"] = (standCoeffInit - ((randint(0, 10)/10.0) + randint(0, standCoeffInit * 2.0))) * 1.0/(randint(1, 10))

    results = tryoutAlgorithm(matchDate, cursor, teamList, championship)

    currentProgress = int(100 * iteration/MONTE_CARLO_ITERATIONS)
    if currentProgress > progress :
      progress = currentProgress
      if printOutput :
        print("## ## ## ## " + str(progress) + "% done.")
    if results["matchOutput"] > bestGlobalOutput :
      bestGlobalOutput = results["matchOutput"]
      
      bestVariables["COEFF_VICT_GEN"] = MUTABLE_VARS["COEFF_VICT_GEN"]
      bestVariables["COEFF_DEF_GEN"] = MUTABLE_VARS["COEFF_DEF_GEN"]
      bestVariables["COEFF_DRAW_GEN"] = MUTABLE_VARS["COEFF_DRAW_GEN"]
      bestVariables["COEFF_SCORED_GEN"] = MUTABLE_VARS["COEFF_SCORED_GEN"]
      bestVariables["COEFF_TAKEN_GEN"] = MUTABLE_VARS["COEFF_TAKEN_GEN"]
      bestVariables["COEFF_LEARNING"] = MUTABLE_VARS["COEFF_LEARNING"]
      bestVariables["COEFF_GOALS"] = MUTABLE_VARS["COEFF_GOALS"]
      bestVariables["COEFF_VALUE"] = MUTABLE_VARS["COEFF_VALUE"]
      bestVariables["COEFF_EXP"] = MUTABLE_VARS["COEFF_EXP"]
      bestVariables["SIMILAR_TEAM_RANGE"] = MUTABLE_VARS["SIMILAR_TEAM_RANGE"]
      bestVariables["COEFF_WIN_STREAK"] = MUTABLE_VARS["COEFF_WIN_STREAK"]
      bestVariables["GLOBAL_COEFF"] = MUTABLE_VARS["GLOBAL_COEFF"]
      
      if printOutput :
        print ("##  ## New best match output : " + str(round(bestGlobalOutput, 2)) 
             + "%, associated exact pronos : " + str(round(results["exactRes"], 2)) + "%, MUTABLE_VARS: "
             + str(MUTABLE_VARS))
        print("##     ##     ##")
        
  bestVariables["WIN_RATE"] = bestGlobalOutput     
  return bestVariables

def pronoMode(cursor, matchDate, teamList, championship, matchesList, varsMap) :         
  for key in varsMap.keys() :
    MUTABLE_VARS[key] = varsMap[key]
  
  nextMatchesDate = datetime.datetime.strptime(matchDate, "%d/%m/%Y")
  allTeamResults = getAllResults(nextMatchesDate, cursor, teamList, championship)
  coeffDict = computeTeamCoeff(allTeamResults)
  statDict = resolveMatches(nextMatchesDate, matchesList, championship, coeffDict, allTeamResults, 1, cursor)

  if len(statDict) > 0 :
    totalVictPercent = statDict["vict"]
    totalLossPercent = statDict["loss"]
    totalDrawPercent = statDict["draws"]
    totalMatchOutputPercent = statDict["matchOutput"]
    totalExactPercent = statDict["exactRes"]
    totalGoalDiffAvg = statDict["avgGoalDiff"]

    outputString = ""
    outputString += "###  ###  ###  ###  ###  ###  ###  ###  ###\n"
    outputString += "###  ### ALGO TOTAL ACCURACY : \n"
    outputString += "### VICTORIES FOR HOME (%) : " + str(totalVictPercent) + "\n"
    outputString += "### LOSSES FOR HOME (%) : " + str(totalLossPercent) + "\n"
    outputString += "### DRAWS (%) : " + str(totalDrawPercent) + "\n"
    outputString += "### GOOD OUTPUT (%) : " + str(totalMatchOutputPercent) + "\n"
    outputString += "### EXACT RESULTS (%) : " + str(totalExactPercent) + "\n"
    outputString += "### GOALS DIFFERENCE (avg) : " + str(totalGoalDiffAvg) + "\n"
    outputString += "###  ###  ###  ###  ###  ###  ###  ###  ###\n"
    print(outputString)


  
