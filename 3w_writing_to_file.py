employees_var = open("employees.txt", "a")

print(employees_var.writable())

employees_var.write("Lukasz - Tower Head")

employees_var.close()

employees_var = open("employees.txt", "a")
employees_var.write("\nKelly - HR")
employees_var.close()

employees_var = open("employees.txt", "r")

for for_var in employees_var.readlines():
    print(for_var)

employees_var.close()

employees_var = open("employees1.txt", "w")
employees_var.write("\nKelly - HR")
employees_var.close()

employees_var = open("employees1.txt", "r")

for for_var in employees_var.readlines():
    print(for_var)

employees_var.close()