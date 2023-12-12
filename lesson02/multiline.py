import pandas as pd

emp_detail : str = """
print("My Name is Tariq")
a : int = 7
b : int = 5

print (a + b)
"""
exec(emp_detail)

print("-------------")

a : list[str] = [i for i in dir(str) if "__" not in i]
print (a)
print (len(a))

print("-------------")

table = pd.read_html('https://www.w3schools.com/python/python_operators.asp')
print (table[0])


a, b, c = "Tariq Maqbool", 40, 5.6
print(a)
print(b)
print(c)

print("-----------")

a, *b = "Tariq Maqbool", 40, 5.6
print(a)
print(*b)

print("-----------")

a = "Tariq Maqbool", 40, 5.6
print(a)
print(*a)


n = 15
if (m := n) > 10:
    print(f"{m} is greater than 10")
else:
    print(f"{m} is not greater than 10")
print("-----------")    
    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for item in data:
    if item > 5:
        result.append(item)
print(f"Data List: {data}")
print(f"Greater than 5: {result}")

    
print("-----------")

numbers = [1, 4, 7, 2, 8, 5]
threshold = 5
index = 0

while (current := numbers[index]) < threshold:
    print(f"Processing {current} (index {index})")
    index += 1

print(f"Stopped at {current} (index {index}), as it is greater than or equal to {threshold}")

a : int = 10_000_00
print(f"Long value for understand (10_000_00): {a}")

my_list : list[str] = list("1234567890")
print(my_list) 
print("-----------")

my_list = [10, 20, 30, 40, 50]

# Basic slicing
print(f"Postive --> {my_list[0:3]}")  
print(f"Negative  --> {my_list[-1:-3:-1]}")  

my_list : list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(f"My List :{my_list}")
print(f"Pop (remove) Index 1: {my_list.pop(2)}")
print(f"My List (Updated) :{my_list}")
my_list.append("3")
print(f"My List (Updated) :{my_list}")
my_list.insert(2,"3")
my_list.pop(10)
print(f"My List (Updated) :{my_list}")