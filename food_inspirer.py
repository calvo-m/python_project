# imports
import time
import re 

# list of ingredients
breakfast_ingredients = ("oats", "yogurt", "seeds", "flour", "sugar", "fuit", "almond milk",\
    "cinnamon", "yogurt")
lunch_ingredients = ("tofu", "pepper", "soy sauce", "lentils", "coconut milk", "onion", \
     "potatoes", "olive oil")
snacks_ingredients = ("flour", "sugar", "chocolate chips", "potatoes", "olive oil", \
    "bread", "cheese")
#meals (find a way of storing these)
breakfast_meals = {'porridge':['oats','yogurt', 'seeds'], 'pancakes':['flour','sugar', 'almond milk'], \
    'fruit smoothie':['fruit', 'almond milk', 'cinnamon', 'yogurt']}
lunch_meals = {'lentil dhaal':['lentils', 'coconut milk', 'onion'], \
    'stir fry':['tofu', 'pepper', 'onion', 'soy sauce'], \
        'spanish omelette':['potatoes', 'onion','olive oil']}
snacks_meals = {'cookies':['flour', 'sugar', 'chocolate chips'], 'roasted chips':['potatoes', \
     'olive oil'], 'cheese sandwich':['bread', 'cheese']}

# method to check if user input (regardless of cases and spaces) is the same as 
# the string in the data base
def strEquals(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if re.sub('\s+', '', str1.strip()) == re.sub('\s+', '', str2.strip()):
        return True
    else:
        return False

def mainMenu():
    # ask for user input on the meal
    print("Please, select a type of meal by entering the number: \
        \n 1 - breakfast \
        \n 2 - lunch/dinner \
        \n 3 - snacks/desserts \
        \n 4 - I don't need to choose. Exit application.")

    # initialise empty value for the meal
    meal = 0
    # get input number
    control = True
    while control:
        choice = int(input("Your choice: "))
        meal = choice
        if choice == 1 or choice == 2 or choice == 3:
            control = False
            time.sleep(0.3)
            askIngredients(choice)
        elif choice == 4:
            control = False
            print("Exiting application.")
        else:
            print("Error selecting an available choice. Please, try again.")
            control = True


def askIngredients(choice):
    # ask for user input on ingredients
    print("Please, enter the name of the ingredients you have (separated by a comma), \
selecting from the list.")
    time.sleep(0.5)
    if choice == 1:
        print(f"List of ingredients:  {breakfast_ingredients}")
    elif choice == 2:
        print(f"List of ingredients:  {lunch_ingredients}")
    else:
        print(f"List of ingredients:  {snacks_ingredients}")
    user_ingredients = input()
    user_ingredients = user_ingredients.split(",")
    findMeals(choice, user_ingredients)


def findMeals(choice, ingredients):
    time.sleep(0.8)
    if choice == 1:
        mealsFound = iterateMeals(breakfast_meals, ingredients)
    elif choice == 2:
        mealsFound = iterateMeals(lunch_meals, ingredients)
    else:
        mealsFound = iterateMeals(snacks_meals, ingredients)
    output(mealsFound)


def iterateMeals(meal_repo, user_ingr):
    mealsFound = []
    for meal, meal_ingr in meal_repo.items():
        ingredientFound = True
        while ingredientFound:
            # iterate through the ingredients the meal needs
            for ingr in meal_ingr:
                # search for it
                for ingredient in user_ingr:
                    if strEquals(ingredient, ingr):
                        # if the ingredient is found, stop looking for it
                        # stop the "for ingredient in user_ingr"
                        # go to next ingr in meal_ingr
                        break
                    # if we get to the last ingredient of the available ones
                    # and we cannot find the one we need, then it means we 
                    # don't have that ingredient, therefore we should skip
                    # to the next meal
                    if strEquals(ingredient, user_ingr[-1]) and strEquals(ingredient, ingr) == False:
                        ingredientFound =  False
            # if we found all the ingredients needed, break the while loop
            # and go to the next meal
            break    
        # if all ingredients have been found, add this meal to the list
        if ingredientFound !=False:
            mealsFound.append(meal)
    return mealsFound

def output(mealsFound):
    time.sleep(0.8)
    if len(mealsFound) == 0:
        print("Sorry, no meals have been found with the \
ingredients you input. You can try again.")
    else:
        print("These are the meals you can make: ")
        print(mealsFound)
        #print("")
    time.sleep(1.8)
    print(" \nGoing back to main menu.")
    time.sleep(2.5)
    mainMenu()


# start the application
print("This is a tool to help you choose something \
to eat (vegetarian/vegan) based on what you have on your fridge :)")
mainMenu()



