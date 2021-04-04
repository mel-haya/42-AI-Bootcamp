cookbook = {
    "sandwich":{
        "ingredients" : ["ham", "bread", "cheese" ,"tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
    },
    "cake":{
        "ingredients" : ("flour", "sugar", "eggs"),
        "meal" : "dessert",
        "prep_time" : 60
    },
    "salad":{
        "ingredients" : ("avocado", "arugula", "tomatoes" ,"spinach"),
        "meal" : "lunch",
        "prep_time" : 15
    }
}


def menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

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
        print("The recipe ",name," is not in the cookbook")
def print_all():
    for key in cookbook:
        print_rec(key)
        print("---------------------------------------")

def add_rec(name, ingredients, meal, time):
    cookbook[name] = {}
    cookbook[name]["ingredients"] = ingredients
    cookbook[name]["meal"] = meal
    cookbook[name]["prep_time"] = time

