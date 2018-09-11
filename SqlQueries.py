#!/usr/bin/python3
#coding: utf-8

TEAM_TABLE = "team"
MATCH_TABLE = "match"

LIGUE_ONE_NAME = "LIGUEONE"
LIGUE_TWO_NAME = "LIGUETWO"
PREMIER_LEAGUE_NAME = "PREMIERLEAGUE"
SPANISH_LIGA_NAME = "SPANISHLIGA"
ITA_SERIE_A_NAME = "ITASERIEA"
BUNDESLIGA_NAME = "BUNDESLIGA"
PORTUGAL_LIGA_NAME = "PORTUGALSERIEA"
ARG_SUPERLIGA_NAME  = "ARGSUPERLIGA"

CURRENT_SEASON = 1

DATABASE_INIT_TEAM = """CREATE TABLE team (id INTEGER PRIMARY_KEY, online_id INTEGER, name TEXT, abbrev TEXT);  -- Teams """
DATABASE_INIT_MATCH = """CREATE TABLE match (id INTEGER PRIMARY_KEY, online_id INTEGER, home_id INTEGER, away_id INTEGER, 
    home_goals INTEGER, away_goals INTEGER, date DATE, championship TEXT, league_season INTEGER);  -- Matches
"""
DATABASE_INIT_FORESEEN = """CREATE TABLE foreseen (id INTEGER PRIMARY_KEY, online_id INTEGER, home_id INTEGER, away_id INTEGER, 
    home_goals INTEGER, away_goals INTEGER, date DATE, championship TEXT, league_season INTEGER);  -- Matches
"""

PREV_ID_TEAM = """SELECT max(id) FROM team;"""
PREV_ID_MATCH = """SELECT max(id) FROM match;"""

ALL_MATCHES = """SELECT DISTINCT online_id FROM match;"""
ALL_TEAMS = """SELECT DISTINCT online_id FROM team;"""
ALL_FORESEEN = """SELECT DISTINCT online_id FROM foreseen;"""

INSERT_TEAM = """INSERT INTO team (id, online_id, name) VALUES (?, ?, ?);"""
INSERT_MATCH = """INSERT INTO match (id, online_id, home_id, away_id, home_goals, away_goals, date, championship, league_season)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""

INSERT_FORESEEN = """INSERT INTO foreseen (online_id, home_id, away_id, home_goals, away_goals, date, championship, league_season)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""				  
				  
GET_MATCH_DATA = """SELECT team_h.name,
                           team_a.name,
                           home_goals,
                           away_goals
                    FROM match
                    INNER JOIN team team_h ON home_id = team_h.online_id
                    INNER JOIN team team_a ON away_id = team_a.online_id
                    WHERE date < ?
                      AND date > ?
                      AND championship = ?
                    ORDER BY date;"""

GET_MATCH_DATES = """
                  SELECT DISTINCT date, away.name, home.name
                  FROM match
                  INNER JOIN team away ON away.online_id = match.away_id
                  INNER JOIN team home ON home.online_id = match.home_id
                  WHERE date > ?
                    AND championship = ?
                  ORDER BY date;
                  """

GET_MATCH_RESULT = """
                   SELECT home_goals,
                          away_goals
                   FROM match
                   INNER JOIN team home ON home.online_id = match.home_id
                   INNER JOIN team away ON away.online_id = match.away_id
                   WHERE home.name = ?
                     AND away.name = ?
                     AND date >= ?
                     AND championship = ?
                   ORDER BY date;
                   """
