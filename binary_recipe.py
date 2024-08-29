def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example list of grocery store ingredients in sorted alphabetical order
ingredients = [
    "apples", "bananas", "carrots", "eggs", "flour", "milk", "prawns", "tomatoes", "yogurt"
]

# Ingredient to search for
target_ingredient = "prawns"

# Perform binary search
result = binary_search(ingredients, target_ingredient)

if result != -1:
    print("Ingredient found at index:", result)
else:
    print("Ingredient not found in the list")