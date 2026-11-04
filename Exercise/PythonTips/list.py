lempty: list = []
print(lempty)
l1 = [1, 2, 3, 4]
l2 = ["d", "w", "i", "g", "h", "t"]
l3 = [None, 3.14, None]
print(l1 + l2 + l3)

n: int = 5
print([False] * n)

# Create a list w/ integer from 0 to 9
# Method 1
l = []
for i in range(10):
    l.append(i)
print(l)

# Method 2
l = [i for i in range(10)]
print(l)

