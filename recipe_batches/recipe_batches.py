#!/usr/bin/python
def recipe_batches(recipe, ingredients):
  # make a new dictionary for comparing key value pairs
  new_ingredients = {}  
  for i in recipe:
    # includes 0 as value for missing ingredients
    if i not in ingredients:
      new_ingredients[i] = 0
    else:
      # update values in new dictionary with rest of ingredients values
      new_ingredients[i] = ingredients[i]
  
  import math
  # track largest possible # of batches
  most = math.inf
  # if missing an ingredient return 0 possible batches
  if 0 in new_ingredients.values():
    return 0
  else:
    # find the greatest common ingredient denominator
    batches = [new_ingredients[i]//recipe[i] for i in recipe]
    for j in batches:
      # update most with greatest
      if j < most:
        most = j
    return most
recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 })

  
  

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5, 'sugar': 10}
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

  
  