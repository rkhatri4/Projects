a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b**2) - (4*a*c)

root1 = (-b + d**0.5) / (2*a)

root2 = (-b - d**0.5) / (2*a)


print("The roots of the quadratic equation are", root1, "and", root2)