#Defining object classes
#Stock
class Stock:
 def __init__(self, ticker, price, good, bad):
  self.ticker = ticker
  self.price = price
  self.good = good
  self.bad = bad
 def chgPrice(self, chg):
  self.price += chg

#Card
class Card:
 def __init__(self, cardtype, effect):
  self.cardtype = cardtype
  self.effect = effect
  
#Deck
class Deck:
 def __init__(self):
  self.pile = []
  
 def addCard(self, card):
  self.pile.append(card)

 def removeCard(self):
  self.pile.remove(pile[0])

 def shuffle(self):
  self.pile = self.pile
  
  
#Portfolio  
class Portfolio:
 def __init__(self):
  self.holdings = []
  
 def addStock(self, stock, quant):
  self.holdings.append([stock, quant])

 def updateQuant(self, stock, chg):
  self.holdings[stock][1] += chg
  
  
#Player 
class Player:
 def __init__(self, ID):
  self.ID = ID
  self.cash = 0
  self.positions = Portfolio()
  self.hand = []

 def buildPortfolio(self):
  self.positions = self.positions
  
 def updatePortfolio(self):
  self.positions = self.positions
  
 def showPortfolio(self):
  print(Player1.ID)
  print("Cash: " + str(Player1.cash))
  for x in self.positions.holdings:
   print(x[0].ticker + " " + str(x[1]))
   
 def drawCard(self, card):
  self.hand.append(card)
  
 def playCard(self, card):
  self.hand.delete(card)

 def updateCash(self, chg):
  self.cash += chg

 def trade(self):
  self.positions = self.positions
  
 def buy(self, stock, quant):
  self.positions.updateQuant(stock, quant)
  self.Updatecash(-1*quant*stock.price)

 def sell(self, stock, quant):
  self.positions.updateQuant(stock, -quant)
  self.Updatecash(quant*stock.price)
  
#Methods
def initStocks():
 crt = Stock("CRT", 5, "Sp", "Su")
 cbg = Stock("CBG", 6, "Sp", "Fa")
 mln = Stock("MLN", 7, "Su", "Sp")
 rds = Stock("RDS", 8, "Su", "Fa")
 crn = Stock("CRN", 9, "Fa", "Sp")
 apl = Stock("APL", 10, "Fa", "Su")
 return [crt, cbg, mln, rds, crn, apl]

def initCards():
 bulls = Deck()
 for i in range(50):
  bulls.addCard(Card("bull","NA"))
  
 bears = Deck()
 for i in range(50):
  bears.addCard(Card("bear","NA"))
             
 market = Deck()
 for i in range(100):
  market.addCard(Card("market","NA"))
             
 bulls.shuffle()
 bears.shuffle()               
 market.shuffle()
 return [bulls, bears, market]

def stockHelper(stocks, symb):
 for stock in stocks:
  if stock.ticker == symb:
   break
  else:
   stock = None
 return stock

def marketPhase(player):
 inPhase = True             
 while inPhase :
  mktcmd = input("What do you wish to buy? ")
  if mktcmd == "End" :
    inPhase = False
    continue                                 
  else:
   action = mktcmd[0]
   stock = mktcmd [2:5]
   quant = int(mktcmd[6:])
   if action == "L":
    player.buy(stockHelper(player.positions.holdings[0:][0], stock), quant)
   print(str(quant) + " " + stock + " " + action)
   continue


#Main

#Create Stocks
stocklist = initStocks()
#Create Cards
decklist = initCards()
#Create Players
Player1 = Player("Boar")
#Add funds
Player1.updateCash(100)
#Create Portfolio
for stock in stocklist:
 Player1.positions.addStock(stock, 0)

marketPhase(Player1)
Player1.showPortfolio()






#Object and Function Testing
#Stock test#
#carrot = Stock("CRT", 8, "Spring", "Winter")
#print(carrot.ticker)
#print(carrot.price)
#print(carrot.good)
#print(carrot.bad)
#carrot.chgPrice(2)
#print(carrot.price)
#carrot.chgPrice(-4)
#print(carrot.price)

#Portfolio test
#porttest = Portfolio()
#print(porttest.holdings)
#porttest.addStock(carrot, 1)
#print(porttest.holdings[0][0].ticker + " " + str(porttest.holdings[0][1]))
#porttest.updateQuant(0, 5)
#print(porttest.holdings[0][0].ticker + " " + str(porttest.holdings[0][1]))
