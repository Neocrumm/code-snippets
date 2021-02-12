import turtle 
screen = turtle.Screen()
myPen = turtle.Turtle()
myPen.speed(0)
myPen.shape('turtle')
myPen.width(1)
myPen.pencolor("black")
myPen.degrees(360)
myPen.penup()

def drawPieChart(percentage1, percentage2, percentage3, percentage4, percentage5):
  # Title of the Pie Chart
  myPen.goto(0,-170)
  myPen.left(90)
  myPen.forward(320)
  myPen.write("Favorite Genres of Music", None, "center", "20pt bold")
  myPen.backward(180)

  # Rock Genre Section
  myPen.right(90)
  myPen.pencolor("#5d5dfa")
  myPen.pendown()
  for x in range(2 * int(percentage1*360)):
      myPen.left(0.5)
      myPen.forward(140)
      myPen.backward(140)
  
  # Rock Genre Label
  myPen.right((percentage1*360)/2)
  myPen.penup()
  myPen.forward(80)
  myPen.seth(0)
  myPen.write("Rock", None, "center", "10pt bold") 
  myPen.seth(270)
  myPen.forward(15)
  myPen.write("30%", None, "center", "10pt bold")
  myPen.backward(15)
  myPen.seth(0)
  myPen.left((percentage1*360)/2)
  myPen.backward(80)
  myPen.left((percentage1*360)/2)
  
  # Electronic Section
  myPen.pendown()
  myPen.pencolor("#ff0000")
  for x in range(2*int(percentage2*360)):
    myPen.left(0.5)
    myPen.forward(140)
    myPen.backward(140)
  
  # Electronic Genre Label
  myPen.right((percentage2*360)/2)
  myPen.penup()
  myPen.forward(80)
  myPen.seth(0)
  myPen.write("EDM", None, "center", "11pt bold")
  myPen.seth(270)
  myPen.forward(15)
  myPen.write("15%", None, "center", "10pt bold")
  myPen.backward(15)
  myPen.seth(0)
  myPen.left(percentage1*360 + (percentage2*360)/2)
  myPen.backward(80)
  myPen.left((percentage2*360)/2)
  
  # Country Section
  myPen.pendown()
  myPen.pencolor("#03f403")
  for x in range(2*int(percentage3*360)):
    myPen.left(0.5)
    myPen.forward(140)
    myPen.backward(140)
    
  # Country Genre Label
  myPen.right((percentage3*360)/2)  
  myPen.penup()
  myPen.forward(80)
  myPen.seth(0)
  myPen.write("Country", None, "center", "11pt bold")
  myPen.seth(270)
  myPen.forward(15)
  myPen.write("10%", None, "center", "10pt bold")
  myPen.backward(15)
  myPen.seth(0)
  myPen.left(percentage1*360 + percentage2*360 + (percentage3*360)/2)
  myPen.backward(80)
  myPen.left((percentage3*360)/2)
  
  # Pop Section
  myPen.pendown()
  myPen.pencolor("rgb(255, 184, 55)")
  for x in range(2*int(percentage4*360)):
    myPen.left(0.5)
    myPen.forward(140)
    myPen.backward(140)
  
  # Pop Genre Label
  myPen.right((percentage4*360)/2)
  myPen.penup()
  myPen.forward(80)
  myPen.seth(0)
  myPen.write("Pop", None, "center", "11pt bold")
  myPen.seth(270)
  myPen.forward(15)
  myPen.write("20%", None, "center", "10pt bold")
  myPen.backward(15)
  myPen.seth(0)
  myPen.left(percentage1*360 + percentage2*360 + percentage3*360 + (percentage4*360)/2)
  myPen.backward(80)
  myPen.left((percentage4*360)/2)
  
  # Hip-Hop Section
  myPen.pendown()
  myPen.pencolor("#ffbdc8")
  for x in range(2*int(percentage5*360)):
    myPen.left(0.5)
    myPen.forward(140)
    myPen.backward(140)
  
  # Hip-Hop Genre Label
  myPen.right((percentage5*360)/2)
  myPen.penup()
  myPen.forward(80)
  myPen.seth(0)
  myPen.write("Hip-Hop", None, "center", "11pt bold")
  myPen.seth(270)
  myPen.forward(15)
  myPen.write("25%", None, "center", "10pt bold")
  myPen.backward(15)
  myPen.seth(0)
  myPen.left(percentage1*360+percentage2*360+percentage3*360+percentage4*460+ (percentage5*360)/2)
  myPen.backward(80)
  myPen.left((percentage5*360)/2)
  myPen.hideturtle()
  
# Percentages
rock_percentage = 0.30
hiphop_percentage = 0.25
pop_percentage = 0.20
electronic_percentage = 0.15
country_percentage = 0.10

# Call the function to draw the pie chart
drawPieChart(rock_percentage, electronic_percentage, country_percentage, pop_percentage, hiphop_percentage)
screen.tracer(0)
