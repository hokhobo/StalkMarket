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
 def __init__(self, decktype):
  self.decktype = decktype
  self.pile = []
  
 def addCard(self, card):
  self.pile.append(card)

 def removeCard(self):
  self.pile.remove(pile[0])

 def shuffleDeck(self):
  self.pile = self.pile
  
  
#Portfolio  
class Portfolio:
 def __init__(self):
  self.holdings = []
  
 def addStock(self, stock, quant):
  self.holdings.append([stock, quant])

 def updateQuant(self, ID, chg):
  self.holdings[ID][1] += chg
  
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

 def drawCard(self):
  self.hand = self.hand








#Object and Function Testing
#Stock test#
carrot = Stock("CRT", 8, "Spring", "Winter")
print(carrot.ticker)
print(carrot.price)
print(carrot.good)
print(carrot.bad)
carrot.chgPrice(2)
print(carrot.price)
carrot.chgPrice(-4)
print(carrot.price)

#Portfolio test
porttest = Portfolio()
print(porttest.holdings)
porttest.addStock(carrot, 1)
print(porttest.holdings[0][0].ticker + " " + str(porttest.holdings[0][1]))
porttest.updateQuant(0, 5)
print(porttest.holdings[0][0].ticker + " " + str(porttest.holdings[0][1]))
