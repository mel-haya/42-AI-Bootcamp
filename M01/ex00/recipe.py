class Recipe:  

    def __init__(self, name, cooking_lvl,cooking_time,recipe_type,ingredients = [],description=None):
        self.name = self._is_valid_name(name)
        self.cooking_lvl = self._is_valid_cooking_lvl(cooking_lvl)
        self.cooking_time = self._is_valid_cooking_time(cooking_time)
        self.ingredients = self._is_valid_ingredients(ingredients)
        self.description = description
        self.recipe_type = self._is_valid_recipe_type(recipe_type)
    def __str__(self):
        i = 0
        txt = "\n"
        txt += "Recipe :" + self.name + "\n"
        txt += "------\n"
        txt += "difficulty : "
        while i < self.cooking_lvl:
            txt += "⭐"
            i+=1
        txt += " | 🕐 Cooking time : " + str(self.cooking_time) + "min\n"
        txt += "------------\n"
        txt += "Ingredients:\n"
        txt += "------------\n"
        for ingredient in self.ingredients:
            txt += "  ✨" + ingredient + "\n"
        txt += "this recipe is a " + self.recipe_type
        if self.description:
            txt += "\ndescription:\n" + self.description
        return txt

    def _is_valid_name(self, name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string.")
        return name

    def _is_valid_cooking_time(self, cooking_time):
        if not isinstance(cooking_time,int) or cooking_time <= 0:
            raise ValueError("Cooking time must be an positive integer")
        return cooking_time

    def _is_valid_cooking_lvl(self, cooking_lvl):
        if not isinstance(cooking_lvl,int) or cooking_lvl <= 0 or cooking_lvl > 5:
            raise ValueError("Cooking level must be an integer between 1 and 5 .")
        return cooking_lvl
    
    def _is_valid_ingredients(self, ingredients):
        for i in ingredients:
            if not isinstance(i,str):
                raise ValueError("the ingredients must be strings.")
        return ingredients

    def _is_valid_recipe_type(self, recipe_type):
        types = ("starter" , "lunch" , "dessert")
        if recipe_type not in types:
            raise ValueError("Recipe type must be a starter , a lunch or a dessert.")
        return recipe_type
    

