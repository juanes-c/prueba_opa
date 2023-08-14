class Item:
    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight
        self.calories = calories

def maximize_calories_within_weight(items, weight_limit, min_calories):
    n = len(items)
    
    dp = [0] * (weight_limit + 1)
    
    for i in range(n):
        for j in range(weight_limit, items[i].weight - 1, -1):
            print(j)
            print('*****',dp[j - items[i].weight])
            dp[j] = max(dp[j], dp[j - items[i].weight] + items[i].calories)

    max_calories = dp[weight_limit]
    print(dp)

    selected_items = []
    j = weight_limit
    for i in range(n - 1, -1, -1):
        while j >= items[i].weight and dp[j] == dp[j - items[i].weight] + items[i].calories:
            selected_items.append(items[i])
            print(items[i], i)
            j -= items[i].weight
    print(selected_items)
    return selected_items, max_calories

# Create instances of the Item class (name, price, weight, calories)
items = [Item("Item 1", 5, 3), Item("Item 2", 3, 5), Item("Item 3", 5, 2),Item("Item 4", 1, 8), Item("Item 5", 2, 3)]

weight_limit = 10
min_calories_requirement = 17

selected_items, max_calories = maximize_calories_within_weight(items, weight_limit, min_calories_requirement)
print(selected_items)
#total_price = sum(item.price for item in selected_items)
total_weight = sum(item.weight for item in selected_items)

print("Selected Items:")
for item in selected_items:
    print(f"{item.name} , Weight: {item.weight}, Calories: {item.calories}")

print("Total Weight:", total_weight)
print("Maximized Calories:", max_calories)
