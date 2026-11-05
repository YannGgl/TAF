# General form : my_dict = {"key1": value1, "key2": value2}

salesman: dict = {"name": "Dwight", "age": 30}
print(salesman)
print(salesman["name"])

salesman["rank"] = "Assistant (to the) regional manager"
print(salesman["rank"], "\n", salesman)
salesman["rank"] = "Regional manager"
print(salesman["rank"], "\n", salesman)

# The item method
key_value_pairs_items = salesman.items()
print(key_value_pairs_items)  # No manipulation as a list
print(list(key_value_pairs_items))  # list() is the constructor of a list
