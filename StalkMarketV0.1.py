#Stalk Market Simulator in Python Version 0.1
#Defining object classes

class Stock:
 def __init__(self, ticker, price, good, bad):
  self.ticker = ticker
  self.price = price
  self.good = good
  self.bad = bad
 def chgPrice(self, chg):
  self.price = self.price + chg

class Card:
 def __init__(self, cardtype, effect):
  self.cardtype = cardtype
  self.effect = effect

class Deck:
 def __init__(self, decktype):
  self.decktype = decktype
  self.pile = []
  
class Portfolio:
 def __init__(self):
  self.holdings = []
  
 def addStock(self, stock, quant):
  self.holdings.append([stock, quant])
  
class Player:
 def __init__(self, ID):
  self.ID = ID
  self.cash = 0
  self.positions = Portfolio()
  self.hand = []









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
print(porttest.holdings[0:][0:])
