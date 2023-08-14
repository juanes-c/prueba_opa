class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def maximize_price(items, budget):
    n = len(items)
    
    # Initialize a 2D list to store optimal solutions
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(budget + 1):
            dp[i][j] = dp[i - 1][j]  # Don't take the current item
            
            if j >= items[i - 1].price:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - items[i - 1].price] + items[i - 1].price)

    # Backtrack to find the selected items
    selected_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1].price
        i -= 1

    return selected_items

# Create instances of the Item class (name, price, weight)
items = [Item("Item 1", 3, 5), Item("Item 2", 5, 3), Item("Item 3", 2, 5),Item("Item 4", 8, 1), Item("Item 5", 3, 2)]

budget = 15
selected_items = maximize_price(items, budget)

total_price = sum(item.price for item in selected_items)
print("Selected Items:")
for item in selected_items:
    print(item.name, item.price)
print("Total Price:", total_price)