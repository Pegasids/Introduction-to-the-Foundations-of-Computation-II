import turtle

def fractal(myTurtle, depth, size):
	if depth == 0:
		myTurtle.forward(size)
	else:
		
		fractal(myTurtle, depth-1, size/3)
		myTurtle.left(60)
		fractal(myTurtle, depth-1, size/3)
		myTurtle.right(120)
		fractal(myTurtle, depth-1, size/3)
		myTurtle.left(60)
		fractal(myTurtle, depth-1, size/3)
		
		

		
		
		

def main():
	myTurtle = turtle.Turtle()
	myScreen = turtle.Screen()

	myTurtle.color("green")
	myTurtle.up()
	myTurtle.goto(-200,0)
	myTurtle.down()	
	fractal(myTurtle, 3, 400)
	myScreen.exitonclick()	

if __name__ == "__main__":
	main()
	