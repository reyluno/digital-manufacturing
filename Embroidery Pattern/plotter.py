import turtle
import csv

def plot_coords(white_coords):
    print("Beginning plot...")
    # Create a new turtle window
    screen = turtle.Screen()
    screen.screensize(2000, 2000)
    screen.title('White Coords')

    # Create a turtle to plot the coordinates
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Go to the first coordinate and start drawing
    t.goto(white_coords[0])
    t.pendown()

    # Plot all of the remaining coordinates
    for coord in white_coords[1:]:
        t.goto(coord)

    turtle.mainloop()

def read_csv_as_tuples(csv_file):
    tuples_list = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row_tuples = tuple(map(int, row))
            tuples_list.append(row_tuples)
    return tuples_list

data = read_csv_as_tuples("newlist.csv")
new_data = []
for i, tup in enumerate(data):
    new_tup = tuple([x*0.1 for x in tup])
    new_data.append(new_tup)

#print(data)

plot_coords(data)