import turtle
import csv
import os 
cities = {"rochester": (-99, 27), "buffalo": (-163, 7), "syracuse": (-16, 19), "watertown": (-10, 70), "utica": (32, 23), "glens_falls": (116, 38), "ithica": (-40, -25), "albany": (106, -9), "elmira": (-53, -50), "binghamton": (-4, -49), "kingston": (99,-68), "nyc": (97, -149)}
	
def getChords(x, y):
	#  This is a helper function to show coordinates as a click method.
	turtle.goto(x, y)
	print(str(x)+ ", " + str(y))
	
def toCity(cityname):
	# plops the turtle on the city according to the name of the city
	turtle.goto(cities[cityname][0], cities[cityname][1])
	
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
		last = finList[0][0]
		
		turtle.color("black")
		turtle.goto(-200, 100)
		turtle.down()
		turtle.write(last)
		turtle.up()
		for j in finList:
			print(j)
			if last != j[0]:
				# This os.system command WILL NOT work on other computers.
				# The line below is meant to generate png images based on what the program highlights gas prices.
				# It requires extra dependencies that are needed via linux 

				#os.system('sleep 1s && import -window "$(xdotool getactivewindow)" ~/Documents/gasData/frames/' + j[0] + ".png")
				last = j[0]

				turtle.reset()
				turtle.speed(0)
				turtle.showturtle()
				turtle.up()
				turtle.bgpic("bg.png")
				turtle.color("black")
				turtle.goto(-200, 100)
				turtle.down()
				turtle.write(last)
				turtle.up()
				continue
			radius = -(3 - (float(j[1]))*10)
			radius = abs((21 - radius)*5)
			radius = (21 - radius)*1.5
			if j[3] in cities:
				toCity(j[3])
				turtle.color("red")
				turtle.showturtle()
				turtle.right(90)
				turtle.forward(radius)
				print(str(j[1]) + " -- " +str(radius))
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
				
		

def main():
	print("Setting turtle stuff")
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
