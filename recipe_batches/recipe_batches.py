#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  if 'butter' in ingredients  :
    print("true")
  else:
    ingredients.update({'butter':500000})
  if 'butter' in recipe  :
    print("true")
  else:
    recipe.update({'butter':5000})
    # setattr(ingredients, butter, 0)
  if ingredients['butter'] == 500000 and recipe['butter'] < 5000:
    return 0
  if recipe['butter'] == 5000 and ingredients['butter'] < 5000:
    return 0
  if 'milk' in ingredients  :
    print("true")
  else:
    ingredients.update({'milk':500000})
  if 'milk' in recipe  :
    print("true")
  else:
    recipe.update({'milk':5000})
    # setattr(ingredients, butter, 0)
  if ingredients['milk'] == 500000 and recipe['milk'] < 5000:
    return 0
  if recipe['milk'] == 5000 and ingredients['milk'] < 5000:
    return 0
  if 'cheese' in ingredients  :
    print("true")
  else:
    ingredients.update({'cheese':500000})
  if 'cheese' in recipe  :
    print("true")
  else:
    recipe.update({'cheese':5000})
    # setattr(ingredients, butter, 0)
  if ingredients['cheese'] == 500000 and recipe['cheese'] < 5000:
    return 0
  if recipe['cheese'] == 5000 and ingredients['cheese'] < 5000:
    return 0
  if 'sugar' in ingredients  :
    print("true")
  else:
    ingredients.update({'sugar':500000})
  if 'sugar' in recipe  :
    print("true")
  else:
    recipe.update({'sugar':5000})
    # setattr(ingredients, butter, 0)
  if ingredients['sugar'] == 500000 and recipe['sugar'] < 5000:
    return 0
  if recipe['sugar'] == 5000 and ingredients['sugar'] < 5000:
    return 0
  if 'flour' in ingredients  :
    print("true")
  else:
    ingredients.update({'flour':500000})
  if 'flour' in recipe  :
    print("true")
  else:
    recipe.update({'flour':5000})
    # setattr(ingredients, butter, 0)
  if ingredients['flour'] == 500000 and recipe['flour'] < 5000:
    return 0
  if recipe['flour'] == 5000 and ingredients['flour'] < 5000:
    return 0
  cheese = round(ingredients['cheese'] / recipe['cheese'])
  sugar = round(ingredients['sugar'] / recipe['sugar'])
  flour = round(ingredients['flour'] / recipe['flour'])
  milk = round(ingredients['milk'] / recipe['milk'])
  butter = round(ingredients['butter'] / recipe['butter'])
  array = [cheese,sugar,flour,milk,butter]
  return min(array)
    
    
  
  
  
  
  
print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))