a : int = 10_000_00
print(f"Long value for understand (10_000_00): {a}")

my_list : list[str] = list("1234567890")
print(my_list) 
print("-----------")

my_list = [10, 20, 30, 40, 50]

# Basic slicing
print(f"Postive --> {my_list[0:3]}")  
print(f"Negative  --> {my_list[-1:-3:-1]}")  