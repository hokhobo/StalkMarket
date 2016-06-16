###SET UP ELEMENTS### AKA SKELETON
import random

movdice = (-1, -1, 0, 1, 1, 1)
magdice = (1, 1, 1, 2, 2, 3)
#Defining object classes

#Stock
class Stock:
 def __init__(self, ticker, price, good, bad):
  self.ticker = ticker
  self.price = price
  self.good = good
  self.bad = bad
  self.lastchg = 0
  
 def mktMove(self, turn):
  chg = random.choice(movdice)*random.choice(magdice)
  #Compare stock season to current season
  self.price += chg
  self.lastchg = chg

crt = Stock("CRT", 5, "sp", "su")
cbg = Stock("CBG", 6, "sp", "fa")
mln = Stock("MLN", 7, "su", "fa")
crn = Stock("CRN", 8, "su", "sp")
rds = Stock("RDS", 9, "fa", "su")
apl = Stock("APL", 10, "fa", "sp")
stocklist = [crt, cbg, mln, crn, rds, apl]

def tickerBoard():
 print("Stock " + "Price " + "Last Move")
 for stock in stocklist:
  print(stock.ticker + " " + str(stock.price) + " "
        + str(stock.lastchg))
    
#Card
class Card:
 def __init__(self, cardtype, effect):
  self.cardtype = cardtype
  self.effect = effect
  self.playtime = "NA"
  self.title = "NA"
  self.hidden = True

#Makes a new Deck object with *amt *cardtype cards
#then shuffles it
def initDeck(amt, cardtype):
 deck = []
 for i in range(amt):
  deck.append(Card(cardtype,"NA"))
 random.shuffle(deck) 
 return deck

bears = initDeck(50, "bears")
bulls = initDeck(50, "bulls")
market = initDeck(100, "market")
discard = initDeck(0, None)
stack = initDeck(0, None)

  
#Turn
class Turn:
 def __init__(self):
  self.turnnum = 0
  self.season = ""
 def happen(self):
  None#All the components of a turn
  
#Liability
class Liability:
 def __init__(self, stock, quant, start, owner):
  self.stock = stock
  self.quant = quant
  self.start = start.turnum
  self.end = start + 2
  self.owner = owner
 def expire(self, turn):
  if self.end == turn.turnnum:
   self.owner.buy(self.stock, self.quant)
   self.owner.contracts.remove(self)

#Player 
class Player:
 def __init__(self, ID):
  self.ID = ID
  self.cash = 100
  self.hand = []
  self.contracts = []
  self.positions = []
  for stocks in stocklist:
   self.positions.append([stocks, 0])
  self.networth = 0

#Show name, cash, and positions of player  
 def showPortfolio(self):
  self.networth = sum([self.cash,
  sum([a*b for a,b in zip([itema[0].price for itema in self.positions],
  [itemb[1] for itemb in self.positions])])])  
  print(self.ID)
  print("Networth: " + str(self.networth))
  print("Cash: " + str(self.cash))
  for x in self.positions:
   print(x[0].ticker + " " + str(x[1]))
   
#Draw from *deck and put into hand  
 def drawCard(self, deck):
  self.hand.append(deck.pop())

#Player removes *card from hand and adds it to play stack  
 def playCard(self, card):
  stack.append(card)
  self.hand.remove(card)

#Current player gives *quant1 *stock1 to player *other for *quant2 *stock2
 def trade(self, other, stock1, quant1, stock2, quant2):
  templist1 = [item[0] for item in self.positions]
  templist2 = [item[0] for item in other.positions]
  self.positions[templist1.index(stock1)][1] -= quant1
  self.positions[templist2.index(stock2)][1] += quant2
  other.positions[templist2.index(stock2)][1] -= quant
  other.positions[templist1.index(stock1)][1] += quant
  
#Changes *stock by *quant and cash by *quant x (stock price)
#Buy *quant > 0, Sell *quant < 0
 def buy(self, stock, quant):
  templist = [item[0] for item in self.positions]
  self.positions[templist.index(stock)][1] += quant
  self.cash += (-1*quant*stock.price)
  
 def sell(self, stock, quant):
   self.buy(stock, -quant)

#Sells *quant *stock then adds Liability for *stock *quant
 def short(self, stock, quant, turn):
  sell(stock, quant)
  self.contracts.append(Liability(stock, quant, turn, self))
 
   
###GAMEPLAY ELEMENTS### AKA MUSCLE

def market(player):
 inPhase = True             
 while inPhase :
  mktcmd = input("Welcome to the market: ")
  if mktcmd == "End" :
    inPhase = False
    continue                                 
  else:
   cmds = mktcmd.split(maxsplit=3)
   eval("player."+cmds[0]+"("+cmds[2]+", "+cmds[1]+")")
   player.showPortfolio()
   continue






   
