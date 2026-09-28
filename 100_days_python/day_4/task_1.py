import random

freinds = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# OPTION ONE : 
print(random.choice(freinds))

# OPTION_2

length = len(freinds)

randomIndex = random.randint(0,length-1)

print(freinds[randomIndex])