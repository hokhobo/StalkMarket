import random
import Skeleton

####Game Set Up####

#Add players#
currentturn = Skeleton.Turn()
playlist = []
players = int(input("How many players? "))
for x in range(players):
 name = input("Enter player's name: ")
 playlist.append(Skeleton.Player(name))

#Each player draws cards
##for player in playlist:
## for i in range(3):
##  deck = input("What deck would you like to draw from? ")
##  eval("player.drawCard(Skeleton."+deck+")")
##
#Show Portfolio and allow them to buy
for player in playlist:
## print("This is how you start out!")
## player.showPortfolio()
 print("Build your portfolio!")
 Skeleton.market(player)

#Move the market
for stock in Skeleton.stocklist:
 stock.mktMove(currentturn)
Skeleton.tickerBoard()

#Show results
for player in playlist:
 player.showPortfolio()
