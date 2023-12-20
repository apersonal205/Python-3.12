import pandas as pd

table = pd.read_html('https://www.w3schools.com/python/python_operators.asp')
print(table[0])


print("---------------------")

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

