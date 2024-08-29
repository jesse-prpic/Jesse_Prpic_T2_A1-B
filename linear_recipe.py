def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example list of grocery store ingredients unsorted
ingredients = [
    "apples", "milk", "carrots", "eggs", "prawns", "tomatoes", "yogurt", "bananas", "flour",
]

# Ingredient to search for
target_ingredient = "prawns"

# Perform linear search
result = linear_search(ingredients, target_ingredient)

if result != -1:
    print("Ingredient found at index:", result)
else:
    print("Ingredient not found in the list")