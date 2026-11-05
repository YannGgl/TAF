names: list = ["Michael", "Jim", "Dwight"]
# Loop over indices only (+ elements indirectly ?)
for indice in range(len(names)):
    print(f"Index: {indice}, element: {names[indice]}")

# Loop over elements only
for name in names:
    print(f"Element: {name}")

# Loop over indices AND elements
for _, name in enumerate(names):  # enumerate returns couple (index, element)
    # The "_" is a convention to say we don't care
    # about the variable (like for indices for example..)
    print(f"Index: {_}, element: {name}")
print(f"Print enumerate output: {enumerate(names)}")
print(f"Print list of enumerate output: {list(enumerate(names))}")

# Loop 'over' a dictionary:
# The items method
salesman: dict = {"name": "Dwight", "age": 30, "rank": "Regional manager"}
for key, value in salesman.items():
    print(f"key: {key}, value: {value}")

# The 'zip' function
names_men = ["Michael", "Jim", "Dwight"]
names_women = ["Holly", "Pam", "Angela"]
for name_man, name_woman in zip(names_men, names_women):  # Doable on 3 or more iterables !
    print(f"{name_man} and {name_woman} form a couple")

# 'enumerate a zip' combo
for indice, (name_man, name_woman) in enumerate(zip(names_men, names_women)):
    print(f"Couple {indice}: {name_man} and {name_woman}")
