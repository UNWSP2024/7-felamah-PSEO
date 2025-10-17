# Author: Faith Lamah
# Date: 10/17/2025
# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math
def main():
    try:
        coordinate1 = []
        print('Enter the coordinates for the first point.')
        x1 = int(input('x1 coordinate:'))
        y1 = int(input('y1 coordinate:'))
        z1 = int(input('z1 coordinate:'))
        coordinate1.append([x1,y1,z1])

        print('Enter the coordinates for the second point.')
        coordinate2 = []
        x2 = int(input('x2 coordinate:'))
        y2 = int(input('y2 coordinate:'))
        z2 = int(input('z2 coordinate:'))
        coordinate2.append([x2, y2, z2])

        function(x1, y1, z1, x2, y2, z2)
    except ValueError:
        print("Invalid input! Please enter only numbers for coordinates.")

def function(x1_cord, y1_cord, z1_cord, x2_cord, y2_cord, z2_cord):
    distance = math.sqrt((x1_cord-x2_cord)**2 + (y1_cord-y2_cord)**2 + (z1_cord-z2_cord)**2)
    print(f'The distance between the two points: {distance:.3f}')

if __name__ == '__main__':
    main()