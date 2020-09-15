import turtle


cities = {"Rochester": (-99, 27), "Buffalo": (-163, 7), "Syracuse": (-16, 19), "Watertown": (-10, 70), "Utica": (32, 23), "Glens Falls": (116, 38), "Ithaca": (-40, -25), "Albany": (106, -9), "Elmira": (-53, -50), "Binghamton": (-4, -49), "Kingston": (), "New York City": (97, -149)}
	
def getChords(x, y):
	turtle.goto(x, y)
	print(str(x)+ ", " + str(y))
	
def toCity(cityname):
	turtle.goto(cities[cityname][0], cities[cityname][1])
	
def main():
	print("Setting turtle stuff")
	screen = turtle.Screen()
	screen.setup(600, 400)
	turtle.showturtle()
	turtle.up()
	turtle.pencolor("red")
	turtle.bgpic("bg.png")
	
	screen.mainloop()
	
	turtle.done()
main()
