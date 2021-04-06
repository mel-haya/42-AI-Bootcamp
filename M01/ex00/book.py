import datetime
from recipe import Recipe
class Book:
    def __init__(self,name):
        self.name = self._is_valid_name(name)
        self.creation_time = datetime.datetime.now()
        self.last_update = self.creation_time
        self.recipes_list = {
            "starter":[],
            "lunch":[],
            "dessert":[]}

    def _is_valid_name(self, name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string.")
        return name

    def get_recipe_by_name(self, name):
        recipes = self.recipes_list["starter"] +\
        self.recipes_list["lunch"] + self.recipes_list["dessert"]
        for r in recipes:
            if r.name == name:
                print(r)
                return r
    
    def get_recipes_by_types(self, recipe_type):
        for r in self.recipes_list[recipe_type]:
            print(r)

    def add_recipe(self, recipe):
        if not isinstance(recipe,Recipe):
            raise ValueError("Invalid recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()


        