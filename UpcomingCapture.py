#!/usr/bin/python3
#coding: utf-8

'''
#
# Does things
# 
'''

import re, io, os, sys, time
import urllib.request
import datetime
from importlib import import_module
import sqlite3

import_module("SqlQueries")
import_module("TeamConstants")

from SqlQueries import *
from TeamConstants import *

APP_FOLDER = "E:/Script/LigueMatches/"
DATABASE_FOLDER = "Database"
FOLDER_SEP = "/"

ALL_LEAGUES = [{'name': BUNDESLIGA_NAME, 'teams': BUNDESLIGA_TEAMS, 'url': BUNDESLIGA_URL, 'file': 'BundesLAAlgorithmConstants.py'},
  {'name': LIGUE_ONE_NAME, 'teams': LIGUEONE_TEAMS, 'url': LEAGUE_ONE_MATCHES_URL, 'file': 'LOAlgorithmConstants.py'},
  {'name': LIGUE_TWO_NAME, 'teams': LIGUETWO_TEAMS, 'url': LEAGUE_TWO_MATCHES_URL, 'file': 'LTAlgorithmConstants.py'},
  {'name': PREMIER_LEAGUE_NAME, 'teams': PREMIERLEAGUE_TEAMS, 'url': PREMIER_LEAGUE_MATCHES_URL, 'file': 'PLAlgorithmConstants.py'},
  {'name': SPANISH_LIGA_NAME, 'teams': SPANISH_LIGA_TEAMS, 'url': SPANISH_LIGA_URL, 'file': 'SpanLAAlgorithmConstants.py'},
  {'name': ITA_SERIE_A_NAME, 'teams': ITA_SERIE_A_TEAMS, 'url': ITA_SERIE_A_URL, 'file': 'ItaSAAlgorithmConstants.py'},
  {'name': PORTUGAL_LIGA_NAME, 'teams': PORTUGAL_LIGA_TEAMS, 'url': PORTUGAL_LIGA_URL, 'file': 'PortLAAlgorithmConstants.py'},
]

MATCH_DATA_URL = "http://www.espnfc.com/matchstats?gameId="
DATE_URL_APPENDIX = "?date="

DATABASE_FILE = DATABASE_FOLDER + FOLDER_SEP + "panda_matches.db"

TEAM_TABLE = "team"
MATCH_TABLE = "match"

MATCHES_IDS_PAT = "(?:report|match)\?gameId=(\d+)"
HOME_TEAM_ID_PAT = "espn.gamepackage.homeTeamId *= *\"(\d+)\""
AWAY_TEAM_ID_PAT = "espn.gamepackage.awayTeamId *= *\"(\d+)\""
HOME_TEAM_NAME_PAT = "espn.gamepackage.homeTeamName *= *\"(.+?)\""
AWAY_TEAM_NAME_PAT = "espn.gamepackage.awayTeamName *= *\"(.+?)\""
HOME_SCORE_PAT = "data-home-away=\"home\" data-stat=\"score\">\s*(\d+)"
AWAY_SCORE_PAT = "data-home-away=\"away\" data-stat=\"score\">\s*(\d+)"
DATE_PATTERN = "<div class=\"game-status\">\s*<span data-date=\"(\d{4})-(\d{2})-(\d{2}).*?\""     # Groups: 1:Year, 2:Month, 3:Day
SCOREBOARD_PATTERN = "<script>window.espn.scoreboardData.*?</script>"

MIN_MATCHES_TO_GET = 10

def getPage (url):
  html = ""
  with urllib.request.urlopen(url) as response :
    bytesPage = response.read()
    html = bytesPage.decode("utf8")
  return html

def insertTeamIfNotExist (teamId, teamName, allTeams, cursor):
  if not teamId in allTeams :
    cursor.execute(INSERT_TEAM_NO_ID, [teamId, teamName])
    allTeams.add(teamId)

#############################################
## ## ##   MAIN PROCESS
#############################################

databaseExists = True

if not os.path.isfile(APP_FOLDER + DATABASE_FILE):
  databaseExists = False

dbConn = sqlite3.connect(APP_FOLDER + DATABASE_FILE)
cursor = dbConn.cursor()

print("Initializing...")
if not databaseExists:
  print("Database does not exists ; creating ...")
  cursor.execute(DATABASE_INIT_TEAM)
  cursor.execute(DATABASE_INIT_MATCH)
  cursor.execute(DATABASE_INIT_FORESEEN)
  dbConn.commit()

print("Getting existing foreseen matches...")
allMatches = set()
cursor.execute(ALL_FORESEEN)
tuples = cursor.fetchall()
for tuple in tuples :
  allMatches.add(str(tuple[0]))

print("Getting teams...")
allTeams = set()
cursor.execute(ALL_TEAMS)
tuples = cursor.fetchall()
for tuple in tuples :
  allTeams.add(str(tuple[0]))

matchIdPat = re.compile(MATCHES_IDS_PAT)
awayTeamIdPat = re.compile(AWAY_TEAM_ID_PAT)
homeTeamIdPat = re.compile(HOME_TEAM_ID_PAT)
awayTeamNamePat = re.compile(AWAY_TEAM_NAME_PAT)
homeTeamNamePat = re.compile(HOME_TEAM_NAME_PAT)
awayScorePat = re.compile(AWAY_SCORE_PAT)
homeScorePat = re.compile(HOME_SCORE_PAT)
matchDatePat = re.compile(DATE_PATTERN)

todayDate = datetime.date.today()

print("INITIALIZATION DONE ! Starting the gathering process...")
for leagueDict in ALL_LEAGUES :
  leagueName = leagueDict["name"]
  leagueTeams = leagueDict["teams"]
  leagueUrl = leagueDict["url"]
  constantFile = leagueDict["file"]
  currentDate = todayDate
  
  comingMatches = []
  addedMatches = 0
  while addedMatches < MIN_MATCHES_TO_GET :
    currentDate += datetime.timedelta(1)  
    dateString = currentDate.strftime('%Y%m%d')
    scoresUrl = leagueUrl + DATE_URL_APPENDIX + dateString
    print("Requesting page " + scoresUrl + " ...")
    scoreHtml = getPage(scoresUrl)

    scoreboardPat = re.compile(SCOREBOARD_PATTERN, re.DOTALL)
    scoreboard = scoreboardPat.search(scoreHtml)

    if scoreboard :
      allIds = matchIdPat.findall(scoreboard.group(0))
      for idFound in allIds :
        if str(idFound) in allMatches :
          continue
  
        allMatches.add(idFound)
        currentMatchUrl = MATCH_DATA_URL + idFound
        htmlData = getPage(currentMatchUrl)
        
        matchAwayId = awayTeamIdPat.search(htmlData)
        matchHomeId = homeTeamIdPat.search(htmlData)
        matchAwayName = awayTeamNamePat.search(htmlData)
        matchHomeName = homeTeamNamePat.search(htmlData)
        matchAwayScore = awayScorePat.search(htmlData)
        matchHomeScore = homeScorePat.search(htmlData)
        
        if not matchAwayId or not matchHomeId or not matchAwayName or not matchHomeName : 
          print("## Warning: missing data for match ID " + idFound)
          continue  
    
        if matchAwayName.group(1) not in leagueTeams or matchHomeName.group(1) not in leagueTeams :
          continue
          
        print(" ## Found everything for match: " + matchAwayName.group(1) + " vs " + matchHomeName.group(1) + " ## Saving match into database...")
    
        awayId = matchAwayId.group(1)
        homeId = matchHomeId.group(1)
        awayName = matchAwayName.group(1)
        homeName = matchHomeName.group(1)
    
        insertTeamIfNotExist(awayId, awayName, allTeams, cursor)
        insertTeamIfNotExist(homeId, homeName, allTeams, cursor)
        
        # TODO: insert request to add upcoming match into the new table
        cursor.execute(INSERT_FORESEEN, [idFound, homeId, awayId, -1, -1, currentDate.strftime('%Y-%m-%d'), leagueName, CURRENT_SEASON])
        comingMatches.append([homeName, awayName])
        addedMatches += 1
  
  constantContents = ""
  with open(constantFile, 'r') as constFile :
    constantContents = constFile.read()
  constantContents = constantContents.replace("WEEK_MATCHES", "DEFAULT_MATCHES_X")
  constantContents = constantContents + "\n\nWEEK_MATCHES = " + str(comingMatches)  
    
  with open(constantFile, 'w') as constFile :
    constFile.write(constantContents)
    
dbConn.commit()
dbConn.close()

