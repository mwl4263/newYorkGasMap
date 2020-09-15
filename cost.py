import turtle



def setChords():
	print("Setting Chords")
	glenx, gleny = 116, 38
	rocx, rocy = -99, 27
	ithx, ithy = -40, -25
	kingx, kingy = 98, -68
	
	print(glenx)
	
def getChords(x, y):
	turtle.goto(x, y)
	print(str(x)+ ", " + str(y))

def main():
	print("Setting turtle stuff")
	screen = turtle.Screen()
	screen.setup(600, 400)
	turtle.showturtle()
	turtle.up()
	turtle.pencolor("red")
	turtle.bgpic("bg.png")
	setChords()
	screen.onclick(getChords)
	screen.mainloop()
	turtle.done()
main()
