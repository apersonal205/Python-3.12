# Integer variable
age : int = 42

# Float variable
height : float = 5.6

# String variable
name : str = "Tariq Maqbool"

# List variable
family_member : list[str] = ["Tariq", "Rizwan", "Nadeem"]

print (f"{name} is {age} year(s) old and his family members: {family_member}")

print("-----------------")

# Creating a dictionary
my_dict : dict[str, str] = {
    "name": "Tariq Maqbool",
    "age": 42,
    "city": "Muscat"
}

# Accessing values using keys
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# Adding a new key-value pair
my_dict["occupation"] = "Engineer"
print(my_dict)


print("Detail: {{age}} ") # Jinja Style
