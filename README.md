# python_project

## introduction
This is a small Python application to help the user choose a meal from different vegetarian and vegan options based on the ingredients they currently have at home.
The application will initially display a main menu where the user can choose what type of meal they want to cook: breakfast, lunch or dinner (grouped together since meals tend to be similar and exchangeable), and snacks or desserts. Finally, the user can exit the application by choosing the 4th option in the main menu. 
The meals and ingredients needed for them form part of the python file itself, but could be extended (see "future functionality"), and everything can be run from one single python file from the terminal. 

## implementation/requirements

### Different data types 
The program mainly works with strings (used for the meals, ingredients, etc.), but also booleans (e.g. for control of code blocks, or for giving different outputs). There is limited use of numeric data types: int variables are used for the choices the user makes in the main menu; and float variables used implicitly with the time.sleep command.

### Collections 
The data for ingredients is stored in 3 different lists (for the 3 different meal options) and they are initialised at the beginning of the program. The meals (and their associated ingredients) form key-value pairs of string:list, that are stored in dictionaries, which again are initialised at the beginning of the program.

### Conditionals 
The code includes several if/else statements, to control the flow. Examples of this include: executing different code depending on what option the user has chosen for the meal, giving different output responses whether there are available meals for the user to make or not, and many others like finding out if the user has a needed ingredient for a specific meal.

### Iteration
There are several uses of iteration throughout the code. Mainly going over the ingredients list (needed for meals, and for the user ingredients), with for loops. Use of while is also used for controlling whether an ingredient has been found or not.

### User input
The user needs to choose the type of meal they want by writing into the terminal the number associated to their choice. Any input that is not associated to one of the programmed options will prompt the user to input another number. Additionally, after choosing, they then have to write in the terminal the ingredients they have available (choosing from a list, and in a specific format, i.e. spearated by a comma), so that the program can read it. Any ingredients not included in the given list by the program will not be recognised in the meals' ingredients, therefore they won't cause trouble but they will also not be useful to find a meal related to them.

## flow of code
The program starts by printing the main menu (mainMenu() function) into the terminal, and allowing the user to make a choice. 

1/2/3 - these are all different meal options

4 - this is an option to exit the application

If any of the meal options are chosen, the function askIngredients() is called, giving the meal choice (either breakfast, lunch/dinner, or snacks/desserts), which then prints in the terminal the list of ingredients that the user can choose from, and also asks the user to input any of those ingredients that they currently have. Regardless of whether the user input is approprately formatted or has correct ingredients (as in, they are in the program database), the program will store these in a list (after splitting the input string). The function findMeals() is called, which makes use of the iterateMeals() function: what iterateMeals() does is go through each meal in the dictionary, and try to find its ingredients in the user's ingredients. When the user has all the needed ingredients, it means they can make this meal, and therefore the meal is added to "mealsFound". If one of the ingredients is not found, the for loop is stopped, and it means the meal cannot be made by the user. This process is repeated for all the meals in the dictionary. This functions returns the mealsFound list to findMeals(), which then calls on the output() function. Basically, this is just a final function to print in the terminal the result of the program: whether there are no meals that the user can make with the ingredients they gave, or printing the meals that can be made by the user. Once this is done, the program circles back to the main menu, where the user can make another choice from.
## limitations/future functionality
- Ingredient input by user: the program relies partially on the user writing correctly the ingredients (e.g. not writing "yogurts" instead of "yogurt"). Although upper/lower case is accounted for and won't affect the result, as well as any white spaces (or lack thereof) between ingredients, there are other user variations of the input that may affect how the program is ran. Steps could be taken to solve this, whether it is not allowing the user to write anything else other than the correct ingredients, or possibly creating a menu/checklist in a GUI that the user can choose from. 
- Lack of data in the program: the limited time and resources for the program means that the amount of meals included in the program is very limited. It would make this program much more functional to have a larger database of meals and ingredients. To do this, it might be worth having a database separate from python (which would be outside the scope of this project that needs to be all done in Python), for example an SQL database might be considered, which would also allow to store more information such as ingredient quantities, a recipe, possible substitutions for ingredients, allergens, etc.
- Output: the program gives a list of the possible meals that the user can make. However, it would be nice to have an associated recipe for each meal (eg. from a website) and print it together with the meal name, so that the user can learn how to make it in case they don't know yet.
- Interface: the user experience for this program is very poor. Everything is printed in the terminal, and the user has to write down manually all their ingredients. A GUI pop-up from Python with buttons that the user can press could make things more visually appealing and easier to use. The time.sleep() command was used so that printing in the terminal did not seem cluttered and the user could have some time to read the commands individually, however this could be done much better in a proper graphical interface (outside of the scope of the project).
- Extension to webapp: cloud services could be used to create a webapp to host this program. However, my knowledge is limited in this area, and I cannot give more details about how this could be implemented.
