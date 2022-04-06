class FanduelPlayer:
  def __init__(self, name, runsScored, pSingles, pDoubles, pTriples, pHr, pRbi, pWalk, pSB, pCS):
    self.name = name
    self.walks = pWalk
    self.singles = pSingles
    self.doubles = pDoubles
    self.triples = pTriples
    self.homeruns = pHr
    self.runs = runsScored
    self.rbis = pRbi
    self.stolenbases = pSB
    self.caughtStealing = pCS
    self.totalPoints = 0

def calculateBestTeam(players):
    for player in players:
        player.totalPoints = player.singles + player.doubles * 2 + player.triples * 3 + player.homeruns * 4 + player.rbis + player.walks + player.stolenbases * 2 + player.runs - player.caughtStealing

filename = 'FanGraphs Leaderboard.csv'
f = open(filename)
Lines = f.readlines() 
batters = []
first = True
for line in Lines:
    if first:
        first = False
        continue 
    splitLine = line.split(',') 
    doubles = int(splitLine[6].replace('"', ''))
    triples = int(splitLine[7].replace('"', ''))
    homeruns = int(splitLine[8].replace('"', ''))
    hits = int(splitLine[5].replace('"', ''))
    singles = hits - homeruns - triples - doubles
    rbis = int(splitLine[10].replace('"', ''))
    runs = int(splitLine[9].replace('"', ''))
    walks = int(splitLine[11].replace('"', ''))
    steals = int(splitLine[14].replace('"', ''))
    cs = int(splitLine[15].replace('"', ''))
    batters.append(FanduelPlayer(splitLine[0].replace('"', ''), runs, singles, doubles, triples, homeruns, rbis, walks, steals, cs))

calculateBestTeam(batters)

batters.sort(key=lambda x: x.totalPoints, reverse=True)

for batter in batters:
    if(batter.totalPoints > 250):
        print (batter.name + ":\t" +  str(batter.totalPoints))