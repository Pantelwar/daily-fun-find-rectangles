from itertools import combinations

inputArray = [
    (1,2), (2,2), (3,2), (4,2), (5,2), (6,2),
    (1,1), (2,1), (3,1), (4,1), (5,1), (6,1)
]
coordinates = combinations(inputArray, 4)

# Print the obtained permutations
if len(inputArray) < 4:
    print "Length of array must be atleast 4"

noOfRectanglesPossible = 0

for fourPoints in list(coordinates):
    twoPoints = combinations(fourPoints, 2)
    # print "fourPoints:", fourPoints
    rectPossible = 0
    for points in list(twoPoints):
        x = points[0][0] - points[1][0]
        y = points[0][1] - points[1][1]
        # print points, x, y
        if y == 0:
            rectPossible += 1
        if x == 0:
            rectPossible -= 1
    # print "isRectPossible: ", rectPossible
    if rectPossible == 0:
        noOfRectanglesPossible += 1
    # print "-------------------------------"

print "No. of rectangles possible parallel to axis: ", noOfRectanglesPossible
