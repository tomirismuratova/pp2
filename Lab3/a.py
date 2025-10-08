fruits = [
    {"name": "apple", "cost": 500},
    {"name": "pineapple", "cost": 600},
    {"name": "peach", "cost": 300},
]

def func(fruits):
    costs = [fruit["cost"] for fruit in fruits]
    return sorted(costs)

print(func(fruits))
