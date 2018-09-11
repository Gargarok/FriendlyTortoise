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

##LEAGUE_ONE_MATCHES_URL = "http://www.espnfc.com/french-ligue-1/9/scores"
##LEAGUE_TWO_MATCHES_URL = "http://www.espnfc.com/french-ligue-2/96/scores"
##PREMIER_LEAGUE_MATCHES_URL = "http://www.espnfc.com/english-premier-league/23/scores"
##BUNDESLIGA_URL = "http://www.espnfc.com/german-bundesliga/10/scores"
##ITA_SERIE_A_URL = "http://www.espnfc.com/italian-serie-a/12/scores"
##SPANISH_LIGA_URL = "http://www.espnfc.com/spanish-primera-division/15/scores"
##ARGENTINA_SUPERLIGA_URL = "http://www.espnfc.com/superliga-argentina/1/scores"
##PORTUGAL_LIGA_URL = "http://www.espnfc.com/portuguese-liga/14/scores"

MATCH_DATA_URL = "http://www.espnfc.com/matchstats?gameId="
#DATE_URL_APPENDIX = "?date="

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
DATE_PATTERN = "<span data-date=\"(\d{4})-(\d{2})-(\d{2}).*?\""     # Groups: 1:Year, 2:Month, 3:Day
SCOREBOARD_PATTERN = "<script>window.espn.scoreboardData.*?</script>"

nextMatchId = 1
nextTeamId = 1
allIds = set()

def insertMatchesForLeague(matchesUrl, leagueName, leagueTeams, currentYear, currentMonth, currentDay):
  global nextTeamId
  global nextMatchId
  global allIds
  ##fullUrl = matchesUrl + DATE_URL_APPENDIX + currentDate
  fullUrl = matchesUrl + currentDate
  print("Requesting page " + fullUrl + " ...")
  htmlResult = getPage(fullUrl)
  
  scoreboardPat = re.compile(SCOREBOARD_PATTERN, re.DOTALL)
  scoreboard = scoreboardPat.search(htmlResult)

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
      #matchDate = matchDatePat.search(htmlData)
      
      if not matchAwayId or not matchHomeId or not matchAwayName or not matchHomeName or not matchAwayScore or not matchHomeScore : # or not matchDate :
        print("## Warning: missing data for match ID " + idFound)
        continue  
  
      if matchAwayName.group(1) not in leagueTeams or matchHomeName.group(1) not in leagueTeams :
        continue
      print(" ## Found everything for match: " + matchAwayName.group(1) + " vs " + matchHomeName.group(1) + " ## Saving match into database...")
  
      awayId = matchAwayId.group(1)
      homeId = matchHomeId.group(1)
      awayName = matchAwayName.group(1)
      homeName = matchHomeName.group(1)
      awayScore = matchAwayScore.group(1)
      homeScore = matchHomeScore.group(1)
      if currentDay == 31 :
        currentDay = 30
  
      date = datetime.datetime(currentYear, currentMonth, currentDay)  # Year, Month, Day
      nextTeamId = insertTeamIfNotExist(awayId, awayName, allTeams, cursor, nextTeamId)
      nextTeamId = insertTeamIfNotExist(homeId, homeName, allTeams, cursor, nextTeamId)
      cursor.execute(INSERT_MATCH, [nextMatchId, idFound, homeId, awayId, homeScore, awayScore, date.strftime('%Y-%m-%d'), leagueName, CURRENT_SEASON])
      nextMatchId += 1

def getPage (url):
  html = ""
  with urllib.request.urlopen(url) as response :
    bytesPage = response.read()
    html = bytesPage.decode("utf8")
  return html

def insertTeamIfNotExist (teamId, teamName, allTeams, cursor, nextTeamId):
  if not teamId in allTeams :
    cursor.execute(INSERT_TEAM, [nextTeamId, teamId, teamName])
    allTeams.add(teamId)
    nextTeamId += 1
  return nextTeamId

def getArrayFromDate (dateFrom):
  todayDate = time.strftime("%Y%m%d")
  dateArray = []
  year = int(dateFrom[0:4])
  month = int(dateFrom[4:6])
  day = int(dateFrom[6:8])
  nextDate = ""

  dateArray.append(dateFrom)
  while nextDate != todayDate :
    day = (day % 31) + 1
    if day == 1 :
      month = (month % 12) + 1
      if (month == 1) :
        year += 1
        
    strDay = str(day)
    if len(strDay) == 1 :
      strDay = "0" + strDay
    strMonth = str(month)
    if len(strMonth) == 1 :
      strMonth = "0" + strMonth
      
    nextDate = str(year) + strMonth + strDay
    dateArray.append(nextDate)
  return dateArray

#############################################
## ## ##   MAIN PROCESS
#############################################
  
datesToParse = []
dateFrom = ""
databaseExists = True

if len(sys.argv) > 1 :
  dateFrom = sys.argv[1]
  datesToParse = getArrayFromDate(dateFrom)
else :
  datesToParse = ["20170930"]

if not os.path.isfile(APP_FOLDER + DATABASE_FILE):
  databaseExists = False

dbConn = sqlite3.connect(APP_FOLDER + DATABASE_FILE)
cursor = dbConn.cursor()

print("Initializing...")
if not databaseExists:
  print("Database does not exists ; creating ...")
  cursor.execute(DATABASE_INIT_TEAM)
  cursor.execute(DATABASE_INIT_MATCH)
  dbConn.commit()
else:
  cursor.execute(PREV_ID_TEAM)
  prevId = cursor.fetchone()
  if prevId[0] : 
    nextTeamId = int(prevId[0]) + 1
  else :
    nextTeamId = 1
  cursor.execute(PREV_ID_MATCH)
  prevId = cursor.fetchone()
  if prevId[0] : 
    nextMatchId = int(prevId[0]) + 1
  else :
    nextMatchId = 1

defaultDates = ["20170925", "20170926", "20170927", "20170928", "20170929", "20170930", "20170931"]

print("Getting matches...")
allMatches = set()
cursor.execute(ALL_MATCHES)
tuples = cursor.fetchall()
for tuple in tuples :
  allMatches.add(str(tuple[0]))

print("Getting teams...")
allTeams = set()
cursor.execute(ALL_TEAMS)
tuples = cursor.fetchall()
for tuple in tuples :
  allTeams.add(str(tuple[0]))

#print("ALL MATCHES: " + str(allMatches))
  #print("ALL TEAMS: " + str(allTeams))
  
matchIdPat = re.compile(MATCHES_IDS_PAT)
awayTeamIdPat = re.compile(AWAY_TEAM_ID_PAT)
homeTeamIdPat = re.compile(HOME_TEAM_ID_PAT)
awayTeamNamePat = re.compile(AWAY_TEAM_NAME_PAT)
homeTeamNamePat = re.compile(HOME_TEAM_NAME_PAT)
awayScorePat = re.compile(AWAY_SCORE_PAT)
homeScorePat = re.compile(HOME_SCORE_PAT)
matchDatePat = re.compile(DATE_PATTERN)

print("INITIALIZATION DONE ! Starting the gathering process...")
for currentDate in datesToParse :
  currentYear = int(currentDate[0:4])
  currentMonth = int(currentDate[4:6])
  currentDay = int(currentDate[6:8])

##  insertMatchesForLeague(LEAGUE_ONE_MATCHES_URL, LIGUE_ONE_NAME, LIGUEONE_TEAMS, currentYear, currentMonth, currentDay)
  insertMatchesForLeague(LEAGUE_TWO_MATCHES_URL, LIGUE_TWO_NAME, LIGUETWO_TEAMS, currentYear, currentMonth, currentDay)
  insertMatchesForLeague(PREMIER_LEAGUE_MATCHES_URL, PREMIER_LEAGUE_NAME, PREMIERLEAGUE_TEAMS, currentYear, currentMonth, currentDay)
  insertMatchesForLeague(BUNDESLIGA_URL, BUNDESLIGA_NAME, BUNDESLIGA_TEAMS, currentYear, currentMonth, currentDay)
  insertMatchesForLeague(ITA_SERIE_A_URL, ITA_SERIE_A_NAME, ITA_SERIE_A_TEAMS, currentYear, currentMonth, currentDay)
  insertMatchesForLeague(SPANISH_LIGA_URL, SPANISH_LIGA_NAME, SPANISH_LIGA_TEAMS, currentYear, currentMonth, currentDay)
  insertMatchesForLeague(PORTUGAL_LIGA_URL, PORTUGAL_LIGA_NAME, PORTUGAL_LIGA_TEAMS, currentYear, currentMonth, currentDay)
  
dbConn.commit()
dbConn.close()

