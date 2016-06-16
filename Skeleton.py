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
  
 def mktMove(self, turn):
  chg = random.choice(movdice)*random.choice(magdice)
  #Compare stock season to current season
  self.price += chg

#Card
class Card:
 def __init__(self, cardtype, effect):
  self.cardtype = cardtype
  self.effect = effect
  self.playtime = "NA"
  self.title = "NA"
  self.hidden = True

#Liability
class Liability:
 def __init__(self, stock, quant, start):
  self.stock = stock
  self.qunat = quant
  self.start = start
  self.end = start + 2
 def expire(self):
  None
  
#Turn
class Turn:
 def __init__(self):
  self.turnnum = 0
  self.season = ""
  
#Player 
class Player:
 def __init__(self, ID, stocklist):
  self.ID = ID
  self.cash = 100
  self.hand = []
  self.contracts = []
  self.positions = []
  for stocks in stocklist:
   self.positions.append([stocks, 0])
  
#Show name, cash, and positions of player  
 def showPortfolio(self):
  print(self.ID)
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
 def buyorsell(self, stock, quant):
  templist = [item[0] for item in self.positions]
  self.positions[templist.index(stock)][1] += quant
  self.cash += (-1*quant*stock.price)

#
def short(self, stock, quant):
 buyorsell(stock, -quant)
 self.contracts.append(Liability(stock, quant, currentturn.turnnum))
 
 
   
