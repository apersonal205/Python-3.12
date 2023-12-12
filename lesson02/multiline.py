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