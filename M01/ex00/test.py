from book import Book
from recipe import Recipe
from time import sleep

frite = Recipe(name="btata frite",cooking_lvl=2,cooking_time=45,ingredients=["btata","zit"],recipe_type="lunch")
lhout = Recipe(name="tajine l7out",cooking_lvl=2,cooking_time=45,ingredients=["7out","btata","zit"],recipe_type="lunch")
banana = Recipe(name="banana",cooking_lvl=1,cooking_time=45,ingredients=["banana"],recipe_type="dessert")

#print(recipe)

book = Book("the book")
print(book.last_update.strftime("%X"))
sleep(5)

book.add_recipe(frite)
book.add_recipe(lhout)
book.add_recipe(banana)

book.get_recipes_by_types("dessert")
# book.get_recipe_by_name("btata frite")
print(book.last_update.strftime("%X"))


