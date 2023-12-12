name : str = "Tariq Maqbool"
f_name : str = "Maqbool Hussain"
age : int = 30
print("Result with old style: ")
print("Emp Name: " + name)
print("Father Name: " + f_name)
print("Age: " + str(age))

print("-------------------------")



fstring_result : str = f"""
Emp Name: {name} 
Father Name: {f_name}
Age: {age}
"""
print("Result with f-string: "+ fstring_result)

print("-------------------------")

result_old : str = """
Emp Name: %s 
Father Name: %s 
Age: %d
"""%(name, f_name,age)
print("Result with '%' style: "+ result_old)


fresult : str = """
Emp Name: {0} 
Father Name: {1} 
Age: {2}
""".format(name, f_name,age)
print("Result with formatiing style: "+ fresult)


fref_result : str = """
Emp Name: {a} 
Father Name: {b} 
Age: {c}
""".format(a=name, b=f_name,c=age)
print("Result with Ref formatiing style: "+ fref_result)