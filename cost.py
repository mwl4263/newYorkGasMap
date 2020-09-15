import turtle
import csv
import pandas as pd
cities = {"rochester": (-99, 27), "buffalo": (-163, 7), "syracuse": (-16, 19), "watertown": (-10, 70), "utica": (32, 23), "glens_falls": (116, 38), "ithaca": (-40, -25), "albany": (106, -9), "elmira": (-53, -50), "binghamton": (-4, -49), "kingston": (0,0), "nyc": (97, -149)}
	
def getChords(x, y):
	#  This is a helper function to show coordinates as a click method.
	turtle.goto(x, y)
	print(str(x)+ ", " + str(y))
	
def toCity(cityname):
	# plops the turtle on the city according to the name of the city
	turtle.goto(cities[cityname][0], cities[cityname][1])
	
def openFile(filename):
	mycsv = pd.read_csv(filename)
	print(mycsv)
	lineCount = 0
	rowCount = 0
	importantRows = []
	for x in mycsv:
		for i in cities:
			if i in x:
				print(x)
	for row in mycsv.iter
		
			

def main():
	print("Setting turtle stuff")
	screen = turtle.Screen()
	screen.setup(600, 400)
	turtle.showturtle()
	turtle.up()
	turtle.pencolor("red")
	turtle.bgpic("bg.png")
	toCity("Syracuse")
	openFile("data.csv")
	screen.mainloop()
	turtle.done()
main()
