#Defining object classes

#Stock
class Stock:
 def __init__(self, ticker, price, good, bad):
  self.ticker = ticker
  self.price = price
  self.good = good
  self.bad = bad
 def chgP(self, chg):
  self.price += chg

#Card
class Card:
 def __init__(self, cardtype, effect):
  self.cardtype = cardtype
  self.effect = effect
  self.hidden = True
  
#Player 
class Player:
 def __init__(self, ID):
  self.ID = ID
  self.cash = 0
  self.positions = []
  self.hand = []

#Create a list of stocks from *stocklist and set quantities to 0
 def buildPortfolio(self, stocklist):
  for stocks in stocklist:
   self.positions.append([stocks, 0])
  self.cash += 100

#Show name, cash, and positions of player  
 def showPortfolio(self):
  print(Player1.ID)
  print("Cash: " + str(Player1.cash))
  for x in self.positions:
   print(x[0].ticker + " " + str(x[1]))
   
#Draw from *deck and put into hand  
 def drawCard(self, deck):
  self.hand.append(deck.pop())

#Player removes* card from hand and adds it to play stack  
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
  
#Increases *stock by *quant, while decreasing cash holdings
 def buy(self, stock, quant):
  templist = [item[0] for item in self.positions]
  self.positions[templist.index(stock)][1] += quant
  self.cash += (-1*quant*stock.price)
  
#Decrease *stock by *quant, while increasing cash holdings
 def sell(self, stock, quant):
  templist = [item[0] for item in self.positions]
  self.positions[templist.index(stock)][1] -= quant
  self.cash += (quant*stock.price)
  
#Methods

#initDeck makes a new Deck object with *amt *cardtype cards then shuffles it
def initDeck(amt, cardtype):
 deck = []
 for i in range(amt):
  deck.append(Card(cardtype,"NA"))
 return deck

#shuffle randomizes *deck
def shuffle(deck):
 None
 
###marketPhase lets the player interact with the market
##def marketPhase(player):
## inPhase = True             
## while inPhase :
##  mktcmd = input("What do you wish to buy? ")
##  if mktcmd == "End" :
##    inPhase = False
##    continue                                 
##  else:
##   action = mktcmd[0]
##   stock = mktcmd [2:5]
##   quant = int(mktcmd[6:])
##   if action == "L":
##    player.buy(stockHelper(player.positions.holdings[0:][0], stock), quant)
##   print(str(quant) + " " + stock + " " + action)
##   continue


#Main (TEST)

#Create Stocks
crt = Stock("CRT", 5, "Sp", "Su")
cbg = Stock("CBG", 6, "Sp", "Fa")
mln = Stock("MLN", 7, "Su", "Sp")
rds = Stock("RDS", 8, "Su", "Fa")
crn = Stock("CRN", 9, "Fa", "Sp")
apl = Stock("APL", 10, "Fa", "Su")
stocklist = [crt, cbg, mln, rds, crn, apl]
#Create Decks
bears = initDeck(50, "bears")
bulls = initDeck(50, "bulls")
market = initDeck(100, "market")
discard = initDeck(0, None)
stack = initDeck(0, None)

#Create Players
Player1 = Player("Boar")
Player1.buildPortfolio(stocklist)
#Create Portfolio




#Testing
Player1.buy(crt, 5)
Player1.sell(crt, 5)
Player1.showPortfolio()
Player1.drawCard(bears)
print(Player1.hand[0].cardtype)
Player1.playCard(Player1.hand[0])
print(Player1.hand)
print(stack[0].cardtype)




