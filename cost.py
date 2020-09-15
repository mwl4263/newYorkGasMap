import turtle
import csv
import os 
from datetime import *
cities = {"rochester": (-99, 27), "buffalo": (-163, 7), "syracuse": (-16, 19), "watertown": (-10, 70), "utica": (32, 23), "glens_falls": (116, 38), "ithica": (-40, -25), "albany": (106, -9), "elmira": (-53, -50), "binghamton": (-4, -49), "kingston": (99,-68), "nyc": (97, -149)}
phases = {"phase1": date(2020, 6, 8), "phase2": date(2020, 6, 22), "phase3": date(2020,7,6), "phase4": date(2020, 7, 20)}
def getChords(x, y):
	#  This is a helper function to show coordinates as a click method.
	turtle.goto(x, y)
	print(str(x)+ ", " + str(y))
	
def toCity(cityname):
	# plops the turtle on the city according to the name of the city
	turtle.goto(cities[cityname][0], cities[cityname][1])
	
	
def gasPricesCalc(finList):
	last = finList[0][0]
	turtle.color("black")
	turtle.goto(-200, 100)
	turtle.down()
	turtle.color("orange")
	turtle.write(last[1:11])
	turtle.color("black")
	turtle.up()
	turtle.goto(-300, 150)
	turtle.down()
	turtle.pensize(10)
	turtle.forward(abs(float(finList[0][2]))*5)
	turtle.pensize(1)
	turtle.up()
	turtle.forward(10)
	turtle.down()
	turtle.write(str(finList[0][2]))
	turtle.up()
	negative = False
	barLength = 0
	for j in finList:
		#print(j)
		if last != j[0]:
			theDate = j[0][1:11]
			#print(str(theDate))
			year, month, day = theDate.split('-')
			year = int(year)
			month = int(month)
			day = int(day)
			if (date(year, month, day) < phases["phase1"]):
				turtle.color("orange")
				turtle.up()
				turtle.goto(-200, 80)
				turtle.down()
				turtle.write("PRE COVID-19 Phases")
				turtle.up()
			if (date(year, month, day) >= phases["phase1"]) and (date(year, month, day) < phases['phase2']):
				turtle.color("orange")
				turtle.up()
				turtle.goto(-200, 80)
				turtle.down()
				turtle.write("COVID-19 Phase 1")
				turtle.up()
			if (date(year, month, day) >= phases["phase2"]) and (date(year, month, day) < phases['phase3']):
				turtle.color("orange")
				turtle.up()
				turtle.goto(-200, 80)
				turtle.down()
				turtle.write("COVID-19 Phase 2")
				turtle.up()
			if (date(year, month, day) >= phases["phase3"]) and (date(year, month, day) <= phases['phase4']):
				turtle.color("orange")
				turtle.up()
				turtle.goto(-200, 80)
				turtle.down()
				turtle.write("COVID-19 Phase 3")
				turtle.up()
			if (date(year, month, day) > phases["phase4"]):
				turtle.color("orange")
				turtle.up()
				turtle.goto(-200, 80)
				turtle.down()
				turtle.write("COVID-19 Phase 4")
				turtle.up()
			turtle.goto(-270, 170)
			turtle.color("black")
			turtle.down()
			turtle.write("Oil Barrel Price")
			turtle.up()
			turtle.goto(200, 170)
			turtle.color("red")
			turtle.down()
			turtle.write("Red = Gas Price")
			turtle.up()
			# This os.system command WILL NOT work on other computers.
			# The line below is meant to generate png images based on what the program highlights gas prices.
			# It requires extra dependencies that are needed via linux 
			# os.system('sleep 1s && import -window "$(xdotool getactivewindow)" ~/Documents/gasData/frames/' + j[0] + ".png")
			last = j[0]
			lastOil =j[2]
			turtle.reset()
			turtle.speed(0)
			turtle.showturtle()
			turtle.up()
			turtle.bgpic("bg.png")
			turtle.color("black")
			turtle.goto(-200, 100)
			turtle.down()
			turtle.color("orange")
			turtle.write(last[1:11])
			turtle.color("black")
			turtle.up()
			turtle.goto(-300, 150)
			turtle.down()
			if float(lastOil) == -999.0:
				barLength = 0
			elif float(lastOil) < 0:
				negative = True
			else:	
				barLength = abs(float(lastOil))*5
			turtle.pensize(10)
			turtle.forward(barLength)
			turtle.pensize(1)
			if negative == True:
				turtle.up()
				turtle.forward(10)
				turtle.down()
				
				turtle.write(str(lastOil))
				turtle.up()
				turtle.forward(40)
				turtle.down()
				turtle.write("(negative)")
				turtle.up()
				negative = False
			else:
				turtle.up()
				turtle.forward(10)
				turtle.down()
				turtle.write(str(lastOil))
				turtle.up()
			continue
		radius = -(3 - (float(j[1]))*10)
		radius = abs((21 - radius)*5)
		radius = (21 - radius)*1.5
		if j[3] in cities:
			print(j[0][1:11] + "," + j[1] + "," + j[2] + "," + j[3])
			toCity(j[3])
			turtle.color("red")
			turtle.showturtle()
			turtle.right(90)
			turtle.forward(radius)
			#print(str(j[1]) + " -- " +str(radius))
			turtle.right(270)
			turtle.down()
			turtle.circle(radius)
			turtle.up()
			turtle.forward(-35)
			turtle.down()
			turtle.write(str(j[1]))
			turtle.up()
			turtle.backward(-35)
			turtle.up()
			turtle.home()
			turtle.hideturtle()
			

def openFile(filename):
	with open(filename, "r") as f:
		dataList = f.read().strip()
		dataList = dataList.split("\n")
		newList = []
		lowerList = []
		finList = []
		for x in dataList:
			#print(x)
			down = x.split("\n")
			newList += down
		#print(newList)
		for y in newList:
			lowerList = []
			spdata = y.split(",")
			lowerList += spdata
			finList += [lowerList]
		gasPricesCalc(finList)
		
				
		

def main():
	screen = turtle.Screen()
	screen.setup(600, 400)
	turtle.speed(0)
	turtle.showturtle()
	turtle.up()
	turtle.pencolor("red")
	turtle.bgpic("bg.png")
	toCity("syracuse")
	openFile("gas.txt")
	#turtle.onscreenclick(getChords)
	turtle.mainloop()
	turtle.done()
main()
