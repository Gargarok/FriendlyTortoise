#!/usr/bin/python3
#coding: utf-8

import re, io, os, sys, time
import datetime
import sqlite3
from importlib import import_module
from math import floor

import_module("TeamConstants")
import_module("SqlQueries")

from SqlQueries import *
from TeamConstants import *

DAYS_FOR_COEFFS = 90 

def tryoutAlgorithm(matchDate, cursor, teamList, championship) :
  allMatchesDates = {}
  getAllWeekDatesFrom(datetime.datetime.strptime(matchDate, "%d/%m/%Y"), cursor, allMatchesDates, teamList, championship)
  firstDate = datetime.datetime.strptime(matchDate, "%d/%m/%Y")

  allDates = []
  for date in allMatchesDates :
    allDates.append(date)
  allDates.sort()

  matches = []
  algoAccuracy = []
  for date in allDates :
    dayMatches = allMatchesDates[date]
    prevDate = datetime.datetime.strptime(date, "%Y-%m-%d") - datetime.timedelta(1)
    allTeamResults = getAllResults(prevDate, cursor, teamList, championship)
    coeffDict = computeTeamCoeff(allTeamResults)
    pronos = resolveMatches(prevDate, dayMatches, championship, coeffDict, allTeamResults, 0, cursor)
    algoAccuracy.append(pronos)

  totalVictPercent = 0.0
  totalLossPercent = 0.0
  totalDrawPercent = 0.0
  totalMatchOutputPercent = 0.0
  totalExactPercent = 0.0
  totalGoalDiffAvg = 0.0
  dayNumbers = len(algoAccuracy)
  for accuracyDetails in algoAccuracy :
    totalVictPercent += accuracyDetails["vict"]
    totalLossPercent += accuracyDetails["loss"]
    totalDrawPercent += accuracyDetails["draws"]
    totalMatchOutputPercent += accuracyDetails["matchOutput"]
    totalExactPercent += accuracyDetails["exactRes"]
    totalGoalDiffAvg += accuracyDetails["avgGoalDiff"]

  statDict = {}
  statDict["vict"] = totalVictPercent / dayNumbers
  statDict["loss"] = totalLossPercent / dayNumbers
  statDict["draws"] = totalDrawPercent / dayNumbers
  statDict["matchOutput"] = totalMatchOutputPercent / dayNumbers
  statDict["exactRes"] = totalExactPercent / dayNumbers
  statDict["avgGoalDiff"] = totalGoalDiffAvg / dayNumbers
  return statDict

def getActualMatchResult(date, championship, teamHome, teamAway, cursor) :
  cursor.execute(GET_MATCH_RESULT, [teamHome, teamAway, date.strftime('%Y-%m-%d'), championship])
  queryRes = cursor.fetchall()
  if not queryRes or len(queryRes) == 0 :
    return {}
  matchResult = queryRes[0]
  resultDict = {}

  if matchResult :
    resultDict["homeScore"] = matchResult[0]
    resultDict["awayScore"] = matchResult[1]
  return resultDict

def getAllWeekDatesFrom(matchDate, cursor, allMatchesWithDates, teamList, championship) :
  cursor.execute(GET_MATCH_DATES, [matchDate.strftime('%Y-%m-%d'), championship])
  matchQueryRes = cursor.fetchall()
  firstDate = matchQueryRes[0][0]
  i = 1
  for matchData in matchQueryRes :
    currentDate = matchData[0]
    awayTeam = matchData[1]
    homeTeam = matchData[2]
    if awayTeam in teamList and homeTeam in teamList :
      i += 1
      if currentDate not in allMatchesWithDates :
        allMatchesWithDates[currentDate] = []
      allMatchesWithDates[currentDate].append([homeTeam, awayTeam])
  return firstDate    
      
def resolveMatches(date, matchesList, championship, coeffDict, allTeamResults, withPrint, cursor) :
  goodMatchOutput = 0
  exactResults = 0
  totalGoalsDifference = 0
  goodLosses = 0.0    # for home team
  goodVictories = 0.0  # for home team
  goodDraws = 0.0
  totalMatches = 0.0
  totalVict = 0.0
  totalLosses = 0.0
  totalDraws = 0.0
  
  for couple in matchesList :
    homeName = couple[0]
    awayName = couple[1]
 
    homeData = coeffDict[homeName]
    awayData = coeffDict[awayName]

    homeAvgGoals = (homeData["homeScored"] + homeData["awayScored"]) / homeData["matchNumber"]
    homeAvgTaken = (homeData["homeTaken"] + homeData["awayTaken"]) / homeData["matchNumber"]
    awayAvgGoals = (awayData["homeScored"] + awayData["awayScored"]) / awayData["matchNumber"]
    awayAvgTaken = (awayData["homeTaken"] + awayData["awayTaken"]) / awayData["matchNumber"]
    
    homeCoeff = homeData[GENERAL_HOME]
    awayCoeff = awayData[GENERAL_AWAY]
    
    homeSimilarTeams = []
    awaySimilarTeams = []
    for team in coeffDict.keys() :
      teamCoeff = coeffDict[team][GENERAL_COEFF]

      coeffDiff = homeCoeff - teamCoeff
      if coeffDiff < MUTABLE_VARS["SIMILAR_TEAM_RANGE"] and coeffDiff > (-1 * MUTABLE_VARS["SIMILAR_TEAM_RANGE"]) :
        homeSimilarTeams.append(team)
      coeffDiff = awayCoeff - teamCoeff
      if coeffDiff < MUTABLE_VARS["SIMILAR_TEAM_RANGE"] and coeffDiff > (-1 * MUTABLE_VARS["SIMILAR_TEAM_RANGE"]) :
        awaySimilarTeams.append(team)

    matchNumber = 0
    allSimGoalsHome = 0
    allSimGoalsAway = 0

    awayExpGoalsTaken = 0
    awayExpGoalsScored = 0
    awayExpTotalMatches = 0
    awayExpVictories = 0
    awayExpLosses = 0
    awayExpDraws = 0
    for teamName in homeSimilarTeams :
      teamMatches = allTeamResults[teamName]
      for match in teamMatches :
        if match["opponent"] in awaySimilarTeams :
          allSimGoalsHome += match["goalsScored"]
          allSimGoalsAway += match["goalsTaken"]
          matchNumber += 1
        if match["opponent"] == awayName :
          awayExpGoalsTaken += match["goalsScored"]
          awayExpGoalsScored += match["goalsTaken"]
          if match["goalsScored"] > match["goalsTaken"] :
            awayExpLosses += 1
          elif match["goalsScored"] < match["goalsTaken"] :
            awayExpVictories += 1
          else :
            awayExpDraws += 1
          awayExpTotalMatches += 1

    homeExpGoalsTaken = 0
    homeExpGoalsScored = 0
    homeExpTotalMatches = 0
    homeExpVictories = 0
    homeExpLosses = 0
    homeExpDraws = 0
    for teamName in awaySimilarTeams :
      teamMatches = allTeamResults[teamName]
      for match in teamMatches :
        if match["opponent"] == homeName :
          homeExpGoalsTaken += match["goalsScored"]
          homeExpGoalsScored += match["goalsTaken"]
          if match["goalsScored"] > match["goalsTaken"] :
            homeExpLosses += 1
          elif match["goalsScored"] < match["goalsTaken"] :
            homeExpVictories += 1
          else :
            homeExpDraws += 1
          homeExpTotalMatches += 1

    if matchNumber > 0 :
      homeLearningCoeff = (allSimGoalsHome / matchNumber)
      awayLearningCoeff = (allSimGoalsAway / matchNumber)
    else :
      homeLearningCoeff = 0
      awayLearningCoeff = 0

    awayExpCoeff = 0
    homeExpCoeff = 0
    if awayExpTotalMatches > 0 :
      firstComponent = ((MUTABLE_VARS["COEFF_VICT_GEN"] * awayExpVictories / awayExpTotalMatches) +
                    (MUTABLE_VARS["COEFF_DRAW_GEN"] * awayExpDraws / awayExpTotalMatches) +
                    (MUTABLE_VARS["COEFF_DEF_GEN"] * awayExpLosses / awayExpTotalMatches) + ADD_MATCHES_GEN)

      secondComponent = ((MUTABLE_VARS["COEFF_SCORED_GEN"] * awayExpGoalsScored / awayExpTotalMatches) +
                    (MUTABLE_VARS["COEFF_TAKEN_GEN"] * awayExpGoalsTaken / awayExpTotalMatches) + ADD_GOALS_GEN)
      
      awayExpCoeff = firstComponent * secondComponent

    if homeExpTotalMatches > 0 :
      firstComponent = ((MUTABLE_VARS["COEFF_VICT_GEN"] * homeExpVictories / homeExpTotalMatches) +
                    (MUTABLE_VARS["COEFF_DRAW_GEN"] * homeExpDraws / homeExpTotalMatches) +
                    (MUTABLE_VARS["COEFF_DEF_GEN"] * homeExpLosses / homeExpTotalMatches) + ADD_MATCHES_GEN)
      secondComponent = ((MUTABLE_VARS["COEFF_SCORED_GEN"] * homeExpGoalsScored / homeExpTotalMatches) +
                    (MUTABLE_VARS["COEFF_TAKEN_GEN"] * homeExpGoalsTaken / homeExpTotalMatches) + ADD_GOALS_GEN)
      homeExpCoeff = firstComponent * secondComponent
      
    homeGoalCoeff = ((homeAvgGoals + awayAvgTaken) / 2)
    awayGoalCoeff = ((awayAvgGoals + homeAvgTaken) / 2)

    homeValueCoeff = (homeCoeff - awayCoeff)
    awayValueCoeff = (awayCoeff - homeCoeff)

    homeWinStreak = homeData["winStreak"]
    awayWinStreak = awayData["winStreak"]

    homeScoreProno = 0
    awayScoreProno = 0

    if awayExpCoeff == 0 or homeExpCoeff == 0 :
      homeScoreProno = round(MUTABLE_VARS["GLOBAL_COEFF"] * ((homeLearningCoeff * MUTABLE_VARS["COEFF_LEARNING"])
                               + (homeGoalCoeff * MUTABLE_VARS["COEFF_GOALS"])
                               + (homeValueCoeff * MUTABLE_VARS["COEFF_VALUE"])
                               + (homeWinStreak * MUTABLE_VARS["COEFF_WIN_STREAK"])))
        
      awayScoreProno = round(MUTABLE_VARS["GLOBAL_COEFF"] * ((awayLearningCoeff * MUTABLE_VARS["COEFF_LEARNING"])
                               + (awayGoalCoeff * MUTABLE_VARS["COEFF_GOALS"])
                               + (awayValueCoeff * MUTABLE_VARS["COEFF_VALUE"])
                               + (homeWinStreak * MUTABLE_VARS["COEFF_WIN_STREAK"])))
    else :
      homeScoreProno = round(MUTABLE_VARS["GLOBAL_COEFF"] * ((homeLearningCoeff * MUTABLE_VARS["COEFF_LEARNING"])
                               + (homeGoalCoeff * MUTABLE_VARS["COEFF_GOALS"])
                               + (homeValueCoeff * MUTABLE_VARS["COEFF_VALUE"])
                               + (homeExpCoeff * MUTABLE_VARS["COEFF_EXP"])
                               + (homeWinStreak * MUTABLE_VARS["COEFF_WIN_STREAK"])))
        
      awayScoreProno = round(MUTABLE_VARS["GLOBAL_COEFF"] * ((awayLearningCoeff * MUTABLE_VARS["COEFF_LEARNING"])
                               + (awayGoalCoeff * MUTABLE_VARS["COEFF_GOALS"])
                               + (awayValueCoeff * MUTABLE_VARS["COEFF_VALUE"])
                               + (awayExpCoeff * MUTABLE_VARS["COEFF_EXP"])
                               + (awayWinStreak * MUTABLE_VARS["COEFF_WIN_STREAK"])))

    homeAppendix = 0
    awayAppendix = 0
    teamCoeffDiff = round((homeCoeff - awayCoeff) / 80)
    if teamCoeffDiff < 0 :
      awayAppendix = teamCoeffDiff * -1
    else :
      homeAppendix = teamCoeffDiff
    homeStanding = floor(homeGoalCoeff + homeAppendix)
    awayStanding = floor(awayGoalCoeff + awayAppendix)

    if homeStanding < 0 :
      homeStanding = 0
    if awayStanding < 0 :
      awayStanding = 0
    
    if homeScoreProno > awayScoreProno :
      while homeStanding <= awayStanding :
        homeStanding += 1
    elif homeScoreProno < awayScoreProno :
      while awayStanding <= homeStanding :
        awayStanding += 1
    else :
      result = min(homeStanding, awayStanding)
      homeStanding = result
      awayStanding = result
    
    if withPrint : 
      print("###  ###  ###  ###")
      print("MATCH: " + homeName + " VS " + awayName)
      print("EXPECTED RESULT : ")
      print("###  " + homeName + " : " + str(homeStanding))
      print("###  " + awayName + " : " + str(awayStanding))
      print("###  ###  ###  ###")
      print("")

    homeVictoryProno = homeStanding - awayStanding   # > 0 if home won, = 0 if draw, and < 0 if loss 
 
    matchActualResult = getActualMatchResult(date, championship, homeName, awayName, cursor)

    if len(matchActualResult) > 0 :
      homeGoals = matchActualResult["homeScore"]
      awayGoals = matchActualResult["awayScore"]

      matchVictory = homeGoals - awayGoals
    
      if matchVictory > 0 :
        if homeVictoryProno > 0 :
          goodVictories += 1.0
          goodMatchOutput += 1.0
        totalVict += 1.0
        
      if matchVictory < 0 :
        if homeVictoryProno < 0 :
          goodLosses += 1.0
          goodMatchOutput += 1.0
        totalLosses += 1.0
        
      if matchVictory == 0 :
        if homeVictoryProno == 0 :
          goodDraws += 1.0
          goodMatchOutput += 1.0
        totalDraws += 1.0

      if homeGoals == homeStanding and awayGoals == awayStanding :
        exactResults += 1.0
      totalGoalsDifference += (abs(homeGoals - homeStanding) + abs(awayGoals - awayStanding))

  totalMatches = len(matchesList)
  if totalVict == 0 :
    totalVict = 1.0
  if totalLosses == 0 :
    totalLosses = 1.0
  if totalDraws == 0 :
    totalDraws = 1.0
    
  if totalMatches > 0 :
      #print("## ## GOOD MATCH OUTPUT: " + str(goodMatchOutput) + ", TOTAL MATCHES: " + str(totalMatches))
      matchOutputPercent = (goodMatchOutput / totalMatches) * 100
      victoriesPercent = (goodVictories / totalVict) * 100
      lossesPercent = (goodLosses / totalLosses) * 100
      drawsPercent = (goodDraws / totalDraws) * 100
      exactResultsPercent = (exactResults / totalMatches) * 100
      averageGoalDifference = totalGoalsDifference / totalMatches

      statDict = {}
      statDict["vict"] = round(victoriesPercent, 1)
      statDict["loss"] = round(lossesPercent, 1)
      statDict["draws"] = round(drawsPercent, 1)
      statDict["matchOutput"] = round(matchOutputPercent, 1)
      statDict["exactRes"] = round(exactResultsPercent, 1)
      statDict["avgGoalDiff"] = averageGoalDifference
      return statDict
  else :
    return {}

def getGeneralCoeff(scored, taken, victories, draws, defeats) :
  totalMatches = victories + draws + defeats
  if totalMatches == 0 :
      return 0
  allGoals = scored + taken

  firstComponent = ((MUTABLE_VARS["COEFF_VICT_GEN"] * victories / totalMatches) + (MUTABLE_VARS["COEFF_DRAW_GEN"] * draws / totalMatches) +
                    (MUTABLE_VARS["COEFF_DEF_GEN"] * defeats / totalMatches) + ADD_MATCHES_GEN)

  secondComponent = (MUTABLE_VARS["COEFF_SCORED_GEN"] * scored / totalMatches) + (MUTABLE_VARS["COEFF_TAKEN_GEN"] * taken / totalMatches) + ADD_GOALS_GEN
    
  return firstComponent * secondComponent

def getDefensiveCoeff(scored, taken, victories, draws, defeats) :
  totalMatches = victories + draws + defeats
  if totalMatches == 0 :
      return 0
  allGoals = scored + taken
  
  firstComponent = FIRST_COEFF_DEF * (
    COEFF_MATCHES_DEF * ((COEFF_VICT_DEF * victories / totalMatches) + (COEFF_DRAW_DEF * draws / totalMatches) + (COEFF_DEF_DEF * defeats / totalMatches))
    + ADD_MATCHES_DEF
    )

  secondComponent = 0
  if not allGoals == 0 :
    secondComponent = SCD_COEFF_DEF * (
      COEFF_GOALS_DEF *(COEFF_SCORED_DEF * scored / allGoals + COEFF_TAKEN_DEF * taken / allGoals)
      + ADD_GOALS_DEF
    )
  return firstComponent + secondComponent

def getOffensiveCoeff(scored, taken, victories, draws, defeats) :
  totalMatches = victories + draws + defeats
  if totalMatches == 0 :
      return 0
  allGoals = scored + taken
  
  firstComponent = FIRST_COEFF_OFF * (
    COEFF_MATCHES_OFF * ((COEFF_VICT_OFF * victories / totalMatches) + (COEFF_DRAW_OFF * draws / totalMatches) + (COEFF_DEF_OFF * defeats / totalMatches))
    + ADD_MATCHES_OFF
    )
  
  secondComponent = 0
  if not allGoals == 0 :  
    secondComponent = SCD_COEFF_OFF * (
      COEFF_GOALS_OFF *(COEFF_SCORED_OFF * scored / allGoals + COEFF_TAKEN_OFF * taken / allGoals)
      + ADD_GOALS_OFF
    )
  return firstComponent + secondComponent
  #retCoeff = (COEFF_VICT_OFF * victories / totalMatches) + (COEFF_DRAW_OFF * draws / totalMatches) + (COEFF_DEF_OFF * defeats / totalMatches) + (COEFF_SCORED_OFF * scored / allGoals)
  #return retCoeff
  
def computeTeamCoeff(teamDescription) :
  allCoeffs = {}
  for teamName in teamDescription.keys() :
    awayScored = 0
    awayTaken = 0
    awayVictories = 0
    awayDraws = 0
    awayLosses = 0
    homeScored = 0
    homeTaken = 0
    homeVictories = 0
    homeDraws = 0
    homeLosses = 0
    
    teamData = teamDescription[teamName]
    winStreak = 0
    for match in teamData :
      goalsScored = match["goalsScored"]
      goalsTaken = match["goalsTaken"]
      goalsDiff = goalsScored - goalsTaken
      
      if match["isHome"] :
        homeScored += goalsScored
        homeTaken += goalsTaken
        if goalsDiff > 0 :
          winStreak += 1
          homeVictories += 1
        elif goalsDiff < 0 :
          winStreak = 0
          homeLosses += 1
        else :
          winStreak = 0
          homeDraws += 1
      else :  
        awayScored += goalsScored
        awayTaken += goalsTaken
        if goalsDiff > 0 :
          winStreak += 1
          awayVictories += 1
        elif goalsDiff < 0 :
          winStreak = 0
          awayLosses += 1
        else :
          winStreak = 0
          awayDraws += 1

    teamCoeffs = {}
    teamCoeffs["winStreak"] = winStreak
    teamCoeffs["awayScored"] = awayScored
    teamCoeffs["awayTaken"] = awayTaken
    teamCoeffs["homeScored"] = homeScored
    teamCoeffs["homeTaken"] = homeTaken
    teamCoeffs["matchNumber"] = awayVictories + awayDraws + awayLosses + homeVictories + homeDraws + homeLosses

    if teamCoeffs["matchNumber"] > 0 :
      teamCoeffs[GENERAL_COEFF] = getGeneralCoeff(awayScored + homeScored, awayTaken + homeTaken, homeVictories + awayVictories,
                                                homeDraws + awayDraws, homeLosses + awayLosses)
      teamCoeffs[GENERAL_HOME] = getGeneralCoeff(homeScored, homeTaken, homeVictories, homeDraws, homeLosses)
      teamCoeffs[GENERAL_AWAY] = getGeneralCoeff(awayScored, awayTaken, awayVictories, awayDraws, awayLosses)
 
      allCoeffs[teamName] = teamCoeffs
  return allCoeffs

def createDictForMatch(opponentName, opponentGoals, teamGoals, isHome) :
  return {"opponent": opponentName, "goalsTaken": opponentGoals, "goalsScored": teamGoals, "isHome": isHome}

## Takes a date object and returns a dictionnary with info on every team's matches
## before the given date
def getAllResults(matchDate, cursor, teamList, championship) :
  allMatches = {}
  startDate = matchDate - datetime.timedelta(DAYS_FOR_COEFFS)
  cursor.execute(GET_MATCH_DATA, [matchDate.strftime('%Y-%m-%d'), startDate, championship])
  matchQueryRes = cursor.fetchall()
  for matchData in matchQueryRes :
    homeName = matchData[0]
    awayName = matchData[1]
    if (awayName in teamList) and (homeName in teamList) :
      homeGoals = int(matchData[2])
      awayGoals = int(matchData[3])

      if not homeName in allMatches.keys() :
        allMatches[homeName] = []
      if not awayName in allMatches.keys() :
        allMatches[awayName] = []
      matchDictHome = createDictForMatch(awayName, awayGoals, homeGoals, 1)
      matchDictAway = createDictForMatch(homeName, homeGoals, awayGoals, 0)
      allMatches[homeName].append(matchDictHome)
      allMatches[awayName].append(matchDictAway)
  return allMatches


