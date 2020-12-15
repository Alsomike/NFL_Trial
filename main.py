import requests
import bs4
from tabulate import tabulate

teams = []
def getTeams(i):
  res =requests.get(i)
  soup = bs4.BeautifulSoup(res.text, features='html5lib')
  team1 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > div.d3-o-club-fullname')
  team2 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(2) > td:nth-child(1) > a > div.d3-o-club-fullname')
  team3 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(3) > td:nth-child(1) > a > div.d3-o-club-fullname')
  team4 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(4) > td:nth-child(1) > a > div.d3-o-club-fullname')
  FirstPlace = team1[0].text.strip()
  SecondPlace = team2[0].text.strip()
  ThirdPlace = team3[0].text.strip()
  FourthPlace = team4[0].text.strip()
  teams.extend([FirstPlace, SecondPlace, ThirdPlace, FourthPlace])


wins = []
def getWins(i):
  res =requests.get(i)
  soup = bs4.BeautifulSoup(res.text, features='html5lib')
  team1 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(1) > td:nth-child(2)')
  team2 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(2) > td:nth-child(2)')
  team3 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(3) > td:nth-child(2)')
  team4 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(4) > td:nth-child(2)')
  FirstPlace = team1[0].text.strip()
  SecondPlace = team2[0].text.strip()
  ThirdPlace = team3[0].text.strip()
  FourthPlace = team4[0].text.strip()
  wins.extend([FirstPlace, SecondPlace, ThirdPlace, FourthPlace])


losses = []
def getLoss(i):
  res =requests.get(i)
  soup = bs4.BeautifulSoup(res.text, features='html5lib')
  team1 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(1) > td:nth-child(3)')
  team2 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(2) > td:nth-child(3)')
  team3 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(3) > td:nth-child(3)')
  team4 = soup.select('#main-content > section.d3-l-grid--outer.d3-l-section-row.nfl-o-standings > div > div > div > div:nth-child(6) > div.d3-o-table--horizontal-scroll > table > tbody > tr:nth-child(4) > td:nth-child(3)')
  FirstPlace = team1[0].text.strip()
  SecondPlace = team2[0].text.strip()
  ThirdPlace = team3[0].text.strip()
  FourthPlace = team4[0].text.strip()
  losses.extend([FirstPlace, SecondPlace, ThirdPlace, FourthPlace])

def InitAll(i):
  getTeams(i)
 # print(teams)
  getWins(i)
 # print(wins)
  getLoss(i)
 # print(losses)


InitAll('https://www.nfl.com/standings/')

header = ['Team', 'Wins', 'Losses', 'Win%']

tuples = list(zip(teams, wins, losses))
# print(tuples)
print()
print(tabulate(tuples, headers=header ))