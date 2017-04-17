'''
This is a cost calculator for painting walls.
It will prompt the user for the number of walls, the height and width of each wall, and the cost of a gallon of paint.
It will use input(), int(), and operators, and functions.
'''


#    ^^ Two new lines for PEP8
# Code goes below

# Data collection phase

def retort(area, cans):
    print("Your wall will require this many gallons of paint:", cans)


def calculate(area):
    cans = area / 400
    retort(area, cans)


def gather():
    number_of_walls = int(input('How many walls will you be painting?  >> '))

    #     if number_of_walls < 1:
    #         height = int(input('How high is your wall in feet? '))
    #         width = int(input('How wide is your wall in feet? '))
    #         calculate_one(height, width)

    #     else number_of_walls > 1:

    area = 0
    for n in range(number_of_walls):
        #  multi_height = ['How', 'high', 'is', 'wall', 'in', 'feet?']
        #  multi_width = ['How', 'wide', 'is', 'wall', 'in', 'feet?']

        #   list_of_heights = []
        #   list_of_widths = []


        height = int(input('How high is wall {0} in feet?  >> '.format(n)))
        width = int(input('How wide is wall {0} in feet?' >> .format(n)))

        this_area = height * width
        area += this_area

    calculate(area)


def go():
    gather()


go()
