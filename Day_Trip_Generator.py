#(5 points): As a developer, I want to make at least three commits with descriptive messages.

#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists. 

#(5 points): As a user, I want a destination to be randomly selected for my day trip.

#(5 points): As a user, I want a restaurant to be randomly selected for my day trip.

#5(points): As a user, I want a mode of transportation to be randomly selected for my day trip.

#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

#(10 points): As a user, I want to display my completed trip in the console.

#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

import random

username = input("Enter your name: ")
print(f'Hello {username}, have you not decided on where you will plan your trip? Do not worry, We will come up with a solution to find the best trip for your stay.')
#Create an introduction for the Day trip generator.

prompt1 = input('Would you like to continue? y/n:')
while prompt1 != 'y':
    print("That's ok, if you decided you still want to continue. Enter y")
    prompt1 = input('Would you like to continue? y/n:')
#Created a while loop to help users to decide if they want to continue the trip or not.

# Random functionality code with while loop to radomly select the place. 
# If user is unsured, it will demostrate the similary while loop as prompt1 shown in line 26. Each list are it's individual variables for it's respective function.
def place_selector(string_list):
    print("Let's select a place for your trip.")
    random_place = random.choice(string_list)
    prompt2 = input(f'Do you like your choice: {random_place}? y/n:')
    while prompt2 != 'y':
        print("Ok, let's help you find another place.")
        random_place = random.choice(string_list)
        prompt2 = input(f'Do you like your choice: {random_place}? y/n:')
    return random_place



def restaurant_selector(string_list):
    print("Let's select a resturant for your trip.")
    random_restaurant = random.choice(string_list)
    prompt3 = input(f'Do you like your choice {random_restaurant}? y/n:')
    while prompt3 != 'y':
        print("Ok, let's help you find another restaurant.")
        random_restaurant = random.choice(string_list)
        prompt3 = input(f'Do you like your choice {random_restaurant}? y/n:')
    return random_restaurant



def transportation_selector(string_list):
    print("Let's select a transportation for your trip. y/n:")
    random_transport = random.choice(string_list)
    prompt4 = input(f'Do you like your choice {random_transport}? y/n:')
    while prompt4 != 'y':
        print("Ok, let's help you find another transportation.")
        random_transport = random.choice(string_list)
        prompt4 = input(f'Do you like your choice {random_transport}? y/n:')
    return random_transport



def entertainment_selector(string_list):
    print("Let's select an entertainment for your trip.")
    random_entertainment = random.choice(string_list)
    prompt5 = input(f'Do you like your choice {random_entertainment}? y/n:')
    while prompt5 != 'y':
        print("Ok, let's you find another form of entertainment.")
        random_entertainment = random.choice(string_list)
        prompt5 = input(f'Do you like your choice {random_entertainment}? y/n:')
    return random_entertainment



def display():
# List for each individual variables
    places = ['Brooklyn', 'Queens', "Bronx", 'Manhattan', 'Staten Island']
    restraurants = ['Mcdonald', 'Burgerking', 'White Castle']
    transportations = ['car', 'tour bus', 'train', "Local bus"]
    entertainment = ['Nightclub', 'Sports Stadium', 'Theaterical entertianment', 'Billards']
    random_place = place_selector(places)
    random_restaurant = restaurant_selector(restraurants)
    random_transportation = transportation_selector(transportations)
    random_entertianment = entertainment_selector(entertainment)
    print('Here is a choices you have selected:')
    print(random_place, '\n' ,random_restaurant, '\n' ,random_transportation, '\n' ,random_entertianment)
display()

confirmation = input('Would you like to confirm your trip? y/n:') 
if confirmation == 'y':
    print('Congratulations, You have completed your desired location for your trip')
else:
    print('That is unfornate, but you can always try again if you change your mind.')

# Note 1; Created individual list for each catergories regarding random function first.
# Note 2; Then edit print functionality with responsive description individually.
# Note 3; Produce if functions for each list functions individually.

# List of lessons learned for this assignment
# Learn how to use random function. (Functions of python in general)
# Learn how to use list.
# Learn how to use if statement.
# Learn how to use a while loop.
# Most importantly, learn how to use print function firsthand.
# This whole assignment is covered by week 1 and 2.