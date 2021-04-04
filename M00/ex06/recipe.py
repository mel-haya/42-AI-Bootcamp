import os

cookbook = {
    "sandwich":{
        "ingredients" : ["ham", "bread", "cheese" ,"tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
    },
    "cake":{
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
    },
    "salad":{
        "ingredients" : ["avocado", "arugula", "tomatoes" ,"spinach"],
        "meal" : "lunch",
        "prep_time" : 15
    }
}

def menu():
    os.system('clear')
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = input(">> ")
    if choice == '1':
        menu_add()
    elif choice == '2':
        menu_del()
    elif choice == '3':
        menu_print_one()
    elif choice == '4':
        menu_print_all()
    elif choice == '5' or choice == "quit":
        exit_menu()
    else:
        input("ERROR: invalid input press Enter to continue...")
    menu()
    

def del_rec(name):
    if name in cookbook:
        cookbook.pop(name)
        print("The recipe ",name," was successfully deleted")
    else:
        print("The recipe ",name," is not in the cookbook")
def print_rec(name):
    if name in cookbook:
        print("Recipe for",name,':')
        print("Ingredients list:", cookbook[name]["ingredients"])
        print("To be eaten for", cookbook[name]["meal"],".")
        print("Takes",cookbook[name]["prep_time"],"minutes of cooking.")
    else:
        print("The recipe",name,"is not in the cookbook")
def print_all():
    print("the recipes:")
    for key in cookbook:
        print('- ',key)

def exit_menu():
    print("\nauf wiedersehen !!")
    exit()

def menu_del():
    print("Enter the name of the recipe you want to be deleted:")
    del_rec(input(">> "))
    input("Press Enter to continue...")

def menu_print_one():
    print("Enter the name of the recipe you want to be printed:")
    print_rec(input(">> "))
    input("Press Enter to continue...")

def menu_print_all(): 
    print_all()
    input("Press Enter to continue...")

def menu_add():
    ingredient = ""
    ingredients = list()
    name = input("Enter the name of the recipe\n>> ")
    if name in cookbook:
        print("this recipe name is already used")
        input("Press Enter to continue...")
        return
    print("Enter the ingredients of the recipe and write \"done\" when finished")
    while(ingredient != "done"):
        ingredient = input(">> ")
        ingredients.append(ingredient)
    ingredients.pop()
    meal = input("Enter the type of the recipe\n>> ")
    time = int(input("Enter the preparation time of the recipe\n>> "))
    add_rec(name, ingredients, meal, time)
    input("Press Enter to continue...")


def add_rec(name, ingredients, meal, time):
    cookbook[name] = {}
    cookbook[name]["ingredients"] = ingredients
    cookbook[name]["meal"] = meal
    cookbook[name]["prep_time"] = time
    print("The recipe", name ,"was succesfully added")

menu()
